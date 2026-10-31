using System;
using System.Collections.Generic;
using System.Linq;

namespace CareerExperience
{
    [Serializable] public class PilotPackage { public int schema_version; public float transitionSeconds; public PilotDefinition[] careers; }
    [Serializable] public class PilotDefinition
    {
        public string scenarioId,version,occupationId,name,roomId,title,brief,limitation;
        public PilotObject[] objects;
        public PilotObject photoSubject;
        public PilotSurface[] surfaces;
        public string requestChangeBrief,requestChangeReasonCode;
        public PilotSurface[] alternateSurfaces;
    }
    [Serializable] public class PilotObject
    {
        public string id,name,candidateId,assetId,assetVersion,instanceId,nodeName;
    }
    [Serializable] public class PilotSurface
    {
        public string id,objectId,kind,title,instruction,successText,workItemId;
        public PilotTile[] tiles;
        public PilotValue[] values;
        public PilotField[] fields;
        public PilotFinding[] findings;
        public float timerMin,timerMax,timerLimit;
        public string timerUnit;
    }
    [Serializable] public class PilotTile
    {
        public string id,label,targetLabel,slotLabel;
        public float initialX,initialY,targetX,targetY,tolerance=.065f;
        public float width=.13f,height=.12f;
    }
    [Serializable] public class PilotValue
    {
        public string id,label,unit;
        public float min,max,initial,target,tolerance;
    }
    [Serializable] public class PilotField { public string id,label,initial,target; }
    [Serializable] public class PilotFinding { public string id,label,detail; }
    public sealed class PilotDraft
    {
        public float[] x,y,values;
        public string[] fields;
        public bool[] observed;
        public bool completed,running;
        public string artifactId,artifactName;
        public int artifactWidth,artifactHeight,artifactBytes;
        public string[] validationErrors=Array.Empty<string>();
        public float elapsed;
        public int generation;
        public int editRevision,savedRevision,savedRequestRevision;
        public PilotDraft(PilotSurface definition,int generation)
        {
            x=(definition.tiles??Array.Empty<PilotTile>()).Select(t=>t.initialX).ToArray();
            y=(definition.tiles??Array.Empty<PilotTile>()).Select(t=>t.initialY).ToArray();
            values=(definition.values??Array.Empty<PilotValue>()).Select(t=>t.initial).ToArray();
            fields=(definition.fields??Array.Empty<PilotField>()).Select(t=>t.initial??"").ToArray();
            observed=new bool[(definition.findings??Array.Empty<PilotFinding>()).Length];
            this.generation=generation;
        }
    }
    // Pure workflow state. UI, transport and career data are separate consumers.
    // Editing is not a submission; only Submit/StartTimer/StopTimer create attempts.
    public sealed class PilotSession
    {
        public readonly PilotDefinition Definition;
        public PilotSurface[] Surfaces { get; private set; }
        public bool HasRequestChange=>Definition.alternateSurfaces!=null&&Definition.alternateSurfaces.Length==Definition.surfaces.Length;
        public int RequestRevision { get; private set; }
        public bool RequestChanged=>HasRequestChange&&RequestRevision>1;
        public PilotDraft[] Drafts { get; private set; }
        public string RunId { get; private set; }
        public int Generation { get; private set; }
        public bool Paused,Ended,WorkStarted,GuidanceUsed;
        public double ActiveMs { get; private set; }
        public double[] WorkActiveMs { get; private set; }
        public int ActiveSurface=-1;
        public int CurrentStep => Array.FindIndex(Drafts,d=>!d.completed);
        public bool Complete => Drafts.All(d=>d.completed);
        public Action<PilotTransition> Transition;
        public PilotSession(PilotDefinition definition) { Definition=definition; NewRun(); }
        public void NewRun()
        {
            Generation++;RunId="run-"+Guid.NewGuid().ToString("N");
            Surfaces=Definition.surfaces;RequestRevision=HasRequestChange?1:0;
            Drafts=Surfaces.Select(s=>new PilotDraft(s,Generation)).ToArray();
            Paused=Ended=WorkStarted=GuidanceUsed=false;ActiveMs=0;WorkActiveMs=new double[Drafts.Length];ActiveSurface=-1;
        }
        public bool Editable(int step) => !Ended&&!Paused&&step>=0&&step<Drafts.Length&&!Drafts[step].completed&&!Drafts[step].running;
        public bool Unlocked(int step) => step==0||step>0&&Drafts.Take(step).All(d=>d.completed);
        public void Edit(int step,Action<PilotDraft> edit)
        {
            if(!Editable(step)||!Unlocked(step))return;
            edit(Drafts[step]);WorkStarted=true;
            Drafts[step].editRevision++;
        }
        public bool Observe(int step,int finding)
        {
            if(!Editable(step)||!Unlocked(step)||finding<0||finding>=Drafts[step].observed.Length)return false;
            if(Drafts[step].observed[finding])return false;
            Drafts[step].observed[finding]=true;Drafts[step].editRevision++;WorkStarted=true;return true;
        }
        public string[] Validate(int step)
        {
            if(step<0||step>=Drafts.Length)return new[]{"UNKNOWN_WORK_SURFACE"};
            var surface=Surfaces[step];var draft=Drafts[step];var errors=new List<string>();
            if(!Unlocked(step))errors.Add("PREREQUISITE_NOT_COMPLETE");
            if(HasRequestChange&&step>0&&Drafts.Take(step).Any(d=>d.savedRequestRevision!=RequestRevision))errors.Add("REQUEST_REVISION_STALE");
            for(int i=0;i<draft.x.Length;i++)
            {
                var tile=surface.tiles[i];
                if(Math.Abs(draft.x[i]-tile.targetX)>tile.tolerance||Math.Abs(draft.y[i]-tile.targetY)>tile.tolerance)errors.Add("PLACEMENT_MISMATCH_"+tile.id.ToUpperInvariant());
            }
            for(int i=0;i<draft.values.Length;i++)if(Math.Abs(draft.values[i]-surface.values[i].target)>surface.values[i].tolerance)errors.Add("SETTING_MISMATCH_"+surface.values[i].id.ToUpperInvariant());
            for(int i=0;i<draft.fields.Length;i++)if((draft.fields[i]??"").Trim()!=surface.fields[i].target)errors.Add("FIELD_MISMATCH_"+surface.fields[i].id.ToUpperInvariant());
            if(draft.observed.Any(v=>!v))errors.Add("INSPECTION_INCOMPLETE");
            if(surface.kind=="photo"&&string.IsNullOrEmpty(draft.artifactId))errors.Add("CAPTURE_REQUIRED");
            return errors.ToArray();
        }
        public bool Submit(int step)
        {
            if(!Editable(step))return false;
            WorkStarted=true;var reasons=Validate(step);
            if(reasons.Length>1)reasons=reasons.Where(r=>r!="CAPTURE_REQUIRED").ToArray();
            return Resolve(step,reasons,Surfaces[step].kind=="photo"?"capture_photo":"submit");
        }
        bool Resolve(int step,string[] reasons,string action)
        {
            Drafts[step].validationErrors=reasons;bool ok=reasons.Length==0;
            if(ok){Drafts[step].completed=true;Drafts[step].savedRevision=Drafts[step].editRevision;Drafts[step].savedRequestRevision=RequestRevision;}
            Transition?.Invoke(new PilotTransition{step=step,action=action,success=ok,reasons=reasons,runId=RunId,generation=Generation});
            return ok;
        }
        public bool StartTimer(int step)
        {
            if(!Editable(step)||!Unlocked(step)||Surfaces[step].kind!="timer")return false;
            WorkStarted=true;string[] reasons=Validate(step);
            if(reasons.Length>0)return Resolve(step,reasons,"start_timer");
            Drafts[step].validationErrors=Array.Empty<string>();Drafts[step].running=true;Drafts[step].elapsed=0;Drafts[step].generation=Generation;
            Transition?.Invoke(new PilotTransition{step=step,action="start_timer",success=true,pending=true,reasons=Array.Empty<string>(),runId=RunId,generation=Generation});return true;
        }
        public bool StopTimer(int step)
        {
            if(Ended||Paused||step<0||step>=Drafts.Length||!Drafts[step].running||Drafts[step].generation!=Generation)return false;
            Drafts[step].running=false;var s=Surfaces[step];float time=Drafts[step].elapsed;
            return Resolve(step,time>=s.timerMin&&time<=s.timerMax?Array.Empty<string>():new[]{"TIMING_OUTSIDE_WINDOW"},"stop_timer");
        }
        public void Tick(float seconds,bool roomVisible,bool focused)
        {
            if(Ended||Paused||Complete||!roomVisible||!focused)return;
            ActiveMs+=Math.Max(0,seconds)*1000.0;
            for(int i=0;i<Drafts.Length;i++)if(i==ActiveSurface||Drafts[i].running)WorkActiveMs[i]+=Math.Max(0,seconds)*1000.0;
            for(int i=0;i<Drafts.Length;i++)
            {
                var d=Drafts[i];if(!d.running||d.generation!=Generation)continue;
                d.elapsed+=Math.Max(0,seconds);var surface=Surfaces[i];
                if(d.elapsed>surface.timerLimit){d.running=false;Resolve(i,new[]{"PROCESS_TIMEOUT"},"timer_timeout");}
            }
        }
        public void End()
        {
            if(Ended)return;Ended=true;
            foreach(var draft in Drafts)draft.running=false;
            Generation++; // Invalidates every old timer/gesture generation.
        }
        public bool ChangeRequest()
        {
            if(!HasRequestChange||RequestChanged||Ended||Paused||Complete)return false;
            // Full replacement data keeps the same three physical objects and
            // work-item identities. Drafts survive; prior confirmations expire.
            Surfaces=Definition.alternateSurfaces;RequestRevision++;Generation++;
            foreach(var draft in Drafts)
            {
                draft.completed=draft.running=false;draft.savedRevision=draft.savedRequestRevision=0;
                draft.generation=Generation;draft.validationErrors=Array.Empty<string>();draft.elapsed=0;
                Array.Clear(draft.observed,0,draft.observed.Length);
            }
            return true;
        }
    }
    public sealed class PilotTransition
    {
        public int step,generation;public string action,runId;public bool success,pending;public string[] reasons;
    }
}

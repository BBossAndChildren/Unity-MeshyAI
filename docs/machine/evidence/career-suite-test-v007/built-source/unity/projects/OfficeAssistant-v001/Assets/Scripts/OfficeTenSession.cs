using System;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text;

namespace CareerExperience
{
    [Serializable] public sealed class OfficeTenCatalog { public int schema_version; public OfficeTenData[] scenarios; }
    [Serializable] public sealed class OfficeTenData
    {
        public string scenario_id, version, occupation_id, name, title, request, help;
        public OfficeTenStep[] steps;
    }
    [Serializable] public sealed class OfficeTenStep
    {
        public string step_id, object_id, work_item_id, title, instruction, kind, receipt_label;
        public OfficeTenField[] fields;
        public OfficeTenItem[] items;
        public string[] destinations;
        public float seconds;
    }
    [Serializable] public sealed class OfficeTenField { public string id, label, initial, expected; }
    [Serializable] public sealed class OfficeTenItem { public string id, label, target; }
    [Serializable] public sealed class OfficeTenSnapshot
    {
        public int stepIndex, requestRevision, documentRevision, run;
        public bool complete, paused, busy;
        public string state, message;
    }
    // Business state and predicates are independent of rendering and protocol transport.
    public sealed class OfficeTenSession
    {
        public readonly OfficeTenData Data;
        public int StepIndex { get; private set; }
        public int RequestRevision { get; private set; }
        public int DocumentRevision { get; private set; }
        public int Run { get; private set; }
        public bool Paused { get; private set; }
        public bool Busy { get; private set; }
        public bool Complete => StepIndex >= Data.steps.Length;
        public string Message { get; private set; }
        public string[] CurrentReasons { get; private set; } = Array.Empty<string>();
        public OfficeTenStep CurrentStep => Data.steps[Math.Min(StepIndex, Data.steps.Length - 1)];
        public readonly List<string> CompletedStepIds = new List<string>();
        public readonly List<Dictionary<string,object>> Results = new List<Dictionary<string,object>>();
        public float Progress => Busy ? Math.Min(1, elapsed / Math.Max(.05f, CurrentStep.seconds)) : StepIndex > 1 ? 1 : 0;
        float elapsed;
        Dictionary<string,object> pending;
        public OfficeTenSession(OfficeTenData data)
        {
            if(data==null||data.steps==null||data.steps.Length!=3)throw new ArgumentException("Exactly three object-bound steps are required.");
            if(data.steps.Select(x=>x.object_id).Distinct().Count()!=3)throw new ArgumentException("Each of the three physical objects has one work surface.");
            Data=data; Reset(false);
        }
        public void Reset(bool changed)
        {
            Run++;StepIndex=0;RequestRevision=1;DocumentRevision=0;Paused=Busy=false;elapsed=0;pending=null;
            CompletedStepIds.Clear();Results.Clear();CurrentReasons=Array.Empty<string>();Message=Data.request;
        }
        public void TogglePause(){Paused=!Paused;Message=Paused?"일시정지 — 작업 진행과 출력 시간을 멈췄습니다.":"작업을 계속합니다.";}
        static string Normal(string value)=>(value??"").Normalize(NormalizationForm.FormC).Trim();
        static bool Same(string actual,string expected)
        {
            actual=Normal(actual);expected=Normal(expected);
            if(decimal.TryParse(actual.Replace(",",""),NumberStyles.Number,CultureInfo.InvariantCulture,out decimal a)&&decimal.TryParse(expected.Replace(",",""),NumberStyles.Number,CultureInfo.InvariantCulture,out decimal b))return a==b;
            return actual==expected;
        }
        static string Code(string value)=>new string((value??"VALUE").ToUpperInvariant().Select(c=>char.IsLetterOrDigit(c)?c:'_').ToArray());
        public bool TryPlace(int stepIndex,int itemIndex,string destination)
        {
            CurrentReasons=Array.Empty<string>();
            if(Paused||Busy||Complete||stepIndex!=StepIndex)return false;
            var items=CurrentStep.items??Array.Empty<OfficeTenItem>();
            if(itemIndex<0||itemIndex>=items.Length)return false;
            if(destination!=items[itemIndex].target){CurrentReasons=new[]{"CLASSIFICATION_MISMATCH_"+Code(items[itemIndex].id)};Message="분류 위치가 다릅니다. "+items[itemIndex].label+"의 요청을 다시 확인하세요. 원래 위치로 되돌렸습니다.";return false;}
            Message="배치 확인: "+items[itemIndex].label+" → "+destination+". 남은 내용과 인계를 확인하세요.";return true;
        }
        public bool Submit(int stepIndex,string[] values,string[] placements)
        {
            CurrentReasons=Array.Empty<string>();
            if(Paused||Busy||Complete){Message=Paused?"계속하기를 선택하세요.":Busy?"진행 중입니다. 중복 실행하지 않습니다.":"이미 인계가 완료됐습니다.";return false;}
            if(stepIndex!=StepIndex){CurrentReasons=new[]{"SEQUENCE_VIOLATION"};Message="현재 업무를 먼저 완료하세요: "+CurrentStep.title;return false;}
            var step=CurrentStep;var fields=step.fields??Array.Empty<OfficeTenField>();var items=step.items??Array.Empty<OfficeTenItem>();var errors=new List<string>();var labels=new List<string>();
            for(int i=0;i<fields.Length;i++)if(values==null||i>=values.Length||!Same(values[i],fields[i].expected)){errors.Add("FIELD_MISMATCH_"+Code(fields[i].id));labels.Add(fields[i].label);}
            for(int i=0;i<items.Length;i++)if(placements==null||i>=placements.Length||placements[i]!=items[i].target){errors.Add("CLASSIFICATION_MISMATCH_"+Code(items[i].id));labels.Add(items[i].label);}
            if(errors.Count>0){CurrentReasons=errors.ToArray();Message="확인할 항목: "+string.Join(" · ",labels)+". 요청 원문과 비교해 수정하세요. 입력과 배치는 유지했습니다.";return false;}
            if(StepIndex==0)DocumentRevision++;
            pending=new Dictionary<string,object>{{"stepId",step.step_id},{"objectId",step.object_id},{"workItemId",step.work_item_id},{"values",(values??Array.Empty<string>()).ToArray()},{"placements",(placements??Array.Empty<string>()).ToArray()},{"documentRevision",DocumentRevision},{"receipt",step.receipt_label}};
            if(step.seconds>0){Busy=true;elapsed=0;Message="출력 중 — 설정과 중복 제출을 잠갔습니다.";}
            else Commit();
            return true;
        }
        void Commit()
        {
            var step=CurrentStep;Results.Add(pending);pending=null;CompletedStepIds.Add(step.step_id);StepIndex++;Busy=false;elapsed=0;
            Message=Complete?"처리 결과와 보관 위치를 인계했습니다.":step.receipt_label+" · 다음 업무: "+CurrentStep.title;
        }
        public void Tick(float delta)
        {
            if(!Busy||Paused||delta<=0)return;elapsed+=delta;if(elapsed>=Math.Max(.05f,CurrentStep.seconds))Commit();
        }
        public object Partial()=>new Dictionary<string,object>{{"scenarioId",Data.scenario_id},{"completedStepIds",CompletedStepIds.ToArray()},{"completedResults",Results.ToArray()},{"handoffConfirmed",Complete},{"inFlightStepId",Busy?CurrentStep.step_id:null},{"printProgress",Busy?(object)Progress:null}};
        public OfficeTenSnapshot Snapshot()=>new OfficeTenSnapshot{stepIndex=StepIndex,requestRevision=RequestRevision,documentRevision=DocumentRevision,run=Run,complete=Complete,paused=Paused,busy=Busy,state=Complete?"complete":Busy?"processing":"step_"+StepIndex,message=Message};
    }
}

using System;
using System.Collections;
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Runtime.InteropServices;
using System.Text;
using UnityEngine;

namespace CareerExperience
{
    // Generic workflow ledger: the selected fixed scenario provides business
    // data; the session owns validation and this module owns event counting.
    [DefaultExecutionOrder(-1000)]
    public sealed class OfficeTenProtocol : MonoBehaviour
    {
        public string buildId = "office-ten-v001";
        public const string Room = "PAN-001";
        static OfficeTenProtocol instance;
        public static OfficeTenProtocol Existing=>instance;
        public static bool HasActiveExperience=>instance!=null&&instance.RunId!=null&&!instance.Ended&&!(instance.standalone&&!instance.WorkStarted);
        public bool HasRequestedExperience=>!standalone&&RunId!=null;
        public OfficeTenSession Session { get; private set; }
        public OfficeTenData SelectedData => Session == null ? null : Session.Data;
        public string ScenarioId => SelectedData == null ? null : SelectedData.scenario_id;
        public string ScenarioVersion => SelectedData == null ? null : SelectedData.version;
        public bool Ended { get; private set; }
        public bool WorkStarted { get; private set; }
        public bool CanSelectScenario => Session == null || Ended || !WorkStarted;
        public string SelectionMessage { get; private set; }
        public string RunId { get; private set; }
        public string ExperienceId { get; private set; }
        public string EndSummary { get; private set; }
        OfficeTenExperience view;
        string sessionId, currentRoom = Room, lastObject, lastStep, endedEventId;
        bool focused = true, standalone = true, scenarioComplete;
        double activeMs, checkpointAt;
        Entry inFlight;
        readonly Dictionary<string, double> interactionMs = new Dictionary<string, double>();
        readonly List<Entry> entries = new List<Entry>();
        readonly List<Dictionary<string, object>> previousRuns = new List<Dictionary<string, object>>();
        readonly Dictionary<string, string> responses = new Dictionary<string, string>();
        readonly Dictionary<string, string> requests = new Dictionary<string, string>();
        readonly HashSet<string> usedExperiences = new HashSet<string>();
        Control pendingStart;
        [DllImport("__Internal")] static extern void CareerPublish(string json);
        [DllImport("__Internal")] static extern void CareerCheckpoint(string json);
        [Serializable] class Control { public int schemaVersion; public string protocol,requestId,action,sessionId,experienceId,roomId,scenarioId,scenarioVersion,reason; }
        sealed class Entry
        {
            public string id,run,session,experience,type,obj,step,item,attempt,failure,key;
            public string[] reasons = Array.Empty<string>();
            public int revision; public long sequence;
            public bool submitted,retry,repeated,assistance;
            public Dictionary<string, object> envelope; public string json;
        }
        static string Id(string prefix) => prefix + Guid.NewGuid().ToString("N");
        static Dictionary<string, object> D(params object[] values) { var d=new Dictionary<string,object>();for(int i=0;i<values.Length;i+=2)d.Add((string)values[i],values[i+1]);return d; }
        public static OfficeTenProtocol Get()
        {
            // Prefer the serialized scene instance: its buildId is assigned by
            // the actual builder. Never replace it with a default-version object
            // merely because the view happened to request the bridge first.
            if(instance==null)instance=FindFirstObjectByType<OfficeTenProtocol>();
            if(instance==null)instance=new GameObject("OfficeTenProtocol").AddComponent<OfficeTenProtocol>();
            return instance;
        }
        void Awake()
        {
            if(instance!=null&&instance!=this){Destroy(gameObject);return;}
            instance=this;gameObject.name="OfficeTenProtocol";DontDestroyOnLoad(gameObject);
            buildId=CareerSuiteMode.BuildId(buildId);
            sessionId=Id("session-");ExperienceId=Id("experience-");
        }
        void OnDestroy(){if(instance==this)instance=null;}
        void Update()
        {
            if(Session!=null&&view!=null&&currentRoom==Room&&focused&&!Session.Paused&&!Ended&&!scenarioComplete)
            {
                double delta=Time.unscaledDeltaTime*1000;activeMs+=delta;
                string obj=view.CurrentObject;var step=StepForObject(obj);
                if(step!=null){string key=ScopeKey(obj,step.step_id);interactionMs[key]=(interactionMs.TryGetValue(key,out double ms)?ms:0)+delta;}
            }
            if(Session!=null&&Time.unscaledTimeAsDouble-checkpointAt>=1){checkpointAt=Time.unscaledTimeAsDouble;PublishCheckpoint();}
        }
        public OfficeTenSession Attach(OfficeTenData data,OfficeTenExperience controller)
        {
            view=controller;currentRoom=Room;
            if(Session==null){Session=new OfficeTenSession(data);if(!CareerSuiteMode.Managed)StartRun(null);}
            if(pendingStart!=null){var request=pendingStart;pendingStart=null;StartExternal(request,FindData(request.scenarioId,request.scenarioVersion));}
            if(RunId!=null)Emit("scene.entered","enter_room",null,null,D("roomId",Room,"scenarioAvailable",true));
            return Session;
        }
        public OfficeTenSession SelectScenario(OfficeTenData data,OfficeTenExperience controller)
        {
            SelectionMessage=null;
            if(data==null){SelectionMessage="체험 데이터를 찾지 못했습니다.";return Session;}
            if(!CanSelectScenario){SelectionMessage="현재 체험을 종료한 후 다른 직업을 선택하세요.";return Session;}
            if(Session!=null&&!Ended)Finish("USER_REQUESTED_END",Id("request-select-"));
            view=controller;Session=new OfficeTenSession(data);ExperienceId=Id("experience-");
            standalone=true;Ended=false;endedEventId=null;previousRuns.Clear();StartRun(null);
            return Session;
        }
        public void Detach(OfficeTenExperience controller){if(view==controller)view=null;}
        public void OnRoomChanged(string roomId)
        {
            if(currentRoom==roomId)return;
            if(Session!=null&&RunId!=null)Emit("scene.exited","leave_room",null,null,D("fromRoomId",currentRoom,"toRoomId",roomId));
            currentRoom=roomId;
        }
        public void RoomChanged(string roomId)=>OnRoomChanged(roomId);
        IEnumerable<Entry> CurrentEntries=>entries.Where(e=>e.run==RunId);
        OfficeTenStep StepAt(int index)=>Session==null||index<0||index>=Session.Data.steps.Length?null:Session.Data.steps[index];
        OfficeTenStep StepForObject(string obj)=>Session==null||obj==null?null:Session.Data.steps.FirstOrDefault(s=>s.object_id==obj);
        static string ScopeKey(string obj,string step)=>obj+"|"+step;
        void StartRun(string requestId)
        {
            usedExperiences.Add(ExperienceId);RunId=Id("run-");activeMs=0;interactionMs.Clear();WorkStarted=false;
            scenarioComplete=false;lastObject=lastStep=null;inFlight=null;EndSummary=null;
            Emit("scenario.started","start_scenario",null,null,D("selectedScenarioId",ScenarioId));
            if(requestId!=null){Entry started=Emit("experience.started","start_experience",null,null,D("ready",true),requestId:requestId);responses[requestId]=started.json;}
            PublishCheckpoint();
        }
        public void Open(string obj)
        {
            if(Ended)return;var step=StepForObject(obj);if(step==null)return;
            int index=Array.IndexOf(Session.Data.steps,step);
            int previous=Array.FindIndex(Session.Data.steps,s=>s.step_id==lastStep);
            if(previous>=0&&index<previous)Emit("workflow.backtracked","recheck_previous_work",obj,step,D("fromStepId",lastStep,"toStepId",step.step_id,"reasonCode","USER_RECHECK"));
            lastObject=obj;lastStep=step.step_id;
            Emit("object.selected","select_object",obj,null,D());
            Emit("interaction.opened","open_work_surface",obj,step,D("readOnly",Session.Complete||index<Session.StepIndex));
        }
        public void Close(string obj)
        {
            if(Ended)return;var step=StepForObject(obj);if(step==null)return;
            Emit("interaction.closed","close_work_surface",obj,step,D("draftPreserved",true));
            Emit("navigation.back","return_to_room",obj,step,D("reasonCode","NORMAL_RETURN"));
        }
        public void Pause(bool paused){if(!Ended&&RunId!=null)Emit(paused?"scenario.paused":"scenario.resumed",paused?"pause":"resume",null,null,D());}
        public void SetFocus(bool value){focused=value;}
        public void Progress(string control,string value,string obj)
        {
            if(Session==null||Ended||Session.Paused||Session.Complete)return;var step=StepForObject(obj);if(step==null)return;
            WorkStarted=true;lastObject=obj;lastStep=step.step_id;
            Emit("interaction.progress","edit_field",obj,step,D("controlId",control,"value",value,"draft",true));
        }
        public string RequestHelp()
        {
            if(Ended)return "종료된 체험입니다.";if(Session.Complete)return "이미 인계가 완료됐습니다.";var step=Session.CurrentStep;
            Emit("guidance.requested","request_help",view==null?null:view.CurrentObject,step,D());
            string help=Session.Data.help;
            Emit("guidance.presented","show_help",view==null?null:view.CurrentObject,step,D("isAssistance",true,"reasonCode","USER_REQUESTED_HINT","text",help),assistance:true);return help;
        }
        public void Action(string action,string obj,OfficeTenSnapshot before,OfficeTenSnapshot after,bool ok,bool attempt,string subItemId=null)
        {
            if(Session==null||Ended||before.complete||before.paused||before.busy)return;
            var step=StepForObject(obj)??StepAt(before.stepIndex);if(step==null)return;
            string attemptId=attempt?Id("attempt-"):null,key=step.step_id+"|"+obj+"|"+step.work_item_id+"|"+before.requestRevision+"|"+action+"|"+(subItemId??"");
            Entry preceding=CurrentEntries.LastOrDefault(e=>e.key==key&&(e.submitted||e.failure!=null));
            bool retry=attempt&&preceding!=null&&preceding.failure!=null;
            WorkStarted=true;lastObject=obj;lastStep=step.step_id;
            if(retry)Emit("interaction.retry_requested",action,obj,step,D("reasonCode","RESUBMIT_AFTER_FAILED_ATTEMPT"),attemptId:attemptId,revision:before.requestRevision);
            Entry started=Emit("interaction.started",action,obj,step,D("isAttempt",attempt,"isRetry",retry,"subItemId",subItemId,"input",view==null?null:view.ActualInput(action)),attemptId:attemptId,submitted:attempt,retry:retry,key:key,revision:before.requestRevision);
            if(!ok)
            {
                string[] reasons=Session.CurrentReasons??Array.Empty<string>();if(reasons.Length==0)reasons=new[]{"SEQUENCE_VIOLATION"};
                string failure=Id("failure-");
                // Repetition is defined by the protocol's fixed business context,
                // independently of the UI command/sub-item retry key.
                bool repeated=CurrentEntries.Any(e=>e.failure!=null
                    &&e.step==step.step_id&&e.obj==obj&&e.item==step.work_item_id
                    &&e.revision==before.requestRevision&&e.reasons.Intersect(reasons).Any());
                var data=D("failureId",failure,"reasonCodes",reasons,"faultSource","player","expected",Expected(step),"actual",view==null?null:view.ActualInput(action));
                Emit("interaction.validation_failed",action,obj,step,data,attemptId:attemptId,failure:failure,reasons:reasons,repeated:repeated,key:key,revision:before.requestRevision);
                Emit("interaction.failed",action,obj,step,data,"failed","VALIDATION_FAILED",attemptId:attemptId,failure:failure,reasons:reasons,repeated:repeated,key:key,revision:before.requestRevision);return;
            }
            if(after.busy){inFlight=started;Emit("interaction.progress",action,obj,step,D("jobId",attemptId,"inFlight",true,"completed",false),attemptId:attemptId);}
            else if(after.stepIndex>before.stepIndex||after.complete)
            {
                Emit("interaction.completed",action,obj,step,D("visualResult",Session.Partial()),"completed","WORK_STEP_COMPLETED",attemptId:attemptId);CheckCompleted();
            }
            else Emit("interaction.progress",action,obj,step,D("accepted",true,"intermediateAction",true,"subItemId",subItemId,"input",view==null?null:view.ActualInput(action)),attemptId:attemptId);
        }
        object Expected(OfficeTenStep step)=>D("fields",step.fields==null?Array.Empty<object>():step.fields.Select(f=>(object)D("id",f.id,"expected",f.expected)).ToArray(),"placements",step.items==null?Array.Empty<object>():step.items.Select(i=>(object)D("id",i.id,"target",i.target)).ToArray());
        public void WorkCompleted()
        {
            if(Session==null||Ended||inFlight==null||Session.Busy)return;var started=inFlight;inFlight=null;
            var step=Session.Data.steps.First(s=>s.step_id==started.step);
            Emit("interaction.completed","complete_async_work",started.obj,step,D("jobId",started.attempt,"visualResult",Session.Partial()),"completed","WORK_STEP_COMPLETED",attemptId:started.attempt);CheckCompleted();
        }
        void CheckCompleted()
        {
            if(!Session.Complete||scenarioComplete||Ended)return;scenarioComplete=true;
            Emit("scenario.completed","complete_scenario",null,null,D("finalResult",Session.Partial()),"completed","OFFICE_WORKFLOW_COMPLETED");
        }
        Dictionary<string,object> Process(string scope,string obj=null,OfficeTenStep step=null)
        {
            var selected=CurrentEntries.Where(e=>scope=="scenario"||step!=null&&e.obj==obj&&e.step==step.step_id&&e.item==step.work_item_id).ToArray();
            double ms=scope=="scenario"?activeMs:step!=null&&interactionMs.TryGetValue(ScopeKey(obj,step.step_id),out double t)?t:0;
            return D("scope",scope,"measurementStatus","complete","measurementNote",null,"attemptCount",selected.Count(e=>e.submitted),"navigationBackCount",selected.Count(e=>e.type=="navigation.back"),"backtrackCount",selected.Count(e=>e.type=="workflow.backtracked"),"retryCount",selected.Count(e=>e.submitted&&e.retry),"mistakeCount",selected.Where(e=>e.failure!=null).Select(e=>e.failure).Distinct().Count(),"repeatedMistakeCount",selected.Where(e=>e.failure!=null&&e.repeated).Select(e=>e.failure).Distinct().Count(),"helpRequestCount",selected.Count(e=>e.type=="guidance.requested"),"guidanceUsed",selected.Any(e=>e.assistance),"elapsedActiveMs",(long)Math.Round(ms));
        }
        Dictionary<string,object> Result(string outcome,string code)=>D("outcome",outcome,"success",outcome=="pending"?(object)null:outcome=="completed","completionCode",code,"data",outcome=="pending"?D():outcome=="aborted"?D("partialResults",Session.Partial()):Session.Partial());
        Dictionary<string,object> Context(string outcome,Dictionary<string,object> process,IEnumerable<Entry> evidence,Dictionary<string,object> termination=null)
        {
            var ev=evidence.ToArray();bool terminal=outcome!="pending";
            string assessment=!terminal?null:outcome!="completed"?"TASK_INCOMPLETE":(int)process["repeatedMistakeCount"]>0?"TASK_REPEATED_ERRORS":(bool)process["guidanceUsed"]?"TASK_GUIDED_COMPLETED":(int)process["mistakeCount"]>0?"TASK_SELF_CORRECTED":"TASK_SMOOTH";
            return D("assessmentStatus",terminal?"evaluated":"pending","assessmentCode",assessment,"ruleVersion","v001","reasonCodes",ev.SelectMany(x=>x.reasons).Concat(termination==null?Array.Empty<string>():new[]{(string)termination["code"]}).Distinct().ToArray(),"evidenceEventIds",ev.Select(x=>x.id).ToArray(),"interpretation",terminal?outcome=="completed"?"선택한 가상 직업 업무의 완료 조건을 충족했습니다. 과정은 원본 이벤트에서 집계했습니다.":"종료 직전까지 완료한 부분과 남은 업무를 보존했습니다. 종료는 업무 실수가 아닙니다.":null,"limitations",new[]{"가상 업무 사례이며 직업 적성·개인의 전반적 능력 진단이 아님","새로고침·통신 단절에서는 마지막 전달이 보장되지 않음"},"termination",termination);
        }
        Entry Emit(string type,string action,string obj,OfficeTenStep step,Dictionary<string,object> data,string outcome="pending",string code=null,string requestId=null,string attemptId=null,bool submitted=false,bool retry=false,string failure=null,string[] reasons=null,bool repeated=false,string key=null,int? revision=null,Dictionary<string,object> termination=null,bool assistance=false)
        {
            var e=new Entry{id=Id("evt-"),run=RunId,session=sessionId,experience=ExperienceId,type=type,obj=obj,step=step==null?null:step.step_id,item=step==null?null:step.work_item_id,attempt=attemptId,failure=failure,key=key,reasons=reasons??Array.Empty<string>(),revision=revision??Session.RequestRevision,sequence=CareerProtocol.NextSequence(sessionId),submitted=submitted,retry=retry,repeated=repeated,assistance=assistance};
            entries.Add(e);bool interaction=step!=null&&obj!=null&&!type.StartsWith("workflow.");var scope=interaction?"interaction":"scenario";var process=Process(scope,obj,step);
            string asset=obj=="monitor"?"AST-005":obj=="copier"?"AST-009":obj=="cabinet"?"AST-015":null;
            var evidence=CurrentEntries.Where(x=>!interaction||x.obj==obj&&x.step==step.step_id&&x.item==step.work_item_id).ToArray();
            e.envelope=D("schemaVersion",1,"protocol","career-experience","eventId",e.id,"sequence",e.sequence,"occurredAt",DateTimeOffset.Now.ToString("o"),"sessionId",sessionId,"scenarioRunId",RunId,"buildId",buildId,"sceneId",Room,"roomId",Room,"experienceId",ExperienceId,"requestId",requestId,"scenarioId",ScenarioId,"scenarioVersion",ScenarioVersion,"objectId",obj,"instanceId",asset==null?null:asset+"-0","assetId",asset,"assetVersion",asset==null?null:"v001","stepId",e.step,"workItemId",e.item,"attemptId",attemptId,"requestRevision",e.revision,"documentRevision",Session.DocumentRevision,"type",type,"action",action,"process",process,"result",Result(outcome,code),"context",Context(outcome,process,evidence,termination),"data",data);
            // A terminal event must never list itself as supporting evidence.
            ((Dictionary<string,object>)e.envelope["context"])["evidenceEventIds"]=evidence.Where(x=>x!=e).Select(x=>x.id).ToArray();
            e.json=Json(e.envelope);Publish(e.json);return e;
        }
        Dictionary<string,object> Termination(string code,string id)=>D("terminationId",id,"code",code,"initiatedBy","user","workStarted",WorkStarted,"lastStepId",lastStep,"lastObjectId",lastObject,"lastState",Session.Snapshot().state,"completedStepIds",Session.CompletedStepIds.ToArray(),"remainingStepIds",Session.Data.steps.Select(s=>s.step_id).Except(Session.CompletedStepIds).ToArray(),"inFlightActionIds",inFlight==null?Array.Empty<string>():new[]{inFlight.attempt});
        Entry AbortRun(string code)
        {
            var termination=Termination(code,Id("termination-"));
            if(WorkStarted&&lastObject!=null){var step=Session.Data.steps.FirstOrDefault(s=>s.step_id==lastStep);if(step!=null&&!Session.CompletedStepIds.Contains(step.step_id))Emit("interaction.aborted","quit_work",lastObject,step,D(),"aborted",code,termination:termination);}
            return Emit("scenario.aborted","quit_scenario",null,null,D(),"aborted",code,termination:termination);
        }
        public void EndFromUser(){if(!Ended&&Session!=null)Finish("USER_REQUESTED_END",Id("request-user-"));}
        void Finish(string reason,string requestId)
        {
            bool complete=Session.Complete;Ended=true;if(view!=null)view.EndUi();
            string code=complete?"OFFICE_WORKFLOW_COMPLETED":WorkStarted?"USER_ABORTED":"USER_EXITED_BEFORE_START";
            Entry aborted=complete?null:AbortRun(code);
            var data=D("previousRuns",previousRuns.ToArray(),"events",entries.Where(x=>x.experience==ExperienceId).Select(x=>x.envelope).ToArray(),"eventsComplete",true);
            var ended=Emit("experience.ended","end_experience",null,null,data,complete?"completed":"aborted",code,requestId:requestId,termination:aborted==null?null:(Dictionary<string,object>)((Dictionary<string,object>)aborted.envelope["context"])["termination"]);
            responses[requestId]=ended.json;endedEventId=ended.id;inFlight=null;EndSummary="체험 종료: "+code;PublishCheckpoint();
        }
        public void ResetRun(bool changed)
        {
            if(Session==null)return;
            if(Ended){ExperienceId=Id("experience-");previousRuns.Clear();standalone=true;Ended=false;endedEventId=null;}
            else
            {
                var terminal=scenarioComplete?CurrentEntries.LastOrDefault(x=>x.type=="scenario.completed"):AbortRun("USER_RESET");if(terminal!=null)previousRuns.Add(terminal.envelope);
                Emit("scenario.reset","reset_scenario",null,null,D("reasonCode","USER_RESET","previousScenarioRunId",RunId));
            }
            inFlight=null;Session.Reset(changed);StartRun(null);
        }
        public void ReceiveControl(string json)
        {
            Control c;try{c=JsonUtility.FromJson<Control>(json);}catch{ControlError(null,"INVALID_JSON","Control must be JSON.");return;}
            if(c==null||c.schemaVersion!=1||c.protocol!="career-experience"||string.IsNullOrEmpty(c.requestId)||string.IsNullOrEmpty(c.sessionId)||string.IsNullOrEmpty(c.experienceId)||string.IsNullOrEmpty(c.roomId)){ControlError(c,"INVALID_CONTROL","Required fields are missing.");return;}
            string normalized=JsonUtility.ToJson(c);
            if(requests.TryGetValue(c.requestId,out string prior))
            {
                if(prior!=normalized){ControlError(c,"REQUEST_ID_REUSED","Same requestId has different input.",false);return;}
                if(responses.TryGetValue(c.requestId,out string receipt))Publish(receipt);return;
            }
            requests[c.requestId]=normalized;
            if(c.action=="start_experience")
            {
                var data=FindData(c.scenarioId,c.scenarioVersion);
                if(c.roomId!=Room||data==null){ControlError(c,"UNSUPPORTED_SCENARIO","Select a registered office-ten scenario and version in PAN-001.");return;}
                if(usedExperiences.Contains(c.experienceId)){ControlError(c,"EXPERIENCE_ID_REUSED","Use a new experienceId.");return;}
                if(pendingStart!=null||PilotRuntime.HasLiveExperience||!CareerProtocol.Get().CanStartAnother||Session!=null&&!Ended&&!(standalone&&!WorkStarted)){ControlError(c,"EXPERIENCE_ACTIVE","End the current experience first.");return;}
                if(view==null)
                {
                    var explorer=FindFirstObjectByType<WorkplaceExplorer>();
                    if(explorer==null){ControlError(c,"ROOM_LOADER_UNAVAILABLE","Office-ten room loader is unavailable.");return;}
                    pendingStart=c;explorer.SelectSceneForExperience(CareerSuiteMode.TenScene);return;
                }
                StartExternal(c,data);view.BeginExternalRun();
            }
            else if(c.action=="end_experience")
            {
                if(c.reason!="USER_REQUESTED_END"){ControlError(c,"INVALID_REASON","Explicit end requires USER_REQUESTED_END.");return;}
                if(Session==null||c.sessionId!=sessionId||c.experienceId!=ExperienceId||c.roomId!=Room){ControlError(c,"EXPERIENCE_MISMATCH","The requested experience is not current.");return;}
                if(Ended){ControlError(c,"ALREADY_ENDED","Original eventId "+endedEventId);return;}
                Finish(c.reason,c.requestId);
            }
            else ControlError(c,"UNKNOWN_ACTION","Only start_experience and end_experience are supported.");
        }
        OfficeTenData FindData(string id,string version)
        {
            var resource=view!=null&&view.scenarios!=null?view.scenarios:Resources.Load<TextAsset>("office-ten-scenarios");
            if(resource==null)return null;
            var catalog=JsonUtility.FromJson<OfficeTenCatalog>(resource.text);
            return catalog.scenarios.FirstOrDefault(s=>s.scenario_id==id&&s.version==version);
        }
        void StartExternal(Control c,OfficeTenData data)
        {
            sessionId=c.sessionId;ExperienceId=c.experienceId;standalone=false;Ended=false;endedEventId=null;previousRuns.Clear();
            Session=new OfficeTenSession(data);StartRun(c.requestId);
        }
        public static bool Handles(string action,string scenarioId,string experienceId)
        {
            if(action=="end_experience")return instance!=null&&instance.usedExperiences.Contains(experienceId??"");
            if(action!="start_experience")return false;
            var resource=Resources.Load<TextAsset>("office-ten-scenarios");
            return resource!=null&&JsonUtility.FromJson<OfficeTenCatalog>(resource.text).scenarios.Any(s=>s.scenario_id==scenarioId);
        }
        void ControlError(Control c,string code,string message,bool cache=true)
        {
            string json=Json(D("schemaVersion",1,"protocol","career-experience","requestId",c?.requestId,"sessionId",c?.sessionId,"experienceId",c?.experienceId,"roomId",c?.roomId,"type","experience.error","error",D("code",code,"message",message)));
            if(cache&&c?.requestId!=null)responses[c.requestId]=json;Publish(json);
        }
        public void Replay(string unused){foreach(var e in entries.Where(x=>x.session==sessionId).OrderBy(x=>x.sequence))Publish(e.json);}
        void PublishCheckpoint()
        {
            if(Session==null)return;
            string json=Json(D("schemaVersion",1,"protocol","career-experience","sessionId",sessionId,"experienceId",ExperienceId,"scenarioRunId",RunId,"roomId",Room,"scenarioId",ScenarioId,"scenarioVersion",ScenarioVersion,"ended",Ended,"state",Session.Snapshot().state,"lastStepId",lastStep,"lastObjectId",lastObject,"process",Process("scenario"),"partialResults",Session.Partial(),"workStarted",WorkStarted,"deliveryStatus","checkpoint_only_not_terminal","checkedAt",DateTimeOffset.Now.ToString("o")));
#if UNITY_WEBGL && !UNITY_EDITOR
            CareerCheckpoint(json);
#endif
        }
        static void Publish(string json)
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            CareerPublish(json);
#else
            Debug.Log("CAREER_EVENT "+json);
#endif
        }
        static string Json(object value)
        {
            if(value==null)return "null";if(value is string s)return "\""+Escape(s)+"\"";if(value is bool b)return b?"true":"false";
            if(value is IDictionary<string,object> d)return "{"+string.Join(",",d.Select(p=>Json(p.Key)+":"+Json(p.Value)))+"}";
            if(value is IEnumerable list){var items=new List<string>();foreach(var item in list)items.Add(Json(item));return "["+string.Join(",",items)+"]";}
            return Convert.ToString(value,CultureInfo.InvariantCulture);
        }
        static string Escape(string value)
        {
            var s=new StringBuilder();foreach(char c in value){if(c=='\\')s.Append("\\\\");else if(c=='"')s.Append("\\\"");else if(c=='\n')s.Append("\\n");else if(c=='\r')s.Append("\\r");else if(c=='\t')s.Append("\\t");else if(c<32)s.Append("\\u"+((int)c).ToString("x4"));else s.Append(c);}return s.ToString();
        }
    }
}

using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace CareerExperience
{
    // Career-specific task data and pure workflow rules live outside this view.
    // The view operates original scene objects; it never clones/recolors meshes.
    public sealed class PilotRuntime : MonoBehaviour
    {
        public static PilotRuntime Instance { get; private set; }
        public static bool HasLiveExperience=>Instance!=null&&Instance.ledger!=null&&!Instance.ledger.Session.Ended;
        public static bool InputCaptured=>Instance!=null&&HasLiveExperience&&(Instance.panel>=0||Instance.transition||Instance.ledger.Session.Paused);
        PilotPackage package;
        WorkplaceRegistry registry;
        WorkplaceExplorer explorer;
        PilotLedger ledger;
        Font font;
        string roomId,feedback="",buildId;
        Camera cameraView;
        int panel=-1,selectedTile=-1;
        bool transition,returning,reducedMotion,focused=true,tracking,dragged,dragTile,resetDialog,endDialog,submitHeld,clearFocus;
        Vector2 pointerStart;
        float transitionTime,checkpointTime,diagnosticTime,photoTime;
        PilotPhoto photo;bool showHint;
        Vector3 savedPosition,fromPosition,toPosition;
        Quaternion savedRotation,fromRotation,toRotation;
        float savedFov,fromFov,toFov;
        Rect savedRect,fromRect,toRect;
        Renderer[] renderers=Array.Empty<Renderer>();bool[] visibility=Array.Empty<bool>();
        readonly Dictionary<string,PilotLedger> receiptsByExperience=new Dictionary<string,PilotLedger>();
        readonly Dictionary<string,string> controls=new Dictionary<string,string>(),receipts=new Dictionary<string,string>();
        readonly List<string> keyboardControls=new List<string>();
        readonly List<object> uiDiagnostics=new List<object>();
        GUIStyle body,heading,button,input,small;
        Texture2D buttonBackground,buttonHover,buttonActive;
        Matrix4x4 matrix;
        Rect board=new Rect(830,285,550,295);
        string focusedControl="",dragRun;
        Vector2 dragStart;
        int dragStep,dragGeneration;
        bool cancelGuiGesture,tileMoved,placementArmed;
        Vector2 tilePointerStart,tileGrabOffset;
        string browserFocusedControl="",pendingBrowserFocus="",pendingGuiFocus="";
        [Serializable] sealed class BrowserField { public string name,label,value;public float x,y,width,height,clipX,clipY,clipWidth,clipHeight;public bool enabled; }
        [Serializable] sealed class BrowserFrame { public string target="CareerPilot",callback="OnBrowserTextInput",context;public int screenWidth,screenHeight;public float fontSize;public BrowserField[] fields; }
        [Serializable] sealed class BrowserEdit { public string context,name,value,kind,reason;public bool composing,backward,windowFocused; }
        readonly List<BrowserField> browserFields=new List<BrowserField>();
        string BrowserContext=>ledger==null?"idle":ledger.Session.RunId+"|"+ledger.Session.Generation+"|"+panel+"|"+ledger.Session.RequestRevision+"|"+ledger.Session.Paused+"|"+ledger.Session.Ended;
#if UNITY_WEBGL && !UNITY_EDITOR
        [DllImport("__Internal")]static extern void OfficeTenTextInputSync(string json);
        [DllImport("__Internal")]static extern void OfficeTenTextInputFocus(string name);
        [DllImport("__Internal")]static extern void OfficeTenTextInputDispose();
#endif
        Control pendingReady;bool started,navigating;
        [Serializable] class Control { public int schemaVersion;public string protocol,requestId,action,sessionId,experienceId,roomId,scenarioId,scenarioVersion,reason; }
        [DllImport("__Internal")] static extern void PublishPilotState(string json);
        public static PilotRuntime Get(WorkplaceExplorer owner,Font koreanFont)
        {
            if(Instance==null)Instance=new GameObject("CareerPilot").AddComponent<PilotRuntime>();
            Instance.explorer=owner;Instance.font=koreanFont;return Instance;
        }
        void Awake()
        {
            if(Instance!=null&&Instance!=this){Destroy(gameObject);return;}
            Instance=this;DontDestroyOnLoad(gameObject);
#if UNITY_WEBGL && !UNITY_EDITOR
            WebGLInput.captureAllKeyboardInput=false;
#endif
            var data=Resources.Load<TextAsset>("career-pilot-content");
            package=data==null?new PilotPackage{careers=Array.Empty<PilotDefinition>()}:JsonUtility.FromJson<PilotPackage>(data.text);
            foreach(string resource in new[]{"career-expansion-content","career-room-expansion-content","career-room-a-content","career-room-b-content","career-room-c-content","career-additional-a-content","career-additional-b-content","career-additional-c-content","career-next-content"})
            {
                var expansion=Resources.Load<TextAsset>(resource);if(expansion==null)continue;
                var additional=JsonUtility.FromJson<PilotPackage>(expansion.text);
                package.careers=(package.careers??Array.Empty<PilotDefinition>()).Concat(additional.careers??Array.Empty<PilotDefinition>()).ToArray();
            }
            package.careers=package.careers.GroupBy(d=>d.roomId+"|"+d.scenarioId+"|"+d.version).Select(g=>g.First()).ToArray();
            registry=JsonUtility.FromJson<WorkplaceRegistry>(Resources.Load<TextAsset>("workplace-registry").text);buildId=CareerSuiteMode.BuildId(registry.buildId);
            SceneManager.sceneLoaded+=Loaded;Loaded(SceneManager.GetActiveScene(),LoadSceneMode.Single);
        }
        void OnDestroy(){photo?.Dispose();if(buttonBackground!=null)Destroy(buttonBackground);if(buttonHover!=null)Destroy(buttonHover);if(buttonActive!=null)Destroy(buttonActive);if(Instance==this){SceneManager.sceneLoaded-=Loaded;Instance=null;}}
        void Loaded(Scene scene,LoadSceneMode mode)
        {
            navigating=false;roomId=Array.Find(registry.rooms,r=>r.scenePath==scene.path)?.roomId;
            if(roomId==null&&CareerSuiteMode.IsOfficeScene(scene.path))roomId="PAN-001";
            cameraView=Camera.main;
            tracking=dragTile=transition=false;panel=selectedTile=-1;
            if(ledger!=null&&!ledger.Session.Ended){if(!started&&roomId==ledger.Session.Definition.roomId)ConfirmReady();else if(started)ledger.Scene(roomId,true);}
        }
        public void BeforeRoomChange(){if(ledger!=null&&!ledger.Session.Ended&&started)ledger.Scene(roomId,false);navigating=true;tracking=dragTile=false;}
        public bool BlocksOfficeNavigation(string requestedRoom)=>HasLiveExperience&&requestedRoom=="PAN-001"&&ledger.Session.Definition.roomId!="PAN-001";
        public bool TryControl(string json)
        {
            Control c;try{c=JsonUtility.FromJson<Control>(json);}catch{return false;}
            bool pilotStart=c!=null&&c.action=="start_experience"&&package.careers.Any(x=>x.scenarioId==c.scenarioId);
            bool pilotEnd=c!=null&&c.action=="end_experience"&&(receiptsByExperience.ContainsKey(c.experienceId??"")||HasLiveExperience);
            if(!pilotStart&&!pilotEnd&&!(c!=null&&controls.ContainsKey(c.requestId??"")))
            {
                if(c!=null&&c.action=="start_experience"&&HasLiveExperience){Error(c,"EXPERIENCE_ACTIVE","진행 중인 체험을 종료한 뒤 시작하세요.");return true;}return false;
            }
            if(c.schemaVersion!=1||c.protocol!="career-experience"||string.IsNullOrEmpty(c.requestId)||string.IsNullOrEmpty(c.sessionId)||string.IsNullOrEmpty(c.experienceId)||string.IsNullOrEmpty(c.roomId)){Error(c,"INVALID_CONTROL","필수 제어 필드가 없습니다.");return true;}
            string normalized=JsonUtility.ToJson(c);
            if(controls.TryGetValue(c.requestId,out string prior))
            {
                if(prior!=normalized)Error(c,"REQUEST_ID_REUSED","같은 requestId의 내용이 달라졌습니다.");
                else if(receipts.TryGetValue(c.requestId,out string response))PilotLedger.Publish(response);
                return true;
            }
            controls[c.requestId]=normalized;
            if(pilotStart)
            {
                var definition=package.careers.FirstOrDefault(x=>x.scenarioId==c.scenarioId&&x.version==c.scenarioVersion&&x.roomId==c.roomId);
                if(definition==null){Error(c,"UNSUPPORTED_SCENARIO","직업의 고정 방·시나리오 버전을 확인하세요.");return true;}
                string issue=DefinitionIssue(definition);
                if(issue!=null){Error(c,"SCENARIO_DATA_INCOMPLETE",issue);return true;}
                if(HasLiveExperience||!CareerProtocol.Get().CanStartAnother||OfficeTenProtocol.HasActiveExperience){Error(c,"EXPERIENCE_ACTIVE","진행 중인 체험을 종료한 뒤 시작하세요.");return true;}
                if(receiptsByExperience.ContainsKey(c.experienceId)||CareerProtocol.ExperienceWasUsed(c.sessionId,c.experienceId)){Error(c,"EXPERIENCE_ID_REUSED","새 체험에는 새 experienceId가 필요합니다.");return true;}
                if(!CareerProtocol.TryClaimExperience(c.sessionId,c.experienceId,"pilot")){Error(c,"EXPERIENCE_ACTIVE","다른 체험 시작 또는 실행이 진행 중입니다.");return true;}
                Begin(definition,c.sessionId,c.experienceId,c.requestId);
            }
            else
            {
                if(c.reason!="USER_REQUESTED_END"){Error(c,"INVALID_REASON","명시적 종료 이유가 필요합니다.");return true;}
                if(!receiptsByExperience.TryGetValue(c.experienceId,out var requested)||c.sessionId!=requested.SessionId||c.roomId!=requested.Session.Definition.roomId){Error(c,"EXPERIENCE_MISMATCH","현재 실행과 요청이 다릅니다.");return true;}
                if(requested.Session.Ended){Error(c,"ALREADY_ENDED","이미 종료 응답을 보존한 체험입니다. original eventId "+requested.EndEventId);return true;}
                if(requested!=ledger){Error(c,"EXPERIENCE_MISMATCH","현재 실행과 요청이 다릅니다.");return true;}
                RestoreImmediately();receipts[c.requestId]=ledger.End(c.requestId);
            }
            return true;
        }
        void Error(Control c,string code,string message)
        {
            string json=PilotLedger.Json(PilotLedger.D("schemaVersion",1,"protocol","career-experience","requestId",c?.requestId,"sessionId",c?.sessionId,"experienceId",c?.experienceId,"roomId",c?.roomId,"type","experience.error","error",PilotLedger.D("code",code,"message",message)));
            if(c?.requestId!=null&&!receipts.ContainsKey(c.requestId))receipts[c.requestId]=json;PilotLedger.Publish(json);
        }
        void Begin(PilotDefinition definition,string session,string experience,string request)
        {
            RestoreImmediately();photo?.Dispose();photo=null;showHint=false;ledger=new PilotLedger(definition,buildId,session,experience,CareerProtocol.NextSequence);receiptsByExperience[experience]=ledger;
            ledger.Session.Transition+=t=>{feedback=t.pending?"작업이 진행 중입니다.":t.success?ledger.Session.Surfaces[t.step].successText:FailureText(t.step,t.reasons);};
            started=false;pendingReady=request==null?null:JsonUtility.FromJson<Control>(controls[request]);
            feedback="3D 물건을 선택해 업무를 시작하세요.";panel=selectedTile=-1;
            if(roomId!=definition.roomId||CareerSuiteMode.IsOfficeScene(SceneManager.GetActiveScene().path))explorer.SelectRoom(definition.roomId);else ConfirmReady();
        }
        static string DefinitionIssue(PilotDefinition definition)
        {
            if(definition.objects==null||definition.objects.Length!=3||definition.surfaces==null||definition.surfaces.Length!=3)return "정확히 세 물건과 세 업무 화면이 필요합니다.";
            if(definition.objects.Select(o=>o.id).Distinct().Count()!=3||definition.objects.Select(o=>o.nodeName).Distinct().Count()!=3)return "물건 ID와 실제 장면 연결은 서로 달라야 합니다.";
            for(int i=0;i<3;i++)
            {
                var surface=definition.surfaces[i];
                if(surface.objectId!=definition.objects[i].id)return "업무 화면과 물건 연결이 일치하지 않습니다.";
                if(string.IsNullOrEmpty(definition.objects[i].nodeName))return "실제 장면 물건 연결이 없습니다.";
                if(surface.kind=="timer")
                {
                    if(surface.timerMin<0||surface.timerMax<surface.timerMin||surface.timerLimit<=surface.timerMax)return "타이머의 목표 시간과 제한 시간이 유효하지 않습니다.";
                }
                else if((surface.tiles??Array.Empty<PilotTile>()).Length==0&&(surface.fields??Array.Empty<PilotField>()).Length==0&&(surface.values??Array.Empty<PilotValue>()).Length==0&&(surface.findings??Array.Empty<PilotFinding>()).Length==0)return "직접 조작할 업무 자료가 없습니다.";
            }
            if(definition.alternateSurfaces!=null&&definition.alternateSurfaces.Length>0)
            {
                if(definition.alternateSurfaces.Length!=3)return "변경 요청의 업무 화면이 누락됐습니다.";
                for(int i=0;i<3;i++)
                {
                    var a=definition.surfaces[i];var b=definition.alternateSurfaces[i];
                    if(a.id!=b.id||a.objectId!=b.objectId||a.kind!=b.kind||(a.tiles?.Length??0)!=(b.tiles?.Length??0)||(a.fields?.Length??0)!=(b.fields?.Length??0)||(a.values?.Length??0)!=(b.values?.Length??0)||(a.findings?.Length??0)!=(b.findings?.Length??0))return "변경 요청은 같은 물건·업무·입력 구조를 사용해야 합니다.";
                }
            }
            return null;
        }
        string FailureText(int step,string[] reasons)
        {
            var surface=ledger.Session.Surfaces[step];var labels=new List<string>();
            foreach(string code in reasons){foreach(var t in surface.tiles??Array.Empty<PilotTile>())if(code=="PLACEMENT_MISMATCH_"+t.id.ToUpperInvariant())labels.Add(t.label+" 위치");foreach(var v in surface.values??Array.Empty<PilotValue>())if(code=="SETTING_MISMATCH_"+v.id.ToUpperInvariant())labels.Add(v.label+" 설정");foreach(var f in surface.fields??Array.Empty<PilotField>())if(code=="FIELD_MISMATCH_"+f.id.ToUpperInvariant())labels.Add(f.label+" 입력");if(code=="INSPECTION_INCOMPLETE")labels.Add("아직 확인하지 않은 정보");if(code=="TIMING_OUTSIDE_WINDOW"||code=="PROCESS_TIMEOUT")labels.Add("정지 시점(목표 "+surface.timerMin+"~"+surface.timerMax+" 가상 초)");if(code=="CAPTURE_REQUIRED")labels.Add("사진 촬영");if(code=="PREREQUISITE_NOT_COMPLETE")labels.Add("앞 단계 완료");}
            return "다시 확인: "+string.Join(", ",labels.Distinct())+". 초안은 유지됩니다.";
        }
        void ConfirmReady()
        {
            if(started||ledger==null||ledger.Session.Ended)return;
            bool bound=ledger.Session.Definition.objects.All(o=>FindObjectsByType<Transform>(FindObjectsSortMode.None).Any(t=>t.name==o.nodeName&&t.GetComponentsInChildren<Renderer>().Length>0&&t.GetComponentsInChildren<Collider>().Length>0));
            if(!bound){if(pendingReady!=null)Error(pendingReady,"MODEL_BINDING_UNAVAILABLE","조작 물건의 실제 메시·콜라이더 연결을 확인하지 못했습니다.");feedback="물건 연결을 확인하지 못했습니다.";ledger.Session.End();CareerProtocol.ReleaseUnstartedExperience(ledger.SessionId,ledger.ExperienceId);pendingReady=null;return;}
            started=true;ledger.Start(pendingReady?.requestId);ledger.Scene(roomId,true);
            if(pendingReady!=null)receipts[pendingReady.requestId]=ledger.StartReceipt;pendingReady=null;
        }
        public void Replay(){foreach(var record in receiptsByExperience.Values)record.Replay();}
        void Styles()
        {
            if(body!=null)return;
            body=new GUIStyle(GUI.skin.label){font=font,fontSize=20,wordWrap=true};body.normal.textColor=Color.white;
            heading=new GUIStyle(body){fontSize=27,fontStyle=FontStyle.Bold};small=new GUIStyle(body){fontSize=16};
            buttonBackground=UiTexture(new Color(.075f,.19f,.21f));buttonHover=UiTexture(new Color(.11f,.31f,.33f));buttonActive=UiTexture(new Color(.16f,.40f,.41f));
            button=new GUIStyle(GUI.skin.button){font=font,fontSize=18,wordWrap=true,padding=new RectOffset(12,12,8,8),border=new RectOffset(),alignment=TextAnchor.MiddleCenter};
            foreach(var state in new[]{button.normal,button.onNormal}){state.background=buttonBackground;state.textColor=Color.white;}
            foreach(var state in new[]{button.hover,button.focused,button.onHover,button.onFocused}){state.background=buttonHover;state.textColor=Color.white;}
            foreach(var state in new[]{button.active,button.onActive}){state.background=buttonActive;state.textColor=Color.white;}
            input=new GUIStyle(GUI.skin.textField){font=font,fontSize=21};input.normal.textColor=input.focused.textColor=Color.black;
            foreach(var state in new[]{input.normal,input.focused,input.hover,input.active,input.onNormal,input.onFocused,input.onHover,input.onActive}){state.background=Texture2D.whiteTexture;state.textColor=new Color(.08f,.1f,.12f);}
            input.padding=new RectOffset(10,10,8,8);
        }
        static Texture2D UiTexture(Color color)
        {
            var texture=new Texture2D(1,1,TextureFormat.RGBA32,false){name="Career UI button",filterMode=FilterMode.Point,wrapMode=TextureWrapMode.Clamp};
            texture.SetPixel(0,0,color);texture.Apply();return texture;
        }
        Vector2 Physical(Vector2 point)=>matrix.MultiplyPoint3x4(point);
        void Label(Rect rect,string text,GUIStyle style=null){GUI.Label(rect,text,style??body);}
        bool Button(Rect rect,string label,string id,Action action,bool enabled=true)
        {
            enabled=enabled&&Input.touchCount<=1;bool prior=GUI.enabled;GUI.enabled=prior&&enabled;GUI.SetNextControlName(id);
            if(GUI.enabled)keyboardControls.Add(id);
            var ev=Event.current;
            bool clicked=false;
            if(GUI.enabled&&ev.type==EventType.KeyDown&&(ev.keyCode==KeyCode.Return||ev.keyCode==KeyCode.Space)&&GUI.GetNameOfFocusedControl()==id)
            {if(!submitHeld){clicked=true;submitHeld=true;}ev.Use();}
            if(GUI.Button(rect,label,button))clicked=true;
            var pos=Physical(rect.center);uiDiagnostics.Add(PilotLedger.D("kind","button","id",id,"label",label,"x",pos.x,"y",pos.y,"enabled",GUI.enabled));
            GUI.enabled=prior;if(clicked&&enabled){GUI.FocusControl(null);action();return true;}return false;
        }
        void OnGUI()
        {
            if(package==null||CareerSuiteMode.IsOfficeScene(SceneManager.GetActiveScene().path))return;Styles();
            float scale=Mathf.Min(Screen.width/1440f,Screen.height/900f);
            var previous=GUI.matrix;matrix=Matrix4x4.TRS(new Vector3((Screen.width-1440*scale)/2,(Screen.height-900*scale)/2,0),Quaternion.identity,Vector3.one*scale);GUI.matrix=matrix;GUI.depth=-20;
            if(cancelGuiGesture){GUIUtility.hotControl=0;cancelGuiGesture=false;}
            if(clearFocus){GUI.FocusControl(null);clearFocus=false;}
            if(pendingGuiFocus.Length>0){GUI.FocusControl(pendingGuiFocus);pendingGuiFocus="";}
            var ev=Event.current;
            if(ev.type==EventType.KeyUp&&(ev.keyCode==KeyCode.Return||ev.keyCode==KeyCode.Space))submitHeld=false;
            if(ev.type==EventType.KeyDown&&ev.keyCode==KeyCode.Tab&&keyboardControls.Count>0)
            {
                int index=keyboardControls.IndexOf(GUI.GetNameOfFocusedControl());index=(index+(ev.shift?-1:1)+keyboardControls.Count)%keyboardControls.Count;FocusControl(keyboardControls[index]);ev.Use();
            }
            keyboardControls.Clear();uiDiagnostics.Clear();browserFields.Clear();
            if(ledger==null||ledger.Session.Ended)DrawSelector();
            else if(roomId!=ledger.Session.Definition.roomId)DrawAway();
            else if(resetDialog||endDialog)DrawConfirmation();
            else if(ledger.Session.Paused)DrawPause();
            else if(panel<0)DrawOverview();
            else DrawWork();
            focusedControl=browserFocusedControl.Length>0?browserFocusedControl:GUI.GetNameOfFocusedControl();GUI.matrix=previous;
            if(Event.current.type==EventType.Repaint)SyncBrowserFields();
        }
        void FocusControl(string id)
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            if(id.StartsWith("field-")){pendingBrowserFocus=id;return;}
#endif
            pendingGuiFocus=id;
        }
        string TextField(Rect rect,string value,string id,string label,bool editable,GUIStyle style=null)
        {
            GUI.SetNextControlName(id);if(editable)keyboardControls.Add(id);
#if UNITY_WEBGL && !UNITY_EDITOR
            Vector2 origin=Physical(rect.min),end=Physical(rect.max);
            browserFields.Add(new BrowserField{name=id,label=label,value=value,x=origin.x,y=origin.y,width=end.x-origin.x,height=end.y-origin.y,clipX=0,clipY=0,clipWidth=Screen.width,clipHeight=Screen.height,enabled=editable});
            GUI.Label(rect,value,style??input);return value;
#else
            bool before=GUI.enabled;GUI.enabled=editable;string changed=GUI.TextField(rect,value,style??input);GUI.enabled=before;return changed;
#endif
        }
        void SyncBrowserFields()
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            OfficeTenTextInputSync(JsonUtility.ToJson(new BrowserFrame{context=BrowserContext,screenWidth=Screen.width,screenHeight=Screen.height,fontSize=21*Mathf.Min(Screen.width/1440f,Screen.height/900f),fields=browserFields.ToArray()}));
            if(browserFields.Count==0)browserFocusedControl="";
            if(pendingBrowserFocus.Length>0){OfficeTenTextInputFocus(pendingBrowserFocus);pendingBrowserFocus="";}
#endif
        }
        public void OnBrowserTextInput(string json)
        {
            BrowserEdit edit;try{edit=JsonUtility.FromJson<BrowserEdit>(json);}catch{return;}
            if(edit==null||ledger==null||panel<0||edit.context!=BrowserContext||!edit.name.StartsWith("field-"))return;
            if(!int.TryParse(edit.name.Substring(6),out int field)||field<0||field>=ledger.Session.Drafts[panel].fields.Length)return;
            if(ledger.Session.Editable(panel)&&ledger.Session.Unlocked(panel)&&!transition&&edit.kind!="focus"&&ledger.Session.Drafts[panel].fields[field]!=(edit.value??""))
            {
                ledger.Session.Edit(panel,d=>d.fields[field]=edit.value??"");ledger.Edit(panel,edit.name);
            }
            if(edit.kind=="focus"){browserFocusedControl=edit.name;clearFocus=false;focused=true;}
            else if(edit.kind=="blur")
            {
                if(browserFocusedControl==edit.name)browserFocusedControl="";
                if(edit.reason=="window-blur"||edit.reason=="document-hidden"){focused=false;CancelGesture();}
            }
            else if(edit.kind=="escape"&&!edit.composing)Close();
            else if(edit.kind=="tab"&&!edit.composing&&keyboardControls.Count>0)
            {
                int index=keyboardControls.IndexOf(edit.name);FocusControl(keyboardControls[(index+(edit.backward?-1:1)+keyboardControls.Count)%keyboardControls.Count]);
            }
        }
        void DrawSelector()
        {
            if(CareerSuiteMode.Managed)return;
            GUI.Box(new Rect(1010,120,410,710),"");Label(new Rect(1030,140,370,40),"직업 체험 "+package.careers.Length+"개",heading);
            for(int i=0;i<package.careers.Length;i++)
            {
                var definition=package.careers[i];Button(new Rect(1030,195+i*55,370,47),definition.name,"career-"+i,()=>Begin(definition,PilotLedger.NewId("session-"),PilotLedger.NewId("experience-"),null));
            }
            Label(new Rect(1030,755,370,65),"가상 업무 체험 · 직업 적성이나 전문 자격을 판정하지 않습니다.",small);
        }
        void DrawAway()
        {
            GUI.Box(new Rect(920,130,500,250),"");Label(new Rect(940,150,460,100),ledger.Session.Definition.name+" 업무를 유지하고 있습니다. 다른 공간에서는 작업 시간이 멈춥니다.");
            Button(new Rect(940,265,220,55),"업무 공간으로 복귀","resume-room",()=>explorer.SelectRoom(ledger.Session.Definition.roomId));
            Button(new Rect(1170,265,225,55),"체험 종료","end-away",()=>endDialog=true);
            if(endDialog)DrawConfirmation();
        }
        void DrawOverview()
        {
            GUI.Box(new Rect(990,120,430,680),"");var d=ledger.Session.Definition;
            Label(new Rect(1010,140,390,45),d.name,heading);
            Label(new Rect(1010,190,390,70),d.title,body);Label(new Rect(1010,270,390,120),d.brief,small);
            for(int i=0;i<3;i++)
            {
                int step=i;Button(new Rect(1010,410+i*65,390,55),(i+1)+" "+d.objects[i].name+(ledger.Session.Drafts[i].completed?" ✓":""),"open-"+i,()=>Open(step));
            }
            int next=ledger.Session.CurrentStep;
            Label(new Rect(1010,615,390,70),ledger.Session.Complete?"업무 결과가 완성됐습니다. 체험 종료로 결과를 인계합니다.":"다음 업무: "+d.objects[Mathf.Max(0,next)].name+" · "+ledger.Session.Surfaces[Mathf.Max(0,next)].title+"\n3D 물건 클릭 / 1·2·3키. 닫기는 초안을 유지합니다.",small);
            Button(new Rect(1010,705,185,48),"일시정지","pause",()=>{CancelGesture();ledger.Pause(true);});Button(new Rect(1205,705,185,48),"체험 종료","end",()=>endDialog=true);
            if(ledger.Session.HasRequestChange&&!ledger.Session.RequestChanged&&!ledger.Session.Complete)Button(new Rect(1010,765,390,42),"마감 변경 요청 확인","request-change",ChangeRequest);
            if(ledger.Session.RequestChanged)Label(new Rect(375,120,580,110),"요청 v"+ledger.Session.RequestRevision+" · "+d.requestChangeBrief,small);
            Label(new Rect(365,805,1010,75),feedback,small);
        }
        void ChangeRequest()
        {
            CancelGesture();RestoreImmediately();
            if(ledger.ChangeRequest())feedback="요청이 변경됐습니다. 초안을 유지하고, 첫 물건부터 새 조건을 다시 확인하세요.";
        }
        void DrawPause()
        {
            GUI.Box(new Rect(500,170,740,560),"");Label(new Rect(535,195,660,55),"일시정지 · 초안과 진행을 유지합니다",heading);
            Button(new Rect(535,280,660,65),"계속하기","resume",()=>ledger.Pause(false));
            Button(new Rect(535,365,660,65),"화면 움직임 줄이기: "+(reducedMotion?"켜짐":"꺼짐"),"motion",()=>reducedMotion=!reducedMotion);
            Button(new Rect(535,450,320,65),"처음부터","reset",()=>resetDialog=true);Button(new Rect(875,450,320,65),"체험 종료","end-pause",()=>endDialog=true);
            Button(new Rect(535,545,660,65),"공간으로 복귀 · 업무 유지","close-pause",()=>{ledger.Pause(false);Close();});
        }
        void DrawConfirmation()
        {
            GUI.Box(new Rect(490,250,760,330),"");Label(new Rect(525,280,690,120),resetDialog?"현재 실행의 결과와 중단 이력을 보존하고 새 연습을 시작할까요?":"체험을 종료하고 완료한 결과·남은 업무·과정 기록을 인계할까요?",heading);
            Button(new Rect(525,440,320,65),"돌아가기","cancel-confirmation",()=>{resetDialog=endDialog=false;});
            Button(new Rect(875,440,320,65),"확인","confirm",()=>{RestoreImmediately();if(resetDialog){ledger.Reset();feedback="새 연습을 시작했습니다.";}else ledger.End(null);resetDialog=endDialog=false;});
        }
        void DrawWork()
        {
            int step=panel;var s=ledger.Session.Surfaces[step];var draft=ledger.Session.Drafts[step];
            GUI.Box(new Rect(790,110,630,730),"");Label(new Rect(815,130,580,50),s.title,heading);Label(new Rect(815,185,580,90),s.instruction);
            if(ledger.Session.HasRequestChange)Label(new Rect(365,120,390,80),"요청 revision "+ledger.Session.RequestRevision+"\n초안 "+draft.editRevision+" / 저장 "+draft.savedRevision+(draft.completed?" · 저장됨":" · 편집 중"),small);
            bool editable=ledger.Session.Editable(step)&&ledger.Session.Unlocked(step)&&!transition&&Input.touchCount<=1;
            if(!ledger.Session.Unlocked(step))Label(new Rect(815,285,575,60),"앞 업무를 완료한 뒤 작업할 수 있습니다.");
            else if((s.tiles??Array.Empty<PilotTile>()).Length>0)DrawTiles(step,editable);
            else if(s.kind=="photo")DrawPhoto(step,editable);
            else if(s.kind=="inspect")DrawFindings(step,editable);
            else if(s.kind=="dialogue")DrawDialogue(step,editable);
            else if(s.kind=="form")DrawFields(step,editable);
            else if(s.kind=="tune"||s.kind=="timer")DrawValues(step,editable);
            if(s.kind=="timer")
            {
                Label(new Rect(825,440,550,60),"경과 "+draft.elapsed.ToString("0.0")+" "+s.timerUnit+" / 목표 "+s.timerMin+"~"+s.timerMax);
                Rect bar=new Rect(830,520,540,30);GUI.Box(bar,"");var old=GUI.color;GUI.color=Color.cyan;GUI.DrawTexture(new Rect(bar.x,bar.y,bar.width*Mathf.Clamp01(draft.elapsed/s.timerLimit),bar.height),Texture2D.whiteTexture);GUI.color=old;
                if(draft.running)Button(new Rect(820,635,575,55),"지금 멈추고 결과 확인","timer-stop",()=>ledger.Session.StopTimer(step),!transition);
                else Button(new Rect(820,635,575,55),"작업 시작","timer-start",()=>ledger.Session.StartTimer(step),editable);
            }
            else Button(new Rect(820,635,575,55),draft.completed?"저장된 결과":s.kind=="photo"?"사진 촬영·저장":"작업 결과 저장·확정","submit",()=>{if(s.kind=="photo")CapturePhoto(step);else ledger.Session.Submit(step);},editable);
            if(draft.completed)
            {
                int next=ledger.Session.CurrentStep;
                feedback="✓ "+s.successText+(next<0?"\n세 업무 완료 · 종료하면 결과를 인계합니다.":"\n닫기 → "+ledger.Session.Definition.objects[next].name+"에서 업무 계속");
                var prior=GUI.color;GUI.color=new Color(.12f,.28f,.24f,.96f);GUI.DrawTexture(new Rect(365,665,390,120),Texture2D.whiteTexture);GUI.color=prior;
                Label(new Rect(382,678,355,30),"✓ 저장된 업무 결과",heading);
                Label(new Rect(382,714,355,65),s.successText,small);
            }
            Label(new Rect(815,700,580,65),feedback,small);
            Button(new Rect(815,775,175,45),"닫기 · Esc","close",Close,!transition);
            Button(new Rect(1000,775,170,45),"도움","help",()=>{ledger.Help(step);showHint=!showHint;feedback=showHint?Hint(step):"도움을 닫았습니다. 초안은 유지됩니다.";},!transition);
            Button(new Rect(1180,775,215,45),"일시정지","pause-work",()=>{CancelGesture();ledger.Pause(true);},!transition);
        }
        string Hint(int step)
        {
            var s=ledger.Session.Surfaces[step];
            var parts=(s.fields??Array.Empty<PilotField>()).Select(f=>f.label+" = "+f.target)
                .Concat((s.values??Array.Empty<PilotValue>()).Select(v=>v.label+" = "+v.target+v.unit))
                .Concat((s.tiles??Array.Empty<PilotTile>()).Select((t,i)=>t.label+" → "+(i+1)+"번 자리"))
                .Concat((s.findings??Array.Empty<PilotFinding>()).Select(f=>f.label+": "+f.detail));
            return "도움: "+string.Join(" / ",parts)+(s.kind=="timer"?" 목표 구간 "+s.timerMin+"~"+s.timerMax+" 가상 초에 정지":"");
        }
        bool RenderPhoto(int step)
        {
            photo=photo??new PilotPhoto();var d=ledger.Session.Drafts[step];var light=ledger.Session.Drafts[1].values;
            return photo.Render(ledger.Session.Definition,cameraView,savedPosition,d.values[0],d.values[1],light.Length>1?(light[0]+light[1])/100f:1);
        }
        void LateUpdate()
        {
            if(ledger!=null&&!ledger.Session.Ended&&!ledger.Session.Paused&&panel>=0&&!transition&&ledger.Session.Surfaces[panel].kind=="photo"&&Time.unscaledTime-photoTime>.4f){photoTime=Time.unscaledTime;RenderPhoto(panel);}
        }
        void DrawPhoto(int step,bool editable)
        {
            if(photo?.Viewfinder!=null)GUI.DrawTexture(new Rect(940,278,320,180),photo.Viewfinder,ScaleMode.ScaleToFit);
            else Label(new Rect(830,285,550,80),photo?.Error??"실제 3D 촬영 대상을 불러옵니다.");
            DrawValues(step,editable,455,60);
            var d=ledger.Session.Drafts[step];var f=ledger.Session.Surfaces[step].fields[0];Label(new Rect(825,602,170,30),f.label,small);
            Rect rect=new Rect(1010,596,370,33);var photoInput=new GUIStyle(input){fontSize=17,padding=new RectOffset(6,6,3,3)};string value=TextField(rect,d.fields[0],"field-0",f.label,editable,photoInput);
            if(editable&&value!=d.fields[0]){ledger.Session.Edit(step,x=>x.fields[0]=value);ledger.Edit(step,"field-0");}var pos=Physical(rect.center);uiDiagnostics.Add(PilotLedger.D("kind","field","id","field-0","value",d.fields[0],"x",pos.x,"y",pos.y,"enabled",editable));
        }
        [DllImport("__Internal")] static extern void PilotStoreArtifact(string id,string filename,string base64);
        void CapturePhoto(int step)
        {
            if(ledger.Session.Validate(step).Any(r=>r!="CAPTURE_REQUIRED")){ledger.Session.Submit(step);return;}
            if(!RenderPhoto(step)){feedback=photo.Error+" 다시 촬영하세요. 업무 실패로 집계하지 않습니다.";return;}
            byte[] png;try{png=photo.Capture();}catch(Exception){feedback="촬영 결과를 읽지 못했습니다. 다시 촬영하세요.";return;}
            if(png==null||png.Length==0){feedback="사진 파일을 만들지 못했습니다. 다시 촬영하세요.";return;}
            var d=ledger.Session.Drafts[step];d.artifactId=PilotLedger.NewId("photo-");d.artifactName=d.fields[0]+".png";d.artifactWidth=320;d.artifactHeight=180;d.artifactBytes=png.Length;
#if UNITY_WEBGL && !UNITY_EDITOR
            PilotStoreArtifact(d.artifactId,d.artifactName,Convert.ToBase64String(png));
#endif
            ledger.Session.Submit(step);
        }
        void DrawFindings(int step,bool editable)
        {
            var s=ledger.Session.Surfaces[step];var d=ledger.Session.Drafts[step];
            for(int i=0;i<s.findings.Length;i++)
            {
                int index=i;Button(new Rect(825,290+i*95,210,75),(d.observed[i]?"✓ ":"")+s.findings[i].label,"finding-"+i,()=>{ledger.Session.Observe(step,index);ledger.Edit(step,"observe-"+index);},editable);
                if(d.observed[i])Label(new Rect(1050,290+i*95,325,85),s.findings[i].detail);
            }
        }
        void DrawDialogue(int step,bool editable)
        {
            var surface=ledger.Session.Surfaces[step];var draft=ledger.Session.Drafts[step];
            for(int i=0;i<surface.findings.Length;i++)
            {
                int index=i;Button(new Rect(825,285+i*65,230,55),surface.findings[i].label,"question-"+i,()=>{ledger.Session.Observe(step,index);ledger.Edit(step,"question-"+index);},editable);
                if(draft.observed[i])Label(new Rect(1070,285+i*65,310,60),surface.findings[i].detail);
            }
            for(int i=0;i<surface.fields.Length;i++)
            {
                int index=i;float y=435+i*80;Label(new Rect(825,y,175,45),surface.fields[i].label);Rect rect=new Rect(1010,y-5,370,50);string id="field-"+i;
                string value=TextField(rect,draft.fields[i],id,surface.fields[i].label,editable);
                if(editable&&value!=draft.fields[i]){ledger.Session.Edit(step,x=>x.fields[index]=value);ledger.Edit(step,id);}
                var point=Physical(rect.center);uiDiagnostics.Add(PilotLedger.D("kind","field","id",id,"value",draft.fields[i],"x",point.x,"y",point.y,"enabled",editable));
            }
        }
        void DrawFields(int step,bool editable)
        {
            var s=ledger.Session.Surfaces[step];var d=ledger.Session.Drafts[step];
            for(int i=0;i<s.fields.Length;i++)
            {
                Label(new Rect(825,290+i*90,180,40),s.fields[i].label);Rect rect=new Rect(1010,285+i*90,370,55);string id="field-"+i;
                string value=TextField(rect,d.fields[i],id,s.fields[i].label,editable);
                if(value!=d.fields[i]&&editable){int index=i;ledger.Session.Edit(step,x=>x.fields[index]=value);ledger.Edit(step,id);}
                var pos=Physical(rect.center);uiDiagnostics.Add(PilotLedger.D("kind","field","id",id,"value",d.fields[i],"x",pos.x,"y",pos.y,"enabled",editable));
            }
        }
        void DrawValues(int step,bool editable,float startY=290,float spacing=125)
        {
            var s=ledger.Session.Surfaces[step];var d=ledger.Session.Drafts[step];
            for(int i=0;i<(s.values??Array.Empty<PilotValue>()).Length;i++)
            {
                int index=i;var v=s.values[i];float y=startY+i*spacing;Label(new Rect(825,y,550,35),v.label+"  "+d.values[i].ToString(v.tolerance==0?"0.######":"0.0")+" "+v.unit);
                bool previous=GUI.enabled;GUI.enabled=editable;GUI.SetNextControlName("slider-"+i);if(editable)keyboardControls.Add("slider-"+i);
                float value=GUI.HorizontalSlider(new Rect(895,y+45,410,25),d.values[i],v.min,v.max);value=SnapValue(v,value);GUI.enabled=previous;
                if(editable&&Mathf.Abs(value-d.values[i])>.0001f){ledger.Session.Edit(step,x=>x.values[index]=value);ledger.Edit(step,"slider-"+i);}
                Button(new Rect(825,y+35,55,45),"−","minus-"+i,()=>ChangeValue(step,index,-1),editable);
                Button(new Rect(1320,y+35,55,45),"+","plus-"+i,()=>ChangeValue(step,index,1),editable);
                var pos=Physical(new Vector2(1100,y+57.5f));uiDiagnostics.Add(PilotLedger.D("kind","slider","id",v.id,"value",d.values[i],"min",v.min,"max",v.max,"x",pos.x,"y",pos.y,"centered",true,"left",Physical(new Vector2(895,y+45)).x,"right",Physical(new Vector2(1305,y+45)).x));
            }
        }
        void ChangeValue(int step,int index,float delta)
        {
            var v=ledger.Session.Surfaces[step].values[index];float increment=v.tolerance==0?1f/ValueScale(v):1f;
            ledger.Session.Edit(step,d=>d.values[index]=SnapValue(v,Mathf.Clamp(d.values[index]+delta*increment,v.min,v.max)));ledger.Edit(step,v.id);
        }
        static float ValueScale(PilotValue value)
        {
            // Exact-count task data declares the required decimal precision.
            // The pointer slider and equivalent buttons use the same grid.
            string target=value.target.ToString("0.######",System.Globalization.CultureInfo.InvariantCulture);
            int point=target.IndexOf('.');return point<0?1:Mathf.Pow(10,target.Length-point-1);
        }
        static float SnapValue(PilotValue definition,float value)
        {
            if(definition.tolerance!=0)return value;
            float scale=ValueScale(definition);
            return Mathf.Clamp((float)(Math.Round((double)value*scale,MidpointRounding.AwayFromZero)/scale),definition.min,definition.max);
        }
        void DrawTiles(int step,bool editable)
        {
            var s=ledger.Session.Surfaces[step];var d=ledger.Session.Drafts[step];GUI.Box(board,"");
            for(int i=0;i<s.tiles.Length;i++)
            {
                var t=s.tiles[i];Rect target=TileRect(t,t.targetX,t.targetY);
                GUI.Box(target,"");var marker=new GUIStyle(small){fontSize=14,wordWrap=false};GUI.Label(new Rect(target.x,target.y-22,target.width,22),SlotLabel(s,i),marker);var pos=Physical(target.center);uiDiagnostics.Add(PilotLedger.D("kind","target","id",t.id,"label",SlotLabel(s,i),"x",pos.x,"y",pos.y,"left",Physical(target.min).x,"top",Physical(target.min).y,"width",Physical(target.max).x-Physical(target.min).x,"height",Physical(target.max).y-Physical(target.min).y));
            }
            var ev=Event.current;Vector2 point=ev.mousePosition;
            if(editable&&ev.type==EventType.MouseDown&&board.Contains(point))
            {
                int previousTile=selectedTile,hit=-1;
                for(int i=s.tiles.Length-1;i>=0;i--)if(TileRect(s.tiles[i],d.x[i],d.y[i]).Contains(point)){hit=i;break;}
                if(placementArmed&&previousTile>=0&&SlotAt(s,point)>=0){PlaceTile(step,previousTile,point,point,"place-"+previousTile);ev.Use();}
                else if(hit>=0){placementArmed=false;selectedTile=hit;dragTile=true;dragStep=step;dragGeneration=ledger.Session.Generation;dragRun=ledger.Session.RunId;dragStart=new Vector2(d.x[hit],d.y[hit]);tilePointerStart=point;tileGrabOffset=point-TileRect(s.tiles[hit],d.x[hit],d.y[hit]).center;tileMoved=false;ev.Use();}
                else if(previousTile>=0){PlaceTile(step,previousTile,point,point,"place-"+previousTile);ev.Use();}
            }
            if(editable&&dragTile&&selectedTile>=0&&(ev.type==EventType.MouseDrag||ev.type==EventType.MouseUp))
            {
                if(ev.type==EventType.MouseUp&&!board.Contains(point)){CancelGesture();feedback="작업면 밖으로 놓아 이동을 취소했습니다.";ev.Use();return;}
                int index=selectedTile;tileMoved=tileMoved||Vector2.Distance(point,tilePointerStart)>=4;
                if(ev.type==EventType.MouseUp){dragTile=false;if(tileMoved)PlaceTile(step,index,point-tileGrabOffset,point,"drag-"+index);}
                else if(tileMoved){Vector2 centre=point-tileGrabOffset;ledger.Session.Edit(step,t=>{t.x[index]=Mathf.Clamp01((centre.x-board.x)/board.width);t.y[index]=Mathf.Clamp01((centre.y-board.y)/board.height);});}ev.Use();
            }
            for(int i=0;i<s.tiles.Length;i++)
            {
                int index=i;var t=s.tiles[i];Rect rect=TileRect(t,d.x[i],d.y[i]);var before=GUI.color;GUI.color=selectedTile==i?new Color(.7f,.9f,1):Color.white;
                var tileStyle=new GUIStyle(button){fontSize=16,padding=new RectOffset(3,3,3,3),alignment=TextAnchor.MiddleCenter};GUI.Box(rect,t.label,tileStyle);GUI.color=before;
                Button(new Rect(830+i*183,board.yMax+5,177,35),"선택 "+(i+1),"tile-"+i,()=>{selectedTile=index;placementArmed=true;feedback=t.label+" 선택. 목적지 칸을 누르거나 4·5·6키로 칸을 지정하세요.";},editable);
                var pos=Physical(rect.center);uiDiagnostics.Add(PilotLedger.D("kind","tile","id",t.id,"label",t.label,"x",pos.x,"y",pos.y,"normalizedX",d.x[i],"normalizedY",d.y[i]));
            }
            if(editable&&selectedTile>=0)
            {
                if(ev.type==EventType.KeyDown&&ev.keyCode>=KeyCode.Alpha4&&ev.keyCode<=KeyCode.Alpha6){int slot=(int)ev.keyCode-(int)KeyCode.Alpha4;if(slot<s.tiles.Length){Vector2 centre=TileRect(s.tiles[slot],s.tiles[slot].targetX,s.tiles[slot].targetY).center;PlaceTile(step,selectedTile,centre,centre,"place-key-"+slot);ev.Use();}}
                if(ev.type==EventType.KeyDown&&new[]{KeyCode.LeftArrow,KeyCode.RightArrow,KeyCode.UpArrow,KeyCode.DownArrow}.Contains(ev.keyCode))
                {int index=selectedTile;float dx=ev.keyCode==KeyCode.LeftArrow?-.025f:ev.keyCode==KeyCode.RightArrow?.025f:0,dy=ev.keyCode==KeyCode.UpArrow?-.025f:ev.keyCode==KeyCode.DownArrow?.025f:0;ledger.Session.Edit(step,t=>{t.x[index]=Mathf.Clamp01(t.x[index]+dx);t.y[index]=Mathf.Clamp01(t.y[index]+dy);});ledger.Edit(step,"nudge-"+index);ev.Use();}
            }
        }
        string SlotLabel(PilotSurface surface,int slot)=>string.IsNullOrEmpty(surface.tiles[slot].slotLabel)?(slot+1)+"번 자리":surface.tiles[slot].slotLabel;
        int SlotAt(PilotSurface surface,Vector2 pointer)
        {
            int best=-1;float distance=float.PositiveInfinity;
            for(int i=0;i<surface.tiles.Length;i++){var t=surface.tiles[i];Rect zone=TileRect(t,t.targetX,t.targetY);if(!zone.Contains(pointer))continue;float next=(pointer-zone.center).sqrMagnitude;if(next<distance){distance=next;best=i;}}
            return best;
        }
        void PlaceTile(int step,int item,Vector2 centre,Vector2 pointer,string control)
        {
            placementArmed=false;var surface=ledger.Session.Surfaces[step];int slot=SlotAt(surface,pointer);
            if(slot>=0){var target=surface.tiles[slot];centre=TileRect(target,target.targetX,target.targetY).center;}
            float x=Mathf.Clamp01((centre.x-board.x)/board.width),y=Mathf.Clamp01((centre.y-board.y)/board.height);
            ledger.Session.Edit(step,d=>{d.x[item]=x;d.y[item]=y;});ledger.Edit(step,control);
            feedback=slot>=0?surface.tiles[item].label+" → "+SlotLabel(surface,slot)+" 배치. 저장 버튼으로 결과를 확인하세요.":"목표 칸 바깥입니다. 칸 안에 놓거나 물건 선택 후 4·5·6키로 칸을 지정하세요.";
        }
        Rect TileRect(PilotTile tile,float x,float y){float width=Mathf.Max(.24f,tile.width),height=Mathf.Max(.20f,tile.height);return new Rect(board.x+(x-width/2)*board.width,board.y+(y-height/2)*board.height,width*board.width,height*board.height); }
        void Open(int step)
        {
            if(!started||transition||ledger==null||ledger.Session.Ended||ledger.Session.Paused||roomId!=ledger.Session.Definition.roomId)return;
            var binding=ledger.Session.Definition.objects[step];var root=FindObjectsByType<Transform>(FindObjectsSortMode.None).FirstOrDefault(t=>t.name==binding.nodeName);
            if(root==null){feedback="작업 물건을 찾지 못했습니다. 공간을 다시 열어 주세요.";return;}
            var selected=root.GetComponentsInChildren<Renderer>();if(selected.Length==0){feedback="물건의 표시 정보를 불러오지 못했습니다.";return;}
            Bounds bounds=selected[0].bounds;foreach(var r in selected)bounds.Encapsulate(r.bounds);
            savedPosition=cameraView.transform.position;savedRotation=cameraView.transform.rotation;savedFov=cameraView.fieldOfView;savedRect=cameraView.rect;
            renderers=FindObjectsByType<Renderer>(FindObjectsSortMode.None);visibility=renderers.Select(r=>r.enabled).ToArray();foreach(var r in renderers)r.enabled=selected.Contains(r)&&r.enabled;
            panel=step;selectedTile=-1;showHint=false;clearFocus=true;ledger.Open(step);
            Vector3 direction=(savedPosition-bounds.center).normalized;float radius=Mathf.Max(.3f,bounds.extents.magnitude);
            float aspect=(Mathf.Max(1,Screen.width)*.29f)/(Mathf.Max(1,Screen.height)*.64f);
            float halfAngle=Mathf.Atan(Mathf.Tan(21*Mathf.Deg2Rad)*Mathf.Min(1,aspect));
            float framingDistance=radius/Mathf.Sin(halfAngle)*1.12f;
            BeginTransition(bounds.center+direction*Mathf.Max(1.1f,framingDistance),Quaternion.LookRotation(-direction),42,new Rect(.245f,.16f,.29f,.64f),false);
        }
        void BeginTransition(Vector3 pos,Quaternion rot,float fov,Rect rect,bool back)
        {
            fromPosition=cameraView.transform.position;fromRotation=cameraView.transform.rotation;fromFov=cameraView.fieldOfView;fromRect=cameraView.rect;
            toPosition=pos;toRotation=rot;toFov=fov;toRect=rect;returning=back;transition=true;transitionTime=0;if(reducedMotion)MoveCamera(1);
        }
        void MoveCamera(float t)
        {
            if(cameraView==null){transition=false;return;}
            cameraView.transform.SetPositionAndRotation(Vector3.Lerp(fromPosition,toPosition,t),Quaternion.Slerp(fromRotation,toRotation,t));cameraView.fieldOfView=Mathf.Lerp(fromFov,toFov,t);
            cameraView.rect=new Rect(Mathf.Lerp(fromRect.x,toRect.x,t),Mathf.Lerp(fromRect.y,toRect.y,t),Mathf.Lerp(fromRect.width,toRect.width,t),Mathf.Lerp(fromRect.height,toRect.height,t));
            if(t>=1){transition=false;if(returning){RestoreVisibility();panel=-1;returning=false;}}
        }
        void Close()
        {
            if(panel<0||transition&&returning)return;
            if(transition)MoveCamera(1);
            CancelGesture();ledger.Close(panel);clearFocus=true;BeginTransition(savedPosition,savedRotation,savedFov,savedRect,true);
        }
        void CancelGesture()
        {
            if(dragTile&&ledger!=null&&!ledger.Session.Ended&&ledger.Session.Generation==dragGeneration&&ledger.Session.RunId==dragRun&&dragStep>=0&&dragStep<ledger.Session.Drafts.Length&&selectedTile>=0)
            {
                var draft=ledger.Session.Drafts[dragStep];if(selectedTile<draft.x.Length){draft.x[selectedTile]=dragStart.x;draft.y[selectedTile]=dragStart.y;}
            }
            dragTile=tracking=placementArmed=false;cancelGuiGesture=true;
        }
        void RestoreVisibility(){for(int i=0;i<renderers.Length;i++)if(renderers[i]!=null)renderers[i].enabled=visibility[i];renderers=Array.Empty<Renderer>();visibility=Array.Empty<bool>();}
        void RestoreImmediately()
        {
            CancelGesture();
            if(panel>=0&&cameraView!=null){cameraView.transform.SetPositionAndRotation(savedPosition,savedRotation);cameraView.fieldOfView=savedFov;cameraView.rect=savedRect;}
            RestoreVisibility();panel=selectedTile=-1;transition=returning=dragTile=tracking=false;
        }
        void OnApplicationFocus(bool value){focused=value;if(!value)CancelGesture();}
        void Update()
        {
            if(ledger==null){if(Time.unscaledTime-diagnosticTime>.25f){diagnosticTime=Time.unscaledTime;Publish();}return;}
            if(Input.touchCount>1||Input.touchCount==1&&Input.GetTouch(0).phase==TouchPhase.Canceled)CancelGesture();
            bool inRoom=started&&!navigating&&roomId==ledger.Session.Definition.roomId;
            ledger.Session.ActiveSurface=panel>=0&&!transition?panel:-1;
            ledger.Session.Tick(Time.unscaledDeltaTime,inRoom,focused);
            if(started&&Time.unscaledTime-checkpointTime>1){checkpointTime=Time.unscaledTime;ledger.Checkpoint();}
            if(ledger.Session.Ended){if(Time.unscaledTime-diagnosticTime>.25f){diagnosticTime=Time.unscaledTime;Publish();}return;}
            if(transition&&!ledger.Session.Paused){transitionTime+=Time.unscaledDeltaTime;MoveCamera(reducedMotion?1:Mathf.SmoothStep(0,1,Mathf.Clamp01(transitionTime/(package.transitionSeconds>=.05f&&package.transitionSeconds<=5?package.transitionSeconds:.45f))));}
            bool editing=focusedControl.StartsWith("field-")||browserFocusedControl.Length>0;
            if(!editing&&Input.GetKeyDown(KeyCode.P)){CancelGesture();ledger.Pause(!ledger.Session.Paused);}
            if(Input.GetKeyDown(KeyCode.Escape)){bool wasDragging=dragTile;CancelGesture();if(wasDragging)selectedTile=-1;else if(resetDialog||endDialog){resetDialog=endDialog=false;}else if(panel>=0)Close();else ledger.Pause(!ledger.Session.Paused);}
            if(inRoom&&!editing&&panel<0&&!transition&&!ledger.Session.Paused)
            {
                for(int i=0;i<3;i++)if(Input.GetKeyDown((KeyCode)((int)KeyCode.Alpha1+i)))Open(i);
                if(Input.touchCount>1){tracking=false;return;}
                Vector2 point=Input.mousePosition;
                if(Input.GetMouseButtonDown(0)){tracking=cameraView!=null&&cameraView.pixelRect.Contains(point)&&point.x<Screen.width*.68f;pointerStart=point;dragged=false;}
                if(tracking&&Input.GetMouseButton(0)&&Vector2.Distance(pointerStart,point)>8)dragged=true;
                if(tracking&&Input.GetMouseButtonUp(0))
                {
                    tracking=false;
                    if(!dragged&&Physics.Raycast(cameraView.ScreenPointToRay(point),out RaycastHit hit,100))
                    {
                        for(int i=0;i<3;i++){Transform t=hit.transform;while(t!=null&&t.name!=ledger.Session.Definition.objects[i].nodeName)t=t.parent;if(t!=null){Open(i);break;}}
                    }
                }
            }
            if(Time.unscaledTime-diagnosticTime>.25f){diagnosticTime=Time.unscaledTime;Publish();}
        }
        void Publish()
        {
            if(ledger==null){PublishJson(PilotLedger.Json(PilotLedger.D("schema_version",3,"buildId",buildId,"roomId",roomId,"careers",package.careers.Select(d=>PilotLedger.D("scenarioId",d.scenarioId,"version",d.version,"roomId",d.roomId,"name",d.name)).ToArray(),"controls",uiDiagnostics.ToArray())));return;}
            var obj=ledger.Session.Definition.objects.Select((o,i)=>{var root=FindObjectsByType<Transform>(FindObjectsSortMode.None).FirstOrDefault(t=>t.name==o.nodeName);var pieces=root==null?Array.Empty<Renderer>():root.GetComponentsInChildren<Renderer>();var bounds=pieces.Length==0?new Bounds():pieces[0].bounds;foreach(var piece in pieces)bounds.Encapsulate(piece.bounds);Vector3 point=cameraView==null?Vector3.zero:cameraView.WorldToScreenPoint(bounds.center);return PilotLedger.D("id",o.id,"name",o.name,"assetId",o.assetId,"assetVersion",o.assetVersion,"instanceId",o.instanceId,"nodeName",o.nodeName,"step",i,"x",point.x,"y",Screen.height-point.y,"inFront",point.z>0,"renderers",pieces.Length,"visibleRenderers",pieces.Count(r=>r.enabled),"colliders",root==null?0:root.GetComponentsInChildren<Collider>().Length);}).ToArray();
            string json=PilotLedger.Json(PilotLedger.D("schema_version",3,"buildId",buildId,"roomId",roomId,"ready",started,"scenarioId",ledger.Session.Definition.scenarioId,"scenarioVersion",ledger.Session.Definition.version,"experienceId",ledger.ExperienceId,"runId",ledger.Session.RunId,"panel",panel,"transition",transition,"reducedMotion",reducedMotion,"paused",ledger.Session.Paused,"ended",ledger.Session.Ended,"complete",ledger.Session.Complete,"activeMs",ledger.Session.ActiveMs,"feedback",feedback,"camera",CameraState(),"visibleRenderers",FindObjectsByType<Renderer>(FindObjectsSortMode.None).Count(r=>r.enabled),"focusedControl",focusedControl,"objects",obj,"surfaces",ledger.Session.Surfaces.Select((s,i)=>PilotLedger.D("id",s.id,"kind",s.kind,"completed",ledger.Session.Drafts[i].completed,"input",ledger.Input(i))).ToArray(),"controls",uiDiagnostics.ToArray()));
            PublishJson(json);
        }
        object CameraState(){if(cameraView==null)return null;var p=cameraView.transform.position;var q=cameraView.transform.rotation;var r=cameraView.rect;return PilotLedger.D("position",new[]{p.x,p.y,p.z},"rotation",new[]{q.x,q.y,q.z,q.w},"fov",cameraView.fieldOfView,"rect",new[]{r.x,r.y,r.width,r.height});}
        void PublishJson(string json)
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            PublishPilotState(json);
#else
            Debug.Log("PILOT_STATE "+json);
#endif
        }
    }
}

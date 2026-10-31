using System;
using System.Collections.Generic;
using System.Linq;
using System.Runtime.InteropServices;
using UnityEngine;
namespace CareerExperience
{
    public sealed class OfficeTenExperience : MonoBehaviour
    {
        public TextAsset scenarios;
        public Font koreanFont;
        public Camera viewCamera;
        public OfficeBinding[] bindings;
        public bool reducedMotion;
        [Min(.05f)] public float transitionSeconds=.45f;
        public OfficeTenSession Session { get; private set; }
        TextMesh monitorDocument;
        MeshRenderer monitorDocumentRenderer;
        Vector3[] monitorPreviewCorners=Array.Empty<Vector3>();
        bool monitorPreviewFits;
        OfficeTenCatalog catalog;
        OfficeTenProtocol protocol;
        string panel="",feedback="",renderedFocus="",focusedControl="",placementInput="";
        string[][] drafts,placements;
        Renderer[] roomRenderers;
        bool[] originalVisibility;
        bool transitioning,hasSavedCamera,tracking,dragging,resetDialog,jobMenu,clearFocus;
        Vector2 pointerStart,pointerLast,scroll;
        float yaw=152,pitch=34,distance=9.7f,transitionStart,transitionFov,savedFov,lastPublish;
        Vector3 overviewPosition,transitionPosition,savedPosition;
        Quaternion overviewRotation,transitionRotation,savedRotation;
        Rect transitionRect,savedRect;
        int focusedObject,selectedItem=-1,dragItem=-1,escapeFrame=-1,pendingJob=-1;
        Vector2 dragStart;
        KeyCode heldKey=KeyCode.None;
        GUIStyle label,small,title,input,button,paper;
        float Scale=>Mathf.Max(.01f,Mathf.Min(Screen.width/1440f,Screen.height/900f));
        Vector2 Offset=>new Vector2((Screen.width-1440*Scale)/2,(Screen.height-900*Scale)/2);
        Vector2 UiPoint(Vector2 screen)=>(new Vector2(screen.x,Screen.height-screen.y)-Offset)/Scale;
        float TransitionDuration=>float.IsNaN(transitionSeconds)||float.IsInfinity(transitionSeconds)? .45f:Mathf.Clamp(transitionSeconds,.05f,5);
        string Context=>Session.Data.scenario_id+"|"+panel+"|"+Session.StepIndex+"|"+Session.Paused+"|"+resetDialog+"|"+jobMenu+"|"+protocol.Ended;
        bool EditingText=>browserFocusedControl.Length>0||focusedControl.StartsWith("field_");
        string browserFocusedControl="",pendingBrowserFocus="",pendingGuiFocus="";
        bool browserComposing;
        string BrowserContext=>protocol.RunId+"|"+Context;
        [Serializable] sealed class BrowserField
        {
            public string name,label,value;
            public float x,y,width,height,clipX,clipY,clipWidth,clipHeight;
            public bool enabled;
        }
        [Serializable] sealed class BrowserFrame
        {
            public string target="OfficeExperience",callback="OnBrowserTextInput",context;
            public int screenWidth,screenHeight;
            public float fontSize;
            public BrowserField[] fields;
        }
        [Serializable] sealed class BrowserEdit
        {
            public string context,name,value,kind,reason;
            public bool composing,backward,windowFocused;
        }
        readonly List<BrowserField> browserFields=new List<BrowserField>();
#if UNITY_WEBGL && !UNITY_EDITOR
        bool previousKeyboardCapture;
        [DllImport("__Internal")]static extern void OfficeTenTextInputSync(string json);
        [DllImport("__Internal")]static extern void OfficeTenTextInputFocus(string name);
        [DllImport("__Internal")]static extern void OfficeTenTextInputBlur();
        [DllImport("__Internal")]static extern void OfficeTenTextInputDispose();
#endif
        sealed class Nav { public string name,context; public Rect rect;public Action action;public bool field;public float scrollY; }
        List<Nav> previousNav=new List<Nav>(),nav=new List<Nav>();
        [Serializable] public class ButtonDiagnostic { public string label;public float x,y;public bool enabled; }
        [Serializable] public class InputDiagnostic { public string name,value;public float x,y;public bool enabled; }
        [Serializable] public class TargetDiagnostic { public string id;public float x,y; }
        [Serializable] public class StepDiagnostic {public string stepId;public string[] values,placements;}
        [Serializable] public class SortDiagnostic {public string id,label,kind;public float x,y;}
        [Serializable] public class DiagnosticState
        {
            public string scenarioId,scenarioVersion,occupationId,name,panel,feedback,viewState,focusedControl,runId,experienceId;
            public OfficeTenSnapshot session;
            public TargetDiagnostic[] targets;
            public ButtonDiagnostic[] buttons;
            public InputDiagnostic[] inputs;
            public SortDiagnostic[] sorting;
            public int interactiveObjects,triangles,visibleRenderers,paletteWidth,paletteHeight,renderedCompletedSheets;
            public StepDiagnostic[] work; public int selectedItem;
            public bool reducedMotion;
            public bool monitorPreviewVisible,monitorPreviewFits,browserInputFocused,browserInputComposing;
            public string monitorPreviewText;
            public Vector3[] monitorPreviewCornersWorld;
            public float transitionSeconds;
            public Vector3 cameraPosition;public Quaternion cameraRotation;public Rect cameraRect;public float cameraFov;
        }
        readonly List<ButtonDiagnostic> buttonDiagnostics=new List<ButtonDiagnostic>();
        readonly List<InputDiagnostic> inputDiagnostics=new List<InputDiagnostic>();
        readonly List<SortDiagnostic> sortDiagnostics=new List<SortDiagnostic>();
        [DllImport("__Internal")]static extern void PublishOfficeState(string json);
        void Awake()
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            previousKeyboardCapture=WebGLInput.captureAllKeyboardInput;
            WebGLInput.captureAllKeyboardInput=false;
#endif
            gameObject.name="OfficeExperience";catalog=JsonUtility.FromJson<OfficeTenCatalog>(scenarios.text);
            protocol=OfficeTenProtocol.Get();Session=protocol.Attach(catalog.scenarios[0],this);
            roomRenderers=bindings[0].renderer.transform.parent.GetComponentsInChildren<Renderer>();originalVisibility=Array.ConvertAll(roomRenderers,r=>r.enabled);
            ClearInputs();PositionCamera(true);
        }
        void OnDestroy()
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            OfficeTenTextInputDispose();WebGLInput.captureAllKeyboardInput=previousKeyboardCapture;
#endif
            if(monitorDocument!=null)Destroy(monitorDocument.gameObject);if(protocol!=null)protocol.Detach(this);
        }
        void ClearInputs()
        {
            drafts=Session.Data.steps.Select(s=>(s.fields??Array.Empty<OfficeTenField>()).Select(f=>f.initial??"").ToArray()).ToArray();
            placements=Session.Data.steps.Select(s=>new string[(s.items??Array.Empty<OfficeTenItem>()).Length]).ToArray();
            panel="";feedback="";scroll=Vector2.zero;jobMenu=resetDialog=false;selectedItem=dragItem=-1;tracking=false;clearFocus=true;heldKey=KeyCode.None;previousNav.Clear();
            browserFocusedControl=pendingBrowserFocus=pendingGuiFocus="";browserComposing=false;
        }
        public void BeginExternalRun(){Session=protocol.Session;ClearInputs();renderedFocus="__restore";}
        public void EndUi(){dragItem=selectedItem=-1;tracking=false;clearFocus=true;}
        public string CurrentObject=>panel.Length>0?panel:null;
        public string ActualInput(string action)
        {
            if(action=="place_item")return placementInput;
            int i=Array.FindIndex(Session.Data.steps,s=>s.object_id==panel);return i<0?action:string.Join(" | ",drafts[i])+" / "+string.Join(" | ",placements[i].Select(x=>x??"未配置"));
        }
        void PositionCamera(bool snap = false)
        {
            Vector3 center = new Vector3(0, .75f, 0);
            overviewPosition = center + Quaternion.Euler(pitch, yaw, 0) * new Vector3(0, 0, -distance);
            overviewRotation = Quaternion.LookRotation(center - overviewPosition);
            if (snap) viewCamera.transform.SetPositionAndRotation(overviewPosition, overviewRotation);
        }
        void UpdateCloseup()
        {
            bool closeup = panel.Length > 0;
            if (renderedFocus != panel)
            {
                transitionStart = Time.unscaledTime; transitioning = !reducedMotion;
                transitionPosition = viewCamera.transform.position; transitionRotation = viewCamera.transform.rotation;
                transitionFov = viewCamera.fieldOfView; transitionRect = viewCamera.rect;
                Renderer selected = closeup ? Array.Find(bindings, b => b.id == panel).renderer : null;
                for (int i = 0; i < roomRenderers.Length; i++) roomRenderers[i].enabled = closeup ? roomRenderers[i] == selected : originalVisibility[i];
                renderedFocus = panel;
            }
            Vector3 desiredPosition = closeup ? overviewPosition : savedPosition;
            Quaternion desiredRotation = closeup ? overviewRotation : savedRotation;
            if (!hasSavedCamera) { desiredPosition = overviewPosition; desiredRotation = overviewRotation; }
            if (!closeup && !transitioning) { desiredPosition = overviewPosition; desiredRotation = overviewRotation; }
            if (closeup)
            {
                Bounds bounds = Array.Find(bindings, b => b.id == panel).renderer.bounds;
                desiredRotation = Quaternion.Euler(panel == "monitor" ? 10 : 22, 164, 0);
                float size = Mathf.Max(bounds.size.y, bounds.size.x / (670f / 585f));
                float focalDistance = size * .5f / Mathf.Tan(18 * Mathf.Deg2Rad) * 1.55f;
                desiredPosition = bounds.center + desiredRotation * new Vector3(0, 0, -focalDistance);
            }
            float blend = reducedMotion ? 1 : Mathf.SmoothStep(0, 1, Mathf.Clamp01((Time.unscaledTime - transitionStart) / TransitionDuration));
            if (!transitioning) blend = 1;
            viewCamera.transform.position = Vector3.Lerp(transitionPosition, desiredPosition, blend);
            viewCamera.transform.rotation = Quaternion.Slerp(transitionRotation, desiredRotation, blend);
            viewCamera.fieldOfView = Mathf.Lerp(transitionFov, closeup ? 36 : hasSavedCamera&&savedFov > 0 ? savedFov : 40, blend);
            Rect logical = closeup ? new Rect(24, 150, 670, 585) : new Rect(0, 121.5f, 936, 648);
            Rect targetRect = new Rect((Offset.x + logical.x * Scale) / Screen.width,
                (Screen.height - Offset.y - (logical.y + logical.height) * Scale) / Screen.height,
                logical.width * Scale / Screen.width, logical.height * Scale / Screen.height);
            if (!closeup && hasSavedCamera&&savedRect.width > 0) targetRect = savedRect;
            viewCamera.rect = new Rect(Mathf.Lerp(transitionRect.x,targetRect.x,blend),Mathf.Lerp(transitionRect.y,targetRect.y,blend),Mathf.Lerp(transitionRect.width,targetRect.width,blend),Mathf.Lerp(transitionRect.height,targetRect.height,blend));
            if (blend >= 1) transitioning = false;
        }
        bool OverUi(Vector2 p) { Vector2 u = UiPoint(p); return panel.Length > 0 || u.x > 930 || u.y < 125 || u.y > 765 || resetDialog || Session.Paused; }
        void BeginPointer(Vector2 p)
        {
            tracking = !OverUi(p); dragging = false; pointerStart = pointerLast = p;
        }
        void MovePointer(Vector2 p)
        {
            if (!tracking) return;
            if (Vector2.Distance(p, pointerStart) > 8) dragging = true;
            if (dragging)
            {
                Vector2 delta = p - pointerLast;
                yaw += delta.x * .22f; pitch = Mathf.Clamp(pitch - delta.y * .15f, 18, 65); PositionCamera();
            }
            pointerLast = p;
        }
        void EndPointer(Vector2 p)
        {
            if (tracking && !dragging && Vector2.Distance(p, pointerStart) <= 8 && !OverUi(p)) Pick(p);
            tracking = false;
        }
        void Pick(Vector2 p)
        {
            if (Physics.Raycast(viewCamera.ScreenPointToRay(p), out RaycastHit hit, 100))
            {
                int idx = Array.FindIndex(bindings, b => b.collider == hit.collider);
                if (idx >= 0) { focusedObject = idx; OpenObject(idx); }
                else feedback = hit.collider.name == "AST-005-1" ? "이 모니터는 배경 업무석입니다. 번호 1의 활성 모니터를 선택하세요." : "배경 물건입니다. 모니터·복합기·뒤쪽 수납장 중 현재 단계의 물건을 선택하세요.";
            }
            else feedback = "물건의 실제 표면을 선택하세요. 드래그는 카메라를 회전합니다.";
        }

        void OpenObject(int idx)
        {
            if(transitioning||protocol.Ended||Session.Paused||panel.Length>0)return;
            int step=Array.FindIndex(Session.Data.steps,s=>s.object_id==bindings[idx].id);
            if(step>Session.StepIndex){feedback="현재 업무를 먼저 마치세요: "+Session.CurrentStep.title;return;}
            savedPosition=viewCamera.transform.position;savedRotation=viewCamera.transform.rotation;savedFov=viewCamera.fieldOfView;savedRect=viewCamera.rect;
            hasSavedCamera=true;transitioning=!reducedMotion;originalVisibility=Array.ConvertAll(roomRenderers,r=>r.enabled);panel=bindings[idx].id;scroll=Vector2.zero;feedback="";clearFocus=true;selectedItem=dragItem=-1;protocol.Open(panel);Publish();
        }
        void CloseWork()
        {
            if(panel.Length==0||transitioning)return;protocol.Close(panel);panel="";transitioning=!reducedMotion;tracking=false;selectedItem=dragItem=-1;clearFocus=true;
        }
        void TogglePause(){if(protocol.Ended)return;Session.TogglePause();tracking=false;dragItem=-1;clearFocus=true;protocol.Pause(Session.Paused);}
        void OnApplicationFocus(bool focused){if(!focused&&browserFocusedControl.Length==0){tracking=false;selectedItem=dragItem=-1;clearFocus=true;heldKey=KeyCode.None;}if(protocol!=null)protocol.SetFocus(focused||browserFocusedControl.Length>0);}
        void Escape()
        {
            if(escapeFrame==Time.frameCount)return;escapeFrame=Time.frameCount;
            if(resetDialog){resetDialog=false;pendingJob=-1;}else if(dragItem>=0||selectedItem>=0){dragItem=selectedItem=-1;}else if(jobMenu)jobMenu=false;else if(panel.Length>0)CloseWork();else TogglePause();clearFocus=true;
        }
        void Update()
        {
            if(CareerSuiteMode.Managed&&(!protocol.HasRequestedExperience||protocol.Ended))return;
            if(Session==null)return;
            bool wasBusy=Session.Busy;if(!protocol.Ended)Session.Tick(Time.deltaTime);if(wasBusy&&!Session.Busy)protocol.WorkCompleted();
            if(!protocol.Ended&&Session.Data.steps[1].kind=="print")CareerAudio.Printing(protocol.RunId,"office-ten-print",Session.Busy,Session.Paused,Session.Busy?Mathf.FloorToInt(Session.Progress*Copies()):Session.StepIndex>1?Copies():0,panel=="copier");
            if(Input.touchCount>1){tracking=false;selectedItem=dragItem=-1;clearFocus=true;}else if(Input.touchCount==1&&Input.GetTouch(0).phase==TouchPhase.Canceled){tracking=false;selectedItem=dragItem=-1;clearFocus=true;}
            if(browserFocusedControl.Length==0&&Input.GetKeyDown(KeyCode.Escape))Escape();
            if(!EditingText&&!transitioning)
            {
                if(Input.GetKeyDown(KeyCode.P))TogglePause();
                if(Input.GetKeyDown(KeyCode.R)){resetDialog=true;pendingJob=-1;}
                if(!Session.Paused&&!resetDialog&&!jobMenu&&!protocol.Ended&&panel.Length==0)
                {
                    for(int i=0;i<3;i++)if(Input.GetKeyDown((KeyCode)((int)KeyCode.Alpha1+i)))OpenObject(i);
                    float rotate=(Input.GetKey(KeyCode.RightArrow)?1:0)-(Input.GetKey(KeyCode.LeftArrow)?1:0),tilt=(Input.GetKey(KeyCode.UpArrow)?1:0)-(Input.GetKey(KeyCode.DownArrow)?1:0);
                    yaw+=rotate*Time.deltaTime*45;pitch=Mathf.Clamp(pitch+tilt*Time.deltaTime*30,18,65);float zoom=Input.mouseScrollDelta.y+(Input.GetKey(KeyCode.Equals)?Time.deltaTime*5:0)-(Input.GetKey(KeyCode.Minus)?Time.deltaTime*5:0);distance=Mathf.Clamp(distance-zoom*.3f,5,12);PositionCamera();
                    if(Input.touchCount==1){Touch t=Input.GetTouch(0);if(t.phase==TouchPhase.Began)BeginPointer(t.position);else if(t.phase==TouchPhase.Moved)MovePointer(t.position);else if(t.phase==TouchPhase.Ended)EndPointer(t.position);}
                    else if(Input.touchCount==0){if(Input.GetMouseButtonDown(0))BeginPointer(Input.mousePosition);if(Input.GetMouseButton(0))MovePointer(Input.mousePosition);if(Input.GetMouseButtonUp(0))EndPointer(Input.mousePosition);}
                }
            }
            UpdateCloseup();if(Time.unscaledTime-lastPublish>.2f){Publish();lastPublish=Time.unscaledTime;}
        }
        void Submit(int index)
        {
            if(transitioning||Session.Paused||Session.Busy||protocol.Ended||index!=Session.StepIndex)return;
            var before=Session.Snapshot();bool ok=Session.Submit(index,drafts[index],placements[index]);protocol.Action("submit",panel,before,Session.Snapshot(),ok,true);feedback=Session.Message;
            if(ok){clearFocus=true;selectedItem=dragItem=-1;}Publish();
        }
        void ChooseJob(int index)
        {
            if(index<0||index>=catalog.scenarios.Length)return;
            if(!protocol.CanSelectScenario){pendingJob=index;resetDialog=true;jobMenu=false;return;}
            Session=protocol.SelectScenario(catalog.scenarios[index],this);ClearInputs();renderedFocus="__restore";Publish();
        }
        void EnsureStyles()
        {
            if(label!=null)return;
            label=new GUIStyle(GUI.skin.label){font=koreanFont,fontSize=20,wordWrap=true,normal={textColor=new Color(.92f,.95f,.95f)}};
            small=new GUIStyle(label){fontSize=17};title=new GUIStyle(label){fontSize=28,fontStyle=FontStyle.Bold};
            input=new GUIStyle(GUI.skin.textField){font=koreanFont,fontSize=20,normal={textColor=new Color(.95f,.98f,1)},focused={textColor=new Color(.95f,.98f,1)},active={textColor=new Color(.95f,.98f,1)},hover={textColor=new Color(.95f,.98f,1)},padding=new RectOffset(10,10,6,6)};
            button=new GUIStyle(GUI.skin.button){font=koreanFont,fontSize=18,wordWrap=true};paper=new GUIStyle(label){fontSize=20,normal={textColor=new Color(.08f,.14f,.17f)}};
        }
        void Fill(Rect r,Color c){Color old=GUI.color;GUI.color=c;GUI.DrawTexture(r,Texture2D.whiteTexture);GUI.color=old;}
        void Text(Rect r,string text,GUIStyle style=null){GUI.Label(r,text,style??label);}
        Vector2 ScreenPoint(Rect r)=>Offset+r.center*Scale;
        void Btn(Rect r,string caption,Action action,bool enabled=true,string name=null,bool transparent=false)
        {
            bool old=GUI.enabled;enabled&=!transitioning;GUI.enabled=old&&enabled;name=name??"btn_"+caption;
            GUI.SetNextControlName(name);Vector2 c=ScreenPoint(r);buttonDiagnostics.Add(new ButtonDiagnostic{label=caption,x=c.x,y=c.y,enabled=GUI.enabled});
            if(GUI.enabled)nav.Add(new Nav{name=name,rect=r,action=action,context=Context});
            bool clicked=GUI.Button(r,transparent?"":caption,transparent?GUIStyle.none:button);GUI.enabled=old;if(clicked){clearFocus=true;CareerAudio.Play(protocol.RunId,"ui_click","button",cooldownMs:60);action();}
        }
        void FocusNavigation(Nav n)
        {
            if(n==null||n.context!=Context)return;
            CareerAudio.Play(protocol.RunId,"ui_focus","focus",cooldownMs:100);
            if(n.field)scroll.y=Mathf.Max(0,n.scrollY-30);
#if UNITY_WEBGL && !UNITY_EDITOR
            if(n.field){pendingBrowserFocus=n.name;return;}
#endif
            pendingGuiFocus=n.name;
        }
        // The browser owns composition, selection and caret movement. Unity receives the
        // complete draft value, scoped to the active run/work surface to reject stale blur events.
        public void OnBrowserTextInput(string json)
        {
            BrowserEdit edit;
            try{edit=JsonUtility.FromJson<BrowserEdit>(json);}catch{return;}
            if(edit==null||Session==null||edit.context!=BrowserContext)return;
            int step=Array.FindIndex(Session.Data.steps,s=>s.object_id==panel);
            if(step<0)return;
            var fields=Session.Data.steps[step].fields??Array.Empty<OfficeTenField>();
            int field=Array.FindIndex(fields,f=>"field_"+step+"_"+f.id==edit.name);
            if(field<0)return;
            bool writable=step==Session.StepIndex&&!Session.Busy&&!Session.Complete&&!Session.Paused&&!resetDialog&&!jobMenu&&!protocol.Ended;
            if(writable&&edit.kind!="focus"&&drafts[step][field]!=(edit.value??""))
            {
                drafts[step][field]=edit.value??"";protocol.Progress(edit.name,drafts[step][field],panel);
            }
            if(edit.kind=="focus")
            {
                browserFocusedControl=edit.name;browserComposing=edit.composing;clearFocus=false;pendingGuiFocus="";protocol.SetFocus(true);
            }
            else if(edit.kind=="blur")
            {
                if(browserFocusedControl==edit.name){browserFocusedControl="";browserComposing=false;}
                if(edit.reason=="window-blur"||edit.reason=="document-hidden")protocol.SetFocus(false);
            }
            else if(edit.kind=="input")browserComposing=edit.composing;
            else if(edit.kind=="escape"&&!edit.composing)Escape();
            else if(edit.kind=="tab"&&!edit.composing&&previousNav.Count>0)
            {
                int index=previousNav.FindIndex(n=>n.name==edit.name);
                FocusNavigation(previousNav[(index+(edit.backward?-1:1)+previousNav.Count)%previousNav.Count]);
            }
            UpdateMonitorDocument();Publish();
        }
        void SyncBrowserFields()
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            OfficeTenTextInputSync(JsonUtility.ToJson(new BrowserFrame{context=BrowserContext,screenWidth=Screen.width,screenHeight=Screen.height,fontSize=20*Scale,fields=browserFields.ToArray()}));
            if(browserFields.Count==0){browserFocusedControl="";browserComposing=false;}
            if(pendingBrowserFocus.Length>0){OfficeTenTextInputFocus(pendingBrowserFocus);pendingBrowserFocus="";}
#endif
        }
        void Keyboard()
        {
            if(browserFocusedControl.Length>0)return;
            Event ev=Event.current;if(ev.type==EventType.KeyUp&&(ev.keyCode==KeyCode.Return||ev.keyCode==KeyCode.KeypadEnter||ev.keyCode==KeyCode.Space))heldKey=KeyCode.None;
            if(ev.type!=EventType.KeyDown)return;
            if(ev.keyCode==KeyCode.Escape){Escape();ev.Use();return;}
            if(ev.keyCode==KeyCode.Tab&&previousNav.Count>0)
            {
                int current=previousNav.FindIndex(n=>n.name==GUI.GetNameOfFocusedControl());int next=(current+(ev.shift?-1:1)+previousNav.Count)%previousNav.Count;Nav n=previousNav[next];
                FocusNavigation(n);ev.Use();return;
            }
            if((ev.keyCode==KeyCode.Return||ev.keyCode==KeyCode.KeypadEnter||ev.keyCode==KeyCode.Space)&&!EditingText)
            {
                Nav n=previousNav.Find(x=>x.name==GUI.GetNameOfFocusedControl());if(n!=null&&n.action!=null&&n.context==Context){if(heldKey!=ev.keyCode){heldKey=ev.keyCode;n.action();}ev.Use();}
            }
        }
        void OnGUI()
        {
            if(Session==null||CareerSuiteMode.Managed&&(!protocol.HasRequestedExperience||protocol.Ended))return;EnsureStyles();Matrix4x4 oldMatrix=GUI.matrix;GUI.matrix=Matrix4x4.TRS(Offset,Quaternion.identity,new Vector3(Scale,Scale,1));
            Keyboard();if(clearFocus)
            {
                GUI.FocusControl("");GUIUtility.hotControl=0;clearFocus=false;
#if UNITY_WEBGL && !UNITY_EDITOR
                OfficeTenTextInputBlur();
#endif
                browserFocusedControl="";browserComposing=false;
            }
            nav=new List<Nav>();buttonDiagnostics.Clear();inputDiagnostics.Clear();sortDiagnostics.Clear();browserFields.Clear();
            Fill(new Rect(0,0,1440,120),new Color(.055f,.09f,.11f));Text(new Rect(24,24,570,42),Session.Data.name+" · 사무실 업무",title);
            if(!CareerSuiteMode.Managed)Btn(new Rect(620,25,155,48),"직업 선택",()=>{jobMenu=!jobMenu;},panel.Length==0&&!resetDialog);
            Btn(new Rect(790,25,180,48),Session.Paused?"계속하기 [P]":"일시정지 [P]",TogglePause,!protocol.Ended);
            Btn(new Rect(985,25,165,48),"처음부터 [R]",()=>{resetDialog=true;pendingJob=-1;},!protocol.Ended);
            Btn(new Rect(1165,25,250,48),"체험 종료",()=>{protocol.EndFromUser();EndUi();},!protocol.Ended);
            Text(new Rect(25,84,1130,30),Session.Complete?"인계 완료":Session.CurrentStep.title,small);
            if(panel.Length>0)Btn(new Rect(1195,83,220,31),"공간으로 복귀 [Esc]",CloseWork);
            if(resetDialog)DrawReset();else if(Session.Paused)DrawPause();else if(jobMenu)DrawJobs();else if(protocol.Ended)DrawEnded();else if(panel.Length>0)DrawWork();else DrawHome();
            Fill(new Rect(0,778,1440,122),new Color(.055f,.09f,.11f));Text(new Rect(24,790,1392,65),string.IsNullOrEmpty(feedback)?Session.Message:feedback);
            Text(new Rect(24,858,1392,30),"1 모니터 · 2 복합기 · 3 수납장 / 실제 물건 클릭·터치 / 방향키·드래그 회전 / +/- 확대 / Tab 초점 / Esc 복귀",small);
            if(pendingGuiFocus.Length>0){GUI.FocusControl(pendingGuiFocus);pendingGuiFocus="";}
            focusedControl=browserFocusedControl.Length>0?browserFocusedControl:GUI.GetNameOfFocusedControl();previousNav=nav;GUI.matrix=oldMatrix;
            if(Event.current.type==EventType.Repaint)SyncBrowserFields();
        }
        void DrawHome()
        {
            Fill(new Rect(956,140,465,622),new Color(.09f,.15f,.18f,.70f));Text(new Rect(978,160,420,85),Session.Data.title,title);Text(new Rect(978,248,420,180),Session.Data.request);
            for(int i=0;i<3;i++){int index=i;bool available=i<=Session.StepIndex&&!Session.Complete;Btn(new Rect(980,445+i*72,414,62),(i+1)+" · "+Session.Data.steps[i].title,()=>OpenObject(index),available||Session.Complete);}
            Btn(new Rect(980,675,414,40),"화면 움직임 줄이기: "+(reducedMotion?"켜짐":"꺼짐"),()=>reducedMotion=!reducedMotion);
            if(Session.Complete)Text(new Rect(980,720,414,35),"세 업무와 인계를 완료했습니다.",small);
        }
        void DrawJobs()
        {
            Fill(new Rect(400,145,1005,615),new Color(.09f,.15f,.18f));Text(new Rect(425,160,940,46),"체험할 사무실 직업을 선택하세요",title);
            for(int i=0;i<catalog.scenarios.Length;i++){int n=i;int col=i/5,row=i%5;Btn(new Rect(425+col*480,225+row*96,455,82),catalog.scenarios[i].name+"\n"+catalog.scenarios[i].title,()=>ChooseJob(n));}
        }
        void DrawPause()
        {
            Fill(new Rect(420,220,600,440),new Color(.09f,.15f,.18f));Text(new Rect(450,250,540,55),"잠시 멈췄습니다",title);Text(new Rect(450,320,540,90),"입력 초안·분류 배치·출력 진행은 유지합니다.");
            Btn(new Rect(450,420,540,60),"계속하기",TogglePause);Btn(new Rect(450,500,540,60),"화면 움직임 줄이기: "+(reducedMotion?"켜짐":"꺼짐"),()=>reducedMotion=!reducedMotion);
        }
        void DrawReset()
        {
            Fill(new Rect(400,240,650,350),new Color(.09f,.15f,.18f));Text(new Rect(430,265,590,110),pendingJob>=0?"현재 체험을 종료하고 다른 직업으로 전환할까요?":"현재 기록을 보존하고 처음부터 연습할까요?",title);
            Btn(new Rect(430,410,275,64),"확인",()=>{int job=pendingJob;pendingJob=-1;resetDialog=false;if(job>=0){protocol.EndFromUser();ChooseJob(job);}else{protocol.ResetRun(false);BeginExternalRun();}});
            Btn(new Rect(725,410,275,64),"취소",()=>{resetDialog=false;pendingJob=-1;});
        }
        void DrawEnded()
        {
            Fill(new Rect(500,200,880,510),new Color(.09f,.15f,.18f));Text(new Rect(530,235,810,55),"체험 기록을 보존했습니다",title);Text(new Rect(530,310,810,160),Session.Complete?"완료된 업무 결과와 처리 과정을 확인할 수 있습니다.":"완료한 부분과 남은 업무를 구분해 종료했습니다.");Btn(new Rect(530,525,810,65),"다른 직업 선택",()=>jobMenu=true);
        }
        void DrawWork()
        {
            int i=Array.FindIndex(Session.Data.steps,s=>s.object_id==panel);OfficeTenStep step=Session.Data.steps[i];bool writable=i==Session.StepIndex&&!Session.Busy&&!Session.Complete;
            Fill(new Rect(715,145,705,620),new Color(.09f,.15f,.18f,.70f));Text(new Rect(735,160,660,45),step.title,title);Text(new Rect(735,214,660,125),step.instruction,small);
            var fields=step.fields??Array.Empty<OfficeTenField>();Rect viewport=new Rect(730,345,675,345);scroll=GUI.BeginScrollView(viewport,scroll,new Rect(0,0,650,Mathf.Max(330,fields.Length*86+20)));
            for(int f=0;f<fields.Length;f++)
            {
                Text(new Rect(12,f*86,620,25),fields[f].label,small);Rect r=new Rect(12,f*86+28,610,44);string name="field_"+i+"_"+fields[f].id;GUI.SetNextControlName(name);bool old=GUI.enabled;GUI.enabled=writable;
                string value=drafts[i][f];
#if UNITY_WEBGL && !UNITY_EDITOR
                GUI.Box(r,"",input);
#else
                value=GUI.TextField(r,value,input);
#endif
                GUI.enabled=old;
                Rect global=new Rect(viewport.x+r.x,viewport.y+r.y-scroll.y,r.width,r.height);Vector2 c=ScreenPoint(global);inputDiagnostics.Add(new InputDiagnostic{name=name,value=value,x=c.x,y=c.y,enabled=writable});
                browserFields.Add(new BrowserField{name=name,label=fields[f].label,value=value,x=Offset.x+global.x*Scale,y=Offset.y+global.y*Scale,width=global.width*Scale,height=global.height*Scale,enabled=writable&&!transitioning,clipX=Offset.x+viewport.x*Scale,clipY=Offset.y+viewport.y*Scale,clipWidth=viewport.width*Scale,clipHeight=viewport.height*Scale});
                if(writable)nav.Add(new Nav{name=name,rect=global,field=true,scrollY=r.y,context=Context});
                if(value!=drafts[i][f]){drafts[i][f]=value;protocol.Progress(name,value,panel);}
            }
            GUI.EndScrollView();
            if((step.items??Array.Empty<OfficeTenItem>()).Length>0)DrawBoard(i,step,writable);
            else if(step.kind=="print")DrawPrint(i,step);
            if(Session.Busy&&i==Session.StepIndex){Fill(new Rect(740,698,650,12),new Color(.2f,.3f,.33f));Fill(new Rect(740,698,650*Session.Progress,12),new Color(.25f,.75f,.6f));}
            Btn(new Rect(740,716,650,40),i<Session.StepIndex?"✓ "+step.receipt_label:Session.Busy?"출력 중 · 중복 실행 잠금":step.kind=="print"?"최신 문서 출력 시작":step.kind=="handoff"?"보관 결과와 처리 내용 인계":"작업 내용 검토·저장",()=>Submit(i),writable);
        }

        // UI text is attached to the existing monitor display, never drawn across its bezel or stand.
        // AST-005 source Screen: center(0,-.025,.39), size(.48,.008,.28), Blender metres.
        // FBX model units are measured from its actual .54m-wide frame bounds.
        void LateUpdate(){UpdateMonitorDocument();}
        static string WrapMonitorLine(string value,int columns=36)
        {
            var b=new System.Text.StringBuilder();int col=0;
            foreach(char ch in (value??"").Replace("\r",""))
            {
                if(ch=='\n'){b.Append(ch);col=0;continue;}
                int width=ch>255?2:1;if(col+width>columns){b.Append('\n');col=0;}
                b.Append(ch);col+=width;
            }
            return b.ToString();
        }
        void UpdateMonitorDocument()
        {
            int index=Session==null?-1:Array.FindIndex(Session.Data.steps,x=>x.object_id==panel);
            bool visible=index>=0&&panel=="monitor"&&!Session.Paused&&!resetDialog&&!jobMenu&&!protocol.Ended;
            OfficeTenStep step=index>=0?Session.Data.steps[index]:null;
            visible=visible&&step!=null&&(step.items??Array.Empty<OfficeTenItem>()).Length==0&&step.kind!="print";
            if(!visible){if(monitorDocument!=null)monitorDocument.gameObject.SetActive(false);monitorPreviewFits=false;return;}
            if(monitorDocument==null)
            {
                monitorDocument=new GameObject("MonitorDocumentUI_AST-005-0").AddComponent<TextMesh>();
                monitorDocument.transform.localScale=Vector3.one*.0001f;
                monitorDocument.font=koreanFont;monitorDocument.fontSize=48;monitorDocument.characterSize=.1f;
                monitorDocument.anchor=TextAnchor.UpperLeft;monitorDocument.alignment=TextAlignment.Left;
                monitorDocument.lineSpacing=1.08f;monitorDocument.richText=false;
                monitorDocument.color=new Color(.93f,.97f,.98f,1);
                monitorDocumentRenderer=monitorDocument.GetComponent<MeshRenderer>();
                monitorDocumentRenderer.sharedMaterial=koreanFont.material;
                monitorDocumentRenderer.shadowCastingMode=UnityEngine.Rendering.ShadowCastingMode.Off;
                monitorDocumentRenderer.receiveShadows=false;
            }
            var text=new System.Text.StringBuilder();
            text.AppendLine(WrapMonitorLine(step.receipt_label));text.AppendLine("입력 미리보기");text.AppendLine();
            for(int n=0;n<(step.fields??Array.Empty<OfficeTenField>()).Length;n++)
                text.AppendLine(WrapMonitorLine(step.fields[n].label+": "+drafts[index][n]));
            string content=text.ToString().TrimEnd();
            if(monitorDocument.text!=content)
            {
                koreanFont.RequestCharactersInTexture(content,48,FontStyle.Normal);
                monitorDocument.text=content;
            }
            monitorDocument.gameObject.SetActive(true);
            Transform monitor=Array.Find(bindings,b=>b.id=="monitor").renderer.transform;
            Mesh mesh=monitor.GetComponent<MeshFilter>().sharedMesh;
            float unit=mesh.bounds.size.x/.54f;
            Vector3 normal=-monitor.up,up=monitor.forward,right=-monitor.right;
            Vector3 center=monitor.TransformPoint(new Vector3(0,-.029f,.39f)*unit)+normal*.001f;
            float width=monitor.TransformVector(Vector3.right*(.48f*unit)).magnitude;
            float height=monitor.TransformVector(Vector3.forward*(.28f*unit)).magnitude;
            Bounds glyphBounds=monitorDocumentRenderer.localBounds;
            if(glyphBounds.size.x<=.00001f||glyphBounds.size.y<=.00001f)return;
            float fit=Mathf.Min((width-.032f)/glyphBounds.size.x,(height-.024f)/glyphBounds.size.y)*.96f;
            Quaternion orientation=Quaternion.LookRotation(-normal,up);
            monitorDocument.transform.rotation=orientation;monitorDocument.transform.localScale=Vector3.one*fit;
            Vector3 topLeft=center-right*(width*.5f-.016f)+up*(height*.5f-.012f);
            monitorDocument.transform.position=topLeft-orientation*(new Vector3(glyphBounds.min.x,glyphBounds.max.y,0)*fit);
            monitorPreviewCorners=new Vector3[4];monitorPreviewFits=true;int c=0;
            foreach(float x in new[]{glyphBounds.min.x,glyphBounds.max.x})
                foreach(float y in new[]{glyphBounds.min.y,glyphBounds.max.y})
                {
                    Vector3 point=monitorDocument.transform.TransformPoint(new Vector3(x,y,0));monitorPreviewCorners[c++]=point;
                    Vector3 d=point-center;
                    monitorPreviewFits&=Mathf.Abs(Vector3.Dot(d,right))<=width*.5f&&Mathf.Abs(Vector3.Dot(d,up))<=height*.5f;
                }
        }
        int Copies()
        {
            var s=Session.Data.steps[1];int f=Array.FindIndex(s.fields,x=>x.id=="copies");return f>=0&&int.TryParse(drafts[1][f],out int n)?Mathf.Clamp(n,1,5):1;
        }
        void SelectPrintValue(string fieldId,string value)
        {
            int index=Array.FindIndex(Session.Data.steps[1].fields,f=>f.id==fieldId);
            if(index<0||Session.StepIndex!=1||Session.Busy||Session.Paused||protocol.Ended)return;
            drafts[1][index]=value;protocol.Progress("field_1_"+fieldId,value,"copier");
        }
        void DrawPrint(int i,OfficeTenStep step)
        {
            bool editable=Session.StepIndex==1&&!Session.Busy&&!Session.Paused&&!Session.Complete;
            Text(new Rect(45,225,625,36),"복합기 자료·버전 목록",small);
            Btn(new Rect(45,268,300,40),"저장 문서: "+Session.Data.steps[0].work_item_id,()=>SelectPrintValue("document_id",Session.Data.steps[0].work_item_id),editable);
            Btn(new Rect(360,268,300,40),"이전 초안: OLD-DRAFT",()=>SelectPrintValue("document_id","OLD-DRAFT"),editable);
            Btn(new Rect(45,316,300,40),"최신 저장본 r"+Session.DocumentRevision,()=>SelectPrintValue("revision",Session.DocumentRevision.ToString()),editable);
            Btn(new Rect(360,316,300,40),"초기 초안 r0",()=>SelectPrintValue("revision","0"),editable);
            int count=Copies();float done=Session.Busy?Session.Progress*count:i<Session.StepIndex?count:0;
            for(int n=0;n<count;n++)
            {
                if(n>=done&&Session.Busy)break;Rect sheet=new Rect(65+n*15,365+n*38,560,235);Fill(sheet,new Color(1,.98f,.9f));Text(new Rect(sheet.x+18,sheet.y+18,525,75),Session.Data.steps[0].receipt_label,paper);Text(new Rect(sheet.x+18,sheet.y+100,525,75),"문서 r"+Session.DocumentRevision+" · "+(n+1)+" / "+count+"부",paper);Text(new Rect(sheet.x+18,sheet.y+175,525,45),i<Session.StepIndex?"✓ 출력 완료":Session.Busy?"용지 배출 중":"출력 미리보기",paper);
            }
        }
        void MoveItem(int step,int item,string destination)
        {
            if(Session.Paused||Session.Busy||step!=Session.StepIndex||protocol.Ended)return;
            placementInput=Session.Data.steps[step].items[item].id+" → "+destination;
            var before=Session.Snapshot();bool ok=Session.TryPlace(step,item,destination);
            if(ok)placements[step][item]=destination;
            protocol.Action("place_item",panel,before,Session.Snapshot(),ok,true,Session.Data.steps[step].items[item].id);feedback=Session.Message;selectedItem=dragItem=-1;Publish();
        }
        void DrawBoard(int stepIndex,OfficeTenStep step,bool writable)
        {
            var items=step.items??Array.Empty<OfficeTenItem>();var destinations=step.destinations??Array.Empty<string>();
            Fill(new Rect(30,352,655,395),new Color(.13f,.20f,.22f));Text(new Rect(45,361,620,40),step.kind=="schedule"?"일정 카드 → 시간 슬롯":"문서·항목 → 분류 칸",small);
            Event ev=Event.current;Rect[] source=new Rect[items.Length],bins=new Rect[destinations.Length];
            for(int d=0;d<destinations.Length;d++)
            {
                int di=d;bins[d]=new Rect(375,410+d*100,292,90);Fill(bins[d],new Color(.75f,.86f,.8f));Text(new Rect(bins[d].x+12,bins[d].y+5,268,30),destinations[d],paper);
                var stored=items.Select((x,j)=>new{item=x,j}).Where(x=>placements[stepIndex][x.j]==destinations[d]);Text(new Rect(bins[d].x+12,bins[d].y+36,268,50),string.Join(" · ",stored.Select(x=>x.item.label)),paper);
                Vector2 c=ScreenPoint(bins[d]);sortDiagnostics.Add(new SortDiagnostic{id=destinations[d],label=destinations[d],kind="destination",x=c.x,y=c.y});
                if(writable){int chosen=selectedItem;Btn(new Rect(bins[d].x,bins[d].y,292,90),"이동: "+destinations[d],()=>{if(selectedItem>=0)MoveItem(stepIndex,selectedItem,destinations[di]);},true,"bin_"+d,true);}
            }
            for(int j=0;j<items.Length;j++)
            {
                int item=j;source[j]=new Rect(45,410+j*100,300,88);Fill(source[j],selectedItem==j?new Color(.98f,.87f,.52f):new Color(1,.98f,.9f));Text(new Rect(source[j].x+9,source[j].y+9,282,67),items[j].label+(placements[stepIndex][j]==null?"":"\n→ "+placements[stepIndex][j]),paper);
                Vector2 c=ScreenPoint(source[j]);sortDiagnostics.Add(new SortDiagnostic{id=items[j].id,label=items[j].label,kind="item",x=c.x,y=c.y});
                if(writable&&ev.rawType==EventType.MouseDown&&source[j].Contains(ev.mousePosition)){CareerAudio.Play(protocol.RunId,"drag_pick");selectedItem=dragItem=j;dragStart=ev.mousePosition;GUI.FocusControl("item_"+j);ev.Use();}
                if(writable)Btn(source[j],"항목 선택: "+items[j].label,()=>{CareerAudio.Play(protocol.RunId,"drag_pick");selectedItem=item;},true,"item_"+j,true);
            }
            if(writable&&ev.rawType==EventType.MouseUp&&dragItem>=0)
            {
                int original=dragItem;for(int d=0;d<bins.Length;d++)if(bins[d].Contains(ev.mousePosition)){MoveItem(stepIndex,original,destinations[d]);break;}dragItem=-1;ev.Use();
            }
            if(writable&&dragItem>=0&&ev.type==EventType.Repaint&&Vector2.Distance(ev.mousePosition,dragStart)*Scale>8){Fill(new Rect(ev.mousePosition.x-40,ev.mousePosition.y-16,150,45),new Color(.98f,.87f,.52f));Text(new Rect(ev.mousePosition.x-34,ev.mousePosition.y-12,138,38),items[dragItem].label,paper);}
        }
        public DiagnosticState Diagnostic()
        {
            var targets=bindings.Select(b=>{var p=viewCamera.WorldToScreenPoint(b.renderer.bounds.center);return new TargetDiagnostic{id=b.id,x=p.x,y=Screen.height-p.y};}).ToArray();var palette=roomRenderers.Select(r=>r.sharedMaterial?.mainTexture).FirstOrDefault(t=>t!=null);
            return new DiagnosticState{browserInputFocused=browserFocusedControl.Length>0,browserInputComposing=browserComposing,monitorPreviewVisible=monitorDocument!=null&&monitorDocument.gameObject.activeSelf,monitorPreviewFits=monitorPreviewFits,monitorPreviewText=monitorDocument==null?"":monitorDocument.text,monitorPreviewCornersWorld=monitorPreviewCorners,scenarioId=Session.Data.scenario_id,scenarioVersion=Session.Data.version,occupationId=Session.Data.occupation_id,name=Session.Data.name,panel=panel,feedback=feedback,session=Session.Snapshot(),targets=targets,buttons=buttonDiagnostics.ToArray(),inputs=inputDiagnostics.ToArray(),sorting=sortDiagnostics.ToArray(),interactiveObjects=bindings.Length,triangles=roomRenderers.Sum(r=>r.GetComponent<MeshFilter>()?.sharedMesh?.triangles.Length/3??0),visibleRenderers=roomRenderers.Count(r=>r.enabled),paletteWidth=palette?.width??0,paletteHeight=palette?.height??0,reducedMotion=reducedMotion,transitionSeconds=TransitionDuration,work=Session.Data.steps.Select((s,i)=>new StepDiagnostic{stepId=s.step_id,values=drafts[i],placements=placements[i]}).ToArray(),selectedItem=selectedItem,renderedCompletedSheets=panel=="copier"&&!Session.Paused&&!resetDialog&&!jobMenu&&!protocol.Ended&&Session.StepIndex>1?Copies():0,runId=protocol.RunId,experienceId=protocol.ExperienceId,focusedControl=focusedControl,viewState=Session.Paused?"paused":transitioning?(panel.Length>0?"focusing":"returning"):panel.Length>0?"working":"exploring",cameraPosition=viewCamera.transform.position,cameraRotation=viewCamera.transform.rotation,cameraRect=viewCamera.rect,cameraFov=viewCamera.fieldOfView};
        }
        void Publish()
        {
            string json=JsonUtility.ToJson(Diagnostic());
#if UNITY_WEBGL && !UNITY_EDITOR
            PublishOfficeState(json);
#else
            if(Time.unscaledTime-lastPublish>.25f)Debug.Log("OFFICE_TEN_STATE "+json);
#endif
        }
    }
}

using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using UnityEngine;

namespace CareerExperience
{
    public sealed class OfficeDirectExperience : MonoBehaviour
    {
        public TextAsset scenario;
        public Font koreanFont;
        public Camera viewCamera;
        public OfficeBinding[] bindings;
        public OfficeSession Session { get; private set; }
        string panel = "", feedback = "", selectedFile;
        int copies = 1, selectedRevision, focusedObject, focusedAction, actionIndex;
        string draftDate, draftTitle, handoffDate, handoffTitle, handoffFolder;
        int handoffCopies = 1;
        bool resetDialog;
        public bool reducedMotion;
        [Min(.05f)] public float transitionSeconds = .45f;
        float TransitionDuration => float.IsNaN(transitionSeconds)||float.IsInfinity(transitionSeconds)||transitionSeconds<=0?.45f:Mathf.Clamp(transitionSeconds,.05f,5f);
        CareerProtocol protocol;
        string copiesInput = "1", handoffCopiesInput = "1";
        bool bundleSelected, bundleDragging, transitioning;
        int binFocus;
        float transitionStart;
        Vector3 transitionPosition, savedPosition;
        Quaternion transitionRotation, savedRotation;
        float transitionFov, savedFov;
        Rect transitionRect, savedRect;
        GUIStyle inputStyle;
        bool editingText, clearGuiFocus, cancelGuiGesture, copierOpened,hasSavedCamera;
        bool EditingText => editingText;
        int escapeHandledFrame=-1;
        string keyboardFocusAnchor,keyboardFocusSchema,focusedControlName;
        string actionsContext;
        KeyCode heldSubmitKey=KeyCode.None;
        string UiContext=>panel+"|"+Session.Stage+"|"+Session.Paused+"|"+resetDialog+"|"+protocol.Ended;
        bool drawingScroll;
        Rect scrollClipScreen;
        readonly List<Action> actions = new List<Action>();
        Vector2 pointerStart, pointerLast;
        bool tracking, dragging;
        float yaw = 152, pitch = 34, distance = 9.7f, lastPublish;
        Vector3 overviewPosition;
        Quaternion overviewRotation;
        Renderer[] roomRenderers;
        bool[] originalVisibility;
        string renderedFocus = "";
        bool paperMode;
        GUIStyle paperBody, paperSmall, paperHeading, paperButton;
        GUIStyle titleStyle, labelStyle, bodyStyle, smallStyle, buttonStyle, headingStyle, targetStyle;
        Vector2 scroll;
        float Scale => Mathf.Min(Screen.width / 1440f, Screen.height / 900f);
        Vector2 Offset => new Vector2((Screen.width - 1440 * Scale) / 2, (Screen.height - 900 * Scale) / 2);
        Vector2 UiPoint(Vector2 screen) => (new Vector2(screen.x, Screen.height - screen.y) - Offset) / Scale;
        Vector2 LayoutScreenPoint(Vector2 point)
        {
            // Nested GUILayout clips keep logical origins. Apply the root scale
            // once to the full unclipped point, including those origins.
            Matrix4x4 matrix=GUI.matrix;
            GUI.matrix=Matrix4x4.identity;
            Vector2 logical=GUIUtility.GUIToScreenPoint(point);
            GUI.matrix=matrix;
            return matrix.MultiplyPoint3x4(logical);
        }
        [DllImport("__Internal")] static extern void PublishOfficeState(string json);
        [DllImport("__Internal")] static extern void PublishOfficeTests(string json);
        [Serializable] public class TargetDiagnostic { public string id; public float x, y; }
        [Serializable] public class ButtonDiagnostic { public string label; public float x, y; public bool enabled,insideScroll; }
        readonly List<ButtonDiagnostic> buttonDiagnostics = new List<ButtonDiagnostic>();
        [Serializable] public class InputDiagnostic { public string name,value; public float x,y; public bool enabled; }
        [Serializable] public class SortDiagnostic { public string name; public float x,y; }
        readonly List<InputDiagnostic> inputDiagnostics=new List<InputDiagnostic>();
        readonly List<SortDiagnostic> sortDiagnostics=new List<SortDiagnostic>();
        [Serializable] public class RuntimeDiagnostic { public OfficeSnapshot session; public string panel, feedback,runId,experienceId,viewState,focusedControl,storedBin; public int focusedObject,focusedAction,renderedCompletedSheets; public TargetDiagnostic[] targets; public ButtonDiagnostic[] buttons; public InputDiagnostic[] inputs; public SortDiagnostic[] sorting; public int triangles, interactiveObjects, visibleRenderers,paletteWidth,paletteHeight; public string unity; public bool closeup,reducedMotion; public float cameraDistance,transitionSeconds; public Vector3 cameraPosition; public Quaternion cameraRotation; public Rect cameraRect,scrollClip; public float cameraFov; }
        sealed class KeyboardControl { public string name;public int action;public float x,y; }
        sealed class CachedUi
        {
            public string run,draftDate,draftTitle,selectedFile,copiesInput,handoffTitle,handoffDate,handoffFolder,handoffCopiesInput;
            public int selectedRevision,binFocus; public float yaw,pitch,distance; public bool copierOpened,reducedMotion;
        }
        static CachedUi cachedUi;
        void Awake()
        {
            gameObject.name = "OfficeExperience";
            protocol = CareerProtocol.Get();
            Session = protocol.Attach(JsonUtility.FromJson<OfficeData>(scenario.text), this);
            roomRenderers = bindings[0].renderer.transform.parent.GetComponentsInChildren<Renderer>();
            originalVisibility = Array.ConvertAll(roomRenderers, r => r.enabled);
            ClearInputs();
            if(cachedUi!=null&&cachedUi.run==protocol.RunId)
            {
                draftDate=cachedUi.draftDate;draftTitle=cachedUi.draftTitle;selectedFile=cachedUi.selectedFile;copiesInput=cachedUi.copiesInput;
                handoffTitle=cachedUi.handoffTitle;handoffDate=cachedUi.handoffDate;handoffFolder=cachedUi.handoffFolder;handoffCopiesInput=cachedUi.handoffCopiesInput;
                selectedRevision=cachedUi.selectedRevision;binFocus=cachedUi.binFocus;yaw=cachedUi.yaw;pitch=cachedUi.pitch;distance=cachedUi.distance;copierOpened=cachedUi.copierOpened;reducedMotion=cachedUi.reducedMotion;
            }
            PositionCamera(true);
        }
        void OnDestroy()
        {
            if(protocol==null||Session==null)return;
            cachedUi=new CachedUi{run=protocol.RunId,draftDate=draftDate,draftTitle=draftTitle,selectedFile=selectedFile,copiesInput=copiesInput,
                handoffTitle=handoffTitle,handoffDate=handoffDate,handoffFolder=handoffFolder,handoffCopiesInput=handoffCopiesInput,
                selectedRevision=selectedRevision,binFocus=binFocus,yaw=yaw,pitch=pitch,distance=distance,copierOpened=copierOpened,reducedMotion=reducedMotion};
            protocol.Detach(this);
        }
        void ClearInputs()
        {
            panel = ""; feedback = ""; copies = handoffCopies = 1; selectedFile = Session.Data.document_id;
            selectedRevision = Session.SavedRevision; draftDate = Session.Date; draftTitle = Session.Title;
            handoffTitle = Session.Data.document_title; handoffDate = Session.Data.initial_date; handoffFolder = "인사자료";
            copiesInput = handoffCopiesInput = "1"; bundleSelected = bundleDragging = false; binFocus = 0;
            copierOpened=false;clearGuiFocus=cancelGuiGesture=true;
            focusedAction = focusedObject = 0; scroll = Vector2.zero; tracking = dragging = false;
            keyboardFocusAnchor=keyboardFocusSchema=null;
            heldSubmitKey=KeyCode.None;
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
            if (transitioning || protocol.Ended||panel.Length>0) return;
            string id = bindings[idx].id;
            if (id == "monitor" || Session.Stage == OfficeStage.complete || id == "copier" && Session.Stage >= OfficeStage.print_ready || Session.SelectObject(id))
            {
                savedPosition = viewCamera.transform.position; savedRotation = viewCamera.transform.rotation;
                savedFov = viewCamera.fieldOfView; savedRect = viewCamera.rect;
                hasSavedCamera=true;transitioning=!reducedMotion;
                originalVisibility = Array.ConvertAll(roomRenderers, r => r.enabled);
                panel = bindings[idx].id; feedback = ""; focusedAction = 0; scroll = Vector2.zero;
                if(id=="copier"&&!copierOpened){selectedRevision=Session.SavedRevision;copierOpened=true;}
                protocol.Open(id);
            }
            else { feedback = Session.Message; }
            Publish();
        }
        void Result(bool ok)
        {
            feedback = Session.Message;
            if (ok && Session.Stage == OfficeStage.request_pending) { panel = "monitor"; focusedAction = 0; }
            Publish();
        }
        void Perform(string action, Func<bool> command, bool attempt = true)
        {
            if (transitioning || protocol.Ended || Session.Paused) return;
            OfficeSnapshot before = Session.Snapshot(); bool ok = command();
            protocol.Action(action, panel, before, Session.Snapshot(), ok, attempt);
            if(ok&&attempt){clearGuiFocus=true;editingText=false;}
            Result(ok);
        }
        void CloseWork()
        {
            if (panel.Length == 0 || transitioning) return;
            protocol.Close(panel); panel = ""; feedback = "";
            transitioning=!reducedMotion;
            bundleDragging = false; tracking = false; clearGuiFocus=cancelGuiGesture=true;
        }
        void TogglePause()
        {
            if (protocol.Ended) return;
            Session.TogglePause(); tracking = bundleDragging = false; clearGuiFocus=cancelGuiGesture=true;protocol.Pause(Session.Paused);
        }
        void OnApplicationFocus(bool focused)
        {
            if (!focused) { tracking = bundleDragging = false; heldSubmitKey=KeyCode.None;cancelGuiGesture=true; }
            if (protocol != null) protocol.SetFocus(focused);
        }
        void HandleEscape()
        {
            if(escapeHandledFrame==Time.frameCount)return;
            escapeHandledFrame=Time.frameCount;
            if(resetDialog)resetDialog=false;
            else if(bundleDragging||bundleSelected){bundleDragging=bundleSelected=false;cancelGuiGesture=true;}
            else if(panel.Length>0)CloseWork();
            else TogglePause();
        }
        void Update()
        {
            if(CareerSuiteMode.Managed&&(!protocol.HasRequestedExperience||protocol.Ended))return;
            OfficeStage beforeTick = Session.Stage;
            if (!protocol.Ended) Session.Tick(Time.deltaTime);
            if (beforeTick == OfficeStage.printing && Session.Stage == OfficeStage.print_ready) protocol.PrintCompleted();
            if(!protocol.Ended)CareerAudio.Printing(protocol.RunId,"office-direct-print-"+Session.RequestRevision+"-"+Session.SavedRevision,Session.Stage==OfficeStage.printing,Session.Paused,Session.Stage==OfficeStage.printing?Mathf.FloorToInt(Session.PrintProgress*Session.PrintedCopies):Session.PrintCompletions>0?Session.PrintedCopies:0,panel=="copier");
            if (transitioning) { UpdateCloseup(); Publish(); return; }
            if (Input.GetKeyDown(KeyCode.Escape))
            {
                HandleEscape();
            }
            if (!EditingText && Input.GetKeyDown(KeyCode.P)) { TogglePause(); focusedAction = 0; }
            if (!EditingText && Input.GetKeyDown(KeyCode.R)) { resetDialog = true; focusedAction = 0; }
            if (!Session.Paused && !resetDialog && !protocol.Ended && !EditingText)
            {
                if (Input.GetKeyDown(KeyCode.Alpha1)) { CloseWork(); focusedObject = 0; }
                if (Input.GetKeyDown(KeyCode.Alpha2)) { CloseWork(); focusedObject = 1; }
                if (Input.GetKeyDown(KeyCode.Alpha3)) { CloseWork(); focusedObject = 2; }
                if (panel.Length == 0)
                {
                    if (Input.GetKeyDown(KeyCode.Tab)) focusedObject = (focusedObject + 1) % bindings.Length;
                    if (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.Space)) OpenObject(focusedObject);
                    float rotate = (Input.GetKey(KeyCode.RightArrow) ? 1 : 0) - (Input.GetKey(KeyCode.LeftArrow) ? 1 : 0);
                    float tilt = (Input.GetKey(KeyCode.UpArrow) ? 1 : 0) - (Input.GetKey(KeyCode.DownArrow) ? 1 : 0);
                    yaw += rotate * Time.deltaTime * 45; pitch = Mathf.Clamp(pitch + tilt * Time.deltaTime * 30, 18, 65);
                    if (rotate != 0 || tilt != 0) PositionCamera();
                    float zoom = Input.mouseScrollDelta.y + (Input.GetKey(KeyCode.Equals) ? Time.deltaTime * 5 : 0) - (Input.GetKey(KeyCode.Minus) ? Time.deltaTime * 5 : 0);
                    if (zoom != 0) { distance = Mathf.Clamp(distance - zoom * .3f, 5, 12); PositionCamera(); }
                }
                if (Input.touchCount > 0)
                {
                    Touch t = Input.GetTouch(0);
                    if (Input.touchCount > 1) { tracking = bundleDragging=false;cancelGuiGesture=true; }
                    else if (t.phase == TouchPhase.Began) BeginPointer(t.position);
                    else if (t.phase == TouchPhase.Moved) MovePointer(t.position);
                    else if (t.phase == TouchPhase.Ended) EndPointer(t.position);
                    else if (t.phase == TouchPhase.Canceled) {tracking = bundleDragging=false;cancelGuiGesture=true;}
                }
                else
                {
                    if (Input.GetMouseButtonDown(0)) BeginPointer(Input.mousePosition);
                    if (Input.GetMouseButton(0)) MovePointer(Input.mousePosition);
                    if (Input.GetMouseButtonUp(0)) EndPointer(Input.mousePosition);
                }
            }
            UpdateCloseup();
            if (Time.unscaledTime - lastPublish > .25f) { Publish(); lastPublish = Time.unscaledTime; }
        }
        void KeyboardActions()
        {
            Event ev=Event.current;
            if(transitioning||ev.type!=EventType.KeyDown||actionsContext!=UiContext)return;
            if(ev.keyCode==KeyCode.Tab)
            {
                bool paper=panel.Length>0&&!Session.Paused&&!resetDialog;
                Rect logical=paper?new Rect(786,197,556,535):new Rect(958,143,426,593);
                Rect visible=new Rect(Offset.x+logical.x*Scale,Offset.y+logical.y*Scale,logical.width*Scale,logical.height*Scale);
                var controls=new List<KeyboardControl>();
                foreach(var field in inputDiagnostics)
                    if(field.enabled&&visible.Contains(new Vector2(field.x,field.y))&&scrollClipScreen.Contains(new Vector2(field.x,field.y)))
                        controls.Add(new KeyboardControl{name="input-"+field.name,action=-1,x=field.x,y=field.y});
                int action=0;
                foreach(var button in buttonDiagnostics)
                {
                    if(!button.enabled)continue;
                    if(visible.Contains(new Vector2(button.x,button.y))&&(!button.insideScroll||scrollClipScreen.Contains(new Vector2(button.x,button.y))))
                        controls.Add(new KeyboardControl{name="button-"+action,action=action,x=button.x,y=button.y});
                    action++;
                }
                controls.Sort((a,b)=>Mathf.Abs(a.y-b.y)>2?a.y.CompareTo(b.y):a.x.CompareTo(b.x));
                if(controls.Count==0)return;
                string schema=string.Join("|",controls.ConvertAll(c=>c.name));
                if(schema!=keyboardFocusSchema){keyboardFocusSchema=schema;keyboardFocusAnchor=null;}
                string current=GUI.GetNameOfFocusedControl();
                int index=controls.FindIndex(c=>c.name==current);
                if(index<0&&keyboardFocusAnchor!=null)index=controls.FindIndex(c=>c.name==keyboardFocusAnchor);
                if(index<0)index=ev.shift?0:-1;
                KeyboardControl next=controls[(index+(ev.shift?-1:1)+controls.Count)%controls.Count];
                keyboardFocusAnchor=next.name;
                if(next.action<0){GUI.FocusControl(next.name);editingText=true;}
                else{GUI.FocusControl(null);editingText=false;focusedAction=next.action;}
                ev.Use();return;
            }
            if(actions.Count==0||EditingText)return;
            if(ev.keyCode==KeyCode.DownArrow){focusedAction=(focusedAction+1)%actions.Count;keyboardFocusAnchor="button-"+focusedAction;ev.Use();}
            else if(ev.keyCode==KeyCode.UpArrow){focusedAction=(focusedAction+actions.Count-1)%actions.Count;keyboardFocusAnchor="button-"+focusedAction;ev.Use();}
            else if(ev.keyCode==KeyCode.Return||ev.keyCode==KeyCode.Space)
            {
                if(heldSubmitKey!=ev.keyCode){heldSubmitKey=ev.keyCode;actions[Mathf.Clamp(focusedAction,0,actions.Count-1)]();}
                ev.Use();
            }
        }
        public RuntimeDiagnostic Diagnostic()
        {
            var targets = new TargetDiagnostic[bindings.Length];
            for (int i = 0; i < targets.Length; i++)
            {
                Vector3 p = viewCamera.WorldToScreenPoint(bindings[i].renderer.bounds.center);
                targets[i] = new TargetDiagnostic { id = bindings[i].id, x = p.x, y = Screen.height - p.y };
            }
            int triangles = 0;
            foreach (MeshFilter m in FindObjectsByType<MeshFilter>(FindObjectsSortMode.None)) triangles += m.sharedMesh.triangles.Length / 3;
            Texture palette=bindings[0].renderer.sharedMaterial.mainTexture;
            return new RuntimeDiagnostic { session = Session.Snapshot(), panel = panel, feedback = feedback, targets = targets,
                focusedObject = focusedObject, focusedAction=focusedAction,focusedControl=focusedControlName,scrollClip=scrollClipScreen,triangles = triangles, interactiveObjects = bindings.Length, unity = Application.unityVersion, buttons = buttonDiagnostics.ToArray(),
                visibleRenderers = Array.FindAll(roomRenderers, r => r.enabled).Length, closeup = panel.Length > 0,
                runId=protocol.RunId,experienceId=protocol.ExperienceId,viewState=Session.Paused?"paused":transitioning?(panel.Length>0?"focusing":"returning"):panel.Length>0?"working":"exploring",
                inputs=inputDiagnostics.ToArray(),sorting=sortDiagnostics.ToArray(),cameraPosition=viewCamera.transform.position,cameraRotation=viewCamera.transform.rotation,cameraRect=viewCamera.rect,cameraFov=viewCamera.fieldOfView,
                paletteWidth=palette==null?0:palette.width,paletteHeight=palette==null?0:palette.height,
                reducedMotion=reducedMotion,transitionSeconds=TransitionDuration,
                renderedCompletedSheets=panel=="copier"&&!Session.Paused&&!resetDialog&&Session.PrintCompletions>0?Session.PrintedCopies:0,
                storedBin=panel=="cabinet"&&!Session.Paused&&!resetDialog?Session.Folder:null,
                cameraDistance = panel.Length > 0 ? Vector3.Distance(viewCamera.transform.position, Array.Find(bindings, b => b.id == panel).renderer.bounds.center) : distance };
        }
        void Publish()
        {
#if UNITY_WEBGL && !UNITY_EDITOR
            PublishOfficeState(JsonUtility.ToJson(Diagnostic()));
#endif
        }
        // Read-only acceptance entry point; it creates independent sessions and never advances the player.
        public void RunAcceptanceSuite(string unused)
        {
            string result = JsonUtility.ToJson(OfficeAcceptance.Run(Session.Data));
            Debug.Log("OFFICE_ACCEPTANCE " + result);
#if UNITY_WEBGL && !UNITY_EDITOR
            PublishOfficeTests(result);
#endif
        }
        void Styles()
        {
            if (titleStyle != null) return;
            GUI.skin.font = koreanFont;
            titleStyle = new GUIStyle(GUI.skin.label) { fontSize = 30, fontStyle = FontStyle.Bold, normal = { textColor = new Color(.94f, .96f, .97f) } };
            headingStyle = new GUIStyle(titleStyle) { fontSize = 23 };
            labelStyle = new GUIStyle(GUI.skin.label) { fontSize = 18, wordWrap = true, normal = { textColor = new Color(.90f, .93f, .94f) } };
            bodyStyle = new GUIStyle(labelStyle) { fontSize = 19 };
            smallStyle = new GUIStyle(labelStyle) { fontSize = 15, normal = { textColor = new Color(.66f, .75f, .78f) } };
            targetStyle = new GUIStyle(labelStyle) { fontSize = 16, fontStyle = FontStyle.Bold, normal = { textColor = Color.white } };
            buttonStyle = new GUIStyle(GUI.skin.button) { fontSize = 17, alignment = TextAnchor.MiddleLeft, padding = new RectOffset(15, 12, 7, 7), wordWrap = true };
            paperBody = new GUIStyle(bodyStyle) { normal = { textColor = new Color(.035f, .065f, .08f) } };
            paperSmall = new GUIStyle(smallStyle) { normal = { textColor = new Color(.10f, .16f, .19f) } };
            paperHeading = new GUIStyle(headingStyle) { normal = { textColor = new Color(.035f, .065f, .08f) } };
            paperButton = new GUIStyle(buttonStyle);
            paperButton.normal.background = Texture2D.whiteTexture; paperButton.hover.background = Texture2D.whiteTexture; paperButton.active.background = Texture2D.whiteTexture;
            paperButton.normal.textColor = paperButton.hover.textColor = paperButton.active.textColor = new Color(.025f, .06f, .075f);
        }
        void Fill(Rect rect, Color color) { Color c = GUI.color; GUI.color = color; GUI.DrawTexture(rect, Texture2D.whiteTexture); GUI.color = c; }
        bool Button(string text, Action action, bool enabled = true)
        {
            enabled=enabled&&GUI.enabled&&!transitioning;
            int index = actionIndex++;
            if (Event.current.type == EventType.Repaint && enabled) actions.Add(action);
            // Disabled buttons do not consume keyboard navigation indices.
            int focusIndex = enabled ? enabledButtonCount++ : -1;
            bool old = GUI.enabled; GUI.enabled = enabled;
            bool keyboardMenu = panel.Length > 0 || Session.Paused || resetDialog;
            Color oldBg = GUI.backgroundColor; GUI.backgroundColor = focusIndex == focusedAction && keyboardMenu ? new Color(.34f, .73f, .60f) : paperMode ? new Color(.73f, .82f, .81f) : new Color(.27f, .39f, .43f);
            bool clicked = GUILayout.Button((focusIndex == focusedAction && keyboardMenu ? "› " : "") + text, paperMode ? paperButton : buttonStyle, GUILayout.MinHeight(43));
            if (Event.current.type == EventType.Repaint)
            {
                Vector2 point = LayoutScreenPoint(GUILayoutUtility.GetLastRect().center);
                buttonDiagnostics.Add(new ButtonDiagnostic { label = text, x = point.x, y = point.y, enabled = enabled,insideScroll=drawingScroll });
            }
            GUI.backgroundColor = oldBg; GUI.enabled = old;
            if (clicked){CareerAudio.Play(protocol.RunId,"ui_click","button",cooldownMs:60);focusedAction=focusIndex;keyboardFocusAnchor="button-"+focusIndex;action();}
            return clicked;
        }
        int enabledButtonCount;
        void Label(string text, GUIStyle style = null)
        {
            if (paperMode) style = style == smallStyle ? paperSmall : style == headingStyle ? paperHeading : paperBody;
            GUILayout.Label(text, style ?? bodyStyle);
        }
        void OnGUI()
        {
            if (Session == null||CareerSuiteMode.Managed&&(!protocol.HasRequestedExperience||protocol.Ended)) return;
            Styles();
            if(Event.current.type==EventType.KeyUp&&Event.current.keyCode==heldSubmitKey)heldSubmitKey=KeyCode.None;
            if(clearGuiFocus){GUI.FocusControl(null);clearGuiFocus=false;editingText=false;}
            if(cancelGuiGesture){GUIUtility.hotControl=0;cancelGuiGesture=false;}
            if(Event.current.type==EventType.KeyDown&&Event.current.keyCode==KeyCode.Escape&&!transitioning){HandleEscape();Event.current.Use();}
            if(!(panel=="cabinet"&&Session.Stage==OfficeStage.print_ready)&&(panel.Length>0||Session.Paused||resetDialog||protocol.Ended))KeyboardActions();
            Matrix4x4 oldMatrix = GUI.matrix;
            GUI.matrix = Matrix4x4.TRS(Offset, Quaternion.identity, Vector3.one * Scale);
            actionIndex = enabledButtonCount = 0;
            drawingScroll=false;
            if (Event.current.type == EventType.Repaint) { actionsContext=UiContext;actions.Clear(); buttonDiagnostics.Clear();inputDiagnostics.Clear();sortDiagnostics.Clear(); }
            Fill(new Rect(0, 0, 1440, 112), new Color(.055f, .10f, .13f));
            GUI.Label(new Rect(32, 17, 930, 44), "OFFICE / 사무보조원의 하루", titleStyle);
            GUI.Label(new Rect(34, 64, 900, 35), "01 요청 확인   →   02 문서 검토   →   03 출력   →   04 보관·인계", labelStyle);
            if(GUI.Button(new Rect(974,29,120,48),"도움 요청",buttonStyle)&&!protocol.Ended)feedback=protocol.RequestHelp();
            if (GUI.Button(new Rect(1112, 29, 120, 48), Session.Paused ? "계속하기 [P]" : "일시정지 [P]", buttonStyle)) TogglePause();
            if (GUI.Button(new Rect(1244, 29, 164, 48), "전체 초기화 [R]", buttonStyle)){resetDialog=true;clearGuiFocus=true;}
            paperMode = panel.Length > 0 && !Session.Paused && !resetDialog;
            if (panel.Length == 0) DrawTargets();
            if (paperMode) DrawCloseupPresentation();
            else Fill(new Rect(934, 125, 474, 635), new Color(.07f, .13f, .16f));
            GUILayout.BeginArea(paperMode ? new Rect(786, 197, 556, 535) : new Rect(958, 143, 426, 593));
            if (protocol.Ended) { Label("체험 종료 기록을 보존했습니다.", headingStyle); Label(protocol.EndSummary, smallStyle); Button("새 연습 시작", () => Reset(false)); }
            else if (Session.Paused) DrawPause();
            else if (resetDialog) DrawReset();
            else
            {
                Label(Session.Stage == OfficeStage.complete ? "업무 인계 완료" : panel == "monitor" ? "01 / 모니터" : panel == "copier" ? "02 / 복합기" : panel == "cabinet" ? "03 / 뒤쪽 수납장" : "작은 확인이 정확한 업무로", headingStyle);
                GUILayout.Space(8);
                drawingScroll=true;scroll = GUILayout.BeginScrollView(scroll, false, false);
                if (Session.Stage == OfficeStage.complete) DrawComplete();
                else if (panel == "monitor") DrawMonitor();
                else if (panel == "copier") DrawCopier();
                else if (panel == "cabinet") DrawCabinet();
                else DrawIntro();
                GUILayout.EndScrollView();
                drawingScroll=false;
                if(Event.current.type==EventType.Repaint){Rect sr=GUILayoutUtility.GetLastRect();Vector2 start=LayoutScreenPoint(sr.min),end=LayoutScreenPoint(sr.max);scrollClipScreen=new Rect(start,end-start);}
                if (panel.Length > 0) Button("사무실로 돌아가기 [Esc]", CloseWork);
            }
            GUILayout.EndArea();
            paperMode = false;
            Fill(new Rect(0, 777, 1440, 123), new Color(.055f, .10f, .13f));
            GUI.Label(new Rect(32, 789, 1370, 58), feedback.Length > 0 ? feedback : Session.Message, bodyStyle);
            GUI.Label(new Rect(32, 855, 1370, 34), "클릭·터치: 물건 선택  /  드래그·←→↑↓: 회전  /  휠·+−: 확대  /  1·2·3 또는 Tab: 물건 초점, Enter: 열기  /  UI: Tab·↑↓·Enter", smallStyle);
            focusedControlName=clearGuiFocus?"":GUI.GetNameOfFocusedControl();
            editingText = focusedControlName.StartsWith("input-");
            GUI.matrix = oldMatrix;
        }
        void DrawCloseupPresentation()
        {
            Fill(new Rect(756, 143, 628, 620), new Color(0, 0, 0, .35f));
            Fill(new Rect(744, 131, 628, 620), new Color(.94f, .92f, .85f));
            Fill(new Rect(744, 131, 628, 52), new Color(.035f, .10f, .13f));
            string title = panel == "monitor" ? (Session.Stage == OfficeStage.request_pending ? "받은 메시지 / 출력 요청" : "문서 검토 / 날짜를 확인하세요")
                : panel == "copier" ? "출력 설정 / 용지 미리보기" : Session.Stage == OfficeStage.filed ? "동료에게 전달 / 인계 카드" : "서류 보관 / 분류함 선택";
            GUI.Label(new Rect(766, 141, 580, 36), title, headingStyle);
            GUI.Label(new Rect(45, 144, 660, 45), bindings[focusedObject].label + " · 자세히 보기", headingStyle);
            GUI.Label(new Rect(45, 718, 660, 40), "선택한 실제 물건을 확대했습니다.  Esc: 사무실로 돌아가기", smallStyle);
            if (panel == "copier")
            {
                bool completed=Session.PrintCompletions>0;
                bool printing=Session.Stage==OfficeStage.printing;
                int count=completed||printing?Session.PrintedCopies:1;
                float produced=printing?Session.PrintProgress*count:count;
                // Each physical sheet has its own exposed edge and page marker.
                // In progress, a sheet emerges only after its share of the job begins.
                for(int i=count-1;i>=0;i--)
                {
                    float emergence=printing?Mathf.Clamp01(produced-i):1;
                    if(emergence<=0)continue;
                    float top=Mathf.Lerp(664,518+i*27,emergence);
                    Rect paper=new Rect(100+i*31,top,478,128);
                    Fill(new Rect(paper.x+5,paper.y+5,paper.width,paper.height),new Color(0,0,0,.25f));
                    Fill(paper,new Color(.98f,.97f,.92f));
                    GUI.Label(new Rect(paper.x+20,top+10,435,30),Session.Data.document_title,paperHeading);
                    GUI.Label(new Rect(paper.x+20,top+46,435,30),"회의일  "+Session.Date,paperBody);
                    GUI.Label(new Rect(paper.x+20,top+87,280,28),completed?"✓ 출력 완료":printing?"용지가 나오고 있어요":"문서 미리보기",paperSmall);
                    GUI.Label(new Rect(paper.x+337,top+99,135,25),"용지 "+(i+1)+" / "+count,paperSmall);
                }
            }
            else if (panel == "cabinet")
            {
                int destination=Array.IndexOf(Session.Data.folders,Session.Folder);
                GUI.Label(new Rect(91,497,580,28),destination<0?"분류 전 · 문서 묶음":"보관 완료 · 묶음의 위치를 확인하세요",smallStyle);
                for(int i=0;i<Session.Data.folders.Length;i++)
                {
                    Rect bin=new Rect(89+i*197,551,184,150);
                    Fill(new Rect(bin.x+8,bin.y-19,120,22),new Color(.73f,.75f,.56f));
                    Fill(bin,new Color(.87f,.86f,.70f));
                    GUI.Label(new Rect(bin.x+10,bin.y+6,170,30),Session.Data.folders[i],paperHeading);
                    if(i==destination)DrawStoredBundle(new Rect(bin.x+12,bin.y+44,158,87));
                }
                if(destination<0)DrawStoredBundle(new Rect(91,404,260,85));
            }
        }
        void DrawStoredBundle(Rect paper)
        {
            int count=Session.PrintCompletions>0?Session.PrintedCopies:0;
            if(count==0)return;
            for(int i=count-1;i>=0;i--)
            {
                Rect sheet=new Rect(paper.x+i*3,paper.y+i*4,paper.width,paper.height);
                Fill(new Rect(sheet.x+2,sheet.y+2,sheet.width,sheet.height),new Color(0,0,0,.18f));
                Fill(sheet,new Color(.98f,.97f,.92f));
            }
            GUI.Label(new Rect(paper.x+6,paper.y+5,paper.width-12,48),Session.Data.document_title,paperBody);
            GUI.Label(new Rect(paper.x+6,paper.y+53,paper.width-12,28),count+"부 · "+Session.Data.expected_date,paperSmall);
        }
        void DrawTargets()
        {
            if (Session.Paused || resetDialog) return;
            for (int i = 0; i < bindings.Length; i++)
            {
                Vector3 p = viewCamera.WorldToScreenPoint(bindings[i].renderer.bounds.center);
                Vector2 u = UiPoint(new Vector2(p.x, p.y));
                if (p.z <= 0 || u.x > 900 || u.x < 0) continue;
                Color color = i == focusedObject ? new Color(.21f, .72f, .57f) : new Color(.09f, .18f, .20f, .92f);
                float labelY = u.y - (i == 0 ? 85 : i == 1 ? 40 : 75);
                Fill(new Rect(u.x - 74, labelY, 148, 33), new Color(.04f, .13f, .16f, .98f));
                GUI.Label(new Rect(u.x - 65, labelY + 1, 140, 32), (i + 1) + "  " + bindings[i].label, targetStyle);
                if (i == focusedObject)
                {
                    // Screen-space outline of the actual renderer; no duplicate 3D geometry or material tint.
                    Bounds b = bindings[i].renderer.bounds;
                    Vector2 min = new Vector2(float.MaxValue, float.MaxValue), max = new Vector2(float.MinValue, float.MinValue);
                    for (int n = 0; n < 8; n++)
                    {
                        Vector3 c = b.center + Vector3.Scale(b.extents, new Vector3((n & 1) == 0 ? -1 : 1, (n & 2) == 0 ? -1 : 1, (n & 4) == 0 ? -1 : 1));
                        Vector3 s = viewCamera.WorldToScreenPoint(c); Vector2 v = UiPoint(new Vector2(s.x, s.y)); min = Vector2.Min(min, v); max = Vector2.Max(max, v);
                    }
                    Fill(new Rect(min.x - 3, min.y - 3, max.x - min.x + 6, 2), color);
                    Fill(new Rect(min.x - 3, max.y + 1, max.x - min.x + 6, 2), color);
                    Fill(new Rect(min.x - 3, min.y - 3, 2, max.y - min.y + 6), color);
                    Fill(new Rect(max.x + 1, min.y - 3, 2, max.y - min.y + 6), color);
                }
            }
        }
        void DrawIntro()
        {
            Label("동료가 회의자료 출력을 부탁했습니다. 빠진 요청을 확인하고, 날짜를 고친 뒤 필요한 만큼 출력해 보관하세요.");
            GUILayout.Space(18);
            Label("3D 사무실의 물건을 직접 선택하세요.");
            Label("1 모니터 — 요청·문서\n2 복합기 — 최신본 출력\n3 뒤쪽 수납장 — 보관·인계", smallStyle);
            GUILayout.Space(12);
            Label("연습 경로: " + (Session.ChangePractice ? "출력 전 2부 → 3부 변경" : "기본 2부"));
            Button("화면 움직임 줄이기: "+(reducedMotion?"켜짐":"꺼짐"),()=>reducedMotion=!reducedMotion);
            Button("경로 변경 / 처음부터 연습", () => resetDialog = true);
            Label("EX-010 이력 복구 연습: 이번 버전 미구현", smallStyle);
            Label("대인관계능력 연결: 확인 질문과 정확한 인계. 가상 교육 사례이며 적성 진단·점수를 제공하지 않습니다.", smallStyle);
        }
        void DrawMonitor()
        {
            if (Session.Stage == OfficeStage.request_pending)
            {
                Label("동료: 회의자료를 출력해 주세요.");
                Button((Session.KnownSlots.Contains("document_id") ? "✓ " : "") + "어떤 자료이고 회의일은 언제인가요?", () => Perform("ask_document", () => Session.Ask("document_id"), false));
                Button((Session.KnownSlots.Contains("copies") ? "✓ " : "") + "몇 부가 필요한가요?", () => Perform("ask_copies", () => Session.Ask("copies"), false));
                Button((Session.KnownSlots.Contains("folder") ? "✓ " : "") + "어느 칸에 보관할까요?", () => Perform("ask_folder", () => Session.Ask("folder"), false));
                Label("요청 r" + Session.RequestRevision + " / " + (Session.KnownSlots.Contains("document_id") ? Session.Data.document_title + " · " + Session.Data.expected_date : "자료·날짜 미확인") + " / " + (Session.KnownSlots.Contains("copies") ? Session.ExpectedCopies + "부" : "부수 미확인") + " / " + (Session.KnownSlots.Contains("folder") ? Session.Data.expected_folder : "보관처 미확인"), smallStyle);
                Button("요청 요약 전송 → 동료 확인 받기", () => Perform("confirm", () => Session.Confirm(true)));
            }
            else
            {
                Label("요청: " + Session.Data.document_title + " / " + Session.Data.expected_date + " / " + Session.ExpectedCopies + "부", smallStyle);
                Label("문서 " + Session.Data.document_id + " r" + Session.DocumentRevision + " (저장 r" + Session.SavedRevision + ")");
                bool editable=GUI.enabled;GUI.enabled=Session.Stage<=OfficeStage.document_saved;
                draftTitle = TextField("문서 제목", "document-title", draftTitle);
                draftDate = TextField("회의일", "document-date", draftDate);
                GUI.enabled=editable;
                Label(draftTitle == Session.Title && draftDate == Session.Date ? "저장본과 같은 초안" : "● 미저장 초안 — 닫아도 유지됩니다.", smallStyle);
                Button("수정 내용 저장", () => {
                    if (draftTitle != Session.Title || draftDate != Session.Date) Perform("edit_document", () => Session.Edit(draftTitle,draftDate), false);
                    Perform("save", Session.Save);
                }, Session.Stage==OfficeStage.request_confirmed||Session.Stage==OfficeStage.document_saved&&(draftTitle!=Session.Title||draftDate!=Session.Date));
                Label("이력: " + string.Join(" → ", Session.History.ConvertAll(h => "r" + h.revision + (h.saved ? " 저장" : " 편집"))), smallStyle);
                if (Session.Stage == OfficeStage.document_saved) Label("저장 완료. 사무실로 돌아가 복합기를 선택하세요.");
            }
        }
        void EditDraft(string title, string date)
        {
            if (Session.Edit(title, date)) { draftTitle = Session.Title; draftDate = Session.Date; }
            Result(true);
        }
        void DrawCopier()
        {
            Label("출력 조건을 확인한 뒤 실행하세요.");
            Button("자료: " + selectedFile + " / 클릭하여 변경", () => selectedFile = selectedFile == Session.Data.document_id ? "DOC-OLD" : Session.Data.document_id, Session.Stage == OfficeStage.document_saved);
            Button("문서 revision: r" + selectedRevision + " / 최신·초기본 전환", () => selectedRevision = selectedRevision == Session.SavedRevision ? 1 : Session.SavedRevision, Session.Stage == OfficeStage.document_saved);
            bool oldEnabled = GUI.enabled; GUI.enabled = Session.Stage == OfficeStage.document_saved;
            copiesInput = TextField("출력 부수", "print-copies", copiesInput);
            GUILayout.BeginHorizontal();
            Button("− 1부", () => { if (!int.TryParse(copiesInput,out copies)) copies=1; copiesInput=Mathf.Max(1,copies-1).ToString(); });
            Button("+ 1부", () => { if (!int.TryParse(copiesInput,out copies)) copies=1; copiesInput=Mathf.Min(99,copies+1).ToString(); });
            GUILayout.EndHorizontal(); GUI.enabled = oldEnabled;
            Label("현재 요청 r" + Session.RequestRevision + " / 확인 r" + Session.ConfirmedRequestRevision + " / 최신 저장 r" + Session.SavedRevision, smallStyle);
            Button(Session.Stage == OfficeStage.printing ? "출력 중… 중복 실행 잠금" : "출력 시작", () => {
                int.TryParse(copiesInput,out copies); Perform("print", () => Session.Print(selectedFile, selectedRevision, copies));
            }, Session.Stage == OfficeStage.document_saved);
            if (Session.Stage == OfficeStage.printing)
            {
                Rect r = GUILayoutUtility.GetRect(400, 18); Fill(r, new Color(.18f, .24f, .27f)); Fill(new Rect(r.x, r.y, r.width * Session.PrintProgress, r.height), new Color(.22f, .70f, .54f));
            }
            if (Session.Stage == OfficeStage.print_ready) Label("출력이 완료되었습니다. 수납장으로 이동하세요.");
        }
        void DrawCabinet()
        {
            if (Session.Stage == OfficeStage.print_ready)
            {
                Label("문서 묶음을 분류함으로 옮기세요. 드래그 또는 묶음 선택 후 칸 선택.", smallStyle);
                DrawSortingBoard(false);
            }
            else if (Session.Stage == OfficeStage.filed)
            {
                Label("동료에게 처리 결과를 요약하세요. 네 항목이 요청과 맞아야 합니다.");
                Label("✓ 보관된 업무 결과", headingStyle);
                GUILayout.Space(10);Label(Session.Data.document_title + " " + Session.PrintedCopies + "부\n「" + Session.Folder + "」 칸 안에 보관됨", smallStyle);GUILayout.Space(12);
                handoffTitle = TextField("제목", "handoff-title", handoffTitle);
                handoffDate = TextField("회의일", "handoff-date", handoffDate);
                handoffCopiesInput = TextField("부수", "handoff-copies", handoffCopiesInput);
                handoffFolder = TextField("보관처", "handoff-folder", handoffFolder);
                Button("인계 요약 전송 → 동료 수신 확인", () => { int.TryParse(handoffCopiesInput,out handoffCopies); Perform("handoff", () => Session.Handoff(handoffTitle,handoffDate,handoffCopies,handoffFolder,true)); });
            }
        }
        void DrawComplete()
        {
            Label("✓ 요청을 질문하고 확인했습니다.\n✓ 날짜를 수정해 최신본을 저장했습니다.\n✓ 요청한 " + Session.PrintedCopies + "부를 한 번 출력했습니다.\n✓ 회의자료 칸에 보관했습니다.\n✓ 처리 결과와 위치를 인계했습니다.");
            GUILayout.Space(18); Label("동료: 정확히 확인하고 알려줘서 고마워요!");
            Label("대인관계능력을 요청 확인·정확한 인계로 연습했습니다. 실제 능력·적성 진단 결과가 아닙니다.", smallStyle);
            Button("새 연습 / 전체 초기화", () => resetDialog = true);
        }
        void DrawPause()
        {
            Label("일시정지", headingStyle); Label("출력과 물건 조작이 멈췄습니다.");
            Button("계속하기", TogglePause);
            Button("화면 움직임 줄이기: "+(reducedMotion?"켜짐":"꺼짐"),()=>reducedMotion=!reducedMotion);
            Button("전체 초기화", () => { TogglePause(); resetDialog = true; });
            Button("체험 그만하기 / 종료 기록 보존", () => protocol.EndFromUser());
        }
        void DrawReset()
        {
            Label("처음부터 연습", headingStyle); Label("진행·출력·문서 이력을 초기화하고 경로를 선택합니다.");
            Button("기본 경로 / 2부", () => Reset(false));
            Button("변경 요청 경로 / 출력 전 3부로 변경", () => Reset(true));
            Button("취소 [Esc]", () => resetDialog = false);
        }
        void Reset(bool changed) { protocol.ResetRun(changed); ClearInputs(); resetDialog = false; renderedFocus="reset"; savedRect=default(Rect);hasSavedCamera=false; savedRotation=default(Quaternion); yaw = 152; pitch = 34; distance = 9.7f; PositionCamera(); Publish(); }
        public void BeginExternalRun() { ClearInputs(); resetDialog=false; renderedFocus="reset"; panel="";hasSavedCamera=false;savedRect=default(Rect); }
        public void EndUi(){tracking=bundleDragging=bundleSelected=false;clearGuiFocus=cancelGuiGesture=true;}
        public string CurrentObject => panel.Length > 0 ? panel : null;
        public string DraftDate => draftDate;
        public string DraftTitle => draftTitle;
        public string ActualInput(string action) => action=="save" ? draftTitle+" / "+draftDate : action=="print" ? selectedFile+" / r"+selectedRevision+" / "+copiesInput : action=="file" ? attemptedFolder : action=="handoff" ? handoffTitle+" / "+handoffDate+" / "+handoffCopiesInput+" / "+handoffFolder : action;
        string attemptedFolder;
        string TextField(string label,string id,string value)
        {
            Label(label,smallStyle);
            if(inputStyle==null)
            {
                inputStyle=new GUIStyle(GUI.skin.textField){font=koreanFont,fontSize=20,padding=new RectOffset(8,8,8,8)};
                Color ink=new Color(.035f,.065f,.08f);
                inputStyle.normal.textColor=inputStyle.focused.textColor=inputStyle.hover.textColor=inputStyle.active.textColor=ink;
            }
            GUI.SetNextControlName("input-"+id);
            string result=GUILayout.TextField(value??"",160,inputStyle,GUILayout.MinHeight(40));
            if(result!=value&&GUI.enabled)protocol.Progress(id,result,panel);
            if(Event.current.type==EventType.Repaint){Vector2 center=LayoutScreenPoint(GUILayoutUtility.GetLastRect().center);inputDiagnostics.Add(new InputDiagnostic{name=id,value=result,x=center.x,y=center.y,enabled=GUI.enabled});}
            return result;
        }
        void MoveBundle(string folder)
        {
            attemptedFolder=folder;
            Perform("file",()=>Session.File(folder));
            bundleDragging=bundleSelected=false;
        }
        void DropOutline(Rect rect,Color color,float width)
        {
            Fill(new Rect(rect.x,rect.y,rect.width,width),color);Fill(new Rect(rect.x,rect.yMax-width,rect.width,width),color);
            Fill(new Rect(rect.x,rect.y,width,rect.height),color);Fill(new Rect(rect.xMax-width,rect.y,width,rect.height),color);
        }
        void DrawSortingBoard(bool readOnly)
        {
            Rect board=GUILayoutUtility.GetRect(500,260);int control=GUIUtility.GetControlID(FocusType.Keyboard);
            Rect source=new Rect(board.x+5,board.y+72,150,90);
            Rect[] bins=new Rect[Session.Data.folders.Length];
            for(int i=0;i<bins.Length;i++)bins[i]=new Rect(board.x+205,board.y+i*78,270,68);
            if(Event.current.type==EventType.Repaint)
            {
                Vector2 c=LayoutScreenPoint(source.center);sortDiagnostics.Add(new SortDiagnostic{name="document-bundle",x=c.x,y=c.y});
                for(int i=0;i<bins.Length;i++){c=LayoutScreenPoint(bins[i].center);sortDiagnostics.Add(new SortDiagnostic{name=Session.Data.folders[i],x=c.x,y=c.y});}
            }
            Fill(source,bundleSelected?new Color(.90f,.82f,.48f):new Color(.96f,.95f,.89f));
            GUI.Label(new Rect(source.x+8,source.y+5,source.width-16,source.height-10),Session.Data.document_title+"\n"+Session.PrintedCopies+"부\n"+(bundleSelected?"↓ 강조된 칸에 놓기":"묶음 선택"),paperBody);
            for(int i=0;i<bins.Length;i++)
            {
                bool hover=bundleSelected&&(bundleDragging?bins[i].Contains(Event.current.mousePosition):i==binFocus);
                Fill(bins[i],hover?new Color(.55f,.91f,.72f):bundleSelected?new Color(.70f,.86f,.80f):new Color(.78f,.78f,.67f));
                if(bundleSelected)DropOutline(bins[i],hover?new Color(.20f,.70f,.49f):new Color(.28f,.61f,.60f),hover?4:2);
                GUI.Label(new Rect(bins[i].x+10,bins[i].y+12,bins[i].width-20,50),(hover?"↓ 놓기 · ":"▣ ")+Session.Data.folders[i],paperBody);
            }
            Event ev=Event.current;
            if(ev.type==EventType.MouseDown&&ev.button==0)
            {
                if(source.Contains(ev.mousePosition)){CareerAudio.Play(protocol.RunId,"drag_pick");bundleSelected=bundleDragging=true;GUIUtility.hotControl=control;GUI.FocusControl(null);ev.Use();}
                else if(bundleSelected){for(int i=0;i<bins.Length;i++)if(bins[i].Contains(ev.mousePosition)){MoveBundle(Session.Data.folders[i]);ev.Use();break;}}
            }
            else if(ev.type==EventType.MouseUp&&bundleDragging)
            {
                bool moved=false;
                for(int i=0;i<bins.Length;i++)if(bins[i].Contains(ev.mousePosition)){MoveBundle(Session.Data.folders[i]);moved=true;break;}
                if(!moved)bundleDragging=false;
                GUIUtility.hotControl=0;ev.Use();
            }
            else if(ev.type==EventType.MouseDrag&&bundleDragging){ev.Use();}
            if(bundleDragging&&ev.type==EventType.Repaint){Fill(new Rect(ev.mousePosition.x-35,ev.mousePosition.y-15,100,42),new Color(.9f,.85f,.65f));GUI.Label(new Rect(ev.mousePosition.x-30,ev.mousePosition.y-13,95,40),"文 "+Session.PrintedCopies+"부",paperBody);}
            if(ev.type==EventType.KeyDown)
            {
                if(ev.keyCode==KeyCode.UpArrow||ev.keyCode==KeyCode.LeftArrow){binFocus=(binFocus+bins.Length-1)%bins.Length;ev.Use();}
                else if(ev.keyCode==KeyCode.DownArrow||ev.keyCode==KeyCode.RightArrow||ev.keyCode==KeyCode.Tab){binFocus=(binFocus+1)%bins.Length;ev.Use();}
                else if(ev.keyCode==KeyCode.Return||ev.keyCode==KeyCode.Space)
                {
                    if(heldSubmitKey!=ev.keyCode){heldSubmitKey=ev.keyCode;if(bundleSelected)MoveBundle(Session.Data.folders[binFocus]);else bundleSelected=true;}
                    ev.Use();
                }
            }
            Label("키보드: Enter/Space로 묶음 선택 → 방향키로 칸 이동 → Enter/Space로 보관 · Esc 선택 취소",smallStyle);
        }
    }
}

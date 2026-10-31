using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using UnityEngine;

namespace CareerExperience
{
    [Serializable] public sealed class OfficeBinding
    {
        public string id, label;
        public MeshCollider collider;
        public Renderer renderer;
    }
    public sealed class OfficeExperience : MonoBehaviour
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
        [DllImport("__Internal")] static extern void PublishOfficeState(string json);
        [DllImport("__Internal")] static extern void PublishOfficeTests(string json);
        [Serializable] public class TargetDiagnostic { public string id; public float x, y; }
        [Serializable] public class ButtonDiagnostic { public string label; public float x, y; public bool enabled; }
        readonly List<ButtonDiagnostic> buttonDiagnostics = new List<ButtonDiagnostic>();
        [Serializable] public class RuntimeDiagnostic { public OfficeSnapshot session; public string panel, feedback; public int focusedObject; public TargetDiagnostic[] targets; public ButtonDiagnostic[] buttons; public int triangles, interactiveObjects, visibleRenderers; public string unity; public bool closeup; public float cameraDistance; }
        void Awake()
        {
            gameObject.name = "OfficeExperience";
            Session = new OfficeSession(JsonUtility.FromJson<OfficeData>(scenario.text));
            roomRenderers = bindings[0].renderer.transform.parent.GetComponentsInChildren<Renderer>();
            originalVisibility = Array.ConvertAll(roomRenderers, r => r.enabled);
            ClearInputs(); PositionCamera(true);
        }
        void ClearInputs()
        {
            panel = ""; feedback = ""; copies = handoffCopies = 1; selectedFile = Session.Data.document_id;
            selectedRevision = Session.SavedRevision; draftDate = Session.Date; draftTitle = Session.Title;
            handoffTitle = Session.Data.document_title; handoffDate = Session.Data.initial_date; handoffFolder = "인사자료";
            focusedAction = focusedObject = 0; scroll = Vector2.zero; tracking = dragging = false;
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
                Renderer selected = closeup ? Array.Find(bindings, b => b.id == panel).renderer : null;
                for (int i = 0; i < roomRenderers.Length; i++) roomRenderers[i].enabled = closeup ? roomRenderers[i] == selected : originalVisibility[i];
                renderedFocus = panel;
            }
            Vector3 desiredPosition = overviewPosition;
            Quaternion desiredRotation = overviewRotation;
            if (closeup)
            {
                Bounds bounds = Array.Find(bindings, b => b.id == panel).renderer.bounds;
                desiredRotation = Quaternion.Euler(panel == "monitor" ? 10 : 22, 164, 0);
                float size = Mathf.Max(bounds.size.y, bounds.size.x / (670f / 585f));
                float focalDistance = size * .5f / Mathf.Tan(18 * Mathf.Deg2Rad) * 1.55f;
                desiredPosition = bounds.center + desiredRotation * new Vector3(0, 0, -focalDistance);
            }
            float blend = 1 - Mathf.Exp(-Time.unscaledDeltaTime * 12);
            viewCamera.transform.position = Vector3.Lerp(viewCamera.transform.position, desiredPosition, blend);
            viewCamera.transform.rotation = Quaternion.Slerp(viewCamera.transform.rotation, desiredRotation, blend);
            viewCamera.fieldOfView = Mathf.Lerp(viewCamera.fieldOfView, closeup ? 36 : 40, blend);
            Rect logical = closeup ? new Rect(24, 150, 670, 585) : new Rect(0, 121.5f, 936, 648);
            viewCamera.rect = new Rect((Offset.x + logical.x * Scale) / Screen.width,
                (Screen.height - Offset.y - (logical.y + logical.height) * Scale) / Screen.height,
                logical.width * Scale / Screen.width, logical.height * Scale / Screen.height);
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
            if (Session.SelectObject(bindings[idx].id))
            {
                panel = bindings[idx].id; feedback = ""; focusedAction = 0; scroll = Vector2.zero;
                selectedRevision = Session.SavedRevision; draftDate = Session.Date; draftTitle = Session.Title;
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
        void Update()
        {
            Session.Tick(Time.deltaTime);
            if (Input.GetKeyDown(KeyCode.Escape))
            {
                if (resetDialog) resetDialog = false;
                else if (panel.Length > 0) panel = "";
                else Session.TogglePause();
            }
            if (Input.GetKeyDown(KeyCode.P)) { Session.TogglePause(); focusedAction = 0; }
            if (Input.GetKeyDown(KeyCode.R)) { resetDialog = true; focusedAction = 0; }
            if (!Session.Paused && !resetDialog)
            {
                if (Input.GetKeyDown(KeyCode.Alpha1)) { panel = ""; focusedObject = 0; }
                if (Input.GetKeyDown(KeyCode.Alpha2)) { panel = ""; focusedObject = 1; }
                if (Input.GetKeyDown(KeyCode.Alpha3)) { panel = ""; focusedObject = 2; }
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
                else KeyboardActions();
                if (Input.touchCount > 0)
                {
                    Touch t = Input.GetTouch(0);
                    if (Input.touchCount > 1) { tracking = false; }
                    else if (t.phase == TouchPhase.Began) BeginPointer(t.position);
                    else if (t.phase == TouchPhase.Moved) MovePointer(t.position);
                    else if (t.phase == TouchPhase.Ended) EndPointer(t.position);
                    else if (t.phase == TouchPhase.Canceled) tracking = false;
                }
                else
                {
                    if (Input.GetMouseButtonDown(0)) BeginPointer(Input.mousePosition);
                    if (Input.GetMouseButton(0)) MovePointer(Input.mousePosition);
                    if (Input.GetMouseButtonUp(0)) EndPointer(Input.mousePosition);
                }
            }
            else KeyboardActions();
            UpdateCloseup();
            if (Time.unscaledTime - lastPublish > .25f) { Publish(); lastPublish = Time.unscaledTime; }
        }
        void KeyboardActions()
        {
            if (actions.Count == 0) return;
            if (Input.GetKeyDown(KeyCode.Tab) || Input.GetKeyDown(KeyCode.DownArrow)) focusedAction = (focusedAction + 1) % actions.Count;
            if (Input.GetKeyDown(KeyCode.UpArrow)) focusedAction = (focusedAction + actions.Count - 1) % actions.Count;
            if (Input.GetKeyDown(KeyCode.Return) || Input.GetKeyDown(KeyCode.Space)) actions[Mathf.Clamp(focusedAction, 0, actions.Count - 1)]();
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
            return new RuntimeDiagnostic { session = Session.Snapshot(), panel = panel, feedback = feedback, targets = targets,
                focusedObject = focusedObject, triangles = triangles, interactiveObjects = bindings.Length, unity = Application.unityVersion, buttons = buttonDiagnostics.ToArray(),
                visibleRenderers = Array.FindAll(roomRenderers, r => r.enabled).Length, closeup = panel.Length > 0,
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
                Vector2 point = GUIUtility.GUIToScreenPoint(GUILayoutUtility.GetLastRect().center);
                buttonDiagnostics.Add(new ButtonDiagnostic { label = text, x = point.x, y = point.y, enabled = enabled });
            }
            GUI.backgroundColor = oldBg; GUI.enabled = old;
            if (clicked) action();
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
            if (Session == null) return;
            Styles();
            Matrix4x4 oldMatrix = GUI.matrix;
            GUI.matrix = Matrix4x4.TRS(Offset, Quaternion.identity, Vector3.one * Scale);
            actionIndex = enabledButtonCount = 0;
            if (Event.current.type == EventType.Repaint) { actions.Clear(); buttonDiagnostics.Clear(); }
            Fill(new Rect(0, 0, 1440, 112), new Color(.055f, .10f, .13f));
            GUI.Label(new Rect(32, 17, 930, 44), "OFFICE / 사무보조원의 하루", titleStyle);
            GUI.Label(new Rect(34, 64, 900, 35), "01 요청 확인   →   02 문서 검토   →   03 출력   →   04 보관·인계", labelStyle);
            if (GUI.Button(new Rect(1112, 29, 120, 48), Session.Paused ? "계속하기 [P]" : "일시정지 [P]", buttonStyle)) Session.TogglePause();
            if (GUI.Button(new Rect(1244, 29, 164, 48), "전체 초기화 [R]", buttonStyle)) resetDialog = true;
            paperMode = panel.Length > 0 && !Session.Paused && !resetDialog;
            if (panel.Length == 0) DrawTargets();
            if (paperMode) DrawCloseupPresentation();
            else Fill(new Rect(934, 125, 474, 635), new Color(.07f, .13f, .16f));
            GUILayout.BeginArea(paperMode ? new Rect(786, 197, 556, 535) : new Rect(958, 143, 426, 593));
            if (Session.Paused) DrawPause();
            else if (resetDialog) DrawReset();
            else
            {
                Label(Session.Stage == OfficeStage.complete ? "업무 인계 완료" : panel == "monitor" ? "01 / 모니터" : panel == "copier" ? "02 / 복합기" : panel == "cabinet" ? "03 / 뒤쪽 수납장" : "작은 확인이 정확한 업무로", headingStyle);
                GUILayout.Space(8);
                scroll = GUILayout.BeginScrollView(scroll, false, false);
                if (Session.Stage == OfficeStage.complete) DrawComplete();
                else if (panel == "monitor") DrawMonitor();
                else if (panel == "copier") DrawCopier();
                else if (panel == "cabinet") DrawCabinet();
                else DrawIntro();
                GUILayout.EndScrollView();
                if (panel.Length > 0) Button("사무실로 돌아가기 [Esc]", () => { panel = ""; feedback = ""; });
            }
            GUILayout.EndArea();
            paperMode = false;
            Fill(new Rect(0, 777, 1440, 123), new Color(.055f, .10f, .13f));
            GUI.Label(new Rect(32, 789, 1370, 58), feedback.Length > 0 ? feedback : Session.Message, bodyStyle);
            GUI.Label(new Rect(32, 855, 1370, 34), "클릭·터치: 물건 선택  /  드래그·←→↑↓: 회전  /  휠·+−: 확대  /  1·2·3 또는 Tab: 물건 초점, Enter: 열기  /  UI: Tab·↑↓·Enter", smallStyle);
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
                float progress = Session.PrintProgress;
                float top = Session.Stage == OfficeStage.printing ? Mathf.Lerp(656, 545, progress) : 555;
                Rect paper = new Rect(115, top, 480, 135);
                Fill(new Rect(paper.x + 6, paper.y + 6, paper.width, paper.height), new Color(0, 0, 0, .2f));
                Fill(paper, new Color(.98f, .97f, .92f));
                GUI.Label(new Rect(paper.x + 22, top + 12, 440, 30), Session.Data.document_title, paperHeading);
                GUI.Label(new Rect(paper.x + 22, top + 48, 440, 30), "회의일  " + Session.Date + "     /     " + (Session.Stage >= OfficeStage.printing ? Session.PrintedCopies : copies) + "부", paperBody);
                GUI.Label(new Rect(paper.x + 22, top + 88, 440, 28), Session.Stage == OfficeStage.print_ready ? "✓ 요청한 용지 출력 완료" : Session.Stage == OfficeStage.printing ? "출력 중 — 용지가 나오고 있어요" : "출력될 문서를 먼저 확인하세요", paperSmall);
            }
            else if (panel == "cabinet")
            {
                Fill(new Rect(117, 568, 160, 31), new Color(.73f, .75f, .56f));
                Fill(new Rect(107, 596, 495, 96), new Color(.87f, .86f, .70f));
                GUI.Label(new Rect(130, 603, 455, 32), Session.Folder == null ? "분류할 문서 묶음" : "✓ 회의자료 칸 보관 완료", paperHeading);
                GUI.Label(new Rect(130, 645, 455, 32), Session.Data.document_title + "  /  " + Session.PrintedCopies + "부  /  " + Session.Data.expected_date, paperBody);
            }
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
            Button("경로 변경 / 처음부터 연습", () => resetDialog = true);
            Label("EX-010 이력 복구 연습: 이번 버전 미구현", smallStyle);
            Label("대인관계능력 연결: 확인 질문과 정확한 인계. 가상 교육 사례이며 적성 진단·점수를 제공하지 않습니다.", smallStyle);
        }
        void DrawMonitor()
        {
            if (Session.Stage == OfficeStage.request_pending)
            {
                Label("동료: 회의자료를 출력해 주세요.");
                Button((Session.KnownSlots.Contains("document_id") ? "✓ " : "") + "어떤 자료이고 회의일은 언제인가요?", () => Result(Session.Ask("document_id")));
                Button((Session.KnownSlots.Contains("copies") ? "✓ " : "") + "몇 부가 필요한가요?", () => Result(Session.Ask("copies")));
                Button((Session.KnownSlots.Contains("folder") ? "✓ " : "") + "어느 칸에 보관할까요?", () => Result(Session.Ask("folder")));
                Label("요청 r" + Session.RequestRevision + " / " + (Session.KnownSlots.Contains("document_id") ? Session.Data.document_title + " · " + Session.Data.expected_date : "자료·날짜 미확인") + " / " + (Session.KnownSlots.Contains("copies") ? Session.ExpectedCopies + "부" : "부수 미확인") + " / " + (Session.KnownSlots.Contains("folder") ? Session.Data.expected_folder : "보관처 미확인"), smallStyle);
                Button("요청 요약 전송 → 동료 확인 받기", () => Result(Session.Confirm(true)));
            }
            else
            {
                Label("요청: " + Session.Data.document_title + " / " + Session.Data.expected_date + " / " + Session.ExpectedCopies + "부", smallStyle);
                Label("문서 " + Session.Data.document_id + " r" + Session.DocumentRevision + " (저장 r" + Session.SavedRevision + ")");
                Label("제목: " + draftTitle + "\n회의일: " + draftDate);
                Button("회의일을 ‘11월 1일’로 편집", () => EditDraft(draftTitle, "11월 1일"));
                Button("회의일을 ‘11월 2일’로 편집", () => EditDraft(draftTitle, "11월 2일"));
                Button("제목만 변경 / 원래 제목", () => EditDraft(draftTitle == Session.Data.document_title ? "팀 회의자료 초안" : Session.Data.document_title, draftDate));
                Button("수정 내용 저장", () => Result(Session.Save()));
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
            Button("자료: " + selectedFile + " / 클릭하여 변경", () => selectedFile = selectedFile == Session.Data.document_id ? "DOC-OLD" : Session.Data.document_id, Session.Stage != OfficeStage.printing);
            Button("문서 revision: r" + selectedRevision + " / 최신·초기본 전환", () => selectedRevision = selectedRevision == Session.SavedRevision ? 1 : Session.SavedRevision, Session.Stage != OfficeStage.printing);
            Button("부수: " + copies + "부 / 1~4 순환", () => copies = copies % 4 + 1, Session.Stage != OfficeStage.printing);
            Label("현재 요청 r" + Session.RequestRevision + " / 확인 r" + Session.ConfirmedRequestRevision + " / 최신 저장 r" + Session.SavedRevision, smallStyle);
            Button(Session.Stage == OfficeStage.printing ? "출력 중… 중복 실행 잠금" : "출력 시작", () => Result(Session.Print(selectedFile, selectedRevision, copies)), Session.Stage != OfficeStage.printing && Session.Stage != OfficeStage.print_ready);
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
                Label("출력한 " + Session.PrintedCopies + "부를 어느 칸에 보관할까요?");
                foreach (string folder in Session.Data.folders) { string f = folder; Button(f + " 칸에 보관", () => Result(Session.File(f))); }
            }
            else if (Session.Stage == OfficeStage.filed)
            {
                Label("동료에게 처리 결과를 요약하세요. 네 항목이 요청과 맞아야 합니다.");
                Button("제목: " + handoffTitle, () => handoffTitle = handoffTitle == Session.Data.document_title ? "팀 회의자료 초안" : Session.Data.document_title);
                Button("날짜: " + handoffDate, () => handoffDate = handoffDate == Session.Data.expected_date ? Session.Data.initial_date : Session.Data.expected_date);
                Button("부수: " + handoffCopies + "부", () => handoffCopies = handoffCopies % 4 + 1);
                Button("보관처: " + handoffFolder, () => handoffFolder = handoffFolder == Session.Data.expected_folder ? "인사자료" : Session.Data.expected_folder);
                Button("인계 요약 전송 → 동료 수신 확인", () => Result(Session.Handoff(handoffTitle, handoffDate, handoffCopies, handoffFolder, true)));
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
            Button("계속하기", () => Session.TogglePause());
            Button("전체 초기화", () => { Session.TogglePause(); resetDialog = true; });
        }
        void DrawReset()
        {
            Label("처음부터 연습", headingStyle); Label("진행·출력·문서 이력을 초기화하고 경로를 선택합니다.");
            Button("기본 경로 / 2부", () => Reset(false));
            Button("변경 요청 경로 / 출력 전 3부로 변경", () => Reset(true));
            Button("취소 [Esc]", () => resetDialog = false);
        }
        void Reset(bool changed) { Session.Reset(changed); ClearInputs(); resetDialog = false; yaw = 152; pitch = 34; distance = 9.7f; PositionCamera(); Publish(); }
    }
}

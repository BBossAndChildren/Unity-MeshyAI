using System;
using System.Collections.Generic;
using System.Runtime.InteropServices;
using UnityEngine;
using UnityEngine.SceneManagement;

namespace CareerExperience
{
    [Serializable] public class WorkplaceRoom
    {
        public string roomId, name, scenePath, panoramaId, promptId, promptVersion, assetId, assetVersion, sourceFbxPath;
        public int triangles, instances;
        public bool available;
    }
    [Serializable] public class WorkplaceRegistry
    {
        public int schema_version = 3;
        public string buildId;
        public WorkplaceRoom[] rooms;
        public WorkplaceAsset[] assets;
    }
    [Serializable] public class WorkplaceAsset { public string assetId,version,name; }
    public sealed class WorkplaceExplorer : MonoBehaviour
    {
        public TextAsset registryJson;
        public Font koreanFont;
        WorkplaceRegistry registry;
        WorkplaceRoom current;
        Camera cameraView;
        Vector2 scroll, pointerStart, pointerLast;
        float yaw = 145, pitch = 35, distance = 9.5f;
        bool tracking, dragging, loading, paused;
        string selected = "";
        string selectedInstance = "";
        static WorkplaceExplorer owner;
        [Serializable] class RoomButton { public string roomId; public float x,y; public bool visible,available; }
        readonly List<RoomButton> roomButtons = new List<RoomButton>();
        GUIStyle textStyle, titleStyle, buttonStyle;
        [DllImport("__Internal")] static extern void PublishWorkplaceState(string json);
        [Serializable] class Snapshot
        {
            public string buildId, roomId, name, panoramaId, scenePath, selected, selectedInstance, unity;
            public int availableRooms, triangles, instances, renderers, measuredTriangles, materials, textures;
            public int textureWidth,textureHeight;
            public bool loading, paused;
            public float yaw, pitch, distance;
            public float menuScrollY;
            public RoomButton[] buttons;
        }
        void Awake()
        {
            if (owner != null) { Destroy(gameObject); return; }
            owner = this; DontDestroyOnLoad(gameObject);
            registry = JsonUtility.FromJson<WorkplaceRegistry>(registryJson.text);
            CareerProtocol.Get();
            PilotRuntime.Get(this,koreanFont);
            SceneManager.sceneLoaded += Loaded;
            Loaded(SceneManager.GetActiveScene(), LoadSceneMode.Single);
        }
        void OnDestroy() { if (owner == this) { SceneManager.sceneLoaded -= Loaded; owner = null; } }
        void Loaded(Scene scene, LoadSceneMode mode)
        {
            current = Array.Find(registry.rooms, room => room.scenePath == scene.path);
            if(current==null&&CareerSuiteMode.IsOfficeScene(scene.path))current=Array.Find(registry.rooms,room=>room.roomId=="PAN-001");
            cameraView = Camera.main; loading = false; tracking = dragging = paused = false;
            selected = selectedInstance = ""; yaw = 145; pitch = 35; distance = 9.5f;
            if (current != null) CareerProtocol.Get().RoomChanged(current.roomId);
            if (current != null && !CareerSuiteMode.IsOfficeScene(scene.path)) PositionCamera();
            Publish();
        }
        public void SelectRoom(string roomId)
        {
            if(PilotRuntime.Instance!=null&&PilotRuntime.Instance.BlocksOfficeNavigation(roomId))return;
            if (loading) return;
            var next = Array.Find(registry.rooms, room => room.roomId == roomId);
            if (next == null || !next.available) return;
            if(current!=null&&current.roomId==roomId&&SceneManager.GetActiveScene().path==next.scenePath)return;
            if(PilotRuntime.Instance!=null)PilotRuntime.Instance.BeforeRoomChange();
            loading = true; tracking = false;
            SceneManager.LoadSceneAsync(next.scenePath, LoadSceneMode.Single);
        }
        public void ReturnToRooms() { SelectRoom("PAN-002"); }
        public void SelectSceneForExperience(string scenePath)
        {
            if(loading||SceneManager.GetActiveScene().path==scenePath)return;
            if(!CareerSuiteMode.IsOfficeScene(scenePath))return;
            if(PilotRuntime.Instance!=null)PilotRuntime.Instance.BeforeRoomChange();
            loading=true;tracking=false;SceneManager.LoadSceneAsync(scenePath,LoadSceneMode.Single);
        }
        void PositionCamera()
        {
            if (cameraView == null || Screen.width <= 0 || Screen.height <= 0) return;
            float sidebar = CareerSuiteMode.Managed?0:Mathf.Min(Screen.width * .42f, Mathf.Max(225, Screen.width * .23f));
            float left = sidebar / Screen.width;
            float right = PilotRuntime.HasLiveExperience ? .68f : 1f;
            if (!PilotRuntime.HasLiveExperience && PilotRuntime.Instance != null&&!CareerSuiteMode.Managed)
            {
                // Match the existing 1440x900 selector's scaled left boundary.
                float uiScale = Mathf.Min(Screen.width / 1440f, Screen.height / 900f);
                right = ((Screen.width - 1440f * uiScale) / 2f + 1000f * uiScale) / Screen.width;
            }
            cameraView.rect = new Rect(left, .08f, Mathf.Max(.1f, right-left), .79f);
            Vector3 target = new Vector3(0, .7f, 0);
            float renderDistance = distance;
            if (!PilotRuntime.HasLiveExperience && PilotRuntime.Instance != null&&!CareerSuiteMode.Managed)
            {
                float viewAspect = Mathf.Max(.1f, cameraView.pixelWidth / (float)Mathf.Max(1,cameraView.pixelHeight));
                renderDistance *= Mathf.Max(1f, 1.2f / viewAspect);
            }
            Vector3 pos = target + Quaternion.Euler(pitch, yaw, 0) * new Vector3(0, 0, -renderDistance);
            cameraView.transform.SetPositionAndRotation(pos, Quaternion.LookRotation(target - pos));
        }
        bool InView(Vector2 point) => cameraView != null && cameraView.pixelRect.Contains(point);
        void Begin(Vector2 point) { tracking = !loading && !paused && InView(point); dragging = false; pointerStart = pointerLast = point; }
        void Move(Vector2 point)
        {
            if (!tracking) return;
            if (Vector2.Distance(point, pointerStart) > 8) dragging = true;
            if (dragging)
            {
                Vector2 delta = point - pointerLast;
                yaw += delta.x * .22f; pitch = Mathf.Clamp(pitch - delta.y * .15f, 12, 75); PositionCamera();
            }
            pointerLast = point;
        }
        static string DisplayName(string name)
        {
            if (string.IsNullOrWhiteSpace(name)) return "공간 구성물";
            string value = System.Text.RegularExpressions.Regex.Replace(name, @"^COM-\d+\s*", "");
            value = System.Text.RegularExpressions.Regex.Replace(value,
                @"\s*[—–]\s*(?:Blender.*|blender_direct.*|Meshy.*)$", "",
                System.Text.RegularExpressions.RegexOptions.IgnoreCase);
            return value.Trim();
        }
        void End(Vector2 point)
        {
            if (tracking && !dragging && InView(point) && Vector2.Distance(point, pointerStart) <= 8 && Physics.Raycast(cameraView.ScreenPointToRay(point), out RaycastHit hit, 100))
            {
                Transform target=hit.collider.transform;
                while(target.parent!=null&&!System.Text.RegularExpressions.Regex.IsMatch(target.name,"^AST-[0-9]+-[0-9]+$"))target=target.parent;
                selectedInstance=target.name;
                int separator=target.name.LastIndexOf('-');
                string assetId=separator>3?target.name.Substring(0,separator):"";
                var label=registry.assets==null?null:Array.FindLast(registry.assets,a=>a.assetId==assetId);
                selected=DisplayName(label==null?null:label.name);
            }
            tracking = false; Publish();
        }
        void OnApplicationFocus(bool focused) { if (!focused) tracking = false; }
        void Update()
        {
            if (current == null || CareerSuiteMode.IsOfficeScene(SceneManager.GetActiveScene().path) || cameraView == null || PilotRuntime.InputCaptured) return;
            PositionCamera();
            if (!PilotRuntime.HasLiveExperience && (Input.GetKeyDown(KeyCode.P) || Input.GetKeyDown(KeyCode.Escape))) { paused = !paused; tracking = false; }
            if (!loading && !paused)
            {
                float horizontal = (Input.GetKey(KeyCode.RightArrow) ? 1 : 0) - (Input.GetKey(KeyCode.LeftArrow) ? 1 : 0);
                float vertical = (Input.GetKey(KeyCode.UpArrow) ? 1 : 0) - (Input.GetKey(KeyCode.DownArrow) ? 1 : 0);
                yaw += horizontal * 45 * Time.unscaledDeltaTime;
                pitch = Mathf.Clamp(pitch + vertical * 30 * Time.unscaledDeltaTime, 12, 75);
                float zoom = InView(Input.mousePosition) ? Input.mouseScrollDelta.y : 0;
                zoom += (Input.GetKey(KeyCode.Equals) ? 1 : 0) * Time.unscaledDeltaTime * 4;
                zoom -= (Input.GetKey(KeyCode.Minus) ? 1 : 0) * Time.unscaledDeltaTime * 4;
                distance = Mathf.Clamp(distance - zoom * .3f, 5, 14);
                if (Input.touchCount > 1) tracking = false;
                else if (Input.touchCount == 1)
                {
                    Touch touch = Input.GetTouch(0);
                    if (touch.phase == TouchPhase.Began) Begin(touch.position);
                    else if (touch.phase == TouchPhase.Moved) Move(touch.position);
                    else if (touch.phase == TouchPhase.Ended) End(touch.position);
                    else if (touch.phase == TouchPhase.Canceled) tracking = false;
                }
                else
                {
                    if (Input.GetMouseButtonDown(0)) Begin(Input.mousePosition);
                    if (Input.GetMouseButton(0)) Move(Input.mousePosition);
                    if (Input.GetMouseButtonUp(0)) End(Input.mousePosition);
                }
            }
            if (Time.frameCount % 30 == 0) Publish();
        }
        void Styles()
        {
            if (textStyle != null) return;
            textStyle = new GUIStyle(GUI.skin.label) { font = koreanFont, fontSize = 16, wordWrap = true };
            textStyle.normal.textColor = Color.white;
            titleStyle = new GUIStyle(textStyle) { fontSize = 23, fontStyle = FontStyle.Bold };
            buttonStyle = new GUIStyle(GUI.skin.button) { font = koreanFont, fontSize = 15, wordWrap = true, alignment = TextAnchor.MiddleLeft };
        }
        void OnGUI()
        {
            if (registry == null||CareerSuiteMode.Managed) return; Styles();
            if (current != null && current.roomId == "PAN-001")
            {
                if (GUI.Button(new Rect(Screen.width - 215, 83, 200, 28), "공간 탐색 · 체험 유지", buttonStyle)) ReturnToRooms();
                return;
            }
            float sidebar = Mathf.Min(Screen.width * .42f, Mathf.Max(225, Screen.width * .23f));
            GUI.Box(new Rect(0, 0, sidebar, Screen.height), "");
            GUI.Label(new Rect(18, 15, sidebar - 30, 45), "직업 공간 탐색", titleStyle);
            int available = Array.FindAll(registry.rooms, room => room.available).Length;
            GUI.Label(new Rect(18, 65, sidebar - 30, 50), available + " / " + registry.rooms.Length + " 공간 · 탐색 가능", textStyle);
            scroll = GUI.BeginScrollView(new Rect(10, 125, sidebar - 20, Screen.height - 145), scroll, new Rect(0, 0, sidebar - 44, registry.rooms.Length * 65));
            if(Event.current.type==EventType.Repaint)roomButtons.Clear();
            for (int i = 0; i < registry.rooms.Length; i++)
            {
                WorkplaceRoom room = registry.rooms[i]; GUI.enabled = room.available && !loading && !PilotRuntime.InputCaptured;
                if(Event.current.type==EventType.Repaint)
                {
                    float y=125+i*65+29-scroll.y;
                    roomButtons.Add(new RoomButton {roomId=room.roomId,x=10+(sidebar-48)/2,y=y,visible=y>=145&&y<Screen.height-35,available=room.available});
                }
                if (GUI.Button(new Rect(0, i * 65, sidebar - 48, 58), room.panoramaId + "  " + room.name + (room.available ? "" : "\n제작 대기"), buttonStyle)) SelectRoom(room.roomId);
            }
            GUI.enabled = true; GUI.EndScrollView();
            if (current != null)
            {
                GUI.Label(new Rect(sidebar + 22, 18, Screen.width - sidebar - 45, 40), current.name, titleStyle);
                GUI.Label(new Rect(sidebar + 22, 55, Screen.width - sidebar - 45, 50), "드래그·방향키: 회전  /  휠·+/−: 확대  /  P·Esc: 일시정지", textStyle);
                GUI.Label(new Rect(sidebar + 22, Screen.height - 65, Screen.width - sidebar - 45, 60), paused ? "일시정지 · P 또는 Esc로 계속" : selected.Length > 0 ? "선택한 물건: " + selected : "오른쪽에서 직업 체험을 선택할 수 있습니다. 사무보조원 업무는 공용 업무 사무실에서 체험합니다.", textStyle);
            }
            if (loading) GUI.Label(new Rect(sidebar + 25, 120, 500, 50), "공간을 불러오는 중…", titleStyle);
        }
        void Publish()
        {
            if (registry == null || current == null) return;
            var mats = new HashSet<Material>(); var images = new HashSet<Texture>(); int triangles = 0, count = 0;
            foreach (MeshFilter filter in FindObjectsByType<MeshFilter>(FindObjectsSortMode.None))
            {
                if (filter.sharedMesh == null) continue;
                triangles += filter.sharedMesh.triangles.Length / 3; count++;
                var renderer = filter.GetComponent<Renderer>(); if (renderer == null) continue;
                foreach (var material in renderer.sharedMaterials) { mats.Add(material); if (material != null && material.mainTexture != null) images.Add(material.mainTexture); }
            }
            var palette=images.Count==1?System.Linq.Enumerable.First(images):null;
            string json = JsonUtility.ToJson(new Snapshot { buildId = registry.buildId, roomId = current.roomId, name = current.name, panoramaId = current.panoramaId, scenePath = current.scenePath, selected = selected, selectedInstance=selectedInstance, unity = Application.unityVersion,textureWidth=palette==null?0:palette.width,textureHeight=palette==null?0:palette.height,
                availableRooms = Array.FindAll(registry.rooms, room => room.available).Length, triangles = current.triangles, instances = current.instances, measuredTriangles = triangles, renderers = count, materials = mats.Count, textures = images.Count,
                loading = loading, paused = paused, yaw = yaw, pitch = pitch, distance = distance, menuScrollY=scroll.y, buttons=roomButtons.ToArray() });
#if UNITY_WEBGL && !UNITY_EDITOR
            PublishWorkplaceState(json);
#else
            Debug.Log("WORKPLACE_STATE " + json);
#endif
        }
    }
}

using System;
using System.IO;
using System.Linq;
using CareerExperience;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEngine;

// Application acceptance runner, explicitly invoked. No hooks or catalog/status mutations.
public static class OfficeEditorPlay
{
    // Explicit application Play Mode acceptance for the new multi-room player.
    // Extends the existing runner; no startup hook or catalog-writing gate.
    [Serializable] class WorkplacePlayReport
    {
        public int schema_version=3;
        public string build_id,checked_at,unity,environment="Actual Unity Editor Play Mode / batchmode -nographics; visual rendering is separately verified in HTTP WebGL",status,error;
        public WorkplacePlayCase[] rooms;
    }
    [Serializable] class WorkplacePlayCase
    {
        public string room_id,scene_path,status,checked_at;
        public int triangles,renderers,materials,textures,colliders,interactive_objects,texture_width,texture_height;
    }
    static CareerExperience.WorkplaceRegistry workplaceRegistry;
    static System.Collections.Generic.List<WorkplacePlayCase> workplaceCases;
    static int workplaceIndex;
    static double workplaceStarted;
    static bool workplaceOldOptions;
    static EnterPlayModeOptions workplaceOptions;
    public static void RunWorkplaces()
    {
        workplaceRegistry=JsonUtility.FromJson<CareerExperience.WorkplaceRegistry>(File.ReadAllText("Assets/Resources/workplace-registry.json"));
        workplaceCases=new System.Collections.Generic.List<WorkplacePlayCase>();workplaceIndex=0;
        workplaceOldOptions=EditorSettings.enterPlayModeOptionsEnabled;workplaceOptions=EditorSettings.enterPlayModeOptions;
        EditorSettings.enterPlayModeOptionsEnabled=true;EditorSettings.enterPlayModeOptions=EnterPlayModeOptions.DisableDomainReload;
        var first=workplaceRegistry.rooms.First(r=>r.available&&r.roomId!="PAN-001");
        EditorSceneManager.OpenScene(first.scenePath);
        EditorApplication.update+=WorkplaceUpdate;workplaceStarted=EditorApplication.timeSinceStartup;
        EditorApplication.isPlaying=true;
    }
    static void WorkplaceUpdate()
    {
        if(!EditorApplication.isPlaying||EditorApplication.isCompiling)return;
        try
        {
            Assert(EditorApplication.timeSinceStartup-workplaceStarted<90,"Room Play Mode load timeout");
            var navigator=UnityEngine.Object.FindFirstObjectByType<CareerExperience.WorkplaceExplorer>();if(navigator==null)return;
            var target=workplaceRegistry.rooms[workplaceIndex];
            if(UnityEngine.SceneManagement.SceneManager.GetActiveScene().path!=target.scenePath){navigator.SelectRoom(target.roomId);return;}
            if(EditorApplication.timeSinceStartup-workplaceStarted<.6)return;
            var filters=UnityEngine.Object.FindObjectsByType<MeshFilter>(FindObjectsSortMode.None);
            var renderers=UnityEngine.Object.FindObjectsByType<MeshRenderer>(FindObjectsSortMode.None);
            var materials=renderers.SelectMany(r=>r.sharedMaterials).Distinct().ToArray();
            var textures=materials.Where(m=>m!=null&&m.mainTexture!=null).Select(m=>m.mainTexture).Distinct().ToArray();
            int triangles=filters.Sum(f=>f.sharedMesh.triangles.Length/3);
            int colliders=UnityEngine.Object.FindObjectsByType<MeshCollider>(FindObjectsSortMode.None).Length;
            var office=UnityEngine.Object.FindFirstObjectByType<CareerExperience.OfficeDirectExperience>();
            Assert(triangles==target.triangles&&triangles<=5000,"Play Mode triangle mismatch "+target.roomId);
            Assert(materials.Length==1&&textures.Length==1,"Play Mode material/texture mismatch "+target.roomId);
            Assert(textures[0].width==2508&&textures[0].height==2508,"Play Mode palette resolution changed "+target.roomId);
            Assert(filters.Length>0&&colliders==filters.Length,"Actual mesh/collider missing "+target.roomId);
            if(target.roomId=="PAN-001")Assert(office!=null&&office.Session!=null&&office.bindings.Length==3,"Direct office setup missing");
            workplaceCases.Add(new WorkplacePlayCase{room_id=target.roomId,scene_path=target.scenePath,status="pass",checked_at=DateTimeOffset.Now.ToString("o"),triangles=triangles,renderers=renderers.Length,materials=materials.Length,textures=textures.Length,texture_width=textures[0].width,texture_height=textures[0].height,colliders=colliders,interactive_objects=office==null?0:office.bindings.Length});
            Debug.Log("WORKPLACE_EDITOR_PLAY "+target.roomId+" "+triangles);
            workplaceIndex++;workplaceStarted=EditorApplication.timeSinceStartup;
            if(workplaceIndex>=workplaceRegistry.rooms.Length)WorkplaceFinish(null);
            else navigator.SelectRoom(workplaceRegistry.rooms[workplaceIndex].roomId);
        }
        catch(Exception error){WorkplaceFinish(error.ToString());}
    }
    static void WorkplaceFinish(string error)
    {
        EditorApplication.update-=WorkplaceUpdate;
        EditorSettings.enterPlayModeOptions=workplaceOptions;EditorSettings.enterPlayModeOptionsEnabled=workplaceOldOptions;
        var result=new WorkplacePlayReport{build_id=workplaceRegistry.buildId,checked_at=DateTimeOffset.Now.ToString("o"),unity=Application.unityVersion,status=error==null?"pass":"fail",error=error,rooms=workplaceCases.ToArray()};
        string repository=Path.GetFullPath(Path.Combine(Application.dataPath,"../../../.."));string folder=Path.Combine(repository,"docs/machine/evidence/"+workplaceRegistry.buildId);Directory.CreateDirectory(folder);
        File.WriteAllText(Path.Combine(folder,"unity-editor-play-rooms.json"),JsonUtility.ToJson(result,true));
        EditorApplication.Exit(error==null?0:1);
    }
    const string Key = "OfficeAcceptance.PlayRun";
    static int phase;
    static double time;
    static Report report;
    static bool oldPlayOptionsEnabled;
    static EnterPlayModeOptions oldPlayOptions;
    [Serializable] public class Report { public int schema_version = 3; public string status, checked_at, unity, environment = "Actual Unity Editor Play Mode, batchmode -nographics", error; public AcceptanceReport state_machine; public OfficeSnapshot completion, reset; public RayCheck[] mesh_ray_checks; }
    [Serializable] public class RayCheck { public string object_id; public bool visible_surface_hit; }
    public static void Run()
    {
        EditorSceneManager.OpenScene("Assets/Scenes/OfficeAssistant.unity");
        phase = 0; report = null;
        oldPlayOptionsEnabled = EditorSettings.enterPlayModeOptionsEnabled;
        oldPlayOptions = EditorSettings.enterPlayModeOptions;
        // Keep this explicitly invoked runner alive across Play Mode entry; restore settings on exit.
        EditorSettings.enterPlayModeOptionsEnabled = true;
        EditorSettings.enterPlayModeOptions = EnterPlayModeOptions.DisableDomainReload;
        EditorApplication.update += Update;
        SessionState.SetBool(Key, true);
        EditorApplication.isPlaying = true;
    }
    static void Assert(bool ok, string message) { if (!ok) throw new Exception(message); }
    static void Update()
    {
        if (!SessionState.GetBool(Key, false) || !EditorApplication.isPlaying || EditorApplication.isCompiling) return;
        try
        {
            var app = UnityEngine.Object.FindFirstObjectByType<OfficeExperience>();
            if (app == null || app.Session == null) return;
            var s = app.Session;
            if (phase == 0)
            {
                report = new Report { unity = Application.unityVersion, checked_at = DateTimeOffset.Now.ToString("o"), state_machine = OfficeAcceptance.Run(s.Data) };
                Assert(report.state_machine.failed == 0, "State machine suite");
                Assert(app.Diagnostic().triangles == 4308 && app.bindings.Length == 3, "Scene counts");
                Physics.SyncTransforms();
                report.mesh_ray_checks = app.bindings.Select(b => {
                    bool hit = false; Bounds bounds = b.renderer.bounds;
                    for (int x = -1; x <= 1; x++) for (int y = -1; y <= 1; y++) for (int z = -1; z <= 1; z++)
                    {
                        Vector3 point = bounds.center + Vector3.Scale(bounds.extents * .85f, new Vector3(x, y, z));
                        if (Physics.Raycast(app.viewCamera.transform.position, (point - app.viewCamera.transform.position).normalized, out RaycastHit result, 100) && result.collider == b.collider) hit = true;
                    }
                    return new RayCheck { object_id = b.id, visible_surface_hit = hit };
                }).ToArray();
                Assert(report.mesh_ray_checks.All(r => r.visible_surface_hit), "Visible selectable surface for each of three meshes");
                Assert(!s.SelectObject("copier"), "Sequence lock"); Assert(s.SelectObject("monitor"), "Monitor selection");
                foreach (string slot in s.Data.required_slots) s.Ask(slot);
                Assert(s.Confirm(true), "Request confirmation"); Assert(!s.Save(), "Date error");
                s.Edit(s.Data.document_title, s.Data.expected_date); Assert(s.Save(), "Save");
                Assert(s.SelectObject("copier"), "Copier selection"); Assert(!s.Print(s.Data.document_id, s.SavedRevision, 1), "Copies error");
                Assert(s.Print(s.Data.document_id, s.SavedRevision, 2), "Start print"); Assert(!s.Print(s.Data.document_id, s.SavedRevision, 2), "Duplicate locked");
                s.TogglePause(); time = EditorApplication.timeSinceStartup; phase = 1;
            }
            else if (phase == 1 && EditorApplication.timeSinceStartup - time > .6)
            {
                Assert(s.Stage == OfficeStage.printing && s.PrintCompletions == 0, "Pause freezes live Update");
                s.TogglePause(); phase = 2; time = EditorApplication.timeSinceStartup;
            }
            else if (phase == 2)
            {
                Assert(EditorApplication.timeSinceStartup - time < 20, "Live print timeout");
                if (s.Stage != OfficeStage.print_ready) return;
                Assert(s.PrintCompletions == 1, "One live completion"); Assert(s.SelectObject("cabinet"), "Cabinet selection");
                Assert(!s.File("인사자료"), "Wrong classification"); Assert(s.File(s.Data.expected_folder), "File");
                Assert(s.Handoff(s.Data.document_title, s.Data.expected_date, 2, s.Data.expected_folder, true), "Handoff");
                report.completion = s.Snapshot(); Assert(!s.SelectObject("monitor"), "Complete reclick");
                s.Reset(false); report.reset = s.Snapshot(); report.status = "pass"; Finish();
            }
        }
        catch (Exception e) { if (report == null) report = new Report(); report.status = "fail"; report.error = e.ToString(); Finish(); }
    }
    static void Finish()
    {
        SessionState.SetBool(Key, false);
        EditorApplication.update -= Update;
        Directory.CreateDirectory(OfficeBuild.EvidenceDirectory);
        File.WriteAllText(Path.Combine(OfficeBuild.EvidenceDirectory, "unity-editor-play.json"), JsonUtility.ToJson(report, true));
        Debug.Log("OFFICE_EDITOR_PLAY " + report.status);
        EditorSettings.enterPlayModeOptions = oldPlayOptions;
        EditorSettings.enterPlayModeOptionsEnabled = oldPlayOptionsEnabled;
        EditorApplication.Exit(report.status == "pass" ? 0 : 1);
    }
}

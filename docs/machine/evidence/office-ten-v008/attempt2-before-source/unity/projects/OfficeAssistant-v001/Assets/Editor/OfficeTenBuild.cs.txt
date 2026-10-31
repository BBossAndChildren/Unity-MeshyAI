using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using System.Security.Cryptography;
using UnityEngine;
using UnityEditor;
using UnityEditor.SceneManagement;
using UnityEditor.Build.Reporting;
using CareerExperience;

public static class OfficeTenBuild
{
    const string ScenePath="Assets/Scenes/OfficeTen.unity";
    static string Repository=>Path.GetFullPath(Path.Combine(Application.dataPath,"../../../.."));
    static string BuildId { get { var args=Environment.GetCommandLineArgs();int i=Array.IndexOf(args,"-officeTenBuildId");string id=i>=0&&i+1<args.Length?args[i+1]:"office-ten-v001";if(!System.Text.RegularExpressions.Regex.IsMatch(id,"^office-ten-v[0-9]{3,}$"))throw new Exception("Invalid build ID");return id; } }
    static string Evidence=>Path.Combine(Repository,"docs/machine/evidence/"+BuildId);
    static string Hash(byte[] bytes){using(var sha=SHA256.Create())return string.Concat(sha.ComputeHash(bytes).Select(b=>b.ToString("x2")));}
    [Serializable] public class InstanceEvidence { public string instance_id,asset_id,version,hierarchy;public int triangles;public Vector3 position,scale;public Quaternion rotation; }
    [Serializable] public class SceneEvidence { public int schema_version=3;public string build_id,scene_path,checked_at,unity,assembly_asset_id="AST-020",assembly_version="v006",palette_sha256;public int triangles,renderers,materials,textures,texture_width,texture_height,interactive_objects,scenario_count;public InstanceEvidence[] instances; }
    static string Hierarchy(Transform t)=>t.parent==null?t.name:Hierarchy(t.parent)+"/"+t.name;
    static SceneEvidence Measure(OfficeTenExperience view)
    {
        var root=view.bindings[0].renderer.transform.parent;
        var filters=root.GetComponentsInChildren<MeshFilter>();var materials=root.GetComponentsInChildren<Renderer>().SelectMany(r=>r.sharedMaterials).Where(m=>m!=null).Distinct().ToArray();
        var textures=materials.Select(m=>m.mainTexture).Where(t=>t!=null).Distinct().ToArray();
        var data=JsonUtility.FromJson<OfficeTenCatalog>(view.scenarios.text);
        if(data.scenarios.Length!=10||data.scenarios.Select(d=>d.scenario_id).Distinct().Count()!=10||data.scenarios.Any(d=>d.steps.Length!=3))throw new Exception("Expected10 unique3-object scenarios");
        if(view.bindings.Length!=3||view.bindings.Any(b=>b.renderer==null||b.collider==null))throw new Exception("Missing actual3D bindings");
        int triangles=filters.Sum(f=>f.sharedMesh.triangles.Length/3);
        if(filters.Length!=30||triangles!=4308||materials.Length!=1||textures.Length!=1||textures[0].width!=2508||textures[0].height!=2508||materials[0].color!=Color.white)throw new Exception("Office geometry/shared palette mismatch");
        string canonical=Path.Combine(Repository,"meshy/models/textures/palettes/v001/palette.png"),unity="Assets/Shared/Textures/v001/palette.png";
        if(!File.ReadAllBytes(canonical).SequenceEqual(File.ReadAllBytes(unity)))throw new Exception("Canonical palette bytes changed");
        return new SceneEvidence {build_id=BuildId,scene_path=ScenePath,checked_at=DateTimeOffset.Now.ToString("o"),unity=Application.unityVersion,triangles=triangles,renderers=filters.Length,materials=materials.Length,textures=textures.Length,texture_width=textures[0].width,texture_height=textures[0].height,interactive_objects=view.bindings.Length,scenario_count=data.scenarios.Length,palette_sha256=Hash(File.ReadAllBytes(canonical)),instances=filters.Select(f=>new InstanceEvidence{instance_id=f.name,asset_id=f.name.Substring(0,7),version=f.name.StartsWith("AST-001-")?"v002":"v001",hierarchy=Hierarchy(f.transform),triangles=f.sharedMesh.triangles.Length/3,position=f.transform.position,rotation=f.transform.rotation,scale=f.transform.lossyScale}).ToArray()};
    }

    [Serializable] class ChairFacingRow { public string chair_instance_id,desk_instance_id; public float yaw_change_degrees,facing_dot;public Vector3 chair_front_world,desk_direction_world; }
    [Serializable] class ChairFacingReport { public int schema_version=3; public string build_id,checked_at,front_axis_basis="AST-003 v001 Blender chair front is negative local Y; backrest source center is positiveY .205m.";public ChairFacingRow[] chairs; }
    static void FaceChairsTowardDesks(OfficeTenExperience view)
    {
        var root=view.bindings[0].renderer.transform.parent;
        var chairs=root.GetComponentsInChildren<MeshFilter>().Where(m=>m.name.StartsWith("AST-003-")).Select(m=>m.transform).ToArray();
        var desks=root.GetComponentsInChildren<MeshFilter>().Where(m=>m.name.StartsWith("AST-004-")).Select(m=>m.transform).ToArray();
        if(chairs.Length!=2||desks.Length!=2)throw new Exception("Expected two office chair/desk pairs");
        var rows=new List<ChairFacingRow>();
        foreach(var chair in chairs)
        {
            var desk=desks.OrderBy(t=>(t.position-chair.position).sqrMagnitude).First();
            Vector3 target=Vector3.ProjectOnPlane(desk.position-chair.position,Vector3.up).normalized;
            Vector3 before=Vector3.ProjectOnPlane(chair.TransformDirection(Vector3.down),Vector3.up).normalized;
            float yaw=Vector3.SignedAngle(before,target,Vector3.up);
            chair.rotation=Quaternion.AngleAxis(yaw,Vector3.up)*chair.rotation;
            Vector3 front=Vector3.ProjectOnPlane(chair.TransformDirection(Vector3.down),Vector3.up).normalized;
            float dot=Vector3.Dot(front,target);if(dot<.999f)throw new Exception("Chair does not face its desk: "+chair.name);
            rows.Add(new ChairFacingRow{chair_instance_id=chair.name,desk_instance_id=desk.name,yaw_change_degrees=yaw,facing_dot=dot,chair_front_world=front,desk_direction_world=target});
        }
        File.WriteAllText(Path.Combine(Evidence,"chair-facing.json"),JsonUtility.ToJson(new ChairFacingReport{build_id=BuildId,checked_at=DateTimeOffset.Now.ToString("o"),chairs=rows.ToArray()},true));
    }

    public static void Prepare()
    {
        Directory.CreateDirectory(Evidence);
        EditorSceneManager.OpenScene("Assets/Scenes/OfficeAssistantDirect.unity");
        var old=UnityEngine.Object.FindFirstObjectByType<OfficeDirectExperience>();if(old==null)throw new Exception("Preserved office direct source missing");
        var view=old.gameObject.AddComponent<OfficeTenExperience>();view.scenarios=AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Resources/office-ten-scenarios.json");view.koreanFont=old.koreanFont;view.viewCamera=old.viewCamera;view.bindings=old.bindings;
        if(view.scenarios==null)throw new Exception("Ten-job dataset missing");
        FaceChairsTowardDesks(view);
        UnityEngine.Object.DestroyImmediate(old);
        foreach(var explorer in UnityEngine.Object.FindObjectsByType<WorkplaceExplorer>(FindObjectsSortMode.None))UnityEngine.Object.DestroyImmediate(explorer.gameObject);
        foreach(var protocol in UnityEngine.Object.FindObjectsByType<CareerProtocol>(FindObjectsSortMode.None))UnityEngine.Object.DestroyImmediate(protocol.gameObject);
        var tenProtocol=new GameObject("CareerProtocol").AddComponent<OfficeTenProtocol>();tenProtocol.buildId=BuildId;
        EditorSceneManager.SaveScene(UnityEngine.SceneManagement.SceneManager.GetActiveScene(),ScenePath);
        File.WriteAllText(Path.Combine(Evidence,"unity-scene.json"),JsonUtility.ToJson(Measure(view),true));
        EditorBuildSettings.scenes=new[]{new EditorBuildSettingsScene(ScenePath,true)};
        PlayerSettings.companyName="Career Practice";PlayerSettings.productName="Office Careers";PlayerSettings.defaultScreenWidth=1440;PlayerSettings.defaultScreenHeight=900;
        PlayerSettings.WebGL.compressionFormat=WebGLCompressionFormat.Disabled;PlayerSettings.WebGL.decompressionFallback=false;PlayerSettings.WebGL.dataCaching=false;
        PlayerSettings.WebGL.template="PROJECT:Workplaces";PlayerSettings.runInBackground=true;PlayerSettings.colorSpace=ColorSpace.Linear;
        AssetDatabase.SaveAssets();Debug.Log("OFFICE_TEN_PREPARED10");
    }
    public static void Build()
    {
        string output=Path.Combine(Repository,"unity/webgl/builds/"+BuildId);if(Directory.Exists(output))throw new Exception("Existing build preserved; choose new ID");
        Prepare();var report=BuildPipeline.BuildPlayer(new BuildPlayerOptions{scenes=new[]{ScenePath},locationPathName=output,target=BuildTarget.WebGL,options=BuildOptions.Development});
        var result=new OfficeBuild.BuildResult{build_id=BuildId,unity=Application.unityVersion,result=report.summary.result.ToString(),checked_at=DateTimeOffset.Now.ToString("o"),bytes=(long)report.summary.totalSize,errors=report.summary.totalErrors,warnings=report.summary.totalWarnings,duration_seconds=report.summary.totalTime.TotalSeconds};
        File.WriteAllText(Path.Combine(Evidence,"build-result.json"),JsonUtility.ToJson(result,true));if(report.summary.result!=BuildResult.Succeeded)throw new Exception("Ten-job build failed");
        File.Copy("Assets/Resources/office-ten-scenarios.json",Path.Combine(output,"office-ten-scenarios.json"),false);
    }
    [Serializable] class NativeRow {public string scenario_id,version,name,status,checked_at;public int triangles,renderers,interactive_objects;}
    [Serializable] class NativeReport {public int schema_version=3;public string build_id,checked_at,status,error,environment="Actual Unity Editor Play Mode batchmode-nographics; scenario selection/geometry/bindings only; native workflow GUI not exercised";public NativeRow[] scenarios;}
    static readonly List<NativeRow> nativeRows=new List<NativeRow>();static OfficeTenCatalog nativeCatalog;static int nativeIndex,nativeTicks;static bool oldOptionsEnabled;static EnterPlayModeOptions oldOptions;
    public static void RunEditorPlay()
    {
        Prepare();EditorSceneManager.OpenScene(ScenePath);nativeRows.Clear();nativeIndex=nativeTicks=0;
        nativeCatalog=JsonUtility.FromJson<OfficeTenCatalog>(AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Resources/office-ten-scenarios.json").text);
        oldOptionsEnabled=EditorSettings.enterPlayModeOptionsEnabled;oldOptions=EditorSettings.enterPlayModeOptions;EditorSettings.enterPlayModeOptionsEnabled=true;EditorSettings.enterPlayModeOptions=EnterPlayModeOptions.DisableDomainReload;
        EditorApplication.update+=NativeTick;EditorApplication.isPlaying=true;
    }
    static void NativeTick()
    {
        if(!EditorApplication.isPlaying||++nativeTicks<10||nativeTicks%5!=0)return;
        try
        {
            if(nativeIndex>=nativeCatalog.scenarios.Length){FinishNative(null);return;}
            var view=UnityEngine.Object.FindFirstObjectByType<OfficeTenExperience>();if(view==null)throw new Exception("Actual playing controller missing");
            var data=nativeCatalog.scenarios[nativeIndex];var protocol=OfficeTenProtocol.Get();protocol.SelectScenario(data,view);view.BeginExternalRun();
            if(protocol.buildId!=BuildId||protocol.SelectedData.scenario_id!=data.scenario_id||view.Session.Data.scenario_id!=data.scenario_id)throw new Exception("Actual build/scenario selection mismatch");
            var measured=Measure(view);nativeRows.Add(new NativeRow{scenario_id=data.scenario_id,version=data.version,name=data.name,status="pass",checked_at=DateTimeOffset.Now.ToString("o"),triangles=measured.triangles,renderers=measured.renderers,interactive_objects=measured.interactive_objects});nativeIndex++;
        }catch(Exception e){FinishNative(e.ToString());}
    }
    static void FinishNative(string error)
    {
        EditorApplication.update-=NativeTick;EditorSettings.enterPlayModeOptionsEnabled=oldOptionsEnabled;EditorSettings.enterPlayModeOptions=oldOptions;
        File.WriteAllText(Path.Combine(Evidence,"unity-editor-play.json"),JsonUtility.ToJson(new NativeReport{build_id=BuildId,checked_at=DateTimeOffset.Now.ToString("o"),status=error==null?"pass":"fail",error=error,scenarios=nativeRows.ToArray()},true));
        EditorApplication.Exit(error==null?0:1);
    }
}

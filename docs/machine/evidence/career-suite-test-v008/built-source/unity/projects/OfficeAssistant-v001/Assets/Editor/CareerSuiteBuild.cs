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

// Production build entry points for two deliveries from the same logical project.
public static class CareerSuiteBuild
{
    static string Repository => Path.GetFullPath(Path.Combine(Application.dataPath,"../../../.."));
    static string Argument(string name,string fallback) { var a=Environment.GetCommandLineArgs();int i=Array.IndexOf(a,name);return i>=0&&i+1<a.Length?a[i+1]:fallback; }
    [Serializable] public class Settings { public int schema_version=3;public string buildId,mode,officeDirectScenePath="Assets/Scenes/OfficeAssistantDirect.unity",officeTenScenePath="Assets/Scenes/OfficeTen.unity";public bool integrationOnly; }
    [Serializable] public class SceneRow { public string scene_path;public int triangles,renderers;public string[] nodes; }
    [Serializable] public class SceneReport { public int schema_version=3;public string build_id,checked_at;public SceneRow[] scenes; }
    [Serializable] public class FileRow { public string path,sha256; }
    [Serializable] public class SourceReport { public int schema_version=3;public string build_id,checked_at;public FileRow[] files; }
    static string Hash(string path) { using(var h=SHA256.Create())return string.Concat(h.ComputeHash(File.ReadAllBytes(path)).Select(b=>b.ToString("x2"))); }
    public static void Build()
    {
        string mode=Argument("-careerSuiteMode","test"),id=Argument("-careerSuiteBuildId","career-suite-"+mode+"-v001");
        if(mode!="test"&&mode!="integration")throw new Exception("Unknown suite mode");
        if(!System.Text.RegularExpressions.Regex.IsMatch(id,"^career-suite-(test|integration)-v[0-9]{3,}$"))throw new Exception("Invalid suite build ID");
        string output=Path.Combine(Repository,"unity/webgl/builds",id),evidence=Path.Combine(Repository,"docs/machine/evidence",id);
        if(Directory.Exists(output))throw new Exception("Existing output is immutable; choose a new build ID");
        Directory.CreateDirectory(evidence);
        const string registryPath="Assets/Resources/workplace-registry.json",settingsPath="Assets/Resources/career-suite-settings.json";
        byte[] originalRegistry=File.ReadAllBytes(registryPath),originalSettings=File.Exists(settingsPath)?File.ReadAllBytes(settingsPath):null;
        var previousScenes=EditorBuildSettings.scenes;string previousTemplate=PlayerSettings.WebGL.template;
        try
        {
            var registry=JsonUtility.FromJson<WorkplaceRegistry>(System.Text.Encoding.UTF8.GetString(originalRegistry).TrimStart('\uFEFF'));
            var frozen=JsonUtility.FromJson<WorkplaceRegistry>(File.ReadAllText(Path.Combine(Repository,"unity/projects/CareerPilotTen-v001/Assets/Resources/workplace-registry.json")));
            foreach(var old in frozen.rooms.Where(r=>r.available&&r.roomId!="PAN-001")) { int i=Array.FindIndex(registry.rooms,r=>r.roomId==old.roomId);if(i>=0)registry.rooms[i]=old; }
            registry.buildId=id;
            if(registry.rooms.Length!=71||registry.rooms.Any(r=>!r.available||!File.Exists(r.scenePath)))throw new Exception("71 actual room scenes required");
            File.WriteAllText(registryPath,JsonUtility.ToJson(registry,true));
            File.Copy(registryPath,Path.Combine(evidence,"registry-source.json"),false);
            var settings=new Settings{buildId=id,mode=mode,integrationOnly=mode=="integration"};
            File.WriteAllText(settingsPath,JsonUtility.ToJson(settings,true));
            AssetDatabase.Refresh(ImportAssetOptions.ForceSynchronousImport);
            var scenes=registry.rooms.OrderBy(r=>r.roomId=="PAN-002"?0:1).Select(r=>r.scenePath).Concat(new[]{settings.officeDirectScenePath,settings.officeTenScenePath}).Distinct().ToArray();
            var rows=new List<SceneRow>();
            foreach(string path in scenes)
            {
                if(!File.Exists(path))throw new Exception("Missing scene "+path);
                var scene=EditorSceneManager.OpenScene(path);var roots=scene.GetRootGameObjects();
                var meshes=roots.SelectMany(r=>r.GetComponentsInChildren<MeshFilter>(true)).Where(m=>m.sharedMesh!=null).ToArray();
                rows.Add(new SceneRow{scene_path=path,triangles=meshes.Sum(m=>m.sharedMesh.triangles.Length/3),renderers=meshes.Length,nodes=roots.SelectMany(r=>r.GetComponentsInChildren<Transform>(true)).Select(t=>t.name).ToArray()});
            }
            File.WriteAllText(Path.Combine(evidence,"unity-scenes.json"),JsonUtility.ToJson(new SceneReport{build_id=id,checked_at=DateTimeOffset.Now.ToString("o"),scenes=rows.ToArray()},true));
            EditorBuildSettings.scenes=scenes.Select(s=>new EditorBuildSettingsScene(s,true)).ToArray();
            PlayerSettings.WebGL.template="PROJECT:"+(mode=="test"?"CareerSuiteTest":"CareerSuiteIntegration");
            PlayerSettings.WebGL.compressionFormat=WebGLCompressionFormat.Disabled;PlayerSettings.WebGL.decompressionFallback=false;PlayerSettings.WebGL.dataCaching=false;
            PlayerSettings.defaultScreenWidth=1440;PlayerSettings.defaultScreenHeight=900;PlayerSettings.runInBackground=true;
            PlayerSettings.companyName="Career Practice";PlayerSettings.productName=mode=="test"?"71 Career Spaces Test":"71 Career Spaces Integration";
            PlayerSettings.SetManagedStrippingLevel(UnityEditor.Build.NamedBuildTarget.WebGL,ManagedStrippingLevel.Low);
            AssetDatabase.SaveAssets();
            var projectSources=Directory.GetFiles("Assets/Scripts","*",SearchOption.AllDirectories).Concat(Directory.GetFiles("Assets/Plugins","*",SearchOption.AllDirectories)).Concat(Directory.GetFiles("Assets/Resources","*.json")).Concat(Directory.GetFiles("Assets/WebGLTemplates/"+(mode=="test"?"CareerSuiteTest":"CareerSuiteIntegration"),"*",SearchOption.AllDirectories)).Concat(Directory.GetFiles("ProjectSettings","*",SearchOption.TopDirectoryOnly)).Concat(Directory.GetFiles("Packages","*.json")).Concat(scenes).Concat(new[]{settingsPath,registryPath,"Assets/Editor/CareerSuiteBuild.cs"}).Select(p=>p.Replace('\\','/')).Distinct(StringComparer.OrdinalIgnoreCase).Select(p=>new FileRow{path="unity/projects/OfficeAssistant-v001/"+p,sha256=Hash(p)});
            string frontend=Path.Combine(Repository,"web/career-preview/v003");
            var frontendSources=Directory.Exists(frontend)?Directory.GetFiles(frontend,"*",SearchOption.AllDirectories).Where(p=>!p.Replace('\\','/').Contains("/node_modules/")).Select(p=>new FileRow{path="web/career-preview/v003/"+Path.GetRelativePath(frontend,p).Replace('\\','/'),sha256=Hash(p)}):Enumerable.Empty<FileRow>();
            var sources=projectSources.Concat(frontendSources).ToArray();
            foreach(var source in sources)
            {
                string saved=Path.Combine(evidence,"built-source",source.path);Directory.CreateDirectory(Path.GetDirectoryName(saved));
                File.Copy(Path.Combine(Repository,source.path),saved,false);
            }
            File.WriteAllText(Path.Combine(evidence,"built-source.json"),JsonUtility.ToJson(new SourceReport{build_id=id,checked_at=DateTimeOffset.Now.ToString("o"),files=sources},true));
            var report=BuildPipeline.BuildPlayer(new BuildPlayerOptions{scenes=scenes,locationPathName=output,target=BuildTarget.WebGL,options=mode=="test"?BuildOptions.Development:BuildOptions.None});
            File.WriteAllText(Path.Combine(evidence,"build-result.json"),JsonUtility.ToJson(new OfficeBuild.BuildResult{build_id=id,unity=Application.unityVersion,result=report.summary.result.ToString(),checked_at=DateTimeOffset.Now.ToString("o"),bytes=(long)report.summary.totalSize,errors=report.summary.totalErrors,warnings=report.summary.totalWarnings,duration_seconds=report.summary.totalTime.TotalSeconds},true));
            if(report.summary.result!=BuildResult.Succeeded)throw new Exception("Suite WebGL build failed");
            File.Copy(settingsPath,Path.Combine(output,"suite-settings.json"),false);
            File.Copy(registryPath,Path.Combine(output,"workplace-registry.json"),false);
        }
        finally
        {
            File.WriteAllBytes(registryPath,originalRegistry);
            if(originalSettings!=null)File.WriteAllBytes(settingsPath,originalSettings);else File.WriteAllText(settingsPath,JsonUtility.ToJson(new Settings{buildId="editor-suite",mode="test",integrationOnly=false},true));
            EditorBuildSettings.scenes=previousScenes;PlayerSettings.WebGL.template=previousTemplate;AssetDatabase.Refresh();AssetDatabase.SaveAssets();
        }
    }
}

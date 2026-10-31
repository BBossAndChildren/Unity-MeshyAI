using System;
using System.IO;
using System.Linq;
using System.Collections.Generic;
using CareerExperience;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.Rendering;

// An additive repair build: existing fixed FBX files, scenes and builds stay intact.
public static class WorshipBuild
{
    static string Id {
        get {var args=Environment.GetCommandLineArgs();int at=Array.IndexOf(args,"-worshipBuildId");return at>=0?args[at+1]:"workplaces-v007";}
    }
    static string Repo=>Path.GetFullPath(Path.Combine(Application.dataPath,"../../../.."));
    static string Evidence=>Path.Combine(Repo,"docs/machine/evidence/"+Id);
    [Serializable] class Placements { public int schema_version;public Placement[] instances; }
    [Serializable] class Copies {public int schema_version;public AssetCopy[] assets;public string[] room_ids;}
    [Serializable] class AssetCopy {public string asset_id,version,source_path,target_path,prefab_path;public bool imported;}
    [Serializable] class Placement { public string asset_id,version,instance_id; }
    [Serializable] class Instance {
        public string instance_id,asset_id,version,hierarchy;
        public int mesh_count,triangles;public Vector3 position,scale;public Quaternion rotation;
    }
    [Serializable] class SceneReport {
        public int schema_version=3;public string build_id=Id,room_id,scene_path,checked_at,unity;
        public int triangles,renderers,material_count,texture_count;public Instance[] instances;
    }
    static string Hierarchy(Transform t)=>t.parent==null?t.name:Hierarchy(t.parent)+"/"+t.name;
    public static void Build()
    {
        string output=Path.Combine(Repo,"unity/webgl/builds/"+Id);
        if(Directory.Exists(output))throw new Exception("Existing build preserved "+output);
        Directory.CreateDirectory(Evidence);
        var json=AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Resources/workplace-registry.json");
        var registry=JsonUtility.FromJson<WorkplaceRegistry>(json.text);
        if(registry.buildId!=Id)throw new Exception("Expected new registry build ID");
        var material=AssetDatabase.LoadAssetAtPath<Material>("Assets/Shared/Materials/OfficePalette.mat");
        var font=AssetDatabase.LoadAssetAtPath<Font>("Assets/Resources/KoreanUI.otf");
        var args=Environment.GetCommandLineArgs();int inputAt=Array.IndexOf(args,"-spatialImportsPath");
        string importsPath=inputAt>=0?args[inputAt+1]:"Assets/Resources/worship-imports.json";
        var copies=JsonUtility.FromJson<Copies>(File.ReadAllText(importsPath));
        foreach(var copy in copies.assets)
        {
            Directory.CreateDirectory(Path.GetDirectoryName(copy.target_path));byte[] bytes=File.ReadAllBytes(Path.Combine(Repo,copy.source_path));
            if(File.Exists(copy.target_path)&&!File.ReadAllBytes(copy.target_path).SequenceEqual(bytes))throw new Exception("Existing prop version preserved");
            if(!File.Exists(copy.target_path))File.WriteAllBytes(copy.target_path,bytes);
            AssetDatabase.ImportAsset(copy.target_path,ImportAssetOptions.ForceSynchronousImport);
            var importer=(ModelImporter)AssetImporter.GetAtPath(copy.target_path);importer.materialImportMode=ModelImporterMaterialImportMode.None;importer.importAnimation=false;importer.isReadable=true;importer.SaveAndReimport();
            if(!File.Exists(copy.prefab_path))
            {
                var prop=(GameObject)PrefabUtility.InstantiatePrefab(AssetDatabase.LoadAssetAtPath<GameObject>(copy.target_path));prop.name=copy.asset_id+"_"+copy.version;
                foreach(var renderer in prop.GetComponentsInChildren<MeshRenderer>()){renderer.sharedMaterial=material;var collider=renderer.gameObject.AddComponent<MeshCollider>();collider.sharedMesh=renderer.GetComponent<MeshFilter>().sharedMesh;}
                PrefabUtility.SaveAsPrefabAsset(prop,copy.prefab_path);UnityEngine.Object.DestroyImmediate(prop);
            }
            copy.imported=AssetDatabase.LoadAssetAtPath<GameObject>(copy.prefab_path)!=null;
        }
        File.WriteAllText(Path.Combine(Evidence,"component-imports.json"),JsonUtility.ToJson(copies,true));
        foreach(var room in registry.rooms.Where(r=>(copies.room_ids??new[]{"PAN-064","PAN-071"}).Contains(r.roomId)))
        {
            string source=Path.Combine(Repo,room.sourceFbxPath);
            string target="Assets/Meshy/"+room.assetId+"/"+room.assetVersion+"/room.fbx";
            Directory.CreateDirectory(Path.GetDirectoryName(target));
            if(File.Exists(target)&&!File.ReadAllBytes(target).SequenceEqual(File.ReadAllBytes(source)))throw new Exception("Existing room import preserved "+target);
            if(!File.Exists(target))File.Copy(source,target);AssetDatabase.ImportAsset(target,ImportAssetOptions.ForceSynchronousImport);
            var importer=(ModelImporter)AssetImporter.GetAtPath(target);
            importer.materialImportMode=ModelImporterMaterialImportMode.None;importer.importAnimation=false;importer.isReadable=true;importer.SaveAndReimport();
            OfficeDirectExperience officeDirect=null;Transform oldOfficeRoot=null;
            if(room.roomId=="PAN-001")
            {
                EditorSceneManager.OpenScene("Assets/Scenes/OfficeAssistantDirect.unity");
                officeDirect=UnityEngine.Object.FindFirstObjectByType<OfficeDirectExperience>();
                if(officeDirect==null)throw new Exception("Preserved office direct source missing");
                oldOfficeRoot=officeDirect.bindings[0].renderer.transform.parent;
            }
            else EditorSceneManager.NewScene(NewSceneSetup.EmptyScene,NewSceneMode.Single);
            var root=(GameObject)PrefabUtility.InstantiatePrefab(AssetDatabase.LoadAssetAtPath<GameObject>(target));root.name="Room_"+room.roomId;
            foreach(var renderer in root.GetComponentsInChildren<MeshRenderer>())
            {
                renderer.sharedMaterial=material;var collider=renderer.gameObject.AddComponent<MeshCollider>();collider.sharedMesh=renderer.GetComponent<MeshFilter>().sharedMesh;
            }
            if(officeDirect!=null)
            {
                root.transform.SetPositionAndRotation(oldOfficeRoot.position,oldOfficeRoot.rotation);root.transform.localScale=oldOfficeRoot.localScale;
                string[] names={"AST-005-0","AST-009-0","AST-015-0"};
                for(int i=0;i<names.Length;i++)
                {
                    var t=root.GetComponentsInChildren<Transform>().Single(x=>x.name==names[i]);
                    officeDirect.bindings[i].renderer=t.GetComponent<Renderer>();officeDirect.bindings[i].collider=t.GetComponent<MeshCollider>();
                    if(officeDirect.bindings[i].renderer==null||officeDirect.bindings[i].collider==null)throw new Exception("Actual office mesh binding missing "+names[i]);
                }
                UnityEngine.Object.DestroyImmediate(oldOfficeRoot.gameObject);
            }
            else
            {
            var clear=new GameObject("Full frame clear").AddComponent<Camera>();clear.clearFlags=CameraClearFlags.SolidColor;clear.backgroundColor=new Color(.075f,.105f,.12f);clear.cullingMask=0;clear.depth=-10;
            var camera=new GameObject("Main Camera").AddComponent<Camera>();camera.tag="MainCamera";camera.clearFlags=CameraClearFlags.SolidColor;camera.fieldOfView=40;camera.nearClipPlane=.05f;camera.farClipPlane=40;camera.backgroundColor=clear.backgroundColor;
            Vector3 aim=new Vector3(0,.7f,0),pos=aim+Quaternion.Euler(35,145,0)*new Vector3(0,0,-9.5f);camera.transform.SetPositionAndRotation(pos,Quaternion.LookRotation(aim-pos));
            var light=new GameObject("Daylight").AddComponent<Light>();light.type=LightType.Directional;light.intensity=1.1f;light.transform.rotation=Quaternion.Euler(48,-25,0);light.shadows=LightShadows.None;
            RenderSettings.ambientMode=AmbientMode.Flat;RenderSettings.ambientLight=new Color(.72f,.75f,.78f);
            var explorer=new GameObject("WorkplaceExplorer").AddComponent<WorkplaceExplorer>();explorer.registryJson=json;explorer.koreanFont=font;
            }
            string placementPath=Path.Combine(Path.GetDirectoryName(Path.GetDirectoryName(source)),"placements.json");
            var lookup=JsonUtility.FromJson<Placements>(File.ReadAllText(placementPath)).instances.ToDictionary(p=>p.instance_id);
            var instances=root.GetComponentsInChildren<Transform>().Where(t=>lookup.ContainsKey(t.name)).Select(t=>new Instance {instance_id=t.name,asset_id=lookup[t.name].asset_id,version=lookup[t.name].version,hierarchy=Hierarchy(t),mesh_count=t.GetComponentsInChildren<MeshFilter>().Length,triangles=t.GetComponentsInChildren<MeshFilter>().Sum(f=>f.sharedMesh.triangles.Length/3),position=t.position,rotation=t.rotation,scale=t.lossyScale}).ToArray();
            int triangles=root.GetComponentsInChildren<MeshFilter>().Sum(f=>f.sharedMesh.triangles.Length/3);
            if(instances.Length!=room.instances||triangles!=room.triangles||instances.Sum(i=>i.triangles)!=triangles||triangles>5000)throw new Exception("Room geometry mismatch "+room.roomId);
            if(!File.Exists(room.scenePath))EditorSceneManager.SaveScene(UnityEngine.SceneManagement.SceneManager.GetActiveScene(),room.scenePath);
            File.WriteAllText(Path.Combine(Evidence,room.roomId+"-unity-scene.json"),JsonUtility.ToJson(new SceneReport{room_id=room.roomId,scene_path=room.scenePath,checked_at=DateTimeOffset.Now.ToString("o"),unity=Application.unityVersion,triangles=triangles,renderers=root.GetComponentsInChildren<MeshFilter>().Length,material_count=root.GetComponentsInChildren<Renderer>().SelectMany(r=>r.sharedMaterials).Distinct().Count(),texture_count=root.GetComponentsInChildren<Renderer>().SelectMany(r=>r.sharedMaterials).Select(m=>m.mainTexture).Distinct().Count(),instances=instances},true));
        }
        var paths=registry.rooms.Where(r=>r.available&&r.roomId!="PAN-001").Select(r=>r.scenePath).Concat(registry.rooms.Where(r=>r.available&&r.roomId=="PAN-001").Select(r=>r.scenePath)).ToArray();EditorBuildSettings.scenes=paths.Select(p=>new EditorBuildSettingsScene(p,true)).ToArray();
        AssetDatabase.SaveAssets();
        var report=BuildPipeline.BuildPlayer(new BuildPlayerOptions{scenes=paths,locationPathName=output,target=BuildTarget.WebGL,options=BuildOptions.Development});
        var result=new OfficeBuild.BuildResult{build_id=Id,unity=Application.unityVersion,result=report.summary.result.ToString(),checked_at=DateTimeOffset.Now.ToString("o"),bytes=(long)report.summary.totalSize,errors=report.summary.totalErrors,warnings=report.summary.totalWarnings,duration_seconds=report.summary.totalTime.TotalSeconds};
        File.WriteAllText(Path.Combine(Evidence,"build-result.json"),JsonUtility.ToJson(result,true));
        if(report.summary.result!=BuildResult.Succeeded)throw new Exception("WebGL build failed");
    }
}

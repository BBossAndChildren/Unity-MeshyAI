using System;
using System.IO;
using System.Linq;
using System.Security.Cryptography;
using CareerExperience;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.Rendering;

public static class WorkplaceBuild
{
    static string Repository => Path.GetFullPath(Path.Combine(Application.dataPath, "../../../.."));
    static string BuildId
    {
        get {
            string[] args = Environment.GetCommandLineArgs(); int i = Array.IndexOf(args, "-workplaceBuildId");
            string id = i >= 0 && i + 1 < args.Length ? args[i + 1] : "workplaces-v001";
            if (!System.Text.RegularExpressions.Regex.IsMatch(id, "^[a-z0-9]+(?:-[a-z0-9]+)*-v[0-9]{3,}$")) throw new Exception("Invalid build ID");
            return id;
        }
    }
    [Serializable] class SceneEvidence
    {
        public int schema_version = 3;
        public string build_id, room_id, scene_path, checked_at, unity;
        public int triangles, renderers, material_count, texture_count;
        public PlacementEvidence[] instances;
    }
    [Serializable] class PlacementEvidence
    {
        public string instance_id, asset_id, version, hierarchy;
        public int mesh_count, triangles;
        public Vector3 position, scale;
        public Quaternion rotation;
    }
    static string Hierarchy(Transform t) => t.parent == null ? t.name : Hierarchy(t.parent) + "/" + t.name;
    [Serializable] class CopyEvidence { public int schema_version=3; public string checked_at; public ImportedAsset[] assets; }
    [Serializable] class ImportedAsset { public string asset_id, version, source_path, unity_path, sha256, prefab_path; public bool byte_identical, imported; }
    [Serializable] class SourcePlacements { public int schema_version; public SourcePlacement[] instances; }
    [Serializable] class SourcePlacement { public string asset_id,version,instance_id; }
    static string Hash(byte[] bytes) { using(var sha=SHA256.Create()) return string.Concat(sha.ComputeHash(bytes).Select(b=>b.ToString("x2"))); }
    static string PixelHash(Texture2D texture)
    {
        var pixels=texture.GetPixels32();var bytes=new byte[pixels.Length*4];
        for(int i=0;i<pixels.Length;i++){bytes[i*4]=pixels[i].r;bytes[i*4+1]=pixels[i].g;bytes[i*4+2]=pixels[i].b;bytes[i*4+3]=pixels[i].a;}
        return Hash(bytes);
    }
    [Serializable] class PaletteEvidence
    {
        public int schema_version=3,width,height,previous_imported_width,previous_imported_height;
        public string checked_at,source_path,source_sha256,source_pixel_sha256,imported_pixel_sha256;
        public bool imported_pixels_identical,npot_resizing_disabled,compression_disabled,mipmaps_disabled,point_filtering;
    }
    [MenuItem("Workplaces/Prepare available rooms")]
    public static void Prepare()
    {
        string evidence = Path.Combine(Repository, "docs/machine/evidence/" + BuildId);
        Directory.CreateDirectory(evidence); Directory.CreateDirectory("Assets/Scenes/Workplaces");
        var registry = JsonUtility.FromJson<WorkplaceRegistry>(File.ReadAllText("Assets/Resources/workplace-registry.json"));
        registry.buildId = BuildId;
        File.WriteAllText("Assets/Resources/workplace-registry.json", JsonUtility.ToJson(registry, true));
        File.Copy("Assets/Resources/workplace-registry.json",Path.Combine(evidence,"registry-source.json"),true);
        var imports = new System.Collections.Generic.List<ImportedAsset>();
        // Import each editable prop separately as well as each assembled room.
        // Scene accounting below uses embedded component instances once only.
        foreach(string folder in Directory.GetDirectories(Path.Combine(Repository,"meshy/models/blender"),"AST-*"))
        {
            string assetId=Path.GetFileName(folder);int number;
            if(!int.TryParse(assetId.Substring(4),out number)||number<1000||number>=2000)continue;
            foreach(string versionFolder in Directory.GetDirectories(folder,"v*"))
            {
                string version=Path.GetFileName(versionFolder);if(!System.Text.RegularExpressions.Regex.IsMatch(version,"^v[0-9]{3,}$"))continue;
                string source=Path.Combine(versionFolder,"exports/model.fbx");if(!File.Exists(source))continue;
                string target="Assets/Meshy/"+assetId+"/"+version+"/model.fbx";
                Directory.CreateDirectory(Path.GetDirectoryName(target));byte[] bytes=File.ReadAllBytes(source);
                if(File.Exists(target)&&!File.ReadAllBytes(target).SequenceEqual(bytes))throw new Exception("Existing prop preserved: "+target);
                if(!File.Exists(target))File.WriteAllBytes(target,bytes);
                imports.Add(new ImportedAsset { asset_id=assetId,version=version,source_path="meshy/models/blender/"+assetId+"/"+version+"/exports/model.fbx",unity_path=target,sha256=Hash(bytes),byte_identical=true });
            }
        }
        foreach (var room in registry.rooms.Where(r => r.available && r.roomId != "PAN-001"))
        {
            string directory = "Assets/Meshy/" + room.assetId + "/" + room.assetVersion;
            Directory.CreateDirectory(directory);
            string target = directory + "/room.fbx";
            byte[] bytes = File.ReadAllBytes(Path.Combine(Repository, room.sourceFbxPath));
            if (File.Exists(target) && !File.ReadAllBytes(target).SequenceEqual(bytes)) throw new Exception("Existing Unity model differs: preserve version " + target);
            if (!File.Exists(target)) File.WriteAllBytes(target, bytes);
        }
        var officeRoom=registry.rooms.Single(r=>r.roomId=="PAN-001");
        string officeModelPath=null;
        if(!string.IsNullOrEmpty(officeRoom.sourceFbxPath))
        {
            officeModelPath="Assets/Meshy/"+officeRoom.assetId+"/"+officeRoom.assetVersion+"/office.fbx";
            Directory.CreateDirectory(Path.GetDirectoryName(officeModelPath));
            byte[] officeBytes=File.ReadAllBytes(Path.Combine(Repository,officeRoom.sourceFbxPath));
            if(File.Exists(officeModelPath)&&!File.ReadAllBytes(officeModelPath).SequenceEqual(officeBytes))throw new Exception("Existing office version preserved");
            if(!File.Exists(officeModelPath))File.WriteAllBytes(officeModelPath,officeBytes);
            imports.Add(new ImportedAsset{asset_id=officeRoom.assetId,version=officeRoom.assetVersion,source_path=officeRoom.sourceFbxPath,unity_path=officeModelPath,sha256=Hash(officeBytes),byte_identical=true});
        }
        AssetDatabase.Refresh(ImportAssetOptions.ForceSynchronousImport);
        string palettePath="Assets/Shared/Textures/v001/palette.png";
        var previousPalette=AssetDatabase.LoadAssetAtPath<Texture2D>(palettePath);
        int previousPaletteWidth=previousPalette==null?0:previousPalette.width,previousPaletteHeight=previousPalette==null?0:previousPalette.height;
        var paletteImporter=(TextureImporter)AssetImporter.GetAtPath(palettePath);
        paletteImporter.npotScale=TextureImporterNPOTScale.None;paletteImporter.maxTextureSize=4096;
        paletteImporter.textureCompression=TextureImporterCompression.Uncompressed;paletteImporter.mipmapEnabled=false;
        paletteImporter.filterMode=FilterMode.Point;paletteImporter.wrapMode=TextureWrapMode.Clamp;paletteImporter.sRGBTexture=true;
        var webPalette=paletteImporter.GetPlatformTextureSettings("WebGL");webPalette.name="WebGL";webPalette.overridden=true;
        webPalette.maxTextureSize=4096;webPalette.format=TextureImporterFormat.RGBA32;webPalette.textureCompression=TextureImporterCompression.Uncompressed;
        paletteImporter.SetPlatformTextureSettings(webPalette);paletteImporter.isReadable=true;paletteImporter.SaveAndReimport();
        var importedPalette=AssetDatabase.LoadAssetAtPath<Texture2D>(palettePath);
        byte[] sourcePaletteBytes=File.ReadAllBytes(Path.Combine(Repository,"meshy/models/textures/palettes/v001/palette.png"));
        if(!sourcePaletteBytes.SequenceEqual(File.ReadAllBytes(palettePath)))throw new Exception("Canonical palette copy bytes differ");
        var decodedPalette=new Texture2D(2,2,TextureFormat.RGBA32,false);
        if(!ImageConversion.LoadImage(decodedPalette,sourcePaletteBytes))throw new Exception("Canonical palette decode failed");
        var paletteEvidence=new PaletteEvidence {checked_at=DateTimeOffset.Now.ToString("o"),source_path="meshy/models/textures/palettes/v001/palette.png",source_sha256=Hash(sourcePaletteBytes),width=importedPalette.width,height=importedPalette.height,previous_imported_width=previousPaletteWidth,previous_imported_height=previousPaletteHeight,source_pixel_sha256=PixelHash(decodedPalette),imported_pixel_sha256=PixelHash(importedPalette),npot_resizing_disabled=true,compression_disabled=true,mipmaps_disabled=true,point_filtering=true};
        paletteEvidence.imported_pixels_identical=paletteEvidence.source_pixel_sha256==paletteEvidence.imported_pixel_sha256;
        UnityEngine.Object.DestroyImmediate(decodedPalette);
        File.WriteAllText(Path.Combine(evidence,"palette-import.json"),JsonUtility.ToJson(paletteEvidence,true));
        if(!paletteEvidence.imported_pixels_identical||paletteEvidence.width!=2508||paletteEvidence.height!=2508)throw new Exception("Imported palette resized or recolored");
        paletteImporter.isReadable=false;paletteImporter.SaveAndReimport();
        foreach(var asset in imports)
        {
            var importer=(ModelImporter)AssetImporter.GetAtPath(asset.unity_path);importer.materialImportMode=ModelImporterMaterialImportMode.None;
            importer.importAnimation=false;importer.isReadable=true;importer.SaveAndReimport();
            asset.imported=AssetDatabase.LoadAssetAtPath<GameObject>(asset.unity_path)!=null;
            if(!asset.imported)throw new Exception("Prop import failed: "+asset.unity_path);
        }
        var palette = AssetDatabase.LoadAssetAtPath<Texture2D>("Assets/Shared/Textures/v001/palette.png");
        if (palette == null) throw new Exception("Registered shared palette missing");
        var material = AssetDatabase.LoadAssetAtPath<Material>("Assets/Shared/Materials/OfficePalette.mat");
        if (material == null || material.mainTexture != palette || material.color != Color.white) throw new Exception("Shared material differs from registered palette");
        var font = AssetDatabase.LoadAssetAtPath<Font>("Assets/Resources/KoreanUI.otf");
        foreach(var asset in imports.Where(i=>i.asset_id!="AST-020"))
        {
            asset.prefab_path=Path.GetDirectoryName(asset.unity_path).Replace('\\','/')+"/asset.prefab";
            if(File.Exists(asset.prefab_path))
            {
                var saved=AssetDatabase.LoadAssetAtPath<GameObject>(asset.prefab_path);
                if(saved==null||saved.GetComponentsInChildren<Renderer>().Any(r=>r.sharedMaterials.Length!=1||r.sharedMaterial!=material))throw new Exception("Existing prop prefab differs: "+asset.prefab_path);
                continue;
            }
            var prototype=(GameObject)PrefabUtility.InstantiatePrefab(AssetDatabase.LoadAssetAtPath<GameObject>(asset.unity_path));
            prototype.name=asset.asset_id+"_"+asset.version;
            foreach(MeshRenderer renderer in prototype.GetComponentsInChildren<MeshRenderer>())
            {
                renderer.sharedMaterial=material;var collider=renderer.gameObject.AddComponent<MeshCollider>();collider.sharedMesh=renderer.GetComponent<MeshFilter>().sharedMesh;
            }
            PrefabUtility.SaveAsPrefabAsset(prototype,asset.prefab_path);UnityEngine.Object.DestroyImmediate(prototype);
        }
        File.WriteAllText(Path.Combine(evidence,"component-imports.json"),JsonUtility.ToJson(new CopyEvidence {checked_at=DateTimeOffset.Now.ToString("o"),assets=imports.ToArray()},true));
        foreach (var room in registry.rooms.Where(r => r.available && r.roomId != "PAN-001"))
        {
            string path = "Assets/Meshy/" + room.assetId + "/" + room.assetVersion + "/room.fbx";
            var importer = (ModelImporter)AssetImporter.GetAtPath(path);
            importer.materialImportMode = ModelImporterMaterialImportMode.None;
            importer.importAnimation = false; importer.isReadable = true; importer.SaveAndReimport();
            EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);
            var root = (GameObject)PrefabUtility.InstantiatePrefab(AssetDatabase.LoadAssetAtPath<GameObject>(path));
            root.name = "Room_" + room.roomId;
            foreach (MeshRenderer renderer in root.GetComponentsInChildren<MeshRenderer>())
            {
                renderer.sharedMaterial = material;
                var collider = renderer.gameObject.AddComponent<MeshCollider>();
                collider.sharedMesh = renderer.GetComponent<MeshFilter>().sharedMesh;
            }
            var clear = new GameObject("Full frame clear").AddComponent<Camera>();
            clear.clearFlags = CameraClearFlags.SolidColor; clear.backgroundColor = new Color(.075f,.105f,.12f); clear.cullingMask = 0; clear.depth = -10;
            var camera = new GameObject("Main Camera").AddComponent<Camera>(); camera.tag = "MainCamera";
            camera.clearFlags = CameraClearFlags.SolidColor; camera.backgroundColor = clear.backgroundColor;
            camera.fieldOfView = 40; camera.nearClipPlane = .05f; camera.farClipPlane = 40;
            Vector3 target = new Vector3(0,.7f,0), position = target + Quaternion.Euler(35,145,0) * new Vector3(0,0,-9.5f);
            camera.transform.SetPositionAndRotation(position,Quaternion.LookRotation(target-position));
            var light = new GameObject("Daylight").AddComponent<Light>(); light.type = LightType.Directional; light.intensity = 1.1f;
            light.transform.rotation = Quaternion.Euler(48,-25,0); light.shadows = LightShadows.None;
            RenderSettings.ambientMode = AmbientMode.Flat; RenderSettings.ambientLight = new Color(.72f,.75f,.78f);
            var explorer = new GameObject("WorkplaceExplorer").AddComponent<WorkplaceExplorer>();
            explorer.registryJson = AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Resources/workplace-registry.json"); explorer.koreanFont = font;
            var placementRoots = root.GetComponentsInChildren<Transform>().Where(t => System.Text.RegularExpressions.Regex.IsMatch(t.name,"^AST-[0-9]+-[0-9]{3}$")).ToArray();
            string placementPath=Path.Combine(Path.GetDirectoryName(Path.GetDirectoryName(Path.Combine(Repository,room.sourceFbxPath))),"placements.json");
            var sourcePlacements=JsonUtility.FromJson<SourcePlacements>(File.ReadAllText(placementPath)).instances.ToDictionary(i=>i.instance_id);
            var instances = placementRoots.Select(t => new PlacementEvidence { instance_id = t.name, asset_id = sourcePlacements[t.name].asset_id, version = sourcePlacements[t.name].version, hierarchy = Hierarchy(t),
                mesh_count = t.GetComponentsInChildren<MeshFilter>().Length, triangles = t.GetComponentsInChildren<MeshFilter>().Sum(f => f.sharedMesh.triangles.Length/3),
                position = t.position, rotation = t.rotation, scale = t.lossyScale }).ToArray();
            int triangles = root.GetComponentsInChildren<MeshFilter>().Sum(f => f.sharedMesh.triangles.Length/3);
            if (triangles != room.triangles || triangles > 5000 || instances.Length != room.instances || instances.Sum(p => p.triangles) != triangles) throw new Exception("Room budget/placement mismatch " + room.roomId);
            EditorSceneManager.SaveScene(UnityEngine.SceneManagement.SceneManager.GetActiveScene(),room.scenePath);
            File.WriteAllText(Path.Combine(evidence,room.roomId+"-unity-scene.json"),JsonUtility.ToJson(new SceneEvidence { build_id=BuildId, room_id=room.roomId, scene_path=room.scenePath, checked_at=DateTimeOffset.Now.ToString("o"), unity=Application.unityVersion,
                triangles=triangles, renderers=root.GetComponentsInChildren<MeshFilter>().Length,
                material_count=root.GetComponentsInChildren<Renderer>().SelectMany(r=>r.sharedMaterials).Distinct().Count(),
                texture_count=root.GetComponentsInChildren<Renderer>().SelectMany(r=>r.sharedMaterials).Where(m=>m!=null&&m.mainTexture!=null).Select(m=>m.mainTexture).Distinct().Count(), instances=instances },true));
        }
        var available = registry.rooms.Where(r => r.available && r.roomId != "PAN-001").Select(r => new EditorBuildSettingsScene(r.scenePath,true)).ToList();
        // Preserve the original v005 scene and implementation. The direct-work
        // adaptation is saved as a new scene with the same 3 physical bindings.
        EditorSceneManager.OpenScene("Assets/Scenes/OfficeAssistant.unity");
        var original=UnityEngine.Object.FindFirstObjectByType<OfficeExperience>();
        if(original==null)throw new Exception("Original office source missing");
        if(officeModelPath!=null)
        {
            Transform oldRoot=original.bindings[0].renderer.transform.parent;
            var newRoot=(GameObject)PrefabUtility.InstantiatePrefab(AssetDatabase.LoadAssetAtPath<GameObject>(officeModelPath));
            newRoot.name="Office_"+officeRoom.assetId+"_"+officeRoom.assetVersion;
            newRoot.transform.SetPositionAndRotation(oldRoot.position,oldRoot.rotation);newRoot.transform.localScale=oldRoot.localScale;
            foreach(MeshRenderer renderer in newRoot.GetComponentsInChildren<MeshRenderer>())
            {
                renderer.sharedMaterial=material;var collider=renderer.gameObject.AddComponent<MeshCollider>();collider.sharedMesh=renderer.GetComponent<MeshFilter>().sharedMesh;
            }
            string[] names={"AST-005-0","AST-009-0","AST-015-0"};
            for(int i=0;i<original.bindings.Length;i++)
            {
                var target=newRoot.GetComponentsInChildren<Transform>().Single(t=>t.name==names[i]);
                original.bindings[i].renderer=target.GetComponent<Renderer>();original.bindings[i].collider=target.GetComponent<MeshCollider>();
            }
            UnityEngine.Object.DestroyImmediate(oldRoot.gameObject);
        }
        var direct=original.gameObject.AddComponent<OfficeDirectExperience>();
        direct.scenario=AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Resources/office-direct-scenario.json");
        if(direct.scenario==null)direct.scenario=original.scenario;
        direct.koreanFont=original.koreanFont;direct.viewCamera=original.viewCamera;direct.bindings=original.bindings;
        UnityEngine.Object.DestroyImmediate(original);
        var officeExplorer=new GameObject("WorkplaceExplorer").AddComponent<WorkplaceExplorer>();
        officeExplorer.registryJson=AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Resources/workplace-registry.json");officeExplorer.koreanFont=font;
        string officePath="Assets/Scenes/OfficeAssistantDirect.unity";
        EditorSceneManager.SaveScene(UnityEngine.SceneManagement.SceneManager.GetActiveScene(),officePath);
        var officeFilters=direct.bindings[0].renderer.transform.parent.GetComponentsInChildren<MeshFilter>();
        var officeInstances=officeFilters.Select(f=>new PlacementEvidence {instance_id=f.name,asset_id=f.name.Substring(0,7),version=f.name.StartsWith("AST-001-")?"v002":"v001",hierarchy=Hierarchy(f.transform),mesh_count=1,triangles=f.sharedMesh.triangles.Length/3,position=f.transform.position,rotation=f.transform.rotation,scale=f.transform.lossyScale}).ToArray();
        File.WriteAllText(Path.Combine(evidence,"PAN-001-unity-scene.json"),JsonUtility.ToJson(new SceneEvidence {build_id=BuildId,room_id="PAN-001",scene_path=officePath,checked_at=DateTimeOffset.Now.ToString("o"),unity=Application.unityVersion,triangles=officeInstances.Sum(i=>i.triangles),renderers=officeInstances.Length,material_count=1,texture_count=1,instances=officeInstances},true));
        available.Add(new EditorBuildSettingsScene(officePath,true));
        EditorBuildSettings.scenes = available.ToArray();
        PlayerSettings.companyName="Career Practice"; PlayerSettings.productName="Workplaces";
        PlayerSettings.defaultScreenWidth=1440; PlayerSettings.defaultScreenHeight=900;
        PlayerSettings.WebGL.compressionFormat=WebGLCompressionFormat.Disabled; PlayerSettings.WebGL.decompressionFallback=false; PlayerSettings.WebGL.dataCaching=false;
        PlayerSettings.WebGL.template="PROJECT:Workplaces"; PlayerSettings.runInBackground=true;
        PlayerSettings.colorSpace=ColorSpace.Linear; PlayerSettings.stripEngineCode=true;
        PlayerSettings.SetManagedStrippingLevel(UnityEditor.Build.NamedBuildTarget.WebGL,ManagedStrippingLevel.Low);
        AssetDatabase.SaveAssets();
        Debug.Log("WORKPLACES_PREPARED " + available.Count);
    }
    public static void Build()
    {
        string output=Path.Combine(Repository,"unity/webgl/builds/"+BuildId);
        if (Directory.Exists(output)) throw new Exception("Existing build directory preserved: choose new build ID");
        Prepare();
        var report=BuildPipeline.BuildPlayer(new BuildPlayerOptions { scenes=EditorBuildSettings.scenes.Select(s=>s.path).ToArray(), locationPathName=output,target=BuildTarget.WebGL,options=BuildOptions.Development });
        var result=new OfficeBuild.BuildResult { build_id=BuildId,unity=Application.unityVersion,result=report.summary.result.ToString(),checked_at=DateTimeOffset.Now.ToString("o"),bytes=(long)report.summary.totalSize,errors=report.summary.totalErrors,warnings=report.summary.totalWarnings,duration_seconds=report.summary.totalTime.TotalSeconds };
        File.WriteAllText(Path.Combine(Repository,"docs/machine/evidence/"+BuildId+"/build-result.json"),JsonUtility.ToJson(result,true));
        if (report.summary.result!=BuildResult.Succeeded) throw new Exception("Workplaces WebGL build failed");
    }
}

using System;
using System.IO;
using System.Linq;
using CareerExperience;
using UnityEditor;
using UnityEditor.Build.Reporting;
using UnityEditor.SceneManagement;
using UnityEngine;
using UnityEngine.Rendering;

public static class OfficeBuild
{
    const string Scene = "Assets/Scenes/OfficeAssistant.unity";
    static string Repository => Path.GetFullPath(Path.Combine(Application.dataPath, "../../../.."));
    public static string CurrentBuildId
    {
        get {
            string[] args = Environment.GetCommandLineArgs(); int index = Array.IndexOf(args, "-officeBuildId");
            string id = index >= 0 && index + 1 < args.Length ? args[index + 1] : "office-assistant-v001";
            if (!System.Text.RegularExpressions.Regex.IsMatch(id, "^[a-z0-9]+(?:-[a-z0-9]+)*-v[0-9]{3,}$")) throw new Exception("Invalid build ID");
            return id;
        }
    }
    public static string EvidenceDirectory => Path.Combine(Repository, "docs/machine/evidence/" + CurrentBuildId);
    static string Evidence => EvidenceDirectory;
    [Serializable] public class SceneEvidence { public int schema_version = 3; public string unity, scene, measured_at; public int triangles, renderer_count, material_count, texture_count, interactive_objects; public BindingEvidence[] bindings; public MeshEvidence[] instances; public string[] palettes; }
    [Serializable] public class BindingEvidence { public string id, hierarchy, collider_type; public Vector3 center, size; public bool convex, enabled; }
    [Serializable] public class MeshEvidence { public string instance_id, asset_id, version, hierarchy; public int triangles; public Vector3 position, scale; public Quaternion rotation; }
    static string Hierarchy(Transform t) => t.parent == null ? t.name : Hierarchy(t.parent) + "/" + t.name;
    [MenuItem("Office Experience/Prepare Scene")]
    public static void Prepare()
    {
        Directory.CreateDirectory(Evidence); Directory.CreateDirectory("Assets/Scenes"); Directory.CreateDirectory("Assets/Shared/Materials");
        var modelImporter = (ModelImporter)AssetImporter.GetAtPath("Assets/Meshy/AST-020/v003/office.fbx");
        modelImporter.materialImportMode = ModelImporterMaterialImportMode.None;
        modelImporter.importAnimation = false; modelImporter.isReadable = true; modelImporter.SaveAndReimport();
        var paletteImporter = (TextureImporter)AssetImporter.GetAtPath("Assets/Shared/Textures/v001/palette.png");
        paletteImporter.textureCompression = TextureImporterCompression.Uncompressed;
        paletteImporter.maxTextureSize = 4096; paletteImporter.mipmapEnabled = false;
        paletteImporter.filterMode = FilterMode.Point; paletteImporter.wrapMode = TextureWrapMode.Clamp; paletteImporter.sRGBTexture = true; paletteImporter.SaveAndReimport();
        var texture = AssetDatabase.LoadAssetAtPath<Texture2D>("Assets/Shared/Textures/v001/palette.png");
        var material = AssetDatabase.LoadAssetAtPath<Material>("Assets/Shared/Materials/OfficePalette.mat");
        if (material == null) { material = new Material(Shader.Find("Standard")); AssetDatabase.CreateAsset(material, "Assets/Shared/Materials/OfficePalette.mat"); }
        material.mainTexture = texture; material.color = Color.white; material.SetFloat("_Glossiness", .15f); material.SetFloat("_Metallic", 0);
        EditorSceneManager.NewScene(NewSceneSetup.EmptyScene, NewSceneMode.Single);
        var office = (GameObject)PrefabUtility.InstantiatePrefab(AssetDatabase.LoadAssetAtPath<GameObject>("Assets/Meshy/AST-020/v003/office.fbx"));
        office.name = "Office_AST-020_v003";
        foreach (MeshRenderer renderer in office.GetComponentsInChildren<MeshRenderer>())
        {
            renderer.sharedMaterial = material;
            var collider = renderer.gameObject.AddComponent<MeshCollider>();
            collider.sharedMesh = renderer.GetComponent<MeshFilter>().sharedMesh; collider.convex = false;
        }
        // Clear the whole frame before the main camera's viewport changes during closeups.
        // No model/mesh/collider is added by this background camera.
        var background = new GameObject("View Background").AddComponent<Camera>();
        background.clearFlags = CameraClearFlags.SolidColor; background.backgroundColor = new Color(.16f, .23f, .26f);
        background.cullingMask = 0; background.depth = -10;
        var camera = new GameObject("Main Camera").AddComponent<Camera>(); camera.tag = "MainCamera";
        camera.clearFlags = CameraClearFlags.SolidColor; camera.backgroundColor = new Color(.16f, .23f, .26f);
        camera.rect = new Rect(0, .145f, .65f, .72f); camera.fieldOfView = 40; camera.nearClipPlane = .05f; camera.farClipPlane = 40;
        var light = new GameObject("Daylight").AddComponent<Light>(); light.type = LightType.Directional; light.intensity = 1.1f;
        light.transform.rotation = Quaternion.Euler(48, -25, 0); light.shadows = LightShadows.None;
        RenderSettings.ambientMode = AmbientMode.Flat; RenderSettings.ambientLight = new Color(.72f, .75f, .78f);
        var controller = new GameObject("OfficeExperience").AddComponent<OfficeExperience>();
        controller.viewCamera = camera;
        controller.scenario = AssetDatabase.LoadAssetAtPath<TextAsset>("Assets/Resources/office-scenario.json");
        controller.koreanFont = AssetDatabase.LoadAssetAtPath<Font>("Assets/Resources/KoreanUI.otf");
        string[] names = { "AST-005-0", "AST-009-0", "AST-015-0" }, ids = { "monitor", "copier", "cabinet" }, labels = { "모니터", "복합기", "수납장" };
        controller.bindings = names.Select((name, i) => {
            var t = office.GetComponentsInChildren<Transform>().Single(x => x.name == name);
            return new OfficeBinding { id = ids[i], label = labels[i], collider = t.GetComponent<MeshCollider>(), renderer = t.GetComponent<Renderer>() };
        }).ToArray();
        // Scene and rendered geometry, not the FBX prefab definition, are the counting basis.
        var filters = office.GetComponentsInChildren<MeshFilter>();
        var instances = filters.Select(f => new MeshEvidence { instance_id = f.name, hierarchy = Hierarchy(f.transform), asset_id = f.name.Substring(0, 7),
            version = f.name.StartsWith("AST-001-") ? "v002" : "v001", triangles = f.sharedMesh.triangles.Length / 3,
            position = f.transform.position, rotation = f.transform.rotation, scale = f.transform.lossyScale }).ToArray();
        if (instances.Length != 30 || instances.Sum(i => i.triangles) != 4308 || controller.bindings.Length != 3) throw new Exception("Unexpected model content");
        if (controller.bindings.Any(b => b.collider == null || b.collider.sharedMesh == null)) throw new Exception("Missing real mesh collider");
        // Reusable prototype definitions reference the same imported meshes. They are not extra scene instances.
        foreach (var group in filters.GroupBy(f => f.name.Substring(0, 7)))
        {
            string version = group.Key == "AST-001" ? "v002" : "v001";
            string dir = "Assets/Meshy/" + group.Key + "/" + version;
            Directory.CreateDirectory(dir); AssetDatabase.Refresh();
            var prototype = UnityEngine.Object.Instantiate(group.First().gameObject);
            prototype.name = group.Key + "_" + version; prototype.transform.position = Vector3.zero;
            PrefabUtility.SaveAsPrefabAsset(prototype, dir + "/asset.prefab");
            UnityEngine.Object.DestroyImmediate(prototype);
        }
        EditorSceneManager.SaveScene(UnityEngine.SceneManagement.SceneManager.GetActiveScene(), Scene);
        EditorBuildSettings.scenes = new[] { new EditorBuildSettingsScene(Scene, true) };
        PlayerSettings.companyName = "Career Practice"; PlayerSettings.productName = "Office Assistant";
        PlayerSettings.defaultScreenWidth = 1440; PlayerSettings.defaultScreenHeight = 900;
        PlayerSettings.WebGL.compressionFormat = WebGLCompressionFormat.Disabled;
        PlayerSettings.WebGL.decompressionFallback = false; PlayerSettings.WebGL.dataCaching = false;
        PlayerSettings.WebGL.template = "PROJECT:Office";
        PlayerSettings.runInBackground = true; PlayerSettings.colorSpace = ColorSpace.Linear;
        PlayerSettings.stripEngineCode = true;
        PlayerSettings.SetManagedStrippingLevel(UnityEditor.Build.NamedBuildTarget.WebGL, ManagedStrippingLevel.Low);
        AssetDatabase.SaveAssets();
        var evidence = new SceneEvidence { unity = Application.unityVersion, scene = Scene, measured_at = DateTimeOffset.Now.ToString("o"), triangles = instances.Sum(i => i.triangles), renderer_count = filters.Length,
            material_count = office.GetComponentsInChildren<Renderer>().SelectMany(r => r.sharedMaterials).Distinct().Count(), texture_count = 1, interactive_objects = controller.bindings.Length, instances = instances,
            palettes = new[] { AssetDatabase.GetAssetPath(texture) }, bindings = controller.bindings.Select(b => new BindingEvidence { id = b.id, hierarchy = Hierarchy(b.collider.transform), collider_type = "MeshCollider", center = b.collider.bounds.center, size = b.collider.bounds.size, convex = b.collider.convex, enabled = b.collider.enabled }).ToArray() };
        File.WriteAllText(Path.Combine(Evidence, "unity-scene.json"), JsonUtility.ToJson(evidence, true));
        var tests = OfficeAcceptance.Run(JsonUtility.FromJson<OfficeData>(controller.scenario.text));
        File.WriteAllText(Path.Combine(Evidence, "unity-csharp-acceptance.json"), JsonUtility.ToJson(tests, true));
        if (tests.failed > 0) throw new Exception("Acceptance cases failed");
        Debug.Log("OFFICE_PREPARED " + evidence.triangles + " triangles, " + tests.passed + " cases pass");
    }
    [MenuItem("Office Experience/Build WebGL")]
    public static void Build()
    {
        Prepare();
        string buildId = CurrentBuildId;
        string output = Path.Combine(Repository, "unity/webgl/builds/" + buildId);
        if (File.Exists(Path.Combine(output, "index.html"))) throw new Exception("Existing build preserved. Choose a new build ID before building again.");
        if (!BuildPipeline.IsBuildTargetSupported(BuildTargetGroup.WebGL, BuildTarget.WebGL)) throw new Exception("WebGL support missing");
        var result = BuildPipeline.BuildPlayer(new BuildPlayerOptions { scenes = new[] { Scene }, locationPathName = output, target = BuildTarget.WebGL, options = BuildOptions.Development });
        File.WriteAllText(Path.Combine(Evidence, buildId + "-build-result.json"), JsonUtility.ToJson(new BuildResult { build_id = buildId, unity = Application.unityVersion, result = result.summary.result.ToString(), bytes = (long)result.summary.totalSize, errors = result.summary.totalErrors, warnings = result.summary.totalWarnings, duration_seconds = result.summary.totalTime.TotalSeconds, checked_at = DateTimeOffset.Now.ToString("o") }, true));
        if (result.summary.result != UnityEditor.Build.Reporting.BuildResult.Succeeded) throw new Exception("WebGL build failed");
    }
    [Serializable] public class BuildResult { public int schema_version = 3; public string build_id, unity, result, checked_at; public long bytes; public int errors, warnings; public double duration_seconds; }
}

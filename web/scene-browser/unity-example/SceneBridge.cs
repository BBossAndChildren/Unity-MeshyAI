using System;
using System.Collections;
using System.Runtime.InteropServices;
using UnityEngine;
using UnityEngine.AddressableAssets;
using UnityEngine.ResourceManagement.AsyncOperations;
using UnityEngine.ResourceManagement.ResourceProviders;
using UnityEngine.SceneManagement;

// Put exactly one SceneBridge on a root GameObject in the Bootstrap scene.
// Content scenes are additive, so Bootstrap and this bridge stay alive.
public sealed class SceneBridge : MonoBehaviour
{
    [Serializable] public class Binding { public string sceneId; public string contentVersion; public string addressableKey; }
    [Serializable] class Request { public string sceneId; public string contentVersion; public string requestId; }
    [Serializable] class Reply { public string type; public string sceneId; public string requestId; public string message; }
    [SerializeField] Binding[] allowedScenes = Array.Empty<Binding>();
    AsyncOperationHandle<SceneInstance> current;
    bool hasCurrent, busy;
    string currentId, currentVersion;
#if UNITY_WEBGL && !UNITY_EDITOR
    [DllImport("__Internal")] static extern void EmitSceneEvent(string json);
#endif
    void Awake() { gameObject.name = "SceneBridge"; }
    void Start() { Emit("ready", null, null); }
    void Emit(string type, Request request, string message)
    {
        string json = JsonUtility.ToJson(new Reply { type=type, sceneId=request?.sceneId, requestId=request?.requestId, message=message });
#if UNITY_WEBGL && !UNITY_EDITOR
        EmitSceneEvent(json);
#else
        Debug.Log(json);
#endif
    }
    // Exact JavaScript target: SendMessage('SceneBridge','OpenScene',JSON.stringify(...))
    public void OpenScene(string json)
    {
        Request request;
        try { request = JsonUtility.FromJson<Request>(json); }
        catch (Exception e) { Emit("error", null, e.Message); return; }
        if(request == null || string.IsNullOrEmpty(request.requestId)) { Emit("error", request, "Invalid request"); return; }
        if(busy) { Emit("error", request, "Scene transition already in progress"); return; }
        Binding binding = Array.Find(allowedScenes, s => s.sceneId==request.sceneId && s.contentVersion==request.contentVersion);
        if(binding == null || string.IsNullOrEmpty(binding.addressableKey)) { Emit("error", request, "Scene/version not published"); return; }
        if(hasCurrent && currentId==request.sceneId && currentVersion==request.contentVersion) { Emit("loaded", request, null); return; }
        StartCoroutine(SwitchScene(request, binding));
    }
    IEnumerator SwitchScene(Request request, Binding binding)
    {
        busy = true;
        if(hasCurrent)
        {
            var unload = Addressables.UnloadSceneAsync(current, false);
            yield return unload;
            bool success = unload.Status == AsyncOperationStatus.Succeeded;
            Addressables.Release(unload);
            if(!success) { busy=false; Emit("error", request, "Previous scene unload failed"); yield break; }
            hasCurrent=false;
        }
        AsyncOperationHandle<SceneInstance> loading = default;
        string startError = null;
        try { loading = Addressables.LoadSceneAsync(binding.addressableKey, LoadSceneMode.Additive, true); }
        catch(Exception e) { startError=e.Message; }
        if(startError != null) { busy=false; Emit("error", request, startError); yield break; }
        yield return loading;
        busy=false;
        if(loading.Status != AsyncOperationStatus.Succeeded)
        {
            string error=loading.OperationException?.Message ?? "Scene load failed";
            Addressables.Release(loading); Emit("error", request, error); yield break;
        }
        current=loading;hasCurrent=true;currentId=request.sceneId;currentVersion=request.contentVersion;
        SceneManager.SetActiveScene(current.Result.Scene);
        Emit("loaded", request, null);
    }
}

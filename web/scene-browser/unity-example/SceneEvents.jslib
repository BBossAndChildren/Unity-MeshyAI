mergeInto(LibraryManager.library, {
  EmitSceneEvent: function (jsonPointer) {
    var payload = JSON.parse(UTF8ToString(jsonPointer));
    window.dispatchEvent(new CustomEvent('unity-scene-event', { detail: payload }));
  }
});

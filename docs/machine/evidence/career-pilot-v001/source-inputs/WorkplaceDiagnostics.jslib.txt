mergeInto(LibraryManager.library, {
  PublishWorkplaceState: function (json) {
    window.workplaceState = JSON.parse(UTF8ToString(json));
  }
});

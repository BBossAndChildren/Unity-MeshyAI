mergeInto(LibraryManager.library, {
  PublishOfficeState: function (json) {
    window.officeState = JSON.parse(UTF8ToString(json));
  },
  PublishOfficeTests: function (json) {
    window.officeTests = JSON.parse(UTF8ToString(json));
  }
});

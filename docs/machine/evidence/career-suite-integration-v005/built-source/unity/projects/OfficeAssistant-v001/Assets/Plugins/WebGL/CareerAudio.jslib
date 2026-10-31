mergeInto(LibraryManager.library, {
  CareerAudioCue: function (pointer) {
    try {
      var detail = JSON.parse(UTF8ToString(pointer));
      window.dispatchEvent(new CustomEvent('career-experience:audio', { detail: detail }));
    } catch (error) { console.warn('Career audio cue rejected', error); }
  },
  CareerPresentationState: function (pointer) {
    try {
      var detail = JSON.parse(UTF8ToString(pointer));
      window.careerPresentationState = detail;
      window.dispatchEvent(new CustomEvent('career-experience:presentation', { detail: detail }));
    } catch (error) { console.warn('Career presentation rejected', error); }
  }
});

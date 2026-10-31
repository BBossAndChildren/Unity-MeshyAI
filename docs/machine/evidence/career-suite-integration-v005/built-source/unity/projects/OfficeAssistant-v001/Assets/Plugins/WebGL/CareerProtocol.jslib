mergeInto(LibraryManager.library, {
  CareerPublish: function (pointer) {
    var event = JSON.parse(UTF8ToString(pointer));
    var history = window.careerExperienceEvents || (window.careerExperienceEvents = []);
    var seen = window.careerExperienceEventIds || (window.careerExperienceEventIds = new Set());
    if (event.eventId && !seen.has(event.eventId)) { seen.add(event.eventId); history.push(event); }
    window.careerExperienceLast = event;
    // Dispatch retries too: receivers perform their own eventId deduplication.
    window.dispatchEvent(new CustomEvent('career-experience:event', {detail: event}));
    if (window.parent !== window && window.careerExperienceParentOrigin) {
      try {
        var origin = new URL(window.careerExperienceParentOrigin).origin;
        if (origin === window.careerExperienceParentOrigin) window.parent.postMessage({channel: 'career-experience', event: event}, origin);
      } catch (_) {}
    }
    try { localStorage.setItem('career-experience:events', JSON.stringify({schema_version:3,protocol:'career-experience',protocolVersion:'v001',events:history})); } catch (_) {}
  },
  CareerCheckpoint: function (pointer) {
    var state = JSON.parse(UTF8ToString(pointer));
    window.careerExperienceCheckpoint = state;
    try { localStorage.setItem('career-experience:checkpoint', JSON.stringify(state)); } catch (_) {}
    if (!window.careerExperienceUnloadBound) {
      window.careerExperienceUnloadBound = true;
      window.addEventListener('pagehide', function () {
        var latest = window.careerExperienceCheckpoint;
        if (!latest || latest.ended) return;
        // Transport observation is not a fabricated user-abort gameplay event.
        try { localStorage.setItem('career-experience:interruption', JSON.stringify({code:'SESSION_INTERRUPTED',initiatedBy:'unknown',deliveryStatus:'unconfirmed',lastCheckpoint:latest,observedAt:new Date().toISOString()})); } catch (_) {}
      });
    }
  }
});

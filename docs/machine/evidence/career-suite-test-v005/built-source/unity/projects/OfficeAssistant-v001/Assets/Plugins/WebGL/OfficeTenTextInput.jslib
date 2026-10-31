mergeInto(LibraryManager.library, {
  $OfficeTenTextInput: {
    state: null,
    number: function (value, fallback) {
      var n = Number(value);
      return Number.isFinite(n) ? n : fallback;
    },
    canvas: function () {
      if (typeof Module !== 'undefined' && Module.canvas) return Module.canvas;
      return document.getElementById('unity-canvas') || document.querySelector('canvas');
    },
    snapshot: function () {
      var s = OfficeTenTextInput.state;
      if (!s) return Object.freeze({ disposed: true, context: '', focusedName: null, composing: false, fields: Object.freeze([]) });
      var rows = s.order.filter(function (name) { return !!s.records[name]; }).map(function (name) {
        var r = s.records[name], rect = r.input.getBoundingClientRect();
        return Object.freeze({ name: name, label: r.label, value: r.input.value, composing: !!r.composing,
          focused: !!r.focused, enabled: !r.input.disabled, visible: r.visible,
          x: rect.left, y: rect.top, width: rect.width, height: rect.height,
          selectionStart: r.input.selectionStart, selectionEnd: r.input.selectionEnd });
      });
      return Object.freeze({ disposed: false, context: s.context, focusedName: s.focusedName,
        composing: rows.some(function (r) { return r.composing; }), windowFocused: s.windowActive,
        devicePixelRatio: window.devicePixelRatio || 1, callbacks: s.callbacks, lastKind: s.lastKind,
        lastError: s.lastError, composition: Object.freeze({ starts: s.composition.starts, updates: s.composition.updates,
          ends: s.composition.ends, trustedStarts: s.composition.trustedStarts, trustedEnds: s.composition.trustedEnds,
          recent: Object.freeze(s.composition.recent.map(function (entry) { return Object.freeze(Object.assign({}, entry)); })) }), fields: Object.freeze(rows) });
    },
    send: function (r, kind, composing, backward, reason) {
      var s = OfficeTenTextInput.state;
      if (!s || !r.alive || s.records[r.name] !== r) return;
      // Capture ownership before SendMessage can synchronously change the C# view.
      var reply = { context: r.context, name: r.name, value: r.input.value, kind: kind,
        composing: !!composing, backward: !!backward, windowFocused: s.windowActive,
        reason: reason || 'field' };
      var target = r.target, callback = r.callback, payload = JSON.stringify(reply);
      s.callbacks++; s.lastKind = kind;
      try {
        if (typeof SendMessage === 'function') SendMessage(target, callback, payload);
        else if (typeof Module !== 'undefined' && typeof Module.SendMessage === 'function') Module.SendMessage(target, callback, payload);
        else if (window.unityInstance && typeof window.unityInstance.SendMessage === 'function') window.unityInstance.SendMessage(target, callback, payload);
        else if (window.officeUnity && typeof window.officeUnity.SendMessage === 'function') window.officeUnity.SendMessage(target, callback, payload);
        else s.lastError = 'Unity SendMessage bridge unavailable';
      } catch (error) { s.lastError = String(error && error.message || error); }
    },
    input: function (r, composing, reason) {
      if (!r.alive) return;
      var value = r.input.value, flag = !!composing;
      if (r.lastSentValue === value && r.lastSentComposing === flag) return;
      r.lastSentValue = value; r.lastSentComposing = flag;
      OfficeTenTextInput.send(r, 'input', flag, false, reason);
    },
    focusRecord: function (r, reason) {
      var s = OfficeTenTextInput.state;
      if (!s || !r.alive || r.input.disabled || !r.visible) return;
      s.windowActive = !document.hidden;
      s.focusedName = r.name;
      if (!r.focused) { r.focused = true; OfficeTenTextInput.send(r, 'focus', r.composing, false, reason || 'field-focus'); }
    },
    blurRecord: function (r, reason) {
      var s = OfficeTenTextInput.state;
      if (!s || !r.alive) return;
      // input first: blur/change/hide never discard the final DOM value.
      r.composing = false;
      OfficeTenTextInput.input(r, false, reason || 'field-blur');
      if (s.focusedName === r.name) s.focusedName = null;
      if (r.focused) { r.focused = false; OfficeTenTextInput.send(r, 'blur', false, false, reason || 'field-blur'); }
    },
    remove: function (r) {
      var s = OfficeTenTextInput.state;
      if (!s || !r || !r.alive || r.removing) return;
      r.removing = true;
      if (document.activeElement === r.input) r.input.blur();
      OfficeTenTextInput.blurRecord(r, 'remove');
      r.alive = false;
      if (r.wrapper.parentNode) r.wrapper.parentNode.removeChild(r.wrapper);
      delete s.records[r.name];
    },
    ensure: function () {
      if (OfficeTenTextInput.state) return OfficeTenTextInput.state;
      var container = document.createElement('div');
      container.id = 'office-ten-native-text-inputs';
      container.style.cssText = 'position:fixed;left:0;top:0;width:0;height:0;overflow:visible;pointer-events:none;z-index:2147483000;';
      document.body.appendChild(container);
      var s = { container: container, records: Object.create(null), order: [], context: '', identity: '',
        frame: null, focusedName: null, pendingFocus: null, windowActive: !document.hidden,
        callbacks: 0, lastKind: null, lastError: null, raf: 0, listeners: [],
        composition: { starts: 0, updates: 0, ends: 0, trustedStarts: 0, trustedEnds: 0, recent: [] } };
      OfficeTenTextInput.state = s;
      Object.defineProperty(window, 'officeTenTextInputState', { configurable: true,
        get: function () { return OfficeTenTextInput.snapshot(); } });
      var listen = function (where, type, fn, capture) {
        where.addEventListener(type, fn, capture);
        s.listeners.push({ where: where, type: type, fn: fn, capture: capture });
      };
      var ownRecord = function (target) {
        return s.order.map(function (name) { return s.records[name]; }).find(function (r) { return r && r.input === target; }) || null;
      };
      var keyboard = function (event) {
        var r = ownRecord(event.target);
        if (!r && s.focusedName && s.records[s.focusedName] && s.records[s.focusedName].composing) r = s.records[s.focusedName];
        if (!r || !r.alive) return;
        // Keep native editing defaults, but do not let Unity consume P/R/digits,
        // arrows, Enter or Escape while the HTML input owns the keyboard.
        event.stopImmediatePropagation();
        if (event.type !== 'keydown') return;
        var composing = r.composing || event.isComposing || event.keyCode === 229;
        if (composing) return; // IME Enter/Escape/Tab belongs to the browser.
        if (event.key === 'Escape' || event.key === 'Esc') {
          event.preventDefault();
          OfficeTenTextInput.input(r, false, 'escape');
          OfficeTenTextInput.send(r, 'escape', false, false, 'escape');
        } else if (event.key === 'Tab') {
          var names = s.order.filter(function (name) { var item = s.records[name]; return item.visible && !item.input.disabled; });
          var index = names.indexOf(r.name), backward = !!event.shiftKey;
          if (index >= 0 && (backward ? index === 0 : index === names.length - 1)) {
            event.preventDefault();
            // Snapshot r before blur callbacks can re-enter Sync. The record
            // carries the original context, target and method for attribution.
            OfficeTenTextInput.input(r, false, 'tab-boundary');
            r.input.blur();
            var canvas = OfficeTenTextInput.canvas();
            if (canvas && typeof canvas.focus === 'function') { try { canvas.focus({ preventScroll: true }); } catch (_) { canvas.focus(); } }
            OfficeTenTextInput.send(r, 'tab', false, backward, 'tab-boundary');
          }
        }
      };
      listen(window, 'keydown', keyboard, true);
      listen(window, 'keypress', keyboard, true);
      listen(window, 'keyup', keyboard, true);
      var loseWindow = function (reason) {
        s.windowActive = false;
        var r = s.focusedName && s.records[s.focusedName];
        if (!r) r = ownRecord(document.activeElement);
        if (r) OfficeTenTextInput.blurRecord(r, reason);
      };
      listen(window, 'blur', function (event) { if (event.target === window) loseWindow('window-blur'); }, true);
      listen(document, 'visibilitychange', function () {
        if (document.hidden) loseWindow('document-hidden');
        else { s.windowActive = true; var r = ownRecord(document.activeElement); if (r) OfficeTenTextInput.focusRecord(r, 'window-focus'); }
      }, true);
      listen(window, 'focus', function (event) {
        if (event.target !== window) return;
        s.windowActive = !document.hidden;
        var r = ownRecord(document.activeElement);
        if (r && s.windowActive) OfficeTenTextInput.focusRecord(r, 'window-focus');
      }, true);
      listen(window, 'resize', function () { OfficeTenTextInput.layout(); }, true);
      listen(window, 'scroll', function () { OfficeTenTextInput.layout(); }, true);
      if (window.visualViewport) {
        listen(window.visualViewport, 'resize', function () { OfficeTenTextInput.layout(); }, false);
        listen(window.visualViewport, 'scroll', function () { OfficeTenTextInput.layout(); }, false);
      }
      var tick = function () {
        if (OfficeTenTextInput.state !== s) return;
        OfficeTenTextInput.layout();
        s.raf = window.requestAnimationFrame(tick);
      };
      s.raf = window.requestAnimationFrame(tick);
      return s;
    },
    create: function (field, frame) {
      var s = OfficeTenTextInput.state, wrapper = document.createElement('div'), input = document.createElement('input');
      wrapper.style.cssText = 'position:fixed;overflow:hidden;pointer-events:auto;box-sizing:border-box;';
      input.type = 'text'; input.autocomplete = 'off'; input.spellcheck = false; input.autocapitalize = 'off';
      input.setAttribute('inputmode', 'text'); input.setAttribute('aria-label', field.label || field.name);
      input.setAttribute('data-office-ten-field', field.name); input.tabIndex = 0;
      input.style.cssText = 'position:absolute;box-sizing:border-box;margin:0;border:1px solid #91a8b4;border-radius:3px;background:#243b46;color:#f2faff;caret-color:#ffffff;font-family:system-ui,"Malgun Gothic",sans-serif;outline-offset:-2px;line-height:normal;';
      input.value = field.value == null ? '' : String(field.value);
      wrapper.appendChild(input); s.container.appendChild(wrapper);
      var r = { name: field.name, label: field.label || field.name, context: frame.context, target: frame.target, callback: frame.callback,
        wrapper: wrapper, input: input, field: field, alive: true, removing: false, visible: false, focused: false, composing: false,
        lastSentValue: input.value, lastSentComposing: false };
      input.addEventListener('focus', function () { if (r.alive) OfficeTenTextInput.focusRecord(r, 'field-focus'); });
      input.addEventListener('blur', function () { if (r.alive) OfficeTenTextInput.blurRecord(r, 'field-blur'); });
      input.addEventListener('input', function (event) { if (r.alive) OfficeTenTextInput.input(r, r.composing || event.isComposing, 'input'); });
      input.addEventListener('change', function () { if (r.alive) OfficeTenTextInput.input(r, r.composing, 'change'); });
      var observeComposition = function (event) {
        var current = OfficeTenTextInput.state;
        if (!r.alive || !current || current.records[r.name] !== r) return;
        var log = current.composition, type = event.type;
        if (type === 'compositionstart') { log.starts++; if (event.isTrusted) log.trustedStarts++; }
        else if (type === 'compositionend') { log.ends++; if (event.isTrusted) log.trustedEnds++; }
        else log.updates++;
        log.recent.push({ context: r.context, name: r.name, type: type, data: String(event.data || '').slice(0, 256), isTrusted: !!event.isTrusted });
        if (log.recent.length > 16) log.recent.shift();
      };
      input.addEventListener('compositionstart', function (event) { if (r.alive) { observeComposition(event); r.composing = true; OfficeTenTextInput.input(r, true, 'compositionstart'); } });
      input.addEventListener('compositionupdate', observeComposition);
      input.addEventListener('compositionend', function (event) { if (r.alive) { observeComposition(event); r.composing = false; OfficeTenTextInput.input(r, false, 'compositionend'); } });
      return r;
    },
    sync: function (json) {
      var frame;
      try { frame = JSON.parse(json); }
      catch (error) { if (OfficeTenTextInput.state) OfficeTenTextInput.state.lastError = 'Invalid text-input frame: ' + error.message; return; }
      frame.context = String(frame.context || ''); frame.target = String(frame.target || 'OfficeExperience'); frame.callback = String(frame.callback || 'OnBrowserTextInput');
      var s = OfficeTenTextInput.ensure(), identity = frame.context + '\n' + frame.target + '\n' + frame.callback;
      if (s.identity !== identity) {
        s.order.slice().forEach(function (name) { OfficeTenTextInput.remove(s.records[name]); });
        s.order = []; s.pendingFocus = null; s.identity = identity; s.context = frame.context;
      }
      s.frame = frame;
      var fields = Array.isArray(frame.fields) && frame.visible !== false ? frame.fields : [], wanted = Object.create(null), order = [];
      fields.forEach(function (field) {
        if (!field || typeof field.name !== 'string' || !field.name || wanted[field.name]) return;
        wanted[field.name] = true; order.push(field.name);
        var r = s.records[field.name];
        if (!r) { r = OfficeTenTextInput.create(field, frame); s.records[field.name] = r; }
        r.field = field; r.label = field.label || field.name;
        r.input.setAttribute('aria-label', r.label);
        var enabled = field.enabled !== false;
        if (!enabled && r.focused) { r.input.blur(); OfficeTenTextInput.blurRecord(r, 'disabled'); }
        r.input.disabled = !enabled;
        var value = field.value == null ? '' : String(field.value);
        // Focused/composing text is DOM-owned until blur. A lagging C# frame
        // must not reset selection, an IME preedit or newly entered characters.
        if (!r.focused && !r.composing && document.activeElement !== r.input && r.input.value !== value) {
          r.input.value = value; r.lastSentValue = value; r.lastSentComposing = false;
        }
      });
      s.order.slice().forEach(function (name) { if (!wanted[name]) OfficeTenTextInput.remove(s.records[name]); });
      s.order = order;
      // Context owns field order. Ordinary frames preserve existing DOM nodes.
      var cursor = s.container.firstChild;
      order.forEach(function (name) { var node = s.records[name].wrapper; if (node !== cursor) s.container.insertBefore(node, cursor); cursor = node.nextSibling; });
      OfficeTenTextInput.layout();
    },
    layout: function () {
      var s = OfficeTenTextInput.state;
      if (!s || !s.frame) return;
      var canvas = OfficeTenTextInput.canvas(), f = s.frame;
      var sw = OfficeTenTextInput.number(f.screenWidth, 0), sh = OfficeTenTextInput.number(f.screenHeight, 0);
      var box = canvas && canvas.getBoundingClientRect();
      var valid = box && sw > 0 && sh > 0 && box.width > 0 && box.height > 0;
      s.order.forEach(function (name) {
        var r = s.records[name], d = r.field, style = r.wrapper.style;
        if (!valid) { style.display = 'none'; r.visible = false; return; }
        var sx = box.width / sw, sy = box.height / sh;
        var x = OfficeTenTextInput.number(d.x, 0), y = OfficeTenTextInput.number(d.y, 0);
        var w = Math.max(0, OfficeTenTextInput.number(d.width, 0)), h = Math.max(0, OfficeTenTextInput.number(d.height, 0));
        var cx = OfficeTenTextInput.number(d.clipX, 0), cy = OfficeTenTextInput.number(d.clipY, 0);
        var cw = Math.max(0, OfficeTenTextInput.number(d.clipWidth, sw)), ch = Math.max(0, OfficeTenTextInput.number(d.clipHeight, sh));
        var left = Math.max(0, x, cx), top = Math.max(0, y, cy), right = Math.min(sw, x + w, cx + cw), bottom = Math.min(sh, y + h, cy + ch);
        r.visible = right > left && bottom > top;
        style.display = r.visible ? 'block' : 'none';
        if (!r.visible) return;
        style.left = (box.left + left * sx) + 'px'; style.top = (box.top + top * sy) + 'px';
        style.width = ((right - left) * sx) + 'px'; style.height = ((bottom - top) * sy) + 'px';
        r.input.style.left = ((x - left) * sx) + 'px'; r.input.style.top = ((y - top) * sy) + 'px';
        r.input.style.width = (w * sx) + 'px'; r.input.style.height = (h * sy) + 'px';
        var font = Math.max(4, Math.min(80, OfficeTenTextInput.number(f.fontSize, 20) * sy));
        r.input.style.fontSize = font + 'px'; r.input.style.padding = Math.max(1, font * .2) + 'px ' + Math.max(2, font * .4) + 'px';
      });
      if (s.pendingFocus) {
        var r = s.records[s.pendingFocus];
        if (r && r.visible && !r.input.disabled) {
          s.pendingFocus = null;
          try { r.input.focus({ preventScroll: true }); } catch (_) { r.input.focus(); }
        }
      }
    },
    focus: function (name) { var s = OfficeTenTextInput.state; if (s) { s.pendingFocus = name; OfficeTenTextInput.layout(); } },
    blur: function () {
      var s = OfficeTenTextInput.state; if (!s) return;
      s.pendingFocus = null;
      var r = s.focusedName && s.records[s.focusedName];
      if (r) { r.input.blur(); OfficeTenTextInput.blurRecord(r, 'api-blur'); }
      var canvas = OfficeTenTextInput.canvas();
      if (canvas && typeof canvas.focus === 'function') { try { canvas.focus({ preventScroll: true }); } catch (_) { canvas.focus(); } }
    },
    dispose: function () {
      var s = OfficeTenTextInput.state; if (!s) return;
      s.order.slice().forEach(function (name) { OfficeTenTextInput.remove(s.records[name]); });
      window.cancelAnimationFrame(s.raf);
      s.listeners.forEach(function (l) { l.where.removeEventListener(l.type, l.fn, l.capture); });
      if (s.container.parentNode) s.container.parentNode.removeChild(s.container);
      OfficeTenTextInput.state = null;
    }
  },
  OfficeTenTextInputSync__deps: ['$OfficeTenTextInput'],
  OfficeTenTextInputSync: function (json) { OfficeTenTextInput.sync(UTF8ToString(json)); },
  OfficeTenTextInputFocus__deps: ['$OfficeTenTextInput'],
  OfficeTenTextInputFocus: function (name) { OfficeTenTextInput.focus(UTF8ToString(name)); },
  OfficeTenTextInputBlur__deps: ['$OfficeTenTextInput'],
  OfficeTenTextInputBlur: function () { OfficeTenTextInput.blur(); },
  OfficeTenTextInputDispose__deps: ['$OfficeTenTextInput'],
  OfficeTenTextInputDispose: function () { OfficeTenTextInput.dispose(); }
});

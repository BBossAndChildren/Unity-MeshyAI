import React, {useEffect, useRef} from 'react';
import {createExperienceClient} from './client.js';

// Keep callbacks and selection stable in the parent. Start is explicitly owned
// by the parent so rerenders/React StrictMode never silently launch a new run.
export function Experience({siteUrl, manifest, sessionId, outbox, onEvent, onStatus, onClient}) {
  const frame = useRef(null), callbacks = useRef({onEvent, onStatus, onClient});
  callbacks.current = {onEvent, onStatus, onClient};
  useEffect(() => {
    const client = createExperienceClient({frame: frame.current, manifest, sessionId, outbox, onEvent: event => callbacks.current.onEvent?.(event), onStatus: status => callbacks.current.onStatus?.(status)});
    callbacks.current.onClient?.(client);
    return () => { client.dispose(); callbacks.current.onClient?.(null); };
  }, [siteUrl, manifest, sessionId, outbox]);
  const url = new URL(siteUrl, location.href); url.searchParams.set('parentOrigin', location.origin);
  return <iframe ref={frame} src={url.href} title="직업 3D 체험" allow="fullscreen" style={{width: '100%', height: '80vh', border: 0}} />;
}

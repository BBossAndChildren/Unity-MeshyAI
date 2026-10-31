/** Common v001 adapter: Unity owns counting; this receiver stores original events. */
export function createCareerReceiver({unity, frameWindow=null, origin=window.location.origin, onChange=()=>{}, storageKey='career-experience:receiver',timeoutMs=30000}) {
  const events=new Map(),pending=new Map(),requests=new Map();
  let sessionId=crypto.randomUUID(),experienceId=null,ended=null,lastError=null,lastUnconfirmedRequestId=null,roomId='PAN-001',scenarioId='career-net-253-office-documents',scenarioVersion='v002',startRejected=false,firstSequence=null;
  const currentEvents=()=>[...events.values()].filter(e=>e.experienceId===experienceId).sort((a,b)=>a.sequence-b.sequence);
  const state=()=>({sessionId,experienceId,roomId,scenarioId,scenarioVersion,ended,lastError,lastUnconfirmedRequestId,startRejected,sequencePrefixStatus:firstSequence===null?'unavailable':'known',pendingRequestIds:[...pending.keys()],events:currentEvents(),sessionEvents:[...events.values()].sort((a,b)=>a.sequence-b.sequence)});
  const persist=()=>{const current=state();const {sessionEvents,...checkpoint}=current;try{localStorage.setItem(storageKey,JSON.stringify(checkpoint));}catch{} onChange(current);};
  const validate=e=>e&&e.schemaVersion===1&&e.protocol==='career-experience'&&typeof e.type==='string';
  function receive(e) {
    if(!validate(e)||e.sessionId!==sessionId||e.experienceId!==experienceId||e.roomId!==roomId)return;
    if(e.type==='experience.error') {
      lastError=e.error;const call=pending.get(e.requestId);if(requests.get(e.requestId)?.request.action==='start_experience')startRejected=true;if(call){clearTimeout(call.timer);pending.delete(e.requestId);call.reject(new Error(e.error.code+': '+e.error.message));}persist();return;
    }
    if(e.scenarioId!==scenarioId||e.scenarioVersion!==scenarioVersion)return;
    if(e.type==='experience.started'&&Number.isSafeInteger(e.data?.firstSequence))firstSequence=e.data.firstSequence;
    if(e.type==='scenario.started'&&firstSequence===null)firstSequence=e.sequence;
    if(typeof e.eventId!=='string'||!Number.isSafeInteger(e.sequence)||e.sequence<1||typeof e.scenarioRunId!=='string')return;
    const previous=events.get(e.eventId);
    if(previous&&JSON.stringify(previous)!==JSON.stringify(e)){lastError={code:'EVENT_ID_CONFLICT',message:e.eventId};persist();return;}
    if(!previous)events.set(e.eventId,e);
    // End payloads may recover the entire ledger after a late listener. They
    // are existing events, never new attempts or a second counting authority.
    if(e.type==='experience.ended'&&Array.isArray(e.data?.events)) {
      for(const old of e.data.events)if(validate(old)&&old.sessionId===sessionId&&old.experienceId===experienceId&&old.roomId===roomId&&old.scenarioId===scenarioId&&old.scenarioVersion===scenarioVersion&&old.eventId&&Number.isSafeInteger(old.sequence)&&!events.has(old.eventId))events.set(old.eventId,old);
      const beginnings=e.data.events.filter(old=>old.type==='scenario.started'&&old.experienceId===experienceId).map(old=>old.sequence);if(beginnings.length)firstSequence=Math.min(...beginnings);
    }
    // A Unity user may end through the in-game pause menu. Such an observed,
    // matching terminal receipt is valid even without a frontend request.
    if(e.type==='experience.ended')ended=e;
    const call=pending.get(e.requestId);
    if(call&&e.type===call.type){clearTimeout(call.timer);pending.delete(e.requestId);call.resolve(e);}
    if(lastUnconfirmedRequestId===e.requestId){lastUnconfirmedRequestId=null;lastError=null;}
    persist();
  }
  const local=e=>{if(!frameWindow)receive(e.detail);};
  const message=e=>{if(e.origin!==origin||e.source!==frameWindow||e.data?.channel!=='career-experience')return;receive(e.data.event);};
  let listening=false;
  function listen(){if(listening)return;listening=true;window.addEventListener('career-experience:event',local);window.addEventListener('message',message);}
  function suspendListening(){if(!listening)return;listening=false;window.removeEventListener('career-experience:event',local);window.removeEventListener('message',message);}
  listen();
  function send(request,expectedType) {
    requests.set(request.requestId,{request,expectedType});
    const existing=pending.get(request.requestId);
    if(existing){unity().SendMessage('CareerProtocol','ReceiveControl',JSON.stringify(request));return existing.promise;}
    const promise=new Promise((resolve,reject)=>{
      const unconfirmed=()=>{pending.delete(request.requestId);lastUnconfirmedRequestId=request.requestId;lastError={code:'DELIVERY_UNCONFIRMED',message:'응답을 확인하지 못했습니다. 같은 요청 ID로 재전송할 수 있습니다.'};persist();reject(new Error(lastError.message));};
      const timer=setTimeout(unconfirmed,timeoutMs);
      pending.set(request.requestId,{resolve,reject,type:expectedType,timer});
      try{unity().SendMessage('CareerProtocol','ReceiveControl',JSON.stringify(request));}catch{clearTimeout(timer);unconfirmed();}
    });
    const call=pending.get(request.requestId);if(call)call.promise=promise;
    return promise;
  }
  const control=(action,extra={})=>({schemaVersion:1,protocol:'career-experience',requestId:crypto.randomUUID(),action,sessionId,experienceId,roomId,...extra});
  return {
    state,
    listen,
    suspendListening,
    start(selection={roomId:'PAN-001',scenarioId:'career-net-253-office-documents',scenarioVersion:'v002'}){if(experienceId&&!ended&&!startRejected)throw new Error('A current experience must end first.');roomId=selection.roomId;scenarioId=selection.scenarioId;scenarioVersion=selection.scenarioVersion;experienceId=crypto.randomUUID();ended=null;lastError=null;startRejected=false;firstSequence=null;persist();return send(control('start_experience',{scenarioId,scenarioVersion}),'experience.started');},
    end(){if(!experienceId)throw new Error('Start an experience first.');return send(control('end_experience',{reason:'USER_REQUESTED_END'}),'experience.ended');},
    retry(requestId){const call=requests.get(requestId);if(!call)throw new Error('Unknown requestId');return send(call.request,call.expectedType);},
    replay(){unity().SendMessage('CareerProtocol','Replay','');},
    sequenceGaps(){let sorted=state().events,missing=[];if(sorted.length&&firstSequence!==null&&sorted[0].sequence>firstSequence)missing.push([firstSequence,sorted[0].sequence-1]);for(let i=1;i<sorted.length;i++)if(sorted[i].sequence>sorted[i-1].sequence+1)missing.push([sorted[i-1].sequence+1,sorted[i].sequence-1]);return missing;},
    // Consumers may inspect this after a reload, but must not fabricate an
    // aborted result from an unconfirmed transport interruption.
    readPrevious(){try{return JSON.parse(localStorage.getItem(storageKey));}catch{return null;}},
    dispose(){suspendListening();for(const call of pending.values()){clearTimeout(call.timer);call.reject(new Error('Receiver detached before response'));}pending.clear();}
  };
}

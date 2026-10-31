import React,{useEffect,useRef,useState} from 'react';
import {createRoot} from 'react-dom/client';
import {createCareerReceiver} from './receiver.js';
import './style.css';
import {careers} from './careers.js';

function App(){
  const frame=useRef(null),adapter=useRef(null);
  const [showEvents,setShowEvents]=useState(false);
  const [selected,setSelected]=useState(careers[0].scenarioId);
  const [ready,setReady]=useState(false),[busy,setBusy]=useState(false),[status,setStatus]=useState('Unity 로딩 중'),[state,setState]=useState({events:[]}),[closed,setClosed]=useState(false),[recovered,setRecovered]=useState(null);
  const build=new URL('../index.html',window.location.href).href;
  useEffect(()=>{
    const timer=setInterval(()=>{
      try{
        const win=frame.current?.contentWindow;
        if(!win?.officeUnity||!win?.workplaceState)return;
        clearInterval(timer);
        win.careerExperienceParentOrigin=window.location.origin;
        adapter.current=createCareerReceiver({unity:()=>win.officeUnity,frameWindow:win,origin:window.location.origin,onChange:s=>{window.careerReceiverState=s;setState(s);}});
        const previous=adapter.current.readPrevious();
        if(previous?.experienceId&&!previous.ended){const interruption={code:'SESSION_INTERRUPTED',initiatedBy:'unknown',deliveryStatus:'unconfirmed',lastSaved:previous};window.careerReceiverRecovered=interruption;setRecovered(interruption);}
        window.careerReceiver=adapter.current;setReady(true);setStatus('준비 완료 · 체험 시작을 선택하세요.');
      }catch{setStatus('실행본과 수신 예제를 같은 HTTP 출처에 두어야 합니다.');}
    },250);
    return()=>{clearInterval(timer);adapter.current?.dispose();};
  },[]);
  async function call(action){setBusy(true);try{const event=action==='retry'?await adapter.current.retry(state.lastUnconfirmedRequestId):action==='start'?await adapter.current.start({scenarioId:selected,scenarioVersion:'v002',roomId:careers.find(x=>x.scenarioId===selected).roomId}):await adapter.current[action]();setStatus(event.type==='experience.ended'?'종료 응답을 수신·보존했습니다: '+event.result.outcome:'선택한 직업 체험을 시작했습니다.');}catch(e){setStatus(e.message);}finally{setBusy(false);}}
  return <><header><h1>직업 10개 직접 작업 체험</h1><label>직업 선택 <select aria-label="직업 선택" value={selected} disabled={busy||!!state.experienceId&&!state.ended&&!state.startRejected} onChange={e=>setSelected(e.target.value)}>{careers.map(c=><option key={c.scenarioId} value={c.scenarioId}>{c.name} · {c.roomId}</option>)}</select></label><p>{status}</p><nav><button disabled={!ready||busy||state.experienceId&&!state.ended&&!state.startRejected} onClick={()=>call('start')}>체험 시작</button><button disabled={!ready||busy||!state.experienceId||!!state.ended} onClick={()=>call('end')}>체험 종료 · 기록 받기</button><button disabled={!ready||busy||!state.lastUnconfirmedRequestId} onClick={()=>call('retry')}>미확인 요청 같은 ID로 재전송</button><button disabled={!ready} onClick={()=>adapter.current.replay()}>기록 재수신</button><button disabled={!state.ended} onClick={()=>setClosed(true)}>응답 보존 후 화면 닫기</button></nav><small>작업 판정과 횟수의 원장은 Unity입니다. 강제 종료·통신 단절은 사용자 포기로 확정하지 않습니다.</small></header>
  {!closed&&<iframe title="실제 Unity WebGL 공간" ref={frame} src={build}/>}
  <section><h2>수신 결과</h2>{recovered&&<p role="status">이전 체험의 종료 응답이 미확인입니다. SESSION_INTERRUPTED / 원인 미확인으로 보존했으며 사용자 포기·실수로 집계하지 않습니다. 현재 페이지는 새 실행이며 이전 진행을 자동 완료·복원하지 않습니다.</p>}<p>고유 이벤트 {state.events.length}개 · {state.lastError?.code??'제어 오류 없음'}</p>{state.ended&&<pre>{JSON.stringify({process:state.ended.process,result:state.ended.result,context:state.ended.context},null,2)}</pre>}<details onToggle={e=>setShowEvents(e.currentTarget.open)}><summary>원본 과정 이벤트 · sequence 정렬</summary>{showEvents&&<pre>{JSON.stringify(state.events,null,2)}</pre>}</details></section></>;
}
createRoot(document.getElementById('root')).render(<App/>);

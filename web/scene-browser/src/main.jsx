import React, {useEffect, useRef, useState} from 'react';
import {createRoot} from 'react-dom/client';
import {bootUnity, openScene} from './unity.js';
import './style.css';

function App() {
 const [data,setData]=useState(null),[error,setError]=useState(''),[query,setQuery]=useState('');
 const [selected,setSelected]=useState(new URLSearchParams(location.search).get('scene') || 'PRM-001');
 const [status,setStatus]=useState('Unity 빌드 연결 전'),[ready,setReady]=useState(false),[busy,setBusy]=useState(false),[progress,setProgress]=useState(0),[command,setCommand]=useState('');
 const [specs,setSpecs]=useState(null),[specError,setSpecError]=useState('');
 async function loadSpecs(){try{const r=await fetch('/asset-specs.json');if(!r.ok)throw Error('소품 명세 로딩 실패');setSpecs(await r.json());}catch(e){setSpecError(e.message);}}
 const canvas=useRef(null), player=useRef(null),bridgeReady=useRef(false),request=useRef(null),timer=useRef(null);
 useEffect(()=>{
  fetch('/scenes.json').then(r=>{if(!r.ok)throw Error('명세서를 읽지 못했습니다.');return r.json()}).then(setData).catch(e=>setError(e.message));
  function event(e){const m=e.detail;if(!m || typeof m.type!=='string')return;
   if(m.type==='ready'){bridgeReady.current=true;if(player.current){setReady(true);setStatus('Unity 준비 완료')}return;}
   if(m.requestId!==request.current)return;
   if(m.type==='loaded'||m.type==='error'){clearTimeout(timer.current);setBusy(false);setStatus(m.type==='loaded'?`${m.sceneId} 실행 완료`:m.message);}
  }
  window.addEventListener('unity-scene-event',event);
  const pop=()=>setSelected(new URLSearchParams(location.search).get('scene')||'PRM-001');window.addEventListener('popstate',pop);
  return ()=>{window.removeEventListener('unity-scene-event',event);window.removeEventListener('popstate',pop);clearTimeout(timer.current);};
 },[]);
 if(error)return <main role="alert">{error}</main>;
 if(!data)return <main>명세서 로딩 중…</main>;
 const scene=data.scenes.find(s=>s.id===selected)||data.scenes[0];
 function choose(s){setSelected(s.id);history.pushState(null,'',`?scene=${encodeURIComponent(s.id)}`);setCommand('');}
 async function start(){setBusy(true);setStatus('공용 실행기 로딩 중');try{
  player.current=await bootUnity(canvas.current,data.unity,setProgress);
  if(bridgeReady.current){setReady(true);setStatus('Unity 준비 완료');}else setStatus('Unity SceneBridge 준비 대기');
 }catch(e){setStatus(e.message);}finally{setBusy(false);}}
 function load(){setBusy(true);setStatus(`${scene.name} 로딩 중`);request.current=openScene(player.current,scene.panoramaId,scene.contentVersion);
  timer.current=setTimeout(()=>{setBusy(false);setStatus('응답 시간 초과: Unity 콘솔과 다운로드 상태를 확인하세요.');request.current=null;},120000);}
 const visible=data.scenes.filter(s=>`${s.id} ${s.name} ${s.category}`.includes(query));
 return <main><header><div><small>SCENE LIBRARY / REACT × UNITY</small><h1>공간을 고르고, 하나의 실행기로.</h1><p>명세서를 확인한 뒤 필요한 장면만 불러옵니다.</p></div><span className="count">{data.scenes.length}개 명세</span></header>
 <div className="layout"><aside><label htmlFor="search">공간 검색</label><input id="search" value={query} onChange={e=>setQuery(e.target.value)} placeholder="일반 사무실, 상담실…"/><div className="list">{visible.map(s=><button className={s.id===scene.id?'chosen':''} key={s.id} onClick={()=>choose(s)}><small>{s.id} · {s.panoramaId||'참고 이미지 미등록'}</small><strong>{s.name}</strong><span>{s.model?'GLB 제작됨 · Unity 연결 전':'제작 전'}</span></button>)}{!visible.length&&<p>검색 결과가 없습니다.</p>}</div></aside>
 <article><div className="detail"><small>{scene.id} / {scene.specVersion}</small><h2>{scene.name}</h2><p>{scene.description}</p><div className="badges"><span>{scene.category}</span><span>{scene.model?'GLB 검수 기록 있음':'기획 명세'}</span><span>Unity 미검증</span></div>
 {scene.image&&<img className="hero" src={scene.image} alt={`${scene.name} 실제 참고 이미지`}/>}
 <h3>구성 명세</h3>{scene.model?<><p>{scene.model.triangles.toLocaleString()}삼각형 · {scene.model.quantity}개 배치 · {scene.model.bytes.toLocaleString()}바이트</p><table><thead><tr><th>소품</th><th>수량</th><th>개당 삼각형</th></tr></thead><tbody>{scene.model.props.map(p=><tr key={p.asset_ref.asset_id}><td>{p.name}</td><td>{p.instance_count}</td><td>{p.triangles_per_instance}</td></tr>)}</tbody></table></>:<p>{scene.keyProps.join(' · ')} — 계획 소품이며 실제 제작·배치 수량은 미정입니다.</p>}
 {scene.layoutIntent&&<section><h3>배치 의도</h3><p>{scene.layoutIntent}</p><details><summary>상세 제작 프롬프트</summary><p style={{whiteSpace:'pre-wrap'}}>{scene.prompt}</p></details></section>}
 <section><h3>개별 소품 제작 명세</h3><p>후보는 제작 완료 모델과 구분합니다. 실제 배치 수량은 위 GLB 기록이 있는 경우 해당 수치를 따릅니다.</p>{!specs&&<button onClick={loadSpecs}>소품 상세 명세 불러오기</button>}{specError&&<p role="alert">{specError}</p>}{specs&&scene.requiredCandidateIds?.map(id=>{const c=specs.candidates.find(x=>x.candidate_id===id);return c?<details key={id}><summary>{c.candidate_id} · {c.name}</summary><p>구성: {c.specification.components.join(' · ')}</p><p>{c.generation_reason}</p><p>{c.reuse_condition}</p><details><summary>전체 원본 명세 · 사용 후보 및 실제 사용 이력</summary><pre>{JSON.stringify(c,null,2)}</pre></details></details>:<p key={id}>{id} 명세 미등록</p>})}</section>
 <div className="actions"><button disabled={!data.unity.enabled||busy||ready} onClick={start}>① Unity 실행기 시작</button><button disabled={!ready||busy||!scene.unityReady} onClick={load}>② 이 공간 실행</button><button onClick={()=>setCommand(`unityInstance.SendMessage('SceneBridge', 'OpenScene', '${JSON.stringify({sceneId:scene.panoramaId||'미등록',contentVersion:scene.contentVersion||'미빌드',requestId:'요청별-고유-ID'})}');`)}>호출 코드 보기</button></div>
 <p role="status">{status}{busy&&!ready?` ${Math.round(progress*100)}%`:''}</p>{!data.unity.enabled&&<p className="notice">현재 Unity 빌드가 없습니다. 아래 코드는 연결 계약 예제이며 장면 실행 결과가 아닙니다.</p>}{command&&<pre>{command}</pre>}
 <canvas ref={canvas} hidden={!data.unity.enabled} aria-label="Unity 공간 실행 화면"/>
 </div></article></div><footer>명세는 저장소 catalog에서 가져온 조회용 스냅샷입니다. 기획 승인·제작·Unity 실행 상태는 각각 구분합니다.</footer></main>;
}
createRoot(document.getElementById('root')).render(<App/>);

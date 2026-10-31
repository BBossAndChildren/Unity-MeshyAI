const {chromium}=require(process.env.PLAYWRIGHT_MODULE||'playwright');
const fs=require('fs');
const path=require('path');
const buildId=process.argv[2]||'office-assistant-v005';
const E=path.join(__dirname,'../../../../docs/machine/evidence/',buildId)+'/';
fs.mkdirSync(E,{recursive:true});
(async()=>{
 const browser=await chromium.launch({headless:true,executablePath:process.env.CHROME_PATH||'C:/Program Files/Google/Chrome/Application/chrome.exe',args:['--enable-webgl','--use-angle=swiftshader','--enable-unsafe-swiftshader']});
 const context=await browser.newContext({viewport:{width:1440,height:900},hasTouch:true});
 const page=await context.newPage();
 const report={schema_version:3,build_id:buildId,checked_at:new Date().toISOString(),environment:'Chrome / Windows / actual Unity WebGL over HTTP; Playwright mouse, keyboard, emulated touch; SwiftShader',cases:[],errors:[]};
 page.on('pageerror',e=>report.errors.push(e.message));
 page.on('console',m=>{if(m.type()==='error')report.errors.push(m.text())});
 const state=()=>page.evaluate(()=>window.officeState);
 const check=(ok,note)=>{if(!ok)throw Error(note)};
 const settle=()=>page.waitForTimeout(520);
 const snap=async(name)=>{await page.screenshot({path:E+name+'.png'})};
 const record=async(name,fn)=>{try{await fn();report.cases.push({name,status:'pass',snapshot:await state()});console.log('PASS '+name)}catch(e){report.cases.push({name,status:'fail',error:e.message,snapshot:await state()});await snap('failure-'+name);throw e}finally{fs.writeFileSync(E+'webgl-ui-acceptance.json',JSON.stringify(report,null,2))}};
 async function button(label,method='mouse'){
  await settle();const s=await state();const b=s.buttons.find(b=>b.label.includes(label));check(b,'button not found '+label+' in '+s.buttons.map(b=>b.label));
  check(b.enabled,'button disabled '+label);
  if(method==='touch')await page.touchscreen.tap(b.x,b.y);else await page.mouse.click(b.x,b.y);
  await settle();
 }
 async function open(id,method='mouse'){
  const s=await state(); const target=s.targets.find(t=>t.id===id);check(target,'target '+id);
  if(method==='touch') await page.touchscreen.tap(target.x,target.y);else if(method==='keyboard'){
   await page.keyboard.press({monitor:'Digit1',copier:'Digit2',cabinet:'Digit3'}[id],{delay:90});await page.waitForTimeout(90);await page.keyboard.press('Enter',{delay:90});
  }else await page.mouse.click(target.x,target.y);
  await settle();
  if((await state()).panel!==id&&id==='cabinet'&&method!=='keyboard'){
   // The cabinet center is behind the background workstation. Select an exposed mesh surface.
   for(const [dx,dy] of [[45,-12],[55,5],[35,25],[-40,-15],[55,-25],[65,-5]]){
    if(method==='touch')await page.touchscreen.tap(target.x+dx,target.y+dy);else await page.mouse.click(target.x+dx,target.y+dy);
    await settle();if((await state()).panel===id){report.cabinet_surface_click={x:target.x+dx,y:target.y+dy};break}
   }
  }
  check((await state()).panel===id,'object did not open '+id+' '+JSON.stringify((await state()).feedback));
  const zoom=await state();check(zoom.closeup&&zoom.visibleRenderers===1&&zoom.cameraDistance<3,'actual selected model not enlarged/isolated '+id);
 }
 async function keyboardButton(id,label){
  await open(id,'keyboard');const s=await state();const enabled=s.buttons.filter(b=>b.enabled);const i=enabled.findIndex(b=>b.label.includes(label));check(i>=0,'keyboard button '+label);
  for(let n=0;n<i;n++){await page.keyboard.press('Tab',{delay:90});await page.waitForTimeout(90)}await page.keyboard.press('Enter',{delay:90});await settle();
 }
 async function confirm(method='mouse'){
  for(const label of ['어떤 자료','몇 부가','어느 칸','요청 요약']){
   if(method==='keyboard')await keyboardButton('monitor',label);else await button(label,method);
  }
 }
 async function save(method='mouse'){
  if(method==='keyboard'){await keyboardButton('monitor','11월 2일');await keyboardButton('monitor','수정 내용 저장')}
  else {await button('11월 2일',method);await button('수정 내용 저장',method)}
 }
 async function close(){await page.keyboard.press('Escape');await settle();const s=await state();check(!s.closeup&&s.visibleRenderers===30,'room view not restored')}
 async function reset(changed){await page.keyboard.press('KeyR');await settle();await button(changed?'변경 요청 경로':'기본 경로');check((await state()).session.state==='request_pending','reset pending')}
 async function finish(method='mouse'){
  await open('cabinet',method);await button('회의자료 칸에 보관',method);
  await button('날짜:',method);await button('부수:',method);
  if((await state()).session.expectedCopies===3)await button('부수:',method);
  await button('보관처:',method);await button('인계 요약 전송',method);
  check((await state()).session.complete,'handoff complete');
 }
 try{
  await page.goto('http://127.0.0.1:8173/'+report.build_id+'/');
  await page.waitForFunction(()=>window.officeState&&window.officeState.buttons,{timeout:120000});await settle();
  await record('actual_unity_scene',async()=>{const s=await state();check(s.triangles===4308&&s.interactiveObjects===3,'scene counts');await snap('office-ready')});
  await record('camera_drag_not_click',async()=>{let t=(await state()).targets[0];await page.mouse.move(t.x,t.y);await page.mouse.down();await page.mouse.move(t.x+35,t.y+20,{steps:10});await page.mouse.up();await settle();check((await state()).panel==='','drag opened panel');await reset(false)});
  await record('sequence_violation',async()=>{const t=(await state()).targets[1];await page.mouse.click(t.x,t.y);await settle();check((await state()).session.state==='request_pending'&&(await state()).panel==='','early copier unlocked')});
  await open('monitor');await snap('monitor-questions');
  await record('selected_item_closeup_and_popup',async()=>{const s=await state();check(s.closeup&&s.cameraDistance<2&&s.visibleRenderers===1,'monitor closeup');check(s.buttons.some(b=>b.x>744),'paper popup controls')});
  await record('missing_request_information',async()=>{await button('요청 요약');check((await state()).session.state==='request_pending','missing slots accepted')});
  await confirm();
  await record('date_error_and_retry',async()=>{await button('수정 내용 저장');check((await state()).session.state==='request_confirmed','wrong date saved');await save();check((await state()).session.state==='document_saved','correct save failed')});
  await snap('monitor-document');await close();await open('copier');await snap('copier-popup');
  await record('copies_file_revision_errors',async()=>{
   await button('출력 시작');check((await state()).session.state==='document_saved','wrong copies printed');
   await button('부수:');await button('자료:');await button('출력 시작');check((await state()).session.state==='document_saved','wrong file printed');await button('자료:');
   await button('문서 revision:');await button('출력 시작');check((await state()).session.state==='document_saved','old revision printed');await button('문서 revision:');
  });
  await record('printing_duplicate_click_and_pause',async()=>{
   await button('출력 시작');let s=await state();check(s.session.state==='printing','printing not started');await snap('copier-printing-paper');let b=s.buttons.find(b=>b.label.includes('중복 실행 잠금'));check(b&&!b.enabled,'print button not locked');
   for(let i=0;i<5;i++)await page.mouse.click(b.x,b.y);await page.keyboard.press('KeyP');await settle();check((await state()).session.paused,'pause');await page.waitForTimeout(2800);check((await state()).session.state==='printing'&&(await state()).session.printCompletions===0,'paused timer progressed');
   await page.keyboard.press('KeyP');await page.waitForFunction(()=>window.officeState.session.state==='print_ready',{timeout:10000});check((await state()).session.printCompletions===1,'duplicate completion');
  });
  await close();await open('cabinet');await snap('cabinet-popup');
  await record('classification_error',async()=>{await button('인사자료 칸에 보관');check((await state()).session.state==='print_ready','wrong folder accepted');await button('회의자료 칸에 보관');check((await state()).session.state==='filed','correct folder')});
  await record('handoff_required_and_base_complete',async()=>{check(!(await state()).session.complete,'premature complete');await button('인계 요약 전송');check((await state()).session.state==='filed','wrong summary accepted');await button('날짜:');await button('부수:');await button('보관처:');await button('인계 요약 전송');check((await state()).session.complete,'base complete');await snap('base-complete')});
  await record('completed_reclick',async()=>{await close();const t=(await state()).targets[1];for(let i=0;i<3;i++)await page.mouse.click(t.x,t.y);await settle();const s=(await state()).session;check(s.complete&&s.printCompletions===1,'completion mutated')});
  await record('full_reset',async()=>{await reset(true);const s=(await state()).session;check(s.documentRevision===1&&s.savedRevision===1&&s.requestRevision===1&&s.confirmedRequestRevision===0&&s.printCompletions===0&&s.printedCopies===0&&!s.complete&&!s.paused,'reset values')});
  await record('keyboard_request_change_reconfirmation',async()=>{await open('monitor','keyboard');await confirm('keyboard');await save('keyboard');let s=(await state()).session;check(s.changed&&s.requestRevision===2&&s.confirmedRequestRevision===0&&s.expectedCopies===3&&s.state==='request_pending','change invalidation');await confirm('keyboard');check((await state()).session.state==='document_saved','reconfirm');await snap('request-change-confirmed')});
  await close();await open('copier','keyboard');
  await record('changed_request_3_copies',async()=>{await keyboardButton('copier','출력 시작');check((await state()).session.state==='document_saved','one copy accepted');await keyboardButton('copier','부수:');await keyboardButton('copier','출력 시작');check((await state()).session.state==='document_saved','old 2 copies accepted');await keyboardButton('copier','부수:');await keyboardButton('copier','출력 시작');await page.waitForFunction(()=>window.officeState.session.state==='print_ready',{timeout:10000});check((await state()).session.printedCopies===3,'3 copies');await close();await finish();await snap('changed-complete')});
  await record('emulated_touch_selection_and_dialogue',async()=>{await reset(false);await open('monitor','touch');await confirm('touch');await save('touch');check((await state()).session.state==='document_saved','touch save');await snap('touch-monitor')});
  await record('reset_during_print',async()=>{await close();await open('copier');await button('부수:');await button('출력 시작');check((await state()).session.state==='printing','reset test printing');await reset(false);await page.waitForTimeout(3000);check((await state()).session.state==='request_pending'&&(await state()).session.printCompletions===0,'old print completed after reset')});
  await page.evaluate(()=>window.officeUnity.SendMessage('OfficeExperience','RunAcceptanceSuite',''));
  await page.waitForFunction(()=>window.officeTests);
  report.csharp_runtime_suite=await page.evaluate(()=>window.officeTests);check(report.csharp_runtime_suite.failed===0,'WebGL C# suite failure');
  await page.setViewportSize({width:960,height:600});await settle();await snap('small-viewport');report.small_viewport={width:960,height:600,status:'rendered'};
  await page.setViewportSize({width:1440,height:900});await reset(false);await snap('office-ready');
  report.status=report.cases.every(c=>c.status==='pass')&&report.errors.length===0?'pass':'fail';report.final_state=await state();
 }catch(e){report.status='fail';report.failure=e.stack;console.error(e)}
 finally{report.finished_at=new Date().toISOString();fs.writeFileSync(E+'webgl-ui-acceptance.json',JSON.stringify(report,null,2));await browser.close()}
 if(report.status!=='pass')process.exit(1);
})().catch(e=>{console.error(e);process.exit(1)});

# 71공간 실제 제작 작업 재개 기록

## 현재 완료 상태 — workplaces-v006 전달 확인 완료

2026-10-31. 71개 실제 3D 공간과 선택된 사무보조원 직접 작업 범위, Unity↔React 수신 예제의 제작·등록·대상 환경 검수·전달을 완료했다. 아래 중간 기록은 당시 상태이며 현재 대기 작업이 아니다.

- 정식 기준: docs/machine/catalog/workplace-production-v001.json 및 docs/human/builds/workplaces-v006.md.
- 현재319 모델 참조(248소품+71조립),805개 배치. 보존489버전 중 현재319 ready,170과거 버전은 각자 상태 보존. 프로젝트 전체835배치에는 legacy30개 포함.
- 실제 v006 Unity nativePlay71/71 및 HTTP71/71+공통2건 pass, 사무체험 실제19건 pass/제품오류0/콘솔오류0. 원본 자동화 관찰3건과 재검증을 보존했다. v005는 작은 화면 입력 결함이 있던 중간본으로 남겼다.
- 최종319 GLB 재가져오기/957방향 이미지/30축소 시트, 지지면476건 및 새로운v00671쌍+원본픽셀 색상검토 통과. 모든 장면908~4308삼각형,공용 재질1/PNG1,2508×2508원본픽셀 일치. 자세한 범위·보이지 않는 작은 부위와 낮은 선 대비의 한계는 최종 시각 보고에 명시했다.
- 전달: unity/webgl/packages/workplaces-v006.zip /30156167bytes / SHA256 1decbc9185889118ca649b410aa220349f35ac0e6de02b9e3e2c77e0ff991798. manifest 동명 .manifest.json. ZIP16파일 CRC/해시 및 실제 압축 해제본 HTTP공간선택·모니터열기·React시작수신2건 pass. package-integrity.json/package-http-boot.json 참조.
- 실행 안내: docs/human/builds/workplaces-v006-run.md. HTTP8178 서버는 실행 중이며 http://127.0.0.1:8178/workplaces-v006/receiver/ 로 체험/이벤트 원장을 확인할 수 있다. 재시작 시 안내의 Python서버 명령을 사용한다. 검수용 Chrome/Node PTY는 종료했다.
- 소스15개와 AGENTS.md는 빌드 전/후/최종 검수 후 동일하다. source-snapshot-after-acceptance.json 참조. 커밋·푸시·외부배포 및 유료 Meshy/이미지 호출은 하지 않았다. Meshy크레딧0,실제 대화 토큰은 제공되지 않아 null.
- 미검증/제외: 네이티브Editor 업무GUI는 Computer Use 앱 접근 승인 시간초과로 미검증(네이티브장면 검수와 별도), 물리모바일·다른브라우저·하드웨어GPU성능·HTTPS외부서버 미검증. EX010추가이력복구연습 및 나머지551직업초안은 선택된 구현범위가 아니다. 71개 공간을 다시 제작할 필요는 없다.

## 보존한 작업 중간 기록

## 최신 재개 지점 — workplaces-v006 실제 최종 검수 중

아래 과거 기록보다 이 절과 현재 catalog를 우선한다. 전체 완료 처리는 아직 하지 않았다.

최신 발견: v005의 실제71 HTTP공간과71 nativePlay는 모두 pass. 그러나900×600사무체험에서GUI좌표 변환 오류 때문에Tab초점이 실패했고 전환시간0.45가하드코딩인점을발견했다. direct_protocol 수정 완료·동결: OfficeDirectExperience SHA256 bb0f6559060478b322636aef9b97090f22c1f9ddc0948efbef71886b1f36d085. GUI 좌표 변환, serialized transitionSeconds 및 모션 감소 UI 옵션을 함께 보완했다. workplaces-v006 실제 빌드 성공(오류0·경고0,57566557bytes). source15개/dataJSON및AGENTS동일성pass. receiverdist-v006복사완료. root는UnityPlay71재실행중, rootHTTP hostPTY38832에서v006init후directagent900x600키보드/모션옵션우선검수결과를기다린다. 통과후모든71실행을다시수행한다. WorkplaceExplorer표시명정리SHA7570fc8c도포함. v005실행증거는중간본으로보존하며최종결과로복사하지않는다. v005ZIP은미제작. v005package중간staging은outputs아래보존한다.

- 2026-10-31: 최종 모델 교정 완료. 현재 71개 조립/248개 구성 에셋, 총 805개 배치. 보존된 옛 OfficeAssistant.unity 30개를 포함한 프로젝트 원장 범위는 835개이며 최종 빌드 배치와 다르다. 등록된 모든 과거 버전을 현재 제작 종수와 혼동하지 않는다.
- workplaces-v005 실제 Unity WebGL 빌드 성공: 오류 0, 경고 0, Unity 보고 57,549,236 bytes. `docs/machine/evidence/workplaces-v005/build-result.json` 및 `unity-build.log` 참조. v001~v004는 중간본으로 보존한다.
- palette-import.json에서 2508×2508 전체 RGBA 픽셀 해시 일치 확인. source-snapshot-after-build.json에서 13개 소스 및 AGENTS.md 변경 없음 확인.
- 최종 receiver는 web/career-receiver/dist-v006 전체이며 v005/receiver에 licenses 포함 복사 완료. 유료 Meshy/이미지 호출 0, 크레딧 0. 실제 대화 토큰은 미제공(null)으로 기록한다.
- root 실제 Chrome HTTP 검수 host PTY 90783, HTTP 8178. functions store roomQAProgramV5. 모든 71개 방을 실제 GUI로 진입하고 회전/선택/1440×900 및 900×600 캡처 중이다. 결과 `docs/machine/evidence/workplaces-v005/http-webgl-rooms.json`. 완료 전 전체 pass로 등록하지 않는다.
- root 실제 Unity batchmode-nographics Play Mode 71장면 검수 완료 여부는 `unity-editor-play-rooms.json`과 outputs/workplaces-v005-editor-play.log를 확인한다. 이 경로는 화면 렌더링 증거가 아니며 브라우저 캡처와 구별한다.
- direct_protocol agent가 v005 actual Unity↔React 사무 체험 회귀 검사 중이다. visual_audit는 모델 수정 완료 후 최종 HTTP 캡처를 읽기 전용 검토한다. catalog_handover는 실제 근거를 기다려 원장/ready/빌드/문서를 마감한다. 공유 catalog는 그 agent만 쓴다.
- 남은 순서: 71 HTTP/native 보고서 확인 → 사무/프로토콜 최종 보고서 확인 및 실패 수정 → catalog/문서 반영 → root가 고유 workplaces-v005 ZIP, manifest, 실행 안내 제작 → ZIP 풀어서 HTTP 재실행 확인 → 최종 요약. 새로운 소스 수정이 필요하면 v005를 중간본으로 보존하고 새 빌드를 생성한다.
- reducedMotion은 Inspector 설정 경로이며 WebGL 사용자 설정 UI/즉시 전환 실검증은 아직 제공하지 않았다. 물리 모바일, 다른 브라우저/하드웨어 GPU, HTTPS 실서버는 미검증으로 남긴다. 승인된 사무 시나리오 1개와 551개 초안을 구별한다.

2026-10-31 KST. 전체 완료 아님. 원장 workplace-production-v001.json, 원본 지침 AGENTS.md. 사용자는 전체 제작/조립/구현/검수를 위임했으며 개별 승인을 기다리지 않는다. 유료 호출 승인 없음: 이번 Meshy/이미지 호출0·크레딧0. 기존 변경/원본/버전/빌드 보존. 커밋·푸시·외부배포 금지.

## 현재 결과

- 최초22개 버전에 더해231종 새 prop,70개 새 방 실제 Blender 제작/재가져오기. 기존 office와 합쳐71공간. 상세 교정 버전은 현재 assets/scene-assemblies/progress를 읽는다. 후보262, 공간 필수244, 기존모델참조후보17, 공통55를 구분한다.
- 71 Unity 장면/총803배치가 v002/v003에서 실제 작성됐다. 새 props는 개별 FBX와 공용재질 prefab으로 적용, 배치 원장은 asset-usages.
- v001 중간5공간, v002/v003 중간71공간 실제 WebGL 생성. v003 오류0·경고0. v004도 중간본: 최근 Esc/키보드 수정 전, 최종 검수에 쓰지 않는다.
- 실제최종GLB current302ID 3방향 검토 중 바닥/지지면 문제를 계속 교정중. agent visual_audit가 침대1044/소파1215 다리, 대기석1025 연결, floor/rotated/support 전체감사를 한번에 수행중. 이 작업 끝 전 다음 finalbuild 금지. 원본은 새버전으로만 보완.
- office 원본 OfficeExperience.cs/CareerRules.cs/OfficeAssistant.unity 보존. 새 OfficeDirectExperience.cs + CareerProtocol.cs + CareerProtocol.jslib, 새 OfficeAssistantDirect.unity를 WorkplaceBuild가 만든다. 3물건/문서직접입력/부수입력/분류보드/인계/종료프로토콜 구현. 실제 v003테스트에서 focused Esc와 분류 Enter 이중처리를 발견해 수정했다. direct_protocol이 수정후 freeze와 최종실행 검수 담당.
- root는 WorkplaceExplorer에 한국어물건명 Registry.assets 표시를 추가했다. 다음 registry 생성에 assets:[{assetId,version,name}] 포함 필요. 진단 selectedInstance는 ID, 제품화면 selected는사람이읽는명칭.

## 담당/경합

- direct_protocol: OfficeDirectExperience/CareerProtocol/jslib + React receiver + scenario amendment, 실제 office/React QA. 새 scenario package v003은 office v002 한개개정이고 다른551초안자동승인없음. receiver 최신 clean dist-v005 예정(이전dist-v004에favicon404 수정). root에최신bundle확인.
- visual_audit: comprehensive floor/support 실제 모델수정 +3방향 증거. 이 agent만 assets/assemblies/progress 제작등록쓰기중.
- catalog_handover: assets/unity paths/사용원장/사람문서 담당. 현재 assets/progress쓰기를 visual교정완료까지 정지. 중간build 사실만 등록, 최종pass없음.
- root: WorkplaceBuild.cs/WorkplaceExplorer.cs/기존 OfficeEditorPlay.cs의 RunWorkplaces 확장, 최종빌드/전체71 HTTP QA/EditorPlay/전달ZIP.

## 실행환경/세션

- Blender D:/Program/Blender/blender-5.2.4-candidate+v52.4f5026e99892-windows.amd64-release/blender.exe
- Unity D:/Program/Unity/Unity Hub/Edit/6000.3.26f1/Editor/Unity.exe
- 실제 호스트 실행은 exec_command require_escalated가 필요했다(자동승인됨). node_repl Chrome은 ERR_NETWORK_ACCESS_DENIED이므로 실제브라우저검수는 escalated host Node PTY, 코드파일설치않고 node -e로만실행.
- HTTP8178 hostserver: python -m http.server8178 --bind127.0.0.1 --directory D:/github/Unity-MeshyAI/unity/webgl/builds. 기존 session9934.
- root host Node PTY session28605 현재 workplaces-v004 중간 QA를 실제 실행한 상태. 최종build init 명령으로 보고서/URL 전환 가능. 명령 JSON line: {action:init,build:workplaces-v005}, {action:rooms,ids:[PAN-002,...]}, {action:common}, {action:state}, {action:close}. 모든 JSON key/value는 실제 전송시 따옴표. functions.store roomQAProgramV4에 실행코드 보존. 실제각방마우스UI선택·삼각형/재질/텍스처·키보드회전·전체/축소스크린샷, http-webgl-rooms.json 저장. 진단30frame지연 때문에 waitForFunction으로갱신기다림. 이전 sessions28705/37418/76575닫음. 실제thumb드래그로먼공간선택성공, GUIwheel은1event20px이라원래드라이버30step으로끝까지못감. v004의2/71/4공간각각실제pass+pause/inputlock/resume/에뮬레이트touch공통pass 있으나최종판증거로승계금지.
- root node_repl qaBrowser는 sandbox미사용으로닫음. direct_protocol은 별도 dp-prefix hostPTY로 office실제테스트중.
- Playwright 모듈 D:/Codex/MeshyAi/outputs/office-browser-tools/node_modules/playwright; Chrome C:/Program Files/Google/Chrome/Application/chrome.exe; flags --enable-webgl --use-angle=swiftshader --enable-unsafe-swiftshader.

## 남은 순서

1. visual_audit의 전체 support교정완료를 기다려 latest71ref 확정. catalog_agent쓰기풀기.
2. Registry current assetrefs/FBXpaths/tri/quantity/한국어이름을 최신catalog에서 생성, buildId workplaces-v005(이미있으면더높은고유버전). source SHA snapshot.
3. Unity -batchmode -quit -nographics -projectPath ... -executeMethod WorkplaceBuild.Build -buildTarget WebGL -workplaceBuildId workplaces-v005 -logFile outputs/workplaces-v005-unity.log. exec가 sessionID반환하면 완료전종속호출않기. 실제success후receiver dist최신을site/receiver로복사.
4. root HTTP71각방 실제진입/스냅샷(최종build만pass), native실행: Unity -batchmode -nographics (quit없이) -executeMethod OfficeEditorPlay.RunWorkplaces. 이기존runner는 실제 PlayMode로71장면순회/mesh·collider·mat검사, nographics 시각은별도HTTP검증.
5. direct_protocol 최종build office+React 전체테스트 실제키보드char/포인터/drag/키보드대체/오류반복/출력closepause/reset/end/종료재전송/replay/강제중단보존. 수정필요하면 새고유build.
6. catalog_handover 실제evidence로 최신revision 사용이력·build_links·executionchecks·전공간상태표/모든모델full후보/실제사용문서 갱신. 검증없는ready금지.
7. 최종 WebGL ZIP site/전체 +manifest schema3 build/assets/palettes +BUILD.md/README.md. unity/webgl/packages/<build>.zip 새파일. 소스/Unity프로젝트는ZIP에넣지않음. 해시/압축구조/HTTP URL검증.
8. 실제실행과정/기록·모델·71공간·체험1개를구분해보고, 다른551초안·실제모바일/하드웨어GPU/SafariFirefox/외부HTTPS 미검증명시. 완료전AGENTS검토항목.

## 이후 추가 확정/대기

- visual comprehensive pass 새prop40+room65제작 게시(현재455모델버전). 최신803placements에서472바닥검사 중1실패(67앞case가선반높이로잘못올라감), microscopeknob/fieldsensorprobe 분리 연결을 마지막함께교정중. 이완료/전수검사최종선언전build금지. source40props+65room의새versions는현재원장에서읽고반드시oldbaseLAYOUTS로돌아가지않기.
- root actualimport검토에서 shared palette.meta nPOTScale1(자동축소)을발견. WorkplaceBuild.Prepare에 NPOTNone,WebGLRGBA32/uncompressed/max4096/Point/NoMip +sourcePNG와Unityimported.GetPixels32전체해시비교+2508size검증을추가. 실행전이므로최종빌드에서 palette-import.json 실제pass필요. previous_imported_width/height도기록. 최종RuntimeExplorer.textureWidth/Height,Direct.paletteWidth/Height로실제값검사.
- Direct 최종수정: focusedEsc OnGUI단일키처리,sorting키와UI키소유분리,submit성공시disabledtextfieldfocus해제(Ppause보장),Tab/ShiftTab입력+버튼통합탐색,키반복한번만처리,진한한글입력잉크. agent Direct 최신hash는후속메시지/실제파일읽기. Protocol81b473...동결. 실제v00317pass+3UI실패(수정완료)등보고서보존. Unicode CDPchar keypress가실제IME경로로동작,insertText는Unity입력못들어가는자동화방식제약(근거보존).
- Receiver최신 clean dist-v006(offline성공),favicon수정/suspendListening+listen late-listener시험API포함. 최종site/receiver에이폴더복사.
- catalog_handover는모든sharedcatalog쓰기정지중. physical완료후풀어주기. 새candidatepackagev004로v003계획+실제배치공간union(예비67common/181noncommon/14inventoryOnly,91추가pair)을보존해만들예정. 원래55/17baseline별도. 변형oldsceneusage는removed최신revisionappend,legacyOfficeAssistant.unity30소스배치보존,최종build803vs프로젝트833scope구분.
- v004buildsuccess오류0경고0. 직접소스가중간에바뀐legacy중간본. 최종v005예정. v003C#before/afterhash일치확인됨. v005sourcefreeze후증거새로. rootWorkspaceExplorer에는선택물건한글이름registry.assets추가,headlessScreen0guard추가;최종registry에assets배열필수.

- RootQA actualGUI driver 마지막은 hostPTY28605, 현재v004의2/71/4공간실제pass, pause/inputlock/resume/touch공통pass; farjump는스크롤바thumb실제드래그로해결. 함수store roomQAProgramV4. 이세션에 init최종build+rooms71명령을보내재사용가능,스냅샷/PNG매번실제생성. wheel단일event는20px이라과거30회반복드라이버가끝까지못갔던것이지공간로더문제아님.
- root importer추가CPU 픽셀검증 구현이완료됐으나 아직새Unitybuild로실행전: canonicalPNG와imported.GetPixels32전체RGBA해시비교,2508sizeassert,NPOTNone+WebGLRGBA32/noMip/Point,검증후isReadablefalse. NativePlayrunner도texture2508assert추가.
- OfficeDirect 최신32fe6df...freeze(단일키소유/UnifiedTab/submitfocus/단일physicalEnter/darktext);Protocol81b473... . Agent실제최종regression은미실행이며v003실패3건을소스에서보완한상태. Receiver dist-v006완료+licenses/포함(전체copy필수).

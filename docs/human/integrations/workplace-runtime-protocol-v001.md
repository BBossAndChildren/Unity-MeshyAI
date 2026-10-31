# 직접 작업 체험의 Unity–React 수신 예제 v001

규칙의 원본은 [AGENTS.md](../../../AGENTS.md)의 공통 응답 v001이다. 이 문서는 실제 구현한 office v002와 수신 예제의 연결·제한을 설명한다. 다른 공간·직업 초안을 구현 완료로 뜻하지 않는다. 실제 통합 pass는 빌드별 실행 근거에서 확인한다.

## 실행 가능한 예제

소스는 `web/career-receiver/`다. 이미 설치된 `web/scene-browser/node_modules`를 재사용해 네트워크 호출 없이 번들한다.

```powershell
cd web/career-receiver
node ../scene-browser/node_modules/vite/bin/vite.js build --outDir dist-v006
```

성공한 dist-v006 전체를 WebGL 출력 폴더의 `receiver/`에 복사한다. 같은 HTTP 서버에서 `<build>/receiver/`를 열면 `../index.html`의 실제 Unity를 iframe으로 연다. React와 런타임은 최종 번들에 포함하며 외부 CDN은 필요 없다. Unity 프로젝트·Blender 원본은 전달 WebGL ZIP에 넣지 않는다.

수신 예제의 체험 시작은 PAN-001의 기존 사무보조원 시나리오 v002만 요청한다. 다른 방에서 임의로 첫 초안을 시작하지 않는다. 화면의 체험 종료는 응답을 기다려 process/result/context와 원본 이력을 저장하며, 응답 보존 뒤에만 Unity iframe 닫기 버튼을 활성화한다. 게임 안의 명시적 종료 버튼으로 발행된 유효한 matching experience.ended도 보존·표시한다.

30초 안에 응답을 확인하지 못하면 DELIVERY_UNCONFIRMED로 표시하며 성공·중단 결과를 만들어 넣지 않는다. 원본 requestId를 보존해 미확인 요청 같은 ID로 재전송 버튼을 제공한다. 브라우저 새로고침 후 이전 nonterminal 수신 기록이 있으면 SESSION_INTERRUPTED / initiatedBy unknown / unconfirmed로 안내한다. 이는 사용자 포기 확정이나 이전 게임 진행의 자동 복원이 아니다.

## 호출과 전달

Unity 서비스 GameObject 이름은 CareerProtocol이며 `ReceiveControl(string json)`과 `Replay(string unused)`를 노출한다. Unity 인스턴스는 템플릿의 `window.officeUnity`다. 시작 호출 예시는 실제 이벤트 증거가 아닌 호출 형식이다.

```json
{"schemaVersion":1,"protocol":"career-experience","requestId":"caller-generated-unique-request","action":"start_experience","sessionId":"caller-session","experienceId":"caller-new-experience","roomId":"PAN-001","scenarioId":"career-net-253-office-documents","scenarioVersion":"v002"}
```

종료는 같은 sessionId·experienceId·roomId에 새 requestId, action=end_experience, reason=USER_REQUESTED_END를 보낸다. 완료·중단 여부는 현재 실제 업무 상태가 결정한다. 재전송은 같은 요청 내용을 같은 requestId로 보낸다. 새 실행은 새 experienceId다. 내부 Reset은 같은 experience에서 새 scenarioRunId를 만들고 과거 run을 previousRuns에 분리한다.

동일 페이지는 career-experience:event CustomEvent.detail, iframe은 `{channel:"career-experience",event:<원본>}`다. 샘플은 같은 HTTP 출처의 부모를 explicit targetOrigin으로 설정한다. 수신은 origin·source 창·schemaVersion·protocol·room/session/experience·eventId/sequence를 확인한다. 배포에서 다른 출처를 쓰려면 송신 부모 origin과 수신 허용 origin을 명시적으로 구성해야 하며 wildcard 전달을 사용하지 않는다.

어댑터는 eventId로 중복을 제거하고 sequence로 정렬한다. 앞 순번 1부터의 누락도 감지하며 Replay로 원본 이력을 요청할 수 있다. 숫자 간격을 가짜 이벤트로 채우지 않는다. 종료 data.events의 원본들도 같은 ID Map에 병합하며 횟수를 다시 증가시키지 않는다. 업무 과정의 집계 권한은 Unity에만 있다.

사무실 작업 화면의 닫기·Esc는 출력을 계속한다. 공간 탐색으로 PAN-001을 떠나면 같은 office run·출력 경과 시간을 보존하고 타이머를 일시정지하며, 돌아오면 그 경과 시간부터 재개한다. 명시적 일시정지도 타이머를 멈춘다. 이 세 동작은 종료 응답을 만들지 않으며, 사용자 종료·초기화만 별도 terminal/과거 run 기록을 남긴다. 이 정책은 v006의 실제 화면 닫기 출력과 2.8초 공간 이탈 검수에서 각각 확인했다.

## 보존과 검증

Unity는 고유 원장을 메모리에 보존한다. JS는 원본 이벤트를 `career-experience:events`, 마지막 실제 상태를 `career-experience:checkpoint`에 저장한다. pagehide가 관측되면 종료를 확정하지 않은 채 `career-experience:interruption` 메타데이터에 unknown/unconfirmed를 남긴다. React의 수신 기록은 `career-experience:receiver`에 따로 보존한다. 강제 프로세스 종료에서는 마지막 pagehide·전달이 보장되지 않으므로 마지막 보존 시점 이후는 미확인이다.

브라우저 진단은 `window.careerReceiverState`, `window.careerReceiverRecovered`, Unity iframe의 `window.careerExperienceEvents`/`careerExperienceCheckpoint`에서 읽을 수 있다. 이 진단값을 실제 업무 조작의 대체 입력으로 쓰지 않는다. 실제 조작은 3D 물건·텍스트 필드·드래그/동등 대체 조작으로 검수한다.

[수신 어댑터 경계 검사](../../machine/evidence/career-receiver-adapter-v001.json)는 Node의 mocked transport 검사이며 Unity·React 화면 실행 pass가 아니다. 중복·앞 순번 누락·잘못된 origin/source·응답 시간 초과·같은 ID 재전송·게임 내 종료 응답을 확인했다. 실제 Unity → React 통합 실행·브라우저 강제 종료·모바일 기기 등은 빌드별 evidence가 있을 때만 통과로 보고한다.


## workplaces-v006 실제 연동 검수

[최종 HTTP 근거](../../machine/evidence/workplaces-v006/office-direct-http-acceptance.json)는 제품 오류0, 실제 통과19사례, 보존된 자동화 관찰3건을 분리한다. Unity 원본 원장에서 횟수를 검산했고 같은 requestId의 시작·종료와 Replay가 같은 원본 eventId/sequence를 유지했다. 30초 리스너 미수신은 ended:null/DELIVERY_UNCONFIRMED로 남았으며, 재전송 UI가 같은 requestId의 원본 종료 응답을 복구했다. 게임 안 종료도 프론트 pending 요청 없이 matching receipt를 보존했다. 실제 새로고침은 기본 PAN-002 탐색 장면으로 시작하며, 수신 기록의 unknown/unconfirmed를 보존한다. 명시적 Start가 office 시나리오를 준비하고 experience.started로 응답한 뒤 officeState가 사용 가능하다.

구현 범위는 office v002 기본2부·변경3부·인계와 공통v001 수신이다. EX-010 선택 이력 복원·나머지551초안·전체10특수유형은 완료 범위가 아니다. 네이티브 Editor 업무 GUI와 실제 모바일·다른 브라우저는 별도 미검증이며, 실제 Unity native 장면 검수와 WebGL 업무 검수를 구별한다.

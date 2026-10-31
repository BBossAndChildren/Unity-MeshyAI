# 사무보조원 직접 작업형 v002

이 문서는 기존 `career-net-253-office-documents` v001을 같은 ID의 v002로 보완한 구현 명세다. [기계용 개정 목록](../../machine/catalog/career-experience-scenarios-v003.json)은 이 한 시나리오만 담는 v003 amendment이며, 552개 전체 목록의 대체본이나 다른 551개 초안·미선택 주제의 자동 승인이 아니다. 원래 pending_user_approval 검토 상태를 보존한다. 사용자 전체 공간 제작 위임에 포함된 기존 대표 체험의 직접 작업형 구현 범위다.

현재 직접 작업과 Unity–React 연동은 workplaces-v006의 실제 HTTP WebGL에서 검수했다. 네이티브 Unity Editor는 장면 로드·기하·콜라이더·텍스처 검수를 통과했으며, 직접 업무 GUI 입력은 이 근거에서 미검증이다. 과거 [office-assistant-v005 검수](../builds/office-assistant-v005.md)를 새 동작의 실행 pass로 승계하지 않는다. 기존 OfficeExperience.cs·CareerRules.cs와 기존 모델·v005 빌드를 보존하고 OfficeDirectExperience.cs·CareerProtocol.cs를 추가했다.

## 업무와 물건

한 미션은 기존 모니터 AST-005 v001, 복합기 AST-009 v001, 수납장 AST-015 v001의 세 물건만 조작한다. 문서·용지·분류함·인계 카드는 이 물건에 귀속된 UI다. NPC·네 번째 3D 조작 물건·별도 재질 이미지를 추가하지 않는다. 기준 공간은 공용 업무 사무실 PRM-001 v001 / PAN-001 v001 / office-shared-work v001이다. 각 모델의 전체 공간 후보·실제 배치 수량은 해당 에셋 명세와 원장 asset-usages.json·scene-assemblies.json에서 조회한다.

1. 모니터에서 자료·회의일, 부수, 보관처를 질문하고 요약 확인을 받는다.
2. 요청 원문과 실제 문서 필드를 비교한다. 제목·회의일을 텍스트 필드에 직접 입력하고 저장한다. 초기 날짜는 11월 1일, 요청 날짜는 11월 2일이다. 틀린 날짜 선택 버튼으로 편집을 대체하지 않는다.
3. 복합기 패널에서 자료·최신 저장 revision·실제 부수 입력을 확인해 출력한다. 기본 2부, 변경 연습은 요청 r2의 3부다. 2.5 활성 초 동안 진행률에 맞춰 개별 용지가 나오며, 완료 후 2장 또는 3장의 서로 다른 가장자리·용지 번호를 실제 부수대로 표시한다. 실제 완료 시 한 묶음으로 확정한다.
4. 수납장에서 문서 묶음을 실제 분류함으로 드래그한다. 묶음 선택 후 목적지 선택, Enter/Space·방향키 조작도 동일 File 명령을 호출한다. 오분류는 확정하지 않고 원위치·오류 안내를 보인다. 왼쪽의 세 분류함에는 보관 전 원본 위치의 묶음이 보이고, 성공 후에는 실제 보관처 칸 안으로 묶음이 이동해 남는다.
5. 보관 후 같은 수납장에서 제목·회의일·부수·보관처를 직접 입력하고 인계 요약을 보낸다. 상대 확인과 실제 출력·보관 조건까지 맞아야 시나리오 완료다.

문서 제목·날짜·부수·대화·정답은 가상 연습 데이터이며 실제 업무 규정·직업 적성 판정이 아니다. 기존 원문 업무와 대인관계능력 연결은 이전 명세의 출처를 유지한다. EX-010 문서 이력 복원 연습은 계속 미구현이다.

## 선택·확대·보존

실제 메시 콜라이더 선택과 8px 초과 카메라 드래그를 구별한다. 기본 0.45초 smoothstep 확대·복귀 동안 입력을 잠그며 물건의 실제 renderer bounds로 거리를 정한다. 전환 시간은 `Assets/Scenes/OfficeAssistantDirect.unity / OfficeExperience / OfficeDirectExperience / Transition Seconds`의 직렬화된 Inspector 데이터로 설정한다. 기본 0.45초, 유효하지 않은 값은 0.45초로 대체하고 0.05~5초 범위로 제한한다. 시작 화면·일시정지의 `화면 움직임 줄이기: 켜짐/꺼짐` 또는 reducedMotion Inspector 데이터가 켜짐이면 즉시 전환하며 같은 run의 공간 이동에도 설정을 유지한다. 배경 메시를 복제·변색하지 않고 기존 renderer 표시 상태를 저장·복원하며 전용 지우기 카메라로 전체 프레임을 지운다.

닫기·Esc는 종료·초기화가 아니다. 저장한 카메라 위치·회전·FOV·viewport와 배경 표시를 복원한다. 미저장 문서 초안, 출력 설정, 분류·인계 진행을 유지한다. 출력은 닫혀도 계속되며 일시정지는 시간을 멈춘다. 출력 중 설정·중복 실행과 완료된 동일 저장·출력의 재제출은 잠근다. 텍스트 입력 중 P/R·숫자·화살표를 전역 단축키로 해석하지 않는다. 취소 터치·다중 터치·초점 상실·Esc/P는 임시 제스처와 GUI hotControl을 취소하고 드롭을 발생시키지 않는다.

작업 화면만 닫고 PAN-001 사무실에 머무르면 시작한 출력은 계속된다. 다른 공간으로 이동하면 사무실 run과 이미 경과한 출력 시간을 메모리에 보존하고 출력 타이머를 일시정지한다. PAN-001로 돌아오면 같은 run에서 보존한 경과 시간부터 출력을 다시 진행한다. 같은 세션에서 돌아오면 저장하지 않은 필드·설정·카메라 방향을 복원한다. 브라우저 새로고침 후에는 플레이 가능한 상태를 자동 복원하지 않는다. 수신 원본 이력·마지막 checkpoint만 남기고 종료 미확인은 SESSION_INTERRUPTED / initiatedBy unknown으로 구분한다.

## 원장·공통 응답

[AGENTS.md](../../../AGENTS.md)의 v001 통신 규격을 적용한다. `schemaVersion:1`, `protocol:career-experience`, roomId=sceneId=PAN-001, scenarioId=career-net-253-office-documents, scenarioVersion=v002다. catalog schema_version은 계속 3이다. 사무실 밖의 미확정 체험을 시나리오 실행으로 만들지 않는다. 사무실 leave/enter 이벤트의 data에는 실제 탐색 목적지·이전 방을 구분한다.

CareerProtocol은 장면 사이에 유지되는 단일 서비스다. 실제 상태 확정 뒤 고유 eventId·session 순번으로 발행한 이력에서 attempt/retry/mistake/repeatedMistake/navigationBack/backtrack/help·활성 시간을 조회한다. 저장·확인·인쇄·보관·인계 실제 제출만 attempt이며 필드 타이핑과 정상 복귀·변경 요청은 실수가 아니다. 같은 failureId를 한 번만 세고, 같은 step/object/work item/request revision/reason 조합의 두 번째 고유 오류부터 repeatedMistake다. 재시도는 같은 요청 아래 직전 실패 뒤 실제 새 제출에서만 센다.

사용자 종료는 시작 전 USER_EXITED_BEFORE_START와 업무 도중 USER_ABORTED를 구분한다. 종료·초기화 자체는 실수·retry를 늘리지 않는다. 마지막 단계·물건·상태·완료/남은 업무·진행 중 출력 job과 완료한 partialResults를 보존한다. 인계 완료 뒤 종료는 completed를 유지한다. Reset은 과거 run을 보존한 뒤 새 run을 만들고 기존 출력 시간·상태를 초기화한다. Ended 상태는 Tick을 막아 늦은 완료가 종료 결과를 바꾸지 못한다.

같은 requestId는 동일 원본 응답을 재전송한다. 이미 종료된 experienceId에 새 종료 requestId를 보내면 ALREADY_ENDED 제어 오류와 원본 종료 eventId를 안내한다. 제어 오류는 업무 실수 원장에 넣지 않는다. `Replay`는 원본 JSON을 다시 보내며 새 이벤트·횟수를 만들지 않는다. 종료 data.events는 부모 자신을 제외한 원본 이력, data.previousRuns는 초기화한 과거 run의 별도 요약이다.

## 검증 경계와 사용량

새 Unity 직접 작업·React 종료 수신의 실제 검증은 빌드별 evidence에 기록한다. 이 문서는 실행 pass가 아니다. Node의 수신 어댑터 행동 검사는 [별도 근거](../../machine/evidence/career-receiver-adapter-v001.json)이며 실제 Unity 통합 검증을 대신하지 않는다.

이번 직접 작업형 전환 Meshy·이미지 생성 호출 0, 크레딧 0. 토큰·에셋별 과금 배분은 도구가 제공하지 않아 미측정이며 추정값을 실측으로 넣지 않았다.

## v003 중간 빌드의 실제 검수

[실제 HTTP 검수 기록](../../machine/evidence/workplaces-v003/office-direct-http-acceptance.json)과 원본 과정 이벤트는 v003에만 귀속된다. 실제 Unicode keypress 문서 입력, 잘못된 날짜·부수·분류·인계와 수정, 2부 완료, 변경 요청 재확인·3부 드래그 보관, 반복 오류/도움 완료 해석, React 종료 요약·재수신 중복 방지, 시작 전 종료·인쇄 중 부분 결과 종료·늦은 완료 차단, 인쇄 중 초기화·과거 run 보존, 재로딩의 unknown 중단 보존을 실행했다.

세 UI 문제가 발견되어 새 소스에서 수정했다: 입력 필드 안 Esc 미복귀, 분류 Enter가 이전 닫기 action까지 실행, 출력 제출 뒤 비활성 필드 초점이 P를 차단. 이 중간 빌드는 전체 통과가 아니며, 수정한 최종 빌드에서 다시 검수해야 한다. CDP insertText가 Unity 키보드 이벤트를 생성하지 않는 자동화 입력 방식 한계와 Node 검수 식의 window 오참조는 제품 오류와 별도로 구분했다. 실제 Unicode char keypress와 수정한 검수 식으로 관련 업무 동작을 확인했다.


v005의 900×600 실제 화면은 필드 대비·배치가 읽히지만, 중첩 GUILayout의 화면 좌표가 축척을 누락해 키보드 Tab 필터가 필드를 놓치는 문제가 발견됐다. 새 소스는 논리 전체 좌표에 루트 축척을 한 번 적용하며 다음 빌드에서 크고 작은 화면 모두 다시 검수한다.


## workplaces-v006 최종 검수

[실제 최종 검수 원본](../../machine/evidence/workplaces-v006/office-direct-http-acceptance.json)의 집계는 pass_verified_scope, 실제 통과 사례 19개, 제품 오류 0개, 콘솔·리소스 오류 0개다. 로딩 준비 전 officeState 접근, 이전 초점 위치에 대한 첫 Tab 가정, 기본 PAN-002 탐색 시작 전 officeState 대기의 자동화 관찰 3건을 삭제하지 않고 harness_observation과 해당 수정 후 통과 사례를 함께 남겼다. 모든 raw case가 통과했다고 표현하지 않는다. v003·v005의 제품 실패 기록을 그대로 보존했고 최종 pass를 그 빌드에서 승계하지 않았다.

900×600과 1440×1100에서 실제 한글 keypress·Tab/ShiftTab·Enter 저장, 입력 중 P/R/숫자 단축키 차단, 보존 초안과 원래 카메라/FOV/viewport/30개 렌더러 복귀를 확인했다. 기본 0.45초의 focusing→working과 움직임 줄이기의 즉시 전환, 설정의 공간 이동 보존도 실행했다. 2부·3부는 서로 다른 용지 가장자리·번호로 보이고 보관 묶음은 실제 회의자료 칸 안에 남는다. 마우스 드래그, 키보드, 브라우저 터치 이벤트의 동일 보관 명령과 취소·다중 터치·완료 후 재열기를 확인했다.

원장은 최종 AST-020 v006 조립 revision5, OfficeAssistantDirect.unity의 모니터 AST-005-0·복합기 AST-009-0·수납장 AST-015-0과 연결했다. 모니터 AST-005-1은 배경이다. 실제 사용 수량 2/1/1은 asset-usages의 해당 세 사용 ID revision9를 참조하며 독립 원장을 만들지 않는다. 사무실 전체는 실제 4,308삼각형·30렌더러, 공용 재질1·텍스처1이며 WebGL GPU 텍스처 크기2508×2508을 확인했다.

종료 응답의 고유 시도·실수 횟수, 반복 오류/도움 평가, 요청 변경의 실수·되돌아감 비가산, 시작 전/인쇄 중/보관 후 종료 부분 결과, 출력 중 초기화의 과거 run과 늦은 완료 차단을 검수했다. 리스너 지연·원본 재수신·같은 ID 재요청·제어 오류, 실제30초 전달 미확인 후 같은 ID 재전송 UI, 게임 안 종료 수신, 잘못된 source 메시지 거부와 새로고침의 unknown/unconfirmed 기록도 확인했다.

구현·검수 범위는 기본2부와 필수 인계 EX-008, 첫 구현에서 필요한 변경 요청3부 EX-007이다. EX-010 이력 복원은 원본 v002에서도 optional_practice_not_required_for_first_implementation인 선택 연습이며 계속 미구현이다. 다른551개 직업 초안·모든10개 특수 상황을 구현 완료로 표시하지 않는다. 실제 모바일 기기·Firefox/Safari, 비기본 Inspector 전환 시간·OS 초점 상실, 네이티브 Editor 업무 GUI 입력은 이 WebGL 검수의 검증 범위가 아니다.

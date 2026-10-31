# 실시간 진행 전달의 실제 구현 범위

`interaction.progress`는 상태가 실제 달라진 경우 최대 200ms 간격(초당5회)으로 묶습니다. 오류·완료·중단·요청 변경 같은 상태 확정 이벤트는 이 제한으로 버리거나 합치지 않습니다.

빠른 편집 직후 닫기·제출·오류·요청 변경·종료 경계가 먼저 오면, 해당 비제한 전이 이벤트의 `data.coalescedProgress` 배열에 최신 불변 입력 스냅샷을 붙입니다. 배열 항목의 실제 키는 `stepId, objectId, workItemId, action, attemptId, requestRevision, documentRevision, input`입니다. `input`에는 `draftRevision, savedRevision, savedRequestRevision`과 작업별 실제 입력이 있습니다. 이 스냅샷을 새 플레이어 행동이나 추가 제출/실수/재시도로 세지 않습니다.

원본 eventId·sequence·occurredAt·본문은 재전송 때 유지합니다. React/백엔드는 원본을 보존하고 process를 범위별 최신 sequence로 대체합니다. 진행 스냅샷과 종료 data.events를 다시 합산하지 않습니다.

이 설명은 최종 소스의 전송 구현이며 모든 전문 업무·특수분기·실제 운영 백엔드 구현 완료를 뜻하지 않습니다. 전체562개 특수분기 항목 중554개는 명시적 미구현이며8개 요청변경 분기는 소스 작성/새 빌드별 검수 범위를 별도로 읽어야 합니다. 서버 소유권 lease·정산은 실제 서비스 계약이 없어 미검증입니다.

## 종료 뒤 원본과 최신 표시의 구분

기존 Unity 일부 경로에서 종료 뒤 pending 원본이 늦게 발행되는 알려진 소스 문제가 남습니다. 프론트와 예제 로컬 수신기는 해당 원본을 포렌식 이력으로 보존하되 닫힌 실행의 최신 종료 결과를 다시 pending으로 낮추지 않습니다. 종료가 순서 역전으로 늦게 도착해도 닫힌 스냅샷을 복구합니다. adapter-validation/의 근거는 Node 모의 전송·로컬 HTTP 수신기 검수이며 실제 Unity 원본 문제를 제거했다거나 운영 백엔드가 구현됐다고 보고하지 않습니다. 실제 외부 서버도 같은 종료 스냅샷 보존 계약을 구현해야 합니다.

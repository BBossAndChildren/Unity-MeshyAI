# 실시간 응답·방/직업 ID 전달 명세 v002

신규 실시간 요구의 명세 패키지이며 실행본/통신 완료 증거가 아닙니다. 기준 규칙은 AGENTS.md입니다.

1. career-integration-registry-v001.json의 rooms에서 정확한 roomId를 선택합니다. office가 아닌 PAN-001입니다.
2. scenarios에서 직업 ID/이름, 고정 시나리오 버전, 설계상 방을 조회합니다. sceneOptions가 있으면 선택 전에는 실행하지 않습니다.
3. runtimeBindings는 현재 소스에서 확인한 실행 설정입니다. 서로 다른 runtimeFamily가 한 빌드에 모두 들어있다고 가정하지 않습니다. 배포별 지원 조합을 검증하기 전 launchApproved는 false입니다.
4. 프론트는 매 시작마다 experienceId를 UUID 등으로 새로 생성합니다. 고정 경험 ID 목록은 없습니다. 같은 호출 재전송에는 requestId와 experienceId를 유지합니다.
5. 리스너 등록 → start_experience → experience.started → 실시간 행동 이벤트 → end_experience → experience.ended 저장 → 화면 제거 순서입니다.

JSON 파일의 schema_version:3은 저장소 문서 봉투입니다. *.example.json에서 실제 Unity로 보내는 값은 request 객체, 이벤트는 events 배열 안의 객체입니다. 통신 자체는 schemaVersion:1입니다.

실시간 process는 누적값이므로 합산하지 않습니다. 같은 범위의 최신 sequence 스냅샷으로 교체하고 원본 이벤트는 (sessionId,eventId) 키로 보존합니다. 순번은 세션 전체 기준입니다. 동일 방의 재실행·전체 초기화 run을 섞지 않습니다.

프린터 선택은 object.selected, 부수 오류는 interaction.validation_failed, 실제 재제출은 새 attemptId, 출력 완료는 interaction.completed입니다. 입력 중/출력 중에는 pending이며 인계까지 완료돼야 시나리오 완료입니다. interaction 평가와 scenario 평가를 분리합니다. 강제 브라우저 종료·누락을 중도 포기로 추정하지 않습니다.

React → 백엔드 저장 API/인증/ACK는 백엔드 팀에서 정합니다. 원본 이벤트와 최신 스냅샷을 함께 저장하고 재전송을 허용하세요. 서버 저장 ACK와 Unity 상태 확정은 서로 다릅니다. 실시간 이벤트를 놓쳐도 종료 요약을 읽을 수 있어야 하며 data.eventsComplete로 원장 전량 여부를 확인합니다.

검증 범위: JSON 파싱, 고정 ID/방 연결·중복·출처 해시, ZIP 바이트 검증. 신규 v002 요구의 Unity/React/백엔드 실시간 왕복은 미검증입니다. 기존 구현 상태는 원본 catalog의 기록을 보존하며 승격하지 않습니다.

# 직업체험 프론트·백엔드 목록 전달 v003

이 ZIP은 **실행 WebGL이 아닌 별도 ID 목록·연동 코드·계약 자료**입니다. Unity 프로젝트·모델 원본·실행 바이너리는 포함하지 않습니다.

- 테스트 보기: [로컬 HTTP 테스트 화면](http://127.0.0.1:8212/career-suite-test-v006/) — 실행 중인 로컬 서버 기준이며 외부 배포 URL은 아닙니다.
- 실제 연동 실행물: 별도 career-suite-integration-v002-package-v003.zip.
- 고정 목록: ids/room-scenario-ids.json 및 CSV(UTF-8 BOM), 공간71·직업/시나리오552·방별 조합555. 같은 시나리오라도 방과 버전을 함께 대조합니다.
- 지원 허용 목록: builds/의 두 최종 supported-manifest.json을 기준으로 buildId+roomId+scenarioId+scenarioVersion을 확인합니다. 알 수 없는 조합을 첫 항목으로 대체하지 않습니다.

프론트는 frontend/Experience.jsx, client.js/client.d.ts, backend.js/backend.d.ts와 react-example.jsx를 사용합니다. siteUrl은 실제 운영 WebGL index.html URL, manifest는 그 빌드 지원 목록을 전달합니다. 리스너·WebGL ready 확인 뒤 명시적 시작 동작에서 client.start(selection)를 호출합니다. 새 체험마다 새 experienceId, 내부 초기화는 새 scenarioRunId입니다. client.end 후 실제 종료 원본을 보존하고 화면을 제거합니다. 재전송은 client.retry(requestId)로 같은 요청을 사용합니다.

frontend/compiled/는 별도 WebGL ZIP의 site/frontend/에 놓고 사용하는 React 예제입니다. 목록 ZIP만으로 Unity 게임이 실행되지 않습니다. 별도 실행물에는 해당 프론트가 이미 들어 있을 수 있습니다. 실제서비스는 기존 React 앱에 소스 컴포넌트를 연결하세요. 로컬 수신기는 frontend/server.mjs이며 실서비스 인증/정산 서버가 아닙니다.

examples/의 start/end는 가상 요청 예시이며 원본 이벤트가 아닙니다. contracts/의 이벤트·정산 JSON도 규격 fixture입니다. 실제 최종 빌드의 원본 이벤트는 actual/에 별도 보존하고 그 출처·범위를 manifest에 기록합니다. 모의 예시나 로컬 ACK를 실제 운영 서버 통합 성공으로 보고하지 않습니다.

process는 누적 스냅샷이며 더하지 않습니다. 원본은 eventId로 중복 제거하고 sequence별 최신 범위를 표시합니다. 종료 응답의 data.events와 실시간 이벤트를 다시 합산하지 않습니다. 종료 미수신은 pending_reconciliation이며 실제 서버 소유권/lease/fence/명시적 새 시작 검증 없이 React가 중단을 확정하지 않습니다. 자세한 정책은 backend/README.md와 contracts/CONTRACT-SNAPSHOT.md를 참고하세요.

이 목록에 포함된 스타터의 플레이 완료와 원래 전문 업무·필수 특수분기 구현 완료는 다릅니다. 전체 미완료 상태는 ids/career-full-targets-v003.json과 docs/full-target-status-v003.md에 유지합니다. 실제 외부 백엔드 통합은 미검증입니다.

실제 진행200ms묶음과 경계 이벤트의 불변 입력 보존은 docs/progress-coalescing-v002.md를 참고하세요. 전체562개 특수분기 항목 중554개 미구현을 포함한 원래 업무의 미완료를 숨기지 않습니다.

최종 검수 범위: 테스트용은71개 공간의 정확한 시작·세 실제 물건 바인딩·업무 시작 전 종료를 확인했습니다. 추출한 실제 연동 ZIP은 외부 React 버튼→Unity→실시간5이벤트→로컬 fsync ACK5, 동일 종료 재전송, 잘못된 버전 거부를 확인했습니다. 이는 모든555개 업무 전체 완료·오류·특수분기·실제 운영 백엔드 검수가 아닙니다. 정상 업무 완료 원본은 earlier-builds의 실제 과거 사례이며 최종본으로 승계하지 않습니다.

최종 정상 업무 UI의 실제 원본도 포함합니다. PAN01910001v003은 출력 전 준비·검수·인계3단계(시도3/실수0/재시도0), PAN060431v003은 문서·3회실제드래그·계기 조절·오류 후복구(시도4/실수1/재시도1)입니다. 실제 프린터 작동은 제공하지 않으며 얇은 케이블 트레이 중앙 포인터 선택은 실패하여 키보드2 대체를 사용했습니다. 세부 한계는 docs/runtime-review-v001.md를 확인하세요.

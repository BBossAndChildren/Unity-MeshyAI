# Career Suite 두 출력의 브리지 v002

동일 Unity 프로젝트의 테스트 출력과 외부 React 연동 출력은 `web/career-preview/v002/client.js`의 시작·종료·이벤트 경로를 공유합니다. 테스트 템플릿은 `CareerSuiteTest`, 실제 연동 템플릿은 `CareerSuiteIntegration`입니다. 공간 우선 선택·전체 대상 검색·같은 공간의 시나리오 선택은 테스트 화면 또는 외부 React 부모에만 있습니다. 실제 연동 Unity에는 선택 목록과 개발 로그를 표시하지 않습니다.

기준 규칙은 [저장소 AGENTS.md](../../../AGENTS.md)의 런타임 v001/v002/v003 절이며, 이 문서는 구현 설명입니다. 전체 대상과 미구현·미검증 상태는 [전체 대상 목록](../../machine/catalog/career-full-targets-v001.json)을 조회합니다. 지원 조합은 각 출력의 `supported-manifest.json`이며 전체 설계 레지스트리와 구별합니다.

시작은 `roomId + scenarioId + scenarioVersion`을 명시하고 실제 `buildId` 지원 조합과 대조합니다. React는 source/origin/버전/실행 귀속을 검사하고 누적 process를 범위별 최신 sequence로 대체합니다. 원본은 별도로 보존하며 재전송·종료 data.events를 중복 합산하지 않습니다. ID 내용 충돌·sequence 충돌은 격리 기록에 남습니다. 이전 실행의 늦은 원본은 해당 실행에 저장하고 새 실행을 변경하지 않습니다.

5초 동안 종료 응답이 없으면 `pending_reconciliation`이며, 사용자 중단·실수·실패 결과를 생성하지 않습니다. `backend.js`는 실제 서비스가 제공한 endpoint와 인증만 사용합니다. 소유자 판정·lease 갱신·명시적 새 시작의 admission·원자적 fence·늦은 종료 검증은 백엔드 구현이 필요합니다. 인증된 `experience.reconciled` 응답은 resolutionId/revision으로 보존하고 실제 Unity 종료 원본과 구별합니다. 실서비스 주소와 인증 계약이 제공되지 않아 해당 서버 통합은 미검증입니다.

실행 가능한 React 예제는 `web/career-preview/v002/dist/integration-example.html`과 그 assets입니다. 원본 JSX·컴포넌트·타입·상세 호출 및 패키징 안내는 [브리지 README](../../../web/career-preview/v002/README.md)를 따릅니다. 로컬 수신기는 `server.mjs`이며 fsync JSONL ACK·중복 제거·충돌 격리를 제공합니다. 실제 서비스의 인증·정산 서버를 대신하지 않습니다.

이번 Node 어댑터 실행은 [11개 확인 항목](../../machine/evidence/career-suite-bridge-v002/adapter-execution.json), 실제 로컬 HTTP 수신기는 [ACK·중복·409 확인](../../machine/evidence/career-suite-bridge-v002/local-receiver-http.json)을 기록했습니다. 전자는 모의 Unity 전송이며 후자는 명시적 fixture 이벤트입니다. 이 증거를 실제 Unity·HTTP WebGL·외부 React·실서비스 전체 왕복 pass로 승계하지 않습니다. 실제 빌드의 브라우저 검수는 각 빌드의 별도 증거를 확인해야 합니다.

중간 출력 `career-suite-integration-v001`에서는 실제 Chrome의 React 번들→production iframe→Unity 시작·실시간 이벤트→종료→로컬 fsync ACK를 확인했습니다. 대상은 PAN-050 / career-net-359-experience @ v002이며, 동일 시작 요청의 실제 Unity 재전송이 같은 원본을 반환하고 잘못된 방의 종료는 현재 체험을 변경하지 않았습니다. [원본 5개 이벤트·ACK·검사 내용](../../machine/evidence/career-suite-integration-v001/react-smoke/actual-react-iframe.json)과 [실제 React 결과 화면](../../machine/evidence/career-suite-integration-v001/react-smoke/actual-react-end-full.png)을 보존했습니다. 이는 시작 전 종료와 통신 경로의 증거이며 정상 업무 전체 완료·모든 시나리오·다른 빌드·실서비스 백엔드의 pass가 아닙니다.

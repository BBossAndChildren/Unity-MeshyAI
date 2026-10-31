# 프론트·백엔드 목록 전달 v003

[테스트 화면](http://127.0.0.1:8212/career-suite-test-v006/)은 현재 로컬 HTTP 서버에서 실행합니다. 외부 배포 URL은 아닙니다.

최종 전달 ZIP은 두 개입니다.

|구분|파일|바이트|SHA-256|
|---|---|---:|---|
|실제 연동용 WebGL|[career-suite-integration-v002-package-v003.zip](../../../unity/webgl/packages/career-suite-integration-v002-package-v003.zip)|31,338,799|5198067e65b21e5853657875ca02b7e7907bb7f95ccf5b4a8200c3841eb3e2a4|
|별도 프론트·백엔드 목록/연동 자료|[career-integration-listing-v003.zip](../../../unity/webgl/packages/career-integration-listing-v003.zip)|923,372|4143f706f45e96c8395c7d51b156f997bc9fbb37ba4bbd4302eb1a1c8fb73a92|

목록 ZIP은 115개 파일이며 Unity 프로젝트·모델 원본·WebGL 실행 바이너리는 포함하지 않습니다. 실행 게임은 첫 번째 ZIP의 site/를 HTTP 서버에서 제공합니다. source/client/backend 타입·React 컴포넌트·로컬 수신기는 목록 ZIP의 frontend/에 있고 실제 API 주소·인증·소유권 서버는 서비스에서 연결해야 합니다.

71개 공간, 552개 직업/시나리오 ID, 555개 방별 고정 조합의 CSV·JSON과 두 최종 supported-manifest를 포함했습니다. 방+시나리오+버전과 실제 buildId를 모두 대조합니다. currentBuildInclusion:false 같은 원본 자료 값은 작성 당시 미빌드 상태이며 최종 포함 여부는 각 빌드 지원 manifest를 기준으로 합니다.

규격은 catalog schema_version3 / Unity 봉투 schemaVersion1 / 실시간 v002 / 종료 미수신 정산 v003입니다. AGENTS.md의 정확한 기준 해시와 고정 스냅샷을 포함했고, 가상 규격 예시와 실제 실행 원본은 폴더로 구별했습니다. 실제 API URL·인증·CSRF/CORS·ACK·소유권 lease/fence/admission·원본 조회 정책이 미제공이므로 실제 운영 백엔드 통합은 미검증입니다.

실제 최종 검수는 71개 공간의 정확한 API 시작·실제 세 물건 바인딩·업무 시작 전 종료, 출력 전 준비 v003의 정상 UI3단계(시도3/실수0/재시도0), DB 관리 v003의 정상 UI3단계와 오류 복구(시도4/실수1/재시도1), 추출한 실제 연동 ZIP의 외부 React 버튼→Unity→5개 이벤트→로컬 fsync ACK5 및 종료 재전송·잘못된 버전 거부입니다. 모든555개 업무의 전체 UI·특수분기·모든 입력 방식 검수를 뜻하지 않습니다.

남은 범위는 명시적으로 유지합니다. 원래562개 특수분기 항목 중554개 미구현, 실제 3D 프린터 작동·출력 미구현, 일부 얇은 트레이 포인터 선택/카메라 보정 미검증, 기존 사무실 계열의 종료 뒤 원본 탐색 이벤트 문제가 있습니다. 프론트/로컬 수신기의 닫힌 스냅샷 보호는 원본 문제 제거와 구별합니다. 정상 업무 완료 과거 원본도 보존했지만 최종 빌드로 성공을 승계하지 않았습니다.

[ZIP 무결성·소스 정합 검토](../../machine/evidence/career-integration-listing-v003-zip-review.json)는 CRC와 모든 멤버 바이트, CSV/JSON/최종 두 manifest의555개 조합, 핵심 프론트6개 파일의 양쪽 출력/목록 일치를 확인했습니다. [최종 제한 검토](../../machine/evidence/career-full-v001/final-bounded-review.json)는 별도 저장소 증거입니다. [전체 목표·남은 업무](../jobs/career-full-implementation-v003.md)와 [427개 에셋의 전체 후보/최신 사용 조회](../assets/career-asset-reuse-report-v002.md)를 함께 읽으세요.

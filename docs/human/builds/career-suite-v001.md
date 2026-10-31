# 전체 직업 체험 전달 작업

2026-10-31 작업 기록. 테스트 결과는 career-suite-test-v006, 외부 연동 결과는 career-suite-integration-v002를 기준으로 합니다. 최종 패키지와 실제 검수 범위는 아래 전달 기록에 정리했습니다.

## 범위

- 기존 71개 공간을 재사용합니다. 552개 직업 시나리오, 공간 대안을 포함한 555개 실행 조합을 대상으로 합니다.
- 추가 471개에는 직업별 가상 요청과 조작 물건 3개를 연결한 기본 미션을 작성했습니다. 입력 문서, 항목 이동, 조립 구성, 일정 배치, 계기 조절, 관찰, 상담, 타이밍, 사진 작업을 재사용합니다.
- 기본 미션이 실행된다는 사실은 원본 시나리오의 모든 특수 분기·실제 전문 장비·전문 업무를 완성했다는 뜻이 아닙니다. 각 시나리오의 남은 범위는 전체 대상 목록에 유지합니다.
- 성직자 체험은 개신교 예배실, 불교 법당, 천주교 성당을 각각 제공합니다. 군무원은 행정실과 생활관을 구분합니다.

## 전달 형태

테스트용은 71개 공간과 직업을 선택하고 체험하며 원본 과정 이벤트·종료 결과·로컬 저장 ACK를 확인하는 페이지입니다. 외부 연동용은 선택기를 내장하지 않고 외부 React 호스트가 고정 roomId/scenarioId/scenarioVersion 조합과 새 experienceId를 전달해 시작합니다.

두 결과물 모두 Unity 편집 프로젝트와 분리한 WebGL입니다. 사용자의 마지막 전달 요청에 따라 테스트는 실행 링크로 제공하고, ZIP은 실제 연동용 WebGL과 별도 프론트·백엔드 리스팅 두 개로 제공합니다. WebGL ZIP에는 site/, manifest.json, BUILD.md, README.md를 넣으며 모델 원본과 Unity 프로젝트를 포함하지 않습니다.

## 실행과 연동

ZIP을 새 폴더에 풀고 해당 폴더에서 다음을 실행합니다. Node.js가 설치된 환경을 사용합니다.

```powershell
node .\site\frontend\server.mjs --root .\site
```

기본 주소는 http://127.0.0.1:8194/ 입니다. 포트가 사용 중이면 PowerShell에서 `$env:PORT='8215'`처럼 다른 포트를 정한 뒤 실행합니다. index.html을 더블클릭하는 file:// 실행은 지원하지 않습니다.

테스트용은 루트 페이지를 사용합니다. 외부 연동용의 독립 React 예제는 `/frontend/integration-example.html`입니다. 실제 서비스에서는 `frontend/Experience.jsx`, `client.js`, `client.d.ts`, `backend.js`, `backend.d.ts`, `react-example.jsx`를 참고합니다. 빌드의 지원 조합은 `supported-manifest.json`을 기준으로 선택합니다.

원본 이벤트는 schemaVersion 1, protocol career-experience 봉투를 유지합니다. sequence는 session 전체에서 누적되며 process 카운트는 최신 스냅샷입니다. 카운트를 이벤트마다 더하지 않습니다. 종료 응답은 원본 이벤트 ID와 결과를 보존하고 저장 ACK와 구별합니다.

이 로컬 서버는 fsync JSONL 수신·중복 방지·ACK 확인용입니다. 실제 서비스의 인증, DB, 소유권 lease, authoritative reconciliation은 제공되지 않았으므로 실제 서비스 연동 완료를 주장하지 않습니다. 네트워크 단절·재개 정책은 별도 backend 어댑터에 연결해야 합니다.

## 보존과 검수

이전 모델·팔레트·빌드·ZIP은 보존했습니다. 모델 생성과 유료 Meshy·이미지 생성은 수행하지 않았으며 이번 Meshy 크레딧은 0입니다. 실제 토큰 사용량은 도구가 제공하지 않아 미측정입니다.

Unity 빌드, 엔진 규칙 검사, 실제 브라우저의 시작·바인딩·종료, 물건 3개의 전체 업무 수행, 외부 React 연결 검수는 각각 다른 증거로 기록합니다. 다른 빌드나 다른 시나리오의 성공을 전체 실행 성공으로 승계하지 않습니다.

- [전체 대상 및 남은 업무](../jobs/career-full-implementation-v003.md)
- [기존 체험 유지·변경 판단](../jobs/career-prior-workflow-audit-v001.md)
- [전체 에셋 후보·사용처 조회](../assets/career-asset-reuse-report-v002.md)
- [Unity 편집 프로젝트](../../../unity/projects/OfficeAssistant-v001/)

최종 빌드·ZIP 이름, 해시, 바이트 수와 검수 결과는 아래와 각 빌드 문서에 기록했습니다.

## 최종 전달 링크·무결성·실제 검수

- [테스트 화면 — 로컬 HTTP](http://127.0.0.1:8212/career-suite-test-v006/)
- [실제 연동 WebGL ZIP package-v003](../../../unity/webgl/packages/career-suite-integration-v002-package-v003.zip):31,338,799바이트, SHA-256 `5198067e65b21e5853657875ca02b7e7907bb7f95ccf5b4a8200c3841eb3e2a4`.
- [별도 프론트·백엔드 목록 ZIP v003](../../../unity/webgl/packages/career-integration-listing-v003.zip):923,372바이트, SHA-256 `4143f706f45e96c8395c7d51b156f997bc9fbb37ba4bbd4302eb1a1c8fb73a92`.
- [목록 전달 안내·검수 범위](../integrations/career-integration-listing-v003.md)

두 ZIP은 각각 실제 실행물과 별도 목록/연동 코드이며 CRC·멤버 바이트를 확인했습니다. 테스트는71공간 API 시작/실제 물건 연결/업무 전 종료, 정상 UI는 준비 과제10001v003과 DB431v003 두 사례, 실제 연동은 추출 ZIP의 React 시작/종료·이벤트·로컬 ACK를 확인했습니다. 555개 전체 업무·필수 특수분기·운영 백엔드는 완료 검수가 아닙니다. 원래 특수분기554개 미구현과 얇은 트레이 포인터 선택 등 알려진 한계는 런타임 검토·전체 목표표에 남겼습니다.

실제 장면73개/공간71개, 사용935건/구성 인스턴스1101개, 포함 에셋427버전(구성355+조립72)을 구분했습니다. 조립 참조를 구성품 수량에 이중 합산하지 않았고, 최종 새 사용 revision의 실행 검사는 미검증으로 유지해 과거 pass를 승계하지 않았습니다. [최종 제한 검토](../../machine/evidence/career-full-v001/final-bounded-review.json)와 [전체 에셋 조회v002](../assets/career-asset-reuse-report-v002.md)를 참조하세요.

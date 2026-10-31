# Unity-MeshyAI

현재71공간 전달 기준: [workplaces-v006](docs/human/builds/workplaces-v006.md) — 현재319모델(248소품+71조립),805배치, 실제Unity Play Mode장면/HTTP71/71·시각71쌍·사무보조원구현범위 통과. v005이하는보존중간본이며 다른551직업초안은별도다.

[전달 ZIP](unity/webgl/packages/workplaces-v006.zip) · [manifest](unity/webgl/packages/workplaces-v006.manifest.json) · [실행 안내](docs/human/builds/workplaces-v006-run.md). 로컬 전달 파일은 Git에서 제외하며 외부 배포하지 않았다.

Meshy 원본 → Blender 수정본 → 실제 사용본 → Unity → WebGL을 에셋 ID와 버전으로 연결합니다.

```text
AGENTS.md                   에이전트 규칙·데이터 계약·검토 절차
docs/
  human/                    사람이 읽는 에셋·빌드 안내와 작업 절차
  machine/catalog/          에셋·빌드·공용 텍스처·원본 이미지 목록
images/original/
  panoramas/                파노라마 원본 이미지
  assets/                   에셋 제작용 원본 이미지
meshy/models/
  original/                 원본·생성 기록·미리보기
  blender/                  Blender 수정본과 exports/ 실제 사용본
  textures/
    color1.jpg              기본 채색
    color2.jpg              필요할 때 사용하는 강조·원색
    palettes/               두 원본을 합친 정사각형 PNG·UV 대응표
unity/
  projects/                 편집용 Unity 프로젝트
  webgl/
    builds/                 WebGL 실행 출력
    packages/               전달용 ZIP
```

- [사람용 문서](docs/human/README.md)
- [웹용 로우폴리 제작 요약](docs/human/guides/web-lowpoly.md)
- [원본 이미지 목록](docs/human/images/README.md)
- [프로그램용 데이터](docs/machine/README.md)
- [에이전트 필수 규칙](AGENTS.md)
- [텍스처 사용 안내](meshy/models/textures/README.md)
- [WebGL 전달 절차](docs/human/guides/webgl-delivery.md)

초기 베타 기록: 팔레트 원본 두 장과 공용 PNG v001, [첫 바닥판 베타 AST-001 v001](docs/human/assets/AST-001-v001.md)이 등록되어 있습니다. Meshy→Blender→GLB→로컬 웹 표시를 검증했습니다. 당시에는 Unity 프로젝트·WebGL 빌드가 없었으며, 현재 결과는 위 workplaces-v006 안내를 기준으로 합니다.

- [사무보조원 실제 Unity WebGL 실행·전달·검증 결과](docs/human/builds/office-assistant-v003.md)

- [보존된 office-assistant-v005 데모: 선택한 물건 확대·종이 팝업 실행](docs/human/builds/office-assistant-v005.md)

## 전체71개 공간 제작·실행

[workplaces-v006 Unity WebGL 보고](docs/human/builds/workplaces-v006.md)에서 실제 빌드·공간별 검수와 전달 범위를 확인한다. [전체 진행 기록](docs/human/jobs/workplace-production-v001.md), [후보v004](docs/human/jobs/workplace-common-assets-v004.md), [모델 전체 버전 색인](docs/human/assets/workplace-models-v001.md)을 함께 유지한다. 기존 데모/원본/버전은 보존하며,71개 공간 제작과552개 직업 시나리오 전체 구현을 구분한다.

### 최신 공간 특색·좌석 방향 수정

[workplaces-v009 검수](docs/human/builds/workplaces-v009.md) · [WebGL ZIP](unity/webgl/packages/workplaces-v009.zip). 교회·성당 구분과7공간 좌석17개 방향·카메라 가림 수정. 공용 장식8개는 분리 라이브러리 검수 중.


## 직업 기본 체험10개 — career-pilot-v007

[ZIP](unity/webgl/packages/career-pilot-v007.zip) · [실행/검수](docs/human/builds/career-pilot-v007.md) · [10직업목록](docs/human/jobs/career-pilot-ten-v001.md). 기존71공간/사무테마10종과 구별되는 선택10개 기본3단계체험이다. 실제30작업면·종료원장·압축해제HTTP 검수완료. 편집은 같은 프로젝트의 고정사본 unity/projects/CareerPilotTen-v001을 따른다.

물류관리사 배치 진행 오류는 career-pilot-v007에서 수정했다. [재현·수정 근거](docs/human/builds/logistics-placement-fix-v001.md). 이전 v005/중간 v006 결과는 보존했으며 현재 권장 전달본은 v007이다.

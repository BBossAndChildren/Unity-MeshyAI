# Unity-MeshyAI

Meshy 원본 → Blender 수정본 → 실제 사용본 → Unity → WebGL을 에셋 ID와 버전으로 연결합니다.

```text
AGENTS.md                   에이전트 규칙·데이터 계약·검토 절차
docs/
  human/                    사람이 읽는 에셋·빌드 안내와 작업 절차
  machine/catalog/          프로그램용 에셋·빌드·공용 텍스처 목록
meshy/models/
  original/                 원본·생성 기록·미리보기
  blender/                  Blender 수정본과 exports/ 실제 사용본
  textures/
    color1.jpg              기본 채색
    color2.jpg              필요할 때 사용하는 강조·원색
unity/
  projects/                 편집용 Unity 프로젝트
  webgl/
    builds/                 WebGL 실행 출력
    packages/               전달용 ZIP
```

- [사람용 문서](docs/human/README.md)
- [프로그램용 데이터](docs/machine/README.md)
- [에이전트 필수 규칙](AGENTS.md)
- [텍스처 사용 안내](meshy/models/textures/README.md)
- [WebGL 전달 절차](docs/human/guides/webgl-delivery.md)

현재 텍스처 두 개가 등록되어 있으며 실제 모델·Unity 프로젝트·WebGL 빌드는 아직 없습니다.

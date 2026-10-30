# WebGL 전달

1. Unity WebGL 출력 전체를 unity/webgl/builds/<build_id>/에 저장합니다.
2. 빌드 목록과 상세 문서를 등록합니다. 업로드 전 artifact_url은 null입니다.
3. 아래 구조로 임시 전달 폴더를 구성한 뒤 unity/webgl/packages/<build_id>.zip으로 압축합니다.
4. 압축을 풀어 파일 구성과 실제 웹 서버 실행을 확인하고 전달합니다.
5. 원격 보관·호스팅 위치가 생기면 artifact_url을 갱신합니다.

```text
<빌드 ID>.zip
  site/           index.html 및 WebGL 출력 전체
  manifest.json   빌드·포함 에셋·사용한 텍스처 메타데이터
  BUILD.md        빌드 상세 설명
  README.md       받는 사람의 실행 안내
```

manifest.json 형식과 검토 기준은 [AGENTS.md](../../../AGENTS.md)를 따릅니다.
기존 ZIP은 덮어쓰지 않습니다. Unity 프로젝트·Meshy 원본·Blender 수정본은 포함하지 않습니다.
site/ 내부 상대 경로를 유지하고 웹 서버에서 실행합니다. 서버의 압축 설정과 외부 의존성은 BUILD.md에 기록합니다.
별도 패키징 스크립트나 자동 검사 훅은 사용하지 않습니다.

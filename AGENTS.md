# 에이전트 필수 작업 규칙

이 저장소에서 작업하는 에이전트는 수정 전에 이 문서를 읽고 반드시 준수합니다.
규칙·목록 형식·검토 절차는 이 파일에서 관리합니다. 별도 에이전트 폴더, 검사 스크립트, 자동 훅은 사용하지 않습니다.
사용자 지시 및 상위 지침이 우선합니다.

## 1. 작업 순서
1. 기존 문서와 JSON 목록, 대상 파일을 확인합니다.
2. 원본을 보존하면서 요청한 자료를 수정하고 목록·설명을 함께 갱신합니다.
3. 완료 전 아래 검토 항목을 확인하고 실제 수행한 검증과 미검증 항목을 보고합니다.
4. 실제 Blender/Unity 실행 없이 모델·빌드 실행을 검증했다고 보고하지 않습니다.

## 2. 파일 구조와 식별자
- 사람용 문서: docs/human/. 프로그램용 데이터: docs/machine/catalog/.
- 모델 원본: meshy/models/original/<asset_id>/<version>/. README.md에 프롬프트, 작업 ID(없으면 사유), 생성일과 사용 조건을 기록합니다.
- Blender 수정본: meshy/models/blender/<asset_id>/<version>/model.blend.
- 실제 사용본: 같은 Blender 버전 폴더의 exports/.
- 미리보기: 원본 버전 폴더의 previews/. 미리보기는 재질용 텍스처가 아닙니다.
- Unity 적용본: unity/projects/<project>/Assets/Meshy/<asset_id>/<version>/.
- asset_id는 AST-001처럼 AST-와 세 자리 이상 숫자, version은 v001처럼 v와 세 자리 이상 숫자입니다.
- (asset_id, version)은 유일하며 등록된 원본·수정본·실제 사용본은 새 버전으로 갱신합니다.
- build_id는 showcase-v001처럼 소문자·숫자·하이픈과 버전 접미사로 구성하고 유일해야 합니다.
- 모든 데이터 경로는 저장소 루트 기준 상대 경로이며 /를 사용합니다. 절대 경로와 ..는 금지합니다.

## 3. 두 공용 텍스처의 역할
- color1: meshy/models/textures/color1.jpg. 모든 모델의 기본 채색에 우선 사용하는 기본 팔레트입니다.
- color2: meshy/models/textures/color2.jpg. 강조 부분이나 선명한 원색이 필요한 경우에만 추가하는 보조 팔레트입니다.
- 기본 구성은 color1만 사용합니다. color2가 필요할 때 color1과 함께 사용하고 해당 에셋의 accent_reason에 용도를 기록합니다.
- 두 파일은 사용자가 제공한 원본을 그대로 보존합니다. 임의 생성·색상 변경·교체·추가 텍스처 제작은 하지 않습니다.
- Blender UV와 재질을 해당 팔레트에 맞춥니다. 실제 사용본에 다른 재질용 이미지나 모델별 텍스처를 추가하지 않습니다.
- 보존용 Meshy 원본의 내장 이미지와 실제 사용본의 허용 텍스처를 구분합니다.
- Unity에서는 Assets/Shared/Textures/에 필요한 파일을 원본과 동일한 바이트로 프로젝트당 한 번씩 복사하고 공유합니다. 모델별 폴더에 복제하지 않습니다.
- Blender/GLB 내부 이미지, UV·재질 연결은 파일 목록만으로 검증할 수 없으므로 별도로 확인합니다.

## 4. 기계용 목록 계약
모든 JSON 파일은 UTF-8, schema_version: 2를 사용합니다. 등록된 에셋·빌드가 없으면 배열은 비어 있습니다.

### shared-textures.json
루트 필드: schema_version, textures.
textures는 아래 두 항목만 포함합니다.
- texture_id: color1, role: base, path: meshy/models/textures/color1.jpg, usage: 기본 채색.
- texture_id: color2, role: accent, path: meshy/models/textures/color2.jpg, usage: 강조 또는 원색이 필요한 경우.
각 항목의 sha256은 원본 파일 바이트의 SHA-256입니다. Unity 임포트 복사본도 이 해시와 같아야 합니다.

### assets.json
루트 필드: schema_version, assets.
각 에셋의 필수 필드:
- asset_id, version, name.
- source_path: 원본 모델 파일.
- blender_path: 수정본 .blend 파일.
- runtime_path: Blender 버전 폴더 exports/ 안의 실제 사용 모델 파일.
- preview_path: 원본 버전 폴더 previews/ 안의 미리보기 파일.
- unity_path: 프로젝트 Assets/Meshy/<asset_id>/<version>/ 디렉터리.
- texture_ids: 기본은 ["color1"], 강조가 필요하면 ["color1", "color2"]. 중복·미등록 ID는 금지합니다.
- accent_reason: color2 사용 시 구체적인 용도를 적은 문자열, 사용하지 않으면 null.
- unity_texture_paths: 사용한 texture_id를 키로, 프로젝트 Assets/Shared/Textures/color1.jpg 또는 color2.jpg 경로를 값으로 하는 객체. texture_ids와 키 집합이 같아야 합니다.

예시 텍스처 필드:
```json
{
  "texture_ids": ["color1", "color2"],
  "accent_reason": "손잡이의 빨간 강조 부분",
  "unity_texture_paths": {
    "color1": "unity/projects/MeshyShowcase/Assets/Shared/Textures/color1.jpg",
    "color2": "unity/projects/MeshyShowcase/Assets/Shared/Textures/color2.jpg"
  }
}
```
동일 에셋 버전의 여러 프로젝트 등록은 현재 지원하지 않습니다.

### builds.json
루트 필드: schema_version, builds.
각 빌드의 필수 필드:
- build_id.
- project_path: unity/projects/<project>.
- output_path: unity/webgl/builds/<build_id>.
- document_path: docs/human/builds/<build_id>.md.
- artifact_url: 업로드 전 null, 업로드 후 실제 HTTPS 실행 또는 다운로드 URL.
- assets: {"asset_id": "AST-001", "version": "v001"} 형태의 참조 배열. 중복 없이 등록된 정확한 버전을 참조하며 해당 프로젝트 소속이어야 합니다.

## 5. Unity와 WebGL 전달
- Unity 프로젝트는 unity/projects/, WebGL 출력은 unity/webgl/builds/로 분리합니다.
- Unity 프로젝트의 Assets/, Packages/, ProjectSettings/ 및 .meta 파일을 관리합니다.
- 빌드 설명에 목적, Unity 버전, 소스 커밋, 날짜, 포함 에셋 설명, 외부 의존성과 서버 설정을 기록합니다.
- 전달 파일은 unity/webgl/packages/<build_id>.zip. 기존 ZIP을 덮어쓰지 않습니다.
- ZIP의 site/에 WebGL 출력 전체를 상대 경로 그대로 넣습니다.
- manifest.json에는 schema_version: 2, build(빌드 항목), assets(참조를 해소한 에셋 배열), textures(실제 참조한 공용 텍스처 메타데이터 배열)를 기록합니다.
- BUILD.md에 해당 빌드 설명, README.md에 실행 안내를 넣습니다.
- Unity 프로젝트와 Meshy·Blender 원본은 ZIP에 넣지 않습니다.
- WebGL은 웹 서버에서 실행 확인합니다. index.html 더블클릭만으로 검증하지 않습니다.
- 로컬 빌드와 ZIP은 Git에서 제외합니다.

## 6. 완료 전 검토
- JSON 구문·schema_version·필수 필드·ID 유일성 확인.
- 원본·Blender·실제 사용본·미리보기·Unity·문서 경로 존재 여부 확인.
- 빌드의 에셋 ID·버전 참조와 프로젝트 소속 확인.
- 텍스처 폴더의 재질용 이미지는 color1.jpg와 color2.jpg뿐인지, 등록 해시와 원본·임포트 복사본이 같은지 확인.
- 기본 채색에 color1을 사용하고 color2 사용 이유가 기록되어 있는지 확인.
- 문서 링크 및 전달 ZIP 구조 확인.
- Blender/Unity 재질·장면·WebGL 실행과 URL 가용성은 실제 확인한 범위만 보고.

이 문서는 에이전트의 준수 지침이며 자동 실행 또는 CI 강제를 의미하지 않습니다.

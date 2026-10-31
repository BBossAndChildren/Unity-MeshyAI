# 에이전트 필수 작업 규칙

이 저장소에서 작업하는 에이전트는 수정 전에 이 문서를 읽고 반드시 준수합니다.
규칙·목록 형식·검토 절차는 이 파일에서 관리합니다. 별도 에이전트 제어 폴더, 검사 스크립트, 자동 훅은 사용하지 않습니다. 모델 제작 결과물인 재사용 후처리 스크립트는 해당 에셋 버전의 processing/에 보관할 수 있습니다.
사용자 지시 및 상위 지침이 우선합니다.

- 모든 모델에 Meshy를 사용할 필요는 없습니다. 제작 도구는 복잡도보다 형태의 특성을 우선해 선택합니다. 반복·대칭 구조, 정확한 치수, 명확한 부품 구성이 중요하면 Blender를, 유기적 형태·불규칙한 실루엣·자유로운 곡면이 중요하면 Meshy를 우선합니다. 복잡해 보여도 기본 도형과 반복 구조로 표현할 수 있으면 Blender를 우선합니다. 스크립트 재사용 가능성과 예상 수정 부담도 함께 고려합니다.

## 에이전트 모델·추론 강도 선택

- 기본 선택은 `gpt-6.1-sol / high`입니다.
- 작업 난이도와 문제의 복잡성에 따라 `high`, `xhigh`, `max` 중에서 선택합니다.
- 동일 문제에 대한 오류 수정·재검증이 현재 단계에서 연속 2회 실패하면 `high → xhigh → max` 순서로 한 단계 상향합니다. 상향 후에는 해당 단계에서의 연속 실패 횟수를 새로 집계합니다.
- `max`에서는 더 높은 단계를 임의로 만들지 않고 실패 원인과 접근 방법을 재검토합니다.
- 이 규칙은 실행 환경의 모델·추론 강도를 자동으로 변경하는 설정이 아닙니다. 변경 수단이 없으면 필요한 설정 변경을 알리고, 실제로 변경하지 않은 상태를 상향 완료로 보고하지 않습니다.

## 1. 작업 순서
1. 기존 문서와 JSON 목록, 대상 파일을 확인합니다.
2. 원본을 보존하면서 요청한 자료를 수정하고 목록·설명을 함께 갱신합니다.
3. 완료 전 아래 검토 항목을 확인하고 실제 수행한 검증과 미검증 항목을 보고합니다.
4. 실제 Blender/Unity 실행 없이 모델·빌드 실행을 검증했다고 보고하지 않습니다.

### 매 작업의 에셋 명세·전체 사용처 갱신
- 이미지·에셋 제작, 수정, 재사용, 장면 조립·배치 작업마다 기존 에셋 목록과 재사용 가능한 모델·스크립트를 먼저 조회하고, 작업에 영향을 받은 개별 에셋의 사람용 명세와 기계용 목록을 함께 갱신합니다. 공통 에셋과 전용 에셋을 구분하고 같은 형상을 공간마다 중복 제작하지 않습니다.
- 각 명세에 후보 ID 또는 실제 asset_id/version, 이름, 구성 부품, 형태·치수 및 미정 항목, 제작 방식·선택 이유, 기존 모델·스크립트 재사용 참조, 색상 변형 계획, 검수 상태·증거를 적습니다. 명세·후보를 제작 완료 모델로 등록하지 않습니다.
- **사용 후보를 요약하거나 생략하지 않습니다.** 해당하는 모든 공간의 정확한 이름, prompt_id/version 및 등록된 경우 context_id/version과 panorama ID/version을 전부 기록합니다. '사무실 등', '외 N곳', 대표 공간만 쓰기, 개수만 쓰기는 전체 후보 명세를 대체하지 못합니다. 수량 미정은 미정으로 표시합니다.
- **실제로 사용한 곳도 에셋마다 별도로 표시합니다.** 근거가 있는 모든 프로젝트·장면·프리팹 또는 Blender/GLB 조립 결과의 ID·버전/revision, 사용 수량과 근거 경로를 빠짐없이 조회해 보여 줍니다. 사용 후보, 이미지의 시각적 등장, 실제 모델 배치, 빌드 포함, 실행 검증을 각각 구분합니다. 사용 기록이 없으면 '실제 사용 이력 미등록/미검증'으로 쓰고 사용하지 않았다고 단정하지 않습니다.
- 실제 사용의 원장은 기존 계약을 따릅니다. Unity 사용은 asset-usages.json, Blender/독립 GLB 조립은 해당 조립 기록과 placements/inspection 증거를 조회합니다. 명세의 사용처 표는 원장에서 파생한 조회 결과이며 별도의 중복 사용 원장으로 관리하지 않습니다. 현재 상태는 최신 revision만 집계하고 과거 이력은 보존합니다.
- 호출 횟수·실제 토큰·Meshy 크레딧 등 측정 가능한 사용량과 출처·측정 시점을 작업별로 남깁니다. 캐시 입력·일반 입력·출력, 대화 토큰과 이미지 생성 비용, 과거 비용과 이번 비용을 구분합니다. 도구가 반환하지 않거나 개별 에셋으로 배분할 수 없는 값은 null과 미측정 사유로 남기며 추정치를 실측값으로 쓰지 않습니다.
- 완료 전 전체 후보 누락·중복, 사용처 근거·ID·버전·수량, 명세와 JSON 참조 일치 및 비용의 미측정 표시를 검토합니다. 이 절은 매번 읽고 수행하는 필수 지침이며 자동 실행 훅·검사 스크립트를 설치하라는 지시가 아닙니다.

## 2. 파일 구조와 식별자
- 사람용 문서: docs/human/. 프로그램용 데이터: docs/machine/catalog/.
- 원본 이미지: images/original/panoramas/는 파노라마, images/original/assets/는 에셋 제작용 이미지입니다. 파일은 <image_id>/<version>/ 아래에 원본 그대로 보관합니다.
- 이미지 등록 시 파노라마는 panoramas.json, 에셋 이미지는 asset-images.json에 반드시 함께 등록합니다. 원본을 덮어쓰지 않고 수정본은 새 버전으로 등록합니다.
- 원본 이미지는 모델 제작·참고용 자료이며 color1/color2 재질 텍스처 및 모델 미리보기와 구분합니다. 이미지 등록 자체가 추가 모델 텍스처 사용을 허용하지 않습니다.
- 모델 원본: meshy/models/original/<asset_id>/<version>/. Meshy 결과 또는 Blender 직접 제작 source.blend를 보존합니다. README.md에 실제 제작 방식·선택 이유·제작일·사용 조건을 적고, Meshy 사용 시 프롬프트·작업 ID·실제 소비 크레딧을 기록합니다. 직접 제작을 Meshy 생성으로 기록하지 않습니다.
- Blender 수정본: meshy/models/blender/<asset_id>/<version>/model.blend.
- 실제 사용본: 같은 Blender 버전 폴더의 exports/.
- 미리보기: 원본 버전 폴더의 previews/. 미리보기는 재질용 텍스처가 아닙니다.
- Unity 적용본: unity/projects/<project>/Assets/Meshy/<asset_id>/<version>/.
- asset_id는 AST-001처럼 AST-와 세 자리 이상 숫자, version은 v001처럼 v와 세 자리 이상 숫자입니다.
- (asset_id, version)은 유일하며 등록된 원본·수정본·실제 사용본은 새 버전으로 갱신합니다.
- build_id는 showcase-v001처럼 소문자·숫자·하이픈과 버전 접미사로 구성하고 유일해야 합니다.
- 모든 데이터 경로는 저장소 루트 기준 상대 경로이며 /를 사용합니다. 절대 경로와 ..는 금지합니다.

## 3. 팔레트 원본과 최종 공용 텍스처
- color1.jpg는 피부·옷·몸통·지형 등 넓은 면의 파스텔 기본색 원본입니다.
- color2.jpg는 강조선·눈·입·작은 장식·포인트의 원색·대비색 원본입니다.
- 원본 두 장은 meshy/models/textures/에 그대로 보존합니다. 이미지에 없는 색을 만들거나 기존 색을 임의 보정하지 않습니다. 사용 색상 수를 4색으로 제한하지 않습니다.
- 실제 사용본은 두 원본의 색상 칸을 함께 담은 정사각형 공용 PNG 한 장과 공용 재질을 사용합니다. 두 JPG를 별도 런타임 텍스처로 사용하는 이전 규칙을 대체합니다.
- 파생 팔레트는 meshy/models/textures/palettes/<version>/palette.png, 대응표는 같은 폴더의 mapping.json에 저장합니다. 원본 색을 보존한 재배치만 허용하며 상세 기준은 7절을 따릅니다.
- 기본 면은 color1 출처 칸, 강조 영역은 color2 출처 칸을 UV로 참조합니다. color2 사용 부위는 accent_reason에 기록합니다.
- Unity에는 최종 palette.png를 Assets/Shared/Textures/<palette_version>/에 동일 바이트로 복사해 공유합니다. 모델별 이미지와 불필요한 재질 맵을 추가하지 않습니다.
- 보존용 Meshy 원본의 내장 이미지와 실제 사용본의 허용 텍스처를 구분합니다.

## 4. 기계용 목록 계약
모든 JSON 파일은 UTF-8, schema_version: 3를 사용합니다. 등록된 에셋·빌드가 없으면 배열은 비어 있습니다.

### shared-textures.json
루트 필드: schema_version, textures.
textures는 아래 두 항목만 포함합니다.
- texture_id: color1, role: base, path: meshy/models/textures/color1.jpg, usage: 기본 채색.
- texture_id: color2, role: accent, path: meshy/models/textures/color2.jpg, usage: 강조 또는 원색이 필요한 경우.
각 항목의 sha256은 원본 파일 바이트의 SHA-256입니다. 이 목록은 색상 출처이며 런타임 텍스처 목록이 아닙니다.

### assets.json
루트 필드: schema_version, assets.
각 에셋의 필수 필드:
- asset_id, version, name.
- source_path: 원본 모델 파일. Blender 직접 제작은 original/<asset_id>/<version>/source.blend를 사용합니다.
- blender_path: 수정본 .blend 파일.
- runtime_path: Blender 버전 폴더 exports/ 안의 실제 사용 모델 파일.
- preview_path: 원본 버전 폴더 previews/ 안의 미리보기 파일.
- unity_path: 프로젝트 Assets/Meshy/<asset_id>/<version>/ 디렉터리.
- kind: prop 또는 diorama. 작업 전에 분류합니다.
- palette_version: palettes.json에 등록된 고정 버전.
- accent_reason: color2 출처 색을 사용한 부위·용도, 미사용 시 null.
- unity_palette_path: Unity 공용 폴더의 최종 palette.png 경로. Unity 적용 전에는 unity_path와 함께 null을 허용하고 상태를 명시합니다.
- inspection_path: 해당 Blender 버전 폴더의 inspection.json.
- processing_paths: 재사용 제작·후처리 스크립트 경로 배열. 기존 에셋의 고정 버전 스크립트를 참조할 수 있습니다. 직접 제작 스크립트는 반드시 보존하고 수작업인 경우 제작 기록에 사유를 남깁니다.
- status: in_progress 또는 ready. ready는 필수 제작·검수 조건을 충족한 경우만 사용합니다.
- generation_method: blender_direct, meshy 또는 hybrid. meshy는 Meshy 형태 생성 후 Blender 후처리를 포함하고, hybrid는 구성 부품을 두 도구로 나누어 제작한 경우입니다.
- generation_reason: 도구 선택 이유 한두 문장.
- production_record_path: 제작 방식·부품별 분담·재사용 경로·Meshy 프롬프트와 작업 ID·비용 근거·실제 결과·다음 개선점을 기록한 원본 버전 README.md 경로.
- meshy_credits_used: 해당 버전 제작 과정의 실제 소비 크레딧. Meshy 미사용이 확인되면 0, 사용했으나 미측정이면 null로 기록하고 제작 기록에 미검증 사유를 남깁니다. 추정치를 실제 비용으로 기록하지 않습니다. 재사용 모델의 과거 생성 비용은 이번 비용과 구분합니다.
제작 메타데이터는 신규 등록 및 기존 에셋의 다음 갱신 때 반영합니다. 기존 항목의 누락값을 근거 없이 채우지 않습니다. 기존 schema_version: 3 목록은 유지하며 누락된 제작 방식·비용을 소비자가 임의 추정하지 않습니다.
제작 중 아직 없는 blender_path, runtime_path, preview_path는 null을 허용하되 inspection.json에 사유를 기록합니다. 없는 파일의 경로를 완료 결과처럼 등록하지 않습니다.

동일 에셋 버전의 여러 프로젝트 등록은 현재 지원하지 않습니다.
이미지를 사용한 모델에는 선택 필드 source_images를 추가합니다. 값은 {"catalog": "asset-images", "image_id": "IMG-001", "version": "v001"} 형태의 참조 배열입니다. catalog는 asset-images 또는 panoramas이며 실제 등록된 ID·버전만 중복 없이 참조합니다. 이미지 없이 제작한 모델은 필드를 생략하거나 빈 배열로 둡니다.

### asset-images.json / panoramas.json
두 파일의 루트 필드는 schema_version: 3와 images 배열입니다. 미등록 상태는 빈 배열입니다.
각 이미지의 필수 필드:
- image_id: 에셋 이미지는 IMG-001, 파노라마는 PAN-001 형식으로 접두사 뒤 세 자리 이상 숫자.
- version: v001 형식. (image_id, version) 쌍은 각 목록에서 유일해야 합니다.
- name: 사람이 식별할 이름.
- path: 에셋 이미지는 images/original/assets/<image_id>/<version>/<파일명>, 파노라마는 images/original/panoramas/<image_id>/<version>/<파일명>.
- sha256: 원본 파일 바이트의 SHA-256.
- width, height: 실제 이미지의 가로·세로 픽셀 수인 양의 정수.
- source: 제공자 또는 생성 도구·작업 ID 등 출처 설명. 알 수 없으면 확인되지 않았음을 명시합니다.
- usage_rights: 사용 조건 또는 권리 확인 상태. 모르는 권리를 추정하지 않습니다.
- description: 이미지 내용과 제작 용도.
파노라마에는 projection도 필수입니다. equirectangular, cubemap, other, unknown 중 실제 확인한 값을 기록하고 화면 비율만으로 투영 형식을 단정하지 않습니다.
이미지는 모델 생성 전에 독립적으로 등록할 수 있습니다. 모델 연결은 assets.json의 source_images를 기준으로 하며 이미지 목록에 역방향 연결을 중복 관리하지 않습니다.

아래 직업 공간 기획 목록의 schema_version은 3이며 모델·빌드와 별도로 조회합니다.

### workplace-contexts.json / occupation-workplace-candidates.json
- 공간 컨텍스트는 모델 등록과 분리된 기획 자료입니다. 파노라마는 개별 에셋을 조립한 최종 공간의 형태·배치·의미 기준이며, 파노라마 신규 생성 지시가 아닙니다.
- 두 목록은 schema_version: 3, review_status를 포함합니다. review_status는 pending_user_approval 또는 approved이며 사용자 승인 없이 approved로 바꾸지 않습니다.
- workplace-contexts.json 루트는 occupation_catalog_path, planning_source_path, shared_context, contexts를 포함합니다. 경로는 실제 저장소 상대 경로입니다.
- contexts 항목은 context_id(소문자 영문·숫자·하이픈), version(vNNN), review_status, name, panorama_ref, reference_role, meaning, tags, office_characteristics, activity_sequence, layout_intent, asset_slots, occupation_groups, avoid_interpretations, adaptation_notes를 포함합니다. (context_id, version)은 유일합니다.
- panorama_ref는 실제 panoramas 목록의 catalog/image_id/version을 참조합니다. reference_role은 final_scene_composition_reference입니다. tags는 space/activity/interaction/visual의 한국어 문자열 배열입니다. 의미·이용자·업무·상호작용·시각 단서를 함께 기록합니다.
- occupation_groups는 label, occupation_ids, mapping_basis, reason, applicability_condition을 포함합니다. occupation_ids는 직업 후보 목록에 존재해야 하며 그룹 안에서 중복하지 않습니다. 장면 기획 추정은 editorial_scene_candidate로 표시하고 실제 근무지 검증과 구분합니다.
- asset_slots는 문맥 전달용 계획이며 실제 에셋 목록이 아닙니다. 각 슬롯에 slot_id(컨텍스트 내 유일), name, semantic_role, placement_relationship, priority(identity/supporting), evidence, asset_ref, quantity, production_status를 기록합니다. 미제작이면 asset_ref와 미정 quantity는 null, production_status는 planning_only입니다. 실제 에셋 연결 시 asset_ref는 존재하는 asset_id/version 쌍이어야 합니다.
- occupation-workplace-candidates.json은 source, sections, occupations를 포함합니다. source에는 원문 경로·SHA-256, 원문이 보고한 날짜·총수와 실제 추출 수, 자료 완전성·한계·검증 범위를 구분해 기록합니다.
- occupations는 occupation_id(직업 원문의 seq에서 career-net-<seq>), name, source_url, source_categories, source_status를 포함합니다. occupation_id는 유일합니다. source_categories에는 name과 basis(source_keyword_candidate/source_work_based_estimate)를 기록해 제공 자료의 추정 표시를 유지합니다. source_status는 candidate_not_verified이며 근무지 사실 확인을 뜻하지 않습니다.
- 직업은 여러 공간의 후보가 될 수 있습니다. 누락 자료·잘린 첨부는 추측으로 복원하지 않습니다. JSON 구문·ID 유일성·원본 해시·파노라마/직업/에셋 참조와 문서 링크를 확인하고 사람용 설명도 함께 갱신합니다.

### panorama-prompts-vNNN.json
- 파노라마 생성 전 기획 프롬프트 목록입니다. schema_version:3, package_id, version, source_document_path, source_document_sha256, occupation_catalog_path, scope, excluded_categories, execution_status, items를 기록합니다.
- 각 items 항목은 prompt_id(PRM-숫자 세 자리 이상), version(vNNN), source_category, name, scene_purpose, key_props, layout_intent, status, existing_panorama_ref, result_panorama_ref, prompt를 갖습니다. (prompt_id, version)은 유일합니다.
- status는 existing_reference(기존 이미지 재사용), prompt_ready(실행 전), needs_subject_selection(주제 선택 필요)입니다. 이번 목록의 execution_status는 not_started입니다.
- source_category는 직업 후보 목록에 존재하는 장소 분류를 참조합니다. 특정 세부 장면에 원문 분류의 모든 직업을 자동 연결하지 않습니다.
- existing_panorama_ref는 실제 등록된 catalog/image_id/version 또는 null, result_panorama_ref는 아직 생성하지 않았으면 null입니다. PRM ID를 이미지·모델 ID로 사용하지 않습니다.
- 파일명 vNNN과 루트 version은 일치해야 합니다. 패키지 개정은 새 파일로 보존하고 변경된 prompt_id의 항목 version을 올립니다. 기존 ID를 재번호화하지 않습니다.
- 프롬프트 작성·업로드를 이미지 생성·모델 제작·사용 권리 확인으로 기록하지 않습니다. 실제 결과 등록은 기존 이미지 catalog 계약을 따릅니다.

### workplace-asset-candidates-vNNN.json — 전체 공간 제작 후보·명세
- 전체 공간별 에셋 후보와 역조회 명세는 버전별 목록으로 보존합니다. 루트에 schema_version:3, package_id, version, document_path, source_paths, candidates, scenes를 기록합니다. 이전 버전을 supersedes로 연결하며 현재 설명용 색인에서 최신 문서로 안내합니다.
- candidates는 정식 AST 등록 전 후보 ID(CND-숫자 세 자리 이상), name, production_status:planning_only, 미정 asset_ref/quantity:null, 원문 표현·출처 refs, 제작 방식 검토·재사용 후보, specification, full_scene_candidates, actual_usage_refs를 포함합니다. 후보 ID는 정식 에셋 ID를 대체하지 않습니다. 일반 명칭·세트는 낱개 형상 확정 전 draft로 표시합니다.
- full_scene_candidates에는 해당하는 모든 공간의 name, 고정 prompt_ref, 실제 panorama_ref 또는 미등록 null, 실제 등록된 context_refs, 미정 quantity:null, placement_state:planning_only를 기록합니다. scenes는 공간별 전체 필요한 candidate ID와 원문 key_props별 대응을 제공하며 누락을 검사합니다.
- actual_usage_refs는 기존 사용 원장을 조회할 수 있는 참조만 기록합니다. 사람용 사용처 표의 수량·환경·증거는 그 원장의 최신 기록에서 파생합니다. 이 후보 목록에 독립적인 실제 배치 원장을 만들지 않습니다. 원장이 없거나 사용 근거가 없으면 미등록/미검증으로 표시합니다.
- 모델별 token·과금 배분을 추정하지 않습니다. 별도 작업 사용량 보고는 schema_version:3과 출처·측정 시점·범위·호출 수·실측값·미측정 사유를 기록하고 원본 메시지나 비밀 값을 복제하지 않습니다.

### inventory-snapshots.json
- 통합 검토 문서의 등록 색인입니다. 루트는 schema_version: 3, snapshots 배열입니다. 실제 에셋·직업 연결·변형·사용 이력의 원장을 대체하지 않습니다.
- 각 항목은 snapshot_id(소문자 영문·숫자·하이픈), version(vNNN), document_path, document_sha256, document_kind, registration_status, planning_status, source_refs, snapshot_counts, context_refs, panorama_refs, asset_refs, notes를 포함합니다. (snapshot_id, version)은 유일합니다.
- document_kind는 inventory_and_planning_snapshot, registration_status는 registered입니다. planning_status는 pending_user_approval 또는 approved이며 저장·등록만으로 제작·검증을 승인하지 않습니다.
- 문서·출처 경로는 저장소 상대 경로이며 실제 파일과 SHA-256을 대조합니다. source_refs 항목은 path와 sha256을 포함합니다. 원문 문서를 보존하고 내용 개정은 새 문서 버전으로 기록합니다.
- context_refs는 context_id/version, panorama_refs는 catalog/image_id/version, asset_refs는 asset_id/version으로 실제 목록의 고정 항목만 참조합니다. 적용 후보를 실제 사용으로 승격하지 않습니다.
- snapshot_counts는 문서 시점의 집계이며 현재 수량으로 자동 사용하지 않습니다. 과거 문서와 현재 catalog의 차이는 notes와 사람용 색인에 설명합니다.
- 직업 후보 목록의 선택 source_history는 이전 source 객체 배열입니다. 출처 교체 시 기존 원문을 보존하고, 전체 원문의 추가 직업을 기존 occupation_groups에 자동 연결하지 않습니다.

### palettes.json
루트 필드: schema_version: 3, palettes 배열. 생성 전에는 빈 배열입니다.
각 팔레트 필수 필드: version(v001 형식, 유일), path, mapping_path, width, height, sha256, source_texture_ids(["color1", "color2"]).
path는 meshy/models/textures/palettes/<version>/palette.png, mapping_path는 같은 폴더의 mapping.json이며 width와 height는 같은 양의 정수입니다.

### mapping.json (팔레트 버전별)
필수 필드: schema_version: 3, palette_version, palette_sha256, width, height, sources, cells.
sources에는 texture_id, sha256, width, height를 기록합니다.
cells에는 texture_id, row, column, source_rect_px([x,y,width,height]), source_sample_px([x,y]), target_rect_px([x,y,width,height]), uv_center([u,v])를 기록합니다.
행·열과 픽셀 좌표는 좌상단 기준 0부터, UV는 Blender 기준 좌하단 원점으로 기록합니다. 이미지 크기 W,H에서 픽셀 중심 (x,y)의 UV는 ((x+0.5)/W, 1-(y+0.5)/H)입니다. GLB 내보내기 시 좌표 변환과 실제 샘플링도 확인합니다.
원본 칸 전체의 출처와 최종 위치를 기록하고 원본/파생 파일 해시로 대응표의 버전을 고정합니다.

### inspection.json (에셋 버전별)
필수 필드: schema_version: 3, asset_id, version, kind, target_web_environment, props, scene_triangles, material_count, texture_count, palette_resolution, glb_bytes, checks, remaining_issues.
props의 각 항목은 name, triangles_per_instance, instance_count, total_triangles를 기록합니다. total_triangles는 앞의 두 수의 곱이며 장면 집계에는 모든 인스턴스와 독립 지형·부품을 중복·누락 없이 포함합니다.
개별 소품 예산에는 눈·입·장식 등 모든 부품을 합산합니다. 검수 수치는 최종 GLB를 다시 연 결과이며 측정 전 수치는 null입니다. 미검증을 0으로 기록하지 않습니다.
checks는 아래 완료 조건별로 status(pass/fail/unverified/not_applicable), evidence, reason을 기록합니다. 적용하지 않는 항목에는 사유가 필요합니다.
검수 기록에서 unverified는 사람이 읽는 보고에서 반드시 '미검증'으로 표시합니다. 초과·실패·미검증 상태에서 ready로 등록하지 않습니다.

### builds.json
루트 필드: schema_version, builds.
각 빌드의 필수 필드:
- build_id.
- project_path: unity/projects/<project>.
- output_path: unity/webgl/builds/<build_id>.
- document_path: docs/human/builds/<build_id>.md.
- artifact_url: 업로드 전 null, 업로드 후 실제 HTTPS 실행 또는 다운로드 URL.
- assets: {"asset_id": "AST-001", "version": "v001"} 형태의 참조 배열. 중복 없이 등록된 정확한 버전을 참조하며 해당 프로젝트 소속이어야 합니다.

### 에셋 분류·재사용·사용 이력 확장 (schema_version: 3 유지)

이 절은 기존 panorama_ref, occupation_groups, asset_slots, source_images, builds.assets 계약에 추가하는 선택적 메타데이터입니다. 기존 필드의 의미·형식·승인 상태는 바꾸지 않습니다. 아래 신규 목록 파일은 계약만 정의하며 실제 등록 작업이 있을 때 생성합니다. 이 문서 수정만으로 파일·항목·승인·배치·검증 상태를 만들지 않습니다.

#### 적용 시점과 공통 의미
- 기존 schema_version: 3을 유지합니다. 기존 필드 변경·삭제 없이 선택 필드와 독립 목록을 추가하므로 기존 항목은 유효하며 즉시 일괄 보완하지 않습니다. 알 수 없는 선택 필드를 거부하는 소비자는 확장 기능 사용 전에 호환성을 확인합니다.
- 신규 메타데이터를 등록하거나 해당 분류·변형·사용 이력을 다음에 수정할 때 실제 근거가 있는 부분만 적용합니다. 누락 필드는 '미등록/미확인'이며 false, 사용 없음 또는 검증 완료로 해석하지 않습니다.
- 선택 객체는 생략 가능하지만 추가하면 아래 내부 필수 필드를 모두 갖춥니다. null은 명시적으로 허용한 미정·미검증·해당 없음에만 사용합니다. 빈 배열은 해당 기록 범위에서 확인된 항목이 없음을 뜻하며 기존 누락과 구분합니다.
- 고정 참조는 원래 계약의 ID·버전을 사용합니다. 'latest'나 이름만으로 연결하지 않습니다. 예시는 모두 설명용 가상 데이터이며 실제 catalog에 넣지 않습니다.

#### assets.json의 선택 태그와 적용 후보
선택 필드 tags는 객체이며 추가하면 object_type, function, space, activity 네 필드가 필수입니다. 각 값은 중복 없는 한국어 문자열 배열이고 null은 금지합니다. object_type은 하나 이상, 나머지는 확인된 해당 항목이 없으면 []를 허용합니다.

| 필드 | 의미 | 정규 표기 예시 | 별칭 입력 → 정규 표기 |
|---|---|---|---|
| object_type | 무엇인가 | 책상, 의자, 바닥판, 바닥표면, 수납장, 모니터 | 데스크 → 책상, 체어 → 의자 |
| function | 어떤 용도인가 | 작업면제공, 착석, 수납, 공간구획, 정보표시 | 물품보관 → 수납 |
| space | 적용 가능한 공간 유형 | 사무실, 공공기관, 일반회사 | 오피스 → 사무실 |
| activity | 지원하는 활동 | 개인PC작업, 문서작성, 출력, 자료보관, 대면상담 | 서류작성 → 문서작성 |

- 허용 문자열 규칙: Unicode NFC, 앞뒤 공백 없음, 내부 공백 없이 붙인 한국어 명사·명사구. 필요한 영문 약어는 기존 표기(PC 등)를 유지합니다. 자유 문장·쉼표로 합친 여러 값·ID를 태그로 쓰지 않습니다.
- 위 표는 초기 정규 어휘와 별칭입니다. space/activity는 기존 workplace-contexts의 같은 차원에 사용된 정확한 표기도 정규 어휘로 인정합니다. 기존 interaction/visual 및 직업 분류 계약은 유지합니다.
- 등록 전에 같은 차원의 기존 값과 이 표를 검색합니다. 동의어는 정규 값으로 변환해 저장하고 별칭은 검색 입력에서만 확장합니다. 새 개념이나 별칭은 이 표에 차원·정규 값·별칭을 먼저 기록합니다. 의미가 다른 책상/테이블 등을 근거 없이 합치지 않습니다. 기존 데이터는 자동 일괄 정규화하지 않습니다.
- tags.space는 사용 가능한 유형이며 실제 사용 증거가 아닙니다. 특정 직업명·context_id·파노라마명을 자유 텍스트 태그로 복제하지 않습니다.
- 선택 applicable_contexts는 배열이며 각 항목은 context_ref({context_id, version}), reason(문자열), applicability_condition(문자열)이 필수입니다. []는 검토한 특정 후보가 없음을 뜻하며 생략은 미검토입니다. 등록된 컨텍스트만 참조하고 같은 쌍을 중복하지 않습니다. 이는 적합성 후보일 뿐 실제 배치를 뜻하지 않습니다.
- 특정 공간의 제작 계획과 수량은 기존 contexts.asset_slots에 두고 asset_ref로 연결합니다. 에셋에 직업·파노라마·공간 이름 목록을 다시 저장하지 않습니다. 여러 컨텍스트가 같은 에셋을 참조할 수 있습니다.

#### 직업 → 공간 → 기준 파노라마 연결 보완
- 직업별 공간 후보는 기존 occupation_groups.occupation_ids를 역조회합니다. mapping_basis, reason, applicability_condition과 원문 source_categories/source_status를 함께 읽습니다. 여러 직업↔여러 공간 연결을 허용하되 별도 중복 매핑을 만들지 않습니다.
- occupation_groups의 선택 verification 객체는 status(unverified/verified/rejected), evidence(근거 문자열 배열), note(문자열), checked_at(ISO 8601 일시 또는 null)를 내부 필수 필드로 갖습니다. verified/rejected에는 구체적 근거와 일시가 필요하며 unverified는 checked_at:null, evidence:[]를 허용합니다. 생략은 미검증입니다. 그룹 일부 직업만 검증됐으면 그 직업을 별도 그룹으로 구분하기 전 전체 그룹을 verified로 표시하지 않습니다.
- 이 verification은 직업·공간 관계의 사실 검증입니다. review_status는 사용자 기획 승인이고 production_status는 제작 상태입니다. 서로 대체하거나 자동 승격하지 않습니다. 기존 candidate_not_verified는 유지하고 사용자 승인만으로 직업 근무지 사실을 검증했다고 기록하지 않습니다.
- panorama_ref는 최종 공간의 형태·배치·의미 참고입니다. 신규 이미지 생성 지시, 구면 투영, 360도 배경·스카이박스 사용을 뜻하지 않습니다.
- source_images는 모델 제작에 직접 참고한 이미지입니다. 장면의 panorama_ref를 모델의 source_images로 자동 복사하지 않습니다. 직접 참고한 사실이 있을 때만 같은 이미지를 양쪽에서 참조할 수 있습니다.

#### asset-color-variants.json — 색상 변형 계약
기준 위치는 docs/machine/catalog/asset-color-variants.json, 루트는 schema_version:3, variants 배열입니다. 이번 문서 작업에서는 생성하지 않습니다.
각 항목의 내부 필수 필드:
- base_asset_ref: 기존 {asset_id, version}. 기준 형상의 고정 버전.
- variant_id: 소문자 영문·숫자·하이픈, 정규식 [a-z0-9]+(?:-[a-z0-9]+)*. (base_asset_ref, variant_id)가 유일합니다. 확정된 레시피를 바꾸면 새 variant_id를 사용합니다.
- state: planned 또는 materialized. 계획만 있으면 planned입니다.
- palette_version: 기존 palettes의 고정 버전.
- regions: 하나 이상의 객체 배열. 각 항목은 part_id(변형 내 유일한 소문자 영문·숫자·하이픈), selector(기준 Blender 파일의 오브젝트·면 그룹 등 재현 가능한 부위 선택 문자열), role(base/accent), cell_ref가 필수입니다. 하나의 면을 상충하는 부위에 중복 지정하지 않습니다.
- cell_ref: {texture_id, row, column}. variant.palette_version이 가리키는 mapping.json의 cells에서 이 세 값이 정확히 하나인 항목을 찾습니다. row/column은 기존 좌상단 0 기준 비음수 정수입니다. UV·RGB·사각형 좌표는 복제하지 않습니다. 중복 칸으로 유일하게 찾을 수 없으면 임의 선택하지 말고 별도 대응표 계약 변경을 검토합니다.
- base 역할은 color1, accent는 color2 출처 칸을 참조합니다. 미지정 부위는 기준 모델의 색을 유지합니다. 실제 사용본은 여전히 공용 PNG 한 장·공용 재질이며 UV 이동을 우선합니다.
- result_asset_ref: planned이면 null. materialized이면 실제 파일을 가진 등록된 {asset_id, version}. 기준과 같은 asset_id의 새 version이어야 합니다. 원본 source/blender/runtime 파일을 덮어쓰지 않습니다. UV만 바뀌어도 메시·GLB·Blender 저장 파일이 바뀌면 새 에셋 버전입니다. 기존 버전에 별도 variant GLB를 숨겨 등록하지 않습니다.
- 계획은 독립 레시피일 뿐 assets.json의 완료 결과물·빌드 포함 항목이 아닙니다. materialized도 기존 assets.status나 검수 상태를 자동 ready로 바꾸지 않습니다. 결과 에셋의 palette_version은 변형과 같아야 하며 검사 기록에 부위·UV 적용 결과를 남깁니다.
- 이번 계약은 저장된 변형 결과만 실제 배치에 허용합니다. 메시 파일을 저장하지 않는 런타임 UV 덮어쓰기·재질 틴트 변형은 지원하지 않습니다.
- 사용 이력의 variant_ref는 {base_asset_ref:{asset_id,version}, variant_id}이고 실제 asset_ref는 result_asset_ref입니다. 기본색 그대로면 variant_ref:null입니다. 한 장면에 기본형과 변형을 함께 배치할 수 있지만 서로 다른 실제 결과 버전으로 기록합니다.

#### asset-usages.json — 실제 사용 이력의 단일 기준
기준 위치는 docs/machine/catalog/asset-usages.json, 루트는 schema_version:3, usages 배열입니다. 이번 문서 작업에서는 생성하지 않습니다. 에셋별 사용처 목록은 이 파일을 조회하고 assets.json이나 사람용 표에 독립 원장을 만들지 않습니다.

각 항목의 내부 필수 필드:
- usage_id: use- 접두사와 소문자 영문·숫자·하이픈. revision: 1부터 증가하는 정수. (usage_id, revision)은 유일합니다. 변경 시 이전 기록을 보존하고 새 revision을 추가합니다. recorded_at은 ISO 8601 일시, change_reason은 변경 이유 문자열입니다.
- record_kind: prefab_definition 또는 scene_instances.
- placement_state: planned, placed, removed. planned는 예정, placed는 실제 Unity 정의/장면에서 확인됨, removed는 제거를 확인한 기록입니다. 에셋 제작 상태와 별개입니다.
- project_path: unity/projects/<project>. scene_path: 프로젝트 내부 .unity 경로 또는 null. prefab_path: 프로젝트 내부 .prefab 경로 또는 null. 모두 저장소 상대 경로입니다. prefab_definition은 prefab_path 필수·scene_path:null, scene_instances는 scene_path 필수·prefab_path는 미사용이면 null입니다. planned의 경로는 예정 위치임을 명시하며 존재 증거로 쓰지 않습니다.
- asset_ref: 등록된 {asset_id,version}, variant_ref: 위 변형 참조 또는 null. placed는 materialized 결과만 참조할 수 있습니다. 계획 변형은 planned 기록에서만 사용하고 그 경우 asset_ref는 base_asset_ref입니다.
- context_ref: {context_id,version} 또는 null. slot_id: 해당 context.asset_slots의 ID 또는 null. slot_id가 있으면 context_ref가 필수입니다. 컨텍스트 없는 범용 사용은 둘 다 null입니다. 슬롯의 asset_ref와 실제 변형의 기준/결과 관계도 확인합니다.
- quantity: scene_instances의 placed이면 양의 정수, planned이면 예상 양의 정수 또는 미정 null, removed이면 0. prefab_definition은 null이며 장면 수량에 포함하지 않습니다.
- instances: scene_instances의 placed이면 quantity와 같은 길이의 배열, planned이면 [] 또는 계획 배열, removed/prefab_definition이면 []. 각 항목은 instance_id(Unity GlobalObjectId 등 장면 내 안정 식별자)가 필수입니다. 계층 경로만 쓸 때에는 변경 시 새 revision에 갱신합니다. 같은 프로젝트·장면의 현재 기록들에서 동일 에셋 인스턴스를 두 번 세지 않습니다.
- 각 instance의 선택 transform은 position_m([x,y,z]), rotation_quaternion_xyzw([x,y,z,w]), scale([x,y,z]), space(world/local), parent_instance_id(문자열 또는 null)가 내부 필수입니다. Unity 좌표계·미터·정규화 쿼터니언을 사용합니다. local은 부모 식별자가 필요하며 world는 null입니다. 미기록 transform은 원점·회전 0·크기 1로 추정하지 않습니다.
- evidence: 근거 경로/식별자 문자열 배열. placed/removed에는 실제 Unity 장면·프리팹 조사 근거를 기록합니다. planned는 []를 허용합니다.
- build_links: 빌드 포함 스냅샷 객체 배열, execution_checks: 실행 검증 객체 배열. 둘 다 []는 이 revision에서 기록된 증거가 없다는 뜻이며 '미포함/실행 실패'로 단정하지 않습니다.

집계와 상태 분리:
- 현재 사용처는 usage_id별 최신 revision만 조회합니다. 과거 revision은 이력이며 현재 수량에 더하지 않습니다. planned/removed 및 prefab_definition은 실제 장면 삼각형 합계에서 제외합니다.
- scene_instances만 실제 장면 수량으로 집계합니다. 프리팹 내부 자식·중첩 프리팹이 장면에 펼쳐진 인스턴스는 한 번만 기록합니다. 조립 에셋과 그 구성 에셋을 같은 집계에 중복 포함하지 않으며 조립 단위 또는 구성 단위 중 선택한 기준을 근거에 명시합니다.
- 삼각형은 사용한 실제 결과 에셋의 최종 GLB 검수값 × 실제 quantity로 계산합니다. 측정값이 없으면 합계를 미검증으로 표시합니다. 프리팹 정의 수량을 배치 횟수처럼 더하지 않습니다.
- 동일 에셋 버전 다중 프로젝트 미지원은 유지합니다. placed 기록의 project_path는 asset.unity_path 소속 프로젝트와 같아야 합니다. unity_path:null이면 planned만 가능합니다. 변형 결과도 결과 에셋의 unity_path와 대조합니다. 기존에 프로젝트가 정해진 에셋 버전을 다른 프로젝트에 실제 등록하지 않습니다. 다른 프로젝트 후보가 생기면 별도 명시적 지원 변경을 먼저 검토합니다. 여러 공간 공유는 한 프로젝트 내 여러 장면·컨텍스트 공유를 뜻할 수 있으며 다중 프로젝트 허가가 아닙니다.
- build_links 항목은 build_id, scene_path, quantity, instance_ids, evidence가 필수입니다. revision 내 실제 배치의 고정 스냅샷이며 포함된 부분집합만 기록할 수 있습니다. quantity는 instance_ids 길이와 같은 양의 정수이고 해당 revision의 instances에 모두 존재해야 합니다. 같은 build_id·scene_path·instance_id를 중복 집계하지 않습니다.
- build_links는 scene_instances의 placed 기록에 실제 빌드 포함을 확인한 경우만 추가합니다. builds.assets의 실제 asset_id/version 및 project_path와 반드시 일치합니다. builds.assets는 기존 집합 참조를 유지하며 수량·변형 메타데이터를 중복 정의하지 않습니다. included는 실행 성공을 뜻하지 않습니다. 이후 장면 변경·제거 시 과거 revision과 빌드 스냅샷은 보존합니다.
- execution_checks 항목은 target(editor_scene/build), build_id(build이면 기존 build_links의 ID, editor_scene이면 null), status(unverified/pass/fail), checked_at(ISO 8601 또는 null), environment(문자열), evidence(문자열 배열), note(문자열)가 필수입니다. pass/fail은 실행 근거와 일시가 필요합니다. unverified는 checked_at:null·evidence:[]를 허용합니다. 확인한 revision의 배치/빌드에만 귀속되며 새 revision에 성공 결과를 자동 승계하지 않습니다. 일반 GLB 뷰어 실행을 Unity WebGL 빌드 검증으로 기록하지 않습니다.

#### 설명용 가상 예시 (실제 catalog에 등록 금지)
가상 책상 에셋 AST-900 v001의 tags는 {"object_type":["책상"],"function":["작업면제공"],"space":["사무실"],"activity":["문서작성"]}처럼 표현합니다. 특정 공간은 tags가 아니라 applicable_contexts의 context_ref로 연결합니다.
색상 변형 mint-top은 기준 AST-900 v001, 팔레트 v009의 cell_ref {"texture_id":"color1","row":3,"column":5}를 상판 부위에 적용하는 레시피입니다. planned이면 result_asset_ref:null, 실제 UV 변경 파일을 등록했다면 예를 들어 AST-900 v002를 result_asset_ref로 참조합니다. 이 ID·버전·색상 칸은 설명용이며 실재 여부나 적합성을 주장하지 않습니다.
프리팹 정의 1건과 그 프리팹을 사용한 장면 인스턴스 4개가 있으면 실제 배치 수량은 4이며 5가 아닙니다. 사용 예정 4개, 실제 배치 4개, 빌드 포함 4개, 실행 검증 통과는 각각 근거가 다른 기록입니다.

### 파노라마 기반 직업체험·상호작용 명세
- 파노라마 기준으로 필요한 에셋을 공통·비공통으로 명세하고 해당 공간의 형태·배치·의미에 맞게 장면을 구성한다. 직업체험은 그 장소 안에서 직업별 업무·핵심역량에 근거한 상호작용으로 수행한다. 동일 장소·형상은 재사용하며, 시나리오를 장소와 무관한 별도 물건 목록으로 관리하지 않는다.
- 직업은 기존 occupation catalog만 기준으로 한다. 원본 업무·역량과 게임용 각색을 구별한다. 원본의 설명·준비방법을 실제 근무지 검증이나 자격·능력 판정으로 승격하지 않는다.
- 한 미션은 상호작용 물건 3개와 연결된 업무 흐름을 갖는다. 여러 단계에서 같은 물건을 다시 사용할 수 있다. 배경 물건·화면 UI와 조작 물건을 구별하되 배경까지 장면 예산에 포함한다.
- 전체 고정 공간 후보에서 서로 다른 prompt_id/version 2개 이상에 연결된 후보를 common, 1개를 noncommon으로 파생 분류한다. 분류는 특정 목록 버전과 계산 근거를 고정하며 실제 사용 원장을 대체하지 않는다. 전체 적용 공간 이름·ID·버전은 기존 full_scene_candidates로 빠짐없이 조회한다.
- career-minigame-types-vNNN.json: schema_version:3, package_id, version, planning_status, document_path, counts, types. types는 고유 type_id/version, kind(core/special_modifier), name, implementation_status, input_description, player_action, success_rule, recovery_rule, required_configuration_fields, states, events, accessibility, asset_policy를 포함한다. MG-001~010은 공통 유형, EX-001~010은 특수 상황 분기이며 모든 직업에 20종 전부를 강제하지 않는다. 명세 작성은 구현 완료가 아니다.
- career-experience-scenarios-vNNN.json: schema_version:3, package_id, version, document_path, source_refs(path/sha256), scope, scenarios, remaining_occupation_ids, usage_measurement. scenarios는 scenario_id/version, occupation_id/name, title, planning_status, production_status, implementation_status, runtime_checks, document_path, implementation_prompt_path, original_ref(path/sha256/json_pointer), source_basis, fictionalization, panorama_ref, prompt_ref, context_ref(미등록이면 null), scene_basis_ref(없으면 null), interaction_objects(정확히 3개), base_game_refs, steps, special_variants, feedback, acceptance_cases, actual_usage_refs, actual_usage_status를 포함한다. 추가 시나리오 데이터 필드는 명세에 설명한다.
- interaction_objects는 object_id(시나리오 내 유일), candidate_ref(기존 고정 catalog/candidate_id), name, asset_reuse_ref(기존 asset_id/version 또는 null), reuse_fit_status, reuse_class, scene_candidate_count, binding_status, unity_binding(미정 null), requirements, mesh_animation_requirement를 포함한다. 재사용 참조는 실제 배치를 뜻하지 않으며 동작·분리 부품·콜라이더·상태 표현을 확인한다. 실제 파일 변경은 기존 버전 보존 규칙을 따른다.
- steps는 step_id, object_id, type_refs, action, from_state, to_state, success_predicate, on_error, configuration을 포함한다. special_variants에는 type_id/version, mode, trigger, required_outcome을 기록한다. 단계·분기의 상태, 입력, 정답 데이터, 선행 조건, 중복 입력 방지와 초기화를 구체화한다. 성공·오류 조건을 미정 문구만으로 채워 구현 완료로 표시하지 않는다.
- panorama-career-experience-layouts-vNNN.json: schema_version:3, package_id, version, document_path, source_refs, classification_basis, scenes. scenes는 prompt_ref, panorama_ref, name, common_asset_candidates, noncommon_asset_candidates, scenario_refs, scenario_coverage, implementation_status를 포함한다. 후보 항목은 candidate_ref, name, reuse_class, full_scene_candidates, asset_ref(미정 null), quantity(미정 null), placement_state:planning_only를 기록한다. 파생 명세의 제작 전 null은 기존 실물 모델이 없다는 단정이 아니다.
- 전체 시나리오 확장 시 source_basis.selected_work_evidence는 원본의 완전한 업무 문장을 보존하고, scene_selection은 method, relation_to_existing_mapping, reason, original_mapping_ref, verification_status로 기존 명시 연결·분류 안 제안·분류 밖 제안을 구별한다. review_status/review_issues 및 problem_data_level로 초안·전문 검토·공통 엔진 연습 데이터의 한계를 명시한다. 실제 전문 정답이나 구현 상태를 자동 확정하지 않는다.
- 미선택 주제가 있는 시나리오는 selection_status:needs_subject_selection, selected_scene_option:null과 scene_options를 기록한다. 각 대안은 고정 prompt_ref/panorama_ref, 정확히 3개의 interaction_objects, steps, base_game_refs, special_variants를 갖는다. 기본 필드의 첫 대안은 미리보기일 뿐 선택·실제 배치를 뜻하지 않는다.
- 공간 역조회 확장 필드 scenario_specific_asset_additions는 기존 필수 후보 밖의 추가 제안이며 원본 후보 목록 자동 갱신이 아니다. interaction_object_reverse_index는 후보별 기존 전체 공간과 모든 시나리오·미선택 대안의 참조를 빠짐없이 제공하며 실제 사용 원장이 아니다. 버전 갱신은 supersedes로 연결하고 과거 명세를 보존한다.
- 계획 승인·모델 제작·시나리오 구현·실제 배치·Unity/WebGL 실행 검증은 각각 구분한다. 기존 actual usages와 assemblies를 참조하고 새로운 상호작용 사용을 근거 없이 placed로 등록하지 않는다. 미구현 유형·시나리오는 명시하며 전체 직업 완료를 주장하지 않는다.

### 물건 확대·직접 작업형 직업체험 — 필수 동작과 명세 계약

#### 적용 범위와 기준 사례
- 직업체험은 **실제 3D 물건 선택 → 부드러운 확대 → 물건에 맞는 작업 화면에서 직접 조작 → 즉시 결과 표시 → 원래 공간으로 복귀 → 다음 물건에서 업무 계속** 흐름으로 설계한다. 파노라마는 공간 구성 기준이며, 평면 그림 위 버튼만으로 완료하는 화면을 실제 3D 체험으로 간주하지 않는다.
- 작업 시작 시 등록된 모든 시나리오 패키지의 ID·버전·상태를 대조해 기존 작성 범위를 확정한다. 중복 시나리오는 최신 설계와 실제 구현 기록을 구별하여 조회한다. 직업 catalog에 있다는 사실만으로 시나리오가 작성됐다고 간주하지 않는다. 기존 작성 시나리오의 설계를 먼저 수정하고, 새 직업의 대량 생성·구현은 수정 기준과 대표 사례를 사용자에게 보여준 뒤 명시적으로 요청된 범위에서 진행한다.
- 기준 사례는 office-assistant-v005의 실제 물건 확대·종이 팝업이다. docs/human/builds/office-assistant-v005.md, 해당 Unity 소스·시나리오 데이터·사용 이력·실행 근거를 직접 확인한다. 이 사례의 확대·복귀를 재사용하되, 기존 선택지 버튼 조작까지 모든 직업의 완성 기준으로 복제하지 않는다. 새로 요구되는 필드 편집·드래그 등의 미구현 동작과 기존 검증 범위를 분리한다.
- 물건의 사용 방식이 느껴지는 작업을 우선한다. 단순히 설명을 읽고 '정답 선택/완료' 버튼을 누르는 것으로 문서 편집·조립·측정·분류를 대신하지 않는다. 질문 선택·요청 전송·저장·인쇄·확정처럼 실제 업무에서 의미가 있는 버튼은 허용한다. 같은 조작 틀을 재사용해도 직업별 업무 자료·도구 역할·판정 근거가 달라야 한다.

#### 선택·확대·복귀의 정확한 동작
- 실제 에셋의 콜라이더 또는 검증된 선택 영역을 클릭·터치해 물건을 선택한다. 카메라 드래그와 선택을 포인터 누름·이동·놓음으로 구별한다. 기본 이동 임계값은 표시 좌표 기준 8px이며 확대율·기기에 맞춰 설정 가능하게 한다. 임계값을 넘은 드래그의 놓음으로 물건이 열리지 않아야 한다.
- 확대 전에 카메라 위치·회전·FOV 또는 직교 크기·뷰포트, 입력 모드, 배경 렌더러별 표시 상태와 선택 초점을 저장한다. 확대는 기본 0.45초, ease-in-out 보간으로 수행하고 값은 데이터로 조정한다. 선택 물건의 실제 bounds와 작업 면을 기준으로 프레이밍하며, 모든 물건에 같은 월드 좌표나 각도를 적용하지 않는다. 확대 중 중복 선택·다른 물건 열기를 잠그고, 모션 감소 설정에서는 즉시 전환할 수 있게 한다.
- 확대 시점은 물건마다 정한다. 문서·모니터·기기 패널은 읽고 조작할 면을 정면에서, 트레이·조립대·분류함은 작업 면과 투입 위치가 보이는 시점에서 보여준다. 선택 물건을 복제하거나 원본 메시·재질·색을 바꿔 확대를 흉내 내지 않는다. 배경을 숨기거나 어둡게 할 경우 처리 방식과 원래 상태 복원을 명시한다.
- 작업 화면이 열린 동안 뒤쪽 공간의 선택·회전·줌 입력을 차단한다. 화면 밖으로 나간 포인터·취소된 터치·다중 터치·앱 초점 상실 시 진행 중 제스처만 취소하고 유효하지 않은 드롭이나 완료 이벤트를 발생시키지 않는다.
- 닫기와 Esc는 작업 화면을 닫고 저장한 카메라·뷰포트·배경 표시 상태로 부드럽게 복귀시킨다. 카메라를 기본 시작 위치로 초기화하지 않는다. 기존 메시가 사라지거나 이전 프레임 잔상이 남지 않도록 전체 화면 지우기·뷰포트 복원을 실제 화면으로 확인한다.
- 닫기는 작업 취소·단계 초기화·세션 초기화가 아니다. 입력 중인 문서 초안, 미저장 표시, 선택한 파일·revision·부수, 분류 진행, 질문·응답·인계 내용과 단계 상태를 세션에 유지하고 다시 열면 같은 작업 위치를 복원한다. 조작 중이던 드래그의 임시 그림자만 취소한다. 저장된 업무 결과와 미저장 초안은 구분한다.
- 출력 같은 비동기 작업은 화면을 닫아도 한 번 시작한 작업을 계속하되, 일시정지 시에는 진행 시간을 멈춘다. 같은 작업의 완료는 한 번만 처리한다. 화면을 다시 열었다고 출력·타이머를 재시작하거나 완료 수량을 늘리지 않는다. 다른 비동기 작업도 닫힘·일시정지 정책을 명세한다.

#### 물건별 작업 화면과 직접 조작
- 모니터: 받은 메시지와 대화를 열어 누락 요청을 질문하고 요약 확인한다. 문서는 제목·날짜·내용 등 편집할 필드를 실제 문서 형태로 표시하고, 플레이어가 해당 필드를 선택해 수정·저장한다. 요청 원문과 비교하고 미저장·저장 revision 및 오류 위치를 표시한다. 날짜의 정답을 고르는 두 버튼만으로 문서 편집을 대체하지 않는다.
- 복합기: 기기 패널에서 문서·버전 목록, 부수 입력·증감, 미리보기를 조작하고 인쇄한다. 최신 요청·저장본과 대조한 뒤 시작하며, 작업 중 설정·중복 인쇄를 잠근다. 진행률과 요청 부수의 용지가 나오는 UI, 완료된 묶음을 즉시 보여준다. 용지는 해당 기기의 UI이며 별도 네 번째 3D 조작 물건이 아니다.
- 수납장: 문서 묶음과 읽을 수 있는 분류함을 표시한다. 묶음을 알맞은 칸에 드롭하거나 같은 의미의 선택·이동 조작으로 보관한다. 오분류는 확정하지 않고 되돌림·이유를 보여준다. 보관 후 묶음의 위치·라벨·수량을 표시하고 결과·보관처를 인계한다. 단순한 '정답 칸' 버튼 선택만으로 분류를 완료하지 않는다.
- 관찰·검사: 물체·문서의 회전·확대·비교·검사 지점 표시·필드 수정 중 대상에 적합한 조작을 제공한다. 분류·선별: 직접 옮길 물품과 구분할 칸을 제공한다. 순서·절차: 물품·도구를 사용하는 단계나 순서 카드를 직접 배열한다. 측정·조절: 눈금·다이얼·슬라이더·계기 값을 조절한다. 조립·배치: 부품을 결합점에 이동·회전·스냅한다.
- 진단·해결은 단서와 가설·대응을 연결하고, 제작·표현은 문서·타임라인·구성판·작품 면에서 결과를 편집하며, 계획·배분은 일정·자원 칸에 항목을 배치한다. 타이밍·추적은 신호와 입력·경로를 연결한다. 대화·응대는 상황에 맞는 질문·응답·요약 확인으로 구현한다. 모듈 이름만 붙이고 동일한 버튼 퀴즈를 모든 물건에 적용하지 않는다.
- 드래그가 적합한 작업에는 드래그를 제공하고 클릭/터치로 항목 선택 후 목적지 선택, 키보드 초점 이동·Enter/Space 확정·Esc 취소 등 동등한 대체 조작을 제공한다. 드래그·대체 조작은 같은 업무 명령·판정 함수를 호출하고 정답·제약·피드백이 같아야 한다. 색·소리만으로 상태를 구별하지 않는다. 입력 필드에 타이핑하는 P/R/숫자/화살표를 전역 단축키로 오인하지 않도록 입력 초점을 처리한다.

#### 시나리오·단계의 필수 추가 명세
- 기존 schema_version:3과 ID를 유지한다. 새 설계는 패키지·변경 시나리오 버전을 올려 보존하고 supersedes 또는 이전 항목 참조로 연결한다. 기존 항목을 근거 없이 일괄 보완하거나 구현·검증 상태를 승격하지 않는다. 아래 선택 확장은 신규/수정하는 직접 작업형 설계에서는 모두 작성하며, 기존 누락은 '아직 이 기준으로 명세하지 않음'이다.
- 시나리오에 interaction_flow를 추가한다. 내부 필수 필드는 mode(object_closeup_direct_work), view_states, transition_seconds, easing, drag_threshold_px, reduced_motion, camera_restore_fields, input_lock_policy, close_policy, pause_policy, reset_policy, persistence_scope다. view_states는 exploring/focusing/working/returning/paused를 구별하며 업무 단계 상태와 별도로 관리한다. persistence_scope는 최소 session을 명시한다. 앱 재실행·새로고침까지 보존을 구현하지 않았다면 이를 지원한다고 기록하지 않는다.
- 각 interaction_objects 항목에 closeup을 추가한다. 내부 필수 필드는 asset_ref(실제 ID·버전 또는 미연결 null), binding_status, work_face, camera_preset, framing, background_policy, restore_policy, calibration_status다. 기계·문서 UI만 있어 실제 에셋이 없으면 미연결 사유를 기록한다. 계산·실측하지 않은 카메라 좌표·bounds·콜라이더를 실측값으로 등록하지 않는다. camera_preset과 framing은 설계값이며 실제 Unity 바인딩 검증과 구별한다.
- 각 steps 항목에 work_surface를 추가한다. 내부 필수 필드는 surface_kind, layout, controls, manipulands, initial_data, target_data, prerequisites, commands, success_rules, error_feedback, retry_policy, visual_result, draft_persistence, next_object, request_change, handoff, reset, implementation_status, verification다. 기존 object_id·type_refs·상태·판정과 모순되지 않게 연결한다. 해당 없음인 객체는 null과 구체적인 사유를 남기며 아무 설명 없는 빈 객체로 대체하지 않는다.
- controls는 control_id, kind, data_binding, pointer_action, touch_action, keyboard_action, command를 갖는 배열이다. manipulands는 직접 조작하는 항목의 ID·표시 내용·허용 목적지/조절 범위/결합점 등을 기록한다. commands는 이름·입력 payload·선행 조건·업무 상태 변화·중복 방지 키를 정의한다. 화면 표현은 명령을 전달하고, 상태·판정 코드는 정답·원본 데이터와 분리한다. 판정식 문자열을 임의 코드 실행으로 평가하지 않는다.
- initial_data와 target_data에는 실제 가상 요청·문서 내용·초깃값·정답 값·분류 규칙·허용 오차를 재현할 수 있게 기록한다. 단순 A/B·0~100 같은 엔진 연습 데이터만 있으면 engine_fixture_only로 표시하고 직업별 문제 데이터 완성으로 간주하지 않는다. 원본의 업무·역량 근거와 게임용 수치·대화·정답은 구별한다.
- success_rules는 제출값·현재 요청 revision·문서 저장 revision·선행 단계·단위/허용 범위·완료 횟수 등 적용 조건을 정확히 명시한다. error_feedback에는 잘못된 조작별 메시지·원위치 복귀/수정 유지·상태 불변 여부를 기록한다. visual_result에는 저장 표시·출력 용지·분류함 안 묶음·스냅 결합·변경된 계기 등 성공 직후 눈으로 확인할 결과를 적는다. 설명문이나 버튼 라벨 변화만으로 모든 결과를 대신하지 않는다.
- next_object는 다음 업무와 물건, 열림 조건, 이전 완료 물건의 재열기 허용·읽기 전용 정책을 명시한다. 완료 물건을 다시 열어도 업무 상태·수량이 바뀌거나 보상이 중복되지 않는다. request_change는 변경 필드·발생 시점·revision 증가·무효화되는 확인/저장/출력 결과·재확인 경로를 정한다. handoff는 전달할 필드·상대 확인·오류 복구를 정한다.
- reset은 확인 후 초안·진행·출력·분류·인계·일시정지·UI 초점·카메라 상태를 일관되게 초기화한다. 세션 generation 또는 취소 토큰으로 이전 세션의 비동기 완료·전환 콜백을 무효화한다. 닫기·재시도·전체 초기화를 서로 다른 동작으로 구현하고 기록한다.

#### 구현·기록·검증의 경계
- 판정·상태 코드, 시나리오 데이터, 물건별 화면 표현을 분리한다. 공통 미니게임 10종·특수 상황 10종은 재사용 설계 목록이며 해당 시나리오에 필요한 모듈만 적용한다. 특수 분기도 동일한 물건 3개와 UI를 재사용한다. 하나의 사례가 통과해도 다른 직업·유형·미구현 분기에 pass를 승계하지 않는다.
- 문서·용지·대화·기기 패널·분류함 표현은 해당 물건에 귀속된 UI로 제공한다. 별도 NPC·네 번째 조작 물건을 임의로 추가하지 않는다. 기존 모델·배치·스크립트와 공용 PNG 한 장·공용 재질을 우선 재사용한다. 문서 글자를 모델용 이미지 텍스처에 굽지 않는다. 이 직접 작업형 전환 범위에서는 유료 Meshy·이미지 생성 호출을 하지 않는다.
- 대표 사례 검수는 실제 Unity와 HTTP에서 실행한 WebGL로 수행한다. 3D 표면 선택/키보드 대체, 확대·원래 카메라/배경 복귀, 팝업 닫기, 카메라 드래그와 선택 구별, 미저장 초안과 설정의 닫기·재열기 유지, 단계 잠금, 잘못된 물건 선택, 드래그·동등 대체 조작, 오답·재시도, 중복 입력, 출력 중 닫기·일시정지·초기화, 요청 변경, 인계, 완료 후 재클릭을 확인한다. 확대·복귀 중 입력·터치 취소·작은 화면의 잘림·잔상도 검수한다.
- 각 검수 항목은 구현 여부, 실행 환경·일시·대상 빌드·근거, pass/fail/미검증을 구별한다. 소스 조사·기존 v005 실행 기록·정적 명세 검토·이번 실제 실행을 구별한다. 기존 구현을 참고했다는 이유로 새 직접 조작 기능을 구현 완료로 보고하지 않는다.
- 실제 바뀐 범위에 맞춰 catalog·사람용 문서·사용 이력·빌드·전달 문서를 함께 갱신한다. 지침/설계만 바꿨을 때 가짜 배치·새 빌드·실행 성공·ZIP을 등록하지 않는다. 실제 구현·전달 단계에서는 기존 모델·빌드·ZIP을 덮어쓰지 않고 고유 버전으로 보존하며 실행 가능한 WebGL ZIP과 실행 안내·manifest를 제공한다.

## 5. Unity와 WebGL 전달
- Unity 프로젝트는 unity/projects/, WebGL 출력은 unity/webgl/builds/로 분리합니다.
- Unity 프로젝트의 Assets/, Packages/, ProjectSettings/ 및 .meta 파일을 관리합니다.
- 빌드 설명에 목적, Unity 버전, 소스 커밋, 날짜, 포함 에셋 설명, 외부 의존성과 서버 설정을 기록합니다.
- 전달 파일은 unity/webgl/packages/<build_id>.zip. 기존 ZIP을 덮어쓰지 않습니다.
- ZIP의 site/에 WebGL 출력 전체를 상대 경로 그대로 넣습니다.
- manifest.json에는 schema_version: 3, build(빌드 항목), assets(참조를 해소한 에셋 배열), palettes(실제 참조한 최종 팔레트 메타데이터 배열)를 기록합니다.
- BUILD.md에 해당 빌드 설명, README.md에 실행 안내를 넣습니다.
- Unity 프로젝트와 Meshy·Blender 원본은 ZIP에 넣지 않습니다.
- WebGL은 웹 서버에서 실행 확인합니다. index.html 더블클릭만으로 검증하지 않습니다.
- 로컬 빌드와 ZIP은 Git에서 제외합니다.

### Unity ↔ React 공통 응답·과정·결과·해석 컨텍스트 규격 v001

#### 적용 범위와 구현 상태

- 앞으로 새로 작성하거나 수정하는 모든 직업체험 시나리오와 Unity/WebGL 구현은 이 공통 규격을 적용한다. 통합 빌드·여러 장면·여러 물건도 같은 이벤트 이름과 봉투 형식을 사용하고 작업별 차이는 `data`에 둔다. 규칙의 기준은 이 AGENTS.md이며 별도 규칙 폴더·자동 훅·검사 스크립트를 만들지 않는다.
- 규격 정의, Unity 송신 구현, React 수신 구현, 실제 통합 실행 검증은 서로 다른 상태다. 기존 빌드에 소급하여 연동 완료를 표시하거나, `window.officeState` 같은 진단 스냅샷을 공통 결과 이벤트 구현으로 간주하지 않는다. 이번 지침 추가 자체는 기존 게임·빌드·catalog의 구현/실행 상태를 변경하지 않는다.
- 런타임 이벤트는 UTF-8 JSON과 아래 camelCase 필드를 사용한다. `schemaVersion:1`은 **통신 봉투의 버전**이며 catalog의 `schema_version:3`을 대체하지 않는다. 이벤트를 저장소 JSON 파일로 보존할 때에는 `{ "schema_version": 3, "protocol": "career-experience", "protocolVersion": "v001", "events": [] }` 봉투 안에 원본 이벤트를 넣는다. 버전 불일치는 명시적으로 처리하고 누락 필드를 추정으로 채우지 않는다.

#### 프론트 방별 호출·체험 종료 응답 프로필

- 프론트의 기본 연동은 `start_experience`로 방별 체험을 시작하고 `end_experience`를 호출하면 `experience.ended`로 그동안의 과정·결과·해석 컨텍스트를 묶어 받는 방식이다. 개별 행동 이벤트는 Unity 내부 원장에 보존하며 프론트가 실시간으로 모든 행동을 구독해야만 종료 응답을 받을 수 있게 만들지 않는다. 신규·수정 구현에서는 아래 실시간 전달 프로필 v002를 필수로 적용한다. 수신자가 실시간 구독을 하지 않아도 종료 요약은 독립적으로 받을 수 있어야 한다.
- 호출 JSON의 공통 필수 필드는 `schemaVersion:1`, `protocol:career-experience`, `requestId`, `action`, `sessionId`, `experienceId`, `roomId`다. 시작 호출에는 `scenarioId`, `scenarioVersion`, 종료 호출에는 `reason:USER_REQUESTED_END`를 추가한다. reason은 사용자의 종료 요청 의도이며 완료/중단 판정을 프론트가 강제로 지정하는 값이 아니다.
- `roomId`는 프론트가 구별하는 논리 방 ID이며 기존 sceneId와의 고정 매핑을 명세한다. 한 방에 여러 시나리오가 있으면 시작 요청의 scenarioId/version으로 선택하며 임의로 첫 시나리오를 실행하지 않는다. 알 수 없는 방·시나리오 또는 실제 실행과 다른 roomId/experienceId의 요청은 명시적인 제어 오류로 처리하고 다른 체험에 적용하지 않는다.
- `experienceId`는 방을 새로 열어 체험을 시작할 때마다 프론트가 생성하는 고유 실행 묶음 ID다. sessionId는 통합 플레이 동안 유지한다. 같은 방을 다시 시작하면 새 experienceId를 사용한다. 내부 전체 초기화는 같은 experienceId 안에서 새 scenarioRunId로 구별하며 이전 run 이력을 보존한다.
- 프론트 프로필의 응답은 기존 공통 이벤트 봉투에 `roomId`, `experienceId`, `requestId`를 필수로 추가한다. 응답의 requestId는 처리한 호출의 ID이며 시작 준비가 끝났을 때 `experience.started`, 종료 처리가 확정됐을 때 `experience.ended`로 응답한다. 내부 자동 행동 이벤트에서 직접 대응하는 호출이 없으면 requestId null을 허용한다. 기존 내부 이벤트 예시는 이 추가 프로필 없이도 유효하다.
- `experience.ended`의 type은 정상 완료·중도 종료·최종 실패 모두 동일하다. 실제 업무 완료 조건에 따라 result.outcome을 completed/aborted/failed로 결정하며, 종료 버튼을 눌렀다는 이유만으로 이미 완료한 업무를 aborted로 바꾸지 않는다. 중도 종료의 partialResults와 context.termination은 아래 기준을 그대로 따른다. 시작/제어 오류 응답은 `experience.error`로 구별하며 오류를 업무 실수나 완료 결과로 집계하지 않는다. 제어 오류 봉투는 schemaVersion/protocol/requestId/sessionId/experienceId/roomId/type 및 `error:{code,message}`를 사용한다.
- 하나의 experience는 선택한 시나리오의 현재 run 종료 요약을 기본 process/result/context로 반환한다. 같은 experience에서 초기화한 과거 run은 선택 확장 `data.previousRuns`에 분리해 보존하며 최종 run과 횟수를 합산하지 않는다. 해당 범위의 근거 원본 이벤트를 부모 응답 자신을 제외한 `data.events` 배열로 함께 전달할 수 있다. events는 시간순 원장의 조회 결과이며 새 행동으로 다시 집계하지 않는다. 전량 전달 여부는 `data.eventsComplete`로 명시하고, 근거 이벤트가 생략되면 실제 구현한 보존/조회 경로를 전달 문서에 적는다. 종료 응답만 있어도 카운트·결과·해석은 읽을 수 있어야 한다.
- 같은 requestId의 전달 재시도는 같은 응답과 eventId로 처리한다. 종료 확정은 experienceId당 한 번이며 새 requestId로 이미 끝난 experience를 다시 종료하려 하면 `ALREADY_ENDED` 제어 오류와 원본 종료 eventId를 안내하고 새 업무 결과·카운트를 만들지 않는다. React는 roomId/experienceId/requestId를 확인해 해당 호출에 연결하고 eventId로 중복을 제거한다. 종료 응답을 수신·보존한 다음 Unity 화면을 제거한다. 수신 전 제거·타임아웃·강제 종료는 정상 응답을 받은 것처럼 꾸미지 않는다.
- 프론트 전달 ZIP은 실행 WebGL ZIP과 구별한 명세·타입·가상 예시 패키지로 만들 수 있다. 규칙의 원본은 이 AGENTS.md이며 전달 문서는 해당 절에서 생성한 버전 고정 스냅샷임을 명시한다. 기준 출처와 해시·미구현 상태를 남기고 독립 규칙 원장으로 수정하지 않는다. 스냅샷을 갱신할 때 새 패키지 버전을 사용한다. 명세 전달만으로 Unity 브리지·React 연동·종료 결과 수신의 실행 pass를 등록하지 않는다.

#### 실시간 전달·고정 ID 레지스트리 프로필 v002

- 신규·수정 시나리오는 상태 확정 시 공통 봉투 그대로 실시간 발행한다. 선택/열기/닫기/뒤로가기, 제출/오류/재시도, 요청 변경, 도움, 실제 완료, 일시정지/복귀/초기화/중단을 기존 고정 type으로 전송한다. 종료 응답도 유지한다. 프레임·키 입력마다 업무 이벤트를 만들지 않는다.
- process는 해당 범위의 현재 누적 스냅샷이다. 백엔드와 React는 이를 더하지 않고 범위(sessionId, experienceId, scenarioRunId, process.scope, interaction이면 stepId/objectId/workItemId)별 최신 sequence로 갱신한다. 원본 이벤트는 별도로 보존한다.
- 진행 중 result는 pending, success/completionCode는 null이며 context는 pending이다. interaction 완료는 해당 작업만 평가할 수 있으나 scenario 전체 평가는 scenario terminal 상태에서만 확정한다. 정상 진행을 TASK_INCOMPLETE로 표시하지 않는다. 종료·중단 자체는 실수에 가산하지 않는다.
- 상태 전이 이벤트는 전이 확정 직후 발행하고 지연된 네트워크 저장과 구별한다. interaction.progress는 변경된 진행률/상태만 최대 초당 5회로 합칠 수 있다. 오류·완료·중단·revision 변경 이벤트는 합치거나 버리지 않는다. 밀리초 단위 도착 보장은 하지 않는다.
- 프론트는 시작 호출 전에 career-experience:event 리스너를 등록한다. 이벤트에 대응 호출이 없으면 requestId:null이다. 동일 페이지 CustomEvent와 iframe의 origin/source 검증 규칙은 기존 규격을 따른다. 백엔드 전송 성공은 별도 저장 ACK이며 Unity 이벤트 발생 자체를 서버 저장 완료로 간주하지 않는다.
- 재전송은 원본 eventId/sequence/occurredAt/내용을 유지한다. 수신자는 (sessionId,eventId)로 중복 제거하며 같은 ID의 다른 내용은 충돌 오류로 보존한다. 순서 역전 이벤트도 원장에 저장하되 오래된 스냅샷으로 최신 상태를 덮지 않는다. 누락은 누락으로 기록하고 종료 data.events와 대조한다. 미구현 replay/ACK API를 지원한다고 명세하지 않는다.
- 고정 식별자는 docs/machine/catalog/career-integration-registry-v001.json의 버전 고정 참조를 따른다. roomId/scenarioId/scenarioVersion/occupationId를 정확히 대조한다. experienceId는 프론트가 생성하는 실행 ID이므로 고정 직업 목록에 넣거나 재사용하지 않는다. 예시 office를 실제 PAN-001 별칭으로 자동 수용하지 않는다.
- 레지스트리의 공간 존재·설계 시나리오·소스 실행 설정·특정 빌드 실행 검증은 별개다. 배포는 검증한 buildId+roomId+scenarioId+scenarioVersion 허용 목록으로 선택한다. 알 수 없는 ID/버전, 선택 미정 대안, 미지원 빌드는 명시적 오류로 거부한다. 최신 파일명만으로 모든 시나리오가 한 빌드에서 지원된다고 추정하지 않는다.
- 전달물은 JSON 규격·ID 목록·가상 예시와 사람용 안내를 함께 갱신하고 새 ZIP 버전으로 보존한다. 이번 명세 변경만으로 기존 Unity 코드·빌드·실시간 통신 실행 상태를 승격하지 않는다.

#### 공통 이벤트 봉투

아래 필드는 모든 이벤트에서 유지한다. null은 해당 없음 또는 명시된 미측정에만 사용하며 해당 사유를 남긴다.

| 필드 | 계약 |
|---|---|
| `schemaVersion`, `protocol` | 각각 `1`, `career-experience`로 고정한다. |
| `eventId`, `sequence`, `occurredAt` | 이벤트 고유 ID, session 내 1부터 증가하는 정수 순번, 시간대가 포함된 ISO 8601 발생 시각. 재전송 시 세 값과 내용이 바뀌지 않는다. |
| `sessionId`, `scenarioRunId` | 통합 플레이 세션 ID와 시나리오 한 번의 실행 ID. 장면 전환·팝업 닫기는 session을 초기화하지 않는다. 전체 재시작은 새 scenarioRunId로 시작하고 이전 기록을 보존한다. |
| `buildId`, `sceneId`, `scenarioId`, `scenarioVersion` | 실제 빌드 ID, 명세에 고정한 논리 장면 ID, 시나리오 ID·고정 버전. 에셋 ID를 장면 ID로 사용하지 않는다. |
| `objectId`, `instanceId`, `assetId`, `assetVersion` | 논리 물건 ID, 실제 장면 인스턴스 식별자, 실제 에셋 ID·버전. 같은 에셋의 반복 배치를 구별한다. 물건에 귀속되지 않는 장면/시나리오 이벤트에서는 네 값 모두 null을 허용한다. |
| `stepId`, `workItemId`, `attemptId` | 업무 단계 ID, 처리할 문서/부품 등 작업 항목 ID, 실제 제출 시도 ID. 해당 없는 선택·장면 이벤트는 null을 허용한다. 새 제출은 새 attemptId이며 전달 재시도는 같은 ID다. |
| `requestRevision`, `documentRevision` | 해당 시나리오의 실제 요청·문서 revision. 사용하지 않는 시나리오는 null이며 임의의 1로 채우지 않는다. 요청 변경을 새 플레이나 실수로 취급하지 않는다. |
| `type`, `action` | 아래 공통 이벤트 종류와 시나리오에 정의한 고정 행동 코드(예: `print`). UI 표시 문장을 코드 ID로 쓰지 않는다. |
| `process`, `result`, `context`, `data` | 각각 아래 공통 구조와 작업별 입력·변경·결과 상세 객체. 아직 발생하지 않은 결과를 성공으로 채우지 않는다. |

최소 공통 이벤트 종류:

- 생명주기: `scene.entered`, `scene.exited`, `scenario.started`, `scenario.paused`, `scenario.resumed`, `scenario.reset`, `scenario.completed`, `scenario.failed`, `scenario.aborted`.
- 물건·화면: `object.selected`, `interaction.opened`, `interaction.closed`, `navigation.back`.
- 업무 과정: `interaction.started`, `interaction.progress`, `interaction.validation_failed`, `interaction.retry_requested`, `workflow.backtracked`, `request.changed`, `guidance.requested`, `guidance.presented`.
- 작업 결과: `interaction.completed`, `interaction.failed`, `interaction.aborted`.

`interaction.failed`는 한 작업 시도의 실패이며 전체 시나리오 실패를 자동 의미하지 않는다. `interaction.progress`는 상태 스냅샷·진행률 용도이며 프레임마다 같은 이벤트를 새 행동처럼 만들지 않는다. 성공 결과는 실제 업무 완료 전이가 확정된 때 한 번 발행한다. 비동기 출력의 시작을 출력 완료로 보고하지 않는다. 인계가 완료 조건이면 출력·보관만으로 `scenario.completed`를 발행하지 않는다.

#### 과정 기록과 카운트

- 과정의 원장은 고유 이벤트 이력이다. 누적 횟수는 이 이력에서 도출한 조회용 요약이며 React와 Unity가 각각 별도로 증가시키지 않는다. Unity의 실제 상태·판정 확정 지점에서 하나의 공통 모듈이 발행하고 집계한다. React는 이를 수신·표시·저장한다.
- `process.scope`는 `interaction` 또는 `scenario`다. interaction 요약은 현재 scenarioRunId의 해당 stepId·objectId·workItemId, scenario 요약은 현재 scenarioRunId 전체를 집계한다. 요청 revision은 각 원본 이벤트에 보존하며 요청 변경만으로 기존 실행 기록·누적 횟수를 지우지 않는다. 서로 다른 범위의 요약을 더해 중복 합산하지 않는다.
- `measurementStatus`는 `complete`, `partial`, `unavailable`이다. 신뢰할 수 없는 횟수·시간은 null과 `measurementNote` 사유로 표시하며 미측정을 0으로 쓰지 않는다. `complete`의 횟수·활성 시간은 측정된 0 이상의 정수이고 guidanceUsed는 boolean이다. 미측정 guidanceUsed도 false가 아닌 null로 표시한다. measurementNote는 complete이면 null, partial/unavailable이면 구체적 사유 문자열이다. 공통 필드는 `attemptCount`, `navigationBackCount`, `backtrackCount`, `retryCount`, `mistakeCount`, `repeatedMistakeCount`, `helpRequestCount`, `guidanceUsed`, `elapsedActiveMs`다.
- `attemptCount`: 실제 업무 판정에 제출한 시도 수. 입력 글자 수정·마우스 이동·카메라 회전·팝업 열기를 제출로 세지 않는다. 동일 비동기 작업 중 잠긴 반복 입력은 새 attempt가 아니다.
- `navigationBackCount`: 사용자가 팝업 닫기·사무실 복귀 등 명시적인 뒤로가기를 실행한 횟수. 이는 UI 사용 기록이며 그 자체로 실수나 업무상 되돌아감이 아니다.
- `backtrackCount`: 이미 진행한 업무 단계에서 이전 업무 단계로 사용자가 실제 돌아가 재확인·수정한 횟수. `workflow.backtracked`의 `data`에 `fromStepId`, `toStepId`, `reasonCode`를 기록한다. 자발적인 재확인도 업무상 되돌아감에는 포함할 수 있지만 실수로 자동 판정하지 않는다. 정상적인 연결 업무·팝업 복귀·시스템의 필수 재확인·변경 요청 대응은 이 카운트에서 제외한다.
- `retryCount`: 실패하거나 중단된 동일 업무 시도 이후 새 attemptId로 실제 다시 제출한 횟수. `interaction.retry_requested` 버튼만 누르고 제출하지 않은 경우는 의도만 기록하고 횟수를 증가시키지 않는다. 새 작업 항목·새 요청 조건에 대한 첫 제출은 재시도가 아니다. 개별 시도의 재시작과 전체 시나리오 초기화를 구별한다.
- `mistakeCount`: 시나리오에 미리 정의한 업무 판정에서 플레이어 입력이 실제 조건을 위반한 고유 failureId 수. `data`에 `failureId`, `reasonCodes`, `faultSource`(`player`/`system`/`none`), `expected`, `actual`을 기록한다. 입력 1회가 여러 조건을 위반해도 failureId 1개로 세고, `validation_failed`와 `failed`가 같은 failureId를 가리키면 한 번만 센다. reasonCode는 고정 시나리오 사전의 코드(예: `COPY_COUNT_MISMATCH`, `DATE_MISMATCH`, `WRONG_CLASSIFICATION`, `SEQUENCE_VIOLATION`)를 사용한다.
- `repeatedMistakeCount`: 같은 scenarioRunId 안에서 `stepId + objectId + workItemId + requestRevision + reasonCode` 조합이 이미 실수로 기록된 뒤 다시 발생한 추가 failureId 수. 같은 실수가 3회면 mistakeCount 3, repeatedMistakeCount 2다. 하나의 failureId에 여러 코드가 있어도 반복 카운트는 최대 1 증가한다. 첫 발생부터 반복 횟수에 포함하지 않는다.
- `helpRequestCount`는 사용자의 명시적 도움 요청 수다. `guidanceUsed`는 선택적 힌트·단계별 정답 안내를 실제로 제시한 경우 true이며 단순 요청만으로 true로 만들지 않는다. 오류 이후 자동으로 제시한 추가 안내도 포함하되, 기본 조작법·일반 오류 설명·필수 동료 대화와 확인 질문은 포함하지 않는다. `guidance.presented`에 `data.isAssistance`와 `reasonCode`를 명시한다.
- `elapsedActiveMs`는 로딩·일시정지를 제외한 해당 범위의 활성 시간이다. 오래 걸림·되돌아감·추가 확인만으로 실수를 만들지 않는다. 중복 전송·출력 잠금 반복 클릭·브라우저/통신 오류·게임 자체 오류는 플레이어 실수에서 제외하고 원인 코드와 별도로 보존한다. 배경 물건 클릭도 명세의 업무 위반 판정이 없으면 실수로 세지 않는다.
- 요청 변경으로 돌아가는 경우 `REQUEST_CHANGED` 또는 `EXPECTED_RECONFIRMATION` 등 고정 원인을 남긴다. 시스템이 요구한 재확인은 backtrack/mistake 증가 없이 기록한다. 명세에 원인이 없거나 확인할 수 없으면 알 수 없음으로 기록하며 추측으로 실수 원인을 붙이지 않는다.

#### 결과와 해석 컨텍스트

- `result`의 필수 필드는 `outcome`(`pending`/`completed`/`failed`/`aborted`), `success`(true/false/null), `completionCode`(고정 코드 또는 null), `data`(작업별 최종 결과 객체)다. 진행 중에는 pending/null/null/{}을 사용한다. completed는 모든 해당 범위 완료 조건을 충족한 경우 true, failed/aborted는 false다. 시나리오의 인계 등 필수 조건 누락을 작업 한 건의 성공으로 덮지 않는다.
- 공통 집계와 판정은 시나리오·범위가 다르면 분리한다. 예를 들어 출력 interaction 완료 평가와 보관·인계까지의 scenario 완료 평가는 별도 이벤트이며 서로 덮어쓰지 않는다. 실패한 개별 제출의 결과·원인도 최종 성공 후 삭제하지 않는다.
- `context`의 필수 필드는 `assessmentStatus`(`pending`/`evaluated`/`unavailable`), `assessmentCode`(아래 고정 코드 또는 null), `ruleVersion`(`v001`), `reasonCodes`(중복 없는 고정 코드 배열), `evidenceEventIds`(근거 원본 eventId 배열), `interpretation`(문자열 또는 null), `limitations`(한계·미측정 사유 배열)이다. 진행 중에는 assessmentStatus pending, assessmentCode/interpretation null이다.
- 수집 누락·미측정·근거 부족으로 같은 입력에서 판정을 재현할 수 없으면 unavailable/null로 남긴다. 이때 불완전한 기록을 실수 없음·실패·`TASK_INCOMPLETE`로 임의 변환하지 않는다. 평가 가능한 terminal 결과에서만 아래 순서를 위에서 아래로 적용해 **하나의 주 평가 코드**를 정한다. 선택된 코드에 가려진 완료·실수·반복·도움 사실은 process/result와 reasonCodes에 그대로 남긴다.

| 판정 순서 | assessmentCode | 결정 조건·의미 |
|---|---|---|
| 1 | `TASK_INCOMPLETE` | 해당 범위의 최종 outcome이 failed 또는 aborted. 미완료·실패·중단 이유를 completionCode/reasonCodes로 구별한다. 사용자 도중 종료는 `USER_ABORTED` 컨텍스트를 함께 남기며 종료 자체를 실수로 세지 않는다. |
| 2 | `TASK_REPEATED_ERRORS` | 최종 completed이고 repeatedMistakeCount가 1 이상. 반복 오류 뒤 완료했다는 사실과 도움 여부를 함께 남긴다. |
| 3 | `TASK_GUIDED_COMPLETED` | 최종 completed, 반복 오류 없음, guidanceUsed true. 선택적 안내를 받아 완료. |
| 4 | `TASK_SELF_CORRECTED` | 최종 completed, 반복 오류 없음, guidanceUsed false, mistakeCount가 1 이상. 기록된 실수를 스스로 수정해 완료. |
| 5 | `TASK_SMOOTH` | 최종 completed, mistakeCount 0, guidanceUsed false. 기록된 실수 없이 완료. 재확인·정상 복귀가 0이었다는 뜻은 아니다. |

- 이 코드들은 이번 가상 업무 수행의 설명용 범주이며 숫자 서열·직업 적성·지능·개인의 전반적 능력 점수가 아니다. 직업마다 임의의 기준으로 같은 코드의 의미를 바꾸지 않는다. 정책·코드 의미·집계 기준을 바꾸면 ruleVersion을 올리고 이전 결과의 버전·원본 이력을 보존한다.
- 해석은 관찰 사실과 근거에서만 만든다. 예: “부수 오류 1회 후 요청을 재확인하고 수정하여 출력 완료.” 횟수만으로 “실제 업무 능력이 낮음”, “이 직업에 부적합함”을 결론내리지 않는다. 추가 설명·추론이 있으면 한계와 근거를 표시하고 관찰 데이터를 덮어쓰지 않는다.

#### 도중 종료·하다가 중단한 경우의 컨텍스트

- 사용자가 명시적으로 ‘작업 그만하기/체험 종료’를 확정하여 미완료 작업을 끝내면 `interaction.aborted`, 전체 시나리오를 끝내면 `scenario.aborted`를 발행한다. 전체 종료 시 진행 중인 개별 작업도 종료한다면 두 이벤트의 범위를 구별하고 같은 terminationId로 연결한다. 두 이벤트를 사용자 종료 2회 또는 실수 2회로 세지 않는다. 팝업 닫기·Esc로 사무실 복귀·일시정지·잠깐 다른 탭 보기·초점 상실은 종료로 처리하지 않는다.
- 실제 업무 행동이 시작된 뒤 사용자가 종료했다는 근거가 있으면 `result.outcome:aborted`, `success:false`, `completionCode:USER_ABORTED`와 `context.reasonCodes`의 `USER_ABORTED`를 사용한다. 이는 “중간에 하다가 그만둠”이라는 완료 상태 컨텍스트이며 업무 오답 판정이 아니다. 작업 시작 전 종료는 `USER_EXITED_BEFORE_START`로 구별한다. 이 추가 정보는 기존 평가 코드의 의미를 바꾸지 않는 선택 확장이므로 schemaVersion 1/ruleVersion v001을 유지한다.
- `context.termination`은 종료된 범위에서 필수이며 그 외에는 null 또는 생략을 허용한다. 내부 필수 필드는 `terminationId`, `code`, `initiatedBy`(`user`/`system`/`unknown`), `workStarted`(boolean 또는 미측정 null), `lastStepId`, `lastObjectId`, `lastState`, `completedStepIds`, `remainingStepIds`, `inFlightActionIds`다. 마지막 단계·물건·상태는 실제 마지막 유효 기록으로 채우고 없거나 알 수 없으면 null로 표시한다. 단계/비동기 작업 배열도 알 수 없으면 []가 아닌 null과 limitations의 사유를 사용한다. 사용자에게 이유를 직접 받은 경우에만 선택 필드 `userProvidedReason`에 보존하고 흥미 저하·능력 부족 등의 이유를 추측하지 않는다.
- 종료 응답의 `process`는 종료 직전까지의 실제 누적 기록을 유지하고 `result.data.partialResults`에 이미 완료한 결과만 보존한다. 미출력·미보관·미인계 결과를 완료로 채우지 않는다. 시간·횟수·이전 실수는 초기화하지 않으며 종료 동작 자체로 mistakeCount/repeatedMistakeCount/retryCount를 증가시키지 않는다. 평가 근거가 충분하면 assessmentCode는 `TASK_INCOMPLETE`, 해석은 “문서 수정·저장 후 출력 도중 사용자 종료. 출력·보관·인계는 미완료”처럼 완료한 범위와 남은 범위를 구별한다. 근거가 불완전하면 assessmentStatus unavailable/assessmentCode null을 유지하면서 확인된 종료 사실과 한계만 제공한다.
- 의도적인 종료·초기화가 확정되면 진행 중 비동기 작업의 취소/분리 정책을 적용하고 닫힌 범위의 늦은 완료 콜백이 새 실행에 반영되거나 aborted를 completed로 덮어쓰지 않게 한다. 완료가 먼저 확정된 작업의 completed 결과는 이후 전체 시나리오 종료로 aborted로 바꾸지 않는다. 초기화로 중단한 경우에는 `USER_RESET` 원인을 구별하고 기존 run을 보존한 뒤 새 run을 시작한다.
- React의 명시적 화면 종료·Unity 제거는 가능한 경우 Unity에 종료를 요청하고 종료 요약을 수신·보존한 다음 수행한다. 브라우저 탭 닫기·강제 종료·통신 단절에서는 마지막 이벤트 전달이 보장되지 않으므로 종료 전 상태를 주기적으로 보존하고 재접속 시 대조한다. 마지막 기록만 있고 사용자 종료 확정 근거가 없으면 `SESSION_INTERRUPTED`/initiatedBy unknown과 측정 한계를 남긴다. 미관측 중단을 사용자 포기로 확정하거나 정상 일시정지를 임의의 시간 초과로 사용자 종료에 바꾸지 않는다. 이력 보완·전달 재시도도 eventId/terminationId로 중복을 제거한다.

복붙용 **도중 종료 부분 양식**은 아래와 같다. 가상 예시이며 기존 공통 봉투의 ID·시각·sequence·process 등 나머지 필드를 유지한 채 병합한다. 정상 완료 예시와 동시에 한 이벤트의 결과로 적용하지 않는다.

```json
{
  "type": "scenario.aborted",
  "action": "quit_scenario",
  "result": {
    "outcome": "aborted",
    "success": false,
    "completionCode": "USER_ABORTED",
    "data": {
      "partialResults": {
        "documentSaved": true,
        "printedCopies": 0,
        "handoffConfirmed": false
      }
    }
  },
  "context": {
    "assessmentStatus": "evaluated",
    "assessmentCode": "TASK_INCOMPLETE",
    "ruleVersion": "v001",
    "reasonCodes": ["USER_ABORTED"],
    "evidenceEventIds": ["evt-work-started", "evt-quit-confirmed"],
    "interpretation": "문서 수정·저장 후 출력 도중 사용자가 종료함. 출력·보관·인계는 미완료",
    "limitations": ["종료 자체는 업무 실수나 적성 판단 근거가 아님"],
    "termination": {
      "terminationId": "termination-example-001",
      "code": "USER_ABORTED",
      "initiatedBy": "user",
      "workStarted": true,
      "lastStepId": "print",
      "lastObjectId": "copier",
      "lastState": "printing",
      "completedStepIds": ["confirm", "review"],
      "remainingStepIds": ["print", "file"],
      "inFlightActionIds": ["print-job-example-001"]
    }
  }
}
```

#### 종료 응답 미수신 정산 프로필 v003 — 백엔드 판정

- 명시적 종료 요청 후 응답 대기 시간 초과, 탭 닫힘, 연결 단절은 먼저 미확정(pending_reconciliation)으로 보존한다. USER_ABORTED·업무 실패·TASK_INCOMPLETE로 추정하지 않는다. end_experience 재전송은 동일 requestId/내용으로 하며 실제 experience.ended만 Unity 종료 원장에 넣는다.
- 다음 플레이를 새로 시작하려는 명시적 요청에서 인증된 동일 소유자의 이전 체험을 서버가 대조한다. 단순 로그인·새 탭·기존 체험 재연결만으로 종료하지 않는다. 기존 체험이 살아 있으면 deferred_active, 생존 여부를 확인할 수 없으면 pending_reconciliation을 유지한다. 클라이언트가 보낸 대상 ID만으로 다른 사용자의 체험을 변경하지 않는다.
- 배포 기본값은 종료 응답 대기 5초(사용자 대기 UI), 소유권 lease heartbeat 30초, 만료 120초다. 이 기능들은 구현 요구이며 현재 제공되는 API가 아니다. heartbeat가 멈췄다는 이유만으로 종료하지 않는다. 명시적 새 시작 요청과 서버 lease 만료가 함께 확인된 경우에만 이전 소유권을 원자적으로 fence한 뒤 중단 정산한다. 일시정지·숨겨진 탭의 timer throttling은 사용자 포기 근거가 아니다. 기존 살아 있는 탭은 lease 상실 시 쓰기를 중지하고 재연결/새 시작 선택을 안내해야 한다. 서버는 갱신·정산 경합을 직렬화한다.
- 최종 종료 응답이 없고 위 조건을 만족하면 운영 상태를 interrupted로 확정한다. 코드는 END_RESPONSE_MISSING_ON_RESTART, 화면 문구는 '종료 응답을 받지 못해 이전 체험을 중단 처리했습니다'다. 사용자 포기라는 해석은 금지한다. 시작 요청만 있고 실제 시작 근거가 없으면 not_started로 정산하며 실제 체험 시작을 꾸미지 않는다.
- 서버 정산은 protocol:career-experience-resolution, type:experience.reconciled의 별도 응답이다. Unity experience.ended나 Unity eventId/sequence/occurredAt을 생성하지 않는다. schemaVersion:1은 별도 서버 봉투 버전이다. resolutionId/revision/resolvedAt/producer:backend/policyVersion:v003/source/evidence로 출처를 명시한다. 동일 reconcileRequestId/내용은 동일 응답, 같은 ID 다른 내용은 충돌 오류다. 클라이언트는 종료 Unity 이벤트와 서버 정산 두 종류를 모두 처리한다.
- lifecycleStatus와 업무 result를 분리한다. 종료 미수신 상태 자체로 result.outcome:aborted를 만들지 않는다. 마지막 검증된 scenario terminal 근거가 없으면 result:null, context.assessmentStatus:unavailable, assessmentCode:null이다. 기존 scenario.completed/failed/aborted 근거가 있으면 해당 범위 결과를 보존하되 experience.ended 수신 여부와 구별한다. 작업 하나의 완료를 시나리오 완료로 승격하지 않는다.
- 미수신 이후 최종 횟수·시간은 알 수 없으므로 최상위 process는 null이다. 마지막 수신 스냅샷은 lastObserved.process와 observedAt/sourceEventId에 그대로 보존하며 최종 전체 카운트로 사용하지 않는다. lastObserved.partialResults·단계·실행 중 작업도 확인한 항목만 기록하고 불명은 null이다. 카운트 증분은 전부 0이며 기존 실수 기록을 삭제하지 않는다. 정산은 추가 실수·재시도·사용자 중단 행동을 생성하지 않는다.
- 소유권 fence 전에 실제 발행된 늦은 experience.ended가 도착하면 인증·빌드·방·체험·run 귀속·이벤트 중복/충돌·lease 귀속을 검증한다. 수신 시각이 늦다는 이유만으로 버리지 않는다. 검증된 원본은 보존하고 같은 resolutionId의 revision을 증가시켜 ended로 정정한다. 이전 interrupted revision은 이력으로 남기고 새 체험은 변경하지 않는다. fence 후 무효 소유권의 신규 행동은 격리하며, 발행 시점/귀속을 검증할 수 없으면 검토 대기로 보존한다. 단순 클라이언트 시각만으로 검증 완료 처리하지 않는다.
- 백엔드 응답의 revision이 오래되면 저장 이력만 추가하고 최신 표시를 덮지 않는다. 정산·종료 이벤트의 이중 집계를 금지한다. 실제 종료 응답 수신 직후에는 ended가 우선하고 정산 중 도착하면 원자적 비교·갱신으로 중단 판정의 덮어쓰기를 막는다. 다시 접속하지 않는 사용자는 자동 사용자 포기로 확정하지 않고 별도 보존 정책 전까지 미확정으로 남는다.
- 프론트/백엔드 담당자는 v003 JSON 계약·예시·수용 사례를 기준으로 구현한다. 이번 전달은 정책/명세이며 서버 endpoint, lease, 재정산, Unity/React 실제 왕복 구현·실행 pass를 뜻하지 않는다. 기존 일부 브리지 코드 존재와 이번 신규 요구의 미검증을 구별한다.

#### 장면 공통 전달·보존

- 공통 통신 모듈은 장면 전환 중에도 유지하고 세션·실행 ID와 이력을 장면마다 새로 초기화하지 않는다. 완료 이벤트는 상태 확정 후 발행하고 동일 완료 전이의 재클릭은 추가 완료·출력·실수를 만들지 않는다.
- Unity → 같은 페이지의 React 전달 이름은 `career-experience:event`로 고정하고 이벤트 detail에 공통 JSON 객체를 넣는다. 렌더링 라이브러리별 코드는 이 규격으로 연결하는 어댑터에만 둔다. iframe이면 `{ "channel": "career-experience", "event": <공통 이벤트> }` 형태로 부모에 전달한다. 송신 targetOrigin을 명시하고 수신 origin·source·버전·ID를 확인한다.
- 전송 재시도는 같은 eventId를 사용하고 수신 측은 중복을 제거한다. 순서가 바뀌면 sequence로 복원하며, 누락 감지 시 원본 이벤트 재전달/조회로 복구한다. 숫자 간격을 추정 이벤트로 채우지 않는다. 리스너가 늦게 연결되거나 장면이 바뀌어도 상태 전이·오류·terminal 이벤트를 잃지 않도록 준비 신호, 보존 이력과 재전달 방식을 구현·전달 문서에 명시한다. 여러 전달 경로를 동시에 듣는 경우에도 같은 eventId를 한 번만 처리한다.
- `scenario.reset`은 초기화 직전의 이전 scenarioRunId와 최종 과정 요약을 보존한다. 미완료 실행은 해당 사용자의 중단/초기화 원인을 기록하고 scenario.aborted로 종료한 뒤 새 scenarioRunId의 scenario.started를 발행한다. 이미 완료된 실행은 completed를 aborted로 바꾸지 않는다. 새 실행의 카운트만 0부터 시작하며 과거 실행과 합산하지 않는다.
- 시나리오 명세에 단계·행동 코드, 물건/실제 인스턴스/에셋 연결, 작업 항목, 이벤트 발생 지점, reasonCode 사전, 정상 복귀·되돌아감·재시도·실수·도움 판정 기준, 작업별 result.data 구조, revision 변경·초기화 규칙을 구체화한다. 전달 문서에는 실제 지원 규격 버전·이벤트와 React 수신 예시·해당 빌드에서 검증한 범위를 적는다. 지침 양식을 실제 측정 결과로 catalog에 등록하지 않는다.

#### 복붙용 공통 응답 예시

아래는 **가상의 시나리오 범위 완료 요약**이다. 물건 이벤트에서는 objectId/instanceId/assetId/assetVersion/stepId/workItemId/attemptId를 해당 실제 값으로 채운다. 아래 evidenceEventIds가 가리키는 원본 과정 이벤트도 함께 보존해야 하며, 이 예시만으로 실제 실행 근거를 만들지 않는다.

```json
{
  "schemaVersion": 1,
  "protocol": "career-experience",
  "eventId": "evt-020",
  "sequence": 20,
  "occurredAt": "2026-10-31T10:30:00+09:00",
  "sessionId": "session-example-001",
  "scenarioRunId": "run-example-001",
  "buildId": "example-v001",
  "sceneId": "office",
  "scenarioId": "career-net-253-office-documents",
  "scenarioVersion": "v001",
  "objectId": null,
  "instanceId": null,
  "assetId": null,
  "assetVersion": null,
  "stepId": null,
  "workItemId": null,
  "attemptId": null,
  "requestRevision": 1,
  "documentRevision": 2,
  "type": "scenario.completed",
  "action": "complete_scenario",
  "process": {
    "scope": "scenario",
    "measurementStatus": "complete",
    "measurementNote": null,
    "attemptCount": 6,
    "navigationBackCount": 3,
    "backtrackCount": 1,
    "retryCount": 1,
    "mistakeCount": 1,
    "repeatedMistakeCount": 0,
    "helpRequestCount": 0,
    "guidanceUsed": false,
    "elapsedActiveMs": 95000
  },
  "result": {
    "outcome": "completed",
    "success": true,
    "completionCode": "OFFICE_DOCUMENTS_HANDED_OFF",
    "data": {
      "documentId": "DOC-001",
      "copies": 2,
      "folder": "회의자료",
      "handoffConfirmed": true
    }
  },
  "context": {
    "assessmentStatus": "evaluated",
    "assessmentCode": "TASK_SELF_CORRECTED",
    "ruleVersion": "v001",
    "reasonCodes": ["COPY_COUNT_MISMATCH", "USER_RECHECK"],
    "evidenceEventIds": ["evt-012", "evt-013", "evt-019"],
    "interpretation": "부수 오류 1회 후 요청을 재확인하고 수정하여 출력·보관·인계를 완료함",
    "limitations": ["가상 체험 한 회의 수행 기록이며 직업 적성·전반적 능력 진단이 아님"]
  },
  "data": {}
}
```

## 6. 완료 전 검토
- 직접 작업형 체험은 물건별 closeup·단계별 work_surface 명세, 실제 조작/동등 대체 입력·정답 데이터·시각 결과, 닫기/초안 유지/복귀·변경 요청/인계/초기화와 비동기 중복 방지의 구체성을 확인한다. 설계만 수정한 경우 실행·사용·빌드 상태를 변경하지 않는다.
- 직업체험의 기존 직업 ID·원본 위치·역량 표기·파노라마·후보·모델·유형 참조, 정확히 3개 조작 물건, 상태 전이·성공/오류·변경·초기화 조건, 전체 공간 후보와 공통/비공통 분류를 확인한다. 명세·구현·실행 검증과 전체 직업 작성 범위를 구별한다.
- 공통 응답 규격을 구현/수정한 경우 여러 장면에서 동일 봉투·이벤트를 수신하는지, 실제 인스턴스·작업 항목·revision·run 귀속이 정확한지 확인한다. 정상 복귀/요청 변경은 실수에서 제외하고, 단일 오류·동일 오류 반복·독립 오류 여러 건·힌트 요청과 제시·자력 복구·미완료·미측정의 카운트와 평가 우선순위를 확인한다. 중복/지연/순서 역전/리스너 지연·장면 전환·비동기 중복 입력·완료 후 재클릭·전체 초기화 후 이전 기록 보존을 실제 Unity → React 실행으로 확인하고 미구현·미검증을 구분한다. 지침만 수정한 경우에는 문서·예시 일관성 검토만 보고하며 통신 구현·실행 pass를 추가하지 않는다.
- 도중 종료 규격을 구현/수정한 경우 개별 작업 중단/전체 시나리오 중단, 시작 전 종료/작업 도중 종료, 정상 팝업 복귀·일시정지와의 구별, 마지막 단계·누적 기록·부분 결과·남은 업무 보존, 종료로 인한 실수 비가산, 같은 terminationId의 중복 방지, 늦은 비동기 완료 차단을 확인한다. 브라우저 강제 종료·통신 단절의 미전달/미확인 상태를 사용자 포기로 오인하지 않는지 확인한다.
- JSON 구문·schema_version·필수 필드·ID 유일성 확인.
- 이미지 파일·해시·실제 크기·분류 경로 및 모델 source_images 참조의 ID·버전 존재 여부 확인. 원본 이미지 폴더에 목록 미등록 파일이 남지 않도록 확인합니다.
- 원본·Blender·실제 사용본·미리보기·Unity·문서 경로 존재 여부 확인.
- 빌드의 에셋 ID·버전 참조와 프로젝트 소속 확인.
- color1/color2 원본 해시와 최종 PNG·대응표의 해시를 확인하고, 런타임에는 공용 PNG 한 장만 사용하는지 확인합니다. Unity 복사본은 최종 PNG와 동일해야 합니다.
- 기본 면의 color1 출처와 강조 영역의 color2 출처, UV 대응표 및 accent_reason을 확인합니다.
- 태그 차원·정규 표기·별칭 처리의 일관성과 적용 후보/실제 사용 구분 확인.
- 컨텍스트·직업·파노라마·슬롯·에셋의 기존 ID·버전 참조 존재 여부 및 승인/사실검증 상태 분리 확인.
- 변형의 기준/결과 버전, materialized 여부, palette_version과 mapping.json 색상 칸의 유일성·부위 선택·실제 UV 적용 확인. planned를 결과물로 집계하지 않음.
- 사용 이력의 프로젝트 소속·장면/프리팹 경로·revision·실제 quantity/instances 길이·인스턴스 중복·삼각형 집계와 빌드 참조 일치 확인. 프리팹 정의와 장면 배치 중복 합산 금지.
- 계획·실제 배치·빌드 포함·실행 검증을 구분하고 증거 없는 상태 승격 금지. 기존 catalog를 추정으로 보완하지 않음.
- 문서 링크 및 전달 ZIP 구조 확인.
- Blender/Unity 재질·장면·WebGL 실행과 URL 가용성은 실제 확인한 범위만 보고.


## 7. 웹용 로우폴리 제작 규칙

### Blender · Meshy AI 작업 분담

#### 기본 원칙과 선택 절차
- 회전 사무의자 베타에서는 직접 제작 792삼각형·0크레딧, Meshy 후처리 964삼각형·5크레딧이었다. 반복·대칭·정확한 구조가 많은 소품은 복잡해 보여도 Blender를 우선 검토하고, 자유로운 곡면이 핵심인 경우 Meshy의 이점을 검토한다. 한 사례의 수치를 다른 모델의 보장값으로 사용하지 않는다. 상세 근거: docs/human/assets/chair-comparison-beta.md.
- 간단한 작업은 Blender 직접 제작을 우선하고, 직접 모델링보다 기본 형태 생성의 이점이 큰 작업에 Meshy를 사용합니다.
- 대상의 실루엣·필요 디테일 확인 → 재사용 모델·스크립트 검색 → 도형·매개변수로 충분하면 Blender → 직접 제작·교정 부담이 크면 Meshy 검토 → 필요시 부품별 혼합 → 선택 이유 한두 문장 기록 순서로 진행합니다.
- 승인된 작업 범위 안의 Blender 직접 제작은 도구 선택만을 이유로 별도 확인을 요구하지 않습니다. 사용자 개별 지시와 승인된 크레딧 범위를 준수합니다.
- 면 수만으로 우열을 판단하지 않고 실루엣·치수 정확도·수정 용이성·재사용성·실제 결과를 함께 비교합니다.

#### Blender 직접 제작 우선 조건
- 박스·원통·평면·단순 곡선 조합으로 표현하거나 크기·두께·반경·반복 개수로 형태를 정의할 수 있습니다.
- 대칭과 일정 간격이 중요하거나 기존 스크립트의 매개변수 변경으로 제작할 수 있습니다.
- Meshy 생성 후 교정하는 것보다 직접 제작이 간단합니다.
- 대표 대상: 바닥판·바닥 표면·타일·단순 러그, 상자·책·서류 묶음, 단순 책상·선반·서랍장, 모니터 본체·단순 간판, 반복 프레임·기둥·받침대.
- 고정 분류가 아니므로 같은 종류라도 복잡한 형태는 다른 방식을 선택할 수 있습니다.

#### Meshy 우선 검토 조건
- 캐릭터·동물·조형물처럼 자유로운 곡면·실루엣이 중요하거나 참고 이미지의 독특한 외형을 기본 도형으로 만들기 어렵습니다.
- 직접 제작 스크립트가 길어지고 반복 수정이 많거나 생성 형태를 쓰면 후처리를 포함해도 부담이 줄어듭니다.
- Meshy는 형태 생성에 집중하고 최종 팔레트는 Blender에서 적용합니다.
- 프롬프트만으로 면 수·부위 분리·정확한 치수가 보장된다고 가정하지 않습니다.
- 승인된 크레딧 안에서 실행하며 마음에 들지 않아도 유료 재생성을 자동 반복하지 않습니다. 먼저 Blender 수정 가능성을 판단합니다.

#### 혼합 제작
- Meshy는 유기적 형태·특징적인 실루엣, Blender는 단순 구조물·받침대·부품·반복 배치를 담당할 수 있습니다.
- Blender에서 전체 조립, 크기·방향·원점 정리, 삼각형 최적화, 팔레트 UV·공용 재질·GLB 내보내기를 수행합니다.
- 예: 나무 수관은 Meshy·받침대와 배치는 Blender, 캐릭터 기본 형태는 Meshy·단순 소품과 전시대는 Blender, 디오라마 가구·바닥은 Blender·특징적 조형물은 Meshy.

#### 베타 비교 기록과 해석
아래는 사용자가 제공한 비교 결과이며 [기존 베타 보고](docs/human/assets/blender-direct-beta.md)에도 기록되어 있습니다. 규칙 갱신 중 새로 실행·재측정한 결과가 아니며 보편적인 성능 보장으로 일반화하지 않습니다.

| 대상 | 제작 방식 | 최종 삼각형 | Meshy 비용 |
|---|---|---:|---:|
| 바닥판 기존 버전 | Meshy 생성 + Blender 교정 | 120 | 5크레딧 |
| 바닥판 비교 버전 | Blender 직접 제작 | 220 | 0크레딧 |
| 바닥 표면 | Blender 생성 함수 재사용 | 108 | 0크레딧 |

- Meshy 바닥판은 원형에 가깝게 생성돼 교정이 필요했고, Blender 직접 제작은 치수·모서리 반경을 정확히 설정하고 다음 표면에 함수를 재사용할 수 있었습니다.
- 직접 제작본은 면 수가 늘어도 상한 안에서 형태 일관성을 확보했습니다. 두 방식 모두 팔레트 UV·GLB 웹 표시가 가능했다는 기존 결과입니다.
- 약 3.3MB 파일 크기는 주로 공용 팔레트 이미지에서 발생했습니다. 도구 변경만으로 텍스처 용량 문제가 해결되지는 않으며 팔레트 용량 최적화는 별도로 판단합니다. 색상 보존 규칙은 유지합니다.
- 모델별 실제 토큰 사용량은 미측정이므로 절감 수치를 주장하지 않습니다. 실행 시간과 스크립트 작성·검수 시간을 구분하고 측정 가능한 범위만 설명합니다.

#### 공통 기준과 기록
- 두 방식 모두 아래 삼각형 예산·팔레트·검수 기준을 그대로 적용합니다.
- 직접 제작은 제작 스크립트와 원본 Blender 파일을 보존합니다. original/ 경로의 source.blend와 README에 직접 제작임과 Meshy 작업 ID가 없는 사유를 명시합니다.
- Meshy 사용 시 프롬프트·작업 ID·실제 소비 크레딧을 기록합니다. 기존 결과는 덮어쓰지 않고 에셋 ID·버전으로 관리합니다.
- 최종 GLB 재가져오기 후 삼각형·재질·텍스처·UV를 확인하고 웹의 실제 크기·축소 상태 외형·색 번짐을 검사합니다. Unity WebGL은 실제 빌드·실행한 경우에만 검증 완료로 보고합니다.

### 적용 원칙
- Meshy 생성, Blender 후처리, 웹용 GLB 제작에 적용합니다. 작업 전에 개별 소품인지 디오라마인지 구분합니다.
- 사용자가 개별 작업에서 명시한 변경 사항을 우선합니다. 기준을 충족하지 못하면 임의로 완화하지 말고 원인과 수정안을 보고합니다.
- 검증하지 않은 항목은 '미검증'으로 표시합니다.

### 삼각형 예산과 형태
- 단순 캐릭터를 포함한 개별 소품은 전체 1,000삼각형 이하입니다. 눈·입·장식·강조선 등 모든 부품을 합산합니다.
- 디오라마는 장면 전체 5,000삼각형을 목표로 합니다. 내부 개별 소품도 각각 1,000삼각형 이하로 유지합니다.
- 반복 소품은 배치 횟수만큼 장면 전체 삼각형에 포함합니다. 목표 초과 시 원인과 최적화안을 제시하고 임의로 목표를 변경하지 않습니다.
- 편집 화면의 사각형 면 수가 아니라 최종 GLB의 삼각형 수로 검수합니다.
- 실루엣과 표정의 가독성을 우선하고 보이지 않는 내부 면·불필요한 작은 디테일을 정리합니다.
- 둥근 디자인에는 부드러운 셰이딩을 사용하고 각진 표현은 필요한 부분에 적용합니다.

### 최종 공용 팔레트 제작
- color1과 color2의 색상 칸을 함께 담은 정사각형 텍스처 한 장을 사용합니다. 원본 칸의 색을 보존해 배치하고 합친 위치에 맞춰 UV를 설정합니다.
- 색을 다시 생성하거나 근사한 색으로 대체하지 않습니다. 보간·색상 보정·손실 압축으로 색을 바꾸지 않고 PNG로 저장합니다.
- 글자·번호·격자선·새 무늬·그림자를 추가하지 않습니다. 형태 참고 이미지의 질감·그림자를 별도 텍스처로 복제하지 않습니다.
- 원본에 미세한 색 변화가 있으면 UV가 칸 중앙의 같은 색을 참조하도록 합니다.
- 각 칸의 원본 출처(color1/color2), 행·열, 최종 UV 위치를 mapping.json에 기록합니다.

### Blender UV와 재질
- 모든 부품은 공용 재질과 동일한 팔레트 텍스처를 사용합니다.
- 각 면의 UV를 원하는 칸 중앙에 모으거나 충분히 안쪽에 배치합니다. 칸 경계를 넘어 다른 색을 참조하지 않게 합니다.
- 서로 다른 색을 쓰는 면은 UV를 분리하고 같은 색의 부위는 같은 칸을 공유할 수 있습니다.
- 색상 변경은 팔레트를 다시 칠하기보다 UV를 다른 칸으로 옮겨 처리합니다.
- 재질 기본색 배율은 흰색으로 유지하고 버텍스 컬러 등으로 추가 착색하지 않습니다. 팔레트를 색상 텍스처로 올바르게 해석하도록 설정합니다.
- 불필요한 노멀·러프니스·메탈릭·AO 이미지 맵을 추가하지 않습니다. 조명 명암은 허용하지만 텍스처에 명암을 덧그리지 않습니다.
- 원거리·축소 표시에서 색 번짐을 확인하고 UV·필터링·밉맵 설정을 조정합니다.
- 공용 재질을 사용했다는 이유만으로 드로콜이 하나라고 가정하지 않습니다.

### 제작 순서
1. 준비: 참고 이미지·팔레트 원본·대상 웹 환경, 재사용 모델·스크립트, Blender 사용 가능 여부와 필요한 경우 Meshy 연결을 확인합니다. 소품별·장면 전체 예산과 승인된 크레딧 범위를 확인하고 위 절차로 제작 방식을 선택합니다.
2. 형태 제작: 단순 형상은 Blender 직접 제작, 복잡한 실루엣은 Meshy 생성 또는 부품별 혼합 제작을 선택합니다. 형태·실루엣을 우선합니다. 프롬프트의 면 수를 실제 결과로 간주하지 않습니다. 디오라마는 가능한 경우 주요 소품을 개별 생성해 Blender에서 조립하고 반복 나무·벤치·가로등은 재사용합니다. 재생성 전에 기존 결과를 후처리로 수정할 수 있는지 검토합니다.
3. Blender 최적화: 정면·측면·후면을 검사하고 의도하지 않은 연결·구멍·떠 있는 조각을 정리합니다. 개별 1,000 이하, 반복을 포함한 디오라마 전체 5,000 목표에 맞춥니다. 실제 표시 크기에서 읽히도록 표정·강조선을 단순화합니다.
4. 팔레트 적용: 기본 면은 color1, 강조는 color2에서 선택합니다. 원본 색을 보존한 정사각형 PNG와 공용 재질·UV를 적용합니다.
5. GLB 내보내기: 모델과 팔레트를 포함해 저장한 뒤 GLB를 다시 열어 형태·삼각형 수·재질·텍스처를 확인합니다. 실제 파일 크기를 바이트로 기록하고 별도 합의 없이 고정 용량 상한을 적용하지 않습니다.
6. 웹 검수: 대상 환경에서 로딩·외형을 확인합니다. 실제 표시 크기와 축소 상태의 색상·표정·강조선, 텍스처 누락·색 번짐·방향·크기를 검사합니다. 필요한 경우 오브젝트 수·드로콜·그림자 비용을 확인합니다.

### 반복 작업과 결과물 보존
- Meshy 생성 모델 또는 Blender 직접 제작 원본과 팔레트 원본을 보존하고 후처리 결과를 구분합니다.
- 색상 변경은 UV 이동으로 우선 처리합니다. 형태 변경은 기존 Blender 모델·스크립트 수정 가능성을 먼저 검토하고 필요한 경우에만 Meshy 재생성을 검토합니다.
- 검증된 설정과 후처리 스크립트를 재사용합니다. 스크립트는 에이전트 제어용 폴더가 아닌 해당 에셋의 processing/에 보관합니다.
- 최종 GLB, 공용 PNG, 원본·행·열·UV 대응표, 재사용 후처리 스크립트, 검수 기록을 저장합니다. 미생성 항목을 생성했다고 보고하지 않습니다.

### 완료 조건
- [ ] 모든 개별 소품은 각 부품 합산 1,000삼각형 이하입니다.
- [ ] 디오라마는 전체 5,000삼각형 목표 충족 여부를 확인했습니다.
- [ ] 반복 배치를 포함해 장면 전체 삼각형을 계산했습니다.
- [ ] 기본 면은 color1, 강조 영역은 color2 출처 색을 사용합니다.
- [ ] 원본에 없는 색을 텍스처나 재질에 추가하지 않았습니다.
- [ ] 정사각형 공용 팔레트 한 장과 공용 재질을 사용합니다.
- [ ] UV가 올바른 칸을 참조하고 색 번짐이 없습니다.
- [ ] 최종 GLB를 다시 열어 검수했습니다.
- [ ] 대상 웹 환경에서 로딩과 표시를 확인했습니다.
- [ ] 미검증 항목과 남은 문제를 명시했습니다.

### 완료 보고
선택한 제작 방식·이유와 실제 결과, Meshy 실제 소비 크레딧(미측정이면 미검증), 재사용 가능한 스크립트·모델, 다음 작업에 적용할 개선점을 포함합니다. 토큰·시간 절감은 측정 가능한 범위만 설명하며 실행 시간과 스크립트 작성·검수 시간을 혼동하지 않습니다.
소품별 삼각형 수, 반복 배치를 포함한 장면 전체 삼각형 수, 재질 수·텍스처 수, 팔레트 해상도, 최종 GLB의 실제 바이트 수, 웹 검수 결과, 미검증 항목·남은 수정 사항을 보고합니다.
미리보기 이미지만으로 삼각형 수·파일 크기·웹 성능을 검증했다고 보고하지 않습니다.

이 문서는 에이전트의 준수 지침이며 자동 실행 또는 CI 강제를 의미하지 않습니다.

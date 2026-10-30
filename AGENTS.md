# 에이전트 필수 작업 규칙

이 저장소에서 작업하는 에이전트는 수정 전에 이 문서를 읽고 반드시 준수합니다.
규칙·목록 형식·검토 절차는 이 파일에서 관리합니다. 별도 에이전트 제어 폴더, 검사 스크립트, 자동 훅은 사용하지 않습니다. 모델 제작 결과물인 재사용 후처리 스크립트는 해당 에셋 버전의 processing/에 보관할 수 있습니다.
사용자 지시 및 상위 지침이 우선합니다.

- 모든 모델에 Meshy를 사용할 필요는 없습니다. 제작 도구는 복잡도보다 형태의 특성을 우선해 선택합니다. 반복·대칭 구조, 정확한 치수, 명확한 부품 구성이 중요하면 Blender를, 유기적 형태·불규칙한 실루엣·자유로운 곡면이 중요하면 Meshy를 우선합니다. 복잡해 보여도 기본 도형과 반복 구조로 표현할 수 있으면 Blender를 우선합니다. 스크립트 재사용 가능성과 예상 수정 부담도 함께 고려합니다.

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

## 6. 완료 전 검토
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

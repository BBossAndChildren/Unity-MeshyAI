# 프로그램용 데이터

현재71공간 전달 기준: [workplaces-v006](../human/builds/workplaces-v006.md) — 현재319모델(248소품+71조립),805배치, 실제Native/HTTP71/71·시각71쌍·사무보조원구현범위 통과. v005이하는보존중간본이며 다른551직업초안은별도다.

직업체험의 물건 확대·직접 작업 설계에는 AGENTS.md의 `interaction_flow`·`interaction_objects.closeup`·`steps.work_surface` 확장 계약을 적용합니다. schema_version:3을 유지하며 이번 지침 작업에서는 catalog 파일·항목을 변경하지 않습니다. 기존 필드 누락은 아직 해당 방식으로 명세하지 않은 상태이며 구현 완료로 해석하지 않습니다. [사람용 적용 안내](../human/guides/object-closeup-direct-work.md)를 참조합니다.

| 파일 | 내용 | 조회 키 |
|---|---|---|
| catalog/assets.json | 에셋·제작 단계·팔레트·검수 경로 | asset_id + version |
| catalog/inventory-snapshots.json | 통합 검토 문서의 해시·출처·고정 참조 | snapshot_id + version |
| catalog/builds.json | 빌드·포함 에셋 | build_id |
| catalog/shared-textures.json | color1/color2 원본·역할·해시 | texture_id |
| catalog/palettes.json | 최종 정사각형 PNG·UV 대응표 | version |
| catalog/asset-images.json | 에셋 제작용 원본 이미지 | image_id + version |
| catalog/panoramas.json | 파노라마 원본 이미지 | image_id + version |
| catalog/workplace-contexts.json | 최종 공간 의미·태그·직업 분류·에셋 역할 (승인 대기) | context_id + version |
| catalog/occupation-workplace-candidates.json | 전체 제공 원문 기반 직업 후보·분류 근거·출처 | occupation_id |

UTF-8 JSON, schema_version: 3입니다. 필수 필드와 제약은 [AGENTS.md](../../AGENTS.md)의 목록 계약을 따릅니다. 모든 경로는 저장소 루트 기준입니다.

조회 흐름: builds.assets → assets → palette_version → palettes → source_texture_ids → shared-textures.
모델의 source_images는 catalog(asset-images 또는 panoramas), image_id, version으로 이미지 목록의 images 배열을 참조합니다.

v2의 texture_ids/unity_texture_paths는 palette_version/unity_palette_path로 대체했습니다. color1/color2는 색상 출처이며 실제 모델은 두 원본의 칸을 합친 공용 PNG 한 장을 사용합니다.
모델 종류(kind), 제작 상태(status), 검수 기록(inspection_path), 후처리 스크립트(processing_paths)를 함께 기록합니다.
제작 방식은 generation_method(blender_direct/meshy/hybrid), 선택 이유는 generation_reason, 제작·비용 근거는 production_record_path, 실제 소비 크레딧은 meshy_credits_used에 기록합니다. 기존 항목은 다음 갱신 시 근거를 확인해 보완하며 누락을 Meshy 생성 또는 비용 0으로 해석하지 않습니다. 상세 계약은 AGENTS.md를 따릅니다.
검수 수치는 최종 GLB를 다시 열어 측정합니다. 미측정 수치는 null, 미검증 상태는 unverified입니다.
팔레트 대응표 mapping.json과 에셋 검수 기록 inspection.json의 형식도 AGENTS.md에서 관리합니다.
실제 팔레트 등록 여부와 고정 버전은 palettes.json에서 조회합니다.

자동 검사 도구는 없으며 에이전트가 AGENTS.md의 검토 절차를 수행합니다.

## 선택적 재사용·이력 확장

schema_version: 3과 기존 참조 형식을 유지합니다. 상세 계약·필수/선택 필드·null·빈 배열 의미는 [AGENTS.md](../../AGENTS.md)의 '에셋 분류·재사용·사용 이력 확장'을 따릅니다.

- assets.tags: object_type/function/space/activity 배열. 정규 어휘와 별칭은 AGENTS.md에서 관리합니다.
- assets.applicable_contexts: 기존 context_id/version의 적용 후보이며 실제 사용과 구분합니다.
- occupation_groups.verification: 기존 분류 근거·적용 조건을 보완하는 사실 검증이며 review_status를 대체하지 않습니다.
- 향후 asset-color-variants.json: 기준 에셋·변형 식별자·부위·mapping 색상 칸·새 결과 버전을 연결합니다. 색상 칸 키는 palette_version + texture_id + row + column이며 UV 데이터를 복제하지 않습니다.
- 향후 asset-usages.json: 프로젝트·장면·프리팹·에셋·변형의 사용 이력 단일 기준입니다. 현재는 usage_id별 최신 revision, 과거 빌드 포함은 해당 revision 스냅샷을 조회합니다.

두 신규 파일은 이번 문서 갱신에서 생성하지 않습니다. 파일·필드 누락은 미등록이며 사용 없음이나 검증 통과로 간주하지 않습니다. 신규 계약은 관련 작업 시 실제 근거로 적용하고 기존 catalog를 추정으로 채우지 않습니다.
직업 → occupation_groups → context → panorama_ref/asset_slots → asset → variant → usage 순서로 연결합니다. prefab_definition을 장면 인스턴스 수량에 합산하지 않고 기존 builds.assets는 포함된 실제 에셋 버전 집합으로 유지합니다. 동일 에셋 버전의 여러 프로젝트 등록은 지원하지 않습니다.

## 공간 컨텍스트 로딩

1. `catalog/workplace-contexts.json`의 `review_status`를 확인합니다. 현재 `pending_user_approval` 초안은 승인된 제작 지시로 실행하지 않습니다.
2. `contexts`에서 `context_id` 또는 `tags.space/activity/interaction/visual`로 공간을 찾습니다. 같은 태그 분류 안에서는 OR, 분류 사이에서는 AND로 필터할 수 있습니다.
3. `panorama_ref`의 `catalog`, `image_id`, `version`으로 `panoramas.json`의 원본 이미지를 찾습니다. 이미지 경로·해시는 이 목록에서 가져오며 컨텍스트에 복제하지 않습니다.
4. `occupation_groups[].occupation_ids`를 `occupation-workplace-candidates.json`의 `occupations[].occupation_id`와 연결합니다. `reason`과 `applicability_condition`을 함께 읽고, 원자료의 `source_categories[].basis`와 장면 기획의 `mapping_basis`를 구분합니다.
5. 에셋 제작 전에 `meaning`, `office_characteristics`, `activity_sequence`, `layout_intent`, `asset_slots`를 읽습니다. 파노라마는 최종 조립 형태의 기준이며 이미지 신규 생성 작업이 아닙니다.
6. `asset_slots[].asset_ref`가 null이면 미제작 계획입니다. 생성 완료 에셋으로 세거나 `assets.json`에 가짜 ID를 넣지 않습니다. 실제 모델 등록 후 정확한 asset_id/version으로 연결합니다.

예: `tags.activity`에 `대면상담`이 있는 공간 → `office-professional-consultation` → `PAN-005 v001` → 법률 자문 기본형과 상담 직종별 변형 조건 확인 → 상담 테이블·대면 좌석·자료 준비석의 역할을 개별 에셋 제작에 전달합니다.

형식 계약은 [AGENTS.md](../../AGENTS.md), 사람용 검토 내용은 [사무실 공간 컨텍스트](../human/images/office-workplace-contexts.md)를 참조합니다. 기존 `shared-textures.json`은 색상 출처 목록으로 유지하며 직업·공간 분류를 넣지 않습니다.

통합 목록은 `inventory-snapshots.json`에서 문서 경로와 SHA-256을 조회합니다. snapshot_counts는 문서 시점의 수량이며 현재 실제 사용량이 아닙니다. 현재 직업 catalog는 job_base.txt의 552개 직업·809개 연결을 포함하고, source_history는 이전 부분 자료의 출처를 보존합니다. 직업·공간 연결과 기획 승인 상태는 자동 변경하지 않습니다.

## 직업 공간·파노라마 제작 자료

- [직업 후보](catalog/occupation-workplace-candidates.json): schema_version:3, 전체 제공 원문 552개 직업·809개 장소 연결. source_history는 과거 부분 원문의 출처입니다.
- [사무실 컨텍스트](catalog/workplace-contexts.json): schema_version:3, context_id/version으로 조회. occupation_groups는 직업 후보, panorama_ref는 실제 참고 이미지, asset_slots는 아직 모델로 확정하지 않은 계획입니다.
- [파노라마 프롬프트](catalog/panorama-prompts-v002.json): schema_version:3, prompt_id/version으로 조회. 25개 유효 분류의 71개 구도이며 기존 5개·신규 66개입니다. result_panorama_ref:null은 이미지 생성 전 상태입니다.
- [사람용 제작 자료](../human/jobs/panorama-production-package.md)

해당 기획 catalog는 위에 명시한 schema_version을 개별적으로 읽습니다. 기존 모델·빌드 catalog의 데이터 계약을 이 문서 작업으로 일괄 변경하지 않습니다. 공간의 원문 분류에 속한 모든 직업이 개별 프롬프트의 확정 사용자라는 뜻은 아닙니다.

## 직업·장소·핵심역량 기준 자료

- [occupation-place-competency-reference-v001.json](catalog/occupation-place-competency-reference-v001.json): 기존 직업 ID 기준의 원본 설명 참조·핵심역량·장소 및 파노라마 후보를 결합한 파생 조회. 원본은 Job_things_list.txt, 직업 식별은 기존 occupation catalog를 따릅니다.
- [사람용 기준 자료](../human/jobs/occupation-place-competency-reference-v001.md)
- core_competencies.values는 원문 핵심능력의 제목과 빈 줄만 제외한 값이며 source_ref로 원본 필드를 추적합니다. 장소 후보·세부 파노라마 적합성·사실 검증 상태는 기존 목록의 구분을 유지합니다.

## 직업체험 설계 목록

- [career-minigame-types-v001.json](catalog/career-minigame-types-v001.json): 공통 조작 10종·특수 상황 10종의 설계. 실제 모듈 구현은 미완료.
- [career-experience-scenarios-v001.json](catalog/career-experience-scenarios-v001.json): 사무보조원 1건의 물건 3개·상태·정답·분기·검수 명세. 나머지 551개 작성 대기.
- [panorama-career-experience-layouts-v001.json](catalog/panorama-career-experience-layouts-v001.json): 전체 71개 공간의 공통·비공통 후보 및 시나리오 연결. 실제 배치 원장이 아님.
- 필드 계약은 AGENTS.md의 파노라마 기반 직업체험·상호작용 명세를 따른다.

## 전체 직업체험 초안 — v002

- [career-experience-scenarios-v002.json](catalog/career-experience-scenarios-v002.json): 기존 552개 직업 전체 초안. 1개 보존·551개 추가. scene_selection과 review_issues로 기존 연결/신규 제안·문제 데이터 한계를 구분.
- [panorama-career-experience-layouts-v002.json](catalog/panorama-career-experience-layouts-v002.json): 전체 71개 공간과 물건별 기존 적용 공간·새 시나리오 적용 후보·미선택 대안 역조회.
- 유형 설계는 career-minigame-types-v001.json 유지. 20종 모두 배정됐으나 모듈 구현 완료를 뜻하지 않음.
- [사람용 상세](../human/jobs/career-experience-scenarios-v002.md) · [정적 검토 기록](evidence/career-experience-scenarios-v002-review.json)

- `catalog/asset-usages.json`: 실제 Unity 사무실 구성 단위 사용 이력. 프리팹 정의는 장면 수량에 포함하지 않음.
- `evidence/office-assistant-v001/`: Blender 재가져오기, Unity 장면·Play Mode·WebGL 실제 실행과 최종 파일 해시 근거.

## 전체 공간 제작 조회 자료

- `catalog/workplace-production-v001.json`: 고정71공간 제작/검수 진행과 범위별 수량.
- `catalog/workplace-asset-candidates-v004.json`: 기존262ID·71공간을 보존한 기획+제작 지원 추가 후보 연결; 실제 사용 원장 아님.
- `catalog/asset-usages.json`: 실제 Unity 장면/프리팹의 단일 사용 원장, 최신revision 집계 및 과거 보존.
- `catalog/scene-assemblies.json`: 실제 Blender/독립GLB 조립 원장.
- `catalog/career-experience-scenarios-v003.json`: 사무보조원v002 한 건 개정; 기존551개 초안 자동 승인/대체 아님.
- `evidence/workplaces-v005/`: 최종 대상 빌드의 실제 생성/실행/소스 근거, 검사 범위와 미검증 구분.



- [효과음 제작 후보 목록](catalog/sound-effects-candidates-v001.json) — ElevenLabs 예정, 108종 기획 후보, 생성 미실행.

- `catalog/spatial-detail-packs.json`: 다중 소품 원본 묶음·분리 고정 에셋·전체 적용 후보·미배치 검수 상태.
- `catalog/workplace-asset-candidates-v005.json`: 기존262 + 공간 장식6 + 선택 라이브러리8 =276개 후보.


- [ElevenLabs 효과음 제작 목록](catalog/sound-effects-v001.json) — 108종 승인 중 32종 생성·저장, 76종 서비스 대기 제한으로 미시작.

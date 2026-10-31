# AST-013 v001 — 낮은 책상 스크린 Unity 재사용 기록

현재 등록 상태: `ready`. 실제 workplaces-v006의 모델·표시 검수 범위다. 전체 후보와 현재/과거 사용 수량은 아래 원장 조회를 기준으로 읽는다. [최종 빌드](../builds/workplaces-v006.md).

2026-10-31. 이 설명은 asset-usages와 scene-assemblies의 조회 결과이며 독립 사용 원장이 아니다. 기존 원본·Blender·GLB 버전과 제작 상태를 보존했다.

## 형상·제작·재사용

- 원본: `meshy/models/original/AST-013/v001/source.blend`
- Blender 수정본: `meshy/models/blender/AST-013/v001/model.blend`
- 실제 사용 GLB: `meshy/models/blender/AST-013/v001/exports/model.glb`
- 제작 방식: blender_direct / Repeatable symmetric office objects and exact layout; reuse existing palette and models.
- 이번 선택 이유: 기존 팔레트·형상·배치 재사용. 새 모델 생성·분리·채색 변경 없음.
- 재사용 제작 스크립트: `meshy/models/blender/AST-020/v001/processing/build_office.py`
- 색상: palette v001 유지, 새 UV 변형 없음. color2 용도: 미사용 기록
- 이번 Meshy·이미지 생성 호출 및 크레딧: 0. 과거 제작 크레딧은 기존 catalog의 0이며 이번 비용과 구분. 토큰 배분 미측정.

- 구성: 기존 메시 통합 소품(분리 애니메이션 추가 없음). 첫 배치 기준 Blender 축 AABB 치수 [1.72, 0.055, 0.46]m. 원본 단품 치수와 배치 배율을 혼동하지 않는다.
- 최종 단품 GLB 12삼각형 × 장면 2개 = 24삼각형.

## 전체 사용 후보 — 고정 workplace-asset-candidates-v003 조회

후보 CND-007 / 비공통 후보. 실제 수량·배치 완료를 뜻하지 않는다.

| 공간 이름 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 수량 |
|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 미정 |


## 실제 사용 이력 — 원장 조회

| 환경·ID | 버전/revision | 수량 | 근거 |
|---|---|---|---|
| Blender/독립 GLB pan-001-office | revision 1 | 2 | `meshy/models/blender/AST-020/v001/placements.json`, `meshy/models/blender/AST-020/v001/inspection.json` |
| Blender/독립 GLB pan-001-office | revision 2 | 2 | `meshy/models/blender/AST-020/v003/placements.json`, `meshy/models/blender/AST-020/v003/inspection.json` |
| Blender/독립 GLB AST-020 v002 보존본(assembly 원장 미등록) | placements 보존 파일 조회 | 2 | `meshy/models/blender/AST-020/v002/placements.json`, `meshy/models/blender/AST-020/v002/inspection.json`; 최신 assembly revision 수량에 합산하지 않음 |
| Unity OfficeAssistant-v001 / OfficeAssistant.unity | use-office-assistant-ast-013-v001-scene revision 2(최신; revision 1 보존) | 2 | `docs/machine/catalog/asset-usages.json`, `docs/machine/evidence/office-assistant-v001/unity-scene.json` |
| Unity 재사용 프리팹 정의 | use-office-assistant-ast-013-v001-prototype revision 1 | 배치 수량 제외 | `unity/projects/OfficeAssistant-v001/Assets/Meshy/AST-013/v001/asset.prefab` |
| Unity WebGL 빌드 포함 | office-assistant-v001, v002, v003 | 각각 2 | 위 scene revision의 build_links; 빌드별 수량을 한 장면에 합산하지 않음 |


실행 검증: 실제 Unity Editor Play Mode와 최종 office-assistant-v003 WebGL. 중간 v001/v002에 최종 실행 pass를 승계하지 않는다. Unity 증거 `docs/machine/evidence/office-assistant-v001/unity-editor-play.json`, 웹 증거 `docs/machine/evidence/office-assistant-v001/webgl-ui-acceptance.json`. 기존 제작 상태 in_progress 유지. 실제 모바일 기기·브라우저별 성능·드로콜은 미검증.

## v005 확대·팝업 적용

같은 에셋 버전·형상·색상·배치 수량을 재사용했다. 사무보조원 v005 빌드 포함과 실제 실행은 `docs/machine/catalog/asset-usages.json`의 최신 scene revision 3에서 조회한다. 이전 revision·빌드 기록은 보존한다. AST-020 조립 부모는 여전히 추가 집계하지 않는다. 신규 검증: `docs/machine/evidence/office-assistant-v005/unity-scene.json`, `docs/machine/evidence/office-assistant-v005/webgl-ui-acceptance.json`. 전체 후보 목록은 위 고정 버전의 모든 공간을 유지한다. v004 중간 빌드에도 같은 수량이 실제 포함되었으며, 해당 빌드의 시각 검수 실패는 원장의 별도 execution_checks에 보존한다.

## 전체 공간 제작 원장 조회 — v001

조회 시각: 2026-10-31T07:24:53.368067+09:00. 후보v004와 정식 조립/Unity 원장의 조회 결과다. 최신 revision만 현재 집계하며 과거/removed/프리팹 정의는 실제 장면 수량에 합산하지 않는다.

고정 모델: AST-013 v001 / 낮은 책상 스크린. 등록 상태: `ready`. 최종 GLB: 12삼각형, 3287712바이트, 모델 재질1개·텍스처1개, 팔레트[2508, 2508].
최신 검수와 미검증 항목: [meshy/models/blender/AST-013/v001/inspection.json](../../../meshy/models/blender/AST-013/v001/inspection.json). 제작 방식/기록: blender_direct / [meshy/models/original/AST-013/v001/README.md](../../../meshy/models/original/AST-013/v001/README.md). 이 버전의 기록된 Meshy비용 0크레딧은 과거 제작 비용과 이번 작업0크레딧을 구별한다. 모델별 토큰·금액 배분은 미측정이다.

### 전체 적용 후보 공간

| 후보 ID·원문 이름 | 정확한 공간 이름 | prompt | panorama | context | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|---|
| CND-007 낮은 책상 스크린 | 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준v003기획 | 미정 |

### 실제 Blender/GLB 조립 사용

| 조립 ID·revision | 현재/과거 | 고정 조립 모델 | 수량·범위 | 근거 |
|---|---|---|---|---|
| pan-001-office revision 1 | 과거 | AST-020 v001 | 2 구성 인스턴스 | [meshy/models/blender/AST-020/v001/placements.json](../../../meshy/models/blender/AST-020/v001/placements.json); [meshy/models/blender/AST-020/v001/inspection.json](../../../meshy/models/blender/AST-020/v001/inspection.json) |
| pan-001-office revision 2 | 과거 | AST-020 v003 | 2 구성 인스턴스 | [meshy/models/blender/AST-020/v003/placements.json](../../../meshy/models/blender/AST-020/v003/placements.json); [meshy/models/blender/AST-020/v003/inspection.json](../../../meshy/models/blender/AST-020/v003/inspection.json) |
| pan-001-office revision 3 | 과거 | AST-020 v004 | 2 구성 인스턴스 | [meshy/models/blender/AST-020/v004/placements.json](../../../meshy/models/blender/AST-020/v004/placements.json); [meshy/models/blender/AST-020/v004/inspection.json](../../../meshy/models/blender/AST-020/v004/inspection.json) |
| pan-001-office revision 4 | 과거 | AST-020 v005 | 2 구성 인스턴스 | [meshy/models/blender/AST-020/v005/placements.json](../../../meshy/models/blender/AST-020/v005/placements.json); [meshy/models/blender/AST-020/v005/inspection.json](../../../meshy/models/blender/AST-020/v005/inspection.json) |
| pan-001-office revision 5 | 현재 | AST-020 v006 | 2 구성 인스턴스 | [meshy/models/blender/AST-020/v006/placements.json](../../../meshy/models/blender/AST-020/v006/placements.json); [meshy/models/blender/AST-020/v006/inspection.json](../../../meshy/models/blender/AST-020/v006/inspection.json) |

### 실제 Unity 사용·빌드·실행

| usage ID·revision | 현재/과거·상태·종류 | 프로젝트 | 장면/프리팹 | 수량 | 빌드 포함 | 실행 검수·근거 |
|---|---|---|---|---|---|---|
| use-office-assistant-ast-013-v001-scene revision 1 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistant.unity | 2 | office-assistant-v001(2), office-assistant-v002(2), office-assistant-v003(2) | editor_scene/None/pass/2026-10-31T04:08:41.1507411+09:00 / Actual Play Mode. Scene instance geometry/colliders verified; graphics inspected in WebGL. / docs/machine/evidence/office-assistant-v001/unity-editor-play.json; build/office-assistant-v001/unverified/None / Build succeeded; full acceptance result is not inherited from final build. / ; build/office-assistant-v002/unverified/None / Build succeeded; full acceptance result is not inherited from final build. / ; build/office-assistant-v003/pass/2026-10-30T19:07:32.970Z / All required gameplay paths tested on final build. / docs/machine/evidence/office-assistant-v001/webgl-ui-acceptance.json |
| use-office-assistant-ast-013-v001-prototype revision 1 | 현재/placed/prefab_definition | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Meshy/AST-013/v001/asset.prefab | 정의; 장면 집계 제외(null) | 이 revision에 등록 없음 | 실행 근거 미등록/미검증 |
| use-office-assistant-ast-013-v001-scene revision 2 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistant.unity | 2 | office-assistant-v001(2), office-assistant-v002(2), office-assistant-v003(2) | editor_scene/None/pass/2026-10-31T04:10:48.3988746+09:00 / Actual Play Mode. Scene instance geometry/colliders verified; graphics inspected in WebGL. / docs/machine/evidence/office-assistant-v001/unity-editor-play.json, docs/machine/evidence/office-assistant-v001/unity-editor-play-manual.log; build/office-assistant-v001/unverified/None / Build succeeded; full acceptance result is not inherited from final build. / ; build/office-assistant-v002/unverified/None / Build succeeded; full acceptance result is not inherited from final build. / ; build/office-assistant-v003/pass/2026-10-30T19:07:32.970Z / All required gameplay paths tested on final build. / docs/machine/evidence/office-assistant-v001/webgl-ui-acceptance.json |
| use-office-assistant-ast-013-v001-scene revision 3 | 현재/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistant.unity | 2 | office-assistant-v004(2), office-assistant-v005(2) | editor_scene/None/pass/2026-10-31T04:27:50.0190168+09:00 / Actual Editor Play Mode on v005 source. / docs/machine/evidence/office-assistant-v005/unity-editor-play.json; build/office-assistant-v005/pass/2026-10-30T19:28:44.330Z / Actual UI controls, closeup/restore, paper popup, mandatory workflow and alternative inputs exercised. / docs/machine/evidence/office-assistant-v005/webgl-ui-acceptance.json; build/office-assistant-v004/fail/2026-10-31T04:26:15.691381+09:00 / Functional UI passed separately; visual review failed on stale pixels outside closeup viewport. Fixed in v005. / docs/machine/evidence/office-assistant-v004/visual-review.json |
| use-workplaces-pan-001-ast-013-v001-scene revision 1 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | 이 revision에 등록 없음 | 실행 근거 미등록/미검증 |
| use-workplaces-pan-001-ast-013-v001-scene revision 2 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | workplaces-v002(2), workplaces-v003(2) | 실행 근거 미등록/미검증 |
| use-workplaces-pan-001-ast-013-v001-scene revision 3 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | 이 revision에 등록 없음 | 실행 근거 미등록/미검증 |
| use-workplaces-pan-001-ast-013-v001-scene revision 4 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | workplaces-v005(2) | 실행 근거 미등록/미검증 |
| use-workplaces-pan-001-ast-013-v001-scene revision 5 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | workplaces-v005(2) | editor_scene/None/pass/2026-10-31T06:52:23.6874000+09:00 / Actual Play Mode room load, geometry, colliders, shared model material/texture and2508px import; nographics, no visual/interaction/WebGL inference. / docs/machine/evidence/workplaces-v005/unity-editor-play-rooms.json, docs/machine/evidence/workplaces-v005/unity-editor-play.log |
| use-workplaces-pan-001-ast-013-v001-scene revision 6 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | workplaces-v005(2) | editor_scene/None/pass/2026-10-31T06:52:23.6874000+09:00 / Actual Play Mode room load, geometry, colliders, shared model material/texture and2508px import; nographics, no visual/interaction/WebGL inference. / docs/machine/evidence/workplaces-v005/unity-editor-play-rooms.json, docs/machine/evidence/workplaces-v005/unity-editor-play.log; build/workplaces-v005/pass/2026-10-30T21:52:26.053Z / Room exploration only: actual entered/captured geometry, shared material/palette2508px. Office direct-work900x600 focus failed; no complete career interaction/protocol acceptance claimed. / docs/machine/evidence/workplaces-v005/http-webgl-rooms.json, docs/machine/evidence/workplaces-v005/PAN-001-http-front.png, docs/machine/evidence/workplaces-v005/PAN-001-http-reduced.png |
| use-workplaces-pan-001-ast-013-v001-scene revision 7 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | workplaces-v005(2), workplaces-v006(2) | 실행 근거 미등록/미검증 |
| use-workplaces-pan-001-ast-013-v001-scene revision 8 | 과거/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | workplaces-v005(2), workplaces-v006(2) | editor_scene/None/pass/2026-10-31T07:08:32.8363824+09:00 / Actual v006 native Play room load, geometry, collider, shared material/texture and2508px import. Batchmode nographics does not establish visual, WebGL or career-workflow acceptance. / docs/machine/evidence/workplaces-v006/unity-editor-play-rooms.json, docs/machine/evidence/workplaces-v006/unity-editor-play.log |
| use-workplaces-pan-001-ast-013-v001-scene revision 9 | 현재/placed/scene_instances | unity/projects/OfficeAssistant-v001 | unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity | 2 | workplaces-v005(2), workplaces-v006(2) | editor_scene/None/pass/2026-10-31T07:08:32.8363824+09:00 / Actual v006 native Play room load, geometry, collider, shared material/texture and2508px import. Batchmode nographics does not establish visual, WebGL or career-workflow acceptance. / docs/machine/evidence/workplaces-v006/unity-editor-play-rooms.json, docs/machine/evidence/workplaces-v006/unity-editor-play.log; build/workplaces-v006/pass/2026-10-30T22:09:35.075Z / Actual v006 room exploration: geometry/palette2508px/shared material and normal/reduced images. Full office direct-work/protocol and final visual acceptance recorded separately; other551career drafts not implemented by this check. / docs/machine/evidence/workplaces-v006/http-webgl-rooms.json, docs/machine/evidence/workplaces-v006/PAN-001-http-front.png, docs/machine/evidence/workplaces-v006/PAN-001-http-reduced.png |

Unity 단일 원장: [docs/machine/catalog/asset-usages.json](../../machine/catalog/asset-usages.json). 조립 단일 원장: [docs/machine/catalog/scene-assemblies.json](../../machine/catalog/scene-assemblies.json). 각 ID/revision의 instances·transform·evidence는 해당 정식 원장에서 조회한다. 프리팹 quantity:null은 수량0이 아니며 장면 배치가 아니다.

### 실제 검수 범위와 한계

각 고정 inspection과 대상 빌드의 실제 근거를 따른다. 과거 pass는 새 모델·빌드에 승계하지 않는다. Native -nographics, HTTP 공간 탐색, 직접 작업/통신, 다른 장치/브라우저의 미검증 범위를 구별한다.

<!-- BEGIN office-ten-scene-usage-ast-013-v001 -->
## OfficeTen 신규10종 실제 공유 사용

이 절은 정식 사용 원장의 최신 조회 결과입니다. 기존 모든 사용 후보·다른 배치 이력은 위 명세를 함께 조회합니다.

| 사용 ID/revision | 프로젝트·장면 | 수량 | 실제 인스턴스 |
|---|---|---:|---|
| use-office-ten-ast-013-v001 / 4 | unity/projects/OfficeAssistant-v001 / unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeTen.unity | 2 | AST-013-0, AST-013-1 |

공유 컨텍스트 office-shared-work v001 / PRM-001 v002 / PAN-001 v001. 기존 모델 재사용, 새 유료 호출 없음.

| 시나리오 | 버전 | 직업 ID·이름 |
|---|---|---|
| career-net-208-experience | v002 | career-net-208 국제무역사무원 |
| career-net-10118-experience | v002 | career-net-10118 데이터 라벨러 |
| career-net-252-experience | v002 | career-net-252 법률사무원 |
| career-net-1432-experience | v002 | career-net-1432 베타테스터 |
| career-net-10032-experience | v002 | career-net-10032 빅 데이터 전문가 |
| career-net-462-experience | v002 | career-net-462 사이버교육운영자 |
| career-net-459-experience | v002 | career-net-459 속기사 |
| career-net-230-experience | v002 | career-net-230 시장 및 여론조사전문가 |
| career-net-378-experience | v002 | career-net-378 전문비서 |
| career-net-258-experience | v002 | career-net-258 회계사무원 |

빌드 포함 v001/v002/v003. v001 드래그 실패·v002 반복 집계 오류 중간본을 보존합니다. 최종 v003 Native 선택·형상10건/HTTP업무10건/공통17건은 별도 증거입니다. 10종 공유 장면의30배치를10배로 계산하지 않습니다.

[사용 원장](../../machine/catalog/asset-usages.json) · [최종 빌드·범위](../builds/office-ten-v003.md) · [직업별 명세](../jobs/office-ten-experiences-v004.md)

<!-- END office-ten-scene-usage-ast-013-v001 -->


<!-- career-pilot-v004:start -->
## career-pilot-v004 실제 재사용 검토

2026-10-31T04:04:03.850Z 기준 단일 원장의 usage_id별 최신 revision 조회이다. 모델 원본/Blender/GLB 버전·팔레트·후보 공간은 변경하지 않았다. 이번 신규 제작0, Meshy호출/크레딧0, 실제 대화 토큰·에셋별 노력시간 미측정null. 고정 빌드 사본은 동일 OfficeAssistant-v001 프로젝트 identity로 취급하며 독립 에셋 프로젝트 등록이 아니다.

확인된 모든 포함 빌드: office-assistant-v001, office-assistant-v002, office-assistant-v003, office-assistant-v004, office-assistant-v005, workplaces-v001, workplaces-v002, workplaces-v003, workplaces-v004, workplaces-v005, workplaces-v006, office-ten-v001, office-ten-v002, office-ten-v003, workplaces-v009, career-pilot-v004. 조립 부모는 구성 에셋 배치를 세는 빌드에서 별도 배치로 가산하지 않는다. 각 빌드의 실제 검증 범위는 builds.json 및 해당 원본 증거를 따른다.

|사용 ID / 최신 revision|유형·상태|프로젝트|장면 또는 프리팹|수량|포함 빌드·수량|실행 검수·근거|
|---|---|---|---|---:|---|---|
|use-office-assistant-ast-013-v001-scene / 3|scene_instances / placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistant.unity|2|office-assistant-v004:2, office-assistant-v005:2|editor_scene/editor/pass docs/machine/evidence/office-assistant-v005/unity-editor-play.json; build/office-assistant-v005/pass docs/machine/evidence/office-assistant-v005/webgl-ui-acceptance.json; build/office-assistant-v004/fail docs/machine/evidence/office-assistant-v004/visual-review.json|
|use-office-assistant-ast-013-v001-prototype / 1|prefab_definition / placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Meshy/AST-013/v001/asset.prefab|정의·수량 해당없음|||
|use-workplaces-pan-001-ast-013-v001-scene / 10|scene_instances / placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity|2|workplaces-v005:2, workplaces-v006:2, career-pilot-v004:2|editor_scene/editor/pass docs/machine/evidence/workplaces-v006/unity-editor-play-rooms.json, docs/machine/evidence/workplaces-v006/unity-editor-play.log; build/workplaces-v006/pass docs/machine/evidence/workplaces-v006/http-webgl-rooms.json, docs/machine/evidence/workplaces-v006/PAN-001-http-front.png, docs/machine/evidence/workplaces-v006/PAN-001-http-reduced.png; editor_scene/editor/pass docs/machine/evidence/career-pilot-v004/unity-editor-play-rooms.json, docs/machine/evidence/career-pilot-v004/unity-editor-play.log; build/career-pilot-v004/pass docs/machine/evidence/career-pilot-v004/http-rooms-r003/http-rooms-and-scene-leave.json, docs/machine/evidence/career-pilot-v004/http-rooms-r003/PAN-001-overview.png, docs/machine/evidence/career-pilot-v004/office-regression/office-regression.json|
|use-office-ten-ast-013-v001 / 2|scene_instances / placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeTen.unity|2|office-ten-v001:2, office-ten-v002:2, office-ten-v003:2|editor_scene/editor/pass docs/machine/evidence/office-ten-v002/unity-editor-play.json, docs/machine/evidence/office-ten-v002/unity-scene.json; editor_scene/office-ten-v003/pass docs/machine/evidence/office-ten-v003/unity-editor-play.json, docs/machine/evidence/office-ten-v003/unity-scene.json; webgl/office-ten-v003/pass docs/machine/evidence/office-ten-v003/browser-first5/acceptance.json, docs/machine/evidence/office-ten-v003/browser-last5/last-five-actual-http.json, docs/machine/evidence/office-ten-v003/browser-common/protocol-http-acceptance.json|

instances·transform과 고정 사본 출처는 각 ID/revision의 원장을 조회한다.

원장: docs/machine/catalog/asset-usages.json. 신규 직접 작업의 실행 pass는 시나리오의 지정3물건과30작업면에 한정한다. 배경 물건의 조작·실제 장비 동작·모든브라우저·물리모바일기기 검수를 뜻하지 않는다.
<!-- career-pilot-v004:end -->


<!-- career-pilot-v005:start -->
## career-pilot-v005 최신 실제 사용 조회

2026-10-31T04:30:53.239Z 기준. 모델/Blender/GLB/팔레트/전체후보 공간은 기존 고정 버전을 보존했다. 신규 모델제작0, 이번Meshy호출/크레딧0, 실제토큰/순수노력시간 미측정null. 동일 프로젝트의 고정 빌드 사본 사용이며 다중 프로젝트 에셋 등록이 아니다.

모든 포함 빌드: office-assistant-v001, office-assistant-v002, office-assistant-v003, office-assistant-v004, office-assistant-v005, workplaces-v001(중간후보), workplaces-v002(중간후보), workplaces-v003(중간후보), workplaces-v004(중간후보), workplaces-v005(중간후보), workplaces-v006, office-ten-v001(중간후보), office-ten-v002(중간후보), office-ten-v003, workplaces-v009, career-pilot-v004(중간후보), career-pilot-v005. 조립 source부모는 구성배치 수량에 가산하지 않는다. v004는 기능/패키지 검증 뒤 카드 가독성 문제로 전달에서 제외하고 보존했다.

|사용ID/revision|유형/상태|프로젝트|장면/프리팹|수량|전체 빌드 포함·수량|전체 실행 검수·근거|
|---|---|---|---|---:|---|---|
|use-office-assistant-ast-013-v001-scene/3|scene_instances/placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistant.unity|2|office-assistant-v004:2, office-assistant-v005:2|editor_scene/editor/pass docs/machine/evidence/office-assistant-v005/unity-editor-play.json; build/office-assistant-v005/pass docs/machine/evidence/office-assistant-v005/webgl-ui-acceptance.json; build/office-assistant-v004/fail docs/machine/evidence/office-assistant-v004/visual-review.json|
|use-office-assistant-ast-013-v001-prototype/1|prefab_definition/placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Meshy/AST-013/v001/asset.prefab|정의·수량해당없음|||
|use-workplaces-pan-001-ast-013-v001-scene/11|scene_instances/placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity|2|workplaces-v005:2, workplaces-v006:2, career-pilot-v004:2, career-pilot-v005:2|editor_scene/editor/pass docs/machine/evidence/workplaces-v006/unity-editor-play-rooms.json, docs/machine/evidence/workplaces-v006/unity-editor-play.log; build/workplaces-v006/pass docs/machine/evidence/workplaces-v006/http-webgl-rooms.json, docs/machine/evidence/workplaces-v006/PAN-001-http-front.png, docs/machine/evidence/workplaces-v006/PAN-001-http-reduced.png; editor_scene/editor/pass docs/machine/evidence/career-pilot-v004/unity-editor-play-rooms.json, docs/machine/evidence/career-pilot-v004/unity-editor-play.log; build/career-pilot-v004/pass docs/machine/evidence/career-pilot-v004/http-rooms-r003/http-rooms-and-scene-leave.json, docs/machine/evidence/career-pilot-v004/http-rooms-r003/PAN-001-overview.png, docs/machine/evidence/career-pilot-v004/office-regression/office-regression.json; editor_scene/editor/pass docs/machine/evidence/career-pilot-v005/unity-editor-play-rooms.json, docs/machine/evidence/career-pilot-v005/unity-editor-play.log; build/career-pilot-v005/pass docs/machine/evidence/career-pilot-v005/http-rooms-r003/http-rooms-and-scene-leave.json, docs/machine/evidence/career-pilot-v005/http-rooms-r003/PAN-001-overview.png|
|use-office-ten-ast-013-v001/2|scene_instances/placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeTen.unity|2|office-ten-v001:2, office-ten-v002:2, office-ten-v003:2|editor_scene/editor/pass docs/machine/evidence/office-ten-v002/unity-editor-play.json, docs/machine/evidence/office-ten-v002/unity-scene.json; editor_scene/office-ten-v003/pass docs/machine/evidence/office-ten-v003/unity-editor-play.json, docs/machine/evidence/office-ten-v003/unity-scene.json; webgl/office-ten-v003/pass docs/machine/evidence/office-ten-v003/browser-first5/acceptance.json, docs/machine/evidence/office-ten-v003/browser-last5/last-five-actual-http.json, docs/machine/evidence/office-ten-v003/browser-common/protocol-http-acceptance.json|

각 ID/revision의 instances·transform·고정build사본 근거는 docs/machine/catalog/asset-usages.json에서 조회한다.

실제 조작 pass는 선택된3물건과지정기본업무에한정하며배경물건조작·전문가정답·모든설정·실물모바일/nativeGUI검수를 뜻하지 않는다.
<!-- career-pilot-v005:end -->


### 메모·좌석 방향 수정본 v006

[office-ten-v006](../builds/office-ten-v006.md)에 같은 모델 버전을 재사용했습니다. 최신 사용 원장 use-office-ten-ast-013-v001 revision3에서 조회합니다. 새 모델·팔레트 변경 없이 메모 배경만 반투명하게 조정했고 AST-003-0/1만 각 책상을 향하도록180도 회전했습니다. 수량·인스턴스ID·전체4308삼각형은 유지됩니다. v004/v005는 보존 중간본, v006의 실제UI/좌석 시각 검수와 v003의10종 전체업무 검수는 구분합니다.


### 모니터 안 한글 미리보기 v007

[office-ten-v007](../builds/office-ten-v007.md)에 같은 고정 모델을 재사용했습니다. 최신 사용 use-office-ten-ast-013-v001 revision4이며 배치/수량/공용팔레트는 그대로입니다. 기존 모니터의 실제 화면 면에 동적 한글 UI를 맞추고 큰 종이 overlay를 제거했습니다. UI폰트 글자 메시를 새로운 AST모델이나 모델재질로 등록하지 않습니다. 현재 모니터·한글 표시/입력 검수와 과거v003 전체업무 검수는 구분합니다.


<!-- career-pilot-v007:start -->
## career-pilot-v007 최신 실제 사용 조회

2026-10-31T05:48:10.226Z 원장 조회. 고정 모델·Blender·GLB·공용 팔레트와 위 전체 후보 공간을 변경하지 않았다. 이번 신규 모델0, Meshy호출·크레딧0, 입력·캐시·출력 토큰과 순수노력시간은 미측정null.

전체 포함 빌드: office-assistant-v001, office-assistant-v002, office-assistant-v003, office-assistant-v004, office-assistant-v005, workplaces-v001(중간후보), workplaces-v002(중간후보), workplaces-v003(중간후보), workplaces-v004(중간후보), workplaces-v005(중간후보), workplaces-v006, office-ten-v001(중간후보), office-ten-v002(중간후보), office-ten-v003, workplaces-v009, career-pilot-v004(중간후보), career-pilot-v005(배치 오류 발견, 이전 전달본), office-ten-v004(중간후보), office-ten-v005(중간후보), office-ten-v006, office-ten-v007, career-pilot-v007, career-pilot-v006(중간후보). 조립 source 부모는 구성 배치 수량에 중복 합산하지 않는다. 이번 UI 배치 수정과 실제 HTTP 검수는 [빌드 설명](../builds/career-pilot-v007.md)을 따른다.

|사용ID/revision|유형/상태|프로젝트|장면/프리팹|수량|전체 빌드 포함·수량|전체 실행 검수·근거|
|---|---|---|---|---:|---|---|
|use-office-assistant-ast-013-v001-prototype/1|prefab_definition/placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Meshy/AST-013/v001/asset.prefab|정의·수량해당없음|||
|use-office-assistant-ast-013-v001-scene/3|scene_instances/placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistant.unity|2|office-assistant-v004:2, office-assistant-v005:2|editor_scene/editor/pass docs/machine/evidence/office-assistant-v005/unity-editor-play.json; build/office-assistant-v005/pass docs/machine/evidence/office-assistant-v005/webgl-ui-acceptance.json; build/office-assistant-v004/fail docs/machine/evidence/office-assistant-v004/visual-review.json|
|use-office-ten-ast-013-v001/4|scene_instances/placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeTen.unity|2|office-ten-v001:2, office-ten-v002:2, office-ten-v003:2, office-ten-v004:2, office-ten-v005:2, office-ten-v006:2, office-ten-v007:2|editor_scene/editor/pass docs/machine/evidence/office-ten-v002/unity-editor-play.json, docs/machine/evidence/office-ten-v002/unity-scene.json; editor_scene/office-ten-v003/pass docs/machine/evidence/office-ten-v003/unity-editor-play.json, docs/machine/evidence/office-ten-v003/unity-scene.json; webgl/office-ten-v003/pass docs/machine/evidence/office-ten-v003/browser-first5/acceptance.json, docs/machine/evidence/office-ten-v003/browser-last5/last-five-actual-http.json, docs/machine/evidence/office-ten-v003/browser-common/protocol-http-acceptance.json; webgl/office-ten-v006/pass docs/machine/evidence/office-ten-v006/browser/visual-qa.json, docs/machine/evidence/office-ten-v006/chair-facing.json, docs/machine/evidence/office-ten-v006/unity-scene.json; webgl/office-ten-v007/pass docs/machine/evidence/office-ten-v007/browser/visual-qa.json, docs/machine/evidence/office-ten-v007/unity-scene.json|
|use-workplaces-pan-001-ast-013-v001-scene/12|scene_instances/placed|unity/projects/OfficeAssistant-v001|unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity|2|workplaces-v005:2, workplaces-v006:2, career-pilot-v004:2, career-pilot-v005:2, career-pilot-v006:2, career-pilot-v007:2|editor_scene/editor/pass docs/machine/evidence/workplaces-v006/unity-editor-play-rooms.json, docs/machine/evidence/workplaces-v006/unity-editor-play.log; build/workplaces-v006/pass docs/machine/evidence/workplaces-v006/http-webgl-rooms.json, docs/machine/evidence/workplaces-v006/PAN-001-http-front.png, docs/machine/evidence/workplaces-v006/PAN-001-http-reduced.png; editor_scene/editor/pass docs/machine/evidence/career-pilot-v004/unity-editor-play-rooms.json, docs/machine/evidence/career-pilot-v004/unity-editor-play.log; build/career-pilot-v004/pass docs/machine/evidence/career-pilot-v004/http-rooms-r003/http-rooms-and-scene-leave.json, docs/machine/evidence/career-pilot-v004/http-rooms-r003/PAN-001-overview.png, docs/machine/evidence/career-pilot-v004/office-regression/office-regression.json; editor_scene/editor/pass docs/machine/evidence/career-pilot-v005/unity-editor-play-rooms.json, docs/machine/evidence/career-pilot-v005/unity-editor-play.log; build/career-pilot-v005/pass docs/machine/evidence/career-pilot-v005/http-rooms-r003/http-rooms-and-scene-leave.json, docs/machine/evidence/career-pilot-v005/http-rooms-r003/PAN-001-overview.png; build/career-pilot-v007/pass docs/machine/evidence/career-pilot-v007/http-rooms-r003/http-rooms-and-scene-leave.json, docs/machine/evidence/career-pilot-v007/http-rooms-r003/PAN-001-overview.png|

단일 원장 docs/machine/catalog/asset-usages.json의 각 ID/revision에서 instances·transform·실제 근거를 조회한다. 최신 revision만 현재 사용으로 집계한다. v007 새 pass는 실제 HTTP 공간 표시이며 선택된3물건의 업무는 별도10직업/30작업면·물류9건으로 검수했다. 과거Native/다른빌드 pass를 v007로 승계하지 않았다. 실물 모바일·Native GUI·전문 업무 정확성은 미검증이다.
<!-- career-pilot-v007:end -->

<!-- spatial-diversity-v011 -->
## 공간 특색 보강 v011 원장 조회 — 낮은 책상 스크린
조회 2026-10-31T15:00:55.263632+09:00. `AST-013` `v001`, 상태 `ready`. 방식 `blender_direct`. Repeatable symmetric office objects and exact layout; reuse existing palette and models.
구성: AST-013.
가상 모델 치수(m): 미등록. 최종 GLB 실제 재열기 12삼각형 · 3287712바이트 · 재질1 · 텍스처1. 공용 palette v0012508×2508. 치수는 실제 장소 실측이 아니다.
원본 `meshy/models/original/AST-013/v001/source.blend` · 수정본 `meshy/models/blender/AST-013/v001/model.blend` · 사용본 `meshy/models/blender/AST-013/v001/exports/model.glb` · 제작 기록 `meshy/models/original/AST-013/v001/README.md` · 검사 `meshy/models/blender/AST-013/v001/inspection.json`.
재사용 기준: `별도 고정 참조 미등록`. 색상 변형: null.

### 전체 적용 후보

| 후보 | 정확한 공간 | prompt 고정 참조 | panorama 고정 참조 | context |
|---|---|---|---|---|
| CND-007 | 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | [{"context_id": "office-shared-work", "version": "v001"}] |

### 실제 Blender/GLB 조립 사용 — 전체 이력

| 조립·revision | 현재/과거 | 고정 버전 수량 | 근거 |
|---|---|---|---|
| pan-001-office rev1 | 보존 과거 | 2개 | `meshy/models/blender/AST-020/v001/placements.json` |
| pan-001-office rev2 | 보존 과거 | 2개 | `meshy/models/blender/AST-020/v003/placements.json` |
| pan-001-office rev3 | 보존 과거 | 2개 | `meshy/models/blender/AST-020/v004/placements.json` |
| pan-001-office rev4 | 보존 과거 | 2개 | `meshy/models/blender/AST-020/v005/placements.json` |
| pan-001-office rev5 | 보존 과거 | 2개 | `meshy/models/blender/AST-020/v006/placements.json` |
| pan-001-office rev6 | 보존 과거 | 2개 | `meshy/models/blender/AST-020/v007/placements.json` |
| pan-001-office rev7 | 현재 | 2개 | `meshy/models/blender/AST-020/v008/placements.json` |

### 실제 Unity 사용·빌드 — usage별 최신 revision

| usage·revision | 장면/프리팹 | 수량 | 빌드 | 실행 검증 |
|---|---|---|---|---|
| use-office-assistant-ast-013-v001-scene rev3 / placed | `unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistant.unity` | 2 | office-assistant-v004, office-assistant-v005 | editor_scene:pass, build:pass, build:fail |
| use-office-assistant-ast-013-v001-prototype rev1 / placed | `unity/projects/OfficeAssistant-v001/Assets/Meshy/AST-013/v001/asset.prefab` | 정의; 합산 제외 | 포함 근거 미등록 | 미검증 |
| use-workplaces-pan-001-ast-013-v001-scene rev12 / placed | `unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeAssistantDirect.unity` | 2 | workplaces-v005, workplaces-v006, career-pilot-v004, career-pilot-v005, career-pilot-v006, career-pilot-v007 | editor_scene:pass, build:pass, editor_scene:pass, build:pass, editor_scene:pass, build:pass, build:pass |
| use-office-ten-ast-013-v001 rev4 / placed | `unity/projects/OfficeAssistant-v001/Assets/Scenes/OfficeTen.unity` | 2 | office-ten-v001, office-ten-v002, office-ten-v003, office-ten-v004, office-ten-v005, office-ten-v006, office-ten-v007 | editor_scene:pass, editor_scene:pass, webgl:pass, webgl:pass, webgl:pass |
| use-spatial-workplaces-v010-pan-001-ast-013-v001 rev1 / placed | `unity/projects/OfficeAssistant-v001/Assets/Scenes/Workplaces/PAN-001-detail-v010.unity` | 2 | workplaces-v010 | 미검증 |
| use-spatial-workplaces-v011-pan-001-ast-013-v001 rev1 / placed | `unity/projects/OfficeAssistant-v001/Assets/Scenes/Workplaces/PAN-001-detail-v011.unity` | 2 | workplaces-v011 | build:pass |

후보와 실제 사용은 별개다. 현재 registry 장면과 보존 과거 장면을 구분하며 과거 revision 전체는 원장에 보존한다. 조립 부모·구성 자식·프리팹 정의를 장면 수량에 중복 합산하지 않는다.

이번 Meshy 자연물 원본 1묶음 실제20크레딧. 기존 꽃·장식 원본40크레딧은 과거 비용이며 이번 재사용 추가0. 자연물4종별 비용·입력/캐시/출력 토큰·금액·시간 배분은 도구가 제공하지 않아 미측정(null). 유료 재생성/refine/remesh/이미지 생성0.

실제 검수와 미검증 범위: `meshy/models/blender/AST-013/v001/inspection.json`, `docs/machine/evidence/workplaces-v011/visual-review.json`. Editor Play Mode·다른 장치/브라우저·전체 직업 업무/React 통신 회귀는 미검증. 개별 소품 상세 검수가 없는 경우 in_progress를 유지한다.

<!-- office-ten-v008:start -->
## 사무실10종 최신 사용 기록 — v008

위 이전 빌드별 표는 해당 시점 기록입니다. 이 사용 ID의 현재값은 원장 최신 revision5이며 같은 장면 배치를 중복 합산하지 않습니다. 고정 모델·배치·후보 공간은 유지하고 입력 브리지만 수정했습니다.

|사용ID/revision|장면 수량|빌드 포함|실행 범위|
|---|---:|---|---|
|use-office-ten-ast-013-v001/5|2|office-ten-v008:2|Chrome CDP 한글 조합·입력 범위만 확인; 전체10업무·공통17은v003 기록|

[실제 빌드와 한계](../builds/office-ten-v008.md) · [입력 관측](../../machine/evidence/office-ten-v008/browser/input-scope-summary.json). 관측7상태를 독립7검수로 세지 않습니다. physical OS/mobile IME, IAB 전용, 마지막 Enter 제출은 새 pass가 아닙니다.
<!-- office-ten-v008:end -->

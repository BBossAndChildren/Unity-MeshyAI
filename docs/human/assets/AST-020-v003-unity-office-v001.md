# AST-020 v003 — PAN-001 일반 사무실 — 위치·회전 정렬 Unity 재사용 기록

2026-10-31. 이 설명은 asset-usages와 scene-assemblies의 조회 결과이며 독립 사용 원장이 아니다. 기존 원본·Blender·GLB 버전과 제작 상태를 보존했다.

## 형상·제작·재사용

- 원본: `meshy/models/original/AST-020/v003/source.blend`
- Blender 수정본: `meshy/models/blender/AST-020/v003/model.blend`
- 실제 사용 GLB: `meshy/models/blender/AST-020/v003/exports/model.glb`
- 제작 방식: blender_direct / Reuse all props; align positions, functional facing and editable instance transforms.
- 이번 선택 이유: 기존 팔레트·형상·배치 재사용. 새 모델 생성·분리·채색 변경 없음.
- 재사용 제작 스크립트: `meshy/models/blender/AST-020/v003/processing/align_office.py`, `meshy/models/blender/AST-020/v001/processing/build_office.py`, `meshy/models/blender/AST-020/v003/processing/export_unity_office.py`
- 색상: palette v001 유지, 새 UV 변형 없음. color2 용도: 미사용 기록
- 이번 Meshy·이미지 생성 호출 및 크레딧: 0. 과거 제작 크레딧은 기존 catalog의 0이며 이번 비용과 구분. 토큰 배분 미측정.

- 구성: 17개 에셋 버전·30개 메시 인스턴스의 사무실 조립본. 최종 GLB와 Unity 장면 각각 4,308삼각형. 집계는 구성 단위이며 이 조립 부모를 추가 합산하지 않는다.

## 전체 사용 후보 — 고정 workplace-asset-candidates-v003 조회

해당 고정 후보 목록에서 개별 연결 미등록. 이를 다른 공간 사용 불가로 해석하지 않는다. 조립본의 실제 참고 공간은 공용 업무 사무실, PRM-001 v001, PAN-001 v001, office-shared-work v001이다.


## 실제 사용 이력 — 원장 조회

| 환경·ID | 버전/revision | 수량 | 근거 |
|---|---|---|---|
| Blender/독립 GLB pan-001-office 조립본 | revision 2 | 1 조립본(구성 합계와 중복 집계 금지) | `meshy/models/blender/AST-020/v003/placements.json`, `meshy/models/blender/AST-020/v003/inspection.json` |
| Unity OfficeAssistant-v001 | 원본 조립 모델 → office.fbx 소스 컨테이너 | 구성 30개로 조회; 조립 부모 수량 추가 없음 | `unity/projects/OfficeAssistant-v001/Assets/Meshy/AST-020/v003/office.fbx`, `docs/machine/evidence/office-assistant-v001/unity-scene.json` |


실행 검증: 실제 Unity Editor Play Mode와 최종 office-assistant-v003 WebGL. 중간 v001/v002에 최종 실행 pass를 승계하지 않는다. Unity 증거 `docs/machine/evidence/office-assistant-v001/unity-editor-play.json`, 웹 증거 `docs/machine/evidence/office-assistant-v001/webgl-ui-acceptance.json`. 기존 제작 상태 in_progress 유지. 실제 모바일 기기·브라우저별 성능·드로콜은 미검증.

## v005 확대·팝업 적용

같은 에셋 버전·형상·색상·배치 수량을 재사용했다. 사무보조원 v005 빌드 포함과 실제 실행은 `docs/machine/catalog/asset-usages.json`의 최신 scene revision 3에서 조회한다. 이전 revision·빌드 기록은 보존한다. AST-020 조립 부모는 여전히 추가 집계하지 않는다. 신규 검증: `docs/machine/evidence/office-assistant-v005/unity-scene.json`, `docs/machine/evidence/office-assistant-v005/webgl-ui-acceptance.json`. 전체 후보 목록은 위 고정 버전의 모든 공간을 유지한다. v004 중간 빌드에도 같은 수량이 실제 포함되었으며, 해당 빌드의 시각 검수 실패는 원장의 별도 execution_checks에 보존한다.

## 실제 부품·색상 칸과 조립 예산

아래는 해당 고정 버전 inspection.json의 실제 최종 GLB 부품/UV 조사값이다. Blender의 색상 칸 행·열은 원본 좌상단0기준이며, 색상 변형은 저장된 고정 버전으로 구별한다.

| 고정 구성 에셋 | 실제 모델 이름 | 개당 삼각형 | 반복 수량 | 합계 삼각형 |
|---|---|---:|---:|---:|
| [AST-001 v002](AST-001-v002-unity-office-v001.md) | COM-01 둥근 모서리 바닥판 — Blender 직접 제작 | 220 | 1 | 220 |
| [AST-002 v001](AST-002-v001-unity-office-v001.md) | COM-02 바닥 표면 — Blender 직접 제작 | 108 | 1 | 108 |
| [AST-003 v001](AST-003-v001-unity-office-v001.md) | COM-04 회전 사무의자 — blender_direct | 792 | 2 | 1584 |
| [AST-004 v001](AST-004-v001-unity-office-v001.md) | 업무 책상 | 60 | 2 | 120 |
| [AST-005 v001](AST-005-v001-unity-office-v001.md) | 모니터 | 48 | 2 | 96 |
| [AST-006 v001](AST-006-v001-unity-office-v001.md) | 키보드 | 12 | 2 | 24 |
| [AST-007 v001](AST-007-v001-unity-office-v001.md) | 마우스 | 12 | 2 | 24 |
| [AST-008 v001](AST-008-v001-unity-office-v001.md) | 책상 아래 서랍장 | 84 | 2 | 168 |
| [AST-009 v001](AST-009-v001-unity-office-v001.md) | 복합기 | 144 | 1 | 144 |
| [AST-010 v001](AST-010-v001-unity-office-v001.md) | 화분 | 308 | 3 | 924 |
| [AST-011 v001](AST-011-v001-unity-office-v001.md) | 책 묶음 | 72 | 3 | 216 |
| [AST-012 v001](AST-012-v001-unity-office-v001.md) | 펜꽂이 | 76 | 2 | 152 |
| [AST-013 v001](AST-013-v001-unity-office-v001.md) | 낮은 책상 스크린 | 12 | 2 | 24 |
| [AST-014 v001](AST-014-v001-unity-office-v001.md) | 관절 스탠드 | 96 | 2 | 192 |
| [AST-015 v001](AST-015-v001-unity-office-v001.md) | 뒤쪽 수납장 | 60 | 1 | 60 |
| [AST-016 v001](AST-016-v001-unity-office-v001.md) | 옷걸이 | 168 | 1 | 168 |
| [AST-017 v001](AST-017-v001-unity-office-v001.md) | 업무용 가방 | 84 | 1 | 84 |

반복을 포함한 최종 GLB 합계 4308삼각형. 구성 소품과 조립 부모를 같은 합계에 중복 포함하지 않는다.

## 전체 공간 제작 원장 조회 — v001

조회 시각: 2026-10-31T07:24:53.368067+09:00. 후보v004와 정식 조립/Unity 원장의 조회 결과다. 최신 revision만 현재 집계하며 과거/removed/프리팹 정의는 실제 장면 수량에 합산하지 않는다.

고정 모델: AST-020 v003 / PAN-001 일반 사무실 — 위치·회전 정렬. 등록 상태: `in_progress`. 최종 GLB: 4308삼각형, 3608484바이트, 모델 재질1개·텍스처1개, 팔레트[2508, 2508].
최신 검수와 미검증 항목: [meshy/models/blender/AST-020/v003/inspection.json](../../../meshy/models/blender/AST-020/v003/inspection.json). 제작 방식/기록: blender_direct / [meshy/models/original/AST-020/v003/README.md](../../../meshy/models/original/AST-020/v003/README.md). 이 버전의 기록된 Meshy비용 0크레딧은 과거 제작 비용과 이번 작업0크레딧을 구별한다. 모델별 토큰·금액 배분은 미측정이다.

### 전체 적용 후보 공간

| 후보 ID·원문 이름 | 정확한 공간 이름 | prompt | panorama | context | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|---|
| 후보 연결 미등록 | 미확인 | 미등록 | 미등록 | 미등록 | 원장 연결 없음 | 미정 |

### 실제 Blender/GLB 조립 사용

| 조립 ID·revision | 현재/과거 | 고정 조립 모델 | 수량·범위 | 근거 |
|---|---|---|---|---|
| pan-001-office revision 2 | 과거 | AST-020 v003 | 조립 결과 정의; 구성과 중복 집계 제외 | [meshy/models/blender/AST-020/v003/placements.json](../../../meshy/models/blender/AST-020/v003/placements.json); [meshy/models/blender/AST-020/v003/inspection.json](../../../meshy/models/blender/AST-020/v003/inspection.json) |

### 실제 Unity 사용·빌드·실행

| usage ID·revision | 현재/과거·상태·종류 | 프로젝트 | 장면/프리팹 | 수량 | 빌드 포함 | 실행 검수·근거 |
|---|---|---|---|---|---|---|
| 실제 Unity 사용 이력 미등록/미검증 | 미확인 | 미등록 | 미등록 | 미정 | 미등록 | 미검증 |

Unity 단일 원장: [docs/machine/catalog/asset-usages.json](../../machine/catalog/asset-usages.json). 조립 단일 원장: [docs/machine/catalog/scene-assemblies.json](../../machine/catalog/scene-assemblies.json). 각 ID/revision의 instances·transform·evidence는 해당 정식 원장에서 조회한다. 프리팹 quantity:null은 수량0이 아니며 장면 배치가 아니다.

### 실제 검수 범위와 한계

각 고정 inspection과 대상 빌드의 실제 근거를 따른다. 과거 pass는 새 모델·빌드에 승계하지 않는다. Native -nographics, HTTP 공간 탐색, 직접 작업/통신, 다른 장치/브라우저의 미검증 범위를 구별한다.

# 전체 에셋 목록

- [직업체험 전체 에셋 재사용·후보·현재 사용 조회 v002](career-asset-reuse-report-v002.md): 427개 에셋 버전(구성355+조립72), 모든 공간 후보와 1,665개 시나리오 물건 참조, 2,778개 최신 사용 원장 기록을 빠짐없이 조회합니다. 새 빌드의 실행 근거는 별도로 갱신합니다.

이전 공간 조립 전달 기록: [workplaces-v006](../builds/workplaces-v006.md) — 현재319모델(248소품+71조립),805배치, 실제Native/HTTP71/71·시각71쌍·사무보조원구현범위 통과. v005이하는보존중간본이며 다른551직업초안은별도다.

[회전 사무의자 비교](chair-comparison-beta.md): AST-003 v001 Blender(792삼각형), v002 Meshy 후처리(964삼각형). 같은 팔레트·조명·카메라로 웹 비교했습니다.

[Blender 직접 제작 비교](blender-direct-beta.md): AST-001 v002 바닥판(220삼각형), AST-002 v001 바닥 표면(108삼각형)을 추가했습니다. 단순 소품은 직접 제작을 우선합니다.

첫 베타 [AST-001 v001 — COM-01 둥근 모서리 바닥판](AST-001-v001.md)이 등록되었습니다. Meshy→Blender→팔레트 UV→GLB→웹 표시를 검증했으며 용량 개선과 외형 검토가 남아 in_progress입니다. Unity 적용은 아직 하지 않았습니다.
[전체 에셋 데이터](../../machine/catalog/assets.json)에서 ID와 버전을 함께 조회합니다.

| 필드 | 내용 |
|---|---|
| asset_id / version / name | 에셋 ID·버전·이름 |
| kind / status | 소품 또는 디오라마 / 제작 중 또는 검수 완료 |
| source_path / source_images | Meshy 원본 / 제작에 쓴 원본 이미지 참조 |
| blender_path / runtime_path | Blender 수정본 / 최종 GLB |
| preview_path / unity_path | 미리보기 / Unity 적용 폴더 |
| palette_version | 사용한 최종 공용 PNG의 고정 버전 |
| accent_reason | color2 출처 색을 사용한 부위·이유 |
| unity_palette_path | Unity 공용 위치의 최종 PNG 복사본 |
| processing_paths | 재사용 후처리 스크립트 |
| inspection_path | 삼각형 수·파일 크기·웹 검수 기록 |

경로는 저장소 루트 기준입니다. 미완성 경로와 검수 수치는 규칙에 따라 null로 기록합니다.
선택 확장 tags는 물체 종류·기능·공간 유형·활동을 구분하고 applicable_contexts는 특정 공간의 적용 후보를 연결합니다. 둘 다 실제 사용 증거는 아닙니다. 색상 변형과 사용처는 [재사용·이력 안내](../guides/asset-reuse-and-history.md)의 단일 기록을 조회하며 이 문서에 별도 원장을 만들지 않습니다. 기존 항목은 근거 없이 일괄 보완하지 않습니다.
[제작 기준 요약](../guides/web-lowpoly.md) · [사용 빌드 목록](../../machine/catalog/builds.json)

- [PAN-001 일반 사무실 제작·조립 v001](PAN-001-office-v001.md): 17종 30개, 4,308삼각형, 독립 GLB 웹 검수. Unity 미검증.

- [PAN-001 위치·회전 정렬 v003](PAN-001-office-alignment-v003.md)

- [사무실 Unity 재사용·개별 에셋별 전체 후보/실제 사용 조회](../builds/office-assistant-v003.md) — 본문에서 18개 고정 에셋 버전의 개별 기록으로 연결.

- [전체 공간 제작 모델 색인 v001](workplace-models-v001.md) — 신규 소품 231버전·공간 조립 70버전, 상태·실행 근거 구분.

## 전체 공간의 현재 후보·모델·지지면 근거

- [전체 후보 v004](../jobs/workplace-common-assets-v004.md): 기준 v003기획+실제 제작 지원 추가 전체 공간을 생략 없이 연결.
- [전체 등록 모델 버전 색인](workplace-models-v001.md): 보존된 모든 버전·최신/과거 실제 사용처.
- [최종 지지면·접지 검토](workplace-model-visual-review-v001.md)와 [실제 버텍스 검수 원문](../../machine/evidence/workplaces-model-review-v001/visual-review-v002.json).

- [공용 장식 분리 라이브러리 v001 — 미배치·추가 검수](shared-spatial-details-v001.md)

<!-- spatial-diversity-v011 -->
- [전체 디테일 후보 v006](workplace-asset-candidates-v006.md) · [자연물 분리 라이브러리](shared-nature-details-v001.md)

- [최신 전체427개 에셋 재사용·사용 이력 v003](career-asset-reuse-report-v003.md) — 355구성·72조립 참조, 최신935개 선택 장면 사용 및 중간/최종4개 빌드 포함. 새 실행 통과 자동 승계 없음.

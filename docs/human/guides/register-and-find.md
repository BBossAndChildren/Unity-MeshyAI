# 자료 등록과 조회

1. [AGENTS.md](../../../AGENTS.md)와 [웹용 로우폴리 요약](web-lowpoly.md)을 읽고 대상이 소품인지 디오라마인지 구분합니다.
2. 참고 이미지가 있으면 [이미지 등록 절차](../images/README.md)에 따라 먼저 등록합니다.
3. 재사용 모델·스크립트를 확인하고 Blender 직접 제작, Meshy, 혼합 중 방식을 선택합니다. 원본은 meshy/models/original/<asset_id>/<version>/에 보존합니다. 직접 제작은 source.blend와 제작 스크립트를 보관하고, README에 선택 이유·실제 결과를 기록합니다. Meshy 사용 시 프롬프트·작업 ID·실제 소비 크레딧도 기록합니다.
4. Blender 수정본과 실제 사용 GLB는 meshy/models/blender/<asset_id>/<version>/ 및 그 안의 exports/에 둡니다.
5. color1/color2 원본의 칸을 색 변화 없이 합친 정사각형 PNG와 UV 대응표를 textures/palettes/<버전>/에 만들고 palettes.json에 등록합니다. 기본 면은 color1 출처, 강조는 color2 출처 칸을 사용합니다.
6. 개별 소품 1,000삼각형 이하, 디오라마 전체 5,000 목표로 제작하고 최종 GLB 재열기·웹 검수를 수행합니다. processing/에 후처리 스크립트, inspection.json에 실제 측정값·미검증 항목을 보관합니다.
7. assets.json에 파일 경로·팔레트 버전·검수 경로·상태 및 generation_method, generation_reason, production_record_path, meshy_credits_used를 등록합니다. 비용이 미측정이면 null, Meshy 미사용이 확인되면 0입니다. 없는 파일이나 미수행 검증을 완료로 만들지 않습니다.
8. Unity 적용 시 모델은 Assets/Meshy/<asset_id>/<version>/에, 최종 PNG는 Assets/Shared/Textures/<palette_version>/에 프로젝트 공용으로 복사합니다.
9. WebGL 출력은 unity/webgl/builds/<build_id>/에 저장하고 빌드 문서·builds.json을 갱신한 뒤 [전달 절차](webgl-delivery.md)를 따릅니다.

조회: 빌드 → 에셋 ID·버전 → 원본·Blender·GLB·검수 기록 → 팔레트 버전 → 원본 색상·UV 대응표.

재사용 작업에서는 [분류·변형·사용 이력 안내](asset-reuse-and-history.md)를 함께 확인합니다. 공간의 기존 occupation_groups·panorama_ref·asset_slots 연결을 먼저 조회하고, 직접 참고 이미지는 source_images로 구분합니다. 적용 가능한 공간과 실제 배치는 별도로 기록하며 색상 UV 파일 변경은 새 에셋 버전으로 보존합니다. 실제 배치·빌드 포함·실행 검증은 근거가 생긴 단계만 기록합니다.

직업체험 설계를 수정할 때는 [물건 확대·직접 작업 적용 안내](object-closeup-direct-work.md)를 확인합니다. 필수 동작과 `interaction_flow`·`closeup`·`work_surface` 계약은 AGENTS.md에서 관리합니다. 기존 작성 시나리오부터 조사·수정하고, 설계 변경만으로 실제 사용·빌드·실행 상태를 변경하지 않습니다.

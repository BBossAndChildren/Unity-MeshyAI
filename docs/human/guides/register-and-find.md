# 자료 등록과 조회

1. [AGENTS.md](../../../AGENTS.md)의 규칙과 목록 형식을 확인합니다.
2. 원본은 meshy/models/original/<asset_id>/<version>/에 저장하고 생성 기록을 README.md에 작성합니다.
3. 수정본은 meshy/models/blender/<asset_id>/<version>/에, 실제 사용본은 그 안의 exports/에 저장합니다.
4. color1.jpg로 기본 채색합니다. 강조·원색이 필요할 때만 color2.jpg를 추가하고 사용 이유를 기록합니다.
5. Unity의 Assets/Meshy/<asset_id>/<version>/에 실제 사용본을 적용합니다. 사용한 팔레트는 Assets/Shared/Textures/에 프로젝트당 한 번씩 그대로 복사합니다.
6. docs/machine/catalog/assets.json에 제작 단계별 경로, texture_ids, accent_reason, unity_texture_paths를 등록합니다.
7. WebGL을 unity/webgl/builds/<build_id>/에 출력하고 빌드 문서와 builds.json을 작성합니다.
8. AGENTS.md의 완료 전 검토를 수행하고 [전달 절차](webgl-delivery.md)에 따라 ZIP을 만듭니다.

조회: 빌드 ID → 포함 에셋 ID·버전 → 원본·Blender·실제 사용본·팔레트·Unity 적용본.
역방향 조회: 에셋 ID·버전 → builds.json의 assets 검색 → 사용 빌드.

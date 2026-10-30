# 전체 에셋 목록

현재 등록된 에셋은 없습니다.
[전체 에셋 데이터](../../machine/catalog/assets.json)에서 ID와 버전을 함께 조회합니다.

| 필드 | 내용 |
|---|---|
| asset_id / version / name | 에셋 ID·버전·이름 |
| source_path | Meshy 원본 |
| blender_path | Blender 수정본 |
| runtime_path | 실제 사용 모델 |
| preview_path | 미리보기 |
| unity_path | Unity 적용본 디렉터리 |
| texture_ids | color1 기본, 필요할 때 color2 추가 |
| accent_reason | color2를 사용하는 구체적 이유; 미사용 시 null |
| unity_texture_paths | 사용한 팔레트의 프로젝트 공용 임포트 경로 |

경로는 저장소 루트 기준입니다.
[빌드 목록](../../machine/catalog/builds.json)의 assets에서 같은 ID·버전을 검색하면 사용된 빌드를 찾을 수 있습니다.

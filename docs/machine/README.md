# 프로그램용 데이터

| 파일 | 내용 | 조회 키 |
|---|---|---|
| catalog/assets.json | 전체 에셋·제작 단계별 경로 | asset_id + version |
| catalog/builds.json | 빌드·포함 에셋 | build_id |
| catalog/shared-textures.json | 공용 팔레트 두 개·역할·원본 해시 | texture_id |

UTF-8 JSON이며 schema_version은 2입니다.
필수 필드와 제약은 [AGENTS.md](../../AGENTS.md)의 목록 계약을 따릅니다.
경로는 저장소 루트 기준입니다.

빌드의 assets 참조를 assets.json에서 조회한 뒤 texture_ids를 shared-textures.json과 연결합니다.
color1은 기본 채색, color2는 강조·원색이 필요한 경우에만 사용합니다.
Unity 임포트 경로는 에셋의 unity_texture_paths에 기록합니다.
artifact_url은 원격 결과물이 없으면 null입니다.

이전 단일 텍스처 필드 texture_path/unity_texture_path는 texture_ids/unity_texture_paths로 대체했습니다.
자동 검사 도구는 없으며 에이전트가 AGENTS.md의 검토 절차를 수행합니다.

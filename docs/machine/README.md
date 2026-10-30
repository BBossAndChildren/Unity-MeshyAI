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

## 직업 공간·파노라마 제작 자료

- [직업 후보](catalog/occupation-workplace-candidates.json): schema_version:3, 전체 제공 원문 552개 직업·809개 장소 연결. source_history는 과거 부분 원문의 출처입니다.
- [사무실 컨텍스트](catalog/workplace-contexts.json): schema_version:3, context_id/version으로 조회. occupation_groups는 직업 후보, panorama_ref는 실제 참고 이미지, asset_slots는 아직 모델로 확정하지 않은 계획입니다.
- [파노라마 프롬프트](catalog/panorama-prompts-v002.json): schema_version:3, prompt_id/version으로 조회. 25개 유효 분류의 71개 구도이며 기존 5개·신규 66개입니다. result_panorama_ref:null은 이미지 생성 전 상태입니다.
- [사람용 제작 자료](../human/jobs/panorama-production-package.md)

해당 기획 catalog는 위에 명시한 schema_version을 개별적으로 읽습니다. 기존 모델·빌드 catalog의 데이터 계약을 이 문서 작업으로 일괄 변경하지 않습니다. 공간의 원문 분류에 속한 모든 직업이 개별 프롬프트의 확정 사용자라는 뜻은 아닙니다.

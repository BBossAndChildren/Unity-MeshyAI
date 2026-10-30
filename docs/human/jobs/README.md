# 직업 원본 자료

## 최신 생성 결과·에셋 명세

- [전체 71개 공간의 필요한 에셋·모든 사용 후보·실제 사용처 v003](workplace-common-assets-v003.md)
- [기계용 전체 에셋 명세 v003](../../machine/catalog/workplace-asset-candidates-v003.json)
- [신규 이미지 66장 생성 기록](panorama-generation-v001.md) · [기계용 실행 기록](../../machine/catalog/panorama-generation-v001.json)
- [작업별 비용·실측 토큰](panorama-costs-v001.md)

아래 통합 원문과 프롬프트는 작성 당시 상태를 보존합니다. 현재 생성 결과와 실제 사용처 조회는 위 최신 문서에서 확인합니다.

- [job_base.txt](job_base.txt): 사용자가 제공한 직업별 근무장소 후보 분류 원본. 파일명·내용·인코딩·줄바꿈을 변경하지 않고 보관했습니다.
- 원문에 표시된 기준일: 2026-10-30. 원문은 552개 직업을 바탕으로 한 장소 후보 분류라고 설명합니다.
- 직업과 장소의 연결은 후보·추정을 포함합니다. 원문 보관은 직업별 실제 근무 장소를 검증했다는 뜻이 아닙니다.
- [직업 catalog](../../machine/catalog/occupation-workplace-candidates.json)는 job_base.txt 기준 552개 고유 직업·809개 장소 연결·26개 분류로 보완했습니다. 기존 부분 자료의 출처는 source_history에 보존했습니다.
- [사무실 컨텍스트 초안](../images/office-workplace-contexts.md)의 기존 직업 연결과 승인 상태는 유지했습니다.

원본 크기: 80044 bytes.

SHA-256: `39ffd920762c4c1688dfbac656ff4a6ee0bd4f9dd074382072704063e21bb925`

## 통합 목록

- [2026-10-31 v001 통합 목록](asset-panorama-inventory-2026-10-31-v001.md): 원문 그대로 보존한 현황 스냅샷과 52개 제작 후보.
- [기계용 등록 목록](../../machine/catalog/inventory-snapshots.json): 문서 해시·출처·고정 참조·스냅샷 수량.

문서에 적힌 기존 catalog 432개·589개는 문서 작성 시점의 수치입니다. 현재 직업 catalog는 전체 제공 원문 기준으로 보완했습니다. 문서 등록은 새 모델·파노라마 생성, 색상 레시피 확정, Unity 배치, 기획·제작 승인 또는 실행 검증을 뜻하지 않습니다.

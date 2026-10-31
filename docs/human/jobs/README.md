# 직업 원본 자료

현재71공간 전달 기준: [workplaces-v006](../builds/workplaces-v006.md) — 현재319모델(248소품+71조립),805배치, 실제Native/HTTP71/71·시각71쌍·사무보조원구현범위 통과. v005이하는보존중간본이며 다른551직업초안은별도다.

## 직업체험 설계 수정 시 먼저 읽기

- [물건 확대·직접 작업 적용 안내](../guides/object-closeup-direct-work.md). 상세 규칙과 추가 데이터 계약은 AGENTS.md에서 관리합니다. 지침 갱신 자체는 아래 기존 시나리오·구현·검증 상태를 바꾸지 않습니다.

## 직업·장소·핵심역량 기준 자료

- [기준 자료 v001](occupation-place-competency-reference-v001.md): 기존 552개 직업의 장소·파노라마 후보와 원본 핵심역량·하는일·준비방법 조회.
- [기계용 기준 자료 v001](../../machine/catalog/occupation-place-competency-reference-v001.json)
- [원본 직업 설명](sources/job-things-list/v001/Job_things_list.txt): 원본 바이트 보존. 장소·파노라마는 별도 기존 목록에서 연결합니다.


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

## 직업별 파노라마 조회

- [직업 552개와 파노라마 71장 매칭·검토 목록 v001](occupation-panorama-matches-v001.md)
- [기계용 조회 스냅샷](../../machine/catalog/occupation-panorama-matches-v001.json)
- 기존 명시 연결과 원문 장소 분류 기반 검토 선택지를 구별합니다. 세부 공간 자동 확정이나 실제 근무지 검증이 아닙니다.

## 원본 직업 설명 연계 — 최신 v002

- [직업별 파노라마 매칭·원본 참고정보 v002](occupation-panorama-matches-v002.md)
- [기계용 연결 목록 v002](../../machine/catalog/occupation-panorama-matches-v002.json)
- [보존 원본 Job_things_list.txt](sources/job-things-list/v001/Job_things_list.txt)
- 기존 저장소 직업 552개만 기준으로 ID·이름 모두 일치. 직업 추가 없이 하는일·핵심능력·준비방법 연결. 기존 파노라마 후보 상태는 유지합니다. v001은 과거 기록으로 보존합니다.

## 파노라마 기반 직업체험 — 첫 사무실 사례

- [장면·에셋·직업체험 구성 명세](panorama-career-experience-spec-v001.md)
- [사무보조원 미션 명세](office-assistant-experience-v001.md)
- [다른 채팅용 Unity WebGL 구현 프롬프트](office-assistant-implementation-prompt-v001.md)
- [미니게임 20종](../../machine/catalog/career-minigame-types-v001.json) · [시나리오](../../machine/catalog/career-experience-scenarios-v001.json) · [전체 71개 공간의 공통·비공통 에셋 분류](../../machine/catalog/panorama-career-experience-layouts-v001.json)
- 사용자 우선 지시에 따라 1개 시나리오 명세 작성, 551개 작성 대기. 실제 3D 게임 구현·실행은 미검증.

## 전체 직업체험 초안 — 최신 v002

- [전체 552개 직업별 상호작용 시나리오](career-experience-scenarios-v002.md)
- [파노라마·공통/비공통 에셋·직업체험 구성 v002](panorama-career-experience-spec-v002.md)
- [기계용 전체 시나리오](../../machine/catalog/career-experience-scenarios-v002.json) · [71개 공간·상호작용 에셋 역조회](../../machine/catalog/panorama-career-experience-layouts-v002.json)
- [구현용 요청 프롬프트](career-experience-implementation-prompt-v002.md)
- 기존 사무보조원 1개 보존 + 551개 신규 초안. 20종 설계 유형 배정. 기획 검토 대기·전문 문제 데이터 보완 필요·새 게임 실행 미검증. 이전 문서의 551개 작성 대기는 당시 상태입니다.

- [사무보조원 실제 Unity WebGL 실행·검증 보고](../builds/office-assistant-v003.md) — 1건 구현, 다른 551개 미구현.

- [최신 v005: 선택한 물건 확대·종이 팝업 실행](../builds/office-assistant-v005.md)

## 전체 공간 제작 후속 자료

- [전체 공간 후보·지원 추가 명세 v004](workplace-common-assets-v004.md): v003기준262개ID/71공간은 보존하고 실제 지원 추가를 별도 표기.
- [공간별 실제 제작·검수 진행](workplace-production-v001.md).
- [사무보조원 직접 작업 설계 v002](office-assistant-direct-work-v002.md): career-experience-scenarios-v003.json은 한 건 개정이며 전체552개 교체/승인이 아님.



- [효과음 제작 후보 목록](sound-effects-candidates-v001.md) — ElevenLabs 예정, 108종 기획 후보, 생성 미실행.


<!-- religion-roles-v001 -->
## 종교 3종 직업·호칭·직책 보완

- [원본관리 폴더의 종교 직업·출처 설명](sources/job-things-list/supplements/religion-roles/v001/README.md)
- [출처를 연결한 직업 보완 목록](../../machine/catalog/religion-occupations-v001.json): 불교 승려(호칭 스님), 개신교 목사·전도사, 천주교 신부·수녀·수사. 6개 표시 직업과 공식 분류 5개를 구분합니다.
- 하는 일·준비방법은 공식 기관 자료와 연결하고 종단·교단 적용 범위 및 확인하지 못한 핵심능력은 명시했습니다. 기존 552개 원본·ID와 종교 체험 미선택 상태를 보존합니다.

- [71공간·552직업·종교 호칭 분리 검토 기록](space-occupation-role-audit-v001.md): 원본 제목은 보존하고 런타임 공간 표시명만 분리했습니다. 과거 workplaces-v006 빌드의 화면을 수정한 것은 아닙니다.


## 사무실 신규10종 구현 결과

[office-ten-v003 실행·ZIP·검수 안내](../builds/office-ten-v003.md) — 기존 사무보조원과 별도10종. 실제 HTTP 업무10건·공통17건 통과. [직업별 명세](office-ten-experiences-v004.md).

- [교회·성당 공간 특색 보강 v001](worship-spatial-details-v001.md)


최신 표시·좌석 수정: [office-ten-v006](../builds/office-ten-v006.md) — 업무 메모/문서 반투명·의자2개 책상 방향 회전. 직업별 업무자료와 원본은 보존합니다.


- [ElevenLabs 효과음 제작 결과](sound-effects-production-v001.md) — 108종 승인 중 32종 생성·저장, 76종 서비스 대기 제한으로 미시작.


최신 표시 수정: [office-ten-v007](../builds/office-ten-v007.md) — 문서 미리보기를 실제 모니터 안에 표시하고 한글 입력·수정·줄바꿈을 실제 확인했습니다. 큰종이 overlay와 오른쪽 이동안은 적용하지 않았습니다.

<!-- spatial-diversity-v011 -->
- [69공간 특색 보강 v001](workplace-spatial-diversity-v001.md)


- [전체 직업체험 구현 대상·71개 공간 우선 진행표 v001](career-full-implementation-v001.md) — 552개 시나리오/555개 방별 대상; 실제 구현·실행 근거와 미완료 분리.

- [전체 직업체험 구현·검수 진행표 v002](career-full-implementation-v002.md) — 552개 시나리오·555개 조합; 스타터/원래 업무·분기/실행 상태 구분.

- [전체 직업체험 구현·검수 진행표 v003](career-full-implementation-v003.md) — 출력 전 준비 v003의 실제 업무 인계 수정; 이전 소스·검수 이력 보존.

- [전체555 체험 설명·jobs 목록](career-experience-descriptions-v001.md) — 현재 실제 작업판 기준 AI 선택용 설명, JSON·CSV 포함.
- [효과음 제작 갱신 v002](sound-effects-production-v002.md) — 34개 저장·74개 미생성 및 실제 비용·혼잡 중단 기록.

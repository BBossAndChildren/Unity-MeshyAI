# 파노라마 기반 직업체험 시나리오 전체 초안 v002

기존 552개 직업 전체에 대표 체험안을 작성했다. 첫 사무보조원 사례 1개를 그대로 보존하고 나머지 551개를 추가했다. 문서 작성 완료와 게임 구현·검증 완료는 다르다. 신규 미니게임은 이번에 구현하거나 실행하지 않았다.

장면별 활동 템플릿에 직업 원본 업무·역량을 연결한 검토용 초안이다. 전문 문제·난이도·정답을 직업별로 모두 검증한 최종 콘텐츠가 아니다. 직업군별 반복 조작은 재사용을 위한 것이며, 직업별 구체 문제와 필요한 전문 형상은 추가 검토한다.

## 구성 원칙

파노라마를 기준으로 에셋을 공통·비공통으로 명세하고 공간을 구성한다. 그 장소 안에서 직업별 업무·핵심역량을 반영한 물건 3개 상호작용을 수행한다. 공통 미니게임 10종과 특수 상황 10종 중 필요한 규칙만 선택한다. 전체 에셋 후보와 상호작용 후보는 실제 사용 원장이 아니다.

[원본 설명](sources/job-things-list/v001/Job_things_list.txt) · [직업·장소·역량 기준 자료](occupation-place-competency-reference-v001.md) · [미니게임 20종](../../machine/catalog/career-minigame-types-v001.json) · [기계용 전체 시나리오](../../machine/catalog/career-experience-scenarios-v002.json) · [공간·에셋 역조회](../../machine/catalog/panorama-career-experience-layouts-v002.json) · [구현 요청 프롬프트](career-experience-implementation-prompt-v002.md)

원문 근거는 직업 업무와 역량이다. 요청·시료·수치·사건·정답은 가상 연습 데이터로 각색했다. 실제 의료·안전·법률·금융 절차를 가르치는 자료가 아니며 실제 업무 판단이나 적성 평가로 사용하지 않는다. 이 분야는 직업 전문가의 내용 검토가 필요하다.

## 적용 현황

- 기존 명시 후보 연결 유지: 24개 신규 초안 및 사무보조원 보존 사례 1개.
- 기존 장소 분류 안의 세부 장면 제안: 338개.
- 기존 장소 분류 밖의 장면 제안: 188개. 원본 분류 수정이나 검증 완료가 아니다.
- 성직자 1개는 종교 전통 미선택. 개신교·불교·천주교의 3개 대안에 각각 물건 3개를 연결했으며 실행 전 사용자 선택이 필요하다.
- 71개 파노라마 각각에 대표 시나리오가 반드시 하나씩 배정되는 것은 아니다. 대표 체험이 미선택인 장면도 원래 에셋 후보를 유지한다.

## 미니게임 배정 수

| 유형 | 이름 | 직업 시나리오 배정 수 |
|---|---|---:|
| MG-001 | 분류·선별 | 385 |
| MG-002 | 조립·배치 | 99 |
| MG-003 | 순서·절차 | 104 |
| MG-004 | 측정·조절 | 219 |
| MG-005 | 관찰·검사 | 411 |
| MG-006 | 진단·해결 | 40 |
| MG-007 | 제작·표현 | 106 |
| MG-008 | 대화·응대 | 124 |
| MG-009 | 계획·배분 | 81 |
| MG-010 | 타이밍·추적 | 42 |
| EX-001 | 긴급 대응 | 25 |
| EX-002 | 안전 확보 | 91 |
| EX-003 | 교차접촉 방지 | 89 |
| EX-004 | 이상 신호 감시 | 23 |
| EX-005 | 정보 부족 조사 | 26 |
| EX-006 | 상충 요구 조정 | 50 |
| EX-007 | 돌발 변경 대응 | 94 |
| EX-008 | 협업·인계 | 71 |
| EX-009 | 개별 맞춤 | 51 |
| EX-010 | 기록·추적·복구 | 34 |

배정은 설계상 연결 수다. 구현 모듈 수나 실행 검증 통과 수가 아니다. 성직자 미선택 대안의 배정은 기본 미리보기 기준이며 실행 선택으로 확정하지 않았다.

## 직업별 빠른 목록

| 직업 | 대표 장면 | 물건 3개 |
|---|---|---|
| [3D 프린팅 전문가](#career-net-10001-experience) | 조립 구역 | 모니터, 소형 생산 기계, 조립 중인 단순 제품 |
| [GIS전문가](#career-net-1092-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [IT컨설턴트](#career-net-450-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [SNS 마케터](#career-net-10077-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [UX 디자인 컨설턴트](#career-net-10003-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [가구제조,수리원](#career-net-159-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [가구조립 및 검사원](#career-net-1152-experience) | 조립 구역 | 부품 트레이, 공구 거치대, 조립 중인 단순 제품 |
| [가사도우미](#career-net-352-experience) | 거실 | 테이블, 수납장, 독립형 TV |
| [가상현실전문가](#career-net-1093-experience) | 공용 업무 사무실 | 모니터, 키보드, 마우스 |
| [가수](#career-net-280-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [가스ㆍ수도ㆍ전기 계기 검침원 및 안전점검원](#career-net-1-experience) | 설비 작업 구역 | 부품 상자, 노출 배관 모형, 제어함 |
| [가전제품 설치 및 수리원](#career-net-41-experience) | 가정 수리 공간 | 간단한 가전제품, 공구 가방, 부품 트레이 |
| [가축사육자](#career-net-174-experience) | 축사 | 사료 통, 급이통, 물통 |
| [간병인](#career-net-353-experience) | 요양실 | 보조 손잡이, 휠체어, 침대 옆 탁자 |
| [간판제작원](#career-net-284-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [간호사](#career-net-354-experience) | 병실 | 호출 장치, 의료 모니터, 이동식 식탁 |
| [간호조무사](#career-net-355-experience) | 병실 | 호출 장치, 의료 모니터, 이동식 식탁 |
| [감성인식기술전문가](#career-net-10102-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [감정평가사](#career-net-198-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [개그맨](#career-net-281-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [개인관리컨설턴트](#career-net-10044-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [개인미디어 콘텐츠제작자(크리에이터)](#career-net-10021-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [개인브랜드매니저](#career-net-10043-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [개인형 이동수단 개발자](#career-net-10103-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [건물도장원](#career-net-65-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [건설견적원](#career-net-1130-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [건설공사품질관리원](#career-net-42-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [건설기계운전원](#career-net-77-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [건축공학기술자](#career-net-46-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [건축사](#career-net-1277-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [검사](#career-net-199-experience) | 법정 | 문서함, 진술대, 당사자 책상 |
| [게임 방송 프로듀서](#career-net-10020-experience) | 방송 스튜디오 | 마이크 암, 소형 오디오 콘솔, 카메라 |
| [게임감시관 및 조사관](#career-net-10068-experience) | 관제실 | 모니터, 관제 콘솔, 통신 기기 |
| [게임기획자](#career-net-923-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [경비원](#career-net-358-experience) | 관제실 | 모니터, 관제 콘솔, 통신 기기 |
| [경영컨설턴트](#career-net-202-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [경제학연구원](#career-net-203-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [경찰관](#career-net-359-experience) | 수사실 | 서류 트레이, 관계 보드, 모니터 |
| [경호원](#career-net-360-experience) | 관제실 | 모니터, 관제 콘솔, 통신 기기 |
| [계산원 및 매표원](#career-net-1116-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [고객관리시스템(CRM)전문가](#career-net-469-experience) | 민원·방문객 접수실 | 번호표 발급기, 모니터, 서비스 카운터 |
| [곡식작물재배자](#career-net-183-experience) | 재배지 | 농작물, 물뿌리개, 수확 상자 |
| [곤충 음식 개발자·조리사](#career-net-10006-experience) | 주방 | 냉장고, 조리대, 가열 기구 |
| [공구제조원](#career-net-1135-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [공업기계설치 및 정비원](#career-net-985-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [공예원](#career-net-929-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [공작기계조작원](#career-net-48-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [공정무역전문가](#career-net-10080-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [과수작물재배자](#career-net-1155-experience) | 재배지 | 농작물, 물뿌리개, 수확 상자 |
| [관세사](#career-net-207-experience) | 금융 창구 | 서류 트레이, 모니터, 서비스 카운터 |
| [광고 및 홍보전문가](#career-net-232-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [광고기획자](#career-net-283-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [광고디자이너](#career-net-285-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [광원 및 채석원](#career-net-49-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [괴롭힘방지조언사](#career-net-10054-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [교도관](#career-net-363-experience) | 수사실 | 서류 트레이, 관계 보드, 모니터 |
| [교육학연구원](#career-net-1103-experience) | 강의실 | 발표 화면, 강연대, 작은 AV 장치 |
| [교장](#career-net-481-experience) | 강의실 | 발표 화면, 강연대, 작은 AV 장치 |
| [구두미화원 및 수선원](#career-net-1119-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [구성작가](#career-net-260-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [국악인](#career-net-286-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [국제개발협력전문가](#career-net-10078-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [국제무역사무원](#career-net-208-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [국제회의전문가](#career-net-209-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [국회의원](#career-net-1061-experience) | 행정·문서 처리 사무실 | 서류철, 모니터, 유선전화 |
| [군무원](#career-net-1100-experience) | 군 행정실 | 일정 보드, 모니터, 통신 기기 |
| [귀금속 및 보석세공원](#career-net-740-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [극작가](#career-net-261-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [금속가공장치조작원](#career-net-52-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [금속공학기술자](#career-net-53-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [금융자산운용가(펀드매니저)](#career-net-244-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [금형원](#career-net-54-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [기계공학 기술자ㆍ연구원](#career-net-56-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [기상연구원](#career-net-6-experience) | 관측 지점 | 삼각대 센서, 소형 관측 장치, 데이터 기록 기기 |
| [기업고위임원](#career-net-238-experience) | 행정·문서 처리 사무실 | 서류철, 모니터, 유선전화 |
| [기자](#career-net-262-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [기후변화 대응 전문가](#career-net-10026-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [나노공학 기술자](#career-net-10109-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [냉동기사](#career-net-58-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [네이미스트](#career-net-247-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [네일아티스트](#career-net-288-experience) | 미용실 | 독립형 거울, 운반 카트, 세발대 |
| [네트워크엔지니어](#career-net-430-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [노년 플래너](#career-net-10011-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [노무사](#career-net-205-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [노인 전문 간호사](#career-net-10013-experience) | 병실 | 호출 장치, 의료 모니터, 이동식 식탁 |
| [녹음기사](#career-net-59-experience) | 영상 편집실 | 미디어 보관함, 모니터, 헤드폰 |
| [농수산물중개인](#career-net-211-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [농업기술자](#career-net-182-experience) | 온실 | 모종 트레이, 환경 센서, 관수 설비 |
| [다문화코디네이터](#career-net-10075-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [단순노무자](#career-net-126-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [단열원](#career-net-1132-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [단조원](#career-net-1139-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [대기환경기술자](#career-net-61-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [대체에너지개발연구원](#career-net-1282-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [대형트럭 및 특수차운전원](#career-net-1078-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [데이터 라벨러](#career-net-10118-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [데이터마이너](#career-net-10051-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [데이터베이스관리자](#career-net-431-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [도금원](#career-net-1141-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [도배원](#career-net-63-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [도선사](#career-net-1110-experience) | 조타실 | 항해 화면, 조타 장치, 통신 기기 |
| [도시 및 교통설계전문가](#career-net-212-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [도시 재생 전문가](#career-net-10004-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [도자기제조원](#career-net-64-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [도장원](#career-net-1140-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [도축원 및 육류가공원](#career-net-163-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [독서지도사](#career-net-365-experience) | 방문 학습 공간 | 교재, 필기구, 업무 책상 |
| [동물랭글러](#career-net-10071-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [동물보호보안관](#career-net-10046-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [동물조련사](#career-net-186-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [드라마작가](#career-net-266-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [드론 전문가](#career-net-10039-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [드론 콘텐츠 전문가](#career-net-10022-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [디스플레이 개발자](#career-net-10107-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [디지털 큐레이터](#career-net-10019-experience) | 전시실 | 전시대, 독립형 액자 거치대, 전시 조명 |
| [디지털 포렌식 수사관](#career-net-10030-experience) | 증거 분석실 | 밀봉 시료 상자, 현미경, 잠금 보관함 |
| [디지털 헬스케어 기기 개발자](#career-net-10115-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [레크리에이션지도자](#career-net-366-experience) | 복지 활동실 | 활동 교구, 이동식 화이트보드, 수납장 |
| [로봇 윤리학자](#career-net-10038-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [로봇연구원](#career-net-66-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [리포터](#career-net-265-experience) | 방송 스튜디오 | 마이크 암, 소형 오디오 콘솔, 카메라 |
| [마술사](#career-net-1259-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [마케팅전문가](#career-net-1068-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [만화가](#career-net-291-experience) | 미술 작업실 | 팔레트 도구, 빈 캔버스, 이젤 |
| [메이크업아티스트](#career-net-293-experience) | 미용실 | 독립형 거울, 운반 카트, 세발대 |
| [메카트로닉스공학기술자](#career-net-1134-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [메타버스 크리에이터](#career-net-10101-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [모델](#career-net-294-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [모바일앱개발자](#career-net-10076-experience) | 공용 업무 사무실 | 모니터, 키보드, 마우스 |
| [목공](#career-net-68-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [목소리코치](#career-net-10069-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [목재가공관련조작원](#career-net-69-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [무대감독](#career-net-296-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [무선주파수(RF)엔지니어](#career-net-476-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [무용가](#career-net-298-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [무인경비시스템종사원](#career-net-1118-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [무인항공기시스템개발자](#career-net-10049-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [무인항공촬영감독](#career-net-10070-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [문화 콘텐츠 전문가](#career-net-10023-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [문화여가사](#career-net-10042-experience) | 복지 활동실 | 활동 교구, 이동식 화이트보드, 수납장 |
| [문화재보존원](#career-net-299-experience) | 전시실 | 전시대, 독립형 액자 거치대, 전시 조명 |
| [물류관리사](#career-net-215-experience) | 물류 창고 | 보관 상자, 팔레트, 수동 운반차 |
| [물리치료사](#career-net-369-experience) | 운동 지도실 | 자세 확인용 독립 거울, 낮은 스텝, 소형 아령 |
| [물리학연구원](#career-net-8-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [미용사](#career-net-1122-experience) | 미용실 | 독립형 거울, 운반 카트, 세발대 |
| [미장원](#career-net-70-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [바닥재시공원](#career-net-155-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [바리스타](#career-net-180-experience) | 주방 | 냉장고, 조리대, 가열 기구 |
| [바이어(구매인)](#career-net-214-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [바텐더](#career-net-370-experience) | 주방 | 냉장고, 조리대, 가열 기구 |
| [반도체공학기술자](#career-net-157-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [반려동물 훈련·상담사](#career-net-10018-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [반려동물미용사](#career-net-319-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [발명가](#career-net-1433-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [발전장치조작원](#career-net-1144-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [방문판매원](#career-net-1113-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [방사선사](#career-net-10-experience) | 처치실 | 부품 트레이, 작업등, 운반 카트 |
| [방사성폐기물관리원](#career-net-1010-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [방송연출가](#career-net-301-experience) | 방송 스튜디오 | 마이크 암, 소형 오디오 콘솔, 카메라 |
| [방송장비(H/W)설치 및 수리원](#career-net-1147-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [방수원](#career-net-72-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [배관원](#career-net-74-experience) | 설비 작업 구역 | 부품 상자, 노출 배관 모형, 제어함 |
| [배터리 기술자](#career-net-10108-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [백댄서(백업댄서)](#career-net-304-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [버스운전기사](#career-net-372-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [번역가](#career-net-267-experience) | 출장 업무 공간 | 휴대 전화, 노트북, 문서 파우치 |
| [범죄과학수사관](#career-net-10064-experience) | 증거 분석실 | 밀봉 시료 상자, 현미경, 잠금 보관함 |
| [범죄심리분석관(프로파일러)](#career-net-10074-experience) | 수사실 | 서류 트레이, 관계 보드, 모니터 |
| [법률사무원](#career-net-252-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [법무사](#career-net-373-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [베타테스터](#career-net-1432-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [변리사](#career-net-374-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [변호사](#career-net-375-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [병원코디네이터](#career-net-1257-experience) | 의료 접수실 | 번호표 발급기, 서류 트레이, 모니터 |
| [보건의료정보관리사](#career-net-256-experience) | 의료 접수실 | 번호표 발급기, 서류 트레이, 모니터 |
| [보석감정사](#career-net-76-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [보석디자이너](#career-net-305-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [보육교사](#career-net-376-experience) | 교실 | 교재, 독립형 칠판, 사물함 |
| [보일러공](#career-net-978-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [보험계리인](#career-net-217-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [부동산중개인](#career-net-219-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [북디자이너](#career-net-927-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [분장사](#career-net-306-experience) | 미용실 | 독립형 거울, 운반 카트, 세발대 |
| [블록체인 전문가](#career-net-10029-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [비디오게임디자이너](#career-net-10067-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [비디오저널리스트(VJ)](#career-net-309-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [비파괴검사원](#career-net-81-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [비행기승무원](#career-net-418-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [비행기조종사](#career-net-150-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [빅 데이터 전문가](#career-net-10032-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [사무보조원](#career-net-253-office-documents) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [사물 인터넷 전문가](#career-net-10035-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [사서](#career-net-268-experience) | 문화 활동실 | 선반, 이동식 화이트보드, 테이블 |
| [사설탐정](#career-net-10063-experience) | 출장 업무 공간 | 휴대 전화, 노트북, 문서 파우치 |
| [사이버 평판 관리자](#career-net-10034-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [사이버교육운영자](#career-net-462-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [사진기자](#career-net-976-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [사진사](#career-net-975-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [사진인화 및 현상관련조작원](#career-net-311-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [사진작가](#career-net-310-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [사회단체활동가](#career-net-934-experience) | 행정·문서 처리 사무실 | 서류철, 모니터, 유선전화 |
| [사회복지사](#career-net-379-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [사회학연구원](#career-net-933-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [산업공학기술자](#career-net-83-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [산업안전관리원](#career-net-84-experience) | 설비 작업 구역 | 부품 상자, 노출 배관 모형, 제어함 |
| [산업카운슬러](#career-net-10053-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [상ㆍ하수도 처리장치 조작원](#career-net-85-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [상담전문가](#career-net-380-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [상수도기술자](#career-net-1007-experience) | 설비 작업 구역 | 부품 상자, 노출 배관 모형, 제어함 |
| [상점판매원](#career-net-243-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [상품대여원](#career-net-1114-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [상품중개인](#career-net-201-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [새시원](#career-net-1138-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [생물 정보 분석가](#career-net-10037-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [생물공학연구원](#career-net-86-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [생물학연구원](#career-net-13-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [생체 인식 전문가](#career-net-10036-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [생활설계사](#career-net-222-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [서예가](#career-net-1109-experience) | 미술 작업실 | 팔레트 도구, 빈 캔버스, 이젤 |
| [석공](#career-net-87-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [석유화학기술자](#career-net-88-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [선물중개인](#career-net-223-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [선박 및 열차객실승무원](#career-net-1125-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [선박갑판원](#career-net-1112-experience) | 선박 갑판 | 구명환, 밧줄 코일, 계류 장치 |
| [선박정비원](#career-net-92-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [선장 및 항해사](#career-net-176-experience) | 조타실 | 항해 화면, 조타 장치, 통신 기기 |
| [설문조사원](#career-net-165-experience) | 출장 업무 공간 | 휴대 전화, 노트북, 문서 파우치 |
| [섬유공학기술자](#career-net-57-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [섬유제조원](#career-net-73-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [성악가](#career-net-313-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [성우](#career-net-270-experience) | 방송 스튜디오 | 마이크 암, 소형 오디오 콘솔, 카메라 |
| [성직자](#career-net-384-experience) | 전통 선택 대기(3개 대안) | 펼친 성경, 설교 강대상, 찬송가 책 거치대 |
| [세무사](#career-net-224-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [세탁원](#career-net-166-experience) | 주택 관리 공간 | 점검 보드, 설비함, 청소 도구 |
| [소믈리에](#career-net-167-experience) | 주방 | 냉장고, 조리대, 가열 기구 |
| [소방관](#career-net-385-experience) | 관제실 | 모니터, 관제 콘솔, 통신 기기 |
| [소비생활어드바이저](#career-net-10041-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [소설가](#career-net-973-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [소음진동기술자](#career-net-539-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [속기사](#career-net-459-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [손실방지전문가](#career-net-10040-experience) | 관제실 | 모니터, 관제 콘솔, 통신 기기 |
| [손해사정사](#career-net-226-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [쇼핑호스트](#career-net-178-experience) | 방송 스튜디오 | 마이크 암, 소형 오디오 콘솔, 카메라 |
| [수의사](#career-net-15-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [수의테크니션](#career-net-10048-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [수질환경연구원](#career-net-1255-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [수학연구원](#career-net-17-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [스마트 그리드 엔지니어](#career-net-10025-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [스마트 도시 전문가](#career-net-10005-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [스마트 의류 개발자](#career-net-10009-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [스마트 재난 관리 전문가](#career-net-10028-experience) | 관제실 | 모니터, 관제 콘솔, 통신 기기 |
| [스마트 팜 구축가](#career-net-10008-experience) | 온실 | 모종 트레이, 환경 센서, 관수 설비 |
| [스마트공장 기술자](#career-net-10112-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [스마트팜 운영자](#career-net-10106-experience) | 온실 | 모종 트레이, 환경 센서, 관수 설비 |
| [스턴트맨](#career-net-314-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [스포츠 심리 상담원](#career-net-10015-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [스포츠강사](#career-net-421-experience) | 운동 지도실 | 자세 확인용 독립 거울, 낮은 스텝, 소형 아령 |
| [스포츠기록분석연구원](#career-net-10066-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [스포츠에이전트](#career-net-1088-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [스포츠트레이너](#career-net-392-experience) | 운동 지도실 | 자세 확인용 독립 거울, 낮은 스텝, 소형 아령 |
| [스포츠해설가](#career-net-1437-experience) | 방송 스튜디오 | 마이크 암, 소형 오디오 콘솔, 카메라 |
| [시각디자이너](#career-net-937-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [시멘트제조원](#career-net-97-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [시스템소프트웨어개발자](#career-net-834-experience) | 공용 업무 사무실 | 모니터, 키보드, 마우스 |
| [시스템엔지니어](#career-net-440-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [시인](#career-net-968-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [시장 및 여론조사전문가](#career-net-230-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [식품가공검사원](#career-net-1150-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [식품공학기술자](#career-net-162-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [식품융합엔지니어](#career-net-10047-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [신경회로망연구원](#career-net-98-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [신소재 개발 연구원](#career-net-10116-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [신약개발연구원](#career-net-1436-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [신용관련추심원](#career-net-1101-experience) | 금융 창구 | 서류 트레이, 모니터, 서비스 카운터 |
| [신용조사원](#career-net-231-experience) | 금융 창구 | 서류 트레이, 모니터, 서비스 카운터 |
| [신재생에너지 전문가](#career-net-10027-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [신호원 및 수송원](#career-net-390-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [심리학연구원](#career-net-20-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [아나운서](#career-net-271-experience) | 방송 스튜디오 | 마이크 암, 소형 오디오 콘솔, 카메라 |
| [아동청소년시설보호사](#career-net-10057-experience) | 요양실 | 보조 손잡이, 휠체어, 침대 옆 탁자 |
| [아이티(IT)교육강사](#career-net-475-experience) | 방문 학습 공간 | 교재, 필기구, 업무 책상 |
| [아이티(IT)기술영업원](#career-net-474-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [아쿠아리스트](#career-net-10073-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [악기수리원 및 조율사](#career-net-347-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [악기제조원](#career-net-318-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [안경사](#career-net-21-experience) | 진료실 | 의료 모니터, 진찰·처치 침대, 업무 책상 |
| [안마사](#career-net-1107-experience) | 운동 지도실 | 자세 확인용 독립 거울, 낮은 스텝, 소형 아령 |
| [안무가](#career-net-966-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [압연원](#career-net-100-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [애견테라피스트](#career-net-10060-experience) | 동물 관리실 | 운반 케이지, 먹이 그릇, 세척대 |
| [애니메이션기획자](#career-net-920-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [애니메이션작가](#career-net-922-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [애니메이터](#career-net-441-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [야외활동지도사](#career-net-10065-experience) | 복지 활동실 | 활동 교구, 이동식 화이트보드, 수납장 |
| [약사 및 한약사](#career-net-23-experience) | 진료실 | 의료 모니터, 진찰·처치 침대, 업무 책상 |
| [양식원](#career-net-187-experience) | 축사 | 사료 통, 급이통, 물통 |
| [양자 컴퓨팅 기술자](#career-net-10110-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [양장사 및 양복사](#career-net-164-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [언어치료사](#career-net-386-experience) | 운동 지도실 | 자세 확인용 독립 거울, 낮은 스텝, 소형 아령 |
| [언어학연구원](#career-net-272-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [에너지공학기술자](#career-net-995-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [여행 기획자](#career-net-10016-experience) | 안내 집결 지점 | 지도 거치대, 안내판, 여행 가방 |
| [여행상품개발원](#career-net-626-experience) | 안내 집결 지점 | 지도 거치대, 안내판, 여행 가방 |
| [여행안내원](#career-net-388-experience) | 안내 집결 지점 | 지도 거치대, 안내판, 여행 가방 |
| [역사학연구원](#career-net-273-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [연극연출가](#career-net-320-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [연근해 어부 및 해녀](#career-net-189-experience) | 선박 갑판 | 구명환, 밧줄 코일, 계류 장치 |
| [연기자](#career-net-303-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [연예인매니저](#career-net-321-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [연주가](#career-net-317-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [영사기사](#career-net-101-experience) | 영상 편집실 | 미디어 보관함, 모니터, 헤드폰 |
| [영양사](#career-net-169-experience) | 주방 | 냉장고, 조리대, 가열 기구 |
| [영업원](#career-net-928-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [영화감독](#career-net-322-experience) | 영상 편집실 | 미디어 보관함, 모니터, 헤드폰 |
| [영화기획자](#career-net-323-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [영화시나리오작가](#career-net-914-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [외교관](#career-net-233-experience) | 출장 업무 공간 | 휴대 전화, 노트북, 문서 파우치 |
| [외환딜러](#career-net-234-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [요리배달원](#career-net-1129-experience) | 식당 홀 | 메뉴 거치대, 식기, 배식 보조대 |
| [용접원](#career-net-102-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [우주전파예보관](#career-net-10114-experience) | 관측 지점 | 삼각대 센서, 소형 관측 장치, 데이터 기록 기기 |
| [우편물집배원](#career-net-383-experience) | 운송 거점 | 안내판, 보관 상자, 운반 카트 |
| [운동감독](#career-net-400-experience) | 운동 지도실 | 자세 확인용 독립 거울, 낮은 스텝, 소형 아령 |
| [운동경기심판](#career-net-391-experience) | 경기 구역 | 공, 작은 골대 한 쌍, 빈 점수판 |
| [운동선수](#career-net-336-experience) | 경기 구역 | 공, 작은 골대 한 쌍, 빈 점수판 |
| [원격진료 코디네이터](#career-net-10010-experience) | 의료 접수실 | 번호표 발급기, 서류 트레이, 모니터 |
| [원양어부](#career-net-1157-experience) | 선박 갑판 | 구명환, 밧줄 코일, 계류 장치 |
| [원예기술자](#career-net-963-experience) | 온실 | 모종 트레이, 환경 센서, 관수 설비 |
| [원자력연구원](#career-net-104-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [웨딩플래너](#career-net-427-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [웹디자이너](#career-net-443-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [웹마스터](#career-net-444-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [웹접근성컨설턴트](#career-net-10052-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [웹툰작가](#career-net-10072-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [웹프로듀서](#career-net-1096-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [위생사](#career-net-1108-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [유리부착원](#career-net-1133-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [유리제품제조원](#career-net-106-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [유전공학연구원](#career-net-24-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [유전상담사](#career-net-10061-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [유전자 재조합 식품 전문가](#career-net-10104-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [유제품제조원](#career-net-190-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [유치원교사](#career-net-395-experience) | 교실 | 교재, 독립형 칠판, 사물함 |
| [은행출납사무원](#career-net-255-experience) | 금융 창구 | 서류 트레이, 모니터, 서비스 카운터 |
| [음료제조관련조작원](#career-net-1149-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [음반기획자](#career-net-917-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [음악강사](#career-net-1431-experience) | 방문 학습 공간 | 교재, 필기구, 업무 책상 |
| [음악치료사](#career-net-396-experience) | 운동 지도실 | 자세 확인용 독립 거울, 낮은 스텝, 소형 아령 |
| [음향기사](#career-net-915-experience) | 영상 편집실 | 미디어 보관함, 모니터, 헤드폰 |
| [응급구조사](#career-net-397-experience) | 처치실 | 부품 트레이, 작업등, 운반 카트 |
| [의료 기기 개발 전문가](#career-net-10014-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [의료장비기사](#career-net-19-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [의료정보시스템개발자](#career-net-467-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [의복수선원](#career-net-1142-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [의복제품검사원](#career-net-1143-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [이공학계열교수](#career-net-364-experience) | 강의실 | 발표 화면, 강연대, 작은 AV 장치 |
| [이미지컨설턴트](#career-net-325-experience) | 미용실 | 독립형 거울, 운반 카트, 세발대 |
| [이용사](#career-net-1121-experience) | 미용실 | 독립형 거울, 운반 카트, 세발대 |
| [인공위성개발원](#career-net-107-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [인공지능 엔지니어](#career-net-10117-experience) | 공용 업무 사무실 | 모니터, 키보드, 마우스 |
| [인문계중등학교교사](#career-net-406-experience) | 교실 | 교재, 독립형 칠판, 사물함 |
| [인문사회계열교수](#career-net-988-experience) | 강의실 | 발표 화면, 강연대, 작은 AV 장치 |
| [인쇄기조작원](#career-net-108-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [인테리어디자이너](#career-net-326-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [일기예보관](#career-net-5-experience) | 관측 지점 | 삼각대 센서, 소형 관측 장치, 데이터 기록 기기 |
| [일러스트레이터](#career-net-327-experience) | 미술 작업실 | 팔레트 도구, 빈 캔버스, 이젤 |
| [일반공무원](#career-net-362-experience) | 행정·문서 처리 사무실 | 서류철, 모니터, 유선전화 |
| [일반의사](#career-net-1440-experience) | 진료실 | 의료 모니터, 진찰·처치 침대, 업무 책상 |
| [임상병리사](#career-net-941-experience) | 처치실 | 부품 트레이, 작업등, 운반 카트 |
| [임상심리사](#career-net-398-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [자동조립라인 및 산업용로봇조작원](#career-net-1158-experience) | 조립 구역 | 부품 트레이, 공구 거치대, 조립 중인 단순 제품 |
| [자동차공학기술자](#career-net-1076-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [자동차영업원](#career-net-236-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [자동차정비원](#career-net-109-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [자동차조립원](#career-net-110-experience) | 조립 구역 | 부품 트레이, 공구 거치대, 조립 중인 단순 제품 |
| [자연계중등학교교사](#career-net-1089-experience) | 교실 | 교재, 독립형 칠판, 사물함 |
| [자연과학연구원](#career-net-1541-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [작가](#career-net-1441-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [작곡가](#career-net-328-experience) | 영상 편집실 | 모니터, 헤드폰, 스피커 |
| [작업치료사](#career-net-401-experience) | 운동 지도실 | 자세 확인용 독립 거울, 낮은 스텝, 소형 아령 |
| [장례지도사](#career-net-403-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [장애인잡코치](#career-net-10056-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [장학사](#career-net-1102-experience) | 강의실 | 발표 화면, 강연대, 작은 AV 장치 |
| [재능기부코디네이터](#career-net-10055-experience) | 복지 활동실 | 활동 교구, 이동식 화이트보드, 수납장 |
| [재료공학기술자](#career-net-112-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [재활용 처리 및 소각로 조작원](#career-net-145-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [재활용코디네이터](#career-net-10045-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [전공](#career-net-113-experience) | 설비 작업 구역 | 부품 상자, 노출 배관 모형, 제어함 |
| [전기 부품 및 제품 생산직](#career-net-1146-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [전기공학기술자](#career-net-114-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [전기설비조작원](#career-net-1145-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [전문비서](#career-net-378-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [전문의사](#career-net-25-experience) | 진료실 | 의료 모니터, 진찰·처치 침대, 업무 책상 |
| [전자 부품 및 제품 생산직](#career-net-1087-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [전자공학기술자](#career-net-119-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [전자상거래전문가](#career-net-470-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [전자장비설치 및 수리원](#career-net-120-experience) | 가정 수리 공간 | 간단한 가전제품, 공구 가방, 부품 트레이 |
| [전통건축원](#career-net-1131-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [전통식품제조원](#career-net-171-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [전화교환원](#career-net-404-experience) | 민원·방문객 접수실 | 번호표 발급기, 모니터, 서비스 카운터 |
| [전화설치 및 수리원](#career-net-121-experience) | 가정 수리 공간 | 간단한 가전제품, 공구 가방, 부품 트레이 |
| [접객원](#career-net-1127-experience) | 식당 홀 | 메뉴 거치대, 식기, 배식 보조대 |
| [정밀 농업기술자](#career-net-10007-experience) | 온실 | 모종 트레이, 환경 센서, 관수 설비 |
| [정밀기기제품제조원](#career-net-122-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [정보보호전문가](#career-net-435-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [정보시스템운영자](#career-net-938-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [정보중개인](#career-net-452-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [정치학연구원](#career-net-269-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [제과사 및 제빵사](#career-net-172-experience) | 제과실 | 믹서, 베이킹 트레이, 오븐 |
| [제관원](#career-net-1137-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [제품디자이너](#career-net-332-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [제화원](#career-net-50-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [조각가](#career-net-333-experience) | 미술 작업실 | 팔레트 도구, 빈 캔버스, 이젤 |
| [조경기술자](#career-net-193-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [조경원](#career-net-192-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [조리사 및 주방장](#career-net-173-experience) | 주방 | 냉장고, 조리대, 가열 기구 |
| [조림 영림 및 벌목원](#career-net-1156-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [조명기사](#career-net-911-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [조선공학기술자](#career-net-90-experience) | 부두 | 보관 상자, 손수레, 계류 기둥 |
| [조적공](#career-net-75-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [조향사](#career-net-334-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [종이제품생산직(기계조작)](#career-net-1151-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [주방보조원](#career-net-1128-experience) | 주방 | 냉장고, 조리대, 가열 기구 |
| [주유원](#career-net-1115-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [주조원](#career-net-127-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [주차관리원](#career-net-1120-experience) | 안내 집결 지점 | 지도 거치대, 안내판, 여행 가방 |
| [주택관리사](#career-net-405-experience) | 주택 관리 공간 | 점검 보드, 설비함, 청소 도구 |
| [증권분석가](#career-net-239-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [증권중개인](#career-net-240-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [지게차운전원](#career-net-1111-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [지능형 로봇개발자](#career-net-10113-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [지리정보시스템기사](#career-net-10050-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [지리학연구원](#career-net-29-experience) | 관측 지점 | 삼각대 센서, 소형 관측 장치, 데이터 기록 기기 |
| [지질학연구원](#career-net-30-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [지휘자](#career-net-335-experience) | 공연 무대 | 마이크 스탠드, 조명 스탠드, 스피커 |
| [직업군인](#career-net-407-experience) | 장비 관리실 | 보관 케이스, 작업대, 선반 |
| [직업능력개발훈련교사](#career-net-409-experience) | 교육 실습실 | 부품 트레이, 교육용 조립 키트, 작업대 |
| [직업상담 및 취업알선원](#career-net-408-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [직조원](#career-net-129-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [창업컨설턴트](#career-net-10079-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [채소 및 특용작물재배자](#career-net-1154-experience) | 재배지 | 농작물, 물뿌리개, 수확 상자 |
| [천문학연구원](#career-net-31-experience) | 관측 지점 | 삼각대 센서, 소형 관측 장치, 데이터 기록 기기 |
| [철골공](#career-net-131-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [철도 및 지하철기관사](#career-net-132-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [철도차량정비원](#career-net-133-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [철학연구원](#career-net-1104-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [청소원](#career-net-356-experience) | 주택 관리 공간 | 점검 보드, 설비함, 청소 도구 |
| [청원경찰](#career-net-1117-experience) | 관제실 | 모니터, 관제 콘솔, 통신 기기 |
| [체형관리사](#career-net-179-experience) | 미용실 | 독립형 거울, 운반 카트, 세발대 |
| [초등학교교사](#career-net-410-experience) | 교실 | 교재, 독립형 칠판, 사물함 |
| [촬영기사](#career-net-337-experience) | 촬영 스튜디오 | 작은 제품 촬영대, 조명 스탠드, 카메라 |
| [출판물기획전문가](#career-net-338-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [출판편집자](#career-net-926-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [측량사](#career-net-32-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [치과기공사](#career-net-33-experience) | 처치실 | 부품 트레이, 작업등, 운반 카트 |
| [치과위생사](#career-net-411-experience) | 처치실 | 부품 트레이, 작업등, 운반 카트 |
| [치과의사](#career-net-34-experience) | 진료실 | 의료 모니터, 진찰·처치 침대, 업무 책상 |
| [치어리더](#career-net-1126-experience) | 경기 구역 | 공, 작은 골대 한 쌍, 빈 점수판 |
| [카레이서](#career-net-1438-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [카지노딜러](#career-net-946-experience) | 소매점 | 단순 포장 상품, POS 기기, 바구니 |
| [카피라이터](#career-net-278-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [캐드원](#career-net-125-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [캐디](#career-net-412-experience) | 안내 집결 지점 | 지도 거치대, 안내판, 여행 가방 |
| [캐릭터디자이너](#career-net-339-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [캐스팅디렉터](#career-net-1439-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [커플매니저](#career-net-1256-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [컬러리스트](#career-net-340-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [컴퓨터게임시나리오작가](#career-net-457-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [컴퓨터그래픽디자이너](#career-net-458-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [컴퓨터설치·수리원](#career-net-466-experience) | 가정 수리 공간 | 간단한 가전제품, 공구 가방, 부품 트레이 |
| [컴퓨터하드웨어 기술자 및 연구원](#career-net-948-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [케어매니저](#career-net-10058-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [콘크리트공](#career-net-1090-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [크라우드 펀딩 전문가](#career-net-10033-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [크레인 및 호이스트운전원](#career-net-592-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [클라우드 시스템 엔지니어](#career-net-10031-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [타이어 및 고무제품 생산직](#career-net-47-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [태양광발전연구 및 개발자](#career-net-10105-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [택배원](#career-net-371-experience) | 운송 거점 | 안내판, 보관 상자, 운반 카트 |
| [택시운전기사](#career-net-426-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [텔레마케터](#career-net-242-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [토목공학기술자](#career-net-137-experience) | 건축 작업 구역 | 안전 펜스, 자재 더미, 부분 벽돌 구조 |
| [토양환경기술자](#career-net-997-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [통계학연구원](#career-net-36-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |
| [통신공학 기술자 및 연구원](#career-net-138-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [통신망설계운영기술자](#career-net-465-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [통신설비설치 및 수리원](#career-net-1148-experience) | 가정 수리 공간 | 간단한 가전제품, 공구 가방, 부품 트레이 |
| [통신엔지니어](#career-net-429-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [통신장비기사](#career-net-140-experience) | 서버실 | 관리 단말, 케이블 트레이, 서버 랙 |
| [통신케이블설치 및 수리원](#career-net-139-experience) | 가정 수리 공간 | 간단한 가전제품, 공구 가방, 부품 트레이 |
| [통역가](#career-net-264-experience) | 출장 업무 공간 | 휴대 전화, 노트북, 문서 파우치 |
| [투자분석가(애널리스트)](#career-net-950-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [트럭운전기사](#career-net-142-experience) | 운송 조종 공간 | 모니터, 조작 콘솔, 통신 기기 |
| [특수교사](#career-net-413-experience) | 교실 | 교재, 독립형 칠판, 사물함 |
| [특수효과기술자](#career-net-916-experience) | 영상 편집실 | 미디어 보관함, 모니터, 헤드폰 |
| [파티플래너](#career-net-1276-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [판금원](#career-net-143-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [판사](#career-net-414-experience) | 법정 | 문서함, 진술대, 당사자 책상 |
| [패션디자이너](#career-net-344-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [패션코디네이터](#career-net-345-experience) | 디자인 작업실 | 시안 보드, 펜 태블릿, 모니터 |
| [패턴사](#career-net-295-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [펄프 및 종이 생산직](#career-net-144-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [편집기사](#career-net-346-experience) | 영상 편집실 | 미디어 보관함, 모니터, 헤드폰 |
| [평등관리사무원](#career-net-10059-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [평론가](#career-net-957-experience) | 공용 업무 사무실 | 모니터, 키보드, 수납장 |
| [포장원](#career-net-1153-experience) | 물류 창고 | 보관 상자, 팔레트, 수동 운반차 |
| [푸드스타일리스트](#career-net-177-experience) | 주방 | 냉장고, 조리대, 가열 기구 |
| [프로게이머](#career-net-1097-experience) | 공용 업무 사무실 | 모니터, 키보드, 마우스 |
| [프로바둑기사](#career-net-415-experience) | 협업·기획 사무실 | 노트북, 테이블, 메모 |
| [플라스틱제품제조원](#career-net-147-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [플로리스트](#career-net-316-experience) | 공예 작업실 | 보관 상자, 작업대, 선반 |
| [피부관리사](#career-net-416-experience) | 미용실 | 독립형 거울, 운반 카트, 세발대 |
| [핀테크 전문가](#career-net-10111-experience) | 금융 상담실 | 서류 파일, 작은 계산기, 노트북 |
| [학습장애간호사](#career-net-10062-experience) | 병실 | 호출 장치, 의료 모니터, 이동식 식탁 |
| [학습지방문교사](#career-net-1106-experience) | 방문 학습 공간 | 교재, 필기구, 업무 책상 |
| [학예사(큐레이터)](#career-net-348-experience) | 전시실 | 전시대, 독립형 액자 거치대, 전시 조명 |
| [학원강사](#career-net-417-experience) | 방문 학습 공간 | 교재, 필기구, 업무 책상 |
| [한복사](#career-net-175-experience) | 공예 작업실 | 보관 상자, 손공구, 바이스 |
| [한의사](#career-net-37-experience) | 진료실 | 의료 모니터, 진찰·처치 침대, 업무 책상 |
| [항공교통관제사](#career-net-148-experience) | 관제실 | 모니터, 관제 콘솔, 통신 기기 |
| [항공기·선박조립 및 검사원](#career-net-1136-experience) | 조립 구역 | 부품 트레이, 공구 거치대, 조립 중인 단순 제품 |
| [항공기정비원](#career-net-149-experience) | 정비 구역 | 공구함, 열린 기계 케이스, 부품 트레이 |
| [항공우주공학기술자](#career-net-151-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [해부학연구원](#career-net-38-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [해양 레저 전문가](#career-net-10017-experience) | 선박 갑판 | 구명환, 밧줄 코일, 계류 장치 |
| [해양 에너지 기술자](#career-net-10024-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [해양공학기술자](#career-net-1081-experience) | 부두 | 보관 상자, 손수레, 계류 기둥 |
| [해양수산기술자](#career-net-195-experience) | 부두 | 보관 상자, 손수레, 계류 기둥 |
| [해양학연구원](#career-net-39-experience) | 관측 지점 | 삼각대 센서, 소형 관측 장치, 데이터 기록 기기 |
| [해양환경기사](#career-net-1006-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [행사기획자](#career-net-951-experience) | 협업·기획 사무실 | 노트북, 이동식 화이트보드, 메모 |
| [행정부고위공무원](#career-net-1278-experience) | 행정·문서 처리 사무실 | 서류철, 모니터, 유선전화 |
| [행정학연구원](#career-net-1105-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [헤드헌터](#career-net-1279-experience) | 복지·심리 상담실 | 상담 노트, 테이블, 선반 |
| [헬스 케어 컨설턴트](#career-net-10012-experience) | 진료실 | 의료 모니터, 진찰·처치 침대, 업무 책상 |
| [호스피스전문간호사](#career-net-428-experience) | 병실 | 호출 장치, 의료 모니터, 이동식 식탁 |
| [호텔지배인](#career-net-795-experience) | 식당 홀 | 메뉴 거치대, 식기, 배식 보조대 |
| [혼례종사원](#career-net-1124-experience) | 식당 홀 | 메뉴 거치대, 식기, 배식 보조대 |
| [홀로그램 전문가](#career-net-10002-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [홍보도우미](#career-net-419-experience) | 안내 집결 지점 | 지도 거치대, 안내판, 여행 가방 |
| [화가](#career-net-349-experience) | 미술 작업실 | 팔레트 도구, 빈 캔버스, 이젤 |
| [화학공학기술자](#career-net-952-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [화학연구원](#career-net-40-experience) | 실험실 | 시험관대, 소형 저울, 비커 |
| [화학제품제조원](#career-net-153-experience) | 생산 구역 | 안전 가드, 제어 패널, 완성품 상자 |
| [화훼재배기술자](#career-net-954-experience) | 온실 | 모종 트레이, 환경 센서, 관수 설비 |
| [환경공학기술자 및 연구원](#career-net-1080-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [환경설비기술자](#career-net-1004-experience) | 설비 작업 구역 | 부품 상자, 노출 배관 모형, 제어함 |
| [환경영향평가원](#career-net-1281-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [환경위생검사원](#career-net-1009-experience) | 분석실 | 부품 트레이, 분석 장비, 모니터 |
| [환경컨설턴트](#career-net-994-experience) | 환경 조사 지점 | 시료 용기, 휴대 측정기, 낮은 지형 |
| [회계사](#career-net-206-experience) | 전문 상담 사무실 | 서류 파일, 테이블, 선반 |
| [회계사무원](#career-net-258-experience) | 공용 업무 사무실 | 모니터, 복합기, 수납장 |

## 직업별 상세 시나리오

<a id="career-net-10001-experience"></a>
### 3D 프린팅 전문가 — 작은 출력물의 형상 오류와 모형 출력 결과 점검

- 직업: `career-net-10001` · 시나리오 `career-net-10001-experience` `v001`.
- 원본 위치: `/items/0/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 조립 구역 · `PRM-019 v001` · [PAN-019 v001](../../../images/original/panoramas/PAN-019/v001/prm-019-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 3D 프린팅 전문가의 업무 표현과 조립 구역의 부품을 순서대로 결합하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 컴퓨터 프로그램을 활용하여 설계된 디자인대로 프린터를 조작하고 운영합니다.
- 체험의 업무 자료: 출력할 3D 형상·가상 출력 조건과 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 요청 형상과 다른 크기·방향 지점 찾기 | 제시한 형상의 크기·방향 불일치 식별 | 관찰·검사 |
| 2 | 소형 생산 기계 · CND-071 | 3D 프린터 변형이 필요한 생산 기계에서 가상 설정 눈금 조절 | 훈련용 가상 설정 범위 충족 | 측정·조절 |
| 3 | 조립 중인 단순 제품 · CND-078 | 출력물 변형이 필요한 제품 모형을 돌려 삽입된 결함 확인 | 출력물의 지정 결함 식별 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 생산 기계 / noncommon / 실제 모델 연결 미정. 범용 생산 기계를 3D 프린터로 구별할 수 있는 별도 형상·부품 명세 필요
- 에셋 준비: 조립 중인 단순 제품 / noncommon / 실제 모델 연결 미정. 사용자 요청 출력물의 형상·결함 상태 변형 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 선택 장면의 기존 필수 후보 밖 추가 제안: CND-005, CND-071. 기존 후보 목록은 자동 수정하지 않음.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1092-experience"></a>
### GIS전문가 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-1092` · 시나리오 `career-net-1092-experience` `v001`.
- 원본 위치: `/items/1/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. GIS전문가의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사용자 의견을 수렴하여 시스템의 구조를 설계하고, 데이터베이스, 사용자 인터페이스 및 네트워크의 기본적인 시스템 구조를 설계합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-450-experience"></a>
### IT컨설턴트 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-450` · 시나리오 `career-net-450-experience` `v001`.
- 원본 위치: `/items/2/data` · 역량: 수리·논리력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. IT컨설턴트의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 현재의 정보시스템을 완전히 교체하기 위해 새로운 시스템을 전면적으로 개발하는 경우, 국내나 국외의 비슷한 시스템에 대해 비교, 분석하며, 필요한 시스템 구성 방안이나 예산을 세우고 시스템이 만들어졌을 때 기대되는 효과를 분석합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10077-experience"></a>
### SNS 마케터 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-10077` · 시나리오 `career-net-10077-experience` `v001`.
- 원본 위치: `/items/3/data` · 역량: 대인관계능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. SNS 마케터의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: SNS(Social Network Service)마케터는 SNS를 통해 상품을 홍보 및 판매하고 소비자 반응을 분석하는 업무를 수행합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10003-experience"></a>
### UX 디자인 컨설턴트 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-10003` · 시나리오 `career-net-10003-experience` `v001`.
- 원본 위치: `/items/4/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. UX 디자인 컨설턴트의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: UX 디자인 컨설턴트는 사용자의 마음과 행동에 대한 조사와 이해를 바탕으로 사용자 입장에서 제품을 설계해 더 편리하게 사용하도록 하는 UX(사용자 경험, UX: User Experience) 디자인 업무를 수행합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-159-experience"></a>
### 가구제조,수리원 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-159` · 시나리오 `career-net-159-experience` `v001`.
- 원본 위치: `/items/5/data` · 역량: 손재능.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 가구제조,수리원의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 가구제조,수리원은 여러 형태의 가구를 가공, 제작하고, 가구의 파손된 부위를 수선하는 일을 담당합니다.
- 체험의 업무 자료: 가구 부품·규격과 완성 상태.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1152-experience"></a>
### 가구조립 및 검사원 — 맞는 부품을 조립하고 완성품 검사

- 직업: `career-net-1152` · 시나리오 `career-net-1152-experience` `v001`.
- 원본 위치: `/items/6/data` · 역량: 손재능.
- 장소 제안: 조립 구역 · `PRM-019 v001` · [PAN-019 v001](../../../images/original/panoramas/PAN-019/v001/prm-019-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 가구조립 및 검사원의 업무 표현과 조립 구역의 부품을 순서대로 결합하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 가구조립 및 검사원은 여러 형태의 가구를 조립하고 조립을 완성한 가구제품의 결함 여부를 검사하는 일을 담당합니다.
- 체험의 업무 자료: 가구 부품·규격과 완성 상태.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 도면에 맞는 부품 선택 | 부품 ID·규격 일치 | 분류·선별 |
| 2 | 공구 거치대 · CND-077 | 공구 거치대의 맞는 공구를 선택해 체결 순서 수행 | 공구·체결 순서 일치 | 순서·절차 |
| 3 | 조립 중인 단순 제품 · CND-078 | 조립 중인 제품을 회전해 결함을 찾아 수정 | 정의된 결함 수정 후 검사 통과 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조립 중인 단순 제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-352-experience"></a>
### 가사도우미 — 가정 방문 요청에 맞춰 정리 활동

- 직업: `career-net-352` · 시나리오 `career-net-352-experience` `v001`.
- 원본 위치: `/items/7/data` · 역량: 대인관계능력.
- 장소 제안: 거실 · `PRM-062 v001` · [PAN-062 v001](../../../images/original/panoramas/PAN-062/v001/prm-062-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 가사도우미의 업무 표현과 거실의 가정 방문·돌봄·생활 행동의 배경이 되는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 가사도우미는 가정에 방문하여 청소, 요리, 세탁 등의 일을 합니다.
- 체험의 업무 자료: 이용자 요청·물품 구역과 점검 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 테이블 · CND-010 | 테이블에서 거주자의 요청·제외 조건 확인 | 요청·제외 조건 확인 | 대화·응대 |
| 2 | 수납장 · CND-009 | 수납장에서 요청 용도별 모형 물건 분류 | 용도·소유 라벨 분류 일치 | 분류·선별 |
| 3 | 독립형 TV · CND-216 | TV UI에서 생활 작업 순서를 정리 | 가상 작업 순서 충족 | 순서·절차 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 TV / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1093-experience"></a>
### 가상현실전문가 — 가상 기능의 요구와 테스트 결과 맞추기

- 직업: `career-net-1093` · 시나리오 `career-net-1093-experience` `v001`.
- 원본 위치: `/items/8/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 가상현실전문가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사용자가 원하는 가상 세계가 무엇인지 파악하거나 개발하고자 하는 시스템을 분석하여 개발 방향을 설정합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 사용자 요구와 다른 실행 결과 찾기 | 명시된 요구·결과 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI로 가상 기능 블록 순서·조건 수정 | 필수 기능 블록과 제약 충족 | 제작·표현 |
| 3 | 마우스 · CND-018 | 마우스로 테스트 단서와 수정 대안을 연결해 재실행 | 가상 테스트의 입력·기대 결과 일치 | 진단·해결 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 마우스 / common / AST-007 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 선택 장면의 기존 필수 후보 밖 추가 제안: CND-018. 기존 후보 목록은 자동 수정하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-280-experience"></a>
### 가수 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-280` · 시나리오 `career-net-280-experience` `v001`.
- 원본 위치: `/items/9/data` · 역량: 음악능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 가수의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 악보를 보고 악기나 녹음된 반주에 맞추어 리듬을 확인하고 노래 연습을 하며, 음반 녹음 및 제작, 방송 출연, 공연이나 콘서트 개최, 각종 행사 출연 등의 활동을 합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1-experience"></a>
### 가스ㆍ수도ㆍ전기 계기 검침원 및 안전점검원 — 배관 모형을 연결하고 상태 확인

- 직업: `career-net-1` · 시나리오 `career-net-1-experience` `v001`.
- 원본 위치: `/items/10/data` · 역량: 신체·운동능력.
- 장소 제안: 설비 작업 구역 · `PRM-037 v001` · [PAN-037 v001](../../../images/original/panoramas/PAN-037/v001/prm-037-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 가스ㆍ수도ㆍ전기 계기 검침원 및 안전점검원의 업무 표현과 설비 작업 구역의 배관과 설비를 설치·점검하는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 가스·수도·전기 계기 검침원 및 안전점검원은 정기적으로 담당 가구나 업소에 방문해서 가스, 수도, 전력 사용량을 검침하고 기록하는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 상자 · CND-137 | 부품 상자에서 연결 규격에 맞는 부품 선택 | 규격·용도 일치 | 분류·선별 |
| 2 | 노출 배관 모형 · CND-135 | 노출 배관 모형의 연결 방향 맞춤 | 위치·방향·연결점 일치 | 조립·배치 |
| 3 | 제어함 · CND-138 | 제어함에서 가상 상태표와 다른 항목 확인 | 가상 오류 항목 식별 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노출 배관 모형 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-41-experience"></a>
### 가전제품 설치 및 수리원 — 가전 모형의 단서를 보고 점검 준비

- 직업: `career-net-41` · 시나리오 `career-net-41-experience` `v001`.
- 원본 위치: `/items/11/data` · 역량: 손재능.
- 장소 제안: 가정 수리 공간 · `PRM-058 v001` · [PAN-058 v001](../../../images/original/panoramas/PAN-058/v001/prm-058-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 가전제품 설치 및 수리원의 업무 표현과 가정 수리 공간의 방문 기술자가 가정용 기기를 점검하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객의 수리 신청이 접수되면 접수된 내용을 확인하고 고객과의 소통을 통해 제품의 문제를 확인합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 간단한 가전제품 · CND-207 | 가전제품 모형의 표시 단서로 고장 가설 선택 | 제공 단서와 가설 일치 | 진단·해결 |
| 2 | 공구 가방 · CND-208 | 공구 가방에서 모형 작업에 맞는 도구 선택 | 도구 역할·가상 작업 조건 일치 | 분류·선별 |
| 3 | 부품 트레이 · CND-040 | 부품 트레이에서 교체 요청과 결과 대조 | 부품·완료 기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 간단한 가전제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 가방 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-174-experience"></a>
### 가축사육자 — 가상 사육 요청에 맞게 용품 준비

- 직업: `career-net-174` · 시나리오 `career-net-174-experience` `v001`.
- 원본 위치: `/items/12/data` · 역량: 자연친화력.
- 장소 제안: 축사 · `PRM-042 v001` · [PAN-042 v001](../../../images/original/panoramas/PAN-042/v001/prm-042-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 가축사육자의 업무 표현과 축사의 가축의 생활과 사료 공급을 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 가축사육자는 가축의 번식과 사육에 대한 지식을 바탕으로 조류, 파충류, 모피생산 동물, 품종을 개량한 조류인 가금, 사냥이 허가 난 새인 엽조류와 더불어 소, 양, 돼지, 산양, 말 등과 같은 가축을 번식하고 사육하며 낙농제품을 생산하는 데 필요한 활동을 기획하고 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 사료 통 · CND-162 | 사료 통의 라벨을 요청 개체 기록과 대조 | 개체 ID·라벨 일치 | 분류·선별 |
| 2 | 급이통 · CND-159 | 급이통의 모형 양을 표시 눈금에 조절 | 교육용 눈금 충족 | 측정·조절 |
| 3 | 물통 · CND-160 | 물통에서 가상 점검표의 누락 항목 확인 | 점검 누락 식별·기록 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 사료 통 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 급이통 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 물통 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-353-experience"></a>
### 간병인 — 생활 요청을 확인하고 이동 환경 점검

- 직업: `career-net-353` · 시나리오 `career-net-353-experience` `v001`.
- 원본 위치: `/items/13/data` · 역량: 대인관계능력.
- 장소 제안: 요양실 · `PRM-017 v001` · [PAN-017 v001](../../../images/original/panoramas/PAN-017/v001/prm-017-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 간병인의 업무 표현과 요양실의 생활 지원과 이동 보조를 받으며 머무는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환자의 체온, 맥박, 호흡수 등을 측정하고 기록하며, 환자가 먹는 음식 및 음료의 양과 내용을 체크하고, 필요에 따라서 환자에게 음식을 먹여 줍니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보조 손잡이 · CND-070 | 보조 손잡이에서 가상 점검표와 다른 상태 확인 | 삽입된 위험 표시 확인 | 관찰·검사 |
| 2 | 휠체어 · CND-069 | 휠체어를 표시된 대기 위치로 옮겨 동선 확보 | 동선·대기 위치 조건 충족 | 조립·배치 |
| 3 | 침대 옆 탁자 · CND-045 | 탁자에서 이용자의 요청을 확인하고 담당자에게 인계 | 요청·조치·인계 확인 응답 | 대화·응대 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보조 손잡이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휠체어 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 침대 옆 탁자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-284-experience"></a>
### 간판제작원 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-284` · 시나리오 `career-net-284-experience` `v001`.
- 원본 위치: `/items/14/data` · 역량: 손재능.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 간판제작원의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 간판제작원은 네온사인이나 안내표지, 실외 간판 등을 설계 및 제작하여 설치하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-354-experience"></a>
### 간호사 — 가상 병실의 요청을 확인하고 편의 준비

- 직업: `career-net-354` · 시나리오 `career-net-354-experience` `v001`.
- 원본 위치: `/items/15/data` · 역량: 대인관계능력.
- 장소 제안: 병실 · `PRM-010 v001` · [PAN-010 v001](../../../images/original/panoramas/PAN-010/v001/prm-010-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 간호사의 업무 표현과 병실의 환자가 머물며 간호를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 수술하는 의사를 돕고, 간호 활동에 대한 기록을 수집하여 관련 문제에 대해 조언을 하기도 합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 호출 장치 · CND-048 | 호출 장치로 요청 내용을 듣고 재확인 | 요청·담당자 확인 | 대화·응대 |
| 2 | 의료 모니터 · CND-042 | 모니터의 가상 기록에서 전달할 변화 항목 확인 | 사례에 제시된 변화 항목 일치 | 관찰·검사 |
| 3 | 이동식 식탁 · CND-047 | 이동 식탁을 지정된 접근 가능한 위치로 이동 | 위치 허용 범위와 동선 확보 | 조립·배치 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 호출 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 식탁 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-355-experience"></a>
### 간호조무사 — 가상 병실의 요청을 확인하고 편의 준비

- 직업: `career-net-355` · 시나리오 `career-net-355-experience` `v001`.
- 원본 위치: `/items/16/data` · 역량: 대인관계능력.
- 장소 제안: 병실 · `PRM-010 v001` · [PAN-010 v001](../../../images/original/panoramas/PAN-010/v001/prm-010-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 간호조무사의 업무 표현과 병실의 환자가 머물며 간호를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환자가 병원에 방문하였을 때 안내해 주고, 각종 의료 검사 및 투약 업무를 보조합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 호출 장치 · CND-048 | 호출 장치로 요청 내용을 듣고 재확인 | 요청·담당자 확인 | 대화·응대 |
| 2 | 의료 모니터 · CND-042 | 모니터의 가상 기록에서 전달할 변화 항목 확인 | 사례에 제시된 변화 항목 일치 | 관찰·검사 |
| 3 | 이동식 식탁 · CND-047 | 이동 식탁을 지정된 접근 가능한 위치로 이동 | 위치 허용 범위와 동선 확보 | 조립·배치 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 호출 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 식탁 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10102-experience"></a>
### 감성인식기술전문가 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10102` · 시나리오 `career-net-10102-experience` `v001`.
- 원본 위치: `/items/17/data` · 역량: 수리·논리력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 감성인식기술전문가의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 인간의 감성을 컴퓨터가 인식할 수 있는 기술을 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-198-experience"></a>
### 감정평가사 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-198` · 시나리오 `career-net-198-experience` `v001`.
- 원본 위치: `/items/18/data` · 역량: 수리·논리력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 감정평가사의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 대상물의 가격에 미치는 모든 요인을 확인하여 부동산 가격을 조사하고, 해당 물건의 용도, 입지 조건, 주변 시설 등을 살핍니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-281-experience"></a>
### 개그맨 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-281` · 시나리오 `career-net-281-experience` `v001`.
- 원본 위치: `/items/19/data` · 역량: 창의력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 개그맨의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 개그맨은 주로 텔레비전이나 라디오 프로그램에 출연하여 말과 몸짓으로 사람들에게 웃음을 줍니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10044-experience"></a>
### 개인관리컨설턴트 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10044` · 시나리오 `career-net-10044-experience` `v001`.
- 원본 위치: `/items/20/data` · 역량: 대인관계능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 개인관리컨설턴트의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 건강관리, 자연치료, 다이어트 등에 관한 조사, 연구를 통해 개인 관리 서비스를 필요로 하는 고객에게 관련 내용을 상담해 줍니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10021-experience"></a>
### 개인미디어 콘텐츠제작자(크리에이터) — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-10021` · 시나리오 `career-net-10021-experience` `v001`.
- 원본 위치: `/items/21/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 개인미디어 콘텐츠제작자(크리에이터)의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 콘텐츠 제작을 위한 자료 조사와 기획·연출, 영상 촬영을 합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10043-experience"></a>
### 개인브랜드매니저 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-10043` · 시나리오 `career-net-10043-experience` `v001`.
- 원본 위치: `/items/22/data` · 역량: 대인관계능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 개인브랜드매니저의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 개인브랜드매니저는 의뢰인이 사회 구성원으로서 원활하게 활동할 수 있도록 의뢰인이 개발하기를 원하는 기술과 능력, 지식에 대해 파악하고, 이러한 특징들을 의뢰인 스스로 인식할 수 있도록 돕는 역할을 수행합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10103-experience"></a>
### 개인형 이동수단 개발자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10103` · 시나리오 `career-net-10103-experience` `v001`.
- 원본 위치: `/items/23/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 개인형 이동수단 개발자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전기자동차, 전동 퀵보드 등 전기를 동력으로 하는 1인용 이동 수단을 연구하고 개발합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-65-experience"></a>
### 건물도장원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-65` · 시나리오 `career-net-65-experience` `v001`.
- 원본 위치: `/items/24/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 건물도장원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 건물도장원은 건축 구조물의 표면에 페인트, 라커 등을 입혀 건축물을 아름답고 오랫동안 보존할 수 있도록 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1130-experience"></a>
### 건설견적원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-1130` · 시나리오 `career-net-1130-experience` `v001`.
- 원본 위치: `/items/25/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 건설견적원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 건설견적원은 도로, 교량, 건축구조물, 전기 및 기계 설비 등의 공사 비용을 분석하고 이에 대한 견적서를 작성하는 일을 담당합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-42-experience"></a>
### 건설공사품질관리원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-42` · 시나리오 `career-net-42-experience` `v001`.
- 원본 위치: `/items/26/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 건설공사품질관리원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 건설 설계도 검토를 통해 품질보증계획서, 품질시험계획서를 작성하고, 건설 현장의 토질과 지반이 예정된 건설 공사에 적합한지 검사합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-77-experience"></a>
### 건설기계운전원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-77` · 시나리오 `career-net-77-experience` `v001`.
- 원본 위치: `/items/27/data` · 역량: 신체·운동능력.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 건설기계운전원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기계의 작동상태를 검사하고 작업지시에 따라 건설기계를 조종합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-46-experience"></a>
### 건축공학기술자 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-46` · 시나리오 `career-net-46-experience` `v001`.
- 원본 위치: `/items/28/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 건축공학기술자의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 건축공학기술자는 건축물 공사 시 전체적인 관리, 감독을 수행하고, 구조 설계, 시공과 관련된 기술적 자문을 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1277-experience"></a>
### 건축사 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-1277` · 시나리오 `career-net-1277-experience` `v001`.
- 원본 위치: `/items/29/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 건축사의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 건축사는 건축주(고객)의 의뢰를 받아 조형미, 경제성, 안전성, 기능성 등을 고려하여 주택, 사무용 빌딩 등의 건축물을 계획하고 설계하는 일을 합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-199-experience"></a>
### 검사 — 가상 사건 자료를 정리하고 설명하기

- 직업: `career-net-199` · 시나리오 `career-net-199-experience` `v001`.
- 원본 위치: `/items/30/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 법정 · `PRM-052 v001` · [PAN-052 v001](../../../images/original/panoramas/PAN-052/v001/prm-052-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 검사의 업무 표현과 법정의 판단·진술·방청의 역할이 좌석 배치로 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 형사사건의 경우 사건의 제반 사항을 조사하고, 사건 관련 증거를 수집하며 이를 분석하고 사건에 적용할 규정이나 기타 법적 문제를 검토한 후 법원의 재판을 요구합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 문서함 · CND-198 | 문서함에서 주장·근거·미확인 자료 구분 | 자료 종류 구분 일치 | 분류·선별 |
| 2 | 진술대 · CND-195 | 진술대에서 확인 질문과 중립적 요약 선택 | 미확인 사실을 단정하지 않는 요약 | 대화·응대 |
| 3 | 당사자 책상 · CND-196 | 당사자 책상에서 제공 근거와 주장 연결 | 가상 자료가 지지하는 관계만 선택 | 진단·해결 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 문서함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 진술대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 당사자 책상 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10020-experience"></a>
### 게임 방송 프로듀서 — 방송 입력을 확인하고 신호에 맞춰 시작

- 직업: `career-net-10020` · 시나리오 `career-net-10020-experience` `v001`.
- 원본 위치: `/items/31/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 방송 스튜디오 · `PRM-031 v001` · [PAN-031 v001](../../../images/original/panoramas/PAN-031/v001/prm-031-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 게임 방송 프로듀서의 업무 표현과 방송 스튜디오의 진행자가 음성과 영상을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 게임 방송 프로듀서는 게임 대회 방송이나 게임 방송 프로그램을 기획하고 제작하는 일을 합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 암 · CND-116 | 마이크 암을 표시 위치로 맞춤 | 위치 허용 범위 충족 | 측정·조절 |
| 2 | 소형 오디오 콘솔 · CND-118 | 오디오 콘솔의 가상 레벨을 목표에 조절 | 가상 레벨 구간 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라의 큐 신호에 맞춰 녹화 입력 | 큐 입력 허용 시간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 암 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 오디오 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10068-experience"></a>
### 게임감시관 및 조사관 — 가상 관제 신호를 확인하고 대응 인계

- 직업: `career-net-10068` · 시나리오 `career-net-10068-experience` `v001`.
- 원본 위치: `/items/32/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 관제실 · `PRM-061 v001` · [PAN-061 v001](../../../images/original/panoramas/PAN-061/v001/prm-061-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 게임감시관 및 조사관의 업무 표현과 관제실의 여러 상태 화면을 확인하고 상황을 조정하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 직원 및 고객의 부정행위 또는 도난 등과 같은 카지노호텔의 비정상적 활동을 감시하고 사전에 예방하는 역할을 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 시간에 따라 바뀌는 이상 신호 확인 | 가상 이상 신호 식별 | 관찰·검사 |
| 2 | 관제 콘솔 · CND-213 | 관제 콘솔에서 가상 대응 우선순위 배치 | 명시된 우선순위 조건 충족 | 계획·배분 |
| 3 | 통신 기기 · CND-175 | 통신 장치로 위치·상태·담당자 전달 | 인계 필드·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관제 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-923-experience"></a>
### 게임기획자 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-923` · 시나리오 `career-net-923-experience` `v001`.
- 원본 위치: `/items/33/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 게임기획자의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국외의 게임 시장 조사를 통해 소비자들이 원하는 게임이 무엇인지를 확인하고, 새로운 게임 제작을 위한 아이디어를 내거나 이에 대한 기획안을 작성합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-358-experience"></a>
### 경비원 — 가상 관제 신호를 확인하고 대응 인계

- 직업: `career-net-358` · 시나리오 `career-net-358-experience` `v001`.
- 원본 위치: `/items/34/data` · 역량: 대인관계능력.
- 장소 제안: 관제실 · `PRM-061 v001` · [PAN-061 v001](../../../images/original/panoramas/PAN-061/v001/prm-061-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 경비원의 업무 표현과 관제실의 여러 상태 화면을 확인하고 상황을 조정하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 경비원은 아파트, 주택, 사무실 등 각종 건물 및 시설물을 관리하며, 건물 내의 거주자들을 화재, 도난, 불법침입으로부터 보호하기 위해 출입자 통제, 내방객 안내 등의 업무를 담당합니다.
- 체험의 업무 자료: 가상 사건·상태 신호와 전달 우선순위.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 시간에 따라 바뀌는 이상 신호 확인 | 가상 이상 신호 식별 | 관찰·검사 |
| 2 | 관제 콘솔 · CND-213 | 관제 콘솔에서 가상 대응 우선순위 배치 | 명시된 우선순위 조건 충족 | 계획·배분 |
| 3 | 통신 기기 · CND-175 | 통신 장치로 위치·상태·담당자 전달 | 인계 필드·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관제 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-202-experience"></a>
### 경영컨설턴트 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-202` · 시나리오 `career-net-202-experience` `v001`.
- 원본 위치: `/items/35/data` · 역량: 수리·논리력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 경영컨설턴트의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 물품의 생산, 유통관리, 판매관리 및 수출입 업무에 대해 상담하고 자문하며, 조사하고 분석합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-203-experience"></a>
### 경제학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-203` · 시나리오 `career-net-203-experience` `v001`.
- 원본 위치: `/items/36/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 경제학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 경제 관계 자료를 검토하고 분석하여 연구 결과를 제시하고, 관련 전문가들과 논의하여 정책 제언 등을 도출합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-359-experience"></a>
### 경찰관 — 가상 사건의 단서와 사실 기록 정리

- 직업: `career-net-359` · 시나리오 `career-net-359-experience` `v001`.
- 원본 위치: `/items/37/data` · 역량: 신체·운동능력.
- 장소 제안: 수사실 · `PRM-050 v001` · [PAN-050 v001](../../../images/original/panoramas/PAN-050/v001/prm-050-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 경찰관의 업무 표현과 수사실의 기록과 단서를 비교하는 업무 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 교통을 단속하고 교통사고 예방을 위한 계획을 세우는 등 교통안전을 위한 일을 합니다.
- 체험의 업무 자료: 가상 사건·상태 신호와 전달 우선순위.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 트레이 · CND-049 | 서류 트레이에서 사실·진술·미확인 자료 구분 | 자료 종류 분류 일치 | 분류·선별 |
| 2 | 관계 보드 · CND-191 | 관계 보드에서 단서와 가설 연결 | 제공 단서에 맞는 가설 관계 | 진단·해결 |
| 3 | 모니터 · CND-005 | 모니터에서 근거 없는 기록을 찾아 보류 | 근거 없는 확정 기록을 보류 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관계 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-360-experience"></a>
### 경호원 — 가상 관제 신호를 확인하고 대응 인계

- 직업: `career-net-360` · 시나리오 `career-net-360-experience` `v001`.
- 원본 위치: `/items/38/data` · 역량: 신체·운동능력.
- 장소 제안: 관제실 · `PRM-061 v001` · [PAN-061 v001](../../../images/original/panoramas/PAN-061/v001/prm-061-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 경호원의 업무 표현과 관제실의 여러 상태 화면을 확인하고 상황을 조정하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 경호 대상자의 정보(개인 경력, 인적 사항, 상황 등) 및 고객의 경호 내용을 확인하고 위험한 요인이 무엇인지 파악하여 적절한 경호 방법을 선택하여 경호 계획을 수립합니다.
- 체험의 업무 자료: 가상 사건·상태 신호와 전달 우선순위.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 시간에 따라 바뀌는 이상 신호 확인 | 가상 이상 신호 식별 | 관찰·검사 |
| 2 | 관제 콘솔 · CND-213 | 관제 콘솔에서 가상 대응 우선순위 배치 | 명시된 우선순위 조건 충족 | 계획·배분 |
| 3 | 통신 기기 · CND-175 | 통신 장치로 위치·상태·담당자 전달 | 인계 필드·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관제 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1116-experience"></a>
### 계산원 및 매표원 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-1116` · 시나리오 `career-net-1116-experience` `v001`.
- 원본 위치: `/items/39/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 계산원 및 매표원의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 매표원은 정원이나 예약 상황을 검토하여 매표 수를 확인하고 시간이나 좌석번호 등을 표에 기록하여 단말기에 입출력하여 고객에게 판매합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-469-experience"></a>
### 고객관리시스템(CRM)전문가 — 방문객의 요청을 확인하고 접수 완료

- 직업: `career-net-469` · 시나리오 `career-net-469-experience` `v001`.
- 원본 위치: `/items/40/data` · 역량: 수리·논리력.
- 장소 제안: 민원·방문객 접수실 · `PRM-004 v001` · [PAN-004 v001](../../../images/original/panoramas/PAN-004/v001/D-public-reception-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 고객관리시스템(CRM)전문가의 업무 표현과 민원·방문객 접수실의 방문객이 대기한 뒤 직원에게 서류를 접수하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객관리시스템전문가는 고객과 관련된 기업의 내외부 자료를 분석 및 통합하여 사용자의 특성에 기초한 기업의 영업 활동을 지원하기 위한 정보시스템을 연구하고 설계하는 일을 합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 번호표 발급기 · CND-024 | 번호표 기기에서 업무 종류와 순번 확인 | 업무 종류와 순번 일치 | 순서·절차 |
| 2 | 모니터 · CND-005 | 화면의 신청 정보와 요청을 대조 | 필수 정보 누락 없음 | 관찰·검사 |
| 3 | 서비스 카운터 · CND-023 | 카운터에서 빠진 정보를 질문하고 다음 절차 안내 | 방문객 확인 응답과 안내 목적지 일치 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 번호표 발급기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서비스 카운터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-183-experience"></a>
### 곡식작물재배자 — 작물 모형 상태를 보고 관리·분류

- 직업: `career-net-183` · 시나리오 `career-net-183-experience` `v001`.
- 원본 위치: `/items/41/data` · 역량: 자연친화력.
- 장소 제안: 재배지 · `PRM-040 v001` · [PAN-040 v001](../../../images/original/panoramas/PAN-040/v001/prm-040-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 곡식작물재배자의 업무 표현과 재배지의 작물을 심고 돌보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 곡식작물재배자는 농업에 대한 지식을 바탕으로 벼, 보리, 쌀 등 곡식을 재배하기 위한 계획을 세우고, 각종 농작물 재배 방법이나 기계 등을 이용하여 곡식을 생산하고 수확하는 일을 담당합니다.
- 체험의 업무 자료: 가상 구획·관리 요청과 상태 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 농작물 · CND-148 | 작물 모형에서 사례의 상태 차이 찾기 | 사례에서 지정한 상태 차이 식별 | 관찰·검사 |
| 2 | 물뿌리개 · CND-149 | 물뿌리개 양을 가상 목표 눈금에 맞춤 | 훈련용 양 범위 충족 | 측정·조절 |
| 3 | 수확 상자 · CND-151 | 수확 상자에 가상 등급별 분류 | 사례 등급 규칙 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 농작물 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 물뿌리개 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수확 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10006-experience"></a>
### 곤충 음식 개발자·조리사 — 주문에 맞게 조리 준비 순서 맞추기

- 직업: `career-net-10006` · 시나리오 `career-net-10006-experience` `v001`.
- 원본 위치: `/items/42/data` · 역량: 손재능.
- 장소 제안: 주방 · `PRM-024 v001` · [PAN-024 v001](../../../images/original/panoramas/PAN-024/v001/prm-024-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 곤충 음식 개발자·조리사의 업무 표현과 주방의 식재료 준비에서 조리와 담기까지 이어지는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 곤충 음식 개발자는 곤충을 재료로 사람이 먹을 수 있는 식품을 연구하고 만드는 방법을 개발합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 냉장고 · CND-090 | 냉장고에서 주문과 재료 라벨 대조 | 재료·주문·구역 구분 일치 | 분류·선별 |
| 2 | 조리대 · CND-088 | 조리대에서 가상 조리 단계를 순서대로 배치 | 가상 레시피 단계 일치 | 순서·절차 |
| 3 | 가열 기구 · CND-089 | 가열 기구를 교육용 표시 범위에 조절 | 훈련용 눈금 범위 충족 | 측정·조절 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 냉장고 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조리대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 가열 기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1135-experience"></a>
### 공구제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1135` · 시나리오 `career-net-1135-experience` `v001`.
- 원본 위치: `/items/43/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 공구제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 공구 설계도나 작업 지시서를 확인하고, 공구 제작 절차와 방법에 따라 선택한 금속재료를 준비합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-985-experience"></a>
### 공업기계설치 및 정비원 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-985` · 시나리오 `career-net-985-experience` `v001`.
- 원본 위치: `/items/44/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 공업기계설치 및 정비원의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 공업기계설치 및 정비원은 각종 제품 생산에 사용되는 기계를 설치하고, 기계의 고장을 확인하여 이를 수리합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-929-experience"></a>
### 공예원 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-929` · 시나리오 `career-net-929-experience` `v001`.
- 원본 위치: `/items/45/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 공예원의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 공예원은 사용하는 재료나 만드는 제품에 따라 목공예원, 석공예원, 도자기공예원, 금속공예원 등으로 구분되며, 목공예원은 나무를 이용하여 목기 제품, 실내 장식장, 일반 가구 등을 제작합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-48-experience"></a>
### 공작기계조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-48` · 시나리오 `career-net-48-experience` `v001`.
- 원본 위치: `/items/46/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 공작기계조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 금속 공작물의 설계 도면, 명세서, 작업지시서를 검토하여 공정 순서에 따라 절삭, 연삭, 용접, 마무리 작업 등의 가공 계획을 세웁니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10080-experience"></a>
### 공정무역전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-10080` · 시나리오 `career-net-10080-experience` `v001`.
- 원본 위치: `/items/47/data` · 역량: 수리·논리력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 공정무역전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 공정무역전문가는 개발도상국에서 생산한 제품을 소비자가 구입할 수 있도록 교역을 돕는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1155-experience"></a>
### 과수작물재배자 — 작물 모형 상태를 보고 관리·분류

- 직업: `career-net-1155` · 시나리오 `career-net-1155-experience` `v001`.
- 원본 위치: `/items/48/data` · 역량: 자연친화력.
- 장소 제안: 재배지 · `PRM-040 v001` · [PAN-040 v001](../../../images/original/panoramas/PAN-040/v001/prm-040-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 과수작물재배자의 업무 표현과 재배지의 작물을 심고 돌보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 재배하는 과수 작물의 종류와 양을 결정하고 계획합니다.
- 체험의 업무 자료: 가상 구획·관리 요청과 상태 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 농작물 · CND-148 | 작물 모형에서 사례의 상태 차이 찾기 | 사례에서 지정한 상태 차이 식별 | 관찰·검사 |
| 2 | 물뿌리개 · CND-149 | 물뿌리개 양을 가상 목표 눈금에 맞춤 | 훈련용 양 범위 충족 | 측정·조절 |
| 3 | 수확 상자 · CND-151 | 수확 상자에 가상 등급별 분류 | 사례 등급 규칙 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 농작물 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 물뿌리개 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수확 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-207-experience"></a>
### 관세사 — 가상 창구 요청과 문서 확인

- 직업: `career-net-207` · 시나리오 `career-net-207-experience` `v001`.
- 원본 위치: `/items/49/data` · 역량: 수리·논리력.
- 장소 제안: 금융 창구 · `PRM-056 v001` · [PAN-056 v001](../../../images/original/panoramas/PAN-056/v001/prm-056-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 관세사의 업무 표현과 금융 창구의 고객이 금융 서류를 제출하고 창구 서비스를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 수출입 물품에 대해 물품 분류 기호에 따라 분류하고 이에 대한 세율을 부과합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 트레이 · CND-049 | 트레이에서 요청 종류별 모형 문서 분류 | 요청별 필수 문서 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | PC에서 가상 입력 정보와 제출 자료 대조 | 가상 기록 필드 일치 | 관찰·검사 |
| 3 | 서비스 카운터 · CND-023 | 창구에서 빠진 정보를 질문하고 결과 요약 | 필수 정보 확인·수신 응답 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서비스 카운터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-232-experience"></a>
### 광고 및 홍보전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-232` · 시나리오 `career-net-232-experience` `v001`.
- 원본 위치: `/items/50/data` · 역량: 언어능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 광고 및 홍보전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 광고전문가는 광고할 상품이나 용역에 대해 조사 및 분석하여 광고 기획서를 작성합니다. 광고의 제작 방향과 소요되는 예산을 수립하고 조정하며 상품의 경쟁 상황, 시장상황, 판매 기간 등에 대한 자료와 광고매체에 대한 효과를 분석하여 광고를 제작합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-283-experience"></a>
### 광고기획자 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-283` · 시나리오 `career-net-283-experience` `v001`.
- 원본 위치: `/items/51/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 광고기획자의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 상품의 판매 자료나 시장조사 자료, 제품 정보 등을 입수하여 소비자의 성향을 분석하고 광고 제작 방향을 정합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-285-experience"></a>
### 광고디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-285` · 시나리오 `career-net-285-experience` `v001`.
- 원본 위치: `/items/52/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 광고디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 제품이나 서비스 등 광고할 대상의 특성 및 소비자의 유형, 시장동향 등을 분석합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-49-experience"></a>
### 광원 및 채석원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-49` · 시나리오 `career-net-49-experience` `v001`.
- 원본 위치: `/items/53/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 광원 및 채석원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 광원 및 채석원은 지하에 매장되어 있는 석탄, 금속, 비금속 등의 광물과 건설 석재를 채굴하고 운반하며, 채석된 석재를 가공하는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10054-experience"></a>
### 괴롭힘방지조언사 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10054` · 시나리오 `career-net-10054-experience` `v001`.
- 원본 위치: `/items/54/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 괴롭힘방지조언사의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 괴롭힘방지조언사는 직장 내 구성원들의 대인관계에서 문제가 발생할 수 있는 원인을 분석하고, 예방 조치를 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-363-experience"></a>
### 교도관 — 가상 사건의 단서와 사실 기록 정리

- 직업: `career-net-363` · 시나리오 `career-net-363-experience` `v001`.
- 원본 위치: `/items/55/data` · 역량: 신체·운동능력.
- 장소 제안: 수사실 · `PRM-050 v001` · [PAN-050 v001](../../../images/original/panoramas/PAN-050/v001/prm-050-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 교도관의 업무 표현과 수사실의 기록과 단서를 비교하는 업무 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 교도관은 교도소, 구치소 등 교정시설에서 수용자를 관리 및 감독하고, 교정 교육을 합니다.
- 체험의 업무 자료: 가상 사건·상태 신호와 전달 우선순위.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 트레이 · CND-049 | 서류 트레이에서 사실·진술·미확인 자료 구분 | 자료 종류 분류 일치 | 분류·선별 |
| 2 | 관계 보드 · CND-191 | 관계 보드에서 단서와 가설 연결 | 제공 단서에 맞는 가설 관계 | 진단·해결 |
| 3 | 모니터 · CND-005 | 모니터에서 근거 없는 기록을 찾아 보류 | 근거 없는 확정 기록을 보류 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관계 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1103-experience"></a>
### 교육학연구원 — 짧은 설명 발표와 장비 준비

- 직업: `career-net-1103` · 시나리오 `career-net-1103-experience` `v001`.
- 원본 위치: `/items/56/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 강의실 · `PRM-014 v001` · [PAN-014 v001](../../../images/original/panoramas/PAN-014/v001/prm-014-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 교육학연구원의 업무 표현과 강의실의 강사가 설명하고 청중이 듣는 소규모 교육 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 교육학연구원은 교육의 목적, 내용, 방법 등에 관한 종합적이며 과학적인 연구를 실시하고, 합리적인 교육체제 및 방법을 설계하고 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 발표 화면 · CND-060 | 발표 화면의 개념 카드를 이해 순서대로 배치 | 필수 개념·논리 순서 충족 | 제작·표현 |
| 2 | 강연대 · CND-059 | 강연대에서 청중 질문에 근거를 들어 설명 | 질문 의도·설명 확인 응답 | 대화·응대 |
| 3 | 작은 AV 장치 · CND-061 | AV 장치의 가상 음량을 목표 구간에 조절 | 연습용 음량 범위 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 발표 화면 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 강연대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 AV 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-481-experience"></a>
### 교장 — 짧은 설명 발표와 장비 준비

- 직업: `career-net-481` · 시나리오 `career-net-481-experience` `v001`.
- 원본 위치: `/items/57/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 강의실 · `PRM-014 v001` · [PAN-014 v001](../../../images/original/panoramas/PAN-014/v001/prm-014-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 교장의 업무 표현과 강의실의 강사가 설명하고 청중이 듣는 소규모 교육 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 교장은 초등학교나 중학교, 고등학교, 특수학교를 대표하는 책임자로서 학교의 교육, 행정 및 기타 운영 활동에 관련된 모든 제반 사항을 기획하고 조정하는 일을 합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 발표 화면 · CND-060 | 발표 화면의 개념 카드를 이해 순서대로 배치 | 필수 개념·논리 순서 충족 | 제작·표현 |
| 2 | 강연대 · CND-059 | 강연대에서 청중 질문에 근거를 들어 설명 | 질문 의도·설명 확인 응답 | 대화·응대 |
| 3 | 작은 AV 장치 · CND-061 | AV 장치의 가상 음량을 목표 구간에 조절 | 연습용 음량 범위 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 발표 화면 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 강연대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 AV 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1119-experience"></a>
### 구두미화원 및 수선원 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-1119` · 시나리오 `career-net-1119-experience` `v001`.
- 원본 위치: `/items/58/data` · 역량: 손재능.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 구두미화원 및 수선원의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 구두미화원 및 수선원은 고객의 구두에 묻은 각종 이물질을 제거하고 구두의 광택을 내는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-260-experience"></a>
### 구성작가 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-260` · 시나리오 `career-net-260-experience` `v001`.
- 원본 위치: `/items/59/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 구성작가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 교양 및 예능 프로그램의 제작 형식을 기획하고 검토하여 제작에 필요한 자료를 수집하고 정리합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-286-experience"></a>
### 국악인 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-286` · 시나리오 `career-net-286-experience` `v001`.
- 원본 위치: `/items/60/data` · 역량: 음악능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 국악인의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국악인은 전통음악을 하는 사람으로, 가야금, 해금 등의 국악기를 연주하거나 판소리, 민요 등을 부릅니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10078-experience"></a>
### 국제개발협력전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-10078` · 시나리오 `career-net-10078-experience` `v001`.
- 원본 위치: `/items/61/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 국제개발협력전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 각 국가의 수요에 따른 개발 사업을 기획 및 논의하고, 진행 과정을 관리합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-208-experience"></a>
### 국제무역사무원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-208` · 시나리오 `career-net-208-experience` `v001`.
- 원본 위치: `/items/62/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 국제무역사무원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 수출, 수입 바이어와 상담을 하며, 수출과 수입 시 발생하는 외국환을 취급하고 관리합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-209-experience"></a>
### 국제회의전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-209` · 시나리오 `career-net-209-experience` `v001`.
- 원본 위치: `/items/63/data` · 역량: 대인관계능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 국제회의전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국제회의전문가는 국제회의의 기획 및 유치, 준비, 진행 등과 관련된 제반 업무를 조정 및 운영하며, 회의 목표를 설정하고 회의 운영과 관련된 예산을 관리하는 등의 업무도 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1061-experience"></a>
### 국회의원 — 접수 문서를 확인하고 담당자에게 전달

- 직업: `career-net-1061` · 시나리오 `career-net-1061-experience` `v001`.
- 원본 위치: `/items/64/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 행정·문서 처리 사무실 · `PRM-003 v001` · [PAN-003 v001](../../../images/original/panoramas/PAN-003/v001/C-public-administration-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 국회의원의 업무 표현과 행정·문서 처리 사무실의 기관 내부 담당자가 기록·검토·결재하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국회의원은 선거를 통해 선출된 국민의 대표로서 국회에서 헌법과 법률의 개정 및 의결과 관련된 일을 하고, 정부 예산안을 심의 및 확정하는 등의 업무를 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류철 · CND-022 | 서류철의 문서를 업무 종류별로 분류 | 문서별 분류 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 기록 화면과 문서의 불일치 수정 | 기록과 문서의 필수 항목 일치 | 관찰·검사 |
| 3 | 유선전화 · CND-019 | 전화로 누락 정보를 확인하고 결과 인계 | 확인 질문과 전달 필드 충족 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류철 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 유선전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1100-experience"></a>
### 군무원 — 행정 일정과 전달 기록 맞추기

- 직업: `career-net-1100` · 시나리오 `career-net-1100-experience` `v001`.
- 원본 위치: `/items/65/data` · 역량: 대인관계능력.
- 장소 제안: 군 행정실 · `PRM-065 v001` · [PAN-065 v001](../../../images/original/panoramas/PAN-065/v001/prm-065-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 군무원의 업무 표현과 군 행정실의 군 조직의 문서·일정 업무를 처리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 업무 분야에 대한 전문 지식을 활용하여 보고서 및 문서를 작성하고 관리합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 일정 보드 · CND-219 | 일정 보드에서 업무·시간 배분 | 일정 충돌·누락 없음 | 계획·배분 |
| 2 | 모니터 · CND-005 | PC에서 문서와 일정 불일치 확인 | 문서와 일정 필드 일치 | 관찰·검사 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 담당자에게 요청 전달 | 담당·기한·수신 확인 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 일정 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-740-experience"></a>
### 귀금속 및 보석세공원 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-740` · 시나리오 `career-net-740-experience` `v001`.
- 원본 위치: `/items/66/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 귀금속 및 보석세공원의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 제작한 귀금속에 보석을 알맞은 크기로 가공하여 맞춰 끼우거나 확대경을 사용해 불순물, 깨짐, 표면 상태, 규격 등을 검사하거나 결함을 수리합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-261-experience"></a>
### 극작가 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-261` · 시나리오 `career-net-261-experience` `v001`.
- 원본 위치: `/items/67/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 극작가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 연극 작품의 주제를 선정하고 내용에 따른 역사적 현실이나 사건의 과정 등을 조사 및 분석하여 작품의 줄거리를 구상합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-52-experience"></a>
### 금속가공장치조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-52` · 시나리오 `career-net-52-experience` `v001`.
- 원본 위치: `/items/68/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 금속가공장치조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 금속가공장치조작원은 광석의 불순물을 제거하고 제련, 정련 과정을 거쳐 제철과 제강 등을 위해 장치를 조작하는 업무를 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-53-experience"></a>
### 금속공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-53` · 시나리오 `career-net-53-experience` `v001`.
- 원본 위치: `/items/69/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 금속공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 금속공학기술자는 금속, 합금의 제조와 가공 방법 개발을 위해 금속의 물리적, 조직적 특성을 실험하고 연구하며, 장단기 기술개발 계획을 수립하는 업무를 수행합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-244-experience"></a>
### 금융자산운용가(펀드매니저) — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-244` · 시나리오 `career-net-244-experience` `v001`.
- 원본 위치: `/items/70/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 금융자산운용가(펀드매니저)의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 간접투자상품을 개발하여 투자 고객들에게 판매하고, 투자신탁의 재산을 운용하거나 기관투자가의 펀드를 관리하고 운용합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-54-experience"></a>
### 금형원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-54` · 시나리오 `career-net-54-experience` `v001`.
- 원본 위치: `/items/71/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 금형원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 설계 도면과 작업지시서 검토를 통해 작업의 절차와 방법에 대한 계획을 세웁니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-56-experience"></a>
### 기계공학 기술자ㆍ연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-56` · 시나리오 `career-net-56-experience` `v001`.
- 원본 위치: `/items/72/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 기계공학 기술자ㆍ연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기계공학 기술자ㆍ연구원은 다양한 산업과 연관된 기계, 기구, 산업 설비, 생산시스템 등을 연구, 개발, 설계, 제조하고, 생산 공정을 운영, 감독하는 업무를 수행합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-6-experience"></a>
### 기상연구원 — 관측 장치를 맞추고 기록 오류 확인

- 직업: `career-net-6` · 시나리오 `career-net-6-experience` `v001`.
- 원본 위치: `/items/73/data` · 역량: 수리·논리력.
- 장소 제안: 관측 지점 · `PRM-039 v001` · [PAN-039 v001](../../../images/original/panoramas/PAN-039/v001/prm-039-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 기상연구원의 업무 표현과 관측 지점의 설치한 측정 장비로 환경 변화를 관찰하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기류의 방향, 속도, 기압, 온도, 습도 등 기상현상과 대기, 기후, 해양기상, 지진 특성 등을 조사하고 분석하여 보다 정확한 일기예보 기법을 개발하기 위한 연구를 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 삼각대 센서 · CND-144 | 삼각대 센서를 표시 방향에 배치 | 위치·방향 일치 | 조립·배치 |
| 2 | 소형 관측 장치 · CND-145 | 관측 장치의 가상 눈금을 조절 | 훈련용 설정 범위 충족 | 측정·조절 |
| 3 | 데이터 기록 기기 · CND-146 | 기록 기기의 이상 데이터 지점을 표시 | 삽입된 이상 지점·기록 일치 | 관찰·검사 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 삼각대 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 관측 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 데이터 기록 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-238-experience"></a>
### 기업고위임원 — 접수 문서를 확인하고 담당자에게 전달

- 직업: `career-net-238` · 시나리오 `career-net-238-experience` `v001`.
- 원본 위치: `/items/74/data` · 역량: 수리·논리력.
- 장소 제안: 행정·문서 처리 사무실 · `PRM-003 v001` · [PAN-003 v001](../../../images/original/panoramas/PAN-003/v001/C-public-administration-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 기업고위임원의 업무 표현과 행정·문서 처리 사무실의 기관 내부 담당자가 기록·검토·결재하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 이사회나 이와 유사한 운영 기관 또는 법령에 의해 위임된 권한 하에 사업체의 전반적인 정책을 수립하고 운영 현황, 과거의 실적, 미래의 계획을 평가하여 사업 계획을 결정합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류철 · CND-022 | 서류철의 문서를 업무 종류별로 분류 | 문서별 분류 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 기록 화면과 문서의 불일치 수정 | 기록과 문서의 필수 항목 일치 | 관찰·검사 |
| 3 | 유선전화 · CND-019 | 전화로 누락 정보를 확인하고 결과 인계 | 확인 질문과 전달 필드 충족 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류철 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 유선전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-262-experience"></a>
### 기자 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-262` · 시나리오 `career-net-262-experience` `v001`.
- 원본 위치: `/items/75/data` · 역량: 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 기자의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 활동하는 매체에 따라 방송기자, 신문기자, 잡지기자 등으로 분류되고, 담당 업무에 따라 취재기자, 편집기자, 사진기자 등으로 구분되며 취재 분야에 따라 스포츠, 연예, 의학 전문기자로 나누기도 합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10026-experience"></a>
### 기후변화 대응 전문가 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-10026` · 시나리오 `career-net-10026-experience` `v001`.
- 원본 위치: `/items/76/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 기후변화 대응 전문가의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기후변화 대응 전문가는 기후변화가 기업이나 정부 정책에 미치는 영향을 분석하고 대응 방안을 제시합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10109-experience"></a>
### 나노공학 기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10109` · 시나리오 `career-net-10109-experience` `v001`.
- 원본 위치: `/items/77/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 나노공학 기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 나노공학 기술자는 나노미터(1 나노는 10억 분의 1m)를 탐구하는 나노기술을 활용하여 전자(소자), 바이오, 소재, 공장장비 및 측정 기기 등을 개발하고 관리합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-58-experience"></a>
### 냉동기사 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-58` · 시나리오 `career-net-58-experience` `v001`.
- 원본 위치: `/items/78/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 냉동기사의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 냉동장치 계측기를 활용해서 온도, 습도, 저항, 압력 등을 측정하고 관찰 및 기록합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-247-experience"></a>
### 네이미스트 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-247` · 시나리오 `career-net-247-experience` `v001`.
- 원본 위치: `/items/79/data` · 역량: 언어능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 네이미스트의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 네이미스트는 문예 창작에 대한 지식을 바탕으로 기업명이나 상표, 도메인, 인명 등 전문적으로 이름을 짓습니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-288-experience"></a>
### 네일아티스트 — 요청 스타일과 준비 물품 확인

- 직업: `career-net-288` · 시나리오 `career-net-288-experience` `v001`.
- 원본 위치: `/items/80/data` · 역량: 손재능.
- 장소 제안: 미용실 · `PRM-023 v001` · [PAN-023 v001](../../../images/original/panoramas/PAN-023/v001/prm-023-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 네일아티스트의 업무 표현과 미용실의 고객의 머리를 손질하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객의 건강 상태와 미용 관리 부위에 대한 정보를 파악하여 손, 손톱, 발, 발톱의 미용 관리 및 제모에 대해 구체적으로 계획을 세웁니다.
- 체험의 업무 자료: 고객의 요청 형태·제외 조건과 준비 도구.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 독립형 거울 · CND-086 | 거울 앞 UI에서 원하는 형태와 불편 사항 확인 | 고객 요청 확인 응답 | 대화·응대 |
| 2 | 운반 카트 · CND-016 | 카트에서 요청에 맞는 모형 도구 선택 | 도구 역할·구역 일치 | 분류·선별 |
| 3 | 세발대 · CND-087 | 세발대에서 가상 준비 단계를 순서대로 선택 | 교육용 준비 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 독립형 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세발대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-430-experience"></a>
### 네트워크엔지니어 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-430` · 시나리오 `career-net-430-experience` `v001`.
- 원본 위치: `/items/81/data` · 역량: 수리·논리력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 네트워크엔지니어의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 네트워크 시스템의 전체 구조를 분석 및 평가하여 문제점과 개선책을 마련하거나 사용자의 요구와 기대를 만족시키는 네트워크 시스템에 대한 기능성, 안정성, 확장성, 변경 가능성, 관리 용이성을 고려하여 구조를 설계합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10011-experience"></a>
### 노년 플래너 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10011` · 시나리오 `career-net-10011-experience` `v001`.
- 원본 위치: `/items/82/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 노년 플래너의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객의 경제 상황이나 가족관계, 건강상태, 정서, 노후 계획 등에 대해 파악하고 적합한 노후생활을 할 수 있도록 상담합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-205-experience"></a>
### 노무사 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-205` · 시나리오 `career-net-205-experience` `v001`.
- 원본 위치: `/items/83/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 노무사의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사업주나 노동조합의 의뢰로 노사 분쟁 예방과 해결을 위해 노사문제에 대한 상담과 자문을 하고, 노사 분쟁을 조정하고 중재하며 단체협약 분석 등 단체교섭을 대리하기도 합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10013-experience"></a>
### 노인 전문 간호사 — 가상 병실의 요청을 확인하고 편의 준비

- 직업: `career-net-10013` · 시나리오 `career-net-10013-experience` `v001`.
- 원본 위치: `/items/84/data` · 역량: 대인관계능력.
- 장소 제안: 병실 · `PRM-010 v001` · [PAN-010 v001](../../../images/original/panoramas/PAN-010/v001/prm-010-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 노인 전문 간호사의 업무 표현과 병실의 환자가 머물며 간호를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 노인의 가족과 상담을 통해 요구 사항을 반영해 간호 계획을 수립하고, 노인의 건강상태에 관한 자료를 기록하고 관리합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 호출 장치 · CND-048 | 호출 장치로 요청 내용을 듣고 재확인 | 요청·담당자 확인 | 대화·응대 |
| 2 | 의료 모니터 · CND-042 | 모니터의 가상 기록에서 전달할 변화 항목 확인 | 사례에 제시된 변화 항목 일치 | 관찰·검사 |
| 3 | 이동식 식탁 · CND-047 | 이동 식탁을 지정된 접근 가능한 위치로 이동 | 위치 허용 범위와 동선 확보 | 조립·배치 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 호출 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 식탁 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-59-experience"></a>
### 녹음기사 — 소재를 골라 짧은 영상 흐름 완성

- 직업: `career-net-59` · 시나리오 `career-net-59-experience` `v001`.
- 원본 위치: `/items/85/data` · 역량: 음악능력.
- 장소 제안: 영상 편집실 · `PRM-032 v001` · [PAN-032 v001](../../../images/original/panoramas/PAN-032/v001/prm-032-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 녹음기사의 업무 표현과 영상 편집실의 영상과 소리를 검토하고 편집하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 촬영 장소에 대한 사전 답사를 통해 주변 환경을 확인하고 촬영에 대한 대비를 제작진에게 요구합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 미디어 보관함 · CND-121 | 미디어 보관함에서 요청 장면 선택 | 소재 ID·권장 용도 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 모니터에서 컷의 순서·길이를 편집 | 필수 장면·순서 충족 | 제작·표현 |
| 3 | 헤드폰 · CND-117 | 헤드폰에서 가상 음성·장면 동기 오류 확인 | 삽입된 동기 오류 표시·수정 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 미디어 보관함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 헤드폰 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-211-experience"></a>
### 농수산물중개인 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-211` · 시나리오 `career-net-211-experience` `v001`.
- 원본 위치: `/items/86/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 농수산물중개인의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 각종 자료를 수집하여 농수산물의 종류, 품질, 가격 등에 대한 시장 정보를 분석하며, 상품의 샘플을 검사하여 등급과 상품의 질을 결정합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-182-experience"></a>
### 농업기술자 — 모종 위치와 가상 재배 환경 맞추기

- 직업: `career-net-182` · 시나리오 `career-net-182-experience` `v001`.
- 원본 위치: `/items/87/data` · 역량: 자연친화력.
- 장소 제안: 온실 · `PRM-041 v001` · [PAN-041 v001](../../../images/original/panoramas/PAN-041/v001/prm-041-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 농업기술자의 업무 표현과 온실의 통제된 재배 환경에서 식물을 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 농업기술자는 농업에 대한 지식을 바탕으로 농업의 발전과 농업인의 복지 향상을 도모하기 위하여 농업과학기술의 진흥을 위한 연구와 농촌지도, 농업 관련인에 대한 교육 훈련 업무를 수행합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모종 트레이 · CND-154 | 모종 트레이에서 요청 모종 선택 | 모종 ID·구획 일치 | 분류·선별 |
| 2 | 환경 센서 · CND-156 | 환경 센서의 가상 기록 변화 확인 | 가상 변화 지점 식별 | 관찰·검사 |
| 3 | 관수 설비 · CND-155 | 관수 설비를 교육용 목표 구간에 조절 | 교육용 설정 범위 충족 | 측정·조절 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모종 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 환경 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관수 설비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10075-experience"></a>
### 다문화코디네이터 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10075` · 시나리오 `career-net-10075-experience` `v001`.
- 원본 위치: `/items/88/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 다문화코디네이터의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 다문화코디네이터는 다문화가정의 자녀가 교육을 받는 데 필요한 프로그램을 소개하고 지원하는 업무를 수행합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-126-experience"></a>
### 단순노무자 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-126` · 시나리오 `career-net-126-experience` `v001`.
- 원본 위치: `/items/89/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 단순노무자의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 단순노무자는 건설업이나 제조업, 유통업 등의 분야에서 제품이나 자재의 운반, 분류 및 단순 포장을 수행하거나 손이나 기계를 이용하여 구성품을 조립하는 등의 일을 담당합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1132-experience"></a>
### 단열원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-1132` · 시나리오 `career-net-1132-experience` `v001`.
- 원본 위치: `/items/90/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 단열원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작업 대상물에 따라 재료와 시공 방법을 결정하고 작업 계획을 세웁니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1139-experience"></a>
### 단조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1139` · 시나리오 `career-net-1139-experience` `v001`.
- 원본 위치: `/items/91/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 단조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 도면과 완성된 제품을 비교하여 제품의 결함 여부와 길이나 크기가 정확한지에 대해 확인합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-61-experience"></a>
### 대기환경기술자 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-61` · 시나리오 `career-net-61-experience` `v001`.
- 원본 위치: `/items/92/data` · 역량: 자연친화력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 대기환경기술자의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 대기환경기술자는 대기오염 상태를 측정, 분석하고, 대기오염을 방지할 수 있는 방법에 대해 연구, 실험하며, 대기오염방지시설과 장치 등을 설계, 개발하는 업무를 담당합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1282-experience"></a>
### 대체에너지개발연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1282` · 시나리오 `career-net-1282-experience` `v001`.
- 원본 위치: `/items/93/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 대체에너지개발연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 대체에너지개발연구원은 태양열, 태양광, 조력, 풍력, 바이오매스 등의 대체 에너지를 연구ㆍ개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1078-experience"></a>
### 대형트럭 및 특수차운전원 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-1078` · 시나리오 `career-net-1078-experience` `v001`.
- 원본 위치: `/items/94/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 대형트럭 및 특수차운전원의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 엔진오일, 냉각수, 타이어의 공기 압력 등을 점검하고 각종 안전장치의 이상 유무를 확인합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10118-experience"></a>
### 데이터 라벨러 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-10118` · 시나리오 `career-net-10118-experience` `v001`.
- 원본 위치: `/items/95/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 데이터 라벨러의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 데이터 라벨러는 인공지능이 학습 데이터를 쉽게 인식할 수 있도록 데이터에 라벨(정보 표식)을 입력합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10051-experience"></a>
### 데이터마이너 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-10051` · 시나리오 `career-net-10051-experience` `v001`.
- 원본 위치: `/items/96/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 데이터마이너의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 정보를 분석하는 소프트웨어를 통해 데이터를 다양한 차원과 관점에서 분류하고 요약하고 분석합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-431-experience"></a>
### 데이터베이스관리자 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-431` · 시나리오 `career-net-431-experience` `v001`.
- 원본 위치: `/items/97/data` · 역량: 수리·논리력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 데이터베이스관리자의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 데이터베이스관리자는 컴퓨터를 사용하여 각종 데이터를 체계적으로 수집, 정리, 가공하거나 입력하여 데이터베이스를 구축, 관리, 분석하는 일을 합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1141-experience"></a>
### 도금원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1141` · 시나리오 `career-net-1141-experience` `v001`.
- 원본 위치: `/items/98/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 도금원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 금속제품의 부식과 마모를 방지하고 품질을 향상시키기 위해 제품 또는 부품의 표면에 금속이나 합금의 얇은 막을 입히는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-63-experience"></a>
### 도배원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-63` · 시나리오 `career-net-63-experience` `v001`.
- 원본 위치: `/items/99/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 도배원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 건축 도면이나 현장에서의 측정을 통해 도배에 필요한 도배지, 풀 등을 준비하고 도배 계획을 세웁니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1110-experience"></a>
### 도선사 — 가상 항로를 확인하고 운항 요청 전달

- 직업: `career-net-1110` · 시나리오 `career-net-1110-experience` `v001`.
- 원본 위치: `/items/100/data` · 역량: 공간지각력.
- 장소 제안: 조타실 · `PRM-045 v001` · [PAN-045 v001](../../../images/original/panoramas/PAN-045/v001/prm-045-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 도선사의 업무 표현과 조타실의 선박의 방향과 상태를 확인하며 운항하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 항구에서 출항하거나 귀항하는 선박의 항로를 검토하고 항만에 입출항하는 선박의 종류와 규모를 확인합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 항해 화면 · CND-174 | 항해 화면에서 장애 구간을 피해 경로 선택 | 가상 경로 제약 충족 | 계획·배분 |
| 2 | 조타 장치 · CND-171 | 조타 장치를 가상 유도 경로에 맞춤 | 경로 추적 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태를 인계 | 위치·상태·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 항해 화면 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조타 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-212-experience"></a>
### 도시 및 교통설계전문가 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-212` · 시나리오 `career-net-212-experience` `v001`.
- 원본 위치: `/items/101/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 도시 및 교통설계전문가의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 도시 및 교통설계전문가는 도시설계와 교통체계에 관한 지식을 바탕으로 기존 도시와 특정 단지의 재개발 또는 신도시 건설과 관련하여 도시 및 단지를 계획하고 설계합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10004-experience"></a>
### 도시 재생 전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-10004` · 시나리오 `career-net-10004-experience` `v001`.
- 원본 위치: `/items/102/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 도시 재생 전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 도시 재생 전문가는 쇠퇴하거나 낙후된 도시를 되살리기 위하여 도시 재생 계획을 세우는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-64-experience"></a>
### 도자기제조원 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-64` · 시나리오 `career-net-64-experience` `v001`.
- 원본 위치: `/items/103/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 도자기제조원의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 도자기제조원은 점토 등의 재료 가공을 통해 실용적이고 미적인 다양한 도자기를 제작하고 생산하는 업무를 수행합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1140-experience"></a>
### 도장원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1140` · 시나리오 `career-net-1140-experience` `v001`.
- 원본 위치: `/items/104/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 도장원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작업이 완료되면 도장된 제품에 결함이 없는지 확인합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-163-experience"></a>
### 도축원 및 육류가공원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-163` · 시나리오 `career-net-163-experience` `v001`.
- 원본 위치: `/items/105/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 도축원 및 육류가공원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 도축원 및 육류가공원은 소, 돼지, 닭 등의 가축을 식용으로 사용할 수 있도록 도살하여 부위별로 알맞은 크기로 자르고, 손질 및 가공, 처리하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-365-experience"></a>
### 독서지도사 — 학습자의 이해를 확인하고 설명하기

- 직업: `career-net-365` · 시나리오 `career-net-365-experience` `v001`.
- 원본 위치: `/items/106/data` · 역량: 대인관계능력, 자기성찰능력.
- 장소 제안: 방문 학습 공간 · `PRM-059 v001` · [PAN-059 v001](../../../images/original/panoramas/PAN-059/v001/prm-059-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 독서지도사의 업무 표현과 방문 학습 공간의 가정에서 교사와 학습자가 교재를 함께 보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 초등학생, 중학생, 고등학생을 대상으로 독서교육 프로그램을 개발하고 교육하고 평가합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 사례 풀이의 오류 위치 확인 | 오류 지점 식별 | 관찰·검사 |
| 2 | 필기구 · CND-209 | 필기구 UI로 풀이 설명 순서 구성 | 설명 필수 단계 포함 | 제작·표현 |
| 3 | 업무 책상 · CND-004 | 책상에서 확인 질문과 다음 활동 합의 | 학습자의 이해 확인과 목표 합의 | 대화·응대 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력, 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 필기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10071-experience"></a>
### 동물랭글러 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-10071` · 시나리오 `career-net-10071-experience` `v001`.
- 원본 위치: `/items/107/data` · 역량: 자연친화력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 동물랭글러의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 동물랭글러는 영화나 드라마, 텔레비전 프로그램, 광고 등에 출연하는 동물을 섭외하고 훈련시킵니다.
- 체험의 업무 자료: 가상 개체 ID·관리 요청과 용품 구분.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10046-experience"></a>
### 동물보호보안관 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-10046` · 시나리오 `career-net-10046-experience` `v001`.
- 원본 위치: `/items/108/data` · 역량: 자연친화력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 동물보호보안관의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 동물을 키우는 사람들이 반려동물을 잘 돌볼 수 있도록 돕거나 교육합니다.
- 체험의 업무 자료: 가상 개체 ID·관리 요청과 용품 구분.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-186-experience"></a>
### 동물조련사 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-186` · 시나리오 `career-net-186-experience` `v001`.
- 원본 위치: `/items/109/data` · 역량: 자연친화력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 동물조련사의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 동물조련사는 동물에 대한 지식을 바탕으로 동물원의 동물을 사육하고 관리하거나, 인명구조 및 맹인 안내 등 특수한 목적을 위해 동물을 훈련합니다.
- 체험의 업무 자료: 가상 개체 ID·관리 요청과 용품 구분.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-266-experience"></a>
### 드라마작가 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-266` · 시나리오 `career-net-266-experience` `v001`.
- 원본 위치: `/items/110/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 드라마작가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 드라마의 주제를 선택하고 내용에 따른 역사적 현실이나 사건의 과정 등을 조사, 분석하여 작품의 줄거리를 구상합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10039-experience"></a>
### 드론 전문가 — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-10039` · 시나리오 `career-net-10039-experience` `v001`.
- 원본 위치: `/items/111/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 드론 전문가의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 드론(drone)은 조종사 없이 무선으로 비행 및 조종이 가능한 비행기나 헬리콥터 모양의 무인 항공기를 말하며, 드론 전문가는 세부적으로 드론 개발자와 드론 조종사를 포함합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10022-experience"></a>
### 드론 콘텐츠 전문가 — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-10022` · 시나리오 `career-net-10022-experience` `v001`.
- 원본 위치: `/items/112/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 드론 콘텐츠 전문가의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 다양한 자료를 조사하여 드론 콘텐츠 주제를 찾아내고, 실제로 콘텐츠 제작이 가능한지 내용을 검토합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10107-experience"></a>
### 디스플레이 개발자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10107` · 시나리오 `career-net-10107-experience` `v001`.
- 원본 위치: `/items/113/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 디스플레이 개발자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 디스플레이 개발자는 컴퓨터나 TV 화면으로 사용되는 디스플레이의 제조 설비를 개발하고, 공정상 발생하는 문제점을 해결합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10019-experience"></a>
### 디지털 큐레이터 — 작품의 관람 흐름과 조명 구성

- 직업: `career-net-10019` · 시나리오 `career-net-10019-experience` `v001`.
- 원본 위치: `/items/114/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 전시실 · `PRM-034 v001` · [PAN-034 v001](../../../images/original/panoramas/PAN-034/v001/prm-034-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 디지털 큐레이터의 업무 표현과 전시실의 작품과 전시물을 차례로 살펴보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사용자가 정보를 쉽게 활용할 수 있도록 인터넷에 등록된 다양한 정보를 비교 및 분석하고 정리하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 전시대 · CND-124 | 전시대에 작품 위치를 배치 | 동선·가림 조건 충족 | 조립·배치 |
| 2 | 독립형 액자 거치대 · CND-126 | 액자 거치대에서 시야·설명 순서를 구성 | 필수 작품·설명 관계 충족 | 제작·표현 |
| 3 | 전시 조명 · CND-128 | 전시 조명의 방향을 요청 구간에 맞춤 | 가상 조도·방향 범위 충족 | 측정·조절 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 전시대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 액자 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 전시 조명 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10030-experience"></a>
### 디지털 포렌식 수사관 — 가상 증거의 라벨과 인계 기록 확인

- 직업: `career-net-10030` · 시나리오 `career-net-10030-experience` `v001`.
- 원본 위치: `/items/115/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 증거 분석실 · `PRM-051 v001` · [PAN-051 v001](../../../images/original/panoramas/PAN-051/v001/prm-051-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 디지털 포렌식 수사관의 업무 표현과 증거 분석실의 증거물을 분리하고 관찰하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 디지털 포렌식 수사관은 PC나 노트북, 휴대폰 등 각종 저장 매체 또는 인터넷상에 남아 있는 디지털 정보를 수집하고 분석해 범죄 단서를 찾는 업무를 수행합니다.
- 체험의 업무 자료: 가상 사건·상태 신호와 전달 우선순위.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 밀봉 시료 상자 · CND-192 | 밀봉 상자에서 기록과 시료 ID 대조 | 시료 ID·라벨 일치 | 분류·선별 |
| 2 | 현미경 · CND-039 | 현미경 UI에서 가상 비교 그림의 차이 찾기 | 제공 그림의 차이 지점 일치 | 관찰·검사 |
| 3 | 잠금 보관함 · CND-193 | 잠금 보관함에서 인계 순서 확인 | 인계 필수 항목과 순서 충족 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 밀봉 시료 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 현미경 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 잠금 보관함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10115-experience"></a>
### 디지털 헬스케어 기기 개발자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10115` · 시나리오 `career-net-10115-experience` `v001`.
- 원본 위치: `/items/116/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 디지털 헬스케어 기기 개발자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 생체신호(심박, 혈압, 혈당, 활동량 등)를 수집·분석하는 기술을 개발합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-366-experience"></a>
### 레크리에이션지도자 — 참여 조건에 맞는 공동 활동 준비

- 직업: `career-net-366` · 시나리오 `career-net-366-experience` `v001`.
- 원본 위치: `/items/117/data` · 역량: 창의력.
- 장소 제안: 복지 활동실 · `PRM-016 v001` · [PAN-016 v001](../../../images/original/panoramas/PAN-016/v001/prm-016-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 레크리에이션지도자의 업무 표현과 복지 활동실의 소규모 집단이 공동 활동을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 레크리에이션지도자는 캠프, 사교 모임 등에서 여가 활동을 즐길 수 있도록 다양한 오락 프로그램을 계획하고 진행하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 활동 교구 · CND-066 | 활동 교구에서 참여자 조건에 맞는 물건 선택 | 참여 조건·교구 기능 일치 | 분류·선별 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에서 활동 순서와 역할을 구성 | 필수 역할·단계 누락 없음 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장 물품을 안전한 접근 위치에 배치 | 위치·접근 범위 충족 | 조립·배치 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 활동 교구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10038-experience"></a>
### 로봇 윤리학자 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-10038` · 시나리오 `career-net-10038-experience` `v001`.
- 원본 위치: `/items/118/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 로봇 윤리학자의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 만일 로봇이 잘못해서 피해가 발생했다면 로봇을 만든 사람, 로봇의 주인, 로봇 사용이나 관리를 감독해야 하는 정부 중에서 누구를 어느 정도로 처벌해야 하는지 윤리나 법적인 면에서 따져 보는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-66-experience"></a>
### 로봇연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-66` · 시나리오 `career-net-66-experience` `v001`.
- 원본 위치: `/items/119/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 로봇연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 로봇의 구성 요소를 연구, 개발하고 하나의 단일체로 조립, 제작합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-265-experience"></a>
### 리포터 — 방송 입력을 확인하고 신호에 맞춰 시작

- 직업: `career-net-265` · 시나리오 `career-net-265-experience` `v001`.
- 원본 위치: `/items/120/data` · 역량: 언어능력.
- 장소 제안: 방송 스튜디오 · `PRM-031 v001` · [PAN-031 v001](../../../images/original/panoramas/PAN-031/v001/prm-031-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 리포터의 업무 표현과 방송 스튜디오의 진행자가 음성과 영상을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 리포터는 뉴스나 시사 문제 등을 취재하여 라디오, TV, 케이블, 인터넷 방송 등에 기사 내용을 전달하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 암 · CND-116 | 마이크 암을 표시 위치로 맞춤 | 위치 허용 범위 충족 | 측정·조절 |
| 2 | 소형 오디오 콘솔 · CND-118 | 오디오 콘솔의 가상 레벨을 목표에 조절 | 가상 레벨 구간 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라의 큐 신호에 맞춰 녹화 입력 | 큐 입력 허용 시간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 암 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 오디오 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1259-experience"></a>
### 마술사 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-1259` · 시나리오 `career-net-1259-experience` `v001`.
- 원본 위치: `/items/121/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 마술사의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 마술을 개발하기 위해 기술을 연구하고, 마술 도구를 직접 제작하기도 합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1068-experience"></a>
### 마케팅전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-1068` · 시나리오 `career-net-1068-experience` `v001`.
- 원본 위치: `/items/122/data` · 역량: 수리·논리력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 마케팅전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 마케팅전문가는 마케팅과 소비자 행동 등에 대한 전문 지식을 활용하여 특정 상품의 시장성, 소비자 취향, 잠재 구매 고객 등에 대해 조사하여 효율적인 판매 전략을 계획하고 실행합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-291-experience"></a>
### 만화가 — 표현 재료를 고르고 작은 작품 구성

- 직업: `career-net-291` · 시나리오 `career-net-291-experience` `v001`.
- 원본 위치: `/items/123/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 미술 작업실 · `PRM-028 v001` · [PAN-028 v001](../../../images/original/panoramas/PAN-028/v001/prm-028-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 만화가의 업무 표현과 미술 작업실의 그림을 그리고 작품을 살펴보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 새로운 만화의 소재를 개발하거나 자료를 수집하여 만화의 주제를 결정하고, 그 주제에 맞게 이야기 전개도(콘티)를 구성합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 팔레트 도구 · CND-107 | 팔레트 도구에서 표현 목표에 맞는 재료 선택 | 재료 역할과 목표 일치 | 분류·선별 |
| 2 | 빈 캔버스 · CND-105 | 캔버스에 형태와 구도를 구성 | 필수 요소·구도 조건 충족 | 제작·표현 |
| 3 | 이젤 · CND-104 | 이젤에서 작품을 다른 시점으로 확인 | 지정 확인 항목 점검 완료 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 팔레트 도구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 빈 캔버스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이젤 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-293-experience"></a>
### 메이크업아티스트 — 요청 스타일과 준비 물품 확인

- 직업: `career-net-293` · 시나리오 `career-net-293-experience` `v001`.
- 원본 위치: `/items/124/data` · 역량: 손재능.
- 장소 제안: 미용실 · `PRM-023 v001` · [PAN-023 v001](../../../images/original/panoramas/PAN-023/v001/prm-023-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 메이크업아티스트의 업무 표현과 미용실의 고객의 머리를 손질하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 메이크업 분야에 따라 뷰티메이크업, 웨딩메이크업, 무대메이크업, 광고메이크업, 포토메이크업, 패션메이크업 등으로 분류됩니다.
- 체험의 업무 자료: 고객의 요청 형태·제외 조건과 준비 도구.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 독립형 거울 · CND-086 | 거울 앞 UI에서 원하는 형태와 불편 사항 확인 | 고객 요청 확인 응답 | 대화·응대 |
| 2 | 운반 카트 · CND-016 | 카트에서 요청에 맞는 모형 도구 선택 | 도구 역할·구역 일치 | 분류·선별 |
| 3 | 세발대 · CND-087 | 세발대에서 가상 준비 단계를 순서대로 선택 | 교육용 준비 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 독립형 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세발대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1134-experience"></a>
### 메카트로닉스공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1134` · 시나리오 `career-net-1134-experience` `v001`.
- 원본 위치: `/items/125/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 메카트로닉스공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 생산 현장을 조사하고 각종 자료 수집과 공정 분석을 거쳐 공장의 자동화 계획을 수립하고 지도합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10101-experience"></a>
### 메타버스 크리에이터 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-10101` · 시나리오 `career-net-10101-experience` `v001`.
- 원본 위치: `/items/126/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 메타버스 크리에이터의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 메타버스 플랫폼에서 제공하는 제작 툴을 사용하여 단일 아이템을 주로 제작하고 판매합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-294-experience"></a>
### 모델 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-294` · 시나리오 `career-net-294-experience` `v001`.
- 원본 위치: `/items/127/data` · 역량: 창의력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 모델의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 특정 상품의 사진 또는 영상 매체를 이용한 광고를 제작하기 위하여 언어, 표정, 자세를 취하거나 연출합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10076-experience"></a>
### 모바일앱개발자 — 가상 기능의 요구와 테스트 결과 맞추기

- 직업: `career-net-10076` · 시나리오 `career-net-10076-experience` `v001`.
- 원본 위치: `/items/128/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 모바일앱개발자의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 애플리케이션이 작동하는데 필요한 구글 안드로이드, 애플 iOS, 윈도우 등 모바일 운영체제(OS: Operation System)별로 기술 변경 사항 등에 대해 확인하고 고객의 요구 사항대로 앱을 개발하기 위한 기술 검토와 업무 분석을 합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 사용자 요구와 다른 실행 결과 찾기 | 명시된 요구·결과 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI로 가상 기능 블록 순서·조건 수정 | 필수 기능 블록과 제약 충족 | 제작·표현 |
| 3 | 마우스 · CND-018 | 마우스로 테스트 단서와 수정 대안을 연결해 재실행 | 가상 테스트의 입력·기대 결과 일치 | 진단·해결 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 마우스 / common / AST-007 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 선택 장면의 기존 필수 후보 밖 추가 제안: CND-018. 기존 후보 목록은 자동 수정하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-68-experience"></a>
### 목공 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-68` · 시나리오 `career-net-68-experience` `v001`.
- 원본 위치: `/items/129/data` · 역량: 손재능.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 목공의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 다듬은 목재를 목조주택의 지붕, 전통 목조건축물의 복원, 수리 등의 목적에 따라 조립합니다.
- 체험의 업무 자료: 가구 부품·규격과 완성 상태.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10069-experience"></a>
### 목소리코치 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10069` · 시나리오 `career-net-10069-experience` `v001`.
- 원본 위치: `/items/130/data` · 역량: 대인관계능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 목소리코치의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기업 대표, 정치인 등 대중을 상대로 연설이나 발표를 자주 해야 하는 사람이 자신감 있게 말할 수 있도록 지도합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-69-experience"></a>
### 목재가공관련조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-69` · 시나리오 `career-net-69-experience` `v001`.
- 원본 위치: `/items/131/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 목재가공관련조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작업명세서를 확인하여 생산할 목제품의 종류를 파악하고, 작업에 필요한 재료와 장비를 준비합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-296-experience"></a>
### 무대감독 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-296` · 시나리오 `career-net-296-experience` `v001`.
- 원본 위치: `/items/132/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 무대감독의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 무대감독은 무대 연출에 필요한 촬영, 무대장치, 편집 등의 기술적인 업무를 계획하고 조정합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-476-experience"></a>
### 무선주파수(RF)엔지니어 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-476` · 시나리오 `career-net-476-experience` `v001`.
- 원본 위치: `/items/133/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 무선주파수(RF)엔지니어의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국내외 시장을 조사하고 경쟁하는 기업의 제품 및 무선통신 장비 관련 기술 변화 등에 대해 분석하여, 새로운 기능과 성능을 갖춘 무선통신 장비를 기획하고 개발합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-298-experience"></a>
### 무용가 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-298` · 시나리오 `career-net-298-experience` `v001`.
- 원본 위치: `/items/134/data` · 역량: 신체·운동능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 무용가의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 공연이 결정되면 연습 스케줄을 계획하고 자신이 맡은 배역과 전체적인 공연 콘셉트 및 분위기를 파악합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1118-experience"></a>
### 무인경비시스템종사원 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-1118` · 시나리오 `career-net-1118-experience` `v001`.
- 원본 위치: `/items/135/data` · 역량: 신체·운동능력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 무인경비시스템종사원의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 무인경비시스템종사원은 가정이나 사업체에 설치되어 있는 보안 기기에 이상이 감지되면 현장에 출동하여 이상 원인을 확인 및 처리하여 상황을 정리하는 일을 담당합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10049-experience"></a>
### 무인항공기시스템개발자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10049` · 시나리오 `career-net-10049-experience` `v001`.
- 원본 위치: `/items/136/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 무인항공기시스템개발자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 무인항공기시스템개발자는 무인항공기 시스템의 설계, 제조, 작동 및 유지에 필요한 활동을 합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10070-experience"></a>
### 무인항공촬영감독 — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-10070` · 시나리오 `career-net-10070-experience` `v001`.
- 원본 위치: `/items/137/data` · 역량: 예술시각능력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 무인항공촬영감독의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 무인항공촬영감독은 소형카메라가 장착된 무인 조종 비행체인 헬리 캠을 조정하여 영화, 드라마, 광고의 스틸 영상이나 동영상을 촬영하는 전 과정을 기획하고 실행합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10023-experience"></a>
### 문화 콘텐츠 전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-10023` · 시나리오 `career-net-10023-experience` `v001`.
- 원본 위치: `/items/138/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 문화 콘텐츠 전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 문화 콘텐츠로 만들어 낼 주제를 찾아내고 다양한 문화 자료를 조사하여 콘텐츠 제작이 가능한지 검토합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10042-experience"></a>
### 문화여가사 — 참여 조건에 맞는 공동 활동 준비

- 직업: `career-net-10042` · 시나리오 `career-net-10042-experience` `v001`.
- 원본 위치: `/items/139/data` · 역량: 자기성찰능력.
- 장소 제안: 복지 활동실 · `PRM-016 v001` · [PAN-016 v001](../../../images/original/panoramas/PAN-016/v001/prm-016-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 문화여가사의 업무 표현과 복지 활동실의 소규모 집단이 공동 활동을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 개인이나 가족, 동호회 등을 대상으로 여가 프로그램에 관한 계획을 세워 줍니다.
- 체험의 업무 자료: 이용자 요청·물품 구역과 점검 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 활동 교구 · CND-066 | 활동 교구에서 참여자 조건에 맞는 물건 선택 | 참여 조건·교구 기능 일치 | 분류·선별 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에서 활동 순서와 역할을 구성 | 필수 역할·단계 누락 없음 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장 물품을 안전한 접근 위치에 배치 | 위치·접근 범위 충족 | 조립·배치 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 활동 교구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-299-experience"></a>
### 문화재보존원 — 작품의 관람 흐름과 조명 구성

- 직업: `career-net-299` · 시나리오 `career-net-299-experience` `v001`.
- 원본 위치: `/items/140/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 전시실 · `PRM-034 v001` · [PAN-034 v001](../../../images/original/panoramas/PAN-034/v001/prm-034-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 문화재보존원의 업무 표현과 전시실의 작품과 전시물을 차례로 살펴보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국가유산수리기술자, 국가유산수리기능자, 보존과학기술자 및 기능자 등으로 구분되며 국가유산수리기술자는 각 분야에 대한 기술을 자문하고, 각종 공사와 국가유산수리기능자를 관리 및 감독합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 전시대 · CND-124 | 전시대에 작품 위치를 배치 | 동선·가림 조건 충족 | 조립·배치 |
| 2 | 독립형 액자 거치대 · CND-126 | 액자 거치대에서 시야·설명 순서를 구성 | 필수 작품·설명 관계 충족 | 제작·표현 |
| 3 | 전시 조명 · CND-128 | 전시 조명의 방향을 요청 구간에 맞춤 | 가상 조도·방향 범위 충족 | 측정·조절 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 전시대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 액자 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 전시 조명 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-215-experience"></a>
### 물류관리사 — 주문 화물을 골라 적재 순서 계획

- 직업: `career-net-215` · 시나리오 `career-net-215-experience` `v001`.
- 원본 위치: `/items/141/data` · 역량: 수리·논리력.
- 장소 제안: 물류 창고 · `PRM-053 v001` · [PAN-053 v001](../../../images/original/panoramas/PAN-053/v001/prm-053-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 물류관리사의 업무 표현과 물류 창고의 물품을 저장하고 꺼내는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 물류의 이동, 보관, 비용 등을 분석하고 분석 결과를 바탕으로 기업의 물류관리와 물류 지원 시스템을 가장 합리적이고 경제적으로 실행할 방법을 설계하고 실행합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 상자의 목적지·규격을 요청과 대조 | 목적지·규격 일치 | 분류·선별 |
| 2 | 팔레트 · CND-200 | 팔레트 모형에 화물을 표시 구획대로 배치 | 가상 적재 제약 충족 | 조립·배치 |
| 3 | 수동 운반차 · CND-201 | 수동 운반차의 가상 이동 순서를 계획 | 막힌 구간·중복 이동 제약 충족 | 계획·배분 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 팔레트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수동 운반차 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-369-experience"></a>
### 물리치료사 — 가상 동작을 비교하고 연습 도구 준비

- 직업: `career-net-369` · 시나리오 `career-net-369-experience` `v001`.
- 원본 위치: `/items/142/data` · 역량: 대인관계능력.
- 장소 제안: 운동 지도실 · `PRM-048 v001` · [PAN-048 v001](../../../images/original/panoramas/PAN-048/v001/prm-048-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 물리치료사의 업무 표현과 운동 지도실의 지도자와 이용자가 자세·동작을 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 신체적 손상이나 움직임을 더 원활하게 하기 위해 치료적 운동, 도수 치료 등의 방법을 사용하기도 하며, 보조 및 보호 기구와 장비를 사용하여 치료하며 환자 교육 등을 실시합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 자세 확인용 독립 거울 · CND-186 | 거울에서 사례 동작의 차이 확인 | 사례 차이 지점 식별 | 관찰·검사 |
| 2 | 낮은 스텝 · CND-184 | 낮은 스텝을 가상 훈련 위치에 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 소형 아령 · CND-185 | 아령 모형의 선택 값을 사례 목표에 맞춤 | 교육용 목표 구간 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 자세 확인용 독립 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 스텝 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 아령 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-8-experience"></a>
### 물리학연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-8` · 시나리오 `career-net-8-experience` `v001`.
- 원본 위치: `/items/143/data` · 역량: 수리·논리력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 물리학연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고형 물질의 구조와 특성을 조사하기 위해 온도, 압력 등의 환경조건을 변화시켜 실험하고 반응을 연구합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1122-experience"></a>
### 미용사 — 요청 스타일과 준비 물품 확인

- 직업: `career-net-1122` · 시나리오 `career-net-1122-experience` `v001`.
- 원본 위치: `/items/144/data` · 역량: 손재능.
- 장소 제안: 미용실 · `PRM-023 v001` · [PAN-023 v001](../../../images/original/panoramas/PAN-023/v001/prm-023-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 미용사의 업무 표현과 미용실의 고객의 머리를 손질하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 이외에도 매니큐어, 얼굴 관리, 화장, 머리 장식 등 미용에 관한 다양한 서비스를 제공하기도 합니다.
- 체험의 업무 자료: 고객의 요청 형태·제외 조건과 준비 도구.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 독립형 거울 · CND-086 | 거울 앞 UI에서 원하는 형태와 불편 사항 확인 | 고객 요청 확인 응답 | 대화·응대 |
| 2 | 운반 카트 · CND-016 | 카트에서 요청에 맞는 모형 도구 선택 | 도구 역할·구역 일치 | 분류·선별 |
| 3 | 세발대 · CND-087 | 세발대에서 가상 준비 단계를 순서대로 선택 | 교육용 준비 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 독립형 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세발대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-70-experience"></a>
### 미장원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-70` · 시나리오 `career-net-70-experience` `v001`.
- 원본 위치: `/items/145/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 미장원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 시멘트, 모르타르, 회반죽 등을 혼합하고, 단계별로 미장재를 시공 면에 바르며, 작업의 결함 여부를 확인하고 수정합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-155-experience"></a>
### 바닥재시공원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-155` · 시나리오 `career-net-155-experience` `v001`.
- 원본 위치: `/items/146/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 바닥재시공원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 바닥재시공원은 각종 타일이나 카펫 등을 설치하여 건물의 내외벽, 바닥, 천장 등을 마무리 또는 장식하는 일을 합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-180-experience"></a>
### 바리스타 — 주문에 맞게 조리 준비 순서 맞추기

- 직업: `career-net-180` · 시나리오 `career-net-180-experience` `v001`.
- 원본 위치: `/items/147/data` · 역량: 손재능.
- 장소 제안: 주방 · `PRM-024 v001` · [PAN-024 v001](../../../images/original/panoramas/PAN-024/v001/prm-024-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 바리스타의 업무 표현과 주방의 식재료 준비에서 조리와 담기까지 이어지는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 좋은 원두를 감별한 후 구입하고, 저장 및 재고 관리를 철저하게 합니다.
- 체험의 업무 자료: 가상 주문·재료 구분과 준비 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 냉장고 · CND-090 | 냉장고에서 주문과 재료 라벨 대조 | 재료·주문·구역 구분 일치 | 분류·선별 |
| 2 | 조리대 · CND-088 | 조리대에서 가상 조리 단계를 순서대로 배치 | 가상 레시피 단계 일치 | 순서·절차 |
| 3 | 가열 기구 · CND-089 | 가열 기구를 교육용 표시 범위에 조절 | 훈련용 눈금 범위 충족 | 측정·조절 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 냉장고 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조리대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 가열 기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-214-experience"></a>
### 바이어(구매인) — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-214` · 시나리오 `career-net-214-experience` `v001`.
- 원본 위치: `/items/148/data` · 역량: 수리·논리력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 바이어(구매인)의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 바이어는 물류와 유통에 대한 지식을 바탕으로 도소매사업체에서 재판매를 하기 위해 공급자로부터 상품을 구매하거나 구매한 상품을 판매합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-370-experience"></a>
### 바텐더 — 주문에 맞게 조리 준비 순서 맞추기

- 직업: `career-net-370` · 시나리오 `career-net-370-experience` `v001`.
- 원본 위치: `/items/149/data` · 역량: 대인관계능력.
- 장소 제안: 주방 · `PRM-024 v001` · [PAN-024 v001](../../../images/original/panoramas/PAN-024/v001/prm-024-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 바텐더의 업무 표현과 주방의 식재료 준비에서 조리와 담기까지 이어지는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 칵테일에 들어갈 재료를 준비하고, 매일 판매된 음료와 술을 기록하고 정리합니다.
- 체험의 업무 자료: 가상 주문·재료 구분과 준비 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 냉장고 · CND-090 | 냉장고에서 주문과 재료 라벨 대조 | 재료·주문·구역 구분 일치 | 분류·선별 |
| 2 | 조리대 · CND-088 | 조리대에서 가상 조리 단계를 순서대로 배치 | 가상 레시피 단계 일치 | 순서·절차 |
| 3 | 가열 기구 · CND-089 | 가열 기구를 교육용 표시 범위에 조절 | 훈련용 눈금 범위 충족 | 측정·조절 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 냉장고 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조리대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 가열 기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-157-experience"></a>
### 반도체공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-157` · 시나리오 `career-net-157-experience` `v001`.
- 원본 위치: `/items/150/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 반도체공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 반도체 제조에 필요한 설비와 장비를 시운전하여 조작 및 운영 방법을 규정하여 작업자에게 지시하고, 불량제품의 원인을 분석하고 그 대책을 수립합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10018-experience"></a>
### 반려동물 훈련·상담사 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-10018` · 시나리오 `career-net-10018-experience` `v001`.
- 원본 위치: `/items/151/data` · 역량: 대인관계능력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 반려동물 훈련·상담사의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 반려동물의 문제 행동을 바로잡기 위한 프로그램을 개발하고 훈련 일정을 계획하고 관리합니다. 그리고 보호자에게 반려동물의 행동을 바로잡는 방법을 알려주고, 보호자의 행동에서도 바로잡아야 하는 부분이 있다면 이를 알려주고 교육합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-319-experience"></a>
### 반려동물미용사 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-319` · 시나리오 `career-net-319-experience` `v001`.
- 원본 위치: `/items/152/data` · 역량: 자연친화력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 반려동물미용사의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객과 상담을 통해 애완동물 털의 커트 모양 및 장식 모양 등을 결정하고, 애완동물의 털 상태를 검사합니다.
- 체험의 업무 자료: 가상 개체 ID·관리 요청과 용품 구분.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1433-experience"></a>
### 발명가 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1433` · 시나리오 `career-net-1433-experience` `v001`.
- 원본 위치: `/items/153/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 발명가의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 발명가는 지금까지 없던 기술이나 물건을 새로 생각하여 만들어 내는 일을 전문적으로 하는 사람으로, 새로운 아이디어를 생각해 내고 시제품을 만듭니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1144-experience"></a>
### 발전장치조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1144` · 시나리오 `career-net-1144-experience` `v001`.
- 원본 위치: `/items/154/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 발전장치조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 각종 지시계기와 기록계를 점검하고 확인하며 현황을 기록합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1113-experience"></a>
### 방문판매원 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-1113` · 시나리오 `career-net-1113-experience` `v001`.
- 원본 위치: `/items/155/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 방문판매원의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 방문판매원은 가정이나 사업체를 직접 찾아다니면서 고객에게 상품이나 서비스를 홍보하고 판매하는 일을 담당합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10-experience"></a>
### 방사선사 — 가상 작업 구역을 확인하고 도구 준비

- 직업: `career-net-10` · 시나리오 `career-net-10-experience` `v001`.
- 원본 위치: `/items/156/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 처치실 · `PRM-009 v001` · [PAN-009 v001](../../../images/original/panoramas/PAN-009/v001/prm-009-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 방사선사의 업무 표현과 처치실의 의료진이 준비한 기구로 처치하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 방사선 촬영 결과를 정리, 분석하여 보고서를 작성하고, 의사에게 전달하며, 치료 기록을 관리합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 기구 트레이에서 요청 라벨과 맞는 모형 도구 선택 | 도구 라벨·구역 구분 일치 | 분류·선별 |
| 2 | 작업등 · CND-043 | 작업등을 표시된 가상 관찰 영역에 맞춤 | 표시 영역과 조명 방향 일치 | 측정·조절 |
| 3 | 운반 카트 · CND-016 | 카트의 물품을 준비 순서대로 정돈 | 준비 순서·누락 없음 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 작업등 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1010-experience"></a>
### 방사성폐기물관리원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1010` · 시나리오 `career-net-1010-experience` `v001`.
- 원본 위치: `/items/157/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 방사성폐기물관리원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 방사성폐기물관리원은 원자력시설 혹은 방사성물질을 다루는 작업장과 실험실에서 나오는 폐기물 처리 설비 및 용기를 관리하고, 작업원을 감독합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-301-experience"></a>
### 방송연출가 — 방송 입력을 확인하고 신호에 맞춰 시작

- 직업: `career-net-301` · 시나리오 `career-net-301-experience` `v001`.
- 원본 위치: `/items/158/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 방송 스튜디오 · `PRM-031 v001` · [PAN-031 v001](../../../images/original/panoramas/PAN-031/v001/prm-031-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 방송연출가의 업무 표현과 방송 스튜디오의 진행자가 음성과 영상을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 시나리오작가를 선정하여 제작될 프로그램의 계획을 설명하고 완성된 대본을 평가합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 암 · CND-116 | 마이크 암을 표시 위치로 맞춤 | 위치 허용 범위 충족 | 측정·조절 |
| 2 | 소형 오디오 콘솔 · CND-118 | 오디오 콘솔의 가상 레벨을 목표에 조절 | 가상 레벨 구간 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라의 큐 신호에 맞춰 녹화 입력 | 큐 입력 허용 시간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 암 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 오디오 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1147-experience"></a>
### 방송장비(H/W)설치 및 수리원 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-1147` · 시나리오 `career-net-1147-experience` `v001`.
- 원본 위치: `/items/159/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 방송장비(H/W)설치 및 수리원의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 방송 관련 장비의 작동 불량 부위를 확인하고 각종 기구를 사용하여 고장원인을 조사합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-72-experience"></a>
### 방수원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-72` · 시나리오 `career-net-72-experience` `v001`.
- 원본 위치: `/items/160/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 방수원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 방수 작업을 할 부위를 확인하고, 방수제와 시멘트 모르타르의 혼합물이나 액체 상태의 방수재 등을 시공 면에 바릅니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-74-experience"></a>
### 배관원 — 배관 모형을 연결하고 상태 확인

- 직업: `career-net-74` · 시나리오 `career-net-74-experience` `v001`.
- 원본 위치: `/items/161/data` · 역량: 손재능.
- 장소 제안: 설비 작업 구역 · `PRM-037 v001` · [PAN-037 v001](../../../images/original/panoramas/PAN-037/v001/prm-037-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 배관원의 업무 표현과 설비 작업 구역의 배관과 설비를 설치·점검하는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 배관원은 건축물에 물, 가스, 증기, 기타 물질을 운반하는 배관시설을 제작, 설치하고, 배관시설의 유지보수와 관련된 업무를 수행합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 상자 · CND-137 | 부품 상자에서 연결 규격에 맞는 부품 선택 | 규격·용도 일치 | 분류·선별 |
| 2 | 노출 배관 모형 · CND-135 | 노출 배관 모형의 연결 방향 맞춤 | 위치·방향·연결점 일치 | 조립·배치 |
| 3 | 제어함 · CND-138 | 제어함에서 가상 상태표와 다른 항목 확인 | 가상 오류 항목 식별 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노출 배관 모형 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10108-experience"></a>
### 배터리 기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10108` · 시나리오 `career-net-10108-experience` `v001`.
- 원본 위치: `/items/162/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 배터리 기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 배터리 기술자는 2차 전지의 기본 단위가 되는 배터리 셀을 비롯하여 각종 배터리 부품을 설계하고, 제품 생산 과정을 관리합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-304-experience"></a>
### 백댄서(백업댄서) — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-304` · 시나리오 `career-net-304-experience` `v001`.
- 원본 위치: `/items/163/data` · 역량: 신체·운동능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 백댄서(백업댄서)의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 백댄서는 가수의 노래와 음악에 어울리는 춤을 개발하고 연습하며, 함께 공연에 참가하여 가수의 무대를 보조하는 일을 합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-372-experience"></a>
### 버스운전기사 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-372` · 시나리오 `career-net-372-experience` `v001`.
- 원본 위치: `/items/164/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 버스운전기사의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 배차 계획에 따라 버스 차량을 배차받고 점검표에 따라 연료, 타이어 등 차량을 점검하고 이상이 발견되면 수리를 맡깁니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-267-experience"></a>
### 번역가 — 출장 요청과 자료를 확인해 전달

- 직업: `career-net-267` · 시나리오 `career-net-267-experience` `v001`.
- 원본 위치: `/items/165/data` · 역량: 언어능력, 창의력.
- 장소 제안: 출장 업무 공간 · `PRM-068 v001` · [PAN-068 v001](../../../images/original/panoramas/PAN-068/v001/prm-068-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 번역가의 업무 표현과 출장 업무 공간의 이동 중 임시 자리에서 업무를 처리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전문 서적의 경우 해당 분야 전문가나 번역 업체를 통해 전문 용어를 감수받아 잘못 번역된 부분이 없는지 확인합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 휴대 전화 · CND-222 | 휴대전화에서 상대 요청과 누락 정보 확인 | 요청·언어·목적 확인 | 대화·응대 |
| 2 | 노트북 · CND-012 | 노트북에서 전달 자료와 원문 차이 확인 | 지정 오류·누락 식별 | 관찰·검사 |
| 3 | 문서 파우치 · CND-223 | 파우치에서 목적별 문서 분류 | 목적별 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 휴대 전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 문서 파우치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10064-experience"></a>
### 범죄과학수사관 — 가상 증거의 라벨과 인계 기록 확인

- 직업: `career-net-10064` · 시나리오 `career-net-10064-experience` `v001`.
- 원본 위치: `/items/166/data` · 역량: 수리·논리력.
- 장소 제안: 증거 분석실 · `PRM-051 v001` · [PAN-051 v001](../../../images/original/panoramas/PAN-051/v001/prm-051-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 범죄과학수사관의 업무 표현과 증거 분석실의 증거물을 분리하고 관찰하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 범죄 현장의 증거 수집 및 분석을 통해 범죄 현장을 재구성하고 조사 및 분석 기법 또는 분석 결과에 대해 법원에서 증언을 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 밀봉 시료 상자 · CND-192 | 밀봉 상자에서 기록과 시료 ID 대조 | 시료 ID·라벨 일치 | 분류·선별 |
| 2 | 현미경 · CND-039 | 현미경 UI에서 가상 비교 그림의 차이 찾기 | 제공 그림의 차이 지점 일치 | 관찰·검사 |
| 3 | 잠금 보관함 · CND-193 | 잠금 보관함에서 인계 순서 확인 | 인계 필수 항목과 순서 충족 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 밀봉 시료 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 현미경 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 잠금 보관함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10074-experience"></a>
### 범죄심리분석관(프로파일러) — 가상 사건의 단서와 사실 기록 정리

- 직업: `career-net-10074` · 시나리오 `career-net-10074-experience` `v001`.
- 원본 위치: `/items/167/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 수사실 · `PRM-050 v001` · [PAN-050 v001](../../../images/original/panoramas/PAN-050/v001/prm-050-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 범죄심리분석관(프로파일러)의 업무 표현과 수사실의 기록과 단서를 비교하는 업무 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 범죄심리분석관(프로파일러)은 증거가 충분히 확보되지 않아 일반수사 기법 조사로는 한계가 있는 이상범죄, 연쇄살인 등의 범죄 사건을 담당, 해결하는 역할을 수행합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 트레이 · CND-049 | 서류 트레이에서 사실·진술·미확인 자료 구분 | 자료 종류 분류 일치 | 분류·선별 |
| 2 | 관계 보드 · CND-191 | 관계 보드에서 단서와 가설 연결 | 제공 단서에 맞는 가설 관계 | 진단·해결 |
| 3 | 모니터 · CND-005 | 모니터에서 근거 없는 기록을 찾아 보류 | 근거 없는 확정 기록을 보류 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관계 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-252-experience"></a>
### 법률사무원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-252` · 시나리오 `career-net-252-experience` `v001`.
- 원본 위치: `/items/168/data` · 역량: 대인관계능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 법률사무원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 법원이나 검찰에서 서류 접수와 사건 분류 등 사법 관련 행정 업무가 원활하게 이루어지도록 돕습니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-373-experience"></a>
### 법무사 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-373` · 시나리오 `career-net-373-experience` `v001`.
- 원본 위치: `/items/169/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 법무사의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 개인, 개인사업자, 법인 등의 법적 분쟁에 대해 자문하고 상담을 합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1432-experience"></a>
### 베타테스터 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-1432` · 시나리오 `career-net-1432-experience` `v001`.
- 원본 위치: `/items/170/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 베타테스터의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 베타테스터는 컴퓨터업체에서 소프트웨어나 하드웨어 제품을 판매하기 전에 제품의 결함 여부를 검사하는 사람으로, 프로그램의 오류를 파악하고 해결 방안을 제시하여 상품성을 높이는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-374-experience"></a>
### 변리사 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-374` · 시나리오 `career-net-374-experience` `v001`.
- 원본 위치: `/items/171/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 변리사의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 특허권을 얻고자 하는 대상의 설계도, 제품 등을 조사 및 검토하고 유사 제품의 특허권을 조사합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-375-experience"></a>
### 변호사 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-375` · 시나리오 `career-net-375-experience` `v001`.
- 원본 위치: `/items/172/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 변호사의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 형사사건에서는 피고인 또는 피의자들을 만나 증거 등을 확인하고, 구속 취소, 보석 등 법원에서 진행하는 업무를 수행합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1257-experience"></a>
### 병원코디네이터 — 가상 방문 자료를 접수하고 기록 확인

- 직업: `career-net-1257` · 시나리오 `career-net-1257-experience` `v001`.
- 원본 위치: `/items/173/data` · 역량: 대인관계능력.
- 장소 제안: 의료 접수실 · `PRM-011 v001` · [PAN-011 v001](../../../images/original/panoramas/PAN-011/v001/prm-011-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 병원코디네이터의 업무 표현과 의료 접수실의 진료 방문객의 접수와 대기를 안내하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 병원코디네이터는 양질의 의료서비스를 제공하기 위해 환자 상담과 지속적 관리, 직원 친절 서비스 교육, 병원 이미지 개선을 위한 일을 합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 번호표 발급기 · CND-024 | 순번 기기에서 방문 유형 확인 | 방문 유형·순서 일치 | 순서·절차 |
| 2 | 서류 트레이 · CND-049 | 서류 트레이에서 필수 문서 분류 | 필수 문서 누락 없음 | 분류·선별 |
| 3 | 모니터 · CND-005 | 화면에서 방문 기록과 입력 내용을 대조 | 입력 ID와 원문 항목 일치 | 관찰·검사 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 번호표 발급기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-256-experience"></a>
### 보건의료정보관리사 — 가상 방문 자료를 접수하고 기록 확인

- 직업: `career-net-256` · 시나리오 `career-net-256-experience` `v001`.
- 원본 위치: `/items/174/data` · 역량: 대인관계능력.
- 장소 제안: 의료 접수실 · `PRM-011 v001` · [PAN-011 v001](../../../images/original/panoramas/PAN-011/v001/prm-011-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 보건의료정보관리사의 업무 표현과 의료 접수실의 진료 방문객의 접수와 대기를 안내하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 의료기관에서 질병과 수술 분류, 진료기록의 분석, 진료 통계, 암 등록, 전사 등 각종 의무에 관한 기록 및 정보를 유지하고 관리하며 확인하는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 번호표 발급기 · CND-024 | 순번 기기에서 방문 유형 확인 | 방문 유형·순서 일치 | 순서·절차 |
| 2 | 서류 트레이 · CND-049 | 서류 트레이에서 필수 문서 분류 | 필수 문서 누락 없음 | 분류·선별 |
| 3 | 모니터 · CND-005 | 화면에서 방문 기록과 입력 내용을 대조 | 입력 ID와 원문 항목 일치 | 관찰·검사 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 번호표 발급기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-76-experience"></a>
### 보석감정사 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-76` · 시나리오 `career-net-76-experience` `v001`.
- 원본 위치: `/items/175/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 보석감정사의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 보석의 가치에 영향을 미치는 특성과 결함을 찾아내기 위해 보석의 내부와 외부 구조를 검사합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-305-experience"></a>
### 보석디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-305` · 시나리오 `career-net-305-experience` `v001`.
- 원본 위치: `/items/176/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 보석디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 새로운 제품에 대한 아이디어를 얻기 위해 국내외 시장조사를 실시합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-376-experience"></a>
### 보육교사 — 학습자의 오류를 확인하고 활동 준비

- 직업: `career-net-376` · 시나리오 `career-net-376-experience` `v001`.
- 원본 위치: `/items/177/data` · 역량: 대인관계능력, 자기성찰능력.
- 장소 제안: 교실 · `PRM-012 v001` · [PAN-012 v001](../../../images/original/panoramas/PAN-012/v001/prm-012-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 보육교사의 업무 표현과 교실의 학생들이 교사를 보며 수업하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 유아를 관찰한 내용과 지도 경과를 보육 일지에 기록하고, 아이들의 보육 상태를 평가하여 부모들과 아동의 성장에 관련된 문제를 상담합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 잘못 이해한 풀이 지점 확인 | 사례의 오류 지점 일치 | 관찰·검사 |
| 2 | 독립형 칠판 · CND-052 | 칠판에서 설명 순서를 구성 | 핵심 개념·설명 단계 포함 | 제작·표현 |
| 3 | 사물함 · CND-054 | 사물함에서 학습 조건에 맞는 교구 선택 | 학습 조건과 교구 기능 일치 | 분류·선별 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력, 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 칠판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 사물함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-978-experience"></a>
### 보일러공 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-978` · 시나리오 `career-net-978-experience` `v001`.
- 원본 위치: `/items/178/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 보일러공의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 보일러공은 산업용 및 건물 난방용 보일러를 설치하고, 고장 난 보일러를 수리하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-217-experience"></a>
### 보험계리인 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-217` · 시나리오 `career-net-217-experience` `v001`.
- 원본 위치: `/items/179/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 보험계리인의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 보험 및 연금 계획을 설계하거나 검토하고 시장 상황을 고려한 합리적인 요금의 정도 비율 산정, 보험금 평가 및 산정 등의 업무를 수행합니다.
- 체험의 업무 자료: 가상 요청 조건·수량·기간과 설명 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-219-experience"></a>
### 부동산중개인 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-219` · 시나리오 `career-net-219-experience` `v001`.
- 원본 위치: `/items/180/data` · 역량: 대인관계능력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 부동산중개인의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 부동산 이용과 개발에 대한 상담, 분양 대행, 경매 대상 부동산에 대한 권리분석 등 컨설팅 업무를 담당하기도 합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-927-experience"></a>
### 북디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-927` · 시나리오 `career-net-927-experience` `v001`.
- 원본 위치: `/items/181/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 북디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국내외의 책 디자인 유행이나 흐름을 알기 위한 시장조사를 하고 북디자인의 방향을 정하거나 소비자의 욕구에 맞는 디자인을 찾아 기획합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-306-experience"></a>
### 분장사 — 요청 스타일과 준비 물품 확인

- 직업: `career-net-306` · 시나리오 `career-net-306-experience` `v001`.
- 원본 위치: `/items/182/data` · 역량: 손재능.
- 장소 제안: 미용실 · `PRM-023 v001` · [PAN-023 v001](../../../images/original/panoramas/PAN-023/v001/prm-023-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 분장사의 업무 표현과 미용실의 고객의 머리를 손질하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 분장사는 영화, 연극, TV 드라마의 작품 내용과 인물의 성격에 어울리도록 배우를 분장하는 일을 담당합니다.
- 체험의 업무 자료: 고객의 요청 형태·제외 조건과 준비 도구.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 독립형 거울 · CND-086 | 거울 앞 UI에서 원하는 형태와 불편 사항 확인 | 고객 요청 확인 응답 | 대화·응대 |
| 2 | 운반 카트 · CND-016 | 카트에서 요청에 맞는 모형 도구 선택 | 도구 역할·구역 일치 | 분류·선별 |
| 3 | 세발대 · CND-087 | 세발대에서 가상 준비 단계를 순서대로 선택 | 교육용 준비 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 독립형 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세발대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10029-experience"></a>
### 블록체인 전문가 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-10029` · 시나리오 `career-net-10029-experience` `v001`.
- 원본 위치: `/items/183/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 블록체인 전문가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 블록체인 전문가는 누구나 열람할 수 있는 장부에 거래 내용을 공개적으로 기록하고 여러 대의 컴퓨터에 복제, 저장하는 기술인 블록체인 기술을 활용할 수 있는 분야와 산업을 찾고 이를 적용하기 위한 소프트웨어를 설계하고 개발합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10067-experience"></a>
### 비디오게임디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-10067` · 시나리오 `career-net-10067-experience` `v001`.
- 원본 위치: `/items/184/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 비디오게임디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 계획된 제작 일정에 맞추어 프로토타입을 개발하고 재미 요소나 구현 가능성을 검증한 후 게임의 다양한 콘텐츠를 균형 있게 경험할 수 있도록 조정합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-309-experience"></a>
### 비디오저널리스트(VJ) — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-309` · 시나리오 `career-net-309-experience` `v001`.
- 원본 위치: `/items/185/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 비디오저널리스트(VJ)의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 비디오저널리스트는 비디오카메라를 가지고 방송물 등을 직접 기획, 취재, 촬영, 편집하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-81-experience"></a>
### 비파괴검사원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-81` · 시나리오 `career-net-81-experience` `v001`.
- 원본 위치: `/items/186/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 비파괴검사원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 검사제품의 특성을 고려하여 검사 방법, 검사 일정 등 검사 계획을 수립하고, 수립된 계획에 따라 장비를 준비하고 설치합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-418-experience"></a>
### 비행기승무원 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-418` · 시나리오 `career-net-418-experience` `v001`.
- 원본 위치: `/items/187/data` · 역량: 대인관계능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 비행기승무원의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기내의 비상장비 및 시설의 이상 유무 확인, 기내 서비스를 위한 용품의 수량 및 탑재 확인, 기내의 청결 상태를 포함한 객실 서비스를 위한 사항을 확인하고 준비합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-150-experience"></a>
### 비행기조종사 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-150` · 시나리오 `career-net-150-experience` `v001`.
- 원본 위치: `/items/188/data` · 역량: 공간지각력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 비행기조종사의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 비행하는 동안 비행기의 장으로 항공승무원의 활동을 지휘하며 운항 일지를 기록하고 비행 중 발생한 각종 설비상의 문제나 이상 현상을 보고합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10032-experience"></a>
### 빅 데이터 전문가 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-10032` · 시나리오 `career-net-10032-experience` `v001`.
- 원본 위치: `/items/189/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 빅 데이터 전문가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 빅 데이터 전문가는 대량의 빅 데이터로 사람들의 행동이나 시장의 변화 등을 분석하는 데 도움이 되는 정보를 제공합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-253-office-documents"></a>
### 요청에 맞는 문서 출력·보관

- 직업: `career-net-253` · 시나리오 `career-net-253-office-documents` `v001`.
- 원본 위치: `/items/190/data` · 역량: 대인관계능력.
- [보존한 첫 사무실 사례의 상세·단계·오류·분기](office-assistant-experience-v001.md). 이 사례는 v001 값을 그대로 유지했다.
- 장소: PAN-001 v001. 모니터 → 복합기 → 수납장. 요청 확인·날짜 오류 수정·출력·보관·인계.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10035-experience"></a>
### 사물 인터넷 전문가 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10035` · 시나리오 `career-net-10035-experience` `v001`.
- 원본 위치: `/items/191/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 사물 인터넷 전문가의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사물 인터넷 전문가는 우리 주변에 있는 사람, 사물, 공간과 관련된 데이터를 인터넷으로 연결하여 새로운 정보가 생성·수집·공유·활용되도록 하고, 이를 통해 새롭게 가치 있는 것을 만들어 이전에 없던 편리함을 사람들에게 제공합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-268-experience"></a>
### 사서 — 책의 주제와 이용자 요청을 연결해 안내

- 직업: `career-net-268` · 시나리오 `career-net-268-experience` `v001`.
- 원본 위치: `/items/192/data` · 역량: 대인관계능력.
- 장소 제안: 문화 활동실 · `PRM-035 v001` · [PAN-035 v001](../../../images/original/panoramas/PAN-035/v001/prm-035-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 사서의 업무 표현과 문화 활동실의 공동 문화 활동과 소규모 워크숍을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 이용자가 자료를 반납하고자 할 때에 자료와 대출자를 확인하고 파손 여부를 점검한 뒤 서가에 재배치합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 선반 · CND-028 | 책 선반에서 주제 라벨에 맞는 책 모형 분류 | 제시한 분류 라벨과 책 ID 일치 | 분류·선별 |
| 2 | 이동식 화이트보드 · CND-013 | 보드 UI에서 대출 요청과 책 ID의 불일치 확인 | 대출·책 ID 오류 식별 | 관찰·검사 |
| 3 | 테이블 · CND-010 | 테이블에서 이용 목적을 묻고 맞는 자료를 설명 | 이용 목적 확인과 자료 설명 충족 | 대화·응대 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10063-experience"></a>
### 사설탐정 — 출장 요청과 자료를 확인해 전달

- 직업: `career-net-10063` · 시나리오 `career-net-10063-experience` `v001`.
- 원본 위치: `/items/193/data` · 역량: 대인관계능력.
- 장소 제안: 출장 업무 공간 · `PRM-068 v001` · [PAN-068 v001](../../../images/original/panoramas/PAN-068/v001/prm-068-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 사설탐정의 업무 표현과 출장 업무 공간의 이동 중 임시 자리에서 업무를 처리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 범죄를 확인하고 법정 소송에 필요한 정보를 얻기 위하여 용의자, 범죄 사실, 혹은 권리 침해 사항에 관한 정보를 얻고 분석합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 휴대 전화 · CND-222 | 휴대전화에서 상대 요청과 누락 정보 확인 | 요청·언어·목적 확인 | 대화·응대 |
| 2 | 노트북 · CND-012 | 노트북에서 전달 자료와 원문 차이 확인 | 지정 오류·누락 식별 | 관찰·검사 |
| 3 | 문서 파우치 · CND-223 | 파우치에서 목적별 문서 분류 | 목적별 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 휴대 전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 문서 파우치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10034-experience"></a>
### 사이버 평판 관리자 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-10034` · 시나리오 `career-net-10034-experience` `v001`.
- 원본 위치: `/items/194/data` · 역량: 대인관계능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 사이버 평판 관리자의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사이버 평판 관리자는 주로 온라인에서 개인이나 기업과 관련된 사람들의 평가나 만족/불만족 내용과 같은 평판을 감시합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-462-experience"></a>
### 사이버교육운영자 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-462` · 시나리오 `career-net-462-experience` `v001`.
- 원본 위치: `/items/195/data` · 역량: 대인관계능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 사이버교육운영자의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사이버교육운영자는 컴퓨터를 이용해 시간과 장소에 상관없이 교사와 학생, 학생과 학생이 양방향으로 의사소통할 수 있는 온라인 교육환경을 설계 및 기획하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-976-experience"></a>
### 사진기자 — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-976` · 시나리오 `career-net-976-experience` `v001`.
- 원본 위치: `/items/196/data` · 역량: 예술시각능력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 사진기자의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사진기자는 신문이나 잡지 등에 게재되는 뉴스, 스포츠, 연예 등 관련 분야의 현장 보도사진을 찍습니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-975-experience"></a>
### 사진사 — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-975` · 시나리오 `career-net-975-experience` `v001`.
- 원본 위치: `/items/197/data` · 역량: 예술시각능력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 사진사의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사진사는 각종 카메라와 보조 장비를 이용하여 인물, 사물 및 자연 풍경 등을 촬영한 다음, 필름을 현상하고 사진을 인화, 수정, 완성합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-311-experience"></a>
### 사진인화 및 현상관련조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-311` · 시나리오 `career-net-311-experience` `v001`.
- 원본 위치: `/items/198/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 사진인화 및 현상관련조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사진인화 및 현상관련조작원은 사진필름 및 인화지 제조기를 조작하며, 사진필름을 가공하고 인화합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-310-experience"></a>
### 사진작가 — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-310` · 시나리오 `career-net-310-experience` `v001`.
- 원본 위치: `/items/199/data` · 역량: 예술시각능력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 사진작가의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 촬영대상의 특징, 거리, 구도를 확인하고 그에 따라 각도, 조명, 초점, 노출정도를 결정하여 촬영합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-934-experience"></a>
### 사회단체활동가 — 접수 문서를 확인하고 담당자에게 전달

- 직업: `career-net-934` · 시나리오 `career-net-934-experience` `v001`.
- 원본 위치: `/items/200/data` · 역량: 자기성찰능력.
- 장소 제안: 행정·문서 처리 사무실 · `PRM-003 v001` · [PAN-003 v001](../../../images/original/panoramas/PAN-003/v001/C-public-administration-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 사회단체활동가의 업무 표현과 행정·문서 처리 사무실의 기관 내부 담당자가 기록·검토·결재하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 개인, 기관, 단체에게 필요한 사회서비스 프로그램을 개발하고 업무 수행을 지원합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류철 · CND-022 | 서류철의 문서를 업무 종류별로 분류 | 문서별 분류 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 기록 화면과 문서의 불일치 수정 | 기록과 문서의 필수 항목 일치 | 관찰·검사 |
| 3 | 유선전화 · CND-019 | 전화로 누락 정보를 확인하고 결과 인계 | 확인 질문과 전달 필드 충족 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류철 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 유선전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-379-experience"></a>
### 사회복지사 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-379` · 시나리오 `career-net-379-experience` `v001`.
- 원본 위치: `/items/201/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 사회복지사의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사회복지사는 아동, 청소년, 노인, 장애인 등 다양한 사회적 보호가 필요한 사람들에게 사회복지제도를 활용하여 사회에 잘 적응할 수 있도록 도우며 사회복지 기획, 상담, 사례 관리, 자원 연결 등의 업무를 합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-933-experience"></a>
### 사회학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-933` · 시나리오 `career-net-933-experience` `v001`.
- 원본 위치: `/items/202/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 사회학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사회의 변화, 가족과 결혼, 사회문제, 소집단, 일탈행위, 집단행동과 사회운동, 인구 문제, 지역사회, 사회통제, 사회정책, 산업사회학 등과 여러 주제의 사회적 현상에 포함된 자료를 과학적으로 수집하고 분석합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-83-experience"></a>
### 산업공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-83` · 시나리오 `career-net-83-experience` `v001`.
- 원본 위치: `/items/203/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 산업공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 경영 기획, 기술 전략, 경영 정보 시스템 분야 등에서 회사에 영향을 끼치는 다양한 요인들을 분석하고 사업전략과 경영관리 방법을 모색합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-84-experience"></a>
### 산업안전관리원 — 배관 모형을 연결하고 상태 확인

- 직업: `career-net-84` · 시나리오 `career-net-84-experience` `v001`.
- 원본 위치: `/items/204/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 설비 작업 구역 · `PRM-037 v001` · [PAN-037 v001](../../../images/original/panoramas/PAN-037/v001/prm-037-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 산업안전관리원의 업무 표현과 설비 작업 구역의 배관과 설비를 설치·점검하는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 산업안전관리원은 산업현장에서 근로자의 생명과 안전 보호를 위한 계획을 세우고, 종사자들에게 안전교육을 실시하여 각종 산업재해를 예방하는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 상자 · CND-137 | 부품 상자에서 연결 규격에 맞는 부품 선택 | 규격·용도 일치 | 분류·선별 |
| 2 | 노출 배관 모형 · CND-135 | 노출 배관 모형의 연결 방향 맞춤 | 위치·방향·연결점 일치 | 조립·배치 |
| 3 | 제어함 · CND-138 | 제어함에서 가상 상태표와 다른 항목 확인 | 가상 오류 항목 식별 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노출 배관 모형 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10053-experience"></a>
### 산업카운슬러 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10053` · 시나리오 `career-net-10053-experience` `v001`.
- 원본 위치: `/items/205/data` · 역량: 대인관계능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 산업카운슬러의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 산업카운슬러는 기업의 환경에 따라 직원들의 정신적 문제를 파악하고 정신건강을 위한 전문적인 도움을 받을 수 있도록 상담하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-85-experience"></a>
### 상ㆍ하수도 처리장치 조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-85` · 시나리오 `career-net-85-experience` `v001`.
- 원본 위치: `/items/206/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 상ㆍ하수도 처리장치 조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 물 정화장치, 공기 및 가스압축기, 펌프장치 등을 정기적으로 점검하여 누수나 파손 등의 결함이 없는지 확인하고 수리합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-380-experience"></a>
### 상담전문가 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-380` · 시나리오 `career-net-380-experience` `v001`.
- 원본 위치: `/items/207/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 상담전문가의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 표준화된 심리검사를 실시하고, 상담을 통해 내담자의 내면을 심층적으로 탐색하여 그 결과를 분석합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1007-experience"></a>
### 상수도기술자 — 배관 모형을 연결하고 상태 확인

- 직업: `career-net-1007` · 시나리오 `career-net-1007-experience` `v001`.
- 원본 위치: `/items/208/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 설비 작업 구역 · `PRM-037 v001` · [PAN-037 v001](../../../images/original/panoramas/PAN-037/v001/prm-037-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 상수도기술자의 업무 표현과 설비 작업 구역의 배관과 설비를 설치·점검하는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 상수도기술자는 안전한 수돗물을 생산해 사람들에게 공급하기 위해 상수도의 수질 상태를 지속적으로 검사하고, 정수 처리 대응 방안 및 배급수의 효과적인 유지, 관리 방법 등에 대해 연구하고 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 상자 · CND-137 | 부품 상자에서 연결 규격에 맞는 부품 선택 | 규격·용도 일치 | 분류·선별 |
| 2 | 노출 배관 모형 · CND-135 | 노출 배관 모형의 연결 방향 맞춤 | 위치·방향·연결점 일치 | 조립·배치 |
| 3 | 제어함 · CND-138 | 제어함에서 가상 상태표와 다른 항목 확인 | 가상 오류 항목 식별 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노출 배관 모형 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-243-experience"></a>
### 상점판매원 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-243` · 시나리오 `career-net-243-experience` `v001`.
- 원본 위치: `/items/209/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 상점판매원의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 상품에 가격표를 부착하고 상품을 진열하며, 수시로 재고량을 확인하여 부족한 상품을 보충합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1114-experience"></a>
### 상품대여원 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-1114` · 시나리오 `career-net-1114-experience` `v001`.
- 원본 위치: `/items/210/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 상품대여원의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 상품대여원은 고객에게 책, 의상, 장난감, 행사용품, 사무용 가구, 영상 장비, 컴퓨터와 같은 정보기기 등의 다양한 상품을 대여하는 일을 담당합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-201-experience"></a>
### 상품중개인 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-201` · 시나리오 `career-net-201-experience` `v001`.
- 원본 위치: `/items/211/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 상품중개인의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 경매인은 시장에 나온 농수산물을 확인하고 물품에 대한 경매 우선순위를 결정하며 가격 평가, 최저 가격 설정, 낙찰자의 결정 등 경매 업무를 주관합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1138-experience"></a>
### 새시원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-1138` · 시나리오 `career-net-1138-experience` `v001`.
- 원본 위치: `/items/212/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 새시원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 새시원은 철재, 알루미늄, 스테인리스, 철사 등을 가공하여 창문틀, 새시, 철망문 등을 제작하고 시공하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10037-experience"></a>
### 생물 정보 분석가 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10037` · 시나리오 `career-net-10037-experience` `v001`.
- 원본 위치: `/items/213/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 생물 정보 분석가의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 데이터를 분석해 새로운 현상을 발견하는 일도 하는데, 이때 그 도구로 컴퓨터 프로그램이나 언어를 활용하며, 이를 개발하는 과정에도 참여합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-86-experience"></a>
### 생물공학연구원 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-86` · 시나리오 `career-net-86-experience` `v001`.
- 원본 위치: `/items/214/data` · 역량: 수리·논리력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 생물공학연구원의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 의학, 약학, 화공, 환경공학 등의 전문가들과 협동하여 유전자 재조합, 생물 공정 등 이미 개발된 기술을 습득하고 새로운 생물공학기술을 개발하는 연구를 수행합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-13-experience"></a>
### 생물학연구원 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-13` · 시나리오 `career-net-13-experience` `v001`.
- 원본 위치: `/items/215/data` · 역량: 수리·논리력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 생물학연구원의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 생물학연구원은 생명체에 대한 기원, 발달, 구조, 해부, 환경 등에 대해 연구하고, 연구 결과를 의학, 농업 등 다른 분야에 적용하거나 응용하는 방법을 연구, 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10036-experience"></a>
### 생체 인식 전문가 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10036` · 시나리오 `career-net-10036-experience` `v001`.
- 원본 위치: `/items/216/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 생체 인식 전문가의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 생체 인식 전문가는 카메라, 스캐너 등의 센서 장치로 생체 정보(지문, 얼굴, 눈동자의 홍채, 정맥 등)를 파악하여, 이를 통해 본인임을 확인해 주는 장치를 만드는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-222-experience"></a>
### 생활설계사 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-222` · 시나리오 `career-net-222-experience` `v001`.
- 원본 위치: `/items/217/data` · 역량: 대인관계능력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 생활설계사의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 생활설계사는 금융보험에 대한 지식을 바탕으로 보험 가입 대상자를 선정 및 방문하여 각종 보험 상품의 종류와 특성을 설명하고, 고객의 생활수준, 가족 상황, 건강상태, 미래 계획 등을 파악하여 적합한 보험상품을 권유하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1109-experience"></a>
### 서예가 — 표현 재료를 고르고 작은 작품 구성

- 직업: `career-net-1109` · 시나리오 `career-net-1109-experience` `v001`.
- 원본 위치: `/items/218/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 미술 작업실 · `PRM-028 v001` · [PAN-028 v001](../../../images/original/panoramas/PAN-028/v001/prm-028-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 서예가의 업무 표현과 미술 작업실의 그림을 그리고 작품을 살펴보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 서예가는 먹과 붓을 이용하여 화선지에 글이나 시를 쓰거나 사군자를 그리는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 팔레트 도구 · CND-107 | 팔레트 도구에서 표현 목표에 맞는 재료 선택 | 재료 역할과 목표 일치 | 분류·선별 |
| 2 | 빈 캔버스 · CND-105 | 캔버스에 형태와 구도를 구성 | 필수 요소·구도 조건 충족 | 제작·표현 |
| 3 | 이젤 · CND-104 | 이젤에서 작품을 다른 시점으로 확인 | 지정 확인 항목 점검 완료 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 팔레트 도구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 빈 캔버스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이젤 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-87-experience"></a>
### 석공 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-87` · 시나리오 `career-net-87-experience` `v001`.
- 원본 위치: `/items/219/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 석공의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 석공은 1차적으로 가공된 석재를 건축 내ㆍ외장재, 석축용 석재 또는 생활도구나 기념품 등의 목적에 따라 자르고, 다듬고, 만드는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-88-experience"></a>
### 석유화학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-88` · 시나리오 `career-net-88-experience` `v001`.
- 원본 위치: `/items/220/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 석유화학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 제조장치 운전 상태의 이상 여부를 일정한 시간마다 점검하고 확인한 내용을 기록합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-223-experience"></a>
### 선물중개인 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-223` · 시나리오 `career-net-223-experience` `v001`.
- 원본 위치: `/items/221/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 선물중개인의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 적정한 거래 시점을 파악하기 위해 국제 선물시장의 동향을 분석하여 고객에게 투자 상담 또는 시장 정보를 제공합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1125-experience"></a>
### 선박 및 열차객실승무원 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-1125` · 시나리오 `career-net-1125-experience` `v001`.
- 원본 위치: `/items/222/data` · 역량: 대인관계능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 선박 및 열차객실승무원의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 승객의 탑승 인원을 확인하고, 운행, 노선, 일정 및 편의 시간 등에 관한 승객의 질문에 응대합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1112-experience"></a>
### 선박갑판원 — 갑판 모형의 준비 상태 확인

- 직업: `career-net-1112` · 시나리오 `career-net-1112-experience` `v001`.
- 원본 위치: `/items/223/data` · 역량: 신체·운동능력.
- 장소 제안: 선박 갑판 · `PRM-044 v001` · [PAN-044 v001](../../../images/original/panoramas/PAN-044/v001/prm-044-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 선박갑판원의 업무 표현과 선박 갑판의 선원이 외부 갑판 설비를 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 선박의 구명 장비, 화물 취급 설비, 닻, 케이블 등의 장비를 점검 및 수리하고, 갑판에 설치된 시설물 및 장비를 보수하며, 선체의 부식과 마멸을 방지하기 위하여 선박에 페인트를 도장하거나 선체를 정비합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 구명환 · CND-168 | 구명환의 가상 점검 항목 확인 | 점검 결함 식별 | 관찰·검사 |
| 2 | 밧줄 코일 · CND-169 | 밧줄 코일을 지정 위치로 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 계류 장치 · CND-170 | 계류 장치 모형에서 교육용 순서 선택 | 모형 훈련 순서 일치 | 순서·절차 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 구명환 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 밧줄 코일 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 계류 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-92-experience"></a>
### 선박정비원 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-92` · 시나리오 `career-net-92-experience` `v001`.
- 원본 위치: `/items/224/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 선박정비원의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 선박정비원은 선박기계를 정비, 점검하고 선박의 고장 상태를 확인하며 수리합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-176-experience"></a>
### 선장 및 항해사 — 가상 항로를 확인하고 운항 요청 전달

- 직업: `career-net-176` · 시나리오 `career-net-176-experience` `v001`.
- 원본 위치: `/items/225/data` · 역량: 신체·운동능력.
- 장소 제안: 조타실 · `PRM-045 v001` · [PAN-045 v001](../../../images/original/panoramas/PAN-045/v001/prm-045-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 선장 및 항해사의 업무 표현과 조타실의 선박의 방향과 상태를 확인하며 운항하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 안전한 운항을 위해 항해 목적지, 기후, 거리 등을 확인하고 선박의 조정실, 기관실, 통신실 등을 점검하며 화물의 적재 상태, 식료품, 연료 등을 검사하고 승무원을 확인해 그에 알맞은 업무를 분담하고 지휘합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 항해 화면 · CND-174 | 항해 화면에서 장애 구간을 피해 경로 선택 | 가상 경로 제약 충족 | 계획·배분 |
| 2 | 조타 장치 · CND-171 | 조타 장치를 가상 유도 경로에 맞춤 | 경로 추적 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태를 인계 | 위치·상태·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 항해 화면 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조타 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-165-experience"></a>
### 설문조사원 — 출장 요청과 자료를 확인해 전달

- 직업: `career-net-165` · 시나리오 `career-net-165-experience` `v001`.
- 원본 위치: `/items/226/data` · 역량: 대인관계능력.
- 장소 제안: 출장 업무 공간 · `PRM-068 v001` · [PAN-068 v001](../../../images/original/panoramas/PAN-068/v001/prm-068-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 설문조사원의 업무 표현과 출장 업무 공간의 이동 중 임시 자리에서 업무를 처리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 설문조사나 시장조사 업무에서는 조사 계획에 따라 작성된 설문지와 조사표를 받은 다음, 조사 대상자와 연락하여 조사표에 따라 설문 내용을 조사합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 휴대 전화 · CND-222 | 휴대전화에서 상대 요청과 누락 정보 확인 | 요청·언어·목적 확인 | 대화·응대 |
| 2 | 노트북 · CND-012 | 노트북에서 전달 자료와 원문 차이 확인 | 지정 오류·누락 식별 | 관찰·검사 |
| 3 | 문서 파우치 · CND-223 | 파우치에서 목적별 문서 분류 | 목적별 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 휴대 전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 문서 파우치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-57-experience"></a>
### 섬유공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-57` · 시나리오 `career-net-57-experience` `v001`.
- 원본 위치: `/items/227/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 섬유공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 섬유 소재의 염색 기법 등을 개발하고, 섬유 소재에 대한 품질관리, 생산관리 업무를 수행하기도 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-73-experience"></a>
### 섬유제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-73` · 시나리오 `career-net-73-experience` `v001`.
- 원본 위치: `/items/228/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 섬유제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기계를 정기적으로 점검하고 이상이 있으면 수리합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-313-experience"></a>
### 성악가 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-313` · 시나리오 `career-net-313-experience` `v001`.
- 원본 위치: `/items/229/data` · 역량: 음악능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 성악가의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 음악 악보를 보고 피아노나 오케스트라의 반주에 맞추어 리듬을 확인하고 노래합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-270-experience"></a>
### 성우 — 방송 입력을 확인하고 신호에 맞춰 시작

- 직업: `career-net-270` · 시나리오 `career-net-270-experience` `v001`.
- 원본 위치: `/items/230/data` · 역량: 창의력.
- 장소 제안: 방송 스튜디오 · `PRM-031 v001` · [PAN-031 v001](../../../images/original/panoramas/PAN-031/v001/prm-031-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 성우의 업무 표현과 방송 스튜디오의 진행자가 음성과 영상을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 성우는 라디오, 텔레비전, 영화녹음 등에서 연기의 감정을 자신의 목소리에 실어 연기합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 암 · CND-116 | 마이크 암을 표시 위치로 맞춤 | 위치 허용 범위 충족 | 측정·조절 |
| 2 | 소형 오디오 콘솔 · CND-118 | 오디오 콘솔의 가상 레벨을 목표에 조절 | 가상 레벨 구간 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라의 큐 신호에 맞춰 녹화 입력 | 큐 입력 허용 시간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 암 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 오디오 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-384-experience"></a>
### 성직자 — 선택한 전통의 공동 모임 준비

- 직업: `career-net-384` · 시나리오 `career-net-384-experience` `v001`.
- 원본 위치: `/items/231/data` · 역량: 자기성찰능력.
- 장소 제안: 기독교(개신교) 예배실 — 목사 · `PRM-064 v002` · [PAN-064 v001](../../../images/original/panoramas/PAN-064/v001/prm-064-v001.png).
- 장소 선택 상태: `preview_option_not_selected`. 기준 성직자 직업만으로 종교를 추정하지 않는다. 기본 필드는 첫 대안의 미리보기이며 실행 대상은 아직 미선택.
- 원본에서 선택한 업무 근거: 성직자는 승려, 목사, 신부 등이 있으며 교리를 해석하고 전달하며 신자들의 고충을 들어주고 안식을 주는 상담자로서 역할을 수행하면서 사회 지도자로서의 역할을 하기도 합니다.
- 체험의 업무 자료: 사용자가 선택한 전통의 모임 목적·참여 요청과 안내.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 펼친 성경 · CND-245 | 성경 거치 자료에서 사용자 지정 주제 확인 | 사용자가 선택한 주제 범위 일치 | 관찰·검사 |
| 2 | 설교 강대상 · CND-244 | 강대상 UI에서 참여자의 요청을 듣고 안내 | 요청 확인·안내 합의 | 대화·응대 |
| 3 | 찬송가 책 거치대 · CND-248 | 찬송가 거치대에서 모임 순서 계획 | 선택한 모임 단계 누락 없음 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 펼친 성경 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 설교 강대상 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 찬송가 책 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 종교 전통을 추정하지 않음. 세 전통의 장면 대안 중 사용자 선택 후 실행 가능. 의례 세부는 별도 검토.
- 미선택 장면 대안: 기독교(개신교) 예배실 — 목사 · PAN-064 v001 / 펼친 성경 CND-245, 설교 강대상 CND-244, 찬송가 책 거치대 CND-248.
- 미선택 장면 대안: 불교 법당 — 스님 · PAN-070 v001 / 낮은 경전 독서대 CND-253, 방석 CND-252, 목탁 CND-254.
- 미선택 장면 대안: 천주교 성당 — 신부님 · PAN-071 v001 / 전례서 CND-261, 독서대 CND-258, 촛대 CND-262.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-224-experience"></a>
### 세무사 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-224` · 시나리오 `career-net-224-experience` `v001`.
- 원본 위치: `/items/232/data` · 역량: 수리·논리력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 세무사의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 세무사는 세무에 대한 법률적 지식을 바탕으로 세금에 대한 상담과 자문을 하고, 의뢰인을 대리하여 세무에 대한 각종 서류를 작성하여 세무서에 신고, 신청, 청구하는 등의 일을 합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-166-experience"></a>
### 세탁원 — 주택 모형 점검과 작업 요청 정리

- 직업: `career-net-166` · 시나리오 `career-net-166-experience` `v001`.
- 원본 위치: `/items/233/data` · 역량: 손재능.
- 장소 제안: 주택 관리 공간 · `PRM-063 v001` · [PAN-063 v001](../../../images/original/panoramas/PAN-063/v001/prm-063-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 세탁원의 업무 표현과 주택 관리 공간의 건물 설비와 생활 지원 도구를 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객으로부터 의뢰받은 세탁물을 옷감의 종류에 따라 분류합니다.
- 체험의 업무 자료: 이용자 요청·물품 구역과 점검 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 점검 보드 · CND-218 | 점검 보드에서 누락된 요청 확인 | 요청 ID·누락 식별 | 관찰·검사 |
| 2 | 설비함 · CND-217 | 설비함의 가상 표시 단서로 점검 담당 선택 | 가상 단서·담당 범위 일치 | 진단·해결 |
| 3 | 청소 도구 · CND-163 | 청소 도구를 작업 구역별로 분류 | 도구 구역 규칙 충족 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 점검 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 설비함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 청소 도구 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-167-experience"></a>
### 소믈리에 — 주문에 맞게 조리 준비 순서 맞추기

- 직업: `career-net-167` · 시나리오 `career-net-167-experience` `v001`.
- 원본 위치: `/items/234/data` · 역량: 대인관계능력.
- 장소 제안: 주방 · `PRM-024 v001` · [PAN-024 v001](../../../images/original/panoramas/PAN-024/v001/prm-024-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 소믈리에의 업무 표현과 주방의 식재료 준비에서 조리와 담기까지 이어지는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 와인의 품목을 선정하고 이에 따른 와인 리스트를 작성하며 와인의 보관과 관리의 책임을 집니다.
- 체험의 업무 자료: 가상 주문·재료 구분과 준비 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 냉장고 · CND-090 | 냉장고에서 주문과 재료 라벨 대조 | 재료·주문·구역 구분 일치 | 분류·선별 |
| 2 | 조리대 · CND-088 | 조리대에서 가상 조리 단계를 순서대로 배치 | 가상 레시피 단계 일치 | 순서·절차 |
| 3 | 가열 기구 · CND-089 | 가열 기구를 교육용 표시 범위에 조절 | 훈련용 눈금 범위 충족 | 측정·조절 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 냉장고 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조리대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 가열 기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-385-experience"></a>
### 소방관 — 가상 관제 신호를 확인하고 대응 인계

- 직업: `career-net-385` · 시나리오 `career-net-385-experience` `v001`.
- 원본 위치: `/items/235/data` · 역량: 신체·운동능력.
- 장소 제안: 관제실 · `PRM-061 v001` · [PAN-061 v001](../../../images/original/panoramas/PAN-061/v001/prm-061-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 소방관의 업무 표현과 관제실의 여러 상태 화면을 확인하고 상황을 조정하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 화재가 발생하였을 경우 신속하게 출동하여 화재를 진압하며, 소방용수 시설을 관리하여 소방용수를 효과적으로 공급합니다.
- 체험의 업무 자료: 가상 사건·상태 신호와 전달 우선순위.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 시간에 따라 바뀌는 이상 신호 확인 | 가상 이상 신호 식별 | 관찰·검사 |
| 2 | 관제 콘솔 · CND-213 | 관제 콘솔에서 가상 대응 우선순위 배치 | 명시된 우선순위 조건 충족 | 계획·배분 |
| 3 | 통신 기기 · CND-175 | 통신 장치로 위치·상태·담당자 전달 | 인계 필드·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관제 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 검토: 전용 활동 공간이 현재 파노라마 목록에 없음. 선택 장면은 관제·상담·연습 등 한정된 보조 장면 제안이며 현장 대표 공간의 대체 완성본이 아님.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10041-experience"></a>
### 소비생활어드바이저 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-10041` · 시나리오 `career-net-10041-experience` `v001`.
- 원본 위치: `/items/236/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 소비생활어드바이저의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 소비생활어드바이저는 기업, 행정 기관, 각종 단체 등의 상담 창구에서 소비자 불만 상담에 응하고, 소비자 의견, 동향 등을 파악하여 상품, 서비스를 개발하고 개선하는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-973-experience"></a>
### 소설가 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-973` · 시나리오 `career-net-973-experience` `v001`.
- 원본 위치: `/items/237/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 소설가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 소설가는 소설의 주제를 결정하고 그 주제를 가장 효과적으로 나타낼 수 있는 소재들을 찾아 적절하게 구성하여 예술적으로 표현합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-539-experience"></a>
### 소음진동기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-539` · 시나리오 `career-net-539-experience` `v001`.
- 원본 위치: `/items/238/data` · 역량: 자연친화력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 소음진동기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 소음과 진동을 측정 및 분석하고 원인을 감소 또는 제거할 수 있는 방지시설이나 방법 등을 연구하고 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-459-experience"></a>
### 속기사 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-459` · 시나리오 `career-net-459-experience` `v001`.
- 원본 위치: `/items/239/data` · 역량: 대인관계능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 속기사의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 속기사는 속기 문자를 사용하여 발언자가 말한 내용을 받아쓰거나 컴퓨터 속기 기계로 기록하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10040-experience"></a>
### 손실방지전문가 — 가상 관제 신호를 확인하고 대응 인계

- 직업: `career-net-10040` · 시나리오 `career-net-10040-experience` `v001`.
- 원본 위치: `/items/240/data` · 역량: 수리·논리력.
- 장소 제안: 관제실 · `PRM-061 v001` · [PAN-061 v001](../../../images/original/panoramas/PAN-061/v001/prm-061-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 손실방지전문가의 업무 표현과 관제실의 여러 상태 화면을 확인하고 상황을 조정하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 손실방지전문가는 기업의 손실을 줄이고 안전을 유지하기 위해 시스템을 관리하는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 시간에 따라 바뀌는 이상 신호 확인 | 가상 이상 신호 식별 | 관찰·검사 |
| 2 | 관제 콘솔 · CND-213 | 관제 콘솔에서 가상 대응 우선순위 배치 | 명시된 우선순위 조건 충족 | 계획·배분 |
| 3 | 통신 기기 · CND-175 | 통신 장치로 위치·상태·담당자 전달 | 인계 필드·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관제 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-226-experience"></a>
### 손해사정사 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-226` · 시나리오 `career-net-226-experience` `v001`.
- 원본 위치: `/items/241/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 손해사정사의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 사고 발생에 관한 정확한 자료를 수집하여 조사 및 분석하고, 보상 범위를 결정하기 위해 보상 협상 사무원의 보고서를 조사하며, 유사한 보험 사례나 판례들을 검토합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-178-experience"></a>
### 쇼핑호스트 — 방송 입력을 확인하고 신호에 맞춰 시작

- 직업: `career-net-178` · 시나리오 `career-net-178-experience` `v001`.
- 원본 위치: `/items/242/data` · 역량: 창의력.
- 장소 제안: 방송 스튜디오 · `PRM-031 v001` · [PAN-031 v001](../../../images/original/panoramas/PAN-031/v001/prm-031-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 쇼핑호스트의 업무 표현과 방송 스튜디오의 진행자가 음성과 영상을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 원활한 방송 진행을 위해 방송 시작 전에 판매 상품에 대한 시장을 조사하고, 제품의 특성을 충분히 파악하며, 방송에 함께 출연하는 출연자와 진행 상황을 연습합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 암 · CND-116 | 마이크 암을 표시 위치로 맞춤 | 위치 허용 범위 충족 | 측정·조절 |
| 2 | 소형 오디오 콘솔 · CND-118 | 오디오 콘솔의 가상 레벨을 목표에 조절 | 가상 레벨 구간 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라의 큐 신호에 맞춰 녹화 입력 | 큐 입력 허용 시간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 암 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 오디오 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-15-experience"></a>
### 수의사 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-15` · 시나리오 `career-net-15-experience` `v001`.
- 원본 위치: `/items/243/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 수의사의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 각종 검사를 통해 아픈 동물의 질병을 진단, 처방, 치료하고, 동물의 분만을 돕거나 외과수술을 시행하며, 동물 질병에 대한 역학조사와 위생 관리를 통해 질병을 예방합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10048-experience"></a>
### 수의테크니션 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-10048` · 시나리오 `career-net-10048-experience` `v001`.
- 원본 위치: `/items/244/data` · 역량: 대인관계능력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 수의테크니션의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 수의테크니션은 동물병원이나 그 외 관련된 기관에서 수의사의 지도하에 동물의 간호 또는 진료를 보조하는 일을 합니다.
- 체험의 업무 자료: 가상 개체 ID·관리 요청과 용품 구분.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1255-experience"></a>
### 수질환경연구원 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-1255` · 시나리오 `career-net-1255-experience` `v001`.
- 원본 위치: `/items/245/data` · 역량: 수리·논리력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 수질환경연구원의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 수질오염 측정 및 분석 도구를 이용하여 지역의 수질 특성과 수질오염 정도를 조사합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-17-experience"></a>
### 수학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-17` · 시나리오 `career-net-17-experience` `v001`.
- 원본 위치: `/items/246/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 수학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 순수수학연구원은 자연현상을 관찰해 얻어진 일반적인 생각을 논리적인 모순이 없는 수학적 모형으로 만든 다음 그 모형을 분석해서 이론을 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10025-experience"></a>
### 스마트 그리드 엔지니어 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10025` · 시나리오 `career-net-10025-experience` `v001`.
- 원본 위치: `/items/247/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스마트 그리드 엔지니어의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 효율적으로 전력을 관리하는 지능형 전력망을 운영합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10005-experience"></a>
### 스마트 도시 전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-10005` · 시나리오 `career-net-10005-experience` `v001`.
- 원본 위치: `/items/248/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 스마트 도시 전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스마트 도시 전문가는 정보 통신 기술을 이용하여 정보를 수집하고 자원을 효율적으로 관리하는 스마트 도시를 계획합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10009-experience"></a>
### 스마트 의류 개발자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10009` · 시나리오 `career-net-10009-experience` `v001`.
- 원본 위치: `/items/249/data` · 역량: 손재능.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스마트 의류 개발자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 음악을 들을 수 있는 멀티미디어, 현재 위치를 확인할 수 있는 위치기반서비스를 활용하여 사람들의 생활을 풍요롭게 만드는 스마트 의류를 개발합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10028-experience"></a>
### 스마트 재난 관리 전문가 — 가상 관제 신호를 확인하고 대응 인계

- 직업: `career-net-10028` · 시나리오 `career-net-10028-experience` `v001`.
- 원본 위치: `/items/250/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 관제실 · `PRM-061 v001` · [PAN-061 v001](../../../images/original/panoramas/PAN-061/v001/prm-061-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 스마트 재난 관리 전문가의 업무 표현과 관제실의 여러 상태 화면을 확인하고 상황을 조정하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 재난 상황의 공통점이나 발생 원인을 분석하여 필요한 대응 방법을 찾고, IT 기술과 최첨단 장비를 융합하여 재난관리 시스템을 기획, 개발합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 시간에 따라 바뀌는 이상 신호 확인 | 가상 이상 신호 식별 | 관찰·검사 |
| 2 | 관제 콘솔 · CND-213 | 관제 콘솔에서 가상 대응 우선순위 배치 | 명시된 우선순위 조건 충족 | 계획·배분 |
| 3 | 통신 기기 · CND-175 | 통신 장치로 위치·상태·담당자 전달 | 인계 필드·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관제 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10008-experience"></a>
### 스마트 팜 구축가 — 모종 위치와 가상 재배 환경 맞추기

- 직업: `career-net-10008` · 시나리오 `career-net-10008-experience` `v001`.
- 원본 위치: `/items/251/data` · 역량: 자연친화력.
- 장소 제안: 온실 · `PRM-041 v001` · [PAN-041 v001](../../../images/original/panoramas/PAN-041/v001/prm-041-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스마트 팜 구축가의 업무 표현과 온실의 통제된 재배 환경에서 식물을 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스마트 팜 구축가는 농업에 정보통신 기술을 접목하여 효율적으로 작물을 재배하거나 가축을 기르는 기술을 개발하고 수집된 정보를 분석합니다.
- 체험의 업무 자료: 가상 구획·관리 요청과 상태 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모종 트레이 · CND-154 | 모종 트레이에서 요청 모종 선택 | 모종 ID·구획 일치 | 분류·선별 |
| 2 | 환경 센서 · CND-156 | 환경 센서의 가상 기록 변화 확인 | 가상 변화 지점 식별 | 관찰·검사 |
| 3 | 관수 설비 · CND-155 | 관수 설비를 교육용 목표 구간에 조절 | 교육용 설정 범위 충족 | 측정·조절 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모종 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 환경 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관수 설비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10112-experience"></a>
### 스마트공장 기술자 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-10112` · 시나리오 `career-net-10112-experience` `v001`.
- 원본 위치: `/items/252/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스마트공장 기술자의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 최적의 설비를 설계하기 위해 시스템의 기술규격을 검토하고 분석합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10106-experience"></a>
### 스마트팜 운영자 — 모종 위치와 가상 재배 환경 맞추기

- 직업: `career-net-10106` · 시나리오 `career-net-10106-experience` `v001`.
- 원본 위치: `/items/253/data` · 역량: 자연친화력.
- 장소 제안: 온실 · `PRM-041 v001` · [PAN-041 v001](../../../images/original/panoramas/PAN-041/v001/prm-041-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스마트팜 운영자의 업무 표현과 온실의 통제된 재배 환경에서 식물을 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 농사 기술에 정보통신기술(ICT)을 결합한 스마트 팜(농장)에서 농사를 운영합니다.
- 체험의 업무 자료: 가상 구획·관리 요청과 상태 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모종 트레이 · CND-154 | 모종 트레이에서 요청 모종 선택 | 모종 ID·구획 일치 | 분류·선별 |
| 2 | 환경 센서 · CND-156 | 환경 센서의 가상 기록 변화 확인 | 가상 변화 지점 식별 | 관찰·검사 |
| 3 | 관수 설비 · CND-155 | 관수 설비를 교육용 목표 구간에 조절 | 교육용 설정 범위 충족 | 측정·조절 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모종 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 환경 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관수 설비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-314-experience"></a>
### 스턴트맨 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-314` · 시나리오 `career-net-314-experience` `v001`.
- 원본 위치: `/items/254/data` · 역량: 창의력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스턴트맨의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스턴트맨은 영화나 텔레비전 드라마에 출연하여 무술 연기를 합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10015-experience"></a>
### 스포츠 심리 상담원 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10015` · 시나리오 `career-net-10015-experience` `v001`.
- 원본 위치: `/items/255/data` · 역량: 대인관계능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스포츠 심리 상담원의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스포츠 심리 상담원은 심리학과 체육학의 지식을 바탕으로 운동선수나 가족, 지도자에게 심리 상담과 교육을 합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-421-experience"></a>
### 스포츠강사 — 가상 동작을 비교하고 연습 도구 준비

- 직업: `career-net-421` · 시나리오 `career-net-421-experience` `v001`.
- 원본 위치: `/items/256/data` · 역량: 신체·운동능력.
- 장소 제안: 운동 지도실 · `PRM-048 v001` · [PAN-048 v001](../../../images/original/panoramas/PAN-048/v001/prm-048-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스포츠강사의 업무 표현과 운동 지도실의 지도자와 이용자가 자세·동작을 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스포츠강사는 공공 또는 민간 체육시설에서 사람들을 대상으로 건강 유지와 증진, 스트레스 해소, 여가의 목적을 위해 여러 운동 프로그램을 개발하거나 가르치는 일을 합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 자세 확인용 독립 거울 · CND-186 | 거울에서 사례 동작의 차이 확인 | 사례 차이 지점 식별 | 관찰·검사 |
| 2 | 낮은 스텝 · CND-184 | 낮은 스텝을 가상 훈련 위치에 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 소형 아령 · CND-185 | 아령 모형의 선택 값을 사례 목표에 맞춤 | 교육용 목표 구간 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 자세 확인용 독립 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 스텝 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 아령 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10066-experience"></a>
### 스포츠기록분석연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-10066` · 시나리오 `career-net-10066-experience` `v001`.
- 원본 위치: `/items/257/data` · 역량: 공간지각력, 손재능.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 스포츠기록분석연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스포츠 경기를 객관적으로 분석하기 위한 기록 시스템과 분석 기법을 개발하고 분석 기법과 통계를 활용한 학문적인 연구 또한 스포츠기록분석연구원이 수행하는 주요한 업무입니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 공간지각력, 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1088-experience"></a>
### 스포츠에이전트 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-1088` · 시나리오 `career-net-1088-experience` `v001`.
- 원본 위치: `/items/258/data` · 역량: 대인관계능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스포츠에이전트의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스포츠에이전트는 스포츠 관련 프로그램 및 서비스를 개발하고 운영을 위한 기획 및 절차를 조직하여 조정 및 관리합니다.
- 체험의 업무 자료: 가상 활동 규칙·도구와 동작 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-392-experience"></a>
### 스포츠트레이너 — 가상 동작을 비교하고 연습 도구 준비

- 직업: `career-net-392` · 시나리오 `career-net-392-experience` `v001`.
- 원본 위치: `/items/259/data` · 역량: 신체·운동능력.
- 장소 제안: 운동 지도실 · `PRM-048 v001` · [PAN-048 v001](../../../images/original/panoramas/PAN-048/v001/prm-048-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스포츠트레이너의 업무 표현과 운동 지도실의 지도자와 이용자가 자세·동작을 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스포츠트레이너는 운동선수들의 건강상태를 확인하고 선수들이 경기에서 최상의 컨디션을 발휘할 수 있도록 조언하고 훈련을 시킵니다.
- 체험의 업무 자료: 가상 활동 규칙·도구와 동작 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 자세 확인용 독립 거울 · CND-186 | 거울에서 사례 동작의 차이 확인 | 사례 차이 지점 식별 | 관찰·검사 |
| 2 | 낮은 스텝 · CND-184 | 낮은 스텝을 가상 훈련 위치에 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 소형 아령 · CND-185 | 아령 모형의 선택 값을 사례 목표에 맞춤 | 교육용 목표 구간 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 자세 확인용 독립 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 스텝 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 아령 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1437-experience"></a>
### 스포츠해설가 — 방송 입력을 확인하고 신호에 맞춰 시작

- 직업: `career-net-1437` · 시나리오 `career-net-1437-experience` `v001`.
- 원본 위치: `/items/260/data` · 역량: 언어능력.
- 장소 제안: 방송 스튜디오 · `PRM-031 v001` · [PAN-031 v001](../../../images/original/panoramas/PAN-031/v001/prm-031-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 스포츠해설가의 업무 표현과 방송 스튜디오의 진행자가 음성과 영상을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 스포츠 분야에서 발생한 각종 정보를 수집하고 분석하여 보도자료를 정리합니다.
- 체험의 업무 자료: 가상 활동 규칙·도구와 동작 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 암 · CND-116 | 마이크 암을 표시 위치로 맞춤 | 위치 허용 범위 충족 | 측정·조절 |
| 2 | 소형 오디오 콘솔 · CND-118 | 오디오 콘솔의 가상 레벨을 목표에 조절 | 가상 레벨 구간 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라의 큐 신호에 맞춰 녹화 입력 | 큐 입력 허용 시간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 암 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 오디오 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-937-experience"></a>
### 시각디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-937` · 시나리오 `career-net-937-experience` `v001`.
- 원본 위치: `/items/261/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 시각디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 완성된 디자인은 내부의 확인을 거쳐 의뢰자에게 보내며, 상업용으로 인쇄, 제작될 경우 제작 과정에서부터 디자인이 생각대로 잘 완성되었는지 확인합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-97-experience"></a>
### 시멘트제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-97` · 시나리오 `career-net-97-experience` `v001`.
- 원본 위치: `/items/262/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 시멘트제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 완성제품을 측정, 계량, 검사하고 명세서와 비교하며, 기계장치를 세척하고 기능 장애를 탐지해 수리하며 생산기록을 작성하고 보관합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-834-experience"></a>
### 시스템소프트웨어개발자 — 가상 기능의 요구와 테스트 결과 맞추기

- 직업: `career-net-834` · 시나리오 `career-net-834-experience` `v001`.
- 원본 위치: `/items/263/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 시스템소프트웨어개발자의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 시스템소프트웨어개발자는 컴퓨터를 작동시키고 각 부품의 활동을 조정, 통제, 관리하는 윈도우, 맥, 리눅스와 같은 오퍼레이팅시스템 소프트웨어를 연구, 개발, 설계하는 일을 합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 사용자 요구와 다른 실행 결과 찾기 | 명시된 요구·결과 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI로 가상 기능 블록 순서·조건 수정 | 필수 기능 블록과 제약 충족 | 제작·표현 |
| 3 | 마우스 · CND-018 | 마우스로 테스트 단서와 수정 대안을 연결해 재실행 | 가상 테스트의 입력·기대 결과 일치 | 진단·해결 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 마우스 / common / AST-007 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 선택 장면의 기존 필수 후보 밖 추가 제안: CND-018. 기존 후보 목록은 자동 수정하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-440-experience"></a>
### 시스템엔지니어 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-440` · 시나리오 `career-net-440-experience` `v001`.
- 원본 위치: `/items/264/data` · 역량: 수리·논리력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 시스템엔지니어의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 시스템엔지니어는 정보 기술의 기술적 사항과 해당 업무에 필요한 사항을 종합적으로 분석하고 설계하여 사용 용도에 따라 가장 빠르면서 안정된 정보시스템을 만드는 일을 합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-968-experience"></a>
### 시인 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-968` · 시나리오 `career-net-968-experience` `v001`.
- 원본 위치: `/items/265/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 시인의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 시인은 자연, 인생 등 여러 현상에 대한 인간의 사상과 감정을 운율이 있는 언어로 표현합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-230-experience"></a>
### 시장 및 여론조사전문가 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-230` · 시나리오 `career-net-230-experience` `v001`.
- 원본 위치: `/items/266/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 시장 및 여론조사전문가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 시장 및 여론조사전문가는 통계학, 경제학, 사회학 및 심리학 등의 전문 지식을 바탕으로 특정 상품이나 여론 및 선거, TV 시청률 등에 대한 조사와 연구를 실시하고, 조사 결과를 분석하여 보고서로 작성하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1150-experience"></a>
### 식품가공검사원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1150` · 시나리오 `career-net-1150-experience` `v001`.
- 원본 위치: `/items/267/data` · 역량: 손재능.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 식품가공검사원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 식품가공검사원은 식품을 생산하고 조리하는 데 사용되는 원료와 최종 식품 생산품이 표준에 맞는지 검사하고 이에 대한 등급을 매기는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-162-experience"></a>
### 식품공학기술자 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-162` · 시나리오 `career-net-162-experience` `v001`.
- 원본 위치: `/items/268/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 식품공학기술자의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 식품공학기술자는 식품에 대한 조사, 개발, 생산 기술 개발, 품질 관리, 포장, 가공 및 이용에 관한 업무를 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10047-experience"></a>
### 식품융합엔지니어 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-10047` · 시나리오 `career-net-10047-experience` `v001`.
- 원본 위치: `/items/269/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 식품융합엔지니어의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 식품융합엔지니어는 미래의 식량 부족 위기에 대비해서 생명과학과식품과학 기술, 전자 및 기계공학 기술 등의 융합을 통해 새로운 기능과 형태를 가진 식재료를 개발하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-98-experience"></a>
### 신경회로망연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-98` · 시나리오 `career-net-98-experience` `v001`.
- 원본 위치: `/items/270/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 신경회로망연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 신경회로망연구원은 영상 및 음성인식, 로봇 제어, 통신 등에 사용되는 인공지능형 반도체 및 응용기술을 연구하고 개발하는 일을 담당합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10116-experience"></a>
### 신소재 개발 연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10116` · 시나리오 `career-net-10116-experience` `v001`.
- 원본 위치: `/items/271/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 신소재 개발 연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 신소재 개발 연구원은 금속, 고분자, 세라믹, 복합소재 등 다양한 신소재를 설계하고, 실험을 통해 새로운 특성이나 기능을 가진 소재를 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1436-experience"></a>
### 신약개발연구원 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-1436` · 시나리오 `career-net-1436-experience` `v001`.
- 원본 위치: `/items/272/data` · 역량: 수리·논리력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 신약개발연구원의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 의약품 개발을 위한 국내·외 각종 전문 자료와 정보를 수집하여 분석합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1101-experience"></a>
### 신용관련추심원 — 가상 창구 요청과 문서 확인

- 직업: `career-net-1101` · 시나리오 `career-net-1101-experience` `v001`.
- 원본 위치: `/items/273/data` · 역량: 대인관계능력.
- 장소 제안: 금융 창구 · `PRM-056 v001` · [PAN-056 v001](../../../images/original/panoramas/PAN-056/v001/prm-056-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 신용관련추심원의 업무 표현과 금융 창구의 고객이 금융 서류를 제출하고 창구 서비스를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 신용관련추심원은 은행이나 카드사 등 금융기관의 채권관리부서 또는 신용정보회사에 고용되어 채무자의 미납된 빚을 받아내는 업무를 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 트레이 · CND-049 | 트레이에서 요청 종류별 모형 문서 분류 | 요청별 필수 문서 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | PC에서 가상 입력 정보와 제출 자료 대조 | 가상 기록 필드 일치 | 관찰·검사 |
| 3 | 서비스 카운터 · CND-023 | 창구에서 빠진 정보를 질문하고 결과 요약 | 필수 정보 확인·수신 응답 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서비스 카운터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-231-experience"></a>
### 신용조사원 — 가상 창구 요청과 문서 확인

- 직업: `career-net-231` · 시나리오 `career-net-231-experience` `v001`.
- 원본 위치: `/items/274/data` · 역량: 수리·논리력.
- 장소 제안: 금융 창구 · `PRM-056 v001` · [PAN-056 v001](../../../images/original/panoramas/PAN-056/v001/prm-056-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 신용조사원의 업무 표현과 금융 창구의 고객이 금융 서류를 제출하고 창구 서비스를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 신용조사 대상자의 분석 결과를 바탕으로 조사 개요, 현황, 전망, 재무 상태, 은행거래 상황 등을 기록하는 신용평가 자료를 최종적으로 작성하여 신용조사 의뢰자에게 제공합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 트레이 · CND-049 | 트레이에서 요청 종류별 모형 문서 분류 | 요청별 필수 문서 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | PC에서 가상 입력 정보와 제출 자료 대조 | 가상 기록 필드 일치 | 관찰·검사 |
| 3 | 서비스 카운터 · CND-023 | 창구에서 빠진 정보를 질문하고 결과 요약 | 필수 정보 확인·수신 응답 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서비스 카운터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10027-experience"></a>
### 신재생에너지 전문가 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10027` · 시나리오 `career-net-10027-experience` `v001`.
- 원본 위치: `/items/275/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 신재생에너지 전문가의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 신재생에너지를 이용하여 보다 효율적으로 전기를 생산하고 공급할 수 있는 장비를 개발하고 관리하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-390-experience"></a>
### 신호원 및 수송원 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-390` · 시나리오 `career-net-390-experience` `v001`.
- 원본 위치: `/items/276/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 신호원 및 수송원의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 신호원은 열차 운전원과 연락하여 열차의 운행 계획이나 시간표 등을 확인하고 역내로 진입하는 열차를 관찰하면서 연결선로와 신호기를 점검합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-20-experience"></a>
### 심리학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-20` · 시나리오 `career-net-20-experience` `v001`.
- 원본 위치: `/items/277/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 심리학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 지능, 능력, 적성, 인성, 기타 인간 행동을 측정하는 검사를 개발하고 시행하며, 검사 자료를 분석하고 해석합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-271-experience"></a>
### 아나운서 — 방송 입력을 확인하고 신호에 맞춰 시작

- 직업: `career-net-271` · 시나리오 `career-net-271-experience` `v001`.
- 원본 위치: `/items/278/data` · 역량: 언어능력.
- 장소 제안: 방송 스튜디오 · `PRM-031 v001` · [PAN-031 v001](../../../images/original/panoramas/PAN-031/v001/prm-031-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 아나운서의 업무 표현과 방송 스튜디오의 진행자가 음성과 영상을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 아나운서는 라디오와 텔레비전 방송을 통하여 각종 정보를 전달하고 프로그램을 진행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 암 · CND-116 | 마이크 암을 표시 위치로 맞춤 | 위치 허용 범위 충족 | 측정·조절 |
| 2 | 소형 오디오 콘솔 · CND-118 | 오디오 콘솔의 가상 레벨을 목표에 조절 | 가상 레벨 구간 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라의 큐 신호에 맞춰 녹화 입력 | 큐 입력 허용 시간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 암 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 오디오 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10057-experience"></a>
### 아동청소년시설보호사 — 생활 요청을 확인하고 이동 환경 점검

- 직업: `career-net-10057` · 시나리오 `career-net-10057-experience` `v001`.
- 원본 위치: `/items/279/data` · 역량: 신체·운동능력.
- 장소 제안: 요양실 · `PRM-017 v001` · [PAN-017 v001](../../../images/original/panoramas/PAN-017/v001/prm-017-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 아동청소년시설보호사의 업무 표현과 요양실의 생활 지원과 이동 보조를 받으며 머무는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 아동청소년시설보호사는 교정 시설에 거주하고 있는 아동 및 청소년을 관리, 감독하고 특별 활동을 제공합니다.
- 체험의 업무 자료: 이용자 요청·물품 구역과 점검 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보조 손잡이 · CND-070 | 보조 손잡이에서 가상 점검표와 다른 상태 확인 | 삽입된 위험 표시 확인 | 관찰·검사 |
| 2 | 휠체어 · CND-069 | 휠체어를 표시된 대기 위치로 옮겨 동선 확보 | 동선·대기 위치 조건 충족 | 조립·배치 |
| 3 | 침대 옆 탁자 · CND-045 | 탁자에서 이용자의 요청을 확인하고 담당자에게 인계 | 요청·조치·인계 확인 응답 | 대화·응대 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보조 손잡이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휠체어 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 침대 옆 탁자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-475-experience"></a>
### 아이티(IT)교육강사 — 학습자의 이해를 확인하고 설명하기

- 직업: `career-net-475` · 시나리오 `career-net-475-experience` `v001`.
- 원본 위치: `/items/280/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 방문 학습 공간 · `PRM-059 v001` · [PAN-059 v001](../../../images/original/panoramas/PAN-059/v001/prm-059-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 아이티(IT)교육강사의 업무 표현과 방문 학습 공간의 가정에서 교사와 학습자가 교재를 함께 보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 아이티(IT)교육강사는 수강생들에게 컴퓨터 정보처리 기술이나 기타 컴퓨터 프로그램을 능숙하게 활용하기 위한 방법과 이론 등을 설명하거나 가르칩니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 사례 풀이의 오류 위치 확인 | 오류 지점 식별 | 관찰·검사 |
| 2 | 필기구 · CND-209 | 필기구 UI로 풀이 설명 순서 구성 | 설명 필수 단계 포함 | 제작·표현 |
| 3 | 업무 책상 · CND-004 | 책상에서 확인 질문과 다음 활동 합의 | 학습자의 이해 확인과 목표 합의 | 대화·응대 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 필기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-474-experience"></a>
### 아이티(IT)기술영업원 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-474` · 시나리오 `career-net-474-experience` `v001`.
- 원본 위치: `/items/281/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 아이티(IT)기술영업원의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객에게 IT 기술 제품(하드웨어 또는 소프트웨어)의 기능과 성능, 사용 방법 등에 대해 조언하고 기존 시스템과 이후 최신화될 기술 관련 문제에 대하여 상담합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10073-experience"></a>
### 아쿠아리스트 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-10073` · 시나리오 `career-net-10073-experience` `v001`.
- 원본 위치: `/items/282/data` · 역량: 자연친화력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 아쿠아리스트의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 아쿠아리스트는 수중생물을 인공적인 환경인 수족관 내에서 기르고 관리하는 업무를 수행합니다.
- 체험의 업무 자료: 가상 개체 ID·관리 요청과 용품 구분.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-347-experience"></a>
### 악기수리원 및 조율사 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-347` · 시나리오 `career-net-347-experience` `v001`.
- 원본 위치: `/items/283/data` · 역량: 음악능력.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 악기수리원 및 조율사의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 악기수리원은 악기를 연주 등을 통해 소리를 점검하여 파손된 부위를 확인한 후 결함이 있는 부분을 수리하고 결함이 있는 부품을 제거하거나 교체합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-318-experience"></a>
### 악기제조원 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-318` · 시나리오 `career-net-318-experience` `v001`.
- 원본 위치: `/items/284/data` · 역량: 음악능력.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 악기제조원의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 악기 설계 도면이나 작업명세서를 통해 제작할 악기의 형태를 파악하고, 필요한 재료 및 공구를 준비하여 악기를 제작합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-21-experience"></a>
### 안경사 — 가상 방문 기록을 확인하고 설명 준비

- 직업: `career-net-21` · 시나리오 `career-net-21-experience` `v001`.
- 원본 위치: `/items/285/data` · 역량: 대인관계능력.
- 장소 제안: 진료실 · `PRM-008 v001` · [PAN-008 v001](../../../images/original/panoramas/PAN-008/v001/prm-008-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 안경사의 업무 표현과 진료실의 진료 상담과 기본 상태 확인을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객의 시력, 난시, 안질환 등을 확인한 후 교정 도수를 결정하고, 적합한 안경 렌즈나 콘택트렌즈를 선별하며, 고객의 눈 상태에 대해 설명합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 의료 모니터 · CND-042 | 의료 모니터에서 기록 ID와 요청 기록 대조 | 기록 ID·누락 항목 식별 | 관찰·검사 |
| 2 | 진찰·처치 침대 · CND-041 | 진찰 침대 옆 UI에서 방문자의 설명을 듣고 확인 질문 | 필수 질문과 설명 확인 | 대화·응대 |
| 3 | 업무 책상 · CND-004 | 책상에서 전달 기록을 필수 항목별로 정리 | 인계 기록 필드 충족 | 분류·선별 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 진찰·처치 침대 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1107-experience"></a>
### 안마사 — 가상 동작을 비교하고 연습 도구 준비

- 직업: `career-net-1107` · 시나리오 `career-net-1107-experience` `v001`.
- 원본 위치: `/items/286/data` · 역량: 대인관계능력.
- 장소 제안: 운동 지도실 · `PRM-048 v001` · [PAN-048 v001](../../../images/original/panoramas/PAN-048/v001/prm-048-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 안마사의 업무 표현과 운동 지도실의 지도자와 이용자가 자세·동작을 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 안마사는 손이나 기구를 이용하여 환자나 고객의 근육을 두드리거나 주물러서 혈액순환을 원활히 하고 육체의 피로를 경감시키는 일을 합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 자세 확인용 독립 거울 · CND-186 | 거울에서 사례 동작의 차이 확인 | 사례 차이 지점 식별 | 관찰·검사 |
| 2 | 낮은 스텝 · CND-184 | 낮은 스텝을 가상 훈련 위치에 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 소형 아령 · CND-185 | 아령 모형의 선택 값을 사례 목표에 맞춤 | 교육용 목표 구간 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 자세 확인용 독립 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 스텝 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 아령 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-966-experience"></a>
### 안무가 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-966` · 시나리오 `career-net-966-experience` `v001`.
- 원본 위치: `/items/287/data` · 역량: 신체·운동능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 안무가의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 안무가는 무대, 영화, 텔레비전 등의 공연을 위해 공연의 주제에 맞춰 춤을 고안하고, 무용수들에게 춤을 가르치는 일을 담당합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-100-experience"></a>
### 압연원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-100` · 시나리오 `career-net-100-experience` `v001`.
- 원본 위치: `/items/288/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 압연원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 압연 과정을 거쳐 생산된 제품이 적절하게 가공되었는지를 검사합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10060-experience"></a>
### 애견테라피스트 — 동물 관리 요청과 준비 상태 확인

- 직업: `career-net-10060` · 시나리오 `career-net-10060-experience` `v001`.
- 원본 위치: `/items/289/data` · 역량: 자기성찰능력.
- 장소 제안: 동물 관리실 · `PRM-043 v001` · [PAN-043 v001](../../../images/original/panoramas/PAN-043/v001/prm-043-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 애견테라피스트의 업무 표현과 동물 관리실의 동물을 돌보고 용품을 정리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 애견테라피스트는 반려동물의 질병이나 마음의 상처를 예방하고 건강을 유지하는 방법에 대해 조언해 줍니다.
- 체험의 업무 자료: 가상 개체 ID·관리 요청과 용품 구분.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 운반 케이지 · CND-164 | 케이지 옆 UI에서 보호자 요청·개체 ID 확인 | 개체·요청 확인 | 대화·응대 |
| 2 | 먹이 그릇 · CND-165 | 먹이 그릇을 개체 라벨별로 분류 | 라벨·구역 일치 | 분류·선별 |
| 3 | 세척대 · CND-036 | 세척대에서 모형 용품 관리 단계를 수행 | 가상 정돈·세척 단계 순서 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 운반 케이지 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 먹이 그릇 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세척대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-920-experience"></a>
### 애니메이션기획자 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-920` · 시나리오 `career-net-920-experience` `v001`.
- 원본 위치: `/items/290/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 애니메이션기획자의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 애니메이션기획자는 애니메이션의 제작에 필요한 각종 업무를 기획하고 조정하는 일을 합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-922-experience"></a>
### 애니메이션작가 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-922` · 시나리오 `career-net-922-experience` `v001`.
- 원본 위치: `/items/291/data` · 역량: 언어능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 애니메이션작가의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국내외의 다양한 자료를 읽거나 조사하고, 애니메이션 시장의 분위기를 파악하여 새로운 작품 소재를 찾아냅니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-441-experience"></a>
### 애니메이터 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-441` · 시나리오 `career-net-441-experience` `v001`.
- 원본 위치: `/items/292/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 애니메이터의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국내외 시장 조사를 하여 만들어야 할 애니메이션의 소재나 주제를 결정하고, 애니메이션 제작에 필요한 사람들을 모읍니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10065-experience"></a>
### 야외활동지도사 — 참여 조건에 맞는 공동 활동 준비

- 직업: `career-net-10065` · 시나리오 `career-net-10065-experience` `v001`.
- 원본 위치: `/items/293/data` · 역량: 대인관계능력.
- 장소 제안: 복지 활동실 · `PRM-016 v001` · [PAN-016 v001](../../../images/original/panoramas/PAN-016/v001/prm-016-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 야외활동지도사의 업무 표현과 복지 활동실의 소규모 집단이 공동 활동을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 야외활동에 필요한 안전시설을 설치하고 이를 관리합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 활동 교구 · CND-066 | 활동 교구에서 참여자 조건에 맞는 물건 선택 | 참여 조건·교구 기능 일치 | 분류·선별 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에서 활동 순서와 역할을 구성 | 필수 역할·단계 누락 없음 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장 물품을 안전한 접근 위치에 배치 | 위치·접근 범위 충족 | 조립·배치 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 활동 교구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-23-experience"></a>
### 약사 및 한약사 — 가상 방문 기록을 확인하고 설명 준비

- 직업: `career-net-23` · 시나리오 `career-net-23-experience` `v001`.
- 원본 위치: `/items/294/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 진료실 · `PRM-008 v001` · [PAN-008 v001](../../../images/original/panoramas/PAN-008/v001/prm-008-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 약사 및 한약사의 업무 표현과 진료실의 진료 상담과 기본 상태 확인을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 약사는 의사의 처방전이나 공인된 조제 방법에 의해 약을 조제하고, 환자나 보호자를 대상으로 질병 치료와 건강 유지에 대한 상담 업무를 수행하며, 한약사는 한약 및 한약제제의 생산, 제조, 조제, 유통, 가공, 연구, 판매 등의 업무를 수행합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 의료 모니터 · CND-042 | 의료 모니터에서 기록 ID와 요청 기록 대조 | 기록 ID·누락 항목 식별 | 관찰·검사 |
| 2 | 진찰·처치 침대 · CND-041 | 진찰 침대 옆 UI에서 방문자의 설명을 듣고 확인 질문 | 필수 질문과 설명 확인 | 대화·응대 |
| 3 | 업무 책상 · CND-004 | 책상에서 전달 기록을 필수 항목별로 정리 | 인계 기록 필드 충족 | 분류·선별 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 진찰·처치 침대 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-187-experience"></a>
### 양식원 — 가상 사육 요청에 맞게 용품 준비

- 직업: `career-net-187` · 시나리오 `career-net-187-experience` `v001`.
- 원본 위치: `/items/295/data` · 역량: 자연친화력.
- 장소 제안: 축사 · `PRM-042 v001` · [PAN-042 v001](../../../images/original/panoramas/PAN-042/v001/prm-042-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 양식원의 업무 표현과 축사의 가축의 생활과 사료 공급을 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 먹이 수급 계획에 따라 먹이를 공급하고 양식장을 관찰하여 양식한 생물의 성장 상태, 각종 병충해, 해상의 변화를 수시로 검사합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 사료 통 · CND-162 | 사료 통의 라벨을 요청 개체 기록과 대조 | 개체 ID·라벨 일치 | 분류·선별 |
| 2 | 급이통 · CND-159 | 급이통의 모형 양을 표시 눈금에 조절 | 교육용 눈금 충족 | 측정·조절 |
| 3 | 물통 · CND-160 | 물통에서 가상 점검표의 누락 항목 확인 | 점검 누락 식별·기록 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 사료 통 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 급이통 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 물통 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10110-experience"></a>
### 양자 컴퓨팅 기술자 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-10110` · 시나리오 `career-net-10110-experience` `v001`.
- 원본 위치: `/items/296/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 양자 컴퓨팅 기술자의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 양자 컴퓨팅 기술자는 양자 물리학의 지식을 이용해서 기존 컴퓨터보다 빠르게 계산할 수 있는 양자 컴퓨터를 개발하고 운용합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-164-experience"></a>
### 양장사 및 양복사 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-164` · 시나리오 `career-net-164-experience` `v001`.
- 원본 위치: `/items/297/data` · 역량: 손재능.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 양장사 및 양복사의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 양장사 및 양복사는 고객의 요구에 따라 여러 디자인의 의복을 제작합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-386-experience"></a>
### 언어치료사 — 가상 동작을 비교하고 연습 도구 준비

- 직업: `career-net-386` · 시나리오 `career-net-386-experience` `v001`.
- 원본 위치: `/items/298/data` · 역량: 대인관계능력.
- 장소 제안: 운동 지도실 · `PRM-048 v001` · [PAN-048 v001](../../../images/original/panoramas/PAN-048/v001/prm-048-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 언어치료사의 업무 표현과 운동 지도실의 지도자와 이용자가 자세·동작을 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 언어치료사는 언어장애의 증상과 원인을 진단하고, 이에 대한 치료 계획을 세워 환자를 치료합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 자세 확인용 독립 거울 · CND-186 | 거울에서 사례 동작의 차이 확인 | 사례 차이 지점 식별 | 관찰·검사 |
| 2 | 낮은 스텝 · CND-184 | 낮은 스텝을 가상 훈련 위치에 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 소형 아령 · CND-185 | 아령 모형의 선택 값을 사례 목표에 맞춤 | 교육용 목표 구간 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 자세 확인용 독립 거울 / noncommon / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 낮은 스텝 / noncommon / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 소형 아령 / noncommon / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-272-experience"></a>
### 언어학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-272` · 시나리오 `career-net-272-experience` `v001`.
- 원본 위치: `/items/299/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 언어학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고어와 현대어에 대한 비교연구를 통해 언어의 기원, 구조, 진화를 연구하고, 언어의 어족과 기원에 따라 고대 및 현대의 불명료한 언어를 분류하고 분석합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-995-experience"></a>
### 에너지공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-995` · 시나리오 `career-net-995-experience` `v001`.
- 원본 위치: `/items/300/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 에너지공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 에너지공학기술자는 에너지 사업을 위한 기술상의 조건을 분석하며 이에 필요한 시스템 장비를 설계, 계획, 조직화합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10016-experience"></a>
### 여행 기획자 — 집결 위치와 이동 안내 준비

- 직업: `career-net-10016` · 시나리오 `career-net-10016-experience` `v001`.
- 원본 위치: `/items/301/data` · 역량: 대인관계능력.
- 장소 제안: 안내 집결 지점 · `PRM-069 v001` · [PAN-069 v001](../../../images/original/panoramas/PAN-069/v001/prm-069-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 여행 기획자의 업무 표현과 안내 집결 지점의 안내자가 사람들을 모아 경로를 설명하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 여행 기획자는 관광에 대한 지식을 바탕으로 국내 여행이나 해외여행 상품을 개발하는 일을 합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 지도 거치대 · CND-224 | 지도 거치대에서 가상 이동 경로 계획 | 가상 동선·시간 제약 충족 | 계획·배분 |
| 2 | 안내판 · CND-205 | 안내판에서 참여자의 질문에 맞는 안내 선택 | 질문 의도·최신 위치 안내 | 대화·응대 |
| 3 | 여행 가방 · CND-221 | 가방에서 일정에 맞는 준비물 선택 | 준비물과 일정 조건 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 지도 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 안내판 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 여행 가방 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-626-experience"></a>
### 여행상품개발원 — 집결 위치와 이동 안내 준비

- 직업: `career-net-626` · 시나리오 `career-net-626-experience` `v001`.
- 원본 위치: `/items/302/data` · 역량: 대인관계능력.
- 장소 제안: 안내 집결 지점 · `PRM-069 v001` · [PAN-069 v001](../../../images/original/panoramas/PAN-069/v001/prm-069-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 여행상품개발원의 업무 표현과 안내 집결 지점의 안내자가 사람들을 모아 경로를 설명하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 여행지로 활성화되지 않은 지역을 찾아내어 현지답사를 한 다음, 여행에 필요한 상황과 조건을 조사 및 분석하여 새로운 여행지를 개발하고 상품화합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 지도 거치대 · CND-224 | 지도 거치대에서 가상 이동 경로 계획 | 가상 동선·시간 제약 충족 | 계획·배분 |
| 2 | 안내판 · CND-205 | 안내판에서 참여자의 질문에 맞는 안내 선택 | 질문 의도·최신 위치 안내 | 대화·응대 |
| 3 | 여행 가방 · CND-221 | 가방에서 일정에 맞는 준비물 선택 | 준비물과 일정 조건 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 지도 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 안내판 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 여행 가방 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-388-experience"></a>
### 여행안내원 — 집결 위치와 이동 안내 준비

- 직업: `career-net-388` · 시나리오 `career-net-388-experience` `v001`.
- 원본 위치: `/items/303/data` · 역량: 대인관계능력.
- 장소 제안: 안내 집결 지점 · `PRM-069 v001` · [PAN-069 v001](../../../images/original/panoramas/PAN-069/v001/prm-069-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 여행안내원의 업무 표현과 안내 집결 지점의 안내자가 사람들을 모아 경로를 설명하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 여행 중에 사고가 발생한 경우 본사와 연락하여 신속하게 해결하고, 여행이 끝난 후 여행의 문제점 및 개선점을 확인하여 이후 여행 계획을 세울 때 참고합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 지도 거치대 · CND-224 | 지도 거치대에서 가상 이동 경로 계획 | 가상 동선·시간 제약 충족 | 계획·배분 |
| 2 | 안내판 · CND-205 | 안내판에서 참여자의 질문에 맞는 안내 선택 | 질문 의도·최신 위치 안내 | 대화·응대 |
| 3 | 여행 가방 · CND-221 | 가방에서 일정에 맞는 준비물 선택 | 준비물과 일정 조건 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 지도 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 안내판 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 여행 가방 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-273-experience"></a>
### 역사학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-273` · 시나리오 `career-net-273-experience` `v001`.
- 원본 위치: `/items/304/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 역사학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 역사학연구원은 선사시대부터 현대에 이르기까지 정치, 경제, 사회, 문화 등 인간 활동에 대해 조사하고 그와 관련한 역사적 사실을 기록하고 연구합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-320-experience"></a>
### 연극연출가 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-320` · 시나리오 `career-net-320-experience` `v001`.
- 원본 위치: `/items/305/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 연극연출가의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 연극연출가는 한 편의 연극을 연출하기 위해 희곡 작품의 주제, 성격 등을 분석하고, 연기자들과 스텝들을 지휘 및 감독합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-189-experience"></a>
### 연근해 어부 및 해녀 — 갑판 모형의 준비 상태 확인

- 직업: `career-net-189` · 시나리오 `career-net-189-experience` `v001`.
- 원본 위치: `/items/306/data` · 역량: 자연친화력.
- 장소 제안: 선박 갑판 · `PRM-044 v001` · [PAN-044 v001](../../../images/original/panoramas/PAN-044/v001/prm-044-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 연근해 어부 및 해녀의 업무 표현과 선박 갑판의 선원이 외부 갑판 설비를 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 연근해 어부 및 해녀는 수산물의 서식지와 특징에 대한 지식을 바탕으로 가까운 바다에서 물고기, 굴, 조개 또는 기타 형태의 물속 동식물을 잡습니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 구명환 · CND-168 | 구명환의 가상 점검 항목 확인 | 점검 결함 식별 | 관찰·검사 |
| 2 | 밧줄 코일 · CND-169 | 밧줄 코일을 지정 위치로 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 계류 장치 · CND-170 | 계류 장치 모형에서 교육용 순서 선택 | 모형 훈련 순서 일치 | 순서·절차 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 구명환 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 밧줄 코일 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 계류 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-303-experience"></a>
### 연기자 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-303` · 시나리오 `career-net-303-experience` `v001`.
- 원본 위치: `/items/307/data` · 역량: 창의력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 연기자의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 연기자는 연극, 영화, TV 드라마에 등장하는 인물의 배역을 맡아 출연하여 대본과 감독의 연출에 따라 연기합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-321-experience"></a>
### 연예인매니저 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-321` · 시나리오 `career-net-321-experience` `v001`.
- 원본 위치: `/items/308/data` · 역량: 대인관계능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 연예인매니저의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 연예인매니저는 가수, 탤런트, 영화배우, 개그맨 등 연예인들의 방송 출연 등 연예 활동과 관련된 모든 일정을 계획 및 관리하는 일을 담당합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-317-experience"></a>
### 연주가 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-317` · 시나리오 `career-net-317-experience` `v001`.
- 원본 위치: `/items/309/data` · 역량: 음악능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 연주가의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 음반 제작을 위해 녹음에 참여하며, 악기를 조율하고 악보를 직접 편곡하기도 합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-101-experience"></a>
### 영사기사 — 소재를 골라 짧은 영상 흐름 완성

- 직업: `career-net-101` · 시나리오 `career-net-101-experience` `v001`.
- 원본 위치: `/items/310/data` · 역량: 예술시각능력.
- 장소 제안: 영상 편집실 · `PRM-032 v001` · [PAN-032 v001](../../../images/original/panoramas/PAN-032/v001/prm-032-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 영사기사의 업무 표현과 영상 편집실의 영상과 소리를 검토하고 편집하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 영화의 상영이 끝난 다음에는 필름을 되감고, 필름의 손상 여부를 확인해 이를 수선합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 미디어 보관함 · CND-121 | 미디어 보관함에서 요청 장면 선택 | 소재 ID·권장 용도 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 모니터에서 컷의 순서·길이를 편집 | 필수 장면·순서 충족 | 제작·표현 |
| 3 | 헤드폰 · CND-117 | 헤드폰에서 가상 음성·장면 동기 오류 확인 | 삽입된 동기 오류 표시·수정 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 미디어 보관함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 헤드폰 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-169-experience"></a>
### 영양사 — 주문에 맞게 조리 준비 순서 맞추기

- 직업: `career-net-169` · 시나리오 `career-net-169-experience` `v001`.
- 원본 위치: `/items/311/data` · 역량: 대인관계능력.
- 장소 제안: 주방 · `PRM-024 v001` · [PAN-024 v001](../../../images/original/panoramas/PAN-024/v001/prm-024-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 영양사의 업무 표현과 주방의 식재료 준비에서 조리와 담기까지 이어지는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 영양사는 건강 증진 및 질병 치료를 목적으로 영양 기법 및 응용에 관하여 연구개발 하고 전문적인 영양 서비스를 제공합니다.
- 체험의 업무 자료: 가상 주문·재료 구분과 준비 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 냉장고 · CND-090 | 냉장고에서 주문과 재료 라벨 대조 | 재료·주문·구역 구분 일치 | 분류·선별 |
| 2 | 조리대 · CND-088 | 조리대에서 가상 조리 단계를 순서대로 배치 | 가상 레시피 단계 일치 | 순서·절차 |
| 3 | 가열 기구 · CND-089 | 가열 기구를 교육용 표시 범위에 조절 | 훈련용 눈금 범위 충족 | 측정·조절 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 냉장고 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조리대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 가열 기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-928-experience"></a>
### 영업원 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-928` · 시나리오 `career-net-928-experience` `v001`.
- 원본 위치: `/items/312/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 영업원의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 영업원은 아직 제품이나 서비스에 대해 구매 의사가 없는 사람이 구매를 할 수 있도록 권하거나 판매합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-322-experience"></a>
### 영화감독 — 소재를 골라 짧은 영상 흐름 완성

- 직업: `career-net-322` · 시나리오 `career-net-322-experience` `v001`.
- 원본 위치: `/items/313/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 영상 편집실 · `PRM-032 v001` · [PAN-032 v001](../../../images/original/panoramas/PAN-032/v001/prm-032-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 영화감독의 업무 표현과 영상 편집실의 영상과 소리를 검토하고 편집하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작품의 주제, 성격을 분석하고 제작 방침을 결정합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 미디어 보관함 · CND-121 | 미디어 보관함에서 요청 장면 선택 | 소재 ID·권장 용도 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 모니터에서 컷의 순서·길이를 편집 | 필수 장면·순서 충족 | 제작·표현 |
| 3 | 헤드폰 · CND-117 | 헤드폰에서 가상 음성·장면 동기 오류 확인 | 삽입된 동기 오류 표시·수정 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 미디어 보관함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 헤드폰 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-323-experience"></a>
### 영화기획자 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-323` · 시나리오 `career-net-323-experience` `v001`.
- 원본 위치: `/items/314/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 영화기획자의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 영화기획자는 영화의 기획에서부터 개봉에 이르는 전 과정에 대한 기획과 관리를 담당합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-914-experience"></a>
### 영화시나리오작가 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-914` · 시나리오 `career-net-914-experience` `v001`.
- 원본 위치: `/items/315/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 영화시나리오작가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 영화의 주제를 선택하고 내용에 따른 역사적 사실이나 사건의 과정 등을 세밀하게 조사 및 분석하여 작품의 전체 줄거리를 구상합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-233-experience"></a>
### 외교관 — 출장 요청과 자료를 확인해 전달

- 직업: `career-net-233` · 시나리오 `career-net-233-experience` `v001`.
- 원본 위치: `/items/316/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 출장 업무 공간 · `PRM-068 v001` · [PAN-068 v001](../../../images/original/panoramas/PAN-068/v001/prm-068-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 외교관의 업무 표현과 출장 업무 공간의 이동 중 임시 자리에서 업무를 처리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 부임한 나라의 정치적 사건과 상황을 본국에 보고하며, 경제 통상 정보, 생활 정보 등을 수집 및 분석하여 본국의 정부나 기업에 알립니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 휴대 전화 · CND-222 | 휴대전화에서 상대 요청과 누락 정보 확인 | 요청·언어·목적 확인 | 대화·응대 |
| 2 | 노트북 · CND-012 | 노트북에서 전달 자료와 원문 차이 확인 | 지정 오류·누락 식별 | 관찰·검사 |
| 3 | 문서 파우치 · CND-223 | 파우치에서 목적별 문서 분류 | 목적별 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 휴대 전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 문서 파우치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-234-experience"></a>
### 외환딜러 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-234` · 시나리오 `career-net-234-experience` `v001`.
- 원본 위치: `/items/317/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 외환딜러의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 세계정세 변화, 외환시장 동향 등 금융 관련 정보를 수집하고 분석합니다.
- 체험의 업무 자료: 가상 요청 조건·수량·기간과 설명 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1129-experience"></a>
### 요리배달원 — 주문을 확인하고 맞는 식기·서빙 준비

- 직업: `career-net-1129` · 시나리오 `career-net-1129-experience` `v001`.
- 원본 위치: `/items/318/data` · 역량: 신체·운동능력.
- 장소 제안: 식당 홀 · `PRM-026 v001` · [PAN-026 v001](../../../images/original/panoramas/PAN-026/v001/prm-026-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 요리배달원의 업무 표현과 식당 홀의 손님이 식사하고 직원이 음식을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 음식이 포장되어 나오면 배달 장소를 확인하여 음식을 배달합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 메뉴 거치대 · CND-100 | 메뉴 거치대에서 요청 조건 확인 | 주문·제외 조건 확인 | 대화·응대 |
| 2 | 식기 · CND-098 | 식기에서 주문에 맞는 구성을 선택 | 식기 종류·개수 일치 | 분류·선별 |
| 3 | 배식 보조대 · CND-099 | 배식 보조대에서 제공 순서 확인 | 주문 ID와 제공 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 메뉴 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 식기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 배식 보조대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-102-experience"></a>
### 용접원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-102` · 시나리오 `career-net-102-experience` `v001`.
- 원본 위치: `/items/319/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 용접원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 용접원은 각종 기계나 금속 구조물 및 압력 용기 등을 제작하기 위하여 금속과 비금속 재료를 용접기 등으로 열이나 압력을 가하여 접합합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10114-experience"></a>
### 우주전파예보관 — 관측 장치를 맞추고 기록 오류 확인

- 직업: `career-net-10114` · 시나리오 `career-net-10114-experience` `v001`.
- 원본 위치: `/items/320/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 관측 지점 · `PRM-039 v001` · [PAN-039 v001](../../../images/original/panoramas/PAN-039/v001/prm-039-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 우주전파예보관의 업무 표현과 관측 지점의 설치한 측정 장비로 환경 변화를 관찰하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 흑점, 태양 X선, 태양전파 등의 자료를 이용하여 태양 흑점에 의한 흑점 폭발 현상을 분석하고 예측합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 삼각대 센서 · CND-144 | 삼각대 센서를 표시 방향에 배치 | 위치·방향 일치 | 조립·배치 |
| 2 | 소형 관측 장치 · CND-145 | 관측 장치의 가상 눈금을 조절 | 훈련용 설정 범위 충족 | 측정·조절 |
| 3 | 데이터 기록 기기 · CND-146 | 기록 기기의 이상 데이터 지점을 표시 | 삽입된 이상 지점·기록 일치 | 관찰·검사 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 삼각대 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 관측 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 데이터 기록 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-383-experience"></a>
### 우편물집배원 — 도착 물품과 인계 순서 맞추기

- 직업: `career-net-383` · 시나리오 `career-net-383-experience` `v001`.
- 원본 위치: `/items/321/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 거점 · `PRM-055 v001` · [PAN-055 v001](../../../images/original/panoramas/PAN-055/v001/prm-055-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 우편물집배원의 업무 표현과 운송 거점의 물품 인계와 출발 준비를 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 지정된 순서에 따라 오토바이 또는 차량으로 해당 주소지에 전달하고, 등기 소포 등의 우편물은 전달한 사람에게 직접 전달하여 확인을 받습니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안내판 · CND-205 | 안내판에서 변경된 인계 위치 확인 | 최신 안내 revision 일치 | 관찰·검사 |
| 2 | 보관 상자 · CND-058 | 포장 상자를 수령 ID에 맞게 분류 | 수령 ID·상자 일치 | 분류·선별 |
| 3 | 운반 카트 · CND-016 | 카트의 방문 순서를 가상 동선에 맞춰 계획 | 시간·동선 제약 충족 | 계획·배분 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안내판 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-400-experience"></a>
### 운동감독 — 가상 동작을 비교하고 연습 도구 준비

- 직업: `career-net-400` · 시나리오 `career-net-400-experience` `v001`.
- 원본 위치: `/items/322/data` · 역량: 신체·운동능력.
- 장소 제안: 운동 지도실 · `PRM-048 v001` · [PAN-048 v001](../../../images/original/panoramas/PAN-048/v001/prm-048-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 운동감독의 업무 표현과 운동 지도실의 지도자와 이용자가 자세·동작을 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 팀이나 개인을 관리하고 지도하여 경기에 참가할 운동선수를 훈련시킵니다.
- 체험의 업무 자료: 가상 활동 규칙·도구와 동작 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 자세 확인용 독립 거울 · CND-186 | 거울에서 사례 동작의 차이 확인 | 사례 차이 지점 식별 | 관찰·검사 |
| 2 | 낮은 스텝 · CND-184 | 낮은 스텝을 가상 훈련 위치에 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 소형 아령 · CND-185 | 아령 모형의 선택 값을 사례 목표에 맞춤 | 교육용 목표 구간 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 자세 확인용 독립 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 스텝 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 아령 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-391-experience"></a>
### 운동경기심판 — 경기 모형의 동작과 기록 확인

- 직업: `career-net-391` · 시나리오 `career-net-391-experience` `v001`.
- 원본 위치: `/items/323/data` · 역량: 신체·운동능력.
- 장소 제안: 경기 구역 · `PRM-049 v001` · [PAN-049 v001](../../../images/original/panoramas/PAN-049/v001/prm-049-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 운동경기심판의 업무 표현과 경기 구역의 하나의 작은 구기 경기 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 운동경기심판은 각종 운동경기의 규칙을 적용하여 경기를 진행하는 일을 담당합니다.
- 체험의 업무 자료: 가상 활동 규칙·도구와 동작 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공 · CND-189 | 공의 이동 경로를 입력으로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 2 | 작은 골대 한 쌍 · CND-188 | 골대 모형을 규칙 카드 위치에 맞춤 | 규칙 카드 위치 일치 | 조립·배치 |
| 3 | 빈 점수판 · CND-190 | 점수판에서 사건 순서와 기록 불일치 수정 | 가상 사건·점수 기록 일치 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 골대 한 쌍 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 빈 점수판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-336-experience"></a>
### 운동선수 — 경기 모형의 동작과 기록 확인

- 직업: `career-net-336` · 시나리오 `career-net-336-experience` `v001`.
- 원본 위치: `/items/324/data` · 역량: 신체·운동능력.
- 장소 제안: 경기 구역 · `PRM-049 v001` · [PAN-049 v001](../../../images/original/panoramas/PAN-049/v001/prm-049-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 운동선수의 업무 표현과 경기 구역의 하나의 작은 구기 경기 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 운동선수는 해당 종목의 규칙을 익히고 좋은 성적과 기록을 내기 위해 체력 훈련과 기술 훈련 및 부상 예방 훈련을 합니다.
- 체험의 업무 자료: 가상 활동 규칙·도구와 동작 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공 · CND-189 | 공의 이동 경로를 입력으로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 2 | 작은 골대 한 쌍 · CND-188 | 골대 모형을 규칙 카드 위치에 맞춤 | 규칙 카드 위치 일치 | 조립·배치 |
| 3 | 빈 점수판 · CND-190 | 점수판에서 사건 순서와 기록 불일치 수정 | 가상 사건·점수 기록 일치 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 골대 한 쌍 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 빈 점수판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10010-experience"></a>
### 원격진료 코디네이터 — 가상 방문 자료를 접수하고 기록 확인

- 직업: `career-net-10010` · 시나리오 `career-net-10010-experience` `v001`.
- 원본 위치: `/items/325/data` · 역량: 대인관계능력.
- 장소 제안: 의료 접수실 · `PRM-011 v001` · [PAN-011 v001](../../../images/original/panoramas/PAN-011/v001/prm-011-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 원격진료 코디네이터의 업무 표현과 의료 접수실의 진료 방문객의 접수와 대기를 안내하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환자의 원격진료 서비스 요청에 대응하여 진료를 위해 상담을 하고 관련 내용을 문서로 정리합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 번호표 발급기 · CND-024 | 순번 기기에서 방문 유형 확인 | 방문 유형·순서 일치 | 순서·절차 |
| 2 | 서류 트레이 · CND-049 | 서류 트레이에서 필수 문서 분류 | 필수 문서 누락 없음 | 분류·선별 |
| 3 | 모니터 · CND-005 | 화면에서 방문 기록과 입력 내용을 대조 | 입력 ID와 원문 항목 일치 | 관찰·검사 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 번호표 발급기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1157-experience"></a>
### 원양어부 — 갑판 모형의 준비 상태 확인

- 직업: `career-net-1157` · 시나리오 `career-net-1157-experience` `v001`.
- 원본 위치: `/items/326/data` · 역량: 자연친화력.
- 장소 제안: 선박 갑판 · `PRM-044 v001` · [PAN-044 v001](../../../images/original/panoramas/PAN-044/v001/prm-044-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 원양어부의 업무 표현과 선박 갑판의 선원이 외부 갑판 설비를 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 그물 등의 장비나 미끼를 이용하여 물고기를 잡고, 잡은 고기들을 종류별로 분류합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 구명환 · CND-168 | 구명환의 가상 점검 항목 확인 | 점검 결함 식별 | 관찰·검사 |
| 2 | 밧줄 코일 · CND-169 | 밧줄 코일을 지정 위치로 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 계류 장치 · CND-170 | 계류 장치 모형에서 교육용 순서 선택 | 모형 훈련 순서 일치 | 순서·절차 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 구명환 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 밧줄 코일 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 계류 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-963-experience"></a>
### 원예기술자 — 모종 위치와 가상 재배 환경 맞추기

- 직업: `career-net-963` · 시나리오 `career-net-963-experience` `v001`.
- 원본 위치: `/items/327/data` · 역량: 자연친화력.
- 장소 제안: 온실 · `PRM-041 v001` · [PAN-041 v001](../../../images/original/panoramas/PAN-041/v001/prm-041-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 원예기술자의 업무 표현과 온실의 통제된 재배 환경에서 식물을 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 원예기술자는 새로운 품종의 채소, 화훼 등을 기르고, 재배하고, 관리하는 일을 담당합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모종 트레이 · CND-154 | 모종 트레이에서 요청 모종 선택 | 모종 ID·구획 일치 | 분류·선별 |
| 2 | 환경 센서 · CND-156 | 환경 센서의 가상 기록 변화 확인 | 가상 변화 지점 식별 | 관찰·검사 |
| 3 | 관수 설비 · CND-155 | 관수 설비를 교육용 목표 구간에 조절 | 교육용 설정 범위 충족 | 측정·조절 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모종 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 환경 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관수 설비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-104-experience"></a>
### 원자력연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-104` · 시나리오 `career-net-104-experience` `v001`.
- 원본 위치: `/items/328/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 원자력연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 원자력연구원은 사람들과 산업체에 에너지를 제공하기 위해 사용되는 원자력의 안전한 이용 방법에 대해 연구하고 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-427-experience"></a>
### 웨딩플래너 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-427` · 시나리오 `career-net-427-experience` `v001`.
- 원본 위치: `/items/329/data` · 역량: 대인관계능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 웨딩플래너의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 웨딩플래너는 결혼을 준비하는 사람을 대신하여 결혼식장 준비, 웨딩 사진, 웨딩드레스 예약, 신혼여행의 예약, 혼수품 구입 등 결혼과 관련된 모든 일을 대신하여 계획하고 조언하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-443-experience"></a>
### 웹디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-443` · 시나리오 `career-net-443-experience` `v001`.
- 원본 위치: `/items/330/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 웹디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 웹사이트의 주요 화면을 필요에 따라 갱신하며 웹사이트를 제작할 때 필요한 기술인 HTML5, CSS, Javascript, JSP, ASP, XML 등을 활용하여 웹에 애니메이션이나 특정한 효과를 구현하기도 합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-444-experience"></a>
### 웹마스터 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-444` · 시나리오 `career-net-444-experience` `v001`.
- 원본 위치: `/items/331/data` · 역량: 수리·논리력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 웹마스터의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 웹마스터는 인터넷 웹사이트의 게시판을 관리하거나 사이트상에서 발생한 오류나 문제들을 확인하고 해결하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10052-experience"></a>
### 웹접근성컨설턴트 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-10052` · 시나리오 `career-net-10052-experience` `v001`.
- 원본 위치: `/items/332/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 웹접근성컨설턴트의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 웹접근성컨설턴트는 콘텐츠의 분석, 설계, 개발, 테스트, 실행의 전 과정에서 웹 접근성에 특화하여 웹디자이너 또는 퍼블리셔와 같은 작업자를 교육하거나 개발물을 진단 및 보완하는 컨설팅 서비스를 제공합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10072-experience"></a>
### 웹툰작가 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-10072` · 시나리오 `career-net-10072-experience` `v001`.
- 원본 위치: `/items/333/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 웹툰작가의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 웹툰작가는 스토리의 소재를 찾고, 기획, 취재하며, 콘티(스토리전개도)를 짜서 스케치, 데생, 채색, 편집 등의 작업을 수행 후 웹툰 플랫폼에 제공하는 업무를 수행합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1096-experience"></a>
### 웹프로듀서 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-1096` · 시나리오 `career-net-1096-experience` `v001`.
- 원본 위치: `/items/334/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 웹프로듀서의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 웹프로듀서는 웹사이트 기획, 구축 및 운영, 마케팅 등을 총괄합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1108-experience"></a>
### 위생사 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1108` · 시나리오 `career-net-1108-experience` `v001`.
- 원본 위치: `/items/335/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 위생사의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 관할 지역 내의 오염원 및 취약 지구를 확인하고 각 지역의 물, 해충, 토양 등의 견본을 채취하여 오염 상태를 검사합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1133-experience"></a>
### 유리부착원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-1133` · 시나리오 `career-net-1133-experience` `v001`.
- 원본 위치: `/items/336/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 유리부착원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 유리 부착 작업이 완료된 후에는 잘못된 부분이 없는지 확인하고 수정합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-106-experience"></a>
### 유리제품제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-106` · 시나리오 `career-net-106-experience` `v001`.
- 원본 위치: `/items/337/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 유리제품제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 성형 작업을 마친 유리 제품을 냉각한 다음, 완성된 유리 제품의 품질과 결함 등을 검사합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-24-experience"></a>
### 유전공학연구원 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-24` · 시나리오 `career-net-24-experience` `v001`.
- 원본 위치: `/items/338/data` · 역량: 수리·논리력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 유전공학연구원의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 유전자를 인위적으로 재조합하여 새로운 품종을 개발하거나 유전질환, 암, 노화, 치매, 에이즈 등과 같은 질병의 유발 원인에 대해 연구합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10061-experience"></a>
### 유전상담사 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10061` · 시나리오 `career-net-10061-experience` `v001`.
- 원본 위치: `/items/339/data` · 역량: 대인관계능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 유전상담사의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환자의 유전자 검사를 통해 질환을 확인합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10104-experience"></a>
### 유전자 재조합 식품 전문가 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-10104` · 시나리오 `career-net-10104-experience` `v001`.
- 원본 위치: `/items/340/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 유전자 재조합 식품 전문가의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 유전자 재조합 식품의 안전성을 검사하고 관리합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-190-experience"></a>
### 유제품제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-190` · 시나리오 `career-net-190-experience` `v001`.
- 원본 위치: `/items/341/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 유제품제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 유제품제조원은 식품 가공에 대한 지식을 바탕으로 젖소로부터 짜낸 우유를 살균 가공하여 우유, 치즈, 버터, 아이스크림 등 각종 우유와 관련된 제품을 생산하는 일을 담당합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-395-experience"></a>
### 유치원교사 — 학습자의 오류를 확인하고 활동 준비

- 직업: `career-net-395` · 시나리오 `career-net-395-experience` `v001`.
- 원본 위치: `/items/342/data` · 역량: 대인관계능력, 자기성찰능력.
- 장소 제안: 교실 · `PRM-012 v001` · [PAN-012 v001](../../../images/original/panoramas/PAN-012/v001/prm-012-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 유치원교사의 업무 표현과 교실의 학생들이 교사를 보며 수업하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 등원, 정리 정돈, 평가, 집단활동(토의, 게임, 요리 등) 및 실외활동 진행, 급식 및 간식 제공, 하원,교육과정의 계획 및 운영 등의 일을 합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 잘못 이해한 풀이 지점 확인 | 사례의 오류 지점 일치 | 관찰·검사 |
| 2 | 독립형 칠판 · CND-052 | 칠판에서 설명 순서를 구성 | 핵심 개념·설명 단계 포함 | 제작·표현 |
| 3 | 사물함 · CND-054 | 사물함에서 학습 조건에 맞는 교구 선택 | 학습 조건과 교구 기능 일치 | 분류·선별 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력, 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 칠판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 사물함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-255-experience"></a>
### 은행출납사무원 — 가상 창구 요청과 문서 확인

- 직업: `career-net-255` · 시나리오 `career-net-255-experience` `v001`.
- 원본 위치: `/items/343/data` · 역량: 수리·논리력.
- 장소 제안: 금융 창구 · `PRM-056 v001` · [PAN-056 v001](../../../images/original/panoramas/PAN-056/v001/prm-056-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 은행출납사무원의 업무 표현과 금융 창구의 고객이 금융 서류를 제출하고 창구 서비스를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 은행에서 고객이 맡긴 돈을 예치하고, 고객의 대출을 상담하는 등의 일을 수행하고. 계좌를 개설하고 개인이나 기업으로부터 단기 또는 장기의 자금을 보관하고 위탁합니다.
- 체험의 업무 자료: 가상 요청 조건·수량·기간과 설명 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 트레이 · CND-049 | 트레이에서 요청 종류별 모형 문서 분류 | 요청별 필수 문서 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | PC에서 가상 입력 정보와 제출 자료 대조 | 가상 기록 필드 일치 | 관찰·검사 |
| 3 | 서비스 카운터 · CND-023 | 창구에서 빠진 정보를 질문하고 결과 요약 | 필수 정보 확인·수신 응답 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서비스 카운터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1149-experience"></a>
### 음료제조관련조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1149` · 시나리오 `career-net-1149-experience` `v001`.
- 원본 위치: `/items/344/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 음료제조관련조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 음료제조관련조작원은 음료수나 기타 기호 식품을 생산하는 관련 제조기기 및 장치를 조작합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-917-experience"></a>
### 음반기획자 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-917` · 시나리오 `career-net-917-experience` `v001`.
- 원본 위치: `/items/345/data` · 역량: 음악능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 음반기획자의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 음반기획자는 국외 음반 시장의 상황과 음반 구매자의 요구를 분석하고 제작할 음반의 주제와 내용을 기획하는 일을 합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1431-experience"></a>
### 음악강사 — 학습자의 이해를 확인하고 설명하기

- 직업: `career-net-1431` · 시나리오 `career-net-1431-experience` `v001`.
- 원본 위치: `/items/346/data` · 역량: 음악능력.
- 장소 제안: 방문 학습 공간 · `PRM-059 v001` · [PAN-059 v001](../../../images/original/panoramas/PAN-059/v001/prm-059-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 음악강사의 업무 표현과 방문 학습 공간의 가정에서 교사와 학습자가 교재를 함께 보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 피아노, 바이올린, 기타, 드럼, 가야금, 해금 악기별로 수강생들에게 음악에 관한 이론과 연주법을 가르칩니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 사례 풀이의 오류 위치 확인 | 오류 지점 식별 | 관찰·검사 |
| 2 | 필기구 · CND-209 | 필기구 UI로 풀이 설명 순서 구성 | 설명 필수 단계 포함 | 제작·표현 |
| 3 | 업무 책상 · CND-004 | 책상에서 확인 질문과 다음 활동 합의 | 학습자의 이해 확인과 목표 합의 | 대화·응대 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 필기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-396-experience"></a>
### 음악치료사 — 가상 동작을 비교하고 연습 도구 준비

- 직업: `career-net-396` · 시나리오 `career-net-396-experience` `v001`.
- 원본 위치: `/items/347/data` · 역량: 음악능력.
- 장소 제안: 운동 지도실 · `PRM-048 v001` · [PAN-048 v001](../../../images/original/panoramas/PAN-048/v001/prm-048-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 음악치료사의 업무 표현과 운동 지도실의 지도자와 이용자가 자세·동작을 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 치료상 개선 상황을 기록하여 관리하고, 개인의 변화를 살펴 보면서 추가적인 치료 방안을 모색하여 치료합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 자세 확인용 독립 거울 · CND-186 | 거울에서 사례 동작의 차이 확인 | 사례 차이 지점 식별 | 관찰·검사 |
| 2 | 낮은 스텝 · CND-184 | 낮은 스텝을 가상 훈련 위치에 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 소형 아령 · CND-185 | 아령 모형의 선택 값을 사례 목표에 맞춤 | 교육용 목표 구간 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 자세 확인용 독립 거울 / noncommon / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 낮은 스텝 / noncommon / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 소형 아령 / noncommon / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-915-experience"></a>
### 음향기사 — 소재를 골라 짧은 영상 흐름 완성

- 직업: `career-net-915` · 시나리오 `career-net-915-experience` `v001`.
- 원본 위치: `/items/348/data` · 역량: 음악능력.
- 장소 제안: 영상 편집실 · `PRM-032 v001` · [PAN-032 v001](../../../images/original/panoramas/PAN-032/v001/prm-032-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 음향기사의 업무 표현과 영상 편집실의 영상과 소리를 검토하고 편집하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 음향기사는 세상에 존재하는 수많은 소리들을 이용해 영화나 드라마의 영상과 음원에 잘 어울릴 수 있도록 음향 장비를 다루고 조작하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 미디어 보관함 · CND-121 | 미디어 보관함에서 요청 장면 선택 | 소재 ID·권장 용도 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 모니터에서 컷의 순서·길이를 편집 | 필수 장면·순서 충족 | 제작·표현 |
| 3 | 헤드폰 · CND-117 | 헤드폰에서 가상 음성·장면 동기 오류 확인 | 삽입된 동기 오류 표시·수정 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 미디어 보관함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 헤드폰 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-397-experience"></a>
### 응급구조사 — 가상 작업 구역을 확인하고 도구 준비

- 직업: `career-net-397` · 시나리오 `career-net-397-experience` `v001`.
- 원본 위치: `/items/349/data` · 역량: 신체·운동능력.
- 장소 제안: 처치실 · `PRM-009 v001` · [PAN-009 v001](../../../images/original/panoramas/PAN-009/v001/prm-009-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 응급구조사의 업무 표현과 처치실의 의료진이 준비한 기구로 처치하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 응급처치가 끝난 후 응급 의료시설로 환자를 이송하고, 응급처치 상황과 환자의 처치 내용을 기록하여 담당 의사에게 보고합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 기구 트레이에서 요청 라벨과 맞는 모형 도구 선택 | 도구 라벨·구역 구분 일치 | 분류·선별 |
| 2 | 작업등 · CND-043 | 작업등을 표시된 가상 관찰 영역에 맞춤 | 표시 영역과 조명 방향 일치 | 측정·조절 |
| 3 | 운반 카트 · CND-016 | 카트의 물품을 준비 순서대로 정돈 | 준비 순서·누락 없음 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작업등 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10014-experience"></a>
### 의료 기기 개발 전문가 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10014` · 시나리오 `career-net-10014-experience` `v001`.
- 원본 위치: `/items/350/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 의료 기기 개발 전문가의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 의료 기기 개발 전문가는 기계공학에 대한 지식을 바탕으로 최신 과학기술을 접목한 의료 기기 개발 계획을 수립하고, 환자 모니터, 초음파기기, X선 촬영(X-ray), 자기공명영상(MRI: Magnetic Resonance Imaging) 등의 의료기기를 설계하고 개발합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-19-experience"></a>
### 의료장비기사 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-19` · 시나리오 `career-net-19-experience` `v001`.
- 원본 위치: `/items/351/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 의료장비기사의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 의료 장비를 적절한 장소에 설치하고 신규기기에 대한 설치부터 폐기 시까지 성능 관리와 정비, 안전 점검 등을 수행하며, 의료기기 사용자의 교육을 진행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-467-experience"></a>
### 의료정보시스템개발자 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-467` · 시나리오 `career-net-467-experience` `v001`.
- 원본 위치: `/items/352/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 의료정보시스템개발자의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국내외의 의료정보시스템 개발 흐름 및 우리나라 의료 체계와 관련된 법과 제도를 분석하여 적합한 의료정보시스템을 기획하고 개발합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1142-experience"></a>
### 의복수선원 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-1142` · 시나리오 `career-net-1142-experience` `v001`.
- 원본 위치: `/items/353/data` · 역량: 손재능.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 의복수선원의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객과의 상담 또는 작업지시서에 따라 의류제품의 수선 부위나 수선 방향을 확인합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1143-experience"></a>
### 의복제품검사원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1143` · 시나리오 `career-net-1143-experience` `v001`.
- 원본 위치: `/items/354/data` · 역량: 손재능.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 의복제품검사원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 의류제품의 크기, 상태, 무게별로 가죽이나 직물 등을 검사하여 제품의 품질에 결함이 있는지를 확인하고 등급을 매깁니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-364-experience"></a>
### 이공학계열교수 — 짧은 설명 발표와 장비 준비

- 직업: `career-net-364` · 시나리오 `career-net-364-experience` `v001`.
- 원본 위치: `/items/355/data` · 역량: 수리·논리력.
- 장소 제안: 강의실 · `PRM-014 v001` · [PAN-014 v001](../../../images/original/panoramas/PAN-014/v001/prm-014-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 이공학계열교수의 업무 표현과 강의실의 강사가 설명하고 청중이 듣는 소규모 교육 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 이공학계열교수는 대학에서 이공학계열 과목을 강의하고, 학생들을 지도하며 자신의 전공 분야에 대한 지속적인 연구 활동을 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 발표 화면 · CND-060 | 발표 화면의 개념 카드를 이해 순서대로 배치 | 필수 개념·논리 순서 충족 | 제작·표현 |
| 2 | 강연대 · CND-059 | 강연대에서 청중 질문에 근거를 들어 설명 | 질문 의도·설명 확인 응답 | 대화·응대 |
| 3 | 작은 AV 장치 · CND-061 | AV 장치의 가상 음량을 목표 구간에 조절 | 연습용 음량 범위 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 발표 화면 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 강연대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 AV 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-325-experience"></a>
### 이미지컨설턴트 — 요청 스타일과 준비 물품 확인

- 직업: `career-net-325` · 시나리오 `career-net-325-experience` `v001`.
- 원본 위치: `/items/356/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 미용실 · `PRM-023 v001` · [PAN-023 v001](../../../images/original/panoramas/PAN-023/v001/prm-023-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 이미지컨설턴트의 업무 표현과 미용실의 고객의 머리를 손질하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 이미지컨설턴트는 개인이나 단체의 성격이나 특성을 분석하여 그에 적합한 이미지를 만들어 주는 일을 합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 독립형 거울 · CND-086 | 거울 앞 UI에서 원하는 형태와 불편 사항 확인 | 고객 요청 확인 응답 | 대화·응대 |
| 2 | 운반 카트 · CND-016 | 카트에서 요청에 맞는 모형 도구 선택 | 도구 역할·구역 일치 | 분류·선별 |
| 3 | 세발대 · CND-087 | 세발대에서 가상 준비 단계를 순서대로 선택 | 교육용 준비 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 독립형 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세발대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1121-experience"></a>
### 이용사 — 요청 스타일과 준비 물품 확인

- 직업: `career-net-1121` · 시나리오 `career-net-1121-experience` `v001`.
- 원본 위치: `/items/357/data` · 역량: 손재능.
- 장소 제안: 미용실 · `PRM-023 v001` · [PAN-023 v001](../../../images/original/panoramas/PAN-023/v001/prm-023-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 이용사의 업무 표현과 미용실의 고객의 머리를 손질하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 이용사는 주로 남성 고객을 대상으로 머리카락, 수염을 자르고 손질하는 등의 이용 서비스를 제공합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 독립형 거울 · CND-086 | 거울 앞 UI에서 원하는 형태와 불편 사항 확인 | 고객 요청 확인 응답 | 대화·응대 |
| 2 | 운반 카트 · CND-016 | 카트에서 요청에 맞는 모형 도구 선택 | 도구 역할·구역 일치 | 분류·선별 |
| 3 | 세발대 · CND-087 | 세발대에서 가상 준비 단계를 순서대로 선택 | 교육용 준비 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 독립형 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세발대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-107-experience"></a>
### 인공위성개발원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-107` · 시나리오 `career-net-107-experience` `v001`.
- 원본 위치: `/items/358/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 인공위성개발원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 시장조사와 세계 인공위성개발의 기술 변화 등에 대해 분석하여 인공위성의 기술적 성능의 개선 및 개발에 참고합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10117-experience"></a>
### 인공지능 엔지니어 — 가상 기능의 요구와 테스트 결과 맞추기

- 직업: `career-net-10117` · 시나리오 `career-net-10117-experience` `v001`.
- 원본 위치: `/items/359/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 인공지능 엔지니어의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 인공지능 엔지니어는 기계 데이터를 기반으로 학습하여 인식, 추론, 판단, 분류, 예측할 수 있도록 최적의 학습모델(알고리즘)을 구현합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 사용자 요구와 다른 실행 결과 찾기 | 명시된 요구·결과 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI로 가상 기능 블록 순서·조건 수정 | 필수 기능 블록과 제약 충족 | 제작·표현 |
| 3 | 마우스 · CND-018 | 마우스로 테스트 단서와 수정 대안을 연결해 재실행 | 가상 테스트의 입력·기대 결과 일치 | 진단·해결 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 마우스 / common / AST-007 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 선택 장면의 기존 필수 후보 밖 추가 제안: CND-018. 기존 후보 목록은 자동 수정하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-406-experience"></a>
### 인문계중등학교교사 — 학습자의 오류를 확인하고 활동 준비

- 직업: `career-net-406` · 시나리오 `career-net-406-experience` `v001`.
- 원본 위치: `/items/360/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 교실 · `PRM-012 v001` · [PAN-012 v001](../../../images/original/panoramas/PAN-012/v001/prm-012-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 인문계중등학교교사의 업무 표현과 교실의 학생들이 교사를 보며 수업하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 학교의 교육 계획과 수업 이수 등을 고려하여 자신이 맡은 교과목의 학습안을 설계하고 교과서를 비롯해 시청각 자료 등 다양한 교재를 활용하여 수업을 진행합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 잘못 이해한 풀이 지점 확인 | 사례의 오류 지점 일치 | 관찰·검사 |
| 2 | 독립형 칠판 · CND-052 | 칠판에서 설명 순서를 구성 | 핵심 개념·설명 단계 포함 | 제작·표현 |
| 3 | 사물함 · CND-054 | 사물함에서 학습 조건에 맞는 교구 선택 | 학습 조건과 교구 기능 일치 | 분류·선별 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 칠판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 사물함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-988-experience"></a>
### 인문사회계열교수 — 짧은 설명 발표와 장비 준비

- 직업: `career-net-988` · 시나리오 `career-net-988-experience` `v001`.
- 원본 위치: `/items/361/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 강의실 · `PRM-014 v001` · [PAN-014 v001](../../../images/original/panoramas/PAN-014/v001/prm-014-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 인문사회계열교수의 업무 표현과 강의실의 강사가 설명하고 청중이 듣는 소규모 교육 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 대학교에서 국문학, 영문학, 사학, 철학, 정치학, 경제학, 사회학 등의 과목을 교육합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 발표 화면 · CND-060 | 발표 화면의 개념 카드를 이해 순서대로 배치 | 필수 개념·논리 순서 충족 | 제작·표현 |
| 2 | 강연대 · CND-059 | 강연대에서 청중 질문에 근거를 들어 설명 | 질문 의도·설명 확인 응답 | 대화·응대 |
| 3 | 작은 AV 장치 · CND-061 | AV 장치의 가상 음량을 목표 구간에 조절 | 연습용 음량 범위 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 발표 화면 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 강연대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 AV 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-108-experience"></a>
### 인쇄기조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-108` · 시나리오 `career-net-108-experience` `v001`.
- 원본 위치: `/items/362/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 인쇄기조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작업지시서 또는 주문서에 따라 제작할 인쇄물의 종류, 용지, 잉크, 인쇄 방식, 인쇄량 등을 확인하고, 인쇄판, 인쇄용지 등을 기계에 장착합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-326-experience"></a>
### 인테리어디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-326` · 시나리오 `career-net-326-experience` `v001`.
- 원본 위치: `/items/363/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 인테리어디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 인테리어디자이너는 주택, 사무실, 상가 건물의 내부 환경을 기능과 용도에 맞게 설계하고 장식합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-5-experience"></a>
### 일기예보관 — 관측 장치를 맞추고 기록 오류 확인

- 직업: `career-net-5` · 시나리오 `career-net-5-experience` `v001`.
- 원본 위치: `/items/364/data` · 역량: 수리·논리력.
- 장소 제안: 관측 지점 · `PRM-039 v001` · [PAN-039 v001](../../../images/original/panoramas/PAN-039/v001/prm-039-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 일기예보관의 업무 표현과 관측 지점의 설치한 측정 장비로 환경 변화를 관찰하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 일기예보관은 각종 기상 관측 자료의 분석을 바탕으로 일기예보와 기상현상에 대한 주의보, 경보, 기상 전망을 발표하는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 삼각대 센서 · CND-144 | 삼각대 센서를 표시 방향에 배치 | 위치·방향 일치 | 조립·배치 |
| 2 | 소형 관측 장치 · CND-145 | 관측 장치의 가상 눈금을 조절 | 훈련용 설정 범위 충족 | 측정·조절 |
| 3 | 데이터 기록 기기 · CND-146 | 기록 기기의 이상 데이터 지점을 표시 | 삽입된 이상 지점·기록 일치 | 관찰·검사 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 삼각대 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 관측 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 데이터 기록 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-327-experience"></a>
### 일러스트레이터 — 표현 재료를 고르고 작은 작품 구성

- 직업: `career-net-327` · 시나리오 `career-net-327-experience` `v001`.
- 원본 위치: `/items/365/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 미술 작업실 · `PRM-028 v001` · [PAN-028 v001](../../../images/original/panoramas/PAN-028/v001/prm-028-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 일러스트레이터의 업무 표현과 미술 작업실의 그림을 그리고 작품을 살펴보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 일러스트레이터는 주로 광고나 영상 매체의 그림이나 문양을 도안하고 제작하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 팔레트 도구 · CND-107 | 팔레트 도구에서 표현 목표에 맞는 재료 선택 | 재료 역할과 목표 일치 | 분류·선별 |
| 2 | 빈 캔버스 · CND-105 | 캔버스에 형태와 구도를 구성 | 필수 요소·구도 조건 충족 | 제작·표현 |
| 3 | 이젤 · CND-104 | 이젤에서 작품을 다른 시점으로 확인 | 지정 확인 항목 점검 완료 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 팔레트 도구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 빈 캔버스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이젤 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-362-experience"></a>
### 일반공무원 — 접수 문서를 확인하고 담당자에게 전달

- 직업: `career-net-362` · 시나리오 `career-net-362-experience` `v001`.
- 원본 위치: `/items/366/data` · 역량: 대인관계능력.
- 장소 제안: 행정·문서 처리 사무실 · `PRM-003 v001` · [PAN-003 v001](../../../images/original/panoramas/PAN-003/v001/C-public-administration-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 일반공무원의 업무 표현과 행정·문서 처리 사무실의 기관 내부 담당자가 기록·검토·결재하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 법령과 업무처리 규정에 따라 관련 업무를 계획하고 시행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류철 · CND-022 | 서류철의 문서를 업무 종류별로 분류 | 문서별 분류 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 기록 화면과 문서의 불일치 수정 | 기록과 문서의 필수 항목 일치 | 관찰·검사 |
| 3 | 유선전화 · CND-019 | 전화로 누락 정보를 확인하고 결과 인계 | 확인 질문과 전달 필드 충족 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류철 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 유선전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1440-experience"></a>
### 일반의사 — 가상 방문 기록을 확인하고 설명 준비

- 직업: `career-net-1440` · 시나리오 `career-net-1440-experience` `v001`.
- 원본 위치: `/items/367/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 진료실 · `PRM-008 v001` · [PAN-008 v001](../../../images/original/panoramas/PAN-008/v001/prm-008-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 일반의사의 업무 표현과 진료실의 진료 상담과 기본 상태 확인을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 청진기, 맥박 기록기 등 간단한 의료 기구를 사용하여 환자를 진찰하고 검사하며 결과를 분석하여 치료 및 약물을 처방합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 의료 모니터 · CND-042 | 의료 모니터에서 기록 ID와 요청 기록 대조 | 기록 ID·누락 항목 식별 | 관찰·검사 |
| 2 | 진찰·처치 침대 · CND-041 | 진찰 침대 옆 UI에서 방문자의 설명을 듣고 확인 질문 | 필수 질문과 설명 확인 | 대화·응대 |
| 3 | 업무 책상 · CND-004 | 책상에서 전달 기록을 필수 항목별로 정리 | 인계 기록 필드 충족 | 분류·선별 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 진찰·처치 침대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-941-experience"></a>
### 임상병리사 — 가상 작업 구역을 확인하고 도구 준비

- 직업: `career-net-941` · 시나리오 `career-net-941-experience` `v001`.
- 원본 위치: `/items/368/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 처치실 · `PRM-009 v001` · [PAN-009 v001](../../../images/original/panoramas/PAN-009/v001/prm-009-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 임상병리사의 업무 표현과 처치실의 의료진이 준비한 기구로 처치하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 인체의 기관, 조직, 세포, 혈액, 분비물 등의 여러 가지 검사물에 대해 현미경 등의 기구나 시약을 사용하여 검사, 분석하여 질병의 여부를 확인하고, 혈액형 및 혈구 수 계산 등의 검사 결과를 확인합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 기구 트레이에서 요청 라벨과 맞는 모형 도구 선택 | 도구 라벨·구역 구분 일치 | 분류·선별 |
| 2 | 작업등 · CND-043 | 작업등을 표시된 가상 관찰 영역에 맞춤 | 표시 영역과 조명 방향 일치 | 측정·조절 |
| 3 | 운반 카트 · CND-016 | 카트의 물품을 준비 순서대로 정돈 | 준비 순서·누락 없음 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작업등 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-398-experience"></a>
### 임상심리사 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-398` · 시나리오 `career-net-398-experience` `v001`.
- 원본 위치: `/items/369/data` · 역량: 대인관계능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 임상심리사의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 내담자가 겪는 어려움의 원인을 분석하고 치료 방법, 기간, 강도 등 적절한 치료 계획을 수립합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1158-experience"></a>
### 자동조립라인 및 산업용로봇조작원 — 맞는 부품을 조립하고 완성품 검사

- 직업: `career-net-1158` · 시나리오 `career-net-1158-experience` `v001`.
- 원본 위치: `/items/370/data` · 역량: 손재능.
- 장소 제안: 조립 구역 · `PRM-019 v001` · [PAN-019 v001](../../../images/original/panoramas/PAN-019/v001/prm-019-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 자동조립라인 및 산업용로봇조작원의 업무 표현과 조립 구역의 부품을 순서대로 결합하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 자동조립라인 및 산업용로봇조작원은 생산 현장의 자동 또는 반자동 조립라인을 조작하거나 산업용 로봇을 조작하는 일을 담당한다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 도면에 맞는 부품 선택 | 부품 ID·규격 일치 | 분류·선별 |
| 2 | 공구 거치대 · CND-077 | 공구 거치대의 맞는 공구를 선택해 체결 순서 수행 | 공구·체결 순서 일치 | 순서·절차 |
| 3 | 조립 중인 단순 제품 · CND-078 | 조립 중인 제품을 회전해 결함을 찾아 수정 | 정의된 결함 수정 후 검사 통과 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조립 중인 단순 제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1076-experience"></a>
### 자동차공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1076` · 시나리오 `career-net-1076-experience` `v001`.
- 원본 위치: `/items/371/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 자동차공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 구성부품 및 기관을 설계하고, 공학기술상의 설계와 일치 여부를 확인하기 위하여 부품, 차량의 제조, 개조, 수리 작업을 감독, 조정합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-236-experience"></a>
### 자동차영업원 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-236` · 시나리오 `career-net-236-experience` `v001`.
- 원본 위치: `/items/372/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 자동차영업원의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 자동차의 제품 정보, 경쟁업체, 시장상황에 대한 정보를 수집하고 분석하여 자동차 영업 및 판매 활동에 활용합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-109-experience"></a>
### 자동차정비원 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-109` · 시나리오 `career-net-109-experience` `v001`.
- 원본 위치: `/items/373/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 자동차정비원의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 자동차 정비원은 자동차를 검사, 정비, 수리합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-110-experience"></a>
### 자동차조립원 — 맞는 부품을 조립하고 완성품 검사

- 직업: `career-net-110` · 시나리오 `career-net-110-experience` `v001`.
- 원본 위치: `/items/374/data` · 역량: 손재능.
- 장소 제안: 조립 구역 · `PRM-019 v001` · [PAN-019 v001](../../../images/original/panoramas/PAN-019/v001/prm-019-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 자동차조립원의 업무 표현과 조립 구역의 부품을 순서대로 결합하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 자동차조립원은 각종 자동차의 차체, 외·내장품, 타이어, 유리 등의 부품들을 조립 및 부착하여 자동차를 완성하거나 완성된 자동차 조립품을 검사합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 도면에 맞는 부품 선택 | 부품 ID·규격 일치 | 분류·선별 |
| 2 | 공구 거치대 · CND-077 | 공구 거치대의 맞는 공구를 선택해 체결 순서 수행 | 공구·체결 순서 일치 | 순서·절차 |
| 3 | 조립 중인 단순 제품 · CND-078 | 조립 중인 제품을 회전해 결함을 찾아 수정 | 정의된 결함 수정 후 검사 통과 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조립 중인 단순 제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1089-experience"></a>
### 자연계중등학교교사 — 학습자의 오류를 확인하고 활동 준비

- 직업: `career-net-1089` · 시나리오 `career-net-1089-experience` `v001`.
- 원본 위치: `/items/375/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 교실 · `PRM-012 v001` · [PAN-012 v001](../../../images/original/panoramas/PAN-012/v001/prm-012-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 자연계중등학교교사의 업무 표현과 교실의 학생들이 교사를 보며 수업하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 학교의 교육계획과 수업일수 등을 고려하여 자신이 전담하는 과목의 학습안을 설계하고 교과서를 비롯해 시청각 자료 등 다양한 교재를 활용합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 잘못 이해한 풀이 지점 확인 | 사례의 오류 지점 일치 | 관찰·검사 |
| 2 | 독립형 칠판 · CND-052 | 칠판에서 설명 순서를 구성 | 핵심 개념·설명 단계 포함 | 제작·표현 |
| 3 | 사물함 · CND-054 | 사물함에서 학습 조건에 맞는 교구 선택 | 학습 조건과 교구 기능 일치 | 분류·선별 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 칠판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 사물함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1541-experience"></a>
### 자연과학연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1541` · 시나리오 `career-net-1541-experience` `v001`.
- 원본 위치: `/items/376/data` · 역량: 수리·논리력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 자연과학연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 물리학, 생물학, 화학, 지구과학, 천문학을 연구하여 관련 개념과 이론을 개선하거나 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1441-experience"></a>
### 작가 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-1441` · 시나리오 `career-net-1441-experience` `v001`.
- 원본 위치: `/items/377/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 작가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 영화, 방송, 연극 제작을 위해 작품의 주제를 선택하고 내용에 따른 등장인물의 성격, 시대적 배경, 장소 등을 결정하며 작품을 전개하는 데 필요한 대사 내용, 동작 등을 작성합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-328-experience"></a>
### 작곡가 — 짧은 가상 음악 구간을 구성하고 소리 흐름 확인

- 직업: `career-net-328` · 시나리오 `career-net-328-experience` `v001`.
- 원본 위치: `/items/378/data` · 역량: 음악능력.
- 장소 제안: 영상 편집실 · `PRM-032 v001` · [PAN-032 v001](../../../images/original/panoramas/PAN-032/v001/prm-032-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 작곡가의 업무 표현과 영상 편집실의 영상과 소리를 검토하고 편집하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작곡가는 관현악, 기악, 성악, 대중가요, 영화음악, 광고음악, 애니메이션음악 및 기타 배경음악 등을 만듭니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 제시된 길이·박자 조건의 가상 음형 배치 | 제시한 길이·박자 제약 충족 | 제작·표현 |
| 2 | 헤드폰 · CND-117 | 헤드폰에서 삽입된 박자·구간 누락 확인 | 삽입된 구간 누락 지점 식별 | 관찰·검사 |
| 3 | 스피커 · CND-120 | 스피커의 가상 박자 신호에 맞춰 재생 구간 확인 | 연습용 신호 입력 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 헤드폰 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-401-experience"></a>
### 작업치료사 — 가상 동작을 비교하고 연습 도구 준비

- 직업: `career-net-401` · 시나리오 `career-net-401-experience` `v001`.
- 원본 위치: `/items/379/data` · 역량: 대인관계능력.
- 장소 제안: 운동 지도실 · `PRM-048 v001` · [PAN-048 v001](../../../images/original/panoramas/PAN-048/v001/prm-048-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 작업치료사의 업무 표현과 운동 지도실의 지도자와 이용자가 자세·동작을 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환자의 병력을 근거로 인지 지각 능력, 운동능력, 손 기능 능력 등을 평가하고, 평가에 의거하여 치료 계획을 수립합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 자세 확인용 독립 거울 · CND-186 | 거울에서 사례 동작의 차이 확인 | 사례 차이 지점 식별 | 관찰·검사 |
| 2 | 낮은 스텝 · CND-184 | 낮은 스텝을 가상 훈련 위치에 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 소형 아령 · CND-185 | 아령 모형의 선택 값을 사례 목표에 맞춤 | 교육용 목표 구간 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 자세 확인용 독립 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 스텝 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 아령 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-403-experience"></a>
### 장례지도사 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-403` · 시나리오 `career-net-403-experience` `v001`.
- 원본 위치: `/items/380/data` · 역량: 대인관계능력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 장례지도사의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 장례 절차 및 방법에 대해 고객과 상담하고 이에 대한 정보를 제공합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 검토: 전용 활동 공간이 현재 파노라마 목록에 없음. 선택 장면은 관제·상담·연습 등 한정된 보조 장면 제안이며 현장 대표 공간의 대체 완성본이 아님.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10056-experience"></a>
### 장애인잡코치 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10056` · 시나리오 `career-net-10056-experience` `v001`.
- 원본 위치: `/items/381/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 장애인잡코치의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 상담을 통해 장애인의 기초 정보를 수집하고 각종 검사 및 직업 수행을 위한 정보를 수집합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1102-experience"></a>
### 장학사 — 짧은 설명 발표와 장비 준비

- 직업: `career-net-1102` · 시나리오 `career-net-1102-experience` `v001`.
- 원본 위치: `/items/382/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 강의실 · `PRM-014 v001` · [PAN-014 v001](../../../images/original/panoramas/PAN-014/v001/prm-014-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 장학사의 업무 표현과 강의실의 강사가 설명하고 청중이 듣는 소규모 교육 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 장학사는 행정상의 지휘권, 명령권, 감독권은 가지고 있지 않으나 학교를 주기적으로 시찰하고 교과과정, 교육 방법, 장비 및 기타 사안 등을 평가하고 제반 문제에 대해 교사와 협의하고 조언하는 역할을 담당합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 발표 화면 · CND-060 | 발표 화면의 개념 카드를 이해 순서대로 배치 | 필수 개념·논리 순서 충족 | 제작·표현 |
| 2 | 강연대 · CND-059 | 강연대에서 청중 질문에 근거를 들어 설명 | 질문 의도·설명 확인 응답 | 대화·응대 |
| 3 | 작은 AV 장치 · CND-061 | AV 장치의 가상 음량을 목표 구간에 조절 | 연습용 음량 범위 충족 | 측정·조절 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 발표 화면 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 강연대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 AV 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10055-experience"></a>
### 재능기부코디네이터 — 참여 조건에 맞는 공동 활동 준비

- 직업: `career-net-10055` · 시나리오 `career-net-10055-experience` `v001`.
- 원본 위치: `/items/383/data` · 역량: 자기성찰능력.
- 장소 제안: 복지 활동실 · `PRM-016 v001` · [PAN-016 v001](../../../images/original/panoramas/PAN-016/v001/prm-016-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 재능기부코디네이터의 업무 표현과 복지 활동실의 소규모 집단이 공동 활동을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 재능 기부자와 수혜자 간 연결 시스템 및 프로그램을 기획하여 운영합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 활동 교구 · CND-066 | 활동 교구에서 참여자 조건에 맞는 물건 선택 | 참여 조건·교구 기능 일치 | 분류·선별 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에서 활동 순서와 역할을 구성 | 필수 역할·단계 누락 없음 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장 물품을 안전한 접근 위치에 배치 | 위치·접근 범위 충족 | 조립·배치 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 활동 교구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-112-experience"></a>
### 재료공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-112` · 시나리오 `career-net-112-experience` `v001`.
- 원본 위치: `/items/384/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 재료공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 화학, 물리적 분석 및 기타 연구를 수행하고 재료의 설계, 부식 관리 방법과 공정을 검사하며 기타 절차들에 관해 자문합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-145-experience"></a>
### 재활용 처리 및 소각로 조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-145` · 시나리오 `career-net-145-experience` `v001`.
- 원본 위치: `/items/385/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 재활용 처리 및 소각로 조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 소각로의 중앙통제 장치를 조작해서 일반 및 산업 폐기물을 소각하고, 폐기물 등의 소각이 잘 처리되었는지를 확인합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10045-experience"></a>
### 재활용코디네이터 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-10045` · 시나리오 `career-net-10045-experience` `v001`.
- 원본 위치: `/items/386/data` · 역량: 자연친화력.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 재활용코디네이터의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 재활용 기술자, 재활용 작업자나 자원봉사자 등을 감독하거나 재활용 운영 예산 등 재활용 프로그램이 잘 운영될 수 있도록 관리하고 관련 법률에 대한 위반 사항을 조사합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-113-experience"></a>
### 전공 — 배관 모형을 연결하고 상태 확인

- 직업: `career-net-113` · 시나리오 `career-net-113-experience` `v001`.
- 원본 위치: `/items/387/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 설비 작업 구역 · `PRM-037 v001` · [PAN-037 v001](../../../images/original/panoramas/PAN-037/v001/prm-037-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 전공의 업무 표현과 설비 작업 구역의 배관과 설비를 설치·점검하는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전공은 발전소에서 주택이나 상가, 공장까지 전기가 안전하게 전달되어 사용될 수 있도록 각종 전력시설을 설치하고 수리합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 상자 · CND-137 | 부품 상자에서 연결 규격에 맞는 부품 선택 | 규격·용도 일치 | 분류·선별 |
| 2 | 노출 배관 모형 · CND-135 | 노출 배관 모형의 연결 방향 맞춤 | 위치·방향·연결점 일치 | 조립·배치 |
| 3 | 제어함 · CND-138 | 제어함에서 가상 상태표와 다른 항목 확인 | 가상 오류 항목 식별 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노출 배관 모형 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1146-experience"></a>
### 전기 부품 및 제품 생산직 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1146` · 시나리오 `career-net-1146-experience` `v001`.
- 원본 위치: `/items/388/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 전기 부품 및 제품 생산직의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 완성된 부품들의 품질을 검사하고 결함 사항들을 확인하며, 전기제품의 생산과 관련된 기계 및 장치를 정기적으로 점검합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-114-experience"></a>
### 전기공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-114` · 시나리오 `career-net-114-experience` `v001`.
- 원본 위치: `/items/389/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 전기공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전기공학기술자는 전력, 자동화 및 제어 시스템, 엔지니어링 및 건설, 전기 설비 등의 분야에서 계획 설계 시공 및 감리 업무와 전력시설물의 유지 보수 및 안전관리 업무를 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1145-experience"></a>
### 전기설비조작원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1145` · 시나리오 `career-net-1145-experience` `v001`.
- 원본 위치: `/items/390/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 전기설비조작원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 수리가 필요한 작업 장소의 주전원 스위치 개폐 상태를 확인하고 작업 표시판을 부착합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-378-experience"></a>
### 전문비서 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-378` · 시나리오 `career-net-378-experience` `v001`.
- 원본 위치: `/items/391/data` · 역량: 대인관계능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 전문비서의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전문비서는 상사가 최대한의 업무 성과를 낼 수 있도록 일정을 계획, 관리, 조정하며, 최적의 조건에서 업무를 수행할 수 있도록 돕습니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-25-experience"></a>
### 전문의사 — 가상 방문 기록을 확인하고 설명 준비

- 직업: `career-net-25` · 시나리오 `career-net-25-experience` `v001`.
- 원본 위치: `/items/392/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 진료실 · `PRM-008 v001` · [PAN-008 v001](../../../images/original/panoramas/PAN-008/v001/prm-008-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 전문의사의 업무 표현과 진료실의 진료 상담과 기본 상태 확인을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 의료 검사와 시험을 통해 얻은 자료를 분석하여 환자의 질병과 장애에 대해 처방하고 치료의 범위와 방법, 종류와 순서를 결정합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 의료 모니터 · CND-042 | 의료 모니터에서 기록 ID와 요청 기록 대조 | 기록 ID·누락 항목 식별 | 관찰·검사 |
| 2 | 진찰·처치 침대 · CND-041 | 진찰 침대 옆 UI에서 방문자의 설명을 듣고 확인 질문 | 필수 질문과 설명 확인 | 대화·응대 |
| 3 | 업무 책상 · CND-004 | 책상에서 전달 기록을 필수 항목별로 정리 | 인계 기록 필드 충족 | 분류·선별 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 진찰·처치 침대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1087-experience"></a>
### 전자 부품 및 제품 생산직 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1087` · 시나리오 `career-net-1087-experience` `v001`.
- 원본 위치: `/items/393/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 전자 부품 및 제품 생산직의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전자 부품 및 제품 생산직은 전자장비에 사용되는 부분품을 제조하는 장치를 조작하고 생산과정이 원활히 진행되도록 이에 대한 제반 사항을 관리합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-119-experience"></a>
### 전자공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-119` · 시나리오 `career-net-119-experience` `v001`.
- 원본 위치: `/items/394/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 전자공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 제품을 설계 및 개발하기 위해서는 시장조사를 거쳐 소비자가 원하는 성능, 기능, 디자인 등에 대한 의견 수렴을 하고 경쟁업체 제품 및 세계 동향, 기술 변화 등을 분석한 후 디자인 설계를 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-470-experience"></a>
### 전자상거래전문가 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-470` · 시나리오 `career-net-470-experience` `v001`.
- 원본 위치: `/items/395/data` · 역량: 수리·논리력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 전자상거래전문가의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전자상거래전문가는 사업 기획부터 콘텐츠 개발, 시스템 구성, 서버 관리 및 운영, 상품 구매 및 판매, 마케팅 및 홍보 등을 담당합니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-120-experience"></a>
### 전자장비설치 및 수리원 — 가전 모형의 단서를 보고 점검 준비

- 직업: `career-net-120` · 시나리오 `career-net-120-experience` `v001`.
- 원본 위치: `/items/396/data` · 역량: 손재능.
- 장소 제안: 가정 수리 공간 · `PRM-058 v001` · [PAN-058 v001](../../../images/original/panoramas/PAN-058/v001/prm-058-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 전자장비설치 및 수리원의 업무 표현과 가정 수리 공간의 방문 기술자가 가정용 기기를 점검하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 검사 계기를 이용하여 전자장비의 전기회로, 잘못된 연결이나 결함 부분의 위치를 파악하고 분석한 다음, 장비를 분해하여 마모된 부품은 교체하는 등의 수리 작업을 합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 간단한 가전제품 · CND-207 | 가전제품 모형의 표시 단서로 고장 가설 선택 | 제공 단서와 가설 일치 | 진단·해결 |
| 2 | 공구 가방 · CND-208 | 공구 가방에서 모형 작업에 맞는 도구 선택 | 도구 역할·가상 작업 조건 일치 | 분류·선별 |
| 3 | 부품 트레이 · CND-040 | 부품 트레이에서 교체 요청과 결과 대조 | 부품·완료 기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 간단한 가전제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 가방 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1131-experience"></a>
### 전통건축원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-1131` · 시나리오 `career-net-1131-experience` `v001`.
- 원본 위치: `/items/397/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 전통건축원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전통건축원은 전통 건축기법을 이용하여 한옥, 사원, 궁궐 등의 전통 건축물을 설계하고 시공하는 일을 합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-171-experience"></a>
### 전통식품제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-171` · 시나리오 `career-net-171-experience` `v001`.
- 원본 위치: `/items/398/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 전통식품제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전통식품제조원은 우리나라의 고유 음식인 떡, 한과, 간장, 된장, 김치 등을 만드는 일을 담당합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-404-experience"></a>
### 전화교환원 — 방문객의 요청을 확인하고 접수 완료

- 직업: `career-net-404` · 시나리오 `career-net-404-experience` `v001`.
- 원본 위치: `/items/399/data` · 역량: 대인관계능력.
- 장소 제안: 민원·방문객 접수실 · `PRM-004 v001` · [PAN-004 v001](../../../images/original/panoramas/PAN-004/v001/D-public-reception-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 전화교환원의 업무 표현과 민원·방문객 접수실의 방문객이 대기한 뒤 직원에게 서류를 접수하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전화교환원은 시내, 시외 및 국제 간 혹은 회사 내부의 전화 통화를 연결하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 번호표 발급기 · CND-024 | 번호표 기기에서 업무 종류와 순번 확인 | 업무 종류와 순번 일치 | 순서·절차 |
| 2 | 모니터 · CND-005 | 화면의 신청 정보와 요청을 대조 | 필수 정보 누락 없음 | 관찰·검사 |
| 3 | 서비스 카운터 · CND-023 | 카운터에서 빠진 정보를 질문하고 다음 절차 안내 | 방문객 확인 응답과 안내 목적지 일치 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 번호표 발급기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서비스 카운터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-121-experience"></a>
### 전화설치 및 수리원 — 가전 모형의 단서를 보고 점검 준비

- 직업: `career-net-121` · 시나리오 `career-net-121-experience` `v001`.
- 원본 위치: `/items/400/data` · 역량: 손재능.
- 장소 제안: 가정 수리 공간 · `PRM-058 v001` · [PAN-058 v001](../../../images/original/panoramas/PAN-058/v001/prm-058-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 전화설치 및 수리원의 업무 표현과 가정 수리 공간의 방문 기술자가 가정용 기기를 점검하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전화설치 및 수리원은 이용자의 전화 이전 신청에 따라 전화를 이전하여 설치 및 연결해주거나 전화기의 고장 사항을 수리해 주는 일을 담당합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 간단한 가전제품 · CND-207 | 가전제품 모형의 표시 단서로 고장 가설 선택 | 제공 단서와 가설 일치 | 진단·해결 |
| 2 | 공구 가방 · CND-208 | 공구 가방에서 모형 작업에 맞는 도구 선택 | 도구 역할·가상 작업 조건 일치 | 분류·선별 |
| 3 | 부품 트레이 · CND-040 | 부품 트레이에서 교체 요청과 결과 대조 | 부품·완료 기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 간단한 가전제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 가방 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1127-experience"></a>
### 접객원 — 주문을 확인하고 맞는 식기·서빙 준비

- 직업: `career-net-1127` · 시나리오 `career-net-1127-experience` `v001`.
- 원본 위치: `/items/401/data` · 역량: 대인관계능력.
- 장소 제안: 식당 홀 · `PRM-026 v001` · [PAN-026 v001](../../../images/original/panoramas/PAN-026/v001/prm-026-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 접객원의 업무 표현과 식당 홀의 손님이 식사하고 직원이 음식을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 접객원은 레스토랑이나 호텔 등에서 고객에게 음식이나 음료의 주문을 받고, 각종 서비스를 제공하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 메뉴 거치대 · CND-100 | 메뉴 거치대에서 요청 조건 확인 | 주문·제외 조건 확인 | 대화·응대 |
| 2 | 식기 · CND-098 | 식기에서 주문에 맞는 구성을 선택 | 식기 종류·개수 일치 | 분류·선별 |
| 3 | 배식 보조대 · CND-099 | 배식 보조대에서 제공 순서 확인 | 주문 ID와 제공 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 메뉴 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 식기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 배식 보조대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10007-experience"></a>
### 정밀 농업기술자 — 모종 위치와 가상 재배 환경 맞추기

- 직업: `career-net-10007` · 시나리오 `career-net-10007-experience` `v001`.
- 원본 위치: `/items/402/data` · 역량: 자연친화력.
- 장소 제안: 온실 · `PRM-041 v001` · [PAN-041 v001](../../../images/original/panoramas/PAN-041/v001/prm-041-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 정밀 농업기술자의 업무 표현과 온실의 통제된 재배 환경에서 식물을 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 정밀 농업에 필요한 기계를 관리하고 작업 정보를 분석합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모종 트레이 · CND-154 | 모종 트레이에서 요청 모종 선택 | 모종 ID·구획 일치 | 분류·선별 |
| 2 | 환경 센서 · CND-156 | 환경 센서의 가상 기록 변화 확인 | 가상 변화 지점 식별 | 관찰·검사 |
| 3 | 관수 설비 · CND-155 | 관수 설비를 교육용 목표 구간에 조절 | 교육용 설정 범위 충족 | 측정·조절 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모종 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 환경 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관수 설비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-122-experience"></a>
### 정밀기기제품제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-122` · 시나리오 `career-net-122-experience` `v001`.
- 원본 위치: `/items/403/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 정밀기기제품제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 정밀기기제품제조원은 각종 센서, 제어장치 등의 부품을 제작 및 조립하여 현미경, 시계, 카메라 등, 모양은 작지만 다양한 기능을 갖춘 기기들을 제조하는 일을 담당합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-435-experience"></a>
### 정보보호전문가 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-435` · 시나리오 `career-net-435-experience` `v001`.
- 원본 위치: `/items/404/data` · 역량: 수리·논리력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 정보보호전문가의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 정보시스템의 위험하고 약한 곳을 확인하여 대비를 하고 컴퓨터바이러스 백신 프로그램을 개발하여 보급하거나 바이러스에 감염된 데이터를 살려냅니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-938-experience"></a>
### 정보시스템운영자 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-938` · 시나리오 `career-net-938-experience` `v001`.
- 원본 위치: `/items/405/data` · 역량: 수리·논리력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 정보시스템운영자의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 정보시스템운영자는 기업이나 기관에서 운영하고 있는 정보시스템을 안전하고 체계적으로 운영 및 관리하고 사용자들에게 서비스를 제공하는 일을 합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-452-experience"></a>
### 정보중개인 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-452` · 시나리오 `career-net-452-experience` `v001`.
- 원본 위치: `/items/406/data` · 역량: 대인관계능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 정보중개인의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 정보중개인은 정보 요구자의 의뢰나 요청에 따라 해당하는 정보의 원천이 어디 있는지를 찾고 이 정보를 고객의 요구 사항에 맞게 가공하여 활용할 수 있는 형태로 제공하는 일을 담당하고 있습니다.
- 체험의 업무 자료: 가상 주문·상품 정보와 인계 조건.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-269-experience"></a>
### 정치학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-269` · 시나리오 `career-net-269-experience` `v001`.
- 원본 위치: `/items/407/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 정치학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 정치학연구원은 정치제도, 정치운동, 국제정치 상황 등의 연구를 통해 정치 이론을 정립 및 발전시키며 관련 자료를 분석하여 정부, 정당 및 기타 단체에게 정치 관련 자문을 하기도 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-172-experience"></a>
### 제과사 및 제빵사 — 반죽을 준비해 트레이에 놓고 굽기 확인

- 직업: `career-net-172` · 시나리오 `career-net-172-experience` `v001`.
- 원본 위치: `/items/408/data` · 역량: 손재능.
- 장소 제안: 제과실 · `PRM-025 v001` · [PAN-025 v001](../../../images/original/panoramas/PAN-025/v001/prm-025-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 제과사 및 제빵사의 업무 표현과 제과실의 반죽을 만들고 굽고 식히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 제과사 및 제빵사는 빵, 케이크, 쿠키, 파이 등 다양한 빵 및 과자류를 만듭니다.
- 체험의 업무 자료: 가상 주문·재료 구분과 준비 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 믹서 · CND-094 | 믹서의 가상 눈금을 목표 범위에 조절 | 교육용 설정 범위 충족 | 측정·조절 |
| 2 | 베이킹 트레이 · CND-096 | 트레이에 반죽을 겹치지 않게 배치 | 위치·간격 조건 충족 | 조립·배치 |
| 3 | 오븐 · CND-095 | 오븐의 연습용 완료 신호에 맞춰 정지 | 완료 신호의 허용 입력 구간 충족 | 타이밍·추적 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 믹서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 베이킹 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 오븐 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1137-experience"></a>
### 제관원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1137` · 시나리오 `career-net-1137-experience` `v001`.
- 원본 위치: `/items/409/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 제관원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 제관원은 두꺼운 철판, 봉, 관 등의 재료를 설계 도면에 맞게 가공하여 보일러, 철 구조물, 금속 용기 등을 제작합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-332-experience"></a>
### 제품디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-332` · 시나리오 `career-net-332-experience` `v001`.
- 원본 위치: `/items/410/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 제품디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 디자인 의뢰가 들어오면, 시장조사를 통해 소비자의 취향과 욕구, 유행을 분석하고 디자인 콘셉트를 정합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-50-experience"></a>
### 제화원 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-50` · 시나리오 `career-net-50-experience` `v001`.
- 원본 위치: `/items/411/data` · 역량: 손재능.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 제화원의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객의 주문서와 작업지시서에 따라 제품 디자인, 크기, 수량을 확인하고 필요한 재료와 공구를 준비합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-333-experience"></a>
### 조각가 — 표현 재료를 고르고 작은 작품 구성

- 직업: `career-net-333` · 시나리오 `career-net-333-experience` `v001`.
- 원본 위치: `/items/412/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 미술 작업실 · `PRM-028 v001` · [PAN-028 v001](../../../images/original/panoramas/PAN-028/v001/prm-028-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 조각가의 업무 표현과 미술 작업실의 그림을 그리고 작품을 살펴보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 석재 또는 콘크리트 등의 재료로 조각상을 제작하기 위하여 진흙, 왁스 등의 재료를 사용하여 모형을 제작합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 팔레트 도구 · CND-107 | 팔레트 도구에서 표현 목표에 맞는 재료 선택 | 재료 역할과 목표 일치 | 분류·선별 |
| 2 | 빈 캔버스 · CND-105 | 캔버스에 형태와 구도를 구성 | 필수 요소·구도 조건 충족 | 제작·표현 |
| 3 | 이젤 · CND-104 | 이젤에서 작품을 다른 시점으로 확인 | 지정 확인 항목 점검 완료 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 팔레트 도구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 빈 캔버스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이젤 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-193-experience"></a>
### 조경기술자 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-193` · 시나리오 `career-net-193-experience` `v001`.
- 원본 위치: `/items/413/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 조경기술자의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 조경기술사는 디자인과 환경에 대한 지식을 바탕으로 정원, 가로, 공원 등을 지형과 용도에 맞게 계획하고 설계하며, 조경공사를 관리 및 감독하고 조경 시설을 유지 및 관리합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-192-experience"></a>
### 조경원 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-192` · 시나리오 `career-net-192-experience` `v001`.
- 원본 위치: `/items/414/data` · 역량: 자연친화력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 조경원의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 조경 계획에 따라 작업에 필요한 공구와 자재를 준비합니다.
- 체험의 업무 자료: 가상 구획·관리 요청과 상태 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-173-experience"></a>
### 조리사 및 주방장 — 주문에 맞게 조리 준비 순서 맞추기

- 직업: `career-net-173` · 시나리오 `career-net-173-experience` `v001`.
- 원본 위치: `/items/415/data` · 역량: 손재능.
- 장소 제안: 주방 · `PRM-024 v001` · [PAN-024 v001](../../../images/original/panoramas/PAN-024/v001/prm-024-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 조리사 및 주방장의 업무 표현과 주방의 식재료 준비에서 조리와 담기까지 이어지는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 주문서나 식단 계획표에 따라 재료를 준비하고 세척하며 식료품의 상태를 검사하고 관리합니다.
- 체험의 업무 자료: 가상 주문·재료 구분과 준비 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 냉장고 · CND-090 | 냉장고에서 주문과 재료 라벨 대조 | 재료·주문·구역 구분 일치 | 분류·선별 |
| 2 | 조리대 · CND-088 | 조리대에서 가상 조리 단계를 순서대로 배치 | 가상 레시피 단계 일치 | 순서·절차 |
| 3 | 가열 기구 · CND-089 | 가열 기구를 교육용 표시 범위에 조절 | 훈련용 눈금 범위 충족 | 측정·조절 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 냉장고 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조리대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 가열 기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1156-experience"></a>
### 조림 영림 및 벌목원 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-1156` · 시나리오 `career-net-1156-experience` `v001`.
- 원본 위치: `/items/416/data` · 역량: 자연친화력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 조림 영림 및 벌목원의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 벌목원은 가구 제작 등의 여러 목적에 사용할 나무를 정해 벌목합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-911-experience"></a>
### 조명기사 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-911` · 시나리오 `career-net-911-experience` `v001`.
- 원본 위치: `/items/417/data` · 역량: 예술시각능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 조명기사의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 무대에 올릴 작품의 내용, 제작 의도, 성격 등을 정확하게 파악한 다음 대본이나 기본 설계도를 보고 조명 감독과 협의하여 조명 계획을 세웁니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-90-experience"></a>
### 조선공학기술자 — 화물 인계와 부두 모형 점검

- 직업: `career-net-90` · 시나리오 `career-net-90-experience` `v001`.
- 원본 위치: `/items/418/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 부두 · `PRM-046 v001` · [PAN-046 v001](../../../images/original/panoramas/PAN-046/v001/prm-046-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 조선공학기술자의 업무 표현과 부두의 화물과 선박을 연결하는 항만 가장자리를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 선박의 기본적인 특성, 구조 등을 개발, 연구하고 선박 및 해양구조물을 설치하기 위하여 설계계획안, 설계서 등의 관련 자료를 검토하고 분석합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 화물 상자를 목적지별로 분류 | 화물 목적지 ID 일치 | 분류·선별 |
| 2 | 손수레 · CND-133 | 손수레로 가상의 막힌 동선을 피해 순서 계획 | 동선·우선순위 조건 충족 | 계획·배분 |
| 3 | 계류 기둥 · CND-178 | 계류 기둥에서 모형 점검 항목 확인 | 정의된 점검 항목 식별 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손수레 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 계류 기둥 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-75-experience"></a>
### 조적공 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-75` · 시나리오 `career-net-75-experience` `v001`.
- 원본 위치: `/items/419/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 조적공의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 건물의 도면도 또는 설계도에 따라 벽돌 시공 계획을 세우고, 시공에 필요한 조적용 공구와 장비, 재료 등을 준비합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-334-experience"></a>
### 조향사 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-334` · 시나리오 `career-net-334-experience` `v001`.
- 원본 위치: `/items/420/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 조향사의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 다양한 향료를 배합하여 각 향료의 특성에 맞는 향수를 디자인하고 새로운 향을 개발하기 위한 실험을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1151-experience"></a>
### 종이제품생산직(기계조작) — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-1151` · 시나리오 `career-net-1151-experience` `v001`.
- 원본 위치: `/items/421/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 종이제품생산직(기계조작)의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 종이제품생산직(기계조작)은 종이 가방, 상자, 종이컵 등의 종이 제품을 생산하기 위해 각종 기계를 조작하는 일을 담당합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1128-experience"></a>
### 주방보조원 — 주문에 맞게 조리 준비 순서 맞추기

- 직업: `career-net-1128` · 시나리오 `career-net-1128-experience` `v001`.
- 원본 위치: `/items/422/data` · 역량: 손재능.
- 장소 제안: 주방 · `PRM-024 v001` · [PAN-024 v001](../../../images/original/panoramas/PAN-024/v001/prm-024-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 주방보조원의 업무 표현과 주방의 식재료 준비에서 조리와 담기까지 이어지는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 주방보조원은 음식점, 학교, 레스토랑, 호텔 등에서 조리장이나 조리사의 지시에 따라 각종 조리 업무를 보조하는 일을 담당합니다.
- 체험의 업무 자료: 가상 주문·재료 구분과 준비 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 냉장고 · CND-090 | 냉장고에서 주문과 재료 라벨 대조 | 재료·주문·구역 구분 일치 | 분류·선별 |
| 2 | 조리대 · CND-088 | 조리대에서 가상 조리 단계를 순서대로 배치 | 가상 레시피 단계 일치 | 순서·절차 |
| 3 | 가열 기구 · CND-089 | 가열 기구를 교육용 표시 범위에 조절 | 훈련용 눈금 범위 충족 | 측정·조절 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 냉장고 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조리대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 가열 기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1115-experience"></a>
### 주유원 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-1115` · 시나리오 `career-net-1115-experience` `v001`.
- 원본 위치: `/items/423/data` · 역량: 대인관계능력.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 주유원의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객이 원하는 주유량을 확인한 다음, 자동차의 연료 주입구를 열고 주유기를 조작하여 연료를 주입하고 주유량에 따른 요금을 계산합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-127-experience"></a>
### 주조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-127` · 시나리오 `career-net-127-experience` `v001`.
- 원본 위치: `/items/424/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 주조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 주조원은 제작하고자 하는 제품의 형태에 맞는 구조물(주형)에 금속을 가열하여 녹인 것(용탕)을 붓고 이를 냉각 및 응고하여 제품을 완성하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1120-experience"></a>
### 주차관리원 — 집결 위치와 이동 안내 준비

- 직업: `career-net-1120` · 시나리오 `career-net-1120-experience` `v001`.
- 원본 위치: `/items/425/data` · 역량: 대인관계능력.
- 장소 제안: 안내 집결 지점 · `PRM-069 v001` · [PAN-069 v001](../../../images/original/panoramas/PAN-069/v001/prm-069-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 주차관리원의 업무 표현과 안내 집결 지점의 안내자가 사람들을 모아 경로를 설명하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 주차관리원은 무료 또는 유료 주차 시설에서 효율적 주차장 사용을 위해 차량의 주차 공간을 안내하는 등의 운영 및 관리 업무를 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 지도 거치대 · CND-224 | 지도 거치대에서 가상 이동 경로 계획 | 가상 동선·시간 제약 충족 | 계획·배분 |
| 2 | 안내판 · CND-205 | 안내판에서 참여자의 질문에 맞는 안내 선택 | 질문 의도·최신 위치 안내 | 대화·응대 |
| 3 | 여행 가방 · CND-221 | 가방에서 일정에 맞는 준비물 선택 | 준비물과 일정 조건 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 지도 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 안내판 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 여행 가방 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-405-experience"></a>
### 주택관리사 — 주택 모형 점검과 작업 요청 정리

- 직업: `career-net-405` · 시나리오 `career-net-405-experience` `v001`.
- 원본 위치: `/items/426/data` · 역량: 대인관계능력.
- 장소 제안: 주택 관리 공간 · `PRM-063 v001` · [PAN-063 v001](../../../images/original/panoramas/PAN-063/v001/prm-063-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 주택관리사의 업무 표현과 주택 관리 공간의 건물 설비와 생활 지원 도구를 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 주택관리사는 아파트와 같은 대규모 공동주택의 각종 시설 및 환경을 유지 관리하며, 공동시설의 유지 및 보수와 관련된 각종 회계 업무를 담당합니다.
- 체험의 업무 자료: 이용자 요청·물품 구역과 점검 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 점검 보드 · CND-218 | 점검 보드에서 누락된 요청 확인 | 요청 ID·누락 식별 | 관찰·검사 |
| 2 | 설비함 · CND-217 | 설비함의 가상 표시 단서로 점검 담당 선택 | 가상 단서·담당 범위 일치 | 진단·해결 |
| 3 | 청소 도구 · CND-163 | 청소 도구를 작업 구역별로 분류 | 도구 구역 규칙 충족 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 점검 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 설비함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 청소 도구 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-239-experience"></a>
### 증권분석가 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-239` · 시나리오 `career-net-239-experience` `v001`.
- 원본 위치: `/items/427/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 증권분석가의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기업의 실적 예상, 기업의 자금조달 형편의 조사 및 분석, 증권의 가격변동과 수익률 추세 분석 등에 대한 업무를 수행하며 고객에게 유용한 투자 정보를 제공합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-240-experience"></a>
### 증권중개인 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-240` · 시나리오 `career-net-240-experience` `v001`.
- 원본 위치: `/items/428/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 증권중개인의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 금융 정기간행물, 기업의 주식 및 채권 보고서, 시장조사 등 여러 투자 정보를 검토하고 분석하여 고객에게 투자 정보를 제공하고 자문합니다.
- 체험의 업무 자료: 가상 요청 조건·수량·기간과 설명 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1111-experience"></a>
### 지게차운전원 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-1111` · 시나리오 `career-net-1111-experience` `v001`.
- 원본 위치: `/items/429/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 지게차운전원의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 지게차운전원은 생산 현장이나 창고, 부두 등에서 화물을 싣거나 내리고, 화물의 운반을 위해 지게차를 운전하는 일을 담당합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10113-experience"></a>
### 지능형 로봇개발자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10113` · 시나리오 `career-net-10113-experience` `v001`.
- 원본 위치: `/items/430/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 지능형 로봇개발자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 지능형 로봇개발자는 로봇이 인간과 유사하게 사고하고, 의사결정을 하도록 인공지능 알고리즘을 개발합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10050-experience"></a>
### 지리정보시스템기사 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-10050` · 시나리오 `career-net-10050-experience` `v001`.
- 원본 위치: `/items/431/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 지리정보시스템기사의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 통합 지리정보시스템의 공간 또는 비공간 데이터베이스의 개발을 설계 또는 조정하는 일을 하거나 효과적으로 정보를 보여주는 데 필요한 지도 제작 요소를 선택합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-29-experience"></a>
### 지리학연구원 — 관측 장치를 맞추고 기록 오류 확인

- 직업: `career-net-29` · 시나리오 `career-net-29-experience` `v001`.
- 원본 위치: `/items/432/data` · 역량: 수리·논리력.
- 장소 제안: 관측 지점 · `PRM-039 v001` · [PAN-039 v001](../../../images/original/panoramas/PAN-039/v001/prm-039-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 지리학연구원의 업무 표현과 관측 지점의 설치한 측정 장비로 환경 변화를 관찰하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 자연, 인문적 현상이 지표상 어디에서 발생하고, 왜 특정 장소에서 특정 형태로 발생하는지에 대해 여러 이론과 분석을 통해 원인을 규명합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 삼각대 센서 · CND-144 | 삼각대 센서를 표시 방향에 배치 | 위치·방향 일치 | 조립·배치 |
| 2 | 소형 관측 장치 · CND-145 | 관측 장치의 가상 눈금을 조절 | 훈련용 설정 범위 충족 | 측정·조절 |
| 3 | 데이터 기록 기기 · CND-146 | 기록 기기의 이상 데이터 지점을 표시 | 삽입된 이상 지점·기록 일치 | 관찰·검사 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 삼각대 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 관측 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 데이터 기록 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-30-experience"></a>
### 지질학연구원 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-30` · 시나리오 `career-net-30-experience` `v001`.
- 원본 위치: `/items/433/data` · 역량: 수리·논리력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 지질학연구원의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 지질학연구원은 암석 분포, 지질구조, 퇴적환경 등에 대한 조사를 통해 지하자원의 개발이나 국토개발의 기초를 제공합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-335-experience"></a>
### 지휘자 — 공연 준비와 큐 신호 맞추기

- 직업: `career-net-335` · 시나리오 `career-net-335-experience` `v001`.
- 원본 위치: `/items/434/data` · 역량: 음악능력.
- 장소 제안: 공연 무대 · `PRM-033 v001` · [PAN-033 v001](../../../images/original/panoramas/PAN-033/v001/prm-033-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 지휘자의 업무 표현과 공연 무대의 공연자와 관객의 시선 관계가 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 연주를 심사하여 기악 연주자를 선정하고, 계획된 공연에 적합하고 연주자들의 재능과 능력에 알맞은 연주곡을 선정합니다.
- 체험의 업무 자료: 공연 구간·표현 조건과 가상 큐.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 마이크 스탠드 · CND-123 | 마이크 스탠드를 표시 위치로 조절 | 위치·동선 조건 충족 | 측정·조절 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드를 큐 신호에 맞춰 선택 | 정해진 조명 큐 순서 일치 | 타이밍·추적 |
| 3 | 스피커 · CND-120 | 스피커에서 가상 박자 신호에 입력 | 연습 박자 허용 구간 충족 | 타이밍·추적 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 음악능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 마이크 스탠드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 스피커 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-407-experience"></a>
### 직업군인 — 장비 상태를 점검하고 반납 계획

- 직업: `career-net-407` · 시나리오 `career-net-407-experience` `v001`.
- 원본 위치: `/items/435/data` · 역량: 신체·운동능력.
- 장소 제안: 장비 관리실 · `PRM-067 v001` · [PAN-067 v001](../../../images/original/panoramas/PAN-067/v001/prm-067-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 직업군인의 업무 표현과 장비 관리실의 비전투 장비를 분류·보관·점검하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 남북한 간의 군사분계선 감시 및 관리, 해안선 및 국가 중요 시설에 대한 경계와 수색 정찰을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 케이스 · CND-114 | 보관 케이스에서 장비 ID와 반납 기록 대조 | 장비·기록 ID 일치 | 분류·선별 |
| 2 | 작업대 · CND-055 | 작업대에서 모형 상태 차이 점검 | 삽입된 결함 표시 | 관찰·검사 |
| 3 | 선반 · CND-028 | 선반에 반납 순서를 계획해 배치 | 보관 구획·순서 제약 충족 | 계획·배분 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 케이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작업대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-409-experience"></a>
### 직업능력개발훈련교사 — 실습 부품을 골라 조립하고 점검

- 직업: `career-net-409` · 시나리오 `career-net-409-experience` `v001`.
- 원본 위치: `/items/436/data` · 역량: 대인관계능력, 자기성찰능력.
- 장소 제안: 교육 실습실 · `PRM-013 v001` · [PAN-013 v001](../../../images/original/panoramas/PAN-013/v001/prm-013-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 직업능력개발훈련교사의 업무 표현과 교육 실습실의 학습자가 기초 조립과 도구 사용을 연습하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 직업능력개발훈련교사는 직업전문학교나 공공직업훈련원 등에서 사람들에게 직업에 필요한 기능과 지식을 가르칩니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 실습 지시와 맞는 부품 선택 | 요청 부품 ID 일치 | 분류·선별 |
| 2 | 교육용 조립 키트 · CND-057 | 조립 키트의 부품을 연결 지점에 결합 | 부품·결합 위치 일치 | 조립·배치 |
| 3 | 작업대 · CND-055 | 작업대에서 시범과 다른 결합 위치 확인 | 오류 결합 수정 완료 | 관찰·검사 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력, 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 교육용 조립 키트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작업대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-408-experience"></a>
### 직업상담 및 취업알선원 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-408` · 시나리오 `career-net-408-experience` `v001`.
- 원본 위치: `/items/437/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 직업상담 및 취업알선원의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 근로기준법을 비롯한 노동관계법규 등 노동시장에서 발생하는 직업과 관련된 법적인 일반 상담과 창업상담, 경력개발상담, 직업 적응상담, 직업전화상담, 은퇴 상담 등을 수행합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-129-experience"></a>
### 직조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-129` · 시나리오 `career-net-129-experience` `v001`.
- 원본 위치: `/items/438/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 직조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작업지시서에 따라 제작할 직물의 조직과 무늬에 대해 파악하고 직물을 생산하기 위해 필요한 실을 준비합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10079-experience"></a>
### 창업컨설턴트 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-10079` · 시나리오 `career-net-10079-experience` `v001`.
- 원본 위치: `/items/439/data` · 역량: 대인관계능력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 창업컨설턴트의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 창업을 원하는 고객과의 상담을 통해 고객의 특성, 희망 업종, 비용, 수익성 등을 분석합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1154-experience"></a>
### 채소 및 특용작물재배자 — 작물 모형 상태를 보고 관리·분류

- 직업: `career-net-1154` · 시나리오 `career-net-1154-experience` `v001`.
- 원본 위치: `/items/440/data` · 역량: 자연친화력.
- 장소 제안: 재배지 · `PRM-040 v001` · [PAN-040 v001](../../../images/original/panoramas/PAN-040/v001/prm-040-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 채소 및 특용작물재배자의 업무 표현과 재배지의 작물을 심고 돌보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 재배할 작물의 종류와 양, 재배면적을 결정하고 계획을 세웁니다.
- 체험의 업무 자료: 가상 구획·관리 요청과 상태 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 농작물 · CND-148 | 작물 모형에서 사례의 상태 차이 찾기 | 사례에서 지정한 상태 차이 식별 | 관찰·검사 |
| 2 | 물뿌리개 · CND-149 | 물뿌리개 양을 가상 목표 눈금에 맞춤 | 훈련용 양 범위 충족 | 측정·조절 |
| 3 | 수확 상자 · CND-151 | 수확 상자에 가상 등급별 분류 | 사례 등급 규칙 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 농작물 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 물뿌리개 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수확 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-31-experience"></a>
### 천문학연구원 — 관측 장치를 맞추고 기록 오류 확인

- 직업: `career-net-31` · 시나리오 `career-net-31-experience` `v001`.
- 원본 위치: `/items/441/data` · 역량: 수리·논리력.
- 장소 제안: 관측 지점 · `PRM-039 v001` · [PAN-039 v001](../../../images/original/panoramas/PAN-039/v001/prm-039-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 천문학연구원의 업무 표현과 관측 지점의 설치한 측정 장비로 환경 변화를 관찰하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 천체관측시설의 운영을 관리하고, 천체관측시설을 사용하여 천체의 현상을 연구하며, 천체관측과 관련된 시스템과 관련 장비 등을 연구, 설계합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 삼각대 센서 · CND-144 | 삼각대 센서를 표시 방향에 배치 | 위치·방향 일치 | 조립·배치 |
| 2 | 소형 관측 장치 · CND-145 | 관측 장치의 가상 눈금을 조절 | 훈련용 설정 범위 충족 | 측정·조절 |
| 3 | 데이터 기록 기기 · CND-146 | 기록 기기의 이상 데이터 지점을 표시 | 삽입된 이상 지점·기록 일치 | 관찰·검사 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 삼각대 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 관측 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 데이터 기록 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-131-experience"></a>
### 철골공 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-131` · 시나리오 `career-net-131-experience` `v001`.
- 원본 위치: `/items/442/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 철골공의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 철골공은 건물이나 다리, 댐 등의 건설에 사용되는 철재 골조나 구조 부품을 제작ㆍ수리하거나 철골재를 이용하여 건축시설물의 골조를 구성하는 일을 담당합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-132-experience"></a>
### 철도 및 지하철기관사 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-132` · 시나리오 `career-net-132-experience` `v001`.
- 원본 위치: `/items/443/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 철도 및 지하철기관사의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 운행 스케줄을 확인하고 전달 사항 및 운행 주의 사항, 운전 조건 등에 대하여 교번 운용원에게 전달받아 운행 일지에 기록합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-133-experience"></a>
### 철도차량정비원 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-133` · 시나리오 `career-net-133-experience` `v001`.
- 원본 위치: `/items/444/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 철도차량정비원의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 열차나 지하철의 이상이나 고장 유무를 확인하고 고장을 수리합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1104-experience"></a>
### 철학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-1104` · 시나리오 `career-net-1104-experience` `v001`.
- 원본 위치: `/items/445/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 철학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 종교와 도덕적 문제를 개념적, 논리적으로 분석하고, 실존적 관심에 대해 연구합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-356-experience"></a>
### 청소원 — 주택 모형 점검과 작업 요청 정리

- 직업: `career-net-356` · 시나리오 `career-net-356-experience` `v001`.
- 원본 위치: `/items/446/data` · 역량: 대인관계능력.
- 장소 제안: 주택 관리 공간 · `PRM-063 v001` · [PAN-063 v001](../../../images/original/panoramas/PAN-063/v001/prm-063-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 청소원의 업무 표현과 주택 관리 공간의 건물 설비와 생활 지원 도구를 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 청소원은 건물의 내부와 외부, 거리 및 기타 공공장소, 운송장비(자동차, 항공기, 선박 등) 등의 청소와 관련된 업무를 담당합니다.
- 체험의 업무 자료: 이용자 요청·물품 구역과 점검 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 점검 보드 · CND-218 | 점검 보드에서 누락된 요청 확인 | 요청 ID·누락 식별 | 관찰·검사 |
| 2 | 설비함 · CND-217 | 설비함의 가상 표시 단서로 점검 담당 선택 | 가상 단서·담당 범위 일치 | 진단·해결 |
| 3 | 청소 도구 · CND-163 | 청소 도구를 작업 구역별로 분류 | 도구 구역 규칙 충족 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 점검 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 설비함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 청소 도구 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1117-experience"></a>
### 청원경찰 — 가상 관제 신호를 확인하고 대응 인계

- 직업: `career-net-1117` · 시나리오 `career-net-1117-experience` `v001`.
- 원본 위치: `/items/447/data` · 역량: 신체·운동능력.
- 장소 제안: 관제실 · `PRM-061 v001` · [PAN-061 v001](../../../images/original/panoramas/PAN-061/v001/prm-061-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 청원경찰의 업무 표현과 관제실의 여러 상태 화면을 확인하고 상황을 조정하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 청원경찰은 공공기관의 기관장이나 사업체의 경영자에 요청에 의해 기관이나 사업장에 배치되어 기관 및 사업장의 재산이나 시설의 치안을 유지하며 절도, 폭력 등의 불법행위를 방지하는 일을 담당합니다.
- 체험의 업무 자료: 가상 사건·상태 신호와 전달 우선순위.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 시간에 따라 바뀌는 이상 신호 확인 | 가상 이상 신호 식별 | 관찰·검사 |
| 2 | 관제 콘솔 · CND-213 | 관제 콘솔에서 가상 대응 우선순위 배치 | 명시된 우선순위 조건 충족 | 계획·배분 |
| 3 | 통신 기기 · CND-175 | 통신 장치로 위치·상태·담당자 전달 | 인계 필드·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관제 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-179-experience"></a>
### 체형관리사 — 요청 스타일과 준비 물품 확인

- 직업: `career-net-179` · 시나리오 `career-net-179-experience` `v001`.
- 원본 위치: `/items/448/data` · 역량: 손재능.
- 장소 제안: 미용실 · `PRM-023 v001` · [PAN-023 v001](../../../images/original/panoramas/PAN-023/v001/prm-023-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 체형관리사의 업무 표현과 미용실의 고객의 머리를 손질하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 체형관리사는 영양학과 체육학의 지식을 바탕으로 체계적인 운동 방법과 식이요법 등을 이용하여 고객의 체중과 몸매를 종합적으로 관리하는 일을 담당합니다.
- 체험의 업무 자료: 고객의 요청 형태·제외 조건과 준비 도구.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 독립형 거울 · CND-086 | 거울 앞 UI에서 원하는 형태와 불편 사항 확인 | 고객 요청 확인 응답 | 대화·응대 |
| 2 | 운반 카트 · CND-016 | 카트에서 요청에 맞는 모형 도구 선택 | 도구 역할·구역 일치 | 분류·선별 |
| 3 | 세발대 · CND-087 | 세발대에서 가상 준비 단계를 순서대로 선택 | 교육용 준비 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 독립형 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세발대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-410-experience"></a>
### 초등학교교사 — 학습자의 오류를 확인하고 활동 준비

- 직업: `career-net-410` · 시나리오 `career-net-410-experience` `v001`.
- 원본 위치: `/items/449/data` · 역량: 대인관계능력, 자기성찰능력.
- 장소 제안: 교실 · `PRM-012 v001` · [PAN-012 v001](../../../images/original/panoramas/PAN-012/v001/prm-012-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 초등학교교사의 업무 표현과 교실의 학생들이 교사를 보며 수업하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 학생들의 전학, 입학, 출석, 생활기록부 등을 관리하고, 가정통신문 작성 등 학사 업무를 하며, 학교 교육과정의 편성 및 운영에 참여하고 교직원 회의에 참석하는 등 학교 업무를 수행합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 잘못 이해한 풀이 지점 확인 | 사례의 오류 지점 일치 | 관찰·검사 |
| 2 | 독립형 칠판 · CND-052 | 칠판에서 설명 순서를 구성 | 핵심 개념·설명 단계 포함 | 제작·표현 |
| 3 | 사물함 · CND-054 | 사물함에서 학습 조건에 맞는 교구 선택 | 학습 조건과 교구 기능 일치 | 분류·선별 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력, 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 칠판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 사물함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-337-experience"></a>
### 촬영기사 — 촬영 대상을 배치하고 구도 완성

- 직업: `career-net-337` · 시나리오 `career-net-337-experience` `v001`.
- 원본 위치: `/items/450/data` · 역량: 예술시각능력.
- 장소 제안: 촬영 스튜디오 · `PRM-030 v001` · [PAN-030 v001](../../../images/original/panoramas/PAN-030/v001/prm-030-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 촬영기사의 업무 표현과 촬영 스튜디오의 피사체를 카메라와 조명으로 촬영하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 촬영이 끝나면 촬영 일시, 장면 등을 기록하며 촬영 장비를 점검하고, 파손된 장비와 인화 장비 등을 수리합니다.
- 체험의 업무 자료: 촬영·편집 요청과 화면·소리 구성.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 작은 제품 촬영대 · CND-112 | 촬영대의 대상 위치를 요청 구도에 배치 | 위치·가림 조건 충족 | 조립·배치 |
| 2 | 조명 스탠드 · CND-111 | 조명 스탠드 방향을 가상 목표에 조절 | 표시 조명 범위 충족 | 측정·조절 |
| 3 | 카메라 · CND-109 | 카메라에서 프레임을 구성하고 촬영 | 필수 대상과 여백 포함 | 제작·표현 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 작은 제품 촬영대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조명 스탠드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 카메라 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-338-experience"></a>
### 출판물기획전문가 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-338` · 시나리오 `career-net-338-experience` `v001`.
- 원본 위치: `/items/451/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 출판물기획전문가의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작가 섭외, 출판물 영업 전략 등 출판물 기획 및 제작에 관련된 모든 일을 담당합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-926-experience"></a>
### 출판편집자 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-926` · 시나리오 `career-net-926-experience` `v001`.
- 원본 위치: `/items/452/data` · 역량: 언어능력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 출판편집자의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 디자인 설계부터 편집까지의 모든 작업을 수행하기도 하며, 디자인 프로그램인 일러스트, 포토샵 등을 이용하여 사진을 합성 또는 수정하여 더욱 좋은 이미지를 만듭니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-32-experience"></a>
### 측량사 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-32` · 시나리오 `career-net-32-experience` `v001`.
- 원본 위치: `/items/453/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 측량사의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 측량사는 국토의 이용, 개발, 건설 공사, 지도 제작을 목적으로 토지의 형태, 지형선, 위치, 고도, 면적 등을 측량하는 업무를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-33-experience"></a>
### 치과기공사 — 가상 작업 구역을 확인하고 도구 준비

- 직업: `career-net-33` · 시나리오 `career-net-33-experience` `v001`.
- 원본 위치: `/items/454/data` · 역량: 대인관계능력.
- 장소 제안: 처치실 · `PRM-009 v001` · [PAN-009 v001](../../../images/original/panoramas/PAN-009/v001/prm-009-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 치과기공사의 업무 표현과 처치실의 의료진이 준비한 기구로 처치하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 치과 병원과 의원에서 제공받은 환자의 치아 모형을 분석, 설계해서 석고 모형을 뜨고, 작업 모형에 맞게 금, 은, 합성수지 등으로 인공 치아를 만들거나 의치, 교정 틀 등 보철 제작물을 주조합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 기구 트레이에서 요청 라벨과 맞는 모형 도구 선택 | 도구 라벨·구역 구분 일치 | 분류·선별 |
| 2 | 작업등 · CND-043 | 작업등을 표시된 가상 관찰 영역에 맞춤 | 표시 영역과 조명 방향 일치 | 측정·조절 |
| 3 | 운반 카트 · CND-016 | 카트의 물품을 준비 순서대로 정돈 | 준비 순서·누락 없음 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 작업등 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-411-experience"></a>
### 치과위생사 — 가상 작업 구역을 확인하고 도구 준비

- 직업: `career-net-411` · 시나리오 `career-net-411-experience` `v001`.
- 원본 위치: `/items/455/data` · 역량: 대인관계능력.
- 장소 제안: 처치실 · `PRM-009 v001` · [PAN-009 v001](../../../images/original/panoramas/PAN-009/v001/prm-009-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 치과위생사의 업무 표현과 처치실의 의료진이 준비한 기구로 처치하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 병원, 가정 및 학교에서 개인 또는 대중을 상대로 구강 보건교육을 실시하며, 학교 및 보건소에서 집단 구강 검사, 칫솔질 교육 등을 합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 기구 트레이에서 요청 라벨과 맞는 모형 도구 선택 | 도구 라벨·구역 구분 일치 | 분류·선별 |
| 2 | 작업등 · CND-043 | 작업등을 표시된 가상 관찰 영역에 맞춤 | 표시 영역과 조명 방향 일치 | 측정·조절 |
| 3 | 운반 카트 · CND-016 | 카트의 물품을 준비 순서대로 정돈 | 준비 순서·누락 없음 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 작업등 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-34-experience"></a>
### 치과의사 — 가상 방문 기록을 확인하고 설명 준비

- 직업: `career-net-34` · 시나리오 `career-net-34-experience` `v001`.
- 원본 위치: `/items/456/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 진료실 · `PRM-008 v001` · [PAN-008 v001](../../../images/original/panoramas/PAN-008/v001/prm-008-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 치과의사의 업무 표현과 진료실의 진료 상담과 기본 상태 확인을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 의료기기를 이용하여 구강 질환을 정밀하게 검사, 진단하고 손상된 치아를 인공적 장치물로 대치하거나 잇몸의 염증 등을 치료합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 의료 모니터 · CND-042 | 의료 모니터에서 기록 ID와 요청 기록 대조 | 기록 ID·누락 항목 식별 | 관찰·검사 |
| 2 | 진찰·처치 침대 · CND-041 | 진찰 침대 옆 UI에서 방문자의 설명을 듣고 확인 질문 | 필수 질문과 설명 확인 | 대화·응대 |
| 3 | 업무 책상 · CND-004 | 책상에서 전달 기록을 필수 항목별로 정리 | 인계 기록 필드 충족 | 분류·선별 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 진찰·처치 침대 / common / 실제 모델 연결 미정. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 현재 장소·장비는 범용 참고. 해당 전문 업무를 구별하는 장비·문제 데이터 적합성 검토 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1126-experience"></a>
### 치어리더 — 경기 모형의 동작과 기록 확인

- 직업: `career-net-1126` · 시나리오 `career-net-1126-experience` `v001`.
- 원본 위치: `/items/457/data` · 역량: 신체·운동능력.
- 장소 제안: 경기 구역 · `PRM-049 v001` · [PAN-049 v001](../../../images/original/panoramas/PAN-049/v001/prm-049-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 치어리더의 업무 표현과 경기 구역의 하나의 작은 구기 경기 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 치어리더는 운동 경기장에서 흥겨운 음악이나 구호에 맞추어 춤을 추면서 관중의 흥과 응원을 유도하는 일을 담당합니다.
- 체험의 업무 자료: 가상 활동 규칙·도구와 동작 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공 · CND-189 | 공의 이동 경로를 입력으로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 2 | 작은 골대 한 쌍 · CND-188 | 골대 모형을 규칙 카드 위치에 맞춤 | 규칙 카드 위치 일치 | 조립·배치 |
| 3 | 빈 점수판 · CND-190 | 점수판에서 사건 순서와 기록 불일치 수정 | 가상 사건·점수 기록 일치 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 골대 한 쌍 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 빈 점수판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1438-experience"></a>
### 카레이서 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-1438` · 시나리오 `career-net-1438-experience` `v001`.
- 원본 위치: `/items/458/data` · 역량: 공간지각력, 손재능.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 카레이서의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 경기 일정에 따라 미리 자동차 경주장의 상태, 상대 팀의 경기력과 과거 경력 등 자료를 수집·분석하여 전략을 세웁니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 공간지각력, 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-946-experience"></a>
### 카지노딜러 — 상품 정보를 확인하고 주문 묶음 준비

- 직업: `career-net-946` · 시나리오 `career-net-946-experience` `v001`.
- 원본 위치: `/items/459/data` · 역량: 공간지각력, 손재능.
- 장소 제안: 소매점 · `PRM-021 v001` · [PAN-021 v001](../../../images/original/panoramas/PAN-021/v001/prm-021-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 카지노딜러의 업무 표현과 소매점의 방문객이 진열 상품을 고르고 계산하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 딜러는 게임 참여자에게 게임의 기본 규칙을 설명하고 참가자들의 착석 여부와 규정된 금액을 사용했는지 확인을 한 후, 카드, 주사위를 통해 게임을 진행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 단순 포장 상품 · CND-082 | 포장 상품의 요청·라벨 불일치 확인 | 상품 ID·라벨 확인 | 관찰·검사 |
| 2 | POS 기기 · CND-083 | POS에서 수량·가상 합계를 맞춤 | 수량·가상 합계 일치 | 측정·조절 |
| 3 | 바구니 · CND-084 | 바구니에 주문별 상품 분류 | 주문별 묶음과 누락 없음 | 분류·선별 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 공간지각력, 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 단순 포장 상품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: POS 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바구니 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-278-experience"></a>
### 카피라이터 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-278` · 시나리오 `career-net-278-experience` `v001`.
- 원본 위치: `/items/460/data` · 역량: 언어능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 카피라이터의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 상품 또는 용역에 관한 정보를 얻고 광고 문안의 길이와 형태 등을 토의하기 위해 광고주 및 시장조사 분석가와 협의합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-125-experience"></a>
### 캐드원 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-125` · 시나리오 `career-net-125-experience` `v001`.
- 원본 위치: `/items/461/data` · 역량: 손재능.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 캐드원의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 약도나 설계서의 내용을 파악하여 캐드 작업을 제품, 기계, 특수, 정밀 도면으로 분류합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-412-experience"></a>
### 캐디 — 집결 위치와 이동 안내 준비

- 직업: `career-net-412` · 시나리오 `career-net-412-experience` `v001`.
- 원본 위치: `/items/462/data` · 역량: 신체·운동능력.
- 장소 제안: 안내 집결 지점 · `PRM-069 v001` · [PAN-069 v001](../../../images/original/panoramas/PAN-069/v001/prm-069-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 캐디의 업무 표현과 안내 집결 지점의 안내자가 사람들을 모아 경로를 설명하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객 또는 선수가 쳐낸 공을 찾고, 골프공과 골프채를 깨끗하게 세척하고 관리합니다.
- 체험의 업무 자료: 가상 활동 규칙·도구와 동작 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 지도 거치대 · CND-224 | 지도 거치대에서 가상 이동 경로 계획 | 가상 동선·시간 제약 충족 | 계획·배분 |
| 2 | 안내판 · CND-205 | 안내판에서 참여자의 질문에 맞는 안내 선택 | 질문 의도·최신 위치 안내 | 대화·응대 |
| 3 | 여행 가방 · CND-221 | 가방에서 일정에 맞는 준비물 선택 | 준비물과 일정 조건 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 지도 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 안내판 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 여행 가방 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-339-experience"></a>
### 캐릭터디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-339` · 시나리오 `career-net-339-experience` `v001`.
- 원본 위치: `/items/463/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 캐릭터디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 캐릭터 대상에 대하여 스타일이나 주제를 연구하고, 시장조사를 통하여 영업 담당자, 상품 제작진과 함께 상품화할 아이템의 회의를 진행합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1439-experience"></a>
### 캐스팅디렉터 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-1439` · 시나리오 `career-net-1439-experience` `v001`.
- 원본 위치: `/items/464/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 캐스팅디렉터의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 시나리오를 읽어 본 후 등장인물의 성격을 파악하고, 각 배역에 적합한 배우를 섭외하기 위해 배우들에 대한 정보를 수집하여 분석합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1256-experience"></a>
### 커플매니저 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-1256` · 시나리오 `career-net-1256-experience` `v001`.
- 원본 위치: `/items/465/data` · 역량: 대인관계능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 커플매니저의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 상담을 통해 회원의 학력, 신체 조건, 직업 등의 인적 사항과 이상형, 인생관, 용모, 태도 등에 대한 정보를 수집·기록합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-340-experience"></a>
### 컬러리스트 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-340` · 시나리오 `career-net-340-experience` `v001`.
- 원본 위치: `/items/466/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 컬러리스트의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 색상에 관한 각종 정보를 수집 및 분석하고 소비자 선호 조사 등을 통해 유행하는 색의 경향을 파악합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-457-experience"></a>
### 컴퓨터게임시나리오작가 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-457` · 시나리오 `career-net-457-experience` `v001`.
- 원본 위치: `/items/467/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 컴퓨터게임시나리오작가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 게임의 스토리 전개를 구성하며, 게임의 개발 과정을 관리하고 감독합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-458-experience"></a>
### 컴퓨터그래픽디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-458` · 시나리오 `career-net-458-experience` `v001`.
- 원본 위치: `/items/468/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 컴퓨터그래픽디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 인터넷 홈페이지에 사용되는 여러 가지 새로운 이미지를 생각해내고 제작하며, 웹페이지에 디자인한 이미지를 올립니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-466-experience"></a>
### 컴퓨터설치·수리원 — 가전 모형의 단서를 보고 점검 준비

- 직업: `career-net-466` · 시나리오 `career-net-466-experience` `v001`.
- 원본 위치: `/items/469/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 가정 수리 공간 · `PRM-058 v001` · [PAN-058 v001](../../../images/original/panoramas/PAN-058/v001/prm-058-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 컴퓨터설치·수리원의 업무 표현과 가정 수리 공간의 방문 기술자가 가정용 기기를 점검하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 컴퓨터설치ㆍ수리원은 고객의 요청에 따라 컴퓨터나 프린터 및 스캐너와 같은 주변기기를 설치하거나 컴퓨터의 고장 사항을 확인하고 수리하는 일을 합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 간단한 가전제품 · CND-207 | 가전제품 모형의 표시 단서로 고장 가설 선택 | 제공 단서와 가설 일치 | 진단·해결 |
| 2 | 공구 가방 · CND-208 | 공구 가방에서 모형 작업에 맞는 도구 선택 | 도구 역할·가상 작업 조건 일치 | 분류·선별 |
| 3 | 부품 트레이 · CND-040 | 부품 트레이에서 교체 요청과 결과 대조 | 부품·완료 기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 간단한 가전제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 가방 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-948-experience"></a>
### 컴퓨터하드웨어 기술자 및 연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-948` · 시나리오 `career-net-948-experience` `v001`.
- 원본 위치: `/items/470/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 컴퓨터하드웨어 기술자 및 연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 컴퓨터 본체, 중앙처리장치, 주기억장치, 그래픽카드 등 컴퓨터와 관련된 각종 부품을 설계, 개발하고, 생산을 관리합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10058-experience"></a>
### 케어매니저 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10058` · 시나리오 `career-net-10058-experience` `v001`.
- 원본 위치: `/items/471/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 케어매니저의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 요양보호사가 제공해야 할 서비스와 일정을 조정하고 행정 업무를 하며 요양보호사를 관리하고 지원합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1090-experience"></a>
### 콘크리트공 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-1090` · 시나리오 `career-net-1090-experience` `v001`.
- 원본 위치: `/items/472/data` · 역량: 손재능.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 콘크리트공의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 콘크리트공은 건축 및 토목 공사에서 일정 수준 이상의 콘크리트 강도가 나오도록 시멘트, 모래, 자갈, 물을 적정하게 배합하여, 이것을 조립된 철근 위에 붓고, 잘 굳도록 관리하는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10033-experience"></a>
### 크라우드 펀딩 전문가 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-10033` · 시나리오 `career-net-10033-experience` `v001`.
- 원본 위치: `/items/473/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 크라우드 펀딩 전문가의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 크라우드 펀딩 전문가는 크라우드 펀딩 중개를 담당하는 금융 투자업자로서, 고객의 재산을 직접 맡아서 관리하지 않고, 자금이 필요한 사람과 자금을 투자하고 싶은 사람 사이를 중개하는 역할을 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-592-experience"></a>
### 크레인 및 호이스트운전원 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-592` · 시나리오 `career-net-592-experience` `v001`.
- 원본 위치: `/items/474/data` · 역량: 신체·운동능력.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 크레인 및 호이스트운전원의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작업지시서에 따라 이동시킬 물품이나 화물의 종류와 위치를 확인하고 안전을 확인하고 신호를 보내는 신호수와 통신 상태를 확인합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10031-experience"></a>
### 클라우드 시스템 엔지니어 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-10031` · 시나리오 `career-net-10031-experience` `v001`.
- 원본 위치: `/items/475/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 클라우드 시스템 엔지니어의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 클라우드 시스템 엔지니어는 인터넷의 서버에 각종 컴퓨터 프로그램을 올려 놓고 여러 이용자들이 인터넷에 접속하여 데이터를 저장하고 처리할 수 있는 기술을 개발합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-47-experience"></a>
### 타이어 및 고무제품 생산직 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-47` · 시나리오 `career-net-47-experience` `v001`.
- 원본 위치: `/items/476/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 타이어 및 고무제품 생산직의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 타이어 및 고무제품 생산직은 각종 고무 제품 제작을 위해 여러 화학제품과 원료를 배합, 가공하는 제조기기와 장치를 조작합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10105-experience"></a>
### 태양광발전연구 및 개발자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10105` · 시나리오 `career-net-10105-experience` `v001`.
- 원본 위치: `/items/477/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 태양광발전연구 및 개발자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 태양전지, 태양광 모듈 등 태양광 분야의 제품을 생산하는 데 필요한 각종 공정 장비를 연구·설계하고 개발합니다.
- 체험의 업무 자료: 사용자 요구·가상 기능과 테스트 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-371-experience"></a>
### 택배원 — 도착 물품과 인계 순서 맞추기

- 직업: `career-net-371` · 시나리오 `career-net-371-experience` `v001`.
- 원본 위치: `/items/478/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 거점 · `PRM-055 v001` · [PAN-055 v001](../../../images/original/panoramas/PAN-055/v001/prm-055-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 택배원의 업무 표현과 운송 거점의 물품 인계와 출발 준비를 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 택배원은 고객이 주문한 상품이나 구매한 상품 등 각종 물품을 고객이 원하는 곳까지 운반하는 일을 합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안내판 · CND-205 | 안내판에서 변경된 인계 위치 확인 | 최신 안내 revision 일치 | 관찰·검사 |
| 2 | 보관 상자 · CND-058 | 포장 상자를 수령 ID에 맞게 분류 | 수령 ID·상자 일치 | 분류·선별 |
| 3 | 운반 카트 · CND-016 | 카트의 방문 순서를 가상 동선에 맞춰 계획 | 시간·동선 제약 충족 | 계획·배분 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안내판 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-426-experience"></a>
### 택시운전기사 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-426` · 시나리오 `career-net-426-experience` `v001`.
- 원본 위치: `/items/479/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 택시운전기사의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 택시 운전을 시작하기 전, 점검표에 따라 차량을 점검하고 이상한 점이 발견되면 정비소에 수리를 맡깁니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-242-experience"></a>
### 텔레마케터 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-242` · 시나리오 `career-net-242-experience` `v001`.
- 원본 위치: `/items/480/data` · 역량: 대인관계능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 텔레마케터의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 텔레마케터는 마케팅에 대한 지식을 바탕으로 각종 상품을 전화 주문을 통해 판매하거나 직접 고객에게 전화를 걸어 상품을 홍보하고 판매하는 일을 담당합니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-137-experience"></a>
### 토목공학기술자 — 작업 구역을 확인하고 구조 모형 배치

- 직업: `career-net-137` · 시나리오 `career-net-137-experience` `v001`.
- 원본 위치: `/items/481/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 건축 작업 구역 · `PRM-036 v001` · [PAN-036 v001](../../../images/original/panoramas/PAN-036/v001/prm-036-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 토목공학기술자의 업무 표현과 건축 작업 구역의 작은 구조물을 세우는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 측량, 조사시험, 설계 등의 용역과 공사 시공에 따른 과업 지시서, 시공품의 중간검사, 설계변경, 준공검사 등과 시설 공사의 감리 업무 등 제반 행정 처리 업무를 수행합니다.
- 체험의 업무 자료: 가구 부품·규격과 완성 상태.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 펜스 · CND-134 | 안전 펜스에서 가상 위험 지점 확인 | 위험 표시 확인 전 작업 잠금 | 관찰·검사 |
| 2 | 자재 더미 · CND-132 | 자재 더미에서 도면 규격의 자재 선택 | 자재 규격 일치 | 분류·선별 |
| 3 | 부분 벽돌 구조 · CND-131 | 벽돌 구조 모형을 표시 위치에 결합 | 연결 위치·방향 일치 | 조립·배치 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 펜스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 자재 더미 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부분 벽돌 구조 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-997-experience"></a>
### 토양환경기술자 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-997` · 시나리오 `career-net-997-experience` `v001`.
- 원본 위치: `/items/482/data` · 역량: 수리·논리력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 토양환경기술자의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 토양환경기술자는 지역의 토양오염 상태를 측정하고, 연구와 실험분석을 통해 토양오염물질이 환경에 미치는 영향을 최소화하고 환경보존에 필요한 공학적 기술들을 연구하고 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-36-experience"></a>
### 통계학연구원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-36` · 시나리오 `career-net-36-experience` `v001`.
- 원본 위치: `/items/483/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 통계학연구원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 통계학연구원은 자연, 사회, 경제 현상 등으로부터 얻어진 자료를 과학적으로 분석, 추론함으로써 최적의 의사결정과 미래 예측에 도움이 되는 정보로 가공하는 업무를 수행합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-138-experience"></a>
### 통신공학 기술자 및 연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-138` · 시나리오 `career-net-138-experience` `v001`.
- 원본 위치: `/items/484/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 통신공학 기술자 및 연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 위성통신 연구 설계, 제작 및 관련 기간 산업 시설, 각종 생활 편리성 등을 연구개발 합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-465-experience"></a>
### 통신망설계운영기술자 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-465` · 시나리오 `career-net-465-experience` `v001`.
- 원본 위치: `/items/485/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 통신망설계운영기술자의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 통신망설계운영기술자는 통신망의 접속자 몰림 현상 해소, 통화 완료율 향상, 기존 통신망의 효율성 극대화 등을 위해 연구 및 개발하는 일을 합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1148-experience"></a>
### 통신설비설치 및 수리원 — 가전 모형의 단서를 보고 점검 준비

- 직업: `career-net-1148` · 시나리오 `career-net-1148-experience` `v001`.
- 원본 위치: `/items/486/data` · 역량: 손재능.
- 장소 제안: 가정 수리 공간 · `PRM-058 v001` · [PAN-058 v001](../../../images/original/panoramas/PAN-058/v001/prm-058-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 통신설비설치 및 수리원의 업무 표현과 가정 수리 공간의 방문 기술자가 가정용 기기를 점검하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 유선전화, 휴대폰, 무선전화, 무선통신기 등의 송신과 수신을 이어주기 위한 설계도에 따라 통신장비 설치 위치를 확인하고, 통신장비를 설비합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 간단한 가전제품 · CND-207 | 가전제품 모형의 표시 단서로 고장 가설 선택 | 제공 단서와 가설 일치 | 진단·해결 |
| 2 | 공구 가방 · CND-208 | 공구 가방에서 모형 작업에 맞는 도구 선택 | 도구 역할·가상 작업 조건 일치 | 분류·선별 |
| 3 | 부품 트레이 · CND-040 | 부품 트레이에서 교체 요청과 결과 대조 | 부품·완료 기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 간단한 가전제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 가방 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-429-experience"></a>
### 통신엔지니어 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-429` · 시나리오 `career-net-429-experience` `v001`.
- 원본 위치: `/items/487/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 통신엔지니어의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 국내외 시장조사, 통신 분야의 최신 기술이나 변화 등을 분석하여 새로운 기능과 성능을 갖춘 통신 제품과 기술을 연구하고 개발합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-140-experience"></a>
### 통신장비기사 — 가상 서버 연결 오류를 찾아 복구안 선택

- 직업: `career-net-140` · 시나리오 `career-net-140-experience` `v001`.
- 원본 위치: `/items/488/data` · 역량: 손재능.
- 장소 제안: 서버실 · `PRM-060 v001` · [PAN-060 v001](../../../images/original/panoramas/PAN-060/v001/prm-060-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 통신장비기사의 업무 표현과 서버실의 서버 장비를 유지·관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 통신장비기사는 무선중계기시스템, 유선통신장비, 무선통신장비, 위성통신장비 등의 장비를 유지하고 관리하며 운용합니다.
- 체험의 업무 자료: 가상 연결·운영 상태와 장애 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 관리 단말 · CND-212 | 관리 단말의 가상 장애 기록 확인 | 장애 ID·이상 항목 식별 | 관찰·검사 |
| 2 | 케이블 트레이 · CND-211 | 케이블 트레이에서 표시 연결 위치를 맞춤 | 논리 연결과 포트 일치 | 조립·배치 |
| 3 | 서버 랙 · CND-210 | 서버 랙의 단서로 복구 순서 선택 | 가상 단서와 복구 순서 일치 | 진단·해결 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 관리 단말 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 케이블 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 서버 랙 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-139-experience"></a>
### 통신케이블설치 및 수리원 — 가전 모형의 단서를 보고 점검 준비

- 직업: `career-net-139` · 시나리오 `career-net-139-experience` `v001`.
- 원본 위치: `/items/489/data` · 역량: 손재능.
- 장소 제안: 가정 수리 공간 · `PRM-058 v001` · [PAN-058 v001](../../../images/original/panoramas/PAN-058/v001/prm-058-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 통신케이블설치 및 수리원의 업무 표현과 가정 수리 공간의 방문 기술자가 가정용 기기를 점검하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 통신케이블설치 및 수리원은 통신망의 기초가 되는 통신선로를 전선, 다리, 선로 등에 시설하고, 정기적으로 유지하고 보수하는 일을 담당합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 간단한 가전제품 · CND-207 | 가전제품 모형의 표시 단서로 고장 가설 선택 | 제공 단서와 가설 일치 | 진단·해결 |
| 2 | 공구 가방 · CND-208 | 공구 가방에서 모형 작업에 맞는 도구 선택 | 도구 역할·가상 작업 조건 일치 | 분류·선별 |
| 3 | 부품 트레이 · CND-040 | 부품 트레이에서 교체 요청과 결과 대조 | 부품·완료 기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 간단한 가전제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 가방 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-264-experience"></a>
### 통역가 — 출장 요청과 자료를 확인해 전달

- 직업: `career-net-264` · 시나리오 `career-net-264-experience` `v001`.
- 원본 위치: `/items/490/data` · 역량: 언어능력.
- 장소 제안: 출장 업무 공간 · `PRM-068 v001` · [PAN-068 v001](../../../images/original/panoramas/PAN-068/v001/prm-068-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 통역가의 업무 표현과 출장 업무 공간의 이동 중 임시 자리에서 업무를 처리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 동시통역은 각종 국제회의나 세미나 등에서 사람들에게 연사의 말을 해당 국가의 언어로 실시간 통역하는 것이며, 순차 통역이란 발표자가 연설을 하면 통역가는 연설 내용을 기록한 후 옆에서 바로 발표자의 말을 이어서 통역을 하는 것입니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 휴대 전화 · CND-222 | 휴대전화에서 상대 요청과 누락 정보 확인 | 요청·언어·목적 확인 | 대화·응대 |
| 2 | 노트북 · CND-012 | 노트북에서 전달 자료와 원문 차이 확인 | 지정 오류·누락 식별 | 관찰·검사 |
| 3 | 문서 파우치 · CND-223 | 파우치에서 목적별 문서 분류 | 목적별 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 휴대 전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 문서 파우치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-950-experience"></a>
### 투자분석가(애널리스트) — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-950` · 시나리오 `career-net-950-experience` `v001`.
- 원본 위치: `/items/491/data` · 역량: 수리·논리력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 투자분석가(애널리스트)의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 투자분석가는 자신의 회사 혹은 회사의 고객들에게 금융 및 투자자문을 제공하기 위해 금융시장 정보를 수집, 분석합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-142-experience"></a>
### 트럭운전기사 — 운송 모형 상태 확인과 운행 인계

- 직업: `career-net-142` · 시나리오 `career-net-142-experience` `v001`.
- 원본 위치: `/items/492/data` · 역량: 신체·운동능력.
- 장소 제안: 운송 조종 공간 · `PRM-054 v001` · [PAN-054 v001](../../../images/original/panoramas/PAN-054/v001/prm-054-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 트럭운전기사의 업무 표현과 운송 조종 공간의 운송 장비의 조작과 상태 확인을 하는 추상화된 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 화물의 운송 목적지를 확인하고 트럭의 엔진 오일, 냉각수, 타이어의 공기압력 상태 및 각종 안전장치의 이상 여부를 점검합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 상태 화면에서 요청 운행과 가상 점검표 대조 | 필수 점검 확인 | 관찰·검사 |
| 2 | 조작 콘솔 · CND-203 | 조작 콘솔로 유도 경로 추적 | 경로 허용 오차 충족 | 타이밍·추적 |
| 3 | 통신 기기 · CND-175 | 통신 기기로 위치·상태 전달 | 전달 항목과 상대 확인 충족 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조작 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-413-experience"></a>
### 특수교사 — 학습자의 오류를 확인하고 활동 준비

- 직업: `career-net-413` · 시나리오 `career-net-413-experience` `v001`.
- 원본 위치: `/items/493/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 교실 · `PRM-012 v001` · [PAN-012 v001](../../../images/original/panoramas/PAN-012/v001/prm-012-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 특수교사의 업무 표현과 교실의 학생들이 교사를 보며 수업하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 특수교사는 신체적, 정신적 장애를 겪고 있는 학생에게 유치원, 초등학교, 중학교, 고등학교에 준하는 교육과 생활에 필요한 지식 및 기능을 가르칩니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 잘못 이해한 풀이 지점 확인 | 사례의 오류 지점 일치 | 관찰·검사 |
| 2 | 독립형 칠판 · CND-052 | 칠판에서 설명 순서를 구성 | 핵심 개념·설명 단계 포함 | 제작·표현 |
| 3 | 사물함 · CND-054 | 사물함에서 학습 조건에 맞는 교구 선택 | 학습 조건과 교구 기능 일치 | 분류·선별 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 칠판 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 사물함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-916-experience"></a>
### 특수효과기술자 — 소재를 골라 짧은 영상 흐름 완성

- 직업: `career-net-916` · 시나리오 `career-net-916-experience` `v001`.
- 원본 위치: `/items/494/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 영상 편집실 · `PRM-032 v001` · [PAN-032 v001](../../../images/original/panoramas/PAN-032/v001/prm-032-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 특수효과기술자의 업무 표현과 영상 편집실의 영상과 소리를 검토하고 편집하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 특수효과기술자는 방송이나 영화에서 연출의 효과를 높이기 위해 컴퓨터 그래픽 프로그램을 이용해 다양한 배경과 특수효과들을 만드는 일을 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 미디어 보관함 · CND-121 | 미디어 보관함에서 요청 장면 선택 | 소재 ID·권장 용도 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 모니터에서 컷의 순서·길이를 편집 | 필수 장면·순서 충족 | 제작·표현 |
| 3 | 헤드폰 · CND-117 | 헤드폰에서 가상 음성·장면 동기 오류 확인 | 삽입된 동기 오류 표시·수정 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 미디어 보관함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 헤드폰 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1276-experience"></a>
### 파티플래너 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-1276` · 시나리오 `career-net-1276-experience` `v001`.
- 원본 위치: `/items/495/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 파티플래너의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 파티플래너는 효과적인 파티 진행을 위하여 기획·운영·연출·홍보 등 파티의 전체 과정을 총괄합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-143-experience"></a>
### 판금원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-143` · 시나리오 `career-net-143-experience` `v001`.
- 원본 위치: `/items/496/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 판금원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 완성된 제품의 형태, 치수, 마무리 상태 등을 확인하고 이상이나 결함이 발견되면 수리합니다.
- 체험의 업무 자료: 가상 도면·자재 규격과 모형 점검 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-414-experience"></a>
### 판사 — 가상 사건 자료를 정리하고 설명하기

- 직업: `career-net-414` · 시나리오 `career-net-414-experience` `v001`.
- 원본 위치: `/items/497/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 법정 · `PRM-052 v001` · [PAN-052 v001](../../../images/original/panoramas/PAN-052/v001/prm-052-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 판사의 업무 표현과 법정의 판단·진술·방청의 역할이 좌석 배치로 읽히는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 판사는 법정에서 재판을 진행하며 검사와 변호사의 논쟁, 변호사 및 증인의 진술, 사건 증거 등 재판에 관련된 자료를 검토하고 법률에 근거해 판결을 내립니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 문서함 · CND-198 | 문서함에서 주장·근거·미확인 자료 구분 | 자료 종류 구분 일치 | 분류·선별 |
| 2 | 진술대 · CND-195 | 진술대에서 확인 질문과 중립적 요약 선택 | 미확인 사실을 단정하지 않는 요약 | 대화·응대 |
| 3 | 당사자 책상 · CND-196 | 당사자 책상에서 제공 근거와 주장 연결 | 가상 자료가 지지하는 관계만 선택 | 진단·해결 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 문서함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 진술대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 당사자 책상 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-344-experience"></a>
### 패션디자이너 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-344` · 시나리오 `career-net-344-experience` `v001`.
- 원본 위치: `/items/498/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 패션디자이너의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 제품이 나오기 약 6개월 전부터 국내외 패션 흐름 등을 파악하고, 유행 경향, 소재, 색 등의 조화 등에 관련된 자료를 종합적으로 분석하여 새로운 패션 디자인을 기획합니다.
- 체험의 업무 자료: 의뢰 조건·형태·배치와 시안.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-345-experience"></a>
### 패션코디네이터 — 요구에 맞는 시안을 만들고 검토

- 직업: `career-net-345` · 시나리오 `career-net-345-experience` `v001`.
- 원본 위치: `/items/499/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 디자인 작업실 · `PRM-027 v001` · [PAN-027 v001](../../../images/original/panoramas/PAN-027/v001/prm-027-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 패션코디네이터의 업무 표현과 디자인 작업실의 시안을 만들고 화면과 출력물을 비교하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 드라마나 영화의 등장인물의 성격과 외모를 분석하고, 이를 방송 연출자와 배우와 상의하여 의상 연출 방향을 결정합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시안 보드 · CND-102 | 시안 보드에서 요구와 어긋난 구성 확인 | 명시한 요구 오류 식별 | 관찰·검사 |
| 2 | 펜 태블릿 · CND-101 | 태블릿에서 형태·배치를 수정 | 필수 시각 조건 충족 | 제작·표현 |
| 3 | 모니터 · CND-005 | 모니터에서 요구 항목과 결과를 대조 | 누락 조건 없음 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시안 보드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 펜 태블릿 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-295-experience"></a>
### 패턴사 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-295` · 시나리오 `career-net-295-experience` `v001`.
- 원본 위치: `/items/500/data` · 역량: 손재능.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 패턴사의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 패턴사는 디자이너의 스케치나 작업지시서에 따라 패턴 용지나 컴퓨터 프로그램을 이용하여 의류의 패턴 즉, 기본 모형을 제작하는 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-144-experience"></a>
### 펄프 및 종이 생산직 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-144` · 시나리오 `career-net-144-experience` `v001`.
- 원본 위치: `/items/501/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 펄프 및 종이 생산직의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 작업명세서를 통해 종이 제작에 필요한 식물성 물질, 섬유, 펄프, 약품 등과 장비를 준비합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-346-experience"></a>
### 편집기사 — 소재를 골라 짧은 영상 흐름 완성

- 직업: `career-net-346` · 시나리오 `career-net-346-experience` `v001`.
- 원본 위치: `/items/502/data` · 역량: 예술시각능력.
- 장소 제안: 영상 편집실 · `PRM-032 v001` · [PAN-032 v001](../../../images/original/panoramas/PAN-032/v001/prm-032-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 편집기사의 업무 표현과 영상 편집실의 영상과 소리를 검토하고 편집하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 편집기사는 영화, 방송에 쓰이는 영상을 대본(시나리오)에 맞게 편집하는 일을 담당합니다.
- 체험의 업무 자료: 독자·주제·원고 구성과 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 미디어 보관함 · CND-121 | 미디어 보관함에서 요청 장면 선택 | 소재 ID·권장 용도 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 모니터에서 컷의 순서·길이를 편집 | 필수 장면·순서 충족 | 제작·표현 |
| 3 | 헤드폰 · CND-117 | 헤드폰에서 가상 음성·장면 동기 오류 확인 | 삽입된 동기 오류 표시·수정 | 관찰·검사 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 미디어 보관함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 헤드폰 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10059-experience"></a>
### 평등관리사무원 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-10059` · 시나리오 `career-net-10059-experience` `v001`.
- 원본 위치: `/items/503/data` · 역량: 자기성찰능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 평등관리사무원의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 평등관리사무원은 일반인들이 다른 문화에 대한 바른 이해와 태도를 가질 수 있도록 하고, 다른 문화권 사람들이 공정한 대우를 받을 수 있도록 돕습니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-957-experience"></a>
### 평론가 — 주제·독자에 맞는 짧은 원고를 구성하고 자료 정리

- 직업: `career-net-957` · 시나리오 `career-net-957-experience` `v001`.
- 원본 위치: `/items/504/data` · 역량: 언어능력, 창의력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 평론가의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 예술작품의 주제, 표현, 기술 등의 요인을 분석한 다음, 개인적 지식과 판단, 경험 등을 근거로 작품에 대한 평론서를 작성합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 주제·독자 조건과 자료의 불일치 확인 | 제시된 자료의 불일치 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드 UI에서 문장·장면 카드를 순서대로 구성 | 필수 주제·문장 역할·분량 조건 충족 | 제작·표현 |
| 3 | 수납장 · CND-009 | 수납장에서 근거 자료·원고·보류 자료를 구분 | 원고와 근거·보류 자료 분류 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 언어능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1153-experience"></a>
### 포장원 — 주문 화물을 골라 적재 순서 계획

- 직업: `career-net-1153` · 시나리오 `career-net-1153-experience` `v001`.
- 원본 위치: `/items/505/data` · 역량: 손재능.
- 장소 제안: 물류 창고 · `PRM-053 v001` · [PAN-053 v001](../../../images/original/panoramas/PAN-053/v001/prm-053-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 포장원의 업무 표현과 물류 창고의 물품을 저장하고 꺼내는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 제품의 품질검사가 완료되면 제품을 옮겨 수량을 확인한 다음, 포장기계를 조작하여 제품을 포장합니다.
- 체험의 업무 자료: 가상 운송 요청·동선과 인계 기록.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 상자의 목적지·규격을 요청과 대조 | 목적지·규격 일치 | 분류·선별 |
| 2 | 팔레트 · CND-200 | 팔레트 모형에 화물을 표시 구획대로 배치 | 가상 적재 제약 충족 | 조립·배치 |
| 3 | 수동 운반차 · CND-201 | 수동 운반차의 가상 이동 순서를 계획 | 막힌 구간·중복 이동 제약 충족 | 계획·배분 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 팔레트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수동 운반차 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-177-experience"></a>
### 푸드스타일리스트 — 주문에 맞게 조리 준비 순서 맞추기

- 직업: `career-net-177` · 시나리오 `career-net-177-experience` `v001`.
- 원본 위치: `/items/506/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 주방 · `PRM-024 v001` · [PAN-024 v001](../../../images/original/panoramas/PAN-024/v001/prm-024-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 푸드스타일리스트의 업무 표현과 주방의 식재료 준비에서 조리와 담기까지 이어지는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 소비자 시장을 조사하고, 조사 결과를 바탕으로 레스토랑의 기존 메뉴를 보완하거나 새로운 메뉴를 추가하며, 잡지나 요리 프로그램의 기획 주제에 적합한 메뉴를 개발합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 냉장고 · CND-090 | 냉장고에서 주문과 재료 라벨 대조 | 재료·주문·구역 구분 일치 | 분류·선별 |
| 2 | 조리대 · CND-088 | 조리대에서 가상 조리 단계를 순서대로 배치 | 가상 레시피 단계 일치 | 순서·절차 |
| 3 | 가열 기구 · CND-089 | 가열 기구를 교육용 표시 범위에 조절 | 훈련용 눈금 범위 충족 | 측정·조절 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 냉장고 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조리대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 가열 기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1097-experience"></a>
### 프로게이머 — 가상 연습 리플레이를 보고 입력 타이밍 개선

- 직업: `career-net-1097` · 시나리오 `career-net-1097-experience` `v001`.
- 원본 위치: `/items/507/data` · 역량: 공간지각력, 손재능.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 프로게이머의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 소속 회사에서 개발한 새로운 게임소프트웨어에 대한 테스트를 하며, 새 게임소프트웨어가 출시되면 시연회와 홍보를 하기도 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 연습 리플레이의 입력 누락 지점 찾기 | 리플레이에 지정한 누락 지점 식별 | 관찰·검사 |
| 2 | 키보드 · CND-006 | 키보드로 가상 연습 신호에 맞는 키 입력 | 연습 키·신호 순서와 허용 구간 충족 | 타이밍·추적 |
| 3 | 마우스 · CND-018 | 마우스로 연습 표적 경로 추적 | 표적 추적 허용 오차 충족 | 타이밍·추적 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 공간지각력, 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 키보드 / common / AST-006 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 마우스 / common / AST-007 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 선택 장면의 기존 필수 후보 밖 추가 제안: CND-018. 기존 후보 목록은 자동 수정하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 검토: 전용 활동 공간이 현재 파노라마 목록에 없음. 선택 장면은 관제·상담·연습 등 한정된 보조 장면 제안이며 현장 대표 공간의 대체 완성본이 아님.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-415-experience"></a>
### 프로바둑기사 — 가상 바둑 연습 장면의 선택과 복기

- 직업: `career-net-415` · 시나리오 `career-net-415-experience` `v001`.
- 원본 위치: `/items/508/data` · 역량: 신체·운동능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 프로바둑기사의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 바둑을 연구하고, 경기에 승리하기 위해 자신 또는 경쟁 상대의 장단점을 조사하고 분석합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 가상 기보의 지정된 변화 지점 찾기 | 제시한 기보의 변화 지점 일치 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블 위 UI에서 제시된 후보 수의 후속 순서를 비교 | 교육용 문제의 후속 수 제약 충족 | 계획·배분 |
| 3 | 메모 · CND-014 | 메모에 선택 근거와 제시된 반례를 연결 | 제공 문제의 근거·반례 관계 일치 | 진단·해결 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 검토: 전용 활동 공간이 현재 파노라마 목록에 없음. 선택 장면은 관제·상담·연습 등 한정된 보조 장면 제안이며 현장 대표 공간의 대체 완성본이 아님.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-147-experience"></a>
### 플라스틱제품제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-147` · 시나리오 `career-net-147-experience` `v001`.
- 원본 위치: `/items/509/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 플라스틱제품제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 플라스틱제품제조원은 각종 플라스틱 제품을 제작하기 위해 여러 화학 재료를 혼합 및 가공하는 기기 및 장치를 조작합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-316-experience"></a>
### 플로리스트 — 의뢰 조건에 맞는 꽃 모형 구성을 만들고 점검

- 직업: `career-net-316` · 시나리오 `career-net-316-experience` `v001`.
- 원본 위치: `/items/510/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 플로리스트의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 행사의 특성을 살펴 장식 계획을 세우고, 고객과 협의하여 행사장에 화훼를 장식합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 의뢰의 색·크기 조건에 맞는 꽃 모형 선택 | 가상 재료의 색·크기 조건 충족 | 분류·선별 |
| 2 | 작업대 · CND-055 | 작업대 UI에서 높이와 배치를 조합해 작은 꽃 구성 제작 | 필수 구성 요소·크기 제약 충족 | 제작·표현 |
| 3 | 선반 · CND-028 | 선반에 올린 구성 모형을 회전해 누락·가림 확인 | 가림·누락 점검 항목 확인 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 꽃 재료·완성 구성 모형은 기존 상자·작업대·선반에 포함된 모델로 간주하지 않음. 추가 부품·후보 명세 필요
- 에셋 준비: 작업대 / common / 실제 모델 연결 미정. 꽃 재료·완성 구성 모형은 기존 상자·작업대·선반에 포함된 모델로 간주하지 않음. 추가 부품·후보 명세 필요
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 꽃 재료·완성 구성 모형은 기존 상자·작업대·선반에 포함된 모델로 간주하지 않음. 추가 부품·후보 명세 필요
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 전문 형상 또는 문제 데이터 확정이 필요한 항목을 interaction_objects에 표시.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-416-experience"></a>
### 피부관리사 — 요청 스타일과 준비 물품 확인

- 직업: `career-net-416` · 시나리오 `career-net-416-experience` `v001`.
- 원본 위치: `/items/511/data` · 역량: 손재능.
- 장소 제안: 미용실 · `PRM-023 v001` · [PAN-023 v001](../../../images/original/panoramas/PAN-023/v001/prm-023-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 피부관리사의 업무 표현과 미용실의 고객의 머리를 손질하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 고객과의 상담을 통해 피부 유형을 파악하고, 적합한 화장품의 종류나 피부 관리법을 소개합니다.
- 체험의 업무 자료: 고객의 요청 형태·제외 조건과 준비 도구.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 독립형 거울 · CND-086 | 거울 앞 UI에서 원하는 형태와 불편 사항 확인 | 고객 요청 확인 응답 | 대화·응대 |
| 2 | 운반 카트 · CND-016 | 카트에서 요청에 맞는 모형 도구 선택 | 도구 역할·구역 일치 | 분류·선별 |
| 3 | 세발대 · CND-087 | 세발대에서 가상 준비 단계를 순서대로 선택 | 교육용 준비 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 독립형 거울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 운반 카트 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 세발대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10111-experience"></a>
### 핀테크 전문가 — 가상 조건을 비교해 상담안 설명

- 직업: `career-net-10111` · 시나리오 `career-net-10111-experience` `v001`.
- 원본 위치: `/items/512/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 금융 상담실 · `PRM-057 v001` · [PAN-057 v001](../../../images/original/panoramas/PAN-057/v001/prm-057-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 핀테크 전문가의 업무 표현과 금융 상담실의 전문가와 고객이 계약·재무 자료를 검토하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 금융기관 방문 없이 스마트폰이나 컴퓨터로 쉽게 이용할 수 있도록 텔레뱅킹, 인터넷 뱅킹, 앱 카드 등 정보기술을 적용하기 위한 설계안을 개발합니다.
- 체험의 업무 자료: 가상 요청 조건·수량·기간과 설명 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 요청 조건과 누락 정보 확인 | 필수 조건 누락 식별 | 관찰·검사 |
| 2 | 작은 계산기 · CND-206 | 계산기의 가상 수량·합계를 맞춤 | 교육용 수량 계산 일치 | 측정·조절 |
| 3 | 노트북 · CND-012 | 노트북에서 조건에 맞는 자원 계획 구성 | 가상의 예산·기간 제약 충족 | 계획·배분 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 작은 계산기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10062-experience"></a>
### 학습장애간호사 — 가상 병실의 요청을 확인하고 편의 준비

- 직업: `career-net-10062` · 시나리오 `career-net-10062-experience` `v001`.
- 원본 위치: `/items/513/data` · 역량: 자기성찰능력.
- 장소 제안: 병실 · `PRM-010 v001` · [PAN-010 v001](../../../images/original/panoramas/PAN-010/v001/prm-010-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 학습장애간호사의 업무 표현과 병실의 환자가 머물며 간호를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 필요에 따라 환자의 가족과 보호자에게 상담을 제공하고, 치료에 동참하도록 독려합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 호출 장치 · CND-048 | 호출 장치로 요청 내용을 듣고 재확인 | 요청·담당자 확인 | 대화·응대 |
| 2 | 의료 모니터 · CND-042 | 모니터의 가상 기록에서 전달할 변화 항목 확인 | 사례에 제시된 변화 항목 일치 | 관찰·검사 |
| 3 | 이동식 식탁 · CND-047 | 이동 식탁을 지정된 접근 가능한 위치로 이동 | 위치 허용 범위와 동선 확보 | 조립·배치 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 호출 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 식탁 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1106-experience"></a>
### 학습지방문교사 — 학습자의 이해를 확인하고 설명하기

- 직업: `career-net-1106` · 시나리오 `career-net-1106-experience` `v001`.
- 원본 위치: `/items/514/data` · 역량: 대인관계능력, 자기성찰능력.
- 장소 제안: 방문 학습 공간 · `PRM-059 v001` · [PAN-059 v001](../../../images/original/panoramas/PAN-059/v001/prm-059-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 학습지방문교사의 업무 표현과 방문 학습 공간의 가정에서 교사와 학습자가 교재를 함께 보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 업무 지역이 배정되면 회원 및 회원 보호자와 가정방문 시간을 협의하고, 회원별 학습 진도를 계획합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 사례 풀이의 오류 위치 확인 | 오류 지점 식별 | 관찰·검사 |
| 2 | 필기구 · CND-209 | 필기구 UI로 풀이 설명 순서 구성 | 설명 필수 단계 포함 | 제작·표현 |
| 3 | 업무 책상 · CND-004 | 책상에서 확인 질문과 다음 활동 합의 | 학습자의 이해 확인과 목표 합의 | 대화·응대 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력, 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 필기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-348-experience"></a>
### 학예사(큐레이터) — 작품의 관람 흐름과 조명 구성

- 직업: `career-net-348` · 시나리오 `career-net-348-experience` `v001`.
- 원본 위치: `/items/515/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 전시실 · `PRM-034 v001` · [PAN-034 v001](../../../images/original/panoramas/PAN-034/v001/prm-034-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 학예사(큐레이터)의 업무 표현과 전시실의 작품과 전시물을 차례로 살펴보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 관람객들에게 소장품이나 자료에 대한 이해를 돕기 위해 교육 프로그램을 개발하고 실행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 전시대 · CND-124 | 전시대에 작품 위치를 배치 | 동선·가림 조건 충족 | 조립·배치 |
| 2 | 독립형 액자 거치대 · CND-126 | 액자 거치대에서 시야·설명 순서를 구성 | 필수 작품·설명 관계 충족 | 제작·표현 |
| 3 | 전시 조명 · CND-128 | 전시 조명의 방향을 요청 구간에 맞춤 | 가상 조도·방향 범위 충족 | 측정·조절 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 전시대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 독립형 액자 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 전시 조명 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-417-experience"></a>
### 학원강사 — 학습자의 이해를 확인하고 설명하기

- 직업: `career-net-417` · 시나리오 `career-net-417-experience` `v001`.
- 원본 위치: `/items/516/data` · 역량: 대인관계능력, 자기성찰능력.
- 장소 제안: 방문 학습 공간 · `PRM-059 v001` · [PAN-059 v001](../../../images/original/panoramas/PAN-059/v001/prm-059-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 학원강사의 업무 표현과 방문 학습 공간의 가정에서 교사와 학습자가 교재를 함께 보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 학원강사는 여러 연령층의 사람들이 가진 다양한 교육적 요구에 따라 필요로 하는 지식과 기능을 교육하는 일을 합니다.
- 체험의 업무 자료: 학습 목표·오류 사례와 설명 순서.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 교재 · CND-053 | 교재에서 사례 풀이의 오류 위치 확인 | 오류 지점 식별 | 관찰·검사 |
| 2 | 필기구 · CND-209 | 필기구 UI로 풀이 설명 순서 구성 | 설명 필수 단계 포함 | 제작·표현 |
| 3 | 업무 책상 · CND-004 | 책상에서 확인 질문과 다음 활동 합의 | 학습자의 이해 확인과 목표 합의 | 대화·응대 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력, 자기성찰능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 교재 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 필기구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-175-experience"></a>
### 한복사 — 재료와 공구로 작은 공예품 만들기

- 직업: `career-net-175` · 시나리오 `career-net-175-experience` `v001`.
- 원본 위치: `/items/517/data` · 역량: 손재능.
- 장소 제안: 공예 작업실 · `PRM-029 v001` · [PAN-029 v001](../../../images/original/panoramas/PAN-029/v001/prm-029-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 한복사의 업무 표현과 공예 작업실의 작은 재료를 가공하고 조립하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 한복 제작 시 직물의 종류, 색상, 원단의 실용성과 디자인에 관하여 고객과 상의하고, 고객의 치수를 재고, 명세서에 규격, 색상, 직물의 종류, 본 등을 기록합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 재료 상자에서 형상에 맞는 재료 선택 | 재료 규격 일치 | 분류·선별 |
| 2 | 손공구 · CND-108 | 손공구로 가상의 가공 순서 수행 | 가상 순서·도구 역할 일치 | 순서·절차 |
| 3 | 바이스 · CND-079 | 바이스에서 부품 방향을 맞춰 결합 | 결합 방향·위치 일치 | 조립·배치 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손공구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 바이스 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-37-experience"></a>
### 한의사 — 가상 방문 기록을 확인하고 설명 준비

- 직업: `career-net-37` · 시나리오 `career-net-37-experience` `v001`.
- 원본 위치: `/items/518/data` · 역량: 자기성찰능력, 수리·논리력.
- 장소 제안: 진료실 · `PRM-008 v001` · [PAN-008 v001](../../../images/original/panoramas/PAN-008/v001/prm-008-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 한의사의 업무 표현과 진료실의 진료 상담과 기본 상태 확인을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 한의사는 한방 의료의 원리와 기술을 활용해서 인체의 질병과 장애를 진료, 예방하는 업무를 수행합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 의료 모니터 · CND-042 | 의료 모니터에서 기록 ID와 요청 기록 대조 | 기록 ID·누락 항목 식별 | 관찰·검사 |
| 2 | 진찰·처치 침대 · CND-041 | 진찰 침대 옆 UI에서 방문자의 설명을 듣고 확인 질문 | 필수 질문과 설명 확인 | 대화·응대 |
| 3 | 업무 책상 · CND-004 | 책상에서 전달 기록을 필수 항목별로 정리 | 인계 기록 필드 충족 | 분류·선별 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 진찰·처치 침대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-148-experience"></a>
### 항공교통관제사 — 가상 관제 신호를 확인하고 대응 인계

- 직업: `career-net-148` · 시나리오 `career-net-148-experience` `v001`.
- 원본 위치: `/items/519/data` · 역량: 공간지각력.
- 장소 제안: 관제실 · `PRM-061 v001` · [PAN-061 v001](../../../images/original/panoramas/PAN-061/v001/prm-061-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 항공교통관제사의 업무 표현과 관제실의 여러 상태 화면을 확인하고 상황을 조정하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 관제탑에서 항공기의 이륙 및 착륙 신고서를 확인하고 활주로 및 공항 주변의 기상 상태를 점검합니다.
- 체험의 업무 자료: 가상 사건·상태 신호와 전달 우선순위.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 모니터에서 시간에 따라 바뀌는 이상 신호 확인 | 가상 이상 신호 식별 | 관찰·검사 |
| 2 | 관제 콘솔 · CND-213 | 관제 콘솔에서 가상 대응 우선순위 배치 | 명시된 우선순위 조건 충족 | 계획·배분 |
| 3 | 통신 기기 · CND-175 | 통신 장치로 위치·상태·담당자 전달 | 인계 필드·수신 확인 | 대화·응대 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관제 콘솔 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 통신 기기 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1136-experience"></a>
### 항공기·선박조립 및 검사원 — 맞는 부품을 조립하고 완성품 검사

- 직업: `career-net-1136` · 시나리오 `career-net-1136-experience` `v001`.
- 원본 위치: `/items/520/data` · 역량: 손재능.
- 장소 제안: 조립 구역 · `PRM-019 v001` · [PAN-019 v001](../../../images/original/panoramas/PAN-019/v001/prm-019-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 항공기·선박조립 및 검사원의 업무 표현과 조립 구역의 부품을 순서대로 결합하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 항공기ㆍ선박 조립 및 검사원은 항공기 또는 선박을 만들기 위해 외장 부분과 내부 부속품을 조립하는 일을 합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 도면에 맞는 부품 선택 | 부품 ID·규격 일치 | 분류·선별 |
| 2 | 공구 거치대 · CND-077 | 공구 거치대의 맞는 공구를 선택해 체결 순서 수행 | 공구·체결 순서 일치 | 순서·절차 |
| 3 | 조립 중인 단순 제품 · CND-078 | 조립 중인 제품을 회전해 결함을 찾아 수정 | 정의된 결함 수정 후 검사 통과 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 공구 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 조립 중인 단순 제품 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-149-experience"></a>
### 항공기정비원 — 가상 고장 단서를 찾아 수리 결과 확인

- 직업: `career-net-149` · 시나리오 `career-net-149-experience` `v001`.
- 원본 위치: `/items/521/data` · 역량: 손재능.
- 장소 제안: 정비 구역 · `PRM-020 v001` · [PAN-020 v001](../../../images/original/panoramas/PAN-020/v001/prm-020-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 항공기정비원의 업무 표현과 정비 구역의 장비를 검사하고 고치는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 설치 또는 수리 부분의 작동 상태를 검사 및 확인합니다.
- 체험의 업무 자료: 점검 요청·모형 고장 단서와 교체 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 공구함 · CND-080 | 공구함에서 작업 조건에 맞는 모형 공구 선택 | 공구 기능과 요청 일치 | 분류·선별 |
| 2 | 열린 기계 케이스 · CND-081 | 열린 케이스에서 단서를 연결해 고장 원인 선택 | 가상 단서가 선택 원인 지지 | 진단·해결 |
| 3 | 부품 트레이 · CND-040 | 트레이에서 교체 부품을 대조하고 수리 기록 점검 | 교체 부품·기록 일치 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 공구함 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 열린 기계 케이스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-151-experience"></a>
### 항공우주공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-151` · 시나리오 `career-net-151-experience` `v001`.
- 원본 위치: `/items/522/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 항공우주공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 항공우주공학기술자는 공기 중을 비행하는 물체 즉, 여객기, 전투기, 우주선 등의 각종 비행 물체를 설계하고 개발하는 일을 담당합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-38-experience"></a>
### 해부학연구원 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-38` · 시나리오 `career-net-38-experience` `v001`.
- 원본 위치: `/items/523/data` · 역량: 수리·논리력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 해부학연구원의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 해부학연구원은 사람과 동물의 해부학적 특성을 분석하여 의학과 관련 분야에 적용하기 위한 연구를 수행합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10017-experience"></a>
### 해양 레저 전문가 — 갑판 모형의 준비 상태 확인

- 직업: `career-net-10017` · 시나리오 `career-net-10017-experience` `v001`.
- 원본 위치: `/items/524/data` · 역량: 신체·운동능력.
- 장소 제안: 선박 갑판 · `PRM-044 v001` · [PAN-044 v001](../../../images/original/panoramas/PAN-044/v001/prm-044-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 해양 레저 전문가의 업무 표현과 선박 갑판의 선원이 외부 갑판 설비를 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 해양레저 시설을 경영하거나 관리하고, 해양 레저 관광 상품을 개발하기도 하며 관광 회사를 운영할 수도 있습니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 구명환 · CND-168 | 구명환의 가상 점검 항목 확인 | 점검 결함 식별 | 관찰·검사 |
| 2 | 밧줄 코일 · CND-169 | 밧줄 코일을 지정 위치로 배치 | 동선·위치 조건 충족 | 조립·배치 |
| 3 | 계류 장치 · CND-170 | 계류 장치 모형에서 교육용 순서 선택 | 모형 훈련 순서 일치 | 순서·절차 |

- 특수 상황: **긴급 대응**. 첫 두 단계를 마친 뒤 가상의 우선 요청 추가. 통과: 필수 대응을 기한 안에 수행. 복구: 시간 압박 없는 연습으로 다시 시작.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 신체·운동능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 구명환 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 밧줄 코일 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 계류 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10024-experience"></a>
### 해양 에너지 기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10024` · 시나리오 `career-net-10024-experience` `v001`.
- 원본 위치: `/items/525/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 해양 에너지 기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 바다를 조사하고 자원을 개발하기 위해 만드는 해양 구조물을 설치하고 관리하는 일을 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1081-experience"></a>
### 해양공학기술자 — 화물 인계와 부두 모형 점검

- 직업: `career-net-1081` · 시나리오 `career-net-1081-experience` `v001`.
- 원본 위치: `/items/526/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 부두 · `PRM-046 v001` · [PAN-046 v001](../../../images/original/panoramas/PAN-046/v001/prm-046-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 해양공학기술자의 업무 표현과 부두의 화물과 선박을 연결하는 항만 가장자리를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 해양공학기술자는 관련 전문 지식을 이용하여 기초 자료를 조사, 분석하고 해양환경 현황을 조사, 관측, 평가, 계획합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 화물 상자를 목적지별로 분류 | 화물 목적지 ID 일치 | 분류·선별 |
| 2 | 손수레 · CND-133 | 손수레로 가상의 막힌 동선을 피해 순서 계획 | 동선·우선순위 조건 충족 | 계획·배분 |
| 3 | 계류 기둥 · CND-178 | 계류 기둥에서 모형 점검 항목 확인 | 정의된 점검 항목 식별 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손수레 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 계류 기둥 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-195-experience"></a>
### 해양수산기술자 — 화물 인계와 부두 모형 점검

- 직업: `career-net-195` · 시나리오 `career-net-195-experience` `v001`.
- 원본 위치: `/items/527/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 부두 · `PRM-046 v001` · [PAN-046 v001](../../../images/original/panoramas/PAN-046/v001/prm-046-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 해양수산기술자의 업무 표현과 부두의 화물과 선박을 연결하는 항만 가장자리를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 수산기술자는 각종 수산자원의 관리와 해산 어류의 생태를 파악하고, 수산자원의 관리, 증식, 양식, 수산물의 생산과 가공 등에 관련된 연구와 기술개발을 담당합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 보관 상자 · CND-058 | 화물 상자를 목적지별로 분류 | 화물 목적지 ID 일치 | 분류·선별 |
| 2 | 손수레 · CND-133 | 손수레로 가상의 막힌 동선을 피해 순서 계획 | 동선·우선순위 조건 충족 | 계획·배분 |
| 3 | 계류 기둥 · CND-178 | 계류 기둥에서 모형 점검 항목 확인 | 정의된 점검 항목 식별 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 보관 상자 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 손수레 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 계류 기둥 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-39-experience"></a>
### 해양학연구원 — 관측 장치를 맞추고 기록 오류 확인

- 직업: `career-net-39` · 시나리오 `career-net-39-experience` `v001`.
- 원본 위치: `/items/528/data` · 역량: 수리·논리력.
- 장소 제안: 관측 지점 · `PRM-039 v001` · [PAN-039 v001](../../../images/original/panoramas/PAN-039/v001/prm-039-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 해양학연구원의 업무 표현과 관측 지점의 설치한 측정 장비로 환경 변화를 관찰하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 해양학연구원은 해양기후, 해양환경, 해양생물자원, 해양안전방제, 해양운송시스템 등 해양 전반과 관련된 과학기술과 정책 개발에 관한 연구를 수행합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 삼각대 센서 · CND-144 | 삼각대 센서를 표시 방향에 배치 | 위치·방향 일치 | 조립·배치 |
| 2 | 소형 관측 장치 · CND-145 | 관측 장치의 가상 눈금을 조절 | 훈련용 설정 범위 충족 | 측정·조절 |
| 3 | 데이터 기록 기기 · CND-146 | 기록 기기의 이상 데이터 지점을 표시 | 삽입된 이상 지점·기록 일치 | 관찰·검사 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 삼각대 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 관측 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 데이터 기록 기기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1006-experience"></a>
### 해양환경기사 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-1006` · 시나리오 `career-net-1006-experience` `v001`.
- 원본 위치: `/items/529/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 해양환경기사의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 해양환경기사는 물리, 화학, 지질 및 해양생물학적 지식과 기술을 활용하여 해양개발에 필요한 기초 조사 및 연구를 수행합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-951-experience"></a>
### 행사기획자 — 팀 요구를 반영한 실행안 만들기

- 직업: `career-net-951` · 시나리오 `career-net-951-experience` `v001`.
- 원본 위치: `/items/530/data` · 역량: 대인관계능력.
- 장소 제안: 협업·기획 사무실 · `PRM-002 v001` · [PAN-002 v001](../../../images/original/panoramas/PAN-002/v001/B-collaboration-office-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 행사기획자의 업무 표현과 협업·기획 사무실의 팀이 자료를 공유하고 아이디어를 토론하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 설문조사, 시장조사, 관련 자료 및 데이터 분석 등 행사에 필요한 자료를 수집·분석하고, 팀원과의 회의를 거쳐 행사의 틀을 잡습니다.
- 체험의 업무 자료: 대상 이용자·필수 요구와 실행 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 노트북 · CND-012 | 노트북에서 요구·예산을 확인하고 작업 순서 배분 | 필수 작업 누락과 자원 중복 없음 | 계획·배분 |
| 2 | 이동식 화이트보드 · CND-013 | 보드에 실행안을 배치하고 충돌 수정 | 보드의 필수 요구 충족 | 제작·표현 |
| 3 | 메모 · CND-014 | 메모를 담당자·기한별로 분류 | 각 메모의 담당·기한 일치 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 노트북 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 화이트보드 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 메모 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1278-experience"></a>
### 행정부고위공무원 — 접수 문서를 확인하고 담당자에게 전달

- 직업: `career-net-1278` · 시나리오 `career-net-1278-experience` `v001`.
- 원본 위치: `/items/531/data` · 역량: 자기성찰능력, 수리·논리력, 언어능력.
- 장소 제안: 행정·문서 처리 사무실 · `PRM-003 v001` · [PAN-003 v001](../../../images/original/panoramas/PAN-003/v001/C-public-administration-v2.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 행정부고위공무원의 업무 표현과 행정·문서 처리 사무실의 기관 내부 담당자가 기록·검토·결재하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 각급 지방자치단체의 행정관리, 주민 복지 증진, 지역개발, 산업 진흥 등 지방행정 분야의 정책수행을 기획, 조직, 통제합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류철 · CND-022 | 서류철의 문서를 업무 종류별로 분류 | 문서별 분류 일치 | 분류·선별 |
| 2 | 모니터 · CND-005 | 기록 화면과 문서의 불일치 수정 | 기록과 문서의 필수 항목 일치 | 관찰·검사 |
| 3 | 유선전화 · CND-019 | 전화로 누락 정보를 확인하고 결과 인계 | 확인 질문과 전달 필드 충족 | 대화·응대 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자기성찰능력, 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류철 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 유선전화 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1105-experience"></a>
### 행정학연구원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1105` · 시나리오 `career-net-1105-experience` `v001`.
- 원본 위치: `/items/532/data` · 역량: 수리·논리력, 언어능력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 행정학연구원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 여러 유형의 공공 과제 및 문제를 해결하기 위한 효율적 행정 운영 체계를 수립하고 합리적 의사결정과 관리 방법 및 기술을 연구 및 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 언어능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1279-experience"></a>
### 헤드헌터 — 요구를 듣고 지원 방법 함께 정하기

- 직업: `career-net-1279` · 시나리오 `career-net-1279-experience` `v001`.
- 원본 위치: `/items/533/data` · 역량: 대인관계능력.
- 장소 제안: 복지·심리 상담실 · `PRM-015 v001` · [PAN-015 v001](../../../images/original/panoramas/PAN-015/v001/prm-015-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 헤드헌터의 업무 표현과 복지·심리 상담실의 상담자와 방문자가 차분히 대화하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 철저한 분석 작업을 거친 다음 추천 대상자의 업무 능력, 조직에서의 역할, 장단점, 주변 평가 등을 정리해서 기업 고객에게 보냅니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 상담 노트 · CND-064 | 상담 노트에서 사실·미확인·요청을 구분 | 미확인 내용을 단정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 공감·확인 질문으로 우선 요구 파악 | 요청 재확인과 동의 응답 | 대화·응대 |
| 3 | 선반 · CND-028 | 참고서 선반에서 조건에 맞는 지원안 선택 | 사례의 시간·접근 조건 충족 | 계획·배분 |

- 특수 상황: **개별 맞춤**. 이용자가 작은 글자를 읽기 어렵다고 설명. 통과: 설정된 이용자 조건과 목표 함께 충족. 복구: 차별적 단정 대신 구체 조건 재확인.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 상담 노트 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10012-experience"></a>
### 헬스 케어 컨설턴트 — 가상 방문 기록을 확인하고 설명 준비

- 직업: `career-net-10012` · 시나리오 `career-net-10012-experience` `v001`.
- 원본 위치: `/items/534/data` · 역량: 대인관계능력.
- 장소 제안: 진료실 · `PRM-008 v001` · [PAN-008 v001](../../../images/original/panoramas/PAN-008/v001/prm-008-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 헬스 케어 컨설턴트의 업무 표현과 진료실의 진료 상담과 기본 상태 확인을 하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 헬스 케어 컨설턴트는 식품영양, 건강관리, 물리치료 등의 지식을 바탕으로 질병 예방과 치료를 위해 상담을 하고, 개인이 건강관리를 체계적으로 할 수 있도록 돕습니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 의료 모니터 · CND-042 | 의료 모니터에서 기록 ID와 요청 기록 대조 | 기록 ID·누락 항목 식별 | 관찰·검사 |
| 2 | 진찰·처치 침대 · CND-041 | 진찰 침대 옆 UI에서 방문자의 설명을 듣고 확인 질문 | 필수 질문과 설명 확인 | 대화·응대 |
| 3 | 업무 책상 · CND-004 | 책상에서 전달 기록을 필수 항목별로 정리 | 인계 기록 필드 충족 | 분류·선별 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 진찰·처치 침대 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 업무 책상 / common / AST-004 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-428-experience"></a>
### 호스피스전문간호사 — 가상 병실의 요청을 확인하고 편의 준비

- 직업: `career-net-428` · 시나리오 `career-net-428-experience` `v001`.
- 원본 위치: `/items/535/data` · 역량: 대인관계능력.
- 장소 제안: 병실 · `PRM-010 v001` · [PAN-010 v001](../../../images/original/panoramas/PAN-010/v001/prm-010-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 호스피스전문간호사의 업무 표현과 병실의 환자가 머물며 간호를 받는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환자의 건강 상태와 통증을 확인하고 이를 완화할 수 있도록 간호합니다.
- 체험의 업무 자료: 가상 이용자 요청·기록 ID와 전달 내용.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 호출 장치 · CND-048 | 호출 장치로 요청 내용을 듣고 재확인 | 요청·담당자 확인 | 대화·응대 |
| 2 | 의료 모니터 · CND-042 | 모니터의 가상 기록에서 전달할 변화 항목 확인 | 사례에 제시된 변화 항목 일치 | 관찰·검사 |
| 3 | 이동식 식탁 · CND-047 | 이동 식탁을 지정된 접근 가능한 위치로 이동 | 위치 허용 범위와 동선 확보 | 조립·배치 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 호출 장치 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 의료 모니터 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이동식 식탁 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-795-experience"></a>
### 호텔지배인 — 주문을 확인하고 맞는 식기·서빙 준비

- 직업: `career-net-795` · 시나리오 `career-net-795-experience` `v001`.
- 원본 위치: `/items/536/data` · 역량: 대인관계능력.
- 장소 제안: 식당 홀 · `PRM-026 v001` · [PAN-026 v001](../../../images/original/panoramas/PAN-026/v001/prm-026-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 호텔지배인의 업무 표현과 식당 홀의 손님이 식사하고 직원이 음식을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 객실부, 연회부 등 각 부서 소속 호텔 종업원의 작업 계획을 만들어 업무가 원활히 운영될 수 있도록 관리 조정하고, 호텔 종업원에게 효과적인 작업 방법을 교육하고 훈련시킵니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 메뉴 거치대 · CND-100 | 메뉴 거치대에서 요청 조건 확인 | 주문·제외 조건 확인 | 대화·응대 |
| 2 | 식기 · CND-098 | 식기에서 주문에 맞는 구성을 선택 | 식기 종류·개수 일치 | 분류·선별 |
| 3 | 배식 보조대 · CND-099 | 배식 보조대에서 제공 순서 확인 | 주문 ID와 제공 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 메뉴 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 식기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 배식 보조대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1124-experience"></a>
### 혼례종사원 — 주문을 확인하고 맞는 식기·서빙 준비

- 직업: `career-net-1124` · 시나리오 `career-net-1124-experience` `v001`.
- 원본 위치: `/items/537/data` · 역량: 대인관계능력.
- 장소 제안: 식당 홀 · `PRM-026 v001` · [PAN-026 v001](../../../images/original/panoramas/PAN-026/v001/prm-026-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 혼례종사원의 업무 표현과 식당 홀의 손님이 식사하고 직원이 음식을 전달하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 혼례종사원은 결혼식의 원활한 진행을 위해 의자, 카펫 등을 정리하고 필요한 자료와 물품을 준비하는 등의 일을 담당합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 메뉴 거치대 · CND-100 | 메뉴 거치대에서 요청 조건 확인 | 주문·제외 조건 확인 | 대화·응대 |
| 2 | 식기 · CND-098 | 식기에서 주문에 맞는 구성을 선택 | 식기 종류·개수 일치 | 분류·선별 |
| 3 | 배식 보조대 · CND-099 | 배식 보조대에서 제공 순서 확인 | 주문 ID와 제공 순서 일치 | 순서·절차 |

- 특수 상황: **돌발 변경 대응**. 최종 완료 전 목표 대상 변경. 통과: 최신 요청 revision에 맞는 결과. 복구: 이전 목표 결과를 최종 완료로 인정하지 않음.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 메뉴 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 식기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 배식 보조대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-10002-experience"></a>
### 홀로그램 전문가 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-10002` · 시나리오 `career-net-10002-experience` `v001`.
- 원본 위치: `/items/538/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 홀로그램 전문가의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 서비스 관련 전문가는 주로 문화 공연이나 전시를 기획하고 설계하여 콘텐츠를 제작함으로써 사람들이 홀로그램을 직접 볼 수 있도록 만드는 일을 합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-419-experience"></a>
### 홍보도우미 — 집결 위치와 이동 안내 준비

- 직업: `career-net-419` · 시나리오 `career-net-419-experience` `v001`.
- 원본 위치: `/items/539/data` · 역량: 대인관계능력.
- 장소 제안: 안내 집결 지점 · `PRM-069 v001` · [PAN-069 v001](../../../images/original/panoramas/PAN-069/v001/prm-069-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 홍보도우미의 업무 표현과 안내 집결 지점의 안내자가 사람들을 모아 경로를 설명하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 전시회, 판촉 행사, 신제품 설명회 등이 시작하기 전에 상품이나 서비스, 시설의 특징, 홍보 방법 등에 대한 교육을 받고 관련 내용을 외웁니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 지도 거치대 · CND-224 | 지도 거치대에서 가상 이동 경로 계획 | 가상 동선·시간 제약 충족 | 계획·배분 |
| 2 | 안내판 · CND-205 | 안내판에서 참여자의 질문에 맞는 안내 선택 | 질문 의도·최신 위치 안내 | 대화·응대 |
| 3 | 여행 가방 · CND-221 | 가방에서 일정에 맞는 준비물 선택 | 준비물과 일정 조건 일치 | 분류·선별 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 대인관계능력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 지도 거치대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 안내판 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 여행 가방 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-349-experience"></a>
### 화가 — 표현 재료를 고르고 작은 작품 구성

- 직업: `career-net-349` · 시나리오 `career-net-349-experience` `v001`.
- 원본 위치: `/items/540/data` · 역량: 예술시각능력, 창의력.
- 장소 제안: 미술 작업실 · `PRM-028 v001` · [PAN-028 v001](../../../images/original/panoramas/PAN-028/v001/prm-028-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 화가의 업무 표현과 미술 작업실의 그림을 그리고 작품을 살펴보는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 화가는 물감, 먹물 등을 사용하여 인물화, 풍경화, 정물화, 추상화 등의 예술 작품을 창작합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 팔레트 도구 · CND-107 | 팔레트 도구에서 표현 목표에 맞는 재료 선택 | 재료 역할과 목표 일치 | 분류·선별 |
| 2 | 빈 캔버스 · CND-105 | 캔버스에 형태와 구도를 구성 | 필수 요소·구도 조건 충족 | 제작·표현 |
| 3 | 이젤 · CND-104 | 이젤에서 작품을 다른 시점으로 확인 | 지정 확인 항목 점검 완료 | 관찰·검사 |

- 특수 상황: **기록·추적·복구**. 완료 직전 수정 실수 발견. 통과: 올바른 근거 상태로 복구하고 새 revision 보존. 복구: 삭제·덮어쓰기 대신 이력 유지.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 예술시각능력, 창의력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 팔레트 도구 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 빈 캔버스 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 이젤 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-952-experience"></a>
### 화학공학기술자 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-952` · 시나리오 `career-net-952-experience` `v001`.
- 원본 위치: `/items/541/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 화학공학기술자의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 생산된 제품이 품질 표준을 만족했는지 확인하는 품질 통제 활동과 품질관리 프로그램을 운영하고 원료, 제품, 폐기물에 대한 기준을 마련하는 활동을 합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-40-experience"></a>
### 화학연구원 — 가상 시료를 구별해 실험 준비하기

- 직업: `career-net-40` · 시나리오 `career-net-40-experience` `v001`.
- 원본 위치: `/items/542/data` · 역량: 수리·논리력.
- 장소 제안: 실험실 · `PRM-006 v001` · [PAN-006 v001](../../../images/original/panoramas/PAN-006/v001/prm-006-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 화학연구원의 업무 표현과 실험실의 시료 준비와 기본 실험을 수행하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 유기화합물 분석을 통해 합성 메커니즘을 밝혀내거나 새로운 고분자물질을 발견, 개발합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시험관대 · CND-032 | 시험관대에서 시료 라벨과 요청을 대조해 선택 | 시료 ID 일치 | 분류·선별 |
| 2 | 소형 저울 · CND-035 | 저울의 가상 재료량을 목표 눈금에 맞춤 | 훈련용 목표 범위 충족 | 측정·조절 |
| 3 | 비커 · CND-033 | 비커에서 표시된 준비 순서 수행 | 준비 단계 순서와 기록 일치 | 순서·절차 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시험관대 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 소형 저울 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 비커 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-153-experience"></a>
### 화학제품제조원 — 가상 생산 조건을 맞추고 제품 분류

- 직업: `career-net-153` · 시나리오 `career-net-153-experience` `v001`.
- 원본 위치: `/items/543/data` · 역량: 손재능.
- 장소 제안: 생산 구역 · `PRM-018 v001` · [PAN-018 v001](../../../images/original/panoramas/PAN-018/v001/prm-018-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 화학제품제조원의 업무 표현과 생산 구역의 재료가 기계를 거쳐 제품으로 이동하는 작업 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 화학물질의 가공 처리 정도와 적합성을 검사하며, 생산 기록을 작성합니다.
- 체험의 업무 자료: 생산 요청·부품 규격과 가상 공정 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 안전 가드 · CND-076 | 안전 가드의 잠금 상태를 점검 | 훈련용 가드 상태 일치 | 관찰·검사 |
| 2 | 제어 패널 · CND-075 | 제어 패널의 훈련용 값을 목표 범위로 조절 | 설정 범위 충족 후만 시작 | 측정·조절 |
| 3 | 완성품 상자 · CND-074 | 완성품 상자에서 규격 일치·보류품 분류 | 가상 검사 결과와 분류 일치 | 분류·선별 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 손재능을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 안전 가드 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어 패널 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 완성품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-954-experience"></a>
### 화훼재배기술자 — 모종 위치와 가상 재배 환경 맞추기

- 직업: `career-net-954` · 시나리오 `career-net-954-experience` `v001`.
- 원본 위치: `/items/544/data` · 역량: 자연친화력.
- 장소 제안: 온실 · `PRM-041 v001` · [PAN-041 v001](../../../images/original/panoramas/PAN-041/v001/prm-041-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 화훼재배기술자의 업무 표현과 온실의 통제된 재배 환경에서 식물을 관리하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 화훼재배기술자는 여러 품종의 과목, 교목, 꽃 등의 화훼 작물을 육성 및 재배하고 관리하는 일을 담당합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모종 트레이 · CND-154 | 모종 트레이에서 요청 모종 선택 | 모종 ID·구획 일치 | 분류·선별 |
| 2 | 환경 센서 · CND-156 | 환경 센서의 가상 기록 변화 확인 | 가상 변화 지점 식별 | 관찰·검사 |
| 3 | 관수 설비 · CND-155 | 관수 설비를 교육용 목표 구간에 조절 | 교육용 설정 범위 충족 | 측정·조절 |

- 특수 상황: **이상 신호 감시**. 2단계 중 가상 상태 신호 변화. 통과: 정해진 이상을 놓치지 않고 오탐 구분. 복구: 놓친 구간을 재생해 재검토.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 자연친화력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모종 트레이 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 환경 센서 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 관수 설비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1080-experience"></a>
### 환경공학기술자 및 연구원 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-1080` · 시나리오 `career-net-1080-experience` `v001`.
- 원본 위치: `/items/545/data` · 역량: 수리·논리력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 환경공학기술자 및 연구원의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환경공학기술자 및 연구원은 각종 환경오염 문제를 확인하여 연구개발을 통해 방지 대책을 세우거나 공해 방지 설비를 설계하고 제작하며 환경 개선 방안을 수립합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1004-experience"></a>
### 환경설비기술자 — 배관 모형을 연결하고 상태 확인

- 직업: `career-net-1004` · 시나리오 `career-net-1004-experience` `v001`.
- 원본 위치: `/items/546/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 설비 작업 구역 · `PRM-037 v001` · [PAN-037 v001](../../../images/original/panoramas/PAN-037/v001/prm-037-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 환경설비기술자의 업무 표현과 설비 작업 구역의 배관과 설비를 설치·점검하는 현장를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 연구자의 관리하에 오염물질의 유입량 및 유입 오염물질의 변화를 살피고 이와 관련한 실험을 관찰하고 결과를 기록합니다.
- 체험의 업무 자료: 조사 질문·가상 측정 자료와 근거.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 상자 · CND-137 | 부품 상자에서 연결 규격에 맞는 부품 선택 | 규격·용도 일치 | 분류·선별 |
| 2 | 노출 배관 모형 · CND-135 | 노출 배관 모형의 연결 방향 맞춤 | 위치·방향·연결점 일치 | 조립·배치 |
| 3 | 제어함 · CND-138 | 제어함에서 가상 상태표와 다른 항목 확인 | 가상 오류 항목 식별 | 관찰·검사 |

- 특수 상황: **안전 확보**. 2단계 진입 전 위험 표시. 통과: 정의된 안전 조건 충족 후 작업 진행. 복구: 위험 원인과 필요한 선행 조치 표시.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 상자 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 노출 배관 모형 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 제어함 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1281-experience"></a>
### 환경영향평가원 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-1281` · 시나리오 `career-net-1281-experience` `v001`.
- 원본 위치: `/items/547/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 환경영향평가원의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환경에 영향을 미치는 사업 계획 수립 시 이러한 사업 계획이 자연환경, 생활환경, 사회·경제 환경 등에 미치는 영향을 미리 예측·분석하고, 환경에 해로운 영향을 줄이는 방안을 모색합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-1009-experience"></a>
### 환경위생검사원 — 가상 분석 결과의 오류를 찾아 기록하기

- 직업: `career-net-1009` · 시나리오 `career-net-1009-experience` `v001`.
- 원본 위치: `/items/548/data` · 역량: 수리·논리력, 공간지각력.
- 장소 제안: 분석실 · `PRM-007 v001` · [PAN-007 v001](../../../images/original/panoramas/PAN-007/v001/prm-007-v001.png).
- 장소 선택 상태: `editorial_selection_within_source_category`. 환경위생검사원의 업무 표현과 분석실의 측정 장비로 시료를 분석하고 결과를 확인하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 환경위생검사원은 음식점, 산업체, 호텔 및 기타 작업장 환경을 조사하고 점검하여, 작업장의 위생 관리, 공해 관리, 위험물 처리가 정부 규정에 따라 잘 운영되고 있는지 감독합니다.
- 체험의 업무 자료: 원본 업무에서 선택한 요청·자료와 처리 결과.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 부품 트레이 · CND-040 | 트레이에서 요청 시료를 골라 위치 확인 | 시료·위치 ID 일치 | 분류·선별 |
| 2 | 분석 장비 · CND-038 | 분석 장비의 가상 측정 조건 조절 | 가상 설정 범위 충족 | 측정·조절 |
| 3 | 모니터 · CND-005 | 화면에서 기준 자료와 다른 결과 항목 찾아 보류 | 삽입된 오류 표시와 보류 이유 일치 | 관찰·검사 |

- 특수 상황: **교차접촉 방지**. 가상 구역 A와 B의 물품이 섞임. 통과: 가상의 청결·구역 구분 규칙 위반 없음. 복구: 구역 오염 상태를 되돌리고 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력, 공간지각력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 부품 트레이 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 분석 장비 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-994-experience"></a>
### 환경컨설턴트 — 조사 위치와 가상 시료 결과 기록

- 직업: `career-net-994` · 시나리오 `career-net-994-experience` `v001`.
- 원본 위치: `/items/549/data` · 역량: 수리·논리력.
- 장소 제안: 환경 조사 지점 · `PRM-038 v001` · [PAN-038 v001](../../../images/original/panoramas/PAN-038/v001/prm-038-v001.png).
- 장소 선택 상태: `editorial_proposal_outside_source_category`. 환경컨설턴트의 업무 표현과 환경 조사 지점의 현장에서 시료를 채취하고 기록하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 기업이나 공공 조직의 환경 관리 상태를 진단하고 체계적인 환경 관리를 위한 조직의 방침 및 장기 계획을 수립하며, 그것을 실행하기 위한 방법들에 대해 조직원들에게 교육합니다.
- 체험의 업무 자료: 이용자 요청·제약 조건과 지원 계획.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 시료 용기 · CND-140 | 시료 용기의 라벨·조사 위치를 맞춤 | 시료·조사 위치 ID 일치 | 분류·선별 |
| 2 | 휴대 측정기 · CND-141 | 휴대 측정기를 가상 목표 눈금에 조절 | 교육용 측정 범위 충족 | 측정·조절 |
| 3 | 낮은 지형 · CND-139 | 지형에서 기록 위치의 불일치 표시 | 채집 위치·기록 위치 일치 | 관찰·검사 |

- 특수 상황: **정보 부족 조사**. 최종 제출 전 필수 정보 1개 누락. 통과: 필수 근거 확보 전 판단하지 않음. 복구: 빠진 근거를 알려주고 추가 조사.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 시료 용기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 휴대 측정기 / noncommon / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 낮은 지형 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 검토: 원문 장소 분류 밖의 장면 제안. 직업의 해당 업무를 이 장소로 표현할 수 있는지 별도 검토 필요.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-206-experience"></a>
### 회계사 — 자료를 함께 검토하고 설명할 준비 마치기

- 직업: `career-net-206` · 시나리오 `career-net-206-experience` `v001`.
- 원본 위치: `/items/550/data` · 역량: 수리·논리력.
- 장소 제안: 전문 상담 사무실 · `PRM-005 v001` · [PAN-005 v001](../../../images/original/panoramas/PAN-005/v001/E-professional-consultation-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 회계사의 업무 표현과 전문 상담 사무실의 전문가가 의뢰인과 문서를 함께 보며 자문하는 공간를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 회계사는 금융, 회계, 세무학 등의 지식을 바탕으로 개인이나 기업, 공공시설, 정부 기관 등의 경영 상태, 재무 상태, 지급 능력 등의 다양한 재무 보고와 관련하여 상담해주거나 관련 서류를 작성합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 서류 파일 · CND-027 | 파일에서 사실과 미확인 항목을 구별 | 미확인 항목을 사실로 확정하지 않음 | 관찰·검사 |
| 2 | 테이블 · CND-010 | 테이블에서 의뢰인의 요구를 묻고 대안을 설명 | 필수 질문·확인 응답 충족 | 대화·응대 |
| 3 | 선반 · CND-028 | 책장에서 설명에 필요한 참고자료 선택 | 질문 주제에 맞는 참고자료 선택 | 분류·선별 |

- 특수 상황: **상충 요구 조정**. 완료 시간을 줄이라는 추가 요구. 통과: 명시된 필수 조건 보존과 절충 이유 확인. 복구: 충돌을 보여주고 대안 재선택.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 서류 파일 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 테이블 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 선반 / common / 실제 모델 연결 미정. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

<a id="career-net-258-experience"></a>
### 회계사무원 — 요청 자료를 확인하고 오류 없는 문서 묶음 전달

- 직업: `career-net-258` · 시나리오 `career-net-258-experience` `v001`.
- 원본 위치: `/items/551/data` · 역량: 수리·논리력.
- 장소 제안: 공용 업무 사무실 · `PRM-001 v001` · [PAN-001 v001](../../../images/original/panoramas/PAN-001/v001/A-basic-office-v2.png).
- 장소 선택 상태: `existing_context_candidate`. 회계사무원의 업무 표현과 공용 업무 사무실의 직원들이 각자 PC 업무를 하며 공용 기기를 공유하는 회사를 연결한 편집상 선택.
- 원본에서 선택한 업무 근거: 회계사무원은 회계학과 관련된 지식을 바탕으로 기업에서 이루어지는 수입과 지출 등 모든 거래 사항을 기록하고 정리하며 회계사의 업무를 지원합니다.
- 체험의 업무 자료: 가상 의뢰 자료·사실·미확인 항목과 설명.

| 순서 | 상호작용 물건·후보 | 행동 | 성공 조건 | 미니게임 |
|---|---|---|---|---|
| 1 | 모니터 · CND-005 | 화면의 요청과 자료를 비교해 잘못된 항목 수정 | 오류 필드와 수정값 일치 | 관찰·검사 |
| 2 | 복합기 · CND-008 | 최신 저장본을 지정 부수로 출력 | 파일 revision과 부수 일치 | 순서·절차 |
| 3 | 수납장 · CND-009 | 문서를 용도별 칸에 보관 | 문서 분류와 인계 항목 일치 | 분류·선별 |

- 특수 상황: **협업·인계**. 3단계 결과 제출 직전 인계 요청. 통과: 필수 항목 전달과 수신 확인. 복구: 누락 항목을 보완해 재전달.
- 오류: 잘못된 입력은 해당 단계에서 이유를 안내하고 재시도한다. 순서 위반·중복 제출은 진행 상태를 바꾸지 않는다. 요청 변경 시 이전 revision의 완료를 인정하지 않는다. 초기화로 세 물건의 논리 상태를 함께 되돌린다.
- 원본 역량 연결: 원문 역량 수리·논리력을 업무 자료 확인·판단·설명 과정과 연결하는 기획 제안. 개별 입력 점수로 역량·적성을 판정하지 않음.
- 에셋 준비: 모니터 / common / AST-005 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 복합기 / noncommon / AST-009 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 에셋 준비: 수납장 / common / AST-015 v001 재사용 후보. 콜라이더·입력·상태 표현 적합성 미검증.
- 검토: 원본 업무를 짧은 게임으로 각색한 초안. 직업별 전문가·사용성 검토 전.
- 검토: 가상 문제 데이터는 공통 엔진 검증용. 직업별 실제 사례·장비·오류 판단을 완전히 재현하지 않음.
- 현재 상태: 기획 검토 대기. 해당 시나리오의 실제 사용·미니게임·Unity·WebGL 실행은 미검증.

## 확인 범위와 한계

전체 직업 ID·이름·원본 인덱스·역량, 세 물건의 후보 ID와 고정 파노라마·프롬프트, 적용 유형, 참조 파일·문서 링크·해시를 대조했다. 기계용 데이터에서 모든 단계의 기본 엔진 설정 필드를 확인했다. 이 검사는 실제 게임 실행·3D 외형·재미·전문 업무 정확성 검증이 아니다.

문제 데이터는 요청 라벨·순서·가상 눈금 등 공통 엔진 연습용이며 직업별 전문 문제 세트 전체가 아니다. 이 초안을 그대로 최종 콘텐츠로 출시하지 않는다. 공간 밖 추가 후보·특수 형상·장소 부적합 가능성·종교 선택 대기를 검토 항목으로 남겼다. 신규 모델·이미지·Unity·WebGL 제작 및 Meshy 유료 호출은 수행하지 않았다.

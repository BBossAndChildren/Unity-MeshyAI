# 종교 3종 직업·호칭·직책과 출처 v001

공식 직업분류와 종교기관 자료로 보완한 목록입니다. 기존 552개 직업 원본과 career-net-384 성직자 ID는 보존했습니다. 세부 직업은 외부 KSCO 식별자로 연결하며 임의 CareerNet 번호를 만들지 않았습니다.

| 종교 | 직업 표시명 | 공식 KSCO8 코드 | 호칭·직책 구분 |
|---|---|---|---|
| 불교 | 승려 | 25413 | 스님(호칭), 주지(직책) |
| 개신교 | 목사 | 25411 | 별도 확인 자료 없음 |
| 천주교 | 신부 | 25412 | 신부님(호칭), 본당 주임(직책), 보좌 사제(직책) |
| 개신교 | 전도사 | 25492 | 별도 확인 자료 없음 |
| 천주교 | 수녀 | 25491 | 별도 확인 자료 없음 |
| 천주교 | 수사 | 25491 | 별도 확인 자료 없음 |

수녀와 수사는 같은 25491 분류를 공유하므로 표시명 6개와 공식 분류 5개를 구별합니다. 전도사·수녀·수사를 모두 성직자로 자동 합치지 않습니다. 스님은 승려의 호칭이며 주지는 임명 직책입니다. 종교 공간 3곳은 기존 미선택 대안을 유지하며 이 등록이 새 체험 구현이나 주제 승인을 뜻하지 않습니다.

- [기계용 출처·필드 연결 목록](../../../../../../../machine/catalog/religion-occupations-v001.json)
- [보존 원본 Job_things_list.txt](../../../v001/Job_things_list.txt)
- 보존 원본 SHA-256: `18f2823d16933080ace4d08ca55f3f965efdaba834c4d536fe16971df516a09d`
- 원본 성직자 위치: `/items/231`, 핵심능력은 원본의 자기성찰능력 표기를 보존합니다. 세부 직업별 핵심능력은 별도 확인되지 않아 null과 사유를 남겼습니다.

## 직업별 하는 일과 준비방법

### 승려

- 하는 일: 수행과 교화에 전념하며 불교 가르침을 전하고 후학을 양성하거나 사회봉사에 참여한다. 종파·소임에 따라 활동은 달라진다.
- 준비방법: 조계종 사례에서는 행자 단계와 수계, 기본교육을 거쳐 전문·특수·연수교육으로 이어지는 교육 체계를 안내한다. 실제 입문·교육·수계 조건은 해당 종단에 확인한다.
- 핵심능력: 미확인(null). 원본 상위 직업의 역량을 세부 직업에 복제하지 않았습니다.
- 업무 출처: [대한불교조계종](sources/jogye-monastic-duties.txt)
- 준비 출처: [대한불교조계종 교육원](sources/jogye-education-overview.txt)

### 목사

- 하는 일: 예배와 설교, 신앙교육, 심방·상담 및 교회 공동체의 목회 실무를 수행한다. 담당 사역과 교단 제도에 따라 책임 범위가 달라진다.
- 준비방법: 한국기독교장로회 사례는 교단이 인정하는 신학교육과 목회수련·고시·청빙·임직을 연결한다. 교단별 절차이므로 개신교 전체의 단일 자격으로 사용하지 않는다.
- 핵심능력: 미확인(null). 원본 상위 직업의 역량을 세부 직업에 복제하지 않았습니다.
- 업무 출처: [한국기독교장로회총회](sources/prok-minister-training.txt)
- 준비 출처: [한국기독교장로회총회](sources/prok-minister-training.txt)

### 신부

- 하는 일: 사제는 맡은 사목과 부여된 권한에 따라 신앙을 가르치고 전례·성사를 집전하며 신자를 돌본다. 본당 외 교회 기관이나 수도회 사도직 등 다른 소임도 있을 수 있다.
- 준비방법: 사제 지망자는 교회가 정한 신학교육과 영성·철학·신학·사목 양성 및 적합성 심사를 거친다. 구체 과정과 성품 수여 요건은 교구·수도회별로 확인한다.
- 핵심능력: 미확인(null). 원본 상위 직업의 역량을 세부 직업에 복제하지 않았습니다.
- 업무 출처: [Holy See / Vatican](sources/vatican-parish-ministry.txt)
- 준비 출처: [Holy See / Vatican](sources/vatican-priest-formation.txt)

### 전도사

- 하는 일: 교단과 교회가 정한 담당 사역을 수행한다. 한국기독교장로회 수련생 사례에서는 지도목사 아래 예배·설교·심방·상담·교육·행정 등 목회실무를 실습한다.
- 준비방법: 소속 교단이 정한 교육·청빙·인정 절차를 확인한다. 한국기독교장로회의 목사수련생 제도는 전임전도사 지위를 부여하지만 모든 전도사가 목사수련생이라는 뜻은 아니다.
- 핵심능력: 미확인(null). 원본 상위 직업의 역량을 세부 직업에 복제하지 않았습니다.
- 업무 출처: [한국기독교장로회총회](sources/prok-minister-training.txt)
- 준비 출처: [한국기독교장로회총회](sources/prok-minister-training.txt)

### 수녀

- 하는 일: 수도회 영성에 따라 기도와 공동생활을 하며 회의 사명에 맞는 봉사·사도직에 참여한다. 관상 중심 회와 외부 활동 회의 생활·업무를 구분한다.
- 준비방법: 지원·식별과 수련을 통해 회의 생활·영성·규율을 배우며, 서원 이후에도 영적·교리적·실무적 양성을 계속한다. 개별 수도회 모집 조건은 별도 확인한다.
- 핵심능력: 미확인(null). 원본 상위 직업의 역량을 세부 직업에 복제하지 않았습니다.
- 업무 출처: [Holy See / Vatican](sources/vatican-religious-formation-work.txt)
- 준비 출처: [Holy See / Vatican](sources/vatican-religious-formation-work.txt)

### 수사

- 하는 일: 수도회 영성에 따라 기도와 공동생활을 하며 회의 사명에 맞는 봉사·사도직에 참여한다. 수도자라는 이유로 미사·고해성사 집전 권한이 있다고 추정하지 않는다.
- 준비방법: 지원·식별과 수련을 통해 회의 생활·영성·규율을 배우며 서원 이후 양성을 계속한다. 성품을 받는 수도사제의 양성과 사제 직무는 별도 구분한다.
- 핵심능력: 미확인(null). 원본 상위 직업의 역량을 세부 직업에 복제하지 않았습니다.
- 업무 출처: [Holy See / Vatican](sources/vatican-religious-formation-work.txt), [Holy See / Vatican](sources/vatican-cleric-religious.txt)
- 준비 출처: [Holy See / Vatican](sources/vatican-religious-formation-work.txt), [Holy See / Vatican](sources/vatican-cleric-religious.txt)

## 출처와 수집 범위

아래 수집본은 전체 원문 복제본이 아니라 출처·위치·짧은 발췌·요약·수집 한계를 보존한 자료입니다. 각 수집본 해시와 바이트 크기, 필드별 출처 ID는 기계용 목록에 연결했습니다. 기관별 교육 과정은 해당 종단·교단·수도회 사례이며 보편적인 국가 자격 조건으로 해석하지 않습니다.

- [국립국어원 온라인가나다: 님 자가 붙은 단어들과 관련하여](https://m.korean.go.kr/front/onlineQna/onlineQnaView.do?mn_id=216&pageIndex=1&qna_seq=334077) — 국립국어원. 조회: 2026-10-31T02:50:13Z. 원문 위치: 답변 본문, 스님 뜻풀이. [수집본·한계](sources/nikl-monastic-address.txt). 취득 범위: `opened_official_page`.
- [대한불교조계종 승려 교육 체계](https://www.buddhism.or.kr/m/edu/sub2/sub2-1.php) — 대한불교조계종 교육원. 조회: 2026-10-31T02:50:13Z. 원문 위치: 기본교육·전문교육·특수교육 문단. [수집본·한계](sources/jogye-education-overview.txt). 취득 범위: `official_page_search_index_excerpt; direct_fetch_502`.
- [대한불교조계종 승려법 2018년 개정 전문](https://www.buddhism.or.kr/board/file_down.php?baidx=243927) — 대한불교조계종. 조회: 2026-10-31T02:50:13Z. 원문 위치: 제29조 수행·교화·불법 홍포·도제 양성·사회봉사 / 제30조 교육. [수집본·한계](sources/jogye-monastic-duties.txt). 취득 범위: `official_document_search_index_excerpt; direct_fetch_502`.
- [대한불교조계종 봉은사 주지 임명 소식](https://www.buddhism.or.kr/board/view.php?board_contents_idx=208410&scale=10&skey=&sval=&tn=news_01_03) — 대한불교조계종. 조회: 2026-10-31T02:50:13Z. 원문 위치: 주지(사찰관리인) 임명 본문. [수집본·한계](sources/jogye-abbot-position.txt). 취득 범위: `official_page_search_index_excerpt`.
- [한국기독교장로회총회 목사수련생 수련과정](https://prok.org/Page/Index/414) — 한국기독교장로회총회. 조회: 2026-10-31T02:50:13Z. 원문 위치: 시행세칙 제3조(교과목), 제4조 수련생 지위, 목사 임직 자격·헌법정치 제24조 소개. [수집본·한계](sources/prok-minister-training.txt). 취득 범위: `official_page_search_index_text; direct_fetch_robots_restricted`.
- [Code of Canon Law, Canons 204–207](https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib2-cann204-207_en.html) — Holy See / Vatican. 조회: 2026-10-31T02:50:13Z. 원문 위치: Canon 207 §§1–2. [수집본·한계](sources/vatican-cleric-religious.txt). 취득 범위: `opened_official_page`.
- [Code of Canon Law, Canons 573–606](https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib2-cann573-606_en.html) — Holy See / Vatican. 조회: 2026-10-31T02:50:13Z. 원문 위치: Canons 573, 577–578, 588. [수집본·한계](sources/vatican-consecrated-state.txt). 취득 범위: `opened_official_page`.
- [Code of Canon Law, Canons 607–709](https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib2-cann607-709_en.html) — Holy See / Vatican. 조회: 2026-10-31T02:50:13Z. 원문 위치: Canons 607, 646, 652, 654, 659–661, 663, 673–676. [수집본·한계](sources/vatican-religious-formation-work.txt). 취득 범위: `opened_official_page`.
- [Code of Canon Law, Canons 208–329](https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib2-cann208-329_en.html) — Holy See / Vatican. 조회: 2026-10-31T02:50:13Z. 원문 위치: Canons 232–235, 241–245, 250, 255. [수집본·한계](sources/vatican-priest-formation.txt). 취득 범위: `opened_official_page`.
- [Code of Canon Law, Canons 460–572](https://www.vatican.va/archive/cod-iuris-canonici/eng/documents/cic_lib2-cann460-572_en.html) — Holy See / Vatican. 조회: 2026-10-31T02:50:13Z. 원문 위치: Canons 519, 528–530, 545–547. [수집본·한계](sources/vatican-parish-ministry.txt). 취득 범위: `opened_official_page`.
- [Eighth Korean Standard Classification of Occupations, revision announcement](https://www.kostat.go.kr/boardDownload.es?bid=246&list_no=431583&seq=1) — Statistics Korea. 조회: 2026-10-31T03:02:18.725433+00:00. 원문 위치: PDF zero-based page16 (17th page), classification table254, lines983-993. [수집본·한계](sources/ksco8-religion-classification.txt). 취득 범위: `opened_official_pdf`.

KSCO8 공식 분류는 2024-07-01 고시·2025-01-01 시행 자료의 PDF 17번째 페이지를 실제 확인했습니다. 조계종 2018년 자료는 당시 판본이며 현행 규정 전체로 표시하지 않았습니다. 일부 기관 직접 수집 실패(502/412/robots 제한)는 수집본에 남겼습니다. 구형 CareerNet 화면의 구분류·과거 통계·다른 역량 표기는 현재 보존 원본으로 이식하지 않았습니다.


## 등록 후 검토

[독립 읽기 검토55건](../../../../../../../machine/evidence/religion-roles-v001/religion-readonly-audit.json)에서 원본552개·6역할·5공식분류·11수집본 해시·필드 연결·문서 링크를 확인했습니다. 이 검토는 저장된 근거의 무결성과 연결 범위이며 모든 기관 페이지의 현재 전체 원문·현재 자격요건을 재검증했다는 뜻은 아닙니다.

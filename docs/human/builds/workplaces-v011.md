# workplaces-v011 — 69공간 특색·재사용 디테일

실행: 저장소에서 `python -m http.server 8173 --bind 127.0.0.1 --directory unity/webgl/builds` 후 `http://127.0.0.1:8173/workplaces-v011/` 접속. ZIP은 압축해제 폴더에서 HTTP서버 실행. file:// 직접 열기는 지원하지 않는다.

## 구현·실행 결과 v011

변경69공간, 교회·성당2공간 보존. Unity6000.3.26f1 실제 빌드 Succeeded, 오류0·경고0. HTTP71공간 로딩·실측·공용 팔레트, 실제 크기/축소 화면 검수. 개별 제어 검사는 http-spatial.json의 해당 case만 확인했다.

| 정확한 공간 | 고정 prompt / panorama | 최종 모델 | 수량 | 삼각형 | 특색·추가/보류 판단 |
|---|---|---|---:|---:|---|
| PAN-001 공용 업무 사무실 | PRM-001 v001 / PAN-001 v001 | AST-020 v008 | 33 | 4716 | 정확한 문서 업무와 정리된 책상; clock:added; papers:added; books:not_added(No collision-free supported position) |
| PAN-002 협업·기획 사무실 | PRM-002 v001 / PAN-002 v001 | AST-2002 v006 | 22 | 3794 | 협업 아이디어와 가벼운 목재 분위기; acoustic:added; art:added; cubby:added; vase:added |
| PAN-003 행정·문서 처리 사무실 | PRM-003 v001 / PAN-003 v001 | AST-2003 v007 | 27 | 4340 | 분류·보관이 강조된 행정 업무; clock:added; books:not_added(No collision-free supported position); papers:added; cubby:added |
| PAN-004 민원·방문객 접수실 | PRM-004 v001 / PAN-004 v001 | AST-2004 v006 | 13 | 2760 | 방문자 안내와 대기 동선; wayfinding:added; clock:added; brochures:added |
| PAN-005 전문 상담 사무실 | PRM-005 v001 / PAN-005 v001 | AST-2005 v004 | 19 | 2966 | 차분한 전문 상담과 서재; art:added; books:added; lamp:added; vase:added |
| PAN-006 실험실 | PRM-006 v001 / PAN-006 v001 | AST-2006 v005 | 14 | 2552 | 밝은 실험대와 실험 비품; labwall:added; labvials:not_added(No collision-free supported position); pegboard:added |
| PAN-007 분석실 | PRM-007 v001 / PAN-007 v001 | AST-2007 v007 | 14 | 2668 | 정밀 분석 장비와 청결한 수납; labwall:added; labvials:added; clock:added |
| PAN-008 진료실 | PRM-008 v001 / PAN-008 v001 | AST-2008 v005 | 16 | 3440 | 진료 프라이버시와 정돈된 비품; curtain:added; clock:added; bottles:added |
| PAN-009 처치실 | PRM-009 v001 / PAN-009 v001 | AST-2009 v005 | 13 | 2608 | 처치 구획과 청결한 도구 준비; curtain:added; labwall:added; labvials:not_added(No collision-free supported position) |
| PAN-010 병실 | PRM-010 v001 / PAN-010 v001 | AST-2010 v006 | 13 | 2288 | 편안한 회복과 개인 침상 구획; curtain:added; clock:added; blanket:added |
| PAN-011 의료 접수실 | PRM-011 v001 / PAN-011 v001 | AST-2011 v005 | 16 | 2912 | 의료 안내·대기·접수; clock:added; brochures:not_added(No collision-free supported position); cubby:added |
| PAN-012 교실 | PRM-012 v001 / PAN-012 v001 | AST-2012 v005 | 18 | 2924 | 학습 자료와 교실의 생활감; learning:added; books:added; coatrack:added |
| PAN-013 교육 실습실 | PRM-013 v001 / PAN-013 v001 | AST-2013 v005 | 16 | 2632 | 조립 학습과 색상별 교구 정리; pegboard:added; cubby:added; learning:added |
| PAN-014 강의실 | PRM-014 v001 / PAN-014 v001 | AST-2014 v005 | 16 | 2500 | 발표 집중과 강의실의 흡음 구성; acoustic:added; books:added; clock:added |
| PAN-015 복지·심리 상담실 | PRM-015 v001 / PAN-015 v001 | AST-2015 v005 | 14 | 2470 | 따뜻한 대화와 직물·목재; art:added; lamp:added; vase:added; blanket:not_added(No collision-free supported position) |
| PAN-016 복지 활동실 | PRM-016 v001 / PAN-016 v001 | AST-2016 v007 | 14 | 2520 | 활동 교구와 밝은 생활 색감; learning:added; cubby:added; coatrack:added |
| PAN-017 요양실 | PRM-017 v001 / PAN-017 v001 | AST-2017 v004 | 13 | 2060 | 안정감 있는 생활·돌봄; clock:added; blanket:added; lamp:added |
| PAN-018 생산 구역 | PRM-018 v001 / PAN-018 v001 | AST-2018 v004 | 14 | 2172 | 생산 구역과 안전한 접근 구획; hazardposts:added; pipe:added; crates:added |
| PAN-019 조립 구역 | PRM-019 v001 / PAN-019 v001 | AST-2019 v004 | 14 | 2428 | 작은 부품을 정리한 조립 작업; pegboard:added; cubby:added; parts:not_added(No collision-free supported position) |
| PAN-020 정비 구역 | PRM-020 v001 / PAN-020 v001 | AST-2020 v003 | 14 | 2268 | 정비 공구와 작업 흔적; pegboard:added; tires:added; parts:added |
| PAN-021 소매점 | PRM-021 v001 / PAN-021 v001 | AST-2021 v004 | 15 | 1902 | 상품 진열과 계절별 판매대; display:added; jars:not_added(No collision-free supported position); basket:added |
| PAN-022 서비스 창구 | PRM-022 v001 / PAN-022 v001 | AST-2022 v007 | 17 | 2448 | 서비스 응대와 서류 안내; clock:added; brochures:added; papers:added |
| PAN-023 미용실 | PRM-023 v001 / PAN-023 v001 | AST-2023 v005 | 12 | 2120 | 부드러운 미용 공간과 제품 정리; bottles:not_added(No collision-free supported position); towels:not_added(No collision-free supported position); art:added; bottles:added(Dedicated self-supported display after tabletop fit rejection) |
| PAN-024 주방 | PRM-024 v001 / PAN-024 v001 | AST-2024 v006 | 13 | 2120 | 조리·세척·보관의 명확한 구역; kitchenwall:added; jars:added; food:added |
| PAN-025 제과실 | PRM-025 v001 / PAN-025 v001 | AST-2025 v004 | 14 | 2472 | 제빵 결과와 밀가루색 작업면; bread:added; jars:added; cubby:added |
| PAN-026 식당 홀 | PRM-026 v001 / PAN-026 v001 | AST-2026 v004 | 18 | 3282 | 식사 공간의 온기와 식기; pendant:added; pitcher:added; jars:added; plant:added |
| PAN-027 디자인 작업실 | PRM-027 v001 / PAN-027 v001 | AST-2027 v006 | 15 | 2220 | 색상·재료 시안을 다루는 디자인; swatches:added; papers:added; cubby:added |
| PAN-028 미술 작업실 | PRM-028 v001 / PAN-028 v001 | AST-2028 v006 | 15 | 1972 | 창작 중인 화구와 작품; art:added; paint:added; cubby:added |
| PAN-029 공예 작업실 | PRM-029 v001 / PAN-029 v001 | AST-2029 v003 | 13 | 2784 | 손작업 재료와 공예 소품; pegboard:added; pitcher:added; paint:not_added(No collision-free supported position); basket:added |
| PAN-030 촬영 스튜디오 | PRM-030 v001 / PAN-030 v001 | AST-2030 v004 | 14 | 1772 | 사진 촬영의 배경과 장비 구획; backdrop:added; cases:added; swatches:added |
| PAN-031 방송 스튜디오 | PRM-031 v001 / PAN-031 v001 | AST-2031 v006 | 15 | 2260 | 방송의 음향과 진행 준비; acoustic:added; signal:added; papers:added |
| PAN-032 영상 편집실 | PRM-032 v001 / PAN-032 v001 | AST-2032 v005 | 16 | 3144 | 집중형 편집과 매체 정리; acoustic:added; media:added; clock:added |
| PAN-033 공연 무대 | PRM-033 v001 / PAN-033 v001 | AST-2033 v004 | 19 | 3240 | 공연의 조명·커튼·목재 무대; stagecurtain:added; signal:added; cases:added |
| PAN-034 전시실 | PRM-034 v001 / PAN-034 v001 | AST-2034 v005 | 13 | 1548 | 여백과 독립 작품 중심의 전시; galleryart:added; sculpture:not_added(No collision-free supported position); wayfinding:added |
| PAN-035 문화 활동실 | PRM-035 v001 / PAN-035 v001 | AST-2035 v005 | 14 | 2324 | 공동 창작과 문화 교구; art:added; cubby:added; paint:added |
| PAN-036 건축 작업 구역 | PRM-036 v001 / PAN-036 v001 | AST-2036 v004 | 13 | 1920 | 시공 중인 구조와 자재·안전; cones:added; crates:added; hazardposts:added |
| PAN-037 설비 작업 구역 | PRM-037 v001 / PAN-037 v001 | AST-2037 v005 | 13 | 2368 | 노출 배관과 설비 점검; pipe:added; pegboard:added; parts:added |
| PAN-038 환경 조사 지점 | PRM-038 v001 / PAN-038 v001 | AST-2038 v003 | 15 | 2884 | 조사 대상 지형과 자연 식생; rocks:added; bush:added; grass:added; flags:added |
| PAN-039 관측 지점 | PRM-039 v001 / PAN-039 v001 | AST-2039 v006 | 14 | 2785 | 바람과 지형을 읽는 관측; rocks:added; bush:added; flags:added |
| PAN-040 재배지 | PRM-040 v001 / PAN-040 v001 | AST-2040 v004 | 16 | 4172 | 재배 베드·수확·관수; tree:added; crates:added; grass:added; basket:not_added(No collision-free supported position) |
| PAN-041 온실 | PRM-041 v001 / PAN-041 v001 | AST-2041 v004 | 14 | 3376 | 시설 재배와 규칙적인 묘목; trellis:added; plant:added; cubby:added |
| PAN-042 축사 | PRM-042 v001 / PAN-042 v001 | AST-2042 v003 | 14 | 1924 | 사료·깔짚·축사 구획; hay:added; woodfence:added; crates:added |
| PAN-043 동물 관리실 | PRM-043 v001 / PAN-043 v001 | AST-2043 v005 | 13 | 2104 | 동물 돌봄과 세척·비품; towels:added; cubby:added; bottles:not_added(No collision-free supported position) |
| PAN-044 선박 갑판 | PRM-044 v001 / PAN-044 v001 | AST-2044 v005 | 15 | 1828 | 선박 갑판의 목재와 계류 설비; nautical:not_added(No collision-free supported position); crates:added; hazardposts:added |
| PAN-045 조타실 | PRM-045 v001 / PAN-045 v001 | AST-2045 v006 | 13 | 1764 | 조타 시야와 항해 계기; windshield:added; status:added; clock:added |
| PAN-046 부두 | PRM-046 v001 / PAN-046 v001 | AST-2046 v005 | 14 | 2192 | 부두의 계류·하역·수변; nautical:added; crates:added; rocks:not_added(No collision-free supported position) |
| PAN-047 체육관 | PRM-047 v001 / PAN-047 v001 | AST-2047 v004 | 10 | 1920 | 운동 바닥과 정리된 체육 비품; gymrack:added; towels:not_added(No collision-free supported position); clock:added |
| PAN-048 운동 지도실 | PRM-048 v001 / PAN-048 v001 | AST-2048 v004 | 11 | 1436 | 개인 운동 구역과 가벼운 도구; gymrack:added; towels:not_added(No collision-free supported position); art:added |
| PAN-049 경기 구역 | PRM-049 v001 / PAN-049 v001 | AST-2049 v004 | 12 | 2054 | 녹색 경기 구역과 관람 경계; benches:added; bush:added; flags:added |
| PAN-050 수사실 | PRM-050 v001 / PAN-050 v001 | AST-2050 v007 | 18 | 2728 | 사건 관계 자료와 정돈된 수사; evidence:added; papers:added; books:added |
| PAN-051 증거 분석실 | PRM-051 v001 / PAN-051 v001 | AST-2051 v007 | 16 | 2288 | 봉인 시료와 청결한 분석; labwall:added; labvials:not_added(No collision-free supported position); cubby:added |
| PAN-052 법정 | PRM-052 v001 / PAN-052 v001 | AST-2052 v004 | 16 | 2184 | 법정의 목재·문서·정면성; legal:added; books:added; woodscreen:added |
| PAN-053 물류 창고 | PRM-053 v001 / PAN-053 v001 | AST-2053 v003 | 15 | 1600 | 적재 단위와 창고 동선; crates:added; cones:added; hazardposts:added |
| PAN-054 운송 조종 공간 | PRM-054 v001 / PAN-054 v001 | AST-2054 v006 | 14 | 1836 | 조종석의 전방 시야와 계기; windshield:added; status:added; cases:added |
| PAN-055 운송 거점 | PRM-055 v001 / PAN-055 v001 | AST-2055 v005 | 14 | 2356 | 이동·대기·안내 동선; wayfinding:added; clock:added; brochures:added |
| PAN-056 금융 창구 | PRM-056 v001 / PAN-056 v001 | AST-2056 v007 | 20 | 3620 | 차분한 금융 응대와 보안 구획; glasspanel:added; clock:added; papers:added |
| PAN-057 금융 상담실 | PRM-057 v001 / PAN-057 v001 | AST-2057 v004 | 13 | 2222 | 신뢰감 있는 금융 상담; art:added; books:not_added(No collision-free supported position); vase:added |
| PAN-058 가정 수리 공간 | PRM-058 v001 / PAN-058 v001 | AST-2058 v005 | 12 | 1800 | 생활 공간에서의 수리 준비; notice:added; parts:not_added(No collision-free supported position); blanket:not_added(No collision-free supported position); parts:added(Dedicated self-supported display after tabletop fit rejection) |
| PAN-059 방문 학습 공간 | PRM-059 v001 / PAN-059 v001 | AST-2059 v005 | 12 | 1760 | 가정 학습과 교재·필기구; learning:added; books:not_added(No collision-free supported position); papers:added |
| PAN-060 서버실 | PRM-060 v001 / PAN-060 v001 | AST-2060 v005 | 15 | 2752 | 차가운 전산 구역과 케이블 정리; server:added; status:added; hazardposts:added |
| PAN-061 관제실 | PRM-061 v001 / PAN-061 v001 | AST-2061 v006 | 15 | 2892 | 상황 인지와 다중 화면·시간; status:added; clocks:added; acoustic:added |
| PAN-062 거실 | PRM-062 v001 / PAN-062 v001 | AST-2062 v004 | 13 | 2406 | 휴식하는 거실의 직물과 소품; art:added; vase:added; blanket:added; lamp:added |
| PAN-063 주택 관리 공간 | PRM-063 v001 / PAN-063 v001 | AST-2063 v006 | 15 | 2080 | 입주자 안내와 관리용 비품; notice:added; cubby:added; papers:added |
| PAN-070 불교 법당 — 스님 | PRM-070 v001 / PAN-070 v001 | AST-2070 v004 | 17 | 1532 | 불단·목재 격자·연꽃과 등; temple:added; lantern:added; lotus:not_added(No collision-free supported position); bowl:not_added(No collision-free supported position) |
| PAN-065 군 행정실 | PRM-065 v001 / PAN-065 v001 | AST-2065 v006 | 17 | 2744 | 절제된 군 행정과 자료 정리; evidence:added; cases:added; papers:added |
| PAN-066 생활관 | PRM-066 v001 / PAN-066 v001 | AST-2066 v005 | 16 | 2372 | 질서 있는 공동생활과 개인 수납; coatrack:added; blanket:added; cubby:added |
| PAN-067 장비 관리실 | PRM-067 v001 / PAN-067 v001 | AST-2067 v004 | 14 | 2320 | 정비 장비의 종류별 보관; pegboard:added; parts:added; crates:added |
| PAN-068 출장 업무 공간 | PRM-068 v001 / PAN-068 v001 | AST-2068 v004 | 13 | 2198 | 이동 중 사용하는 간결한 작업 자리; papers:added; cases:added; vase:added |
| PAN-069 안내 집결 지점 | PRM-069 v001 / PAN-069 v001 | AST-2069 v004 | 15 | 2588 | 야외 집결과 명확한 안내 동선; tree:added; rocks:not_added(No collision-free supported position); grass:added; wayfinding:added |

편집 프로젝트 `unity/projects/OfficeAssistant-v001`; WebGL `unity/webgl/builds/workplaces-v011`; 전달 ZIP `unity/webgl/packages/workplaces-v011.zip`. 기존 모델/장면/빌드는 덮어쓰지 않았다. 기존 미니게임 대상/로직 보존은 소스·실제 바인딩을 확인한 범위이며 전체업무/React 프로토콜 회귀 완료를 뜻하지 않는다.

바닥 색상27종·좌석 색상6종은 기존 고정 형상을 재사용한 materialized UV 변형이다. 공간 무늬는 기하 면으로 제작했으며 새 이미지 텍스처를 모델에 넣지 않았다. palette v0012508×2508 PNG 한 장·공용 재질, 소품1,000 이하·장면5,000 이하. 반복 배치 포함·부모 조립 중복 제외.

비용: 이번 자연물 한 묶음20크레딧, 이전 꽃/장식40은 과거 비용, 재사용 추가0. 입력·캐시·출력 토큰/금액/시간 배분은 미측정. 개별 자연물 비용 분배null.

미검증: Editor Play Mode, 다른 브라우저/장치, 완전한 개별 소품 상세/숨은 면(해당 AST inspection 참조), 전체 직업 업무·React 통신 회귀, ZIP 압축해제 복사본 HTTP실행. 근거 `docs/machine/evidence/workplaces-v011/build-result.json`, `http-spatial.json`, `visual-review.json`, 공간별 `*-unity-scene.json`.


카메라·조명·좌석 방향 오류 9개를 고쳤으며, 지지대 없는 사다리는 AST-1136 v002 A형으로 수정했다. 경계 밖으로 나가던 바닥 무늬는 새 고정 버전으로 교체했다. 실제 배치 회전·최종 GLB 검사는 `docs/machine/evidence/spatial-diversity-v001/source-audit-v011.json`, 지지·경계 검사는 `docs/machine/evidence/spatial-diversity-v001/floor-pattern-repair.json`을 참조한다.

사무실 추가 실제 조작 3건: 확대 애니메이션 완료 후 질문 UI 활성화, 질문에 대한 자료·날짜 응답, Esc 복귀 시 전체 사무실 복원. `docs/machine/evidence/workplaces-v011/office-stable-smoke.json`. 기존 `office-monitor.png`는 focusing 도중 캡처이므로 완료된 확대 화면은 `office-monitor-settled.png`를 사용한다.


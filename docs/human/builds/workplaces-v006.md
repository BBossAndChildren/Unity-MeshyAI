# workplaces-v006 — 71개 3D 공간 Unity WebGL

> 실제 v006에서71개 공간·Native·HTTP·표시 검수와 사무보조원 v002의 구현 범위가 통과했다. 이전 빌드의pass를 승계하지 않았다. 최종 ZIP의 무결성과 새로 추출한 HTTP 실행2건도 실제 통과했다.

기존71개 파노라마를 기준으로 만든 실제3D 공간을 한 Unity 프로젝트에서 선택·회전·확대해 탐색하는 빌드다. 스카이박스/평면 파노라마 대체가 아니다. 사무보조원은 기존세 물건을 선택해 확대하고 문서 입력·출력·묶음 분류·인계를 수행하는 직접 작업형으로 확장했다. 다른 551개 직업 초안·미선택 대안은 자동 확정하지 않았다.

## 실제 결과·버전과 범위

| 항목 | 실제 기록 |
|---|---|
| 현재 공간·배치 | 최종71개 장면 /805개 구성 인스턴스 |
| 현재 모델 참조 |248개 구성 소품 버전 +71개 조립 버전 =319개 |
| 보존 등록 버전 |489버전 /319개 고유 에셋 ID |
| 보존 프로젝트 전체 source 배치 |835개(최종805+legacy OfficeAssistant.unity30); 프리팹 정의는 집계 제외 |
| 시나리오 | 사무보조원 career-net-253-office-documents v002 한 건; 기존552개 전체 구현과 구별 |
| 공통 통신 | career-experience v001; 수신 예제 dist-v006 |
| 후보 목록 | v003기준262개/공통55개/기존모델참조17개 보존; v004지원추가 포함 공통68개/전용180개/inventory-only14개 |

[전체 모델 색인](../assets/workplace-models-v001.md), [전체 후보·지원 추가 v004](../jobs/workplace-common-assets-v004.md), [직접 작업 설계](../jobs/office-assistant-direct-work-v002.md), [실제 통신·수신 예제](../integrations/workplace-runtime-protocol-v001.md), [공간별 진행 원장](../jobs/workplace-production-v001.md).

## 빌드·소스·팔레트

| 항목 | 실제 기록 |
|---|---|
| Unity | 6000.3.26f1 |
| 빌드 | Succeeded / 2026-10-31T07:08:08.6356228+09:00 |
| Unity 보고 크기 | 57566557바이트 |
| 오류·경고 | 0 / 0 |
| Unity 빌드 시간 | 66.9143637초(모델링·작성·검수 전체 시간 아님) |
| 소스 HEAD | `308507ce0429cc85106035ee3fac367db6756c1d` + 기존/이번 미커밋 변경 보존 |
| 편집 프로젝트 | `unity/projects/OfficeAssistant-v001` |
| WebGL 출력 | `unity/webgl/builds/workplaces-v006` |
| 모델 채색 | palette v0012508×2508PNG한 장·공용 모델 재질한 개, 원본 색 유지 |
| 의존성 | Unity WebGL 및 수신 예제의 번들 React/ReactDOM/scheduler; 새 유료 서비스/런타임GLB로더 없음 |

[실제 빌드 근거](../../machine/evidence/workplaces-v006/build-result.json), [15개 소스·AGENTS 동일성 검수](../../machine/evidence/workplaces-v006/source-snapshot-after-build.json). 원본 color1/color2와 최종PNG는 보존했고512개 색상 칸을 원본JPEG디코드값과 대조했다([근거](../../machine/evidence/workplaces-model-review-v001/palette-source-cells.json)). 모델 재질/팔레트는 UI폰트·화면 자원과 구별한다.

## 모델과 실제 실행 검수

최종GLB를 실제Blender로 다시 열고 삼각형·UV·재질을 조사했다. 반복 배치 포함 공간별908~4308삼각형으로5000목표 이내다. 모든 개별 소품은1000이하 기록이다. 실제 변환 버텍스 지지면/접지476건0실패를 검사했다([지지면 보고](../../machine/evidence/workplaces-model-review-v001/visual-review-v002.json), [상세 결과](../../machine/evidence/workplaces-model-review-v001/support-summary-v003.json)). 이 근거를 Unity/HTTP실행의 대체로 사용하지 않는다.

실제 v006 Unity Editor Play Mode71/71통과([보고](../../machine/evidence/workplaces-v006/unity-editor-play-rooms.json), [로그](../../machine/evidence/workplaces-v006/unity-editor-play.log)). 환경은batchmode -nographics이며 시각/HTTP/직접 작업/통신 검수는 별도다. 실제 v006 HTTP 공간 탐색71/71과 공통2건이 통과했고 콘솔 오류0건이다([실제 보고](../../machine/evidence/workplaces-v006/http-webgl-rooms.json)). [최종 시각 검수](../../machine/evidence/workplaces-v006/visual-review/screenshot-review.json)는71개 실제 크기/축소쌍과71개 native-pixel색상쌍을 확인했다. 대상에서 보이는 색 번짐·배치·지지면의 차단 문제0건이며 얇은 어두운 선의 대비 관찰1건을 보존했다. [현재319모델의 개별3방향 검수](../assets/workplace-current-model-coverage-v001.md)와 함께 조회한다. v005는 공간 탐색71/71통과와 사무보조원 실제 900×600입력 문제를 함께 보존한 중간본이며 수정한v006은 새로 실제 검수한다.

| 공간 | 고정 prompt | 고정 조립 | 구성 수량 | 삼각형 | GLB 바이트 | Unity Play | 최종 HTTP |
|---|---|---|---:|---:|---:|---|---|
| PAN-001 공용 업무 사무실 | PRM-001 v001 | [AST-020 v006](../assets/AST-020-v006.md) | 30 | 4308 | 3608352 | pass(nographics) | pass(공간 탐색) |
| PAN-002 협업·기획 사무실 | PRM-002 v001 | [AST-2002 v003](../assets/AST-2002-v003.md) | 17 | 2552 | 3503348 | pass(nographics) | pass(공간 탐색) |
| PAN-003 행정·문서 처리 사무실 | PRM-003 v001 | [AST-2003 v004](../assets/AST-2003-v004.md) | 23 | 3764 | 3597220 | pass(nographics) | pass(공간 탐색) |
| PAN-004 민원·방문객 접수실 | PRM-004 v001 | [AST-2004 v003](../assets/AST-2004-v003.md) | 9 | 2256 | 3474112 | pass(nographics) | pass(공간 탐색) |
| PAN-005 전문 상담 사무실 | PRM-005 v001 | [AST-2005 v002](../assets/AST-2005-v002.md) | 14 | 1832 | 3453236 | pass(nographics) | pass(공간 탐색) |
| PAN-006 실험실 | PRM-006 v001 | [AST-2006 v002](../assets/AST-2006-v002.md) | 11 | 1552 | 3429852 | pass(nographics) | pass(공간 탐색) |
| PAN-007 분석실 | PRM-007 v001 | [AST-2007 v004](../assets/AST-2007-v004.md) | 10 | 1700 | 3428396 | pass(nographics) | pass(공간 탐색) |
| PAN-008 진료실 | PRM-008 v001 | [AST-2008 v003](../assets/AST-2008-v003.md) | 12 | 2732 | 3515952 | pass(nographics) | pass(공간 탐색) |
| PAN-009 처치실 | PRM-009 v001 | [AST-2009 v002](../assets/AST-2009-v002.md) | 10 | 1804 | 3448788 | pass(nographics) | pass(공간 탐색) |
| PAN-010 병실 | PRM-010 v001 | [AST-2010 v004](../assets/AST-2010-v004.md) | 9 | 1604 | 3432332 | pass(nographics) | pass(공간 탐색) |
| PAN-011 의료 접수실 | PRM-011 v001 | [AST-2011 v003](../assets/AST-2011-v003.md) | 13 | 2432 | 3495312 | pass(nographics) | pass(공간 탐색) |
| PAN-012 교실 | PRM-012 v001 | [AST-2012 v002](../assets/AST-2012-v002.md) | 14 | 1872 | 3462752 | pass(nographics) | pass(공간 탐색) |
| PAN-013 교육 실습실 | PRM-013 v001 | [AST-2013 v002](../assets/AST-2013-v002.md) | 12 | 1420 | 3418360 | pass(nographics) | pass(공간 탐색) |
| PAN-014 강의실 | PRM-014 v001 | [AST-2014 v003](../assets/AST-2014-v003.md) | 12 | 1780 | 3444980 | pass(nographics) | pass(공간 탐색) |
| PAN-015 복지·심리 상담실 | PRM-015 v001 | [AST-2015 v002](../assets/AST-2015-v002.md) | 10 | 1516 | 3421412 | pass(nographics) | pass(공간 탐색) |
| PAN-016 복지 활동실 | PRM-016 v001 | [AST-2016 v003](../assets/AST-2016-v003.md) | 10 | 1396 | 3415520 | pass(nographics) | pass(공간 탐색) |
| PAN-017 요양실 | PRM-017 v001 | [AST-2017 v002](../assets/AST-2017-v002.md) | 9 | 1496 | 3421140 | pass(nographics) | pass(공간 탐색) |
| PAN-018 생산 구역 | PRM-018 v001 | [AST-2018 v003](../assets/AST-2018-v003.md) | 10 | 1684 | 3438264 | pass(nographics) | pass(공간 탐색) |
| PAN-019 조립 구역 | PRM-019 v001 | [AST-2019 v002](../assets/AST-2019-v002.md) | 11 | 1680 | 3445368 | pass(nographics) | pass(공간 탐색) |
| PAN-020 정비 구역 | PRM-020 v001 | [AST-2020 v002](../assets/AST-2020-v002.md) | 10 | 1540 | 3429944 | pass(nographics) | pass(공간 탐색) |
| PAN-021 소매점 | PRM-021 v001 | [AST-2021 v002](../assets/AST-2021-v002.md) | 12 | 1068 | 3387896 | pass(nographics) | pass(공간 탐색) |
| PAN-022 서비스 창구 | PRM-022 v001 | [AST-2022 v004](../assets/AST-2022-v004.md) | 13 | 1932 | 3449508 | pass(nographics) | pass(공간 탐색) |
| PAN-023 미용실 | PRM-023 v001 | [AST-2023 v002](../assets/AST-2023-v002.md) | 9 | 1532 | 3424304 | pass(nographics) | pass(공간 탐색) |
| PAN-024 주방 | PRM-024 v001 | [AST-2024 v003](../assets/AST-2024-v003.md) | 9 | 1448 | 3416584 | pass(nographics) | pass(공간 탐색) |
| PAN-025 제과실 | PRM-025 v001 | [AST-2025 v002](../assets/AST-2025-v002.md) | 10 | 1524 | 3426072 | pass(nographics) | pass(공간 탐색) |
| PAN-026 식당 홀 | PRM-026 v001 | [AST-2026 v002](../assets/AST-2026-v002.md) | 13 | 1928 | 3457664 | pass(nographics) | pass(공간 탐색) |
| PAN-027 디자인 작업실 | PRM-027 v001 | [AST-2027 v004](../assets/AST-2027-v004.md) | 11 | 1692 | 3428596 | pass(nographics) | pass(공간 탐색) |
| PAN-028 미술 작업실 | PRM-028 v001 | [AST-2028 v004](../assets/AST-2028-v004.md) | 11 | 1432 | 3411824 | pass(nographics) | pass(공간 탐색) |
| PAN-029 공예 작업실 | PRM-029 v001 | [AST-2029 v001](../assets/AST-2029-v001.md) | 9 | 1256 | 3399892 | pass(nographics) | pass(공간 탐색) |
| PAN-030 촬영 스튜디오 | PRM-030 v001 | [AST-2030 v002](../assets/AST-2030-v002.md) | 10 | 1216 | 3394844 | pass(nographics) | pass(공간 탐색) |
| PAN-031 방송 스튜디오 | PRM-031 v001 | [AST-2031 v004](../assets/AST-2031-v004.md) | 11 | 1624 | 3420784 | pass(nographics) | pass(공간 탐색) |
| PAN-032 영상 편집실 | PRM-032 v001 | [AST-2032 v003](../assets/AST-2032-v003.md) | 12 | 2428 | 3440500 | pass(nographics) | pass(공간 탐색) |
| PAN-033 공연 무대 | PRM-033 v001 | [AST-2033 v002](../assets/AST-2033-v002.md) | 15 | 2580 | 3484428 | pass(nographics) | pass(공간 탐색) |
| PAN-034 전시실 | PRM-034 v001 | [AST-2034 v002](../assets/AST-2034-v002.md) | 10 | 1212 | 3395716 | pass(nographics) | pass(공간 탐색) |
| PAN-035 문화 활동실 | PRM-035 v001 | [AST-2035 v002](../assets/AST-2035-v002.md) | 10 | 1700 | 3441416 | pass(nographics) | pass(공간 탐색) |
| PAN-036 건축 작업 구역 | PRM-036 v001 | [AST-2036 v003](../assets/AST-2036-v003.md) | 9 | 1452 | 3435932 | pass(nographics) | pass(공간 탐색) |
| PAN-037 설비 작업 구역 | PRM-037 v001 | [AST-2037 v003](../assets/AST-2037-v003.md) | 9 | 1376 | 3413400 | pass(nographics) | pass(공간 탐색) |
| PAN-038 환경 조사 지점 | PRM-038 v001 | [AST-2038 v002](../assets/AST-2038-v002.md) | 10 | 1068 | 3376760 | pass(nographics) | pass(공간 탐색) |
| PAN-039 관측 지점 | PRM-039 v001 | [AST-2039 v004](../assets/AST-2039-v004.md) | 10 | 1648 | 3430856 | pass(nographics) | pass(공간 탐색) |
| PAN-040 재배지 | PRM-040 v001 | [AST-2040 v003](../assets/AST-2040-v003.md) | 12 | 2736 | 3607032 | pass(nographics) | pass(공간 탐색) |
| PAN-041 온실 | PRM-041 v001 | [AST-2041 v002](../assets/AST-2041-v002.md) | 10 | 2588 | 3562840 | pass(nographics) | pass(공간 탐색) |
| PAN-042 축사 | PRM-042 v001 | [AST-2042 v002](../assets/AST-2042-v002.md) | 10 | 1152 | 3389664 | pass(nographics) | pass(공간 탐색) |
| PAN-043 동물 관리실 | PRM-043 v001 | [AST-2043 v003](../assets/AST-2043-v003.md) | 10 | 1568 | 3434908 | pass(nographics) | pass(공간 탐색) |
| PAN-044 선박 갑판 | PRM-044 v001 | [AST-2044 v003](../assets/AST-2044-v003.md) | 12 | 1456 | 3405372 | pass(nographics) | pass(공간 탐색) |
| PAN-045 조타실 | PRM-045 v001 | [AST-2045 v003](../assets/AST-2045-v003.md) | 9 | 1236 | 3403492 | pass(nographics) | pass(공간 탐색) |
| PAN-046 부두 | PRM-046 v001 | [AST-2046 v003](../assets/AST-2046-v003.md) | 11 | 1280 | 3388544 | pass(nographics) | pass(공간 탐색) |
| PAN-047 체육관 | PRM-047 v001 | [AST-2047 v002](../assets/AST-2047-v002.md) | 7 | 1392 | 3411240 | pass(nographics) | pass(공간 탐색) |
| PAN-048 운동 지도실 | PRM-048 v001 | [AST-2048 v002](../assets/AST-2048-v002.md) | 8 | 908 | 3363064 | pass(nographics) | pass(공간 탐색) |
| PAN-049 경기 구역 | PRM-049 v001 | [AST-2049 v002](../assets/AST-2049-v002.md) | 8 | 1388 | 3412092 | pass(nographics) | pass(공간 탐색) |
| PAN-050 수사실 | PRM-050 v001 | [AST-2050 v004](../assets/AST-2050-v004.md) | 14 | 2104 | 3470176 | pass(nographics) | pass(공간 탐색) |
| PAN-051 증거 분석실 | PRM-051 v001 | [AST-2051 v004](../assets/AST-2051-v004.md) | 13 | 1508 | 3435132 | pass(nographics) | pass(공간 탐색) |
| PAN-052 법정 | PRM-052 v001 | [AST-2052 v001](../assets/AST-2052-v001.md) | 12 | 1560 | 3430524 | pass(nographics) | pass(공간 탐색) |
| PAN-053 물류 창고 | PRM-053 v001 | [AST-2053 v002](../assets/AST-2053-v002.md) | 11 | 1132 | 3396680 | pass(nographics) | pass(공간 탐색) |
| PAN-054 운송 조종 공간 | PRM-054 v001 | [AST-2054 v003](../assets/AST-2054-v003.md) | 10 | 1260 | 3406792 | pass(nographics) | pass(공간 탐색) |
| PAN-055 운송 거점 | PRM-055 v001 | [AST-2055 v002](../assets/AST-2055-v002.md) | 10 | 1852 | 3454400 | pass(nographics) | pass(공간 탐색) |
| PAN-056 금융 창구 | PRM-056 v001 | [AST-2056 v004](../assets/AST-2056-v004.md) | 16 | 3140 | 3540680 | pass(nographics) | pass(공간 탐색) |
| PAN-057 금융 상담실 | PRM-057 v001 | [AST-2057 v002](../assets/AST-2057-v002.md) | 10 | 1376 | 3412696 | pass(nographics) | pass(공간 탐색) |
| PAN-058 가정 수리 공간 | PRM-058 v001 | [AST-2058 v002](../assets/AST-2058-v002.md) | 9 | 1224 | 3393268 | pass(nographics) | pass(공간 탐색) |
| PAN-059 방문 학습 공간 | PRM-059 v001 | [AST-2059 v002](../assets/AST-2059-v002.md) | 9 | 960 | 3370004 | pass(nographics) | pass(공간 탐색) |
| PAN-060 서버실 | PRM-060 v001 | [AST-2060 v003](../assets/AST-2060-v003.md) | 11 | 2252 | 3528072 | pass(nographics) | pass(공간 탐색) |
| PAN-061 관제실 | PRM-061 v001 | [AST-2061 v004](../assets/AST-2061-v004.md) | 11 | 2076 | 3475632 | pass(nographics) | pass(공간 탐색) |
| PAN-062 거실 | PRM-062 v001 | [AST-2062 v002](../assets/AST-2062-v002.md) | 8 | 1272 | 3394780 | pass(nographics) | pass(공간 탐색) |
| PAN-063 주택 관리 공간 | PRM-063 v001 | [AST-2063 v004](../assets/AST-2063-v004.md) | 11 | 1396 | 3416700 | pass(nographics) | pass(공간 탐색) |
| PAN-064 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | [AST-2064 v002](../assets/AST-2064-v002.md) | 11 | 1532 | 3432096 | pass(nographics) | pass(공간 탐색) |
| PAN-070 불교 법당 — 스님 | PRM-070 v001 | [AST-2070 v003](../assets/AST-2070-v003.md) | 14 | 1164 | 3396196 | pass(nographics) | pass(공간 탐색) |
| PAN-071 천주교 성당 — 신부님 | PRM-071 v001 | [AST-2071 v002](../assets/AST-2071-v002.md) | 14 | 1760 | 3445180 | pass(nographics) | pass(공간 탐색) |
| PAN-065 군 행정실 | PRM-065 v001 | [AST-2065 v003](../assets/AST-2065-v003.md) | 13 | 2060 | 3462212 | pass(nographics) | pass(공간 탐색) |
| PAN-066 생활관 | PRM-066 v001 | [AST-2066 v002](../assets/AST-2066-v002.md) | 12 | 1616 | 3449836 | pass(nographics) | pass(공간 탐색) |
| PAN-067 장비 관리실 | PRM-067 v001 | [AST-2067 v003](../assets/AST-2067-v003.md) | 10 | 1584 | 3437080 | pass(nographics) | pass(공간 탐색) |
| PAN-068 출장 업무 공간 | PRM-068 v001 | [AST-2068 v002](../assets/AST-2068-v002.md) | 9 | 1136 | 3385068 | pass(nographics) | pass(공간 탐색) |
| PAN-069 안내 집결 지점 | PRM-069 v001 | [AST-2069 v002](../assets/AST-2069-v002.md) | 11 | 1468 | 3418740 | pass(nographics) | pass(공간 탐색) |

## 직접 작업·통신·미검증·전달

[실제 사무보조원 검수](../../machine/evidence/workplaces-v006/office-direct-http-acceptance.json)는19건 통과·제품 실패 0·콘솔/자원 오류0건이다. 검수기 관찰 3건과 해결 근거를 원문에 보존했다. 실제 900×600 Tab/ShiftTab·Unicode 입력·저장·Esc복귀·보이는 모션 감소 토글의 즉시 전환, 기본 0.45초 전환, 실제 출력/분류/인계·요청 변경, Unity→React 과정/결과/종료·복원은 해당 보고의 범위에서 통과했다. EX010은 기존 선택형 연습으로 미구현이며 다른 551개 직업 초안은 구현/승인하지 않았다. Native 업무 UI 전체는 별도 미검증이며 Native 71개 장면 로드 통과와 구별한다.

Safari·Firefox·실제 모바일 기기·하드웨어 GPU 성능/드로콜·화면낭독기·외부HTTPS배포는 미검증이다. 작은/가려진 부위와 임의각도/필터링환경은 실제 [시각 검수의 한계](../assets/workplace-browser-visual-review-v006.md)를 따른다. 이 한계와 얇은 선의 비차단 대비 관찰을 숨기지 않는다.

최종 ZIP·manifest·추출 HTTP 검수는 완료했고 실제 영수증을 등록했다. Unity 편집 프로젝트와 Meshy/Blender 원본은 WebGL 전달본과 분리하며 이전 빌드/ZIP을 보존한다. `unity/webgl/builds/workplaces-v006`를 HTTP로 제공하고 receiver/와 licenses/를 함께 보존한다. index.html 더블클릭은 검수 대상이 아니다. wasm은 application/wasm으로 제공한다.

이번 Meshy 호출 0·실제 크레딧 0·유료 이미지 생성 0이다. Blender 직접 제작·교정과 기존 고정 모델/스크립트를 재사용했다. 과거 비용은 별도이며 입력/캐시/출력토큰·작업별 시간/비용 배분은 도구 미제공으로 null/미측정이다. 빌드 실행 시간을 전체 제작 시간으로 쓰지 않는다.

[최종 원장·readiness 검토](../../machine/evidence/workplaces-catalog-review-v001/v006-final-readiness.json): 현재319개 모델,805개 배치, 원장·후보·소스·실제 이미지 해시와 문서 링크를 독립 대조했다. 패키지 추출 HTTP 검수는 별도 영수증을 따른다.

## 최종 전달 파일과 실제 추출 검수

- [WebGL ZIP](../../../unity/webgl/packages/workplaces-v006.zip): 30,156,167바이트, 파일16개. Unity/Blender 편집 원본은 ZIP과 분리했다.
- [전달 manifest](../../../unity/webgl/packages/workplaces-v006.manifest.json), [무결성 영수증](../../machine/evidence/workplaces-v006/package-integrity.json), [새로 추출한 HTTP 실행](../../machine/evidence/workplaces-v006/package-http-boot.json), [실행 안내](workplaces-v006-run.md).
- ZIP SHA-256: `1decbc9185889118ca649b410aa220349f35ac0e6de02b9e3e2c77e0ff991798`.

CRC·모든 payload 해시가 통과했다. 새 추출본에서 71개 공간 목록을 로드하고 실제 PAN-001 버튼→3D 모니터 확대를 확인했다. 번들 React의 상대경로 iframe과 실제 체험 시작→동일 experienceId의 experience.started 수신도 통과했다. 추출본 검수는 이 2건의 부팅/연결 범위다. 71개 공간·직접 업무 전체를 추출본에서 다시 실행했다고 기록하지 않는다.

ZIP 안의 manifest와 동봉 사본은 생성 당시 readiness 스냅샷이다. 완성된 ZIP의 최종 SHA/상태/추출 영수증은 ZIP 밖의 현재 builds.json과 package-integrity.json에 기록한다. 이 작성 순서에 따라 manifest를 다시 쓰거나 검수한 ZIP을 변경하지 않았다. 외부 HTTPS 배포는 수행하지 않아 artifact_url은 null이다.

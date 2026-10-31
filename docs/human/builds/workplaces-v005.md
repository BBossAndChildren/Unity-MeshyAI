# workplaces-v005 — 71개 3D 공간 Unity WebGL

> 현재 재개 지점: v005는 실제71개 공간·Native검수 근거를 보존한 중간본이다. 사무보조원900×600Tab/진단좌표 및 전환 설정 보완을 후속 workplaces-v006에서 실제 재검수한다. v005의 공간 통과를 v006의 체험·통신 최종 통과로 승계하지 않는다. 최종 ZIP/ready는 아직 등록하지 않았다.

기존71개 파노라마를 기준으로 만든 실제3D 공간을 한 Unity 프로젝트에서 선택·회전·확대해 탐색하는 빌드다. 스카이박스/평면 파노라마 대체가 아니다. 사무보조원은 기존세 물건을 선택해 확대하고 문서 입력·출력·묶음 분류·인계를 수행하는 직접 작업형으로 확장했다. 다른551개 직업 초안·미선택 대안은 자동 확정하지 않았다.

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
| 빌드 | Succeeded / 2026-10-31T06:50:18.6640486+09:00 |
| Unity 보고 크기 | 57549236바이트 |
| 오류·경고 | 0 / 0 |
| Unity 빌드 시간 | 121.8642465초(모델링·작성·검수 전체 시간 아님) |
| 소스 HEAD | `308507ce0429cc85106035ee3fac367db6756c1d` + 기존/이번 미커밋 변경 보존 |
| 편집 프로젝트 | `unity/projects/OfficeAssistant-v001` |
| WebGL 출력 | `unity/webgl/builds/workplaces-v005` |
| 모델 채색 | palette v0012508×2508PNG한 장·공용 모델 재질한 개, 원본 색 유지 |
| 의존성 | Unity WebGL 및 수신 예제의 번들 React/ReactDOM/scheduler; 새 유료 서비스/런타임GLB로더 없음 |

[실제 빌드 근거](../../machine/evidence/workplaces-v005/build-result.json), [13개 소스·AGENTS 동일성 검수](../../machine/evidence/workplaces-v005/source-snapshot-after-build.json). 원본 color1/color2와 최종PNG는 보존했고512개 색상 칸을 원본JPEG디코드값과 대조했다([근거](../../machine/evidence/workplaces-model-review-v001/palette-source-cells.json)). 모델 재질/팔레트는 UI폰트·화면 자원과 구별한다.

## 모델과 실제 실행 검수

최종GLB를 실제Blender로 다시 열고 삼각형·UV·재질을 조사했다. 반복 배치 포함 공간별908~4308삼각형으로5000목표 이내다. 모든 개별 소품은1000이하 기록이다. 실제 변환 버텍스 지지면/접지476건0실패를 검사했다([지지면 보고](../../machine/evidence/workplaces-model-review-v001/visual-review-v002.json), [상세 결과](../../machine/evidence/workplaces-model-review-v001/support-summary-v003.json)). 이 근거를 Unity/HTTP실행의 대체로 사용하지 않는다.

실제 Unity Editor Play Mode71/71통과([보고](../../machine/evidence/workplaces-v005/unity-editor-play-rooms.json), [로그](../../machine/evidence/workplaces-v005/unity-editor-play.log)). 환경은 batchmode -nographics다. 실제 장면 로드·메시·콜라이더·모델 재질/텍스처·2508×2508임포트를 확인했으며 시각 검수와 HTTP실행은 별도다.

실제HTTP 공간 탐색71/71과 공통2건(일시정지 입력 잠금·복귀, 에뮬레이션 터치 공간 선택)이 통과했고 콘솔 오류0건이다([실제 보고](../../machine/evidence/workplaces-v005/http-webgl-rooms.json)). 별도의 [사무보조원 중간 검수](../../machine/evidence/workplaces-v005/office-direct-http-acceptance.json)는15통과·실제900×600Tab/좌표 문제1건·검수기 관찰2건을 기록했다. 따라서 이 빌드는 공간 탐색 범위의 통과이며 최종 체험/통신 전체 통과가 아니다. 후속v006은 다시 실제 검수한다.

| 공간 | 고정 prompt | 고정 조립 | 구성 수량 | 삼각형 | GLB 바이트 | Unity Play | 최종 HTTP |
|---|---|---|---:|---:|---:|---|---|
| PAN-001 공용 업무 사무실 | PRM-001 v001 | [AST-020 v006](../assets/AST-020-v006.md) | 30 | 4308 | 3608352 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-002 협업·기획 사무실 | PRM-002 v001 | [AST-2002 v003](../assets/AST-2002-v003.md) | 17 | 2552 | 3503348 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-003 행정·문서 처리 사무실 | PRM-003 v001 | [AST-2003 v004](../assets/AST-2003-v004.md) | 23 | 3764 | 3597220 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-004 민원·방문객 접수실 | PRM-004 v001 | [AST-2004 v003](../assets/AST-2004-v003.md) | 9 | 2256 | 3474112 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-005 전문 상담 사무실 | PRM-005 v001 | [AST-2005 v002](../assets/AST-2005-v002.md) | 14 | 1832 | 3453236 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-006 실험실 | PRM-006 v001 | [AST-2006 v002](../assets/AST-2006-v002.md) | 11 | 1552 | 3429852 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-007 분석실 | PRM-007 v001 | [AST-2007 v004](../assets/AST-2007-v004.md) | 10 | 1700 | 3428396 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-008 진료실 | PRM-008 v001 | [AST-2008 v003](../assets/AST-2008-v003.md) | 12 | 2732 | 3515952 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-009 처치실 | PRM-009 v001 | [AST-2009 v002](../assets/AST-2009-v002.md) | 10 | 1804 | 3448788 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-010 병실 | PRM-010 v001 | [AST-2010 v004](../assets/AST-2010-v004.md) | 9 | 1604 | 3432332 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-011 의료 접수실 | PRM-011 v001 | [AST-2011 v003](../assets/AST-2011-v003.md) | 13 | 2432 | 3495312 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-012 교실 | PRM-012 v001 | [AST-2012 v002](../assets/AST-2012-v002.md) | 14 | 1872 | 3462752 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-013 교육 실습실 | PRM-013 v001 | [AST-2013 v002](../assets/AST-2013-v002.md) | 12 | 1420 | 3418360 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-014 강의실 | PRM-014 v001 | [AST-2014 v003](../assets/AST-2014-v003.md) | 12 | 1780 | 3444980 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-015 복지·심리 상담실 | PRM-015 v001 | [AST-2015 v002](../assets/AST-2015-v002.md) | 10 | 1516 | 3421412 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-016 복지 활동실 | PRM-016 v001 | [AST-2016 v003](../assets/AST-2016-v003.md) | 10 | 1396 | 3415520 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-017 요양실 | PRM-017 v001 | [AST-2017 v002](../assets/AST-2017-v002.md) | 9 | 1496 | 3421140 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-018 생산 구역 | PRM-018 v001 | [AST-2018 v003](../assets/AST-2018-v003.md) | 10 | 1684 | 3438264 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-019 조립 구역 | PRM-019 v001 | [AST-2019 v002](../assets/AST-2019-v002.md) | 11 | 1680 | 3445368 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-020 정비 구역 | PRM-020 v001 | [AST-2020 v002](../assets/AST-2020-v002.md) | 10 | 1540 | 3429944 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-021 소매점 | PRM-021 v001 | [AST-2021 v002](../assets/AST-2021-v002.md) | 12 | 1068 | 3387896 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-022 서비스 창구 | PRM-022 v001 | [AST-2022 v004](../assets/AST-2022-v004.md) | 13 | 1932 | 3449508 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-023 미용실 | PRM-023 v001 | [AST-2023 v002](../assets/AST-2023-v002.md) | 9 | 1532 | 3424304 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-024 주방 | PRM-024 v001 | [AST-2024 v003](../assets/AST-2024-v003.md) | 9 | 1448 | 3416584 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-025 제과실 | PRM-025 v001 | [AST-2025 v002](../assets/AST-2025-v002.md) | 10 | 1524 | 3426072 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-026 식당 홀 | PRM-026 v001 | [AST-2026 v002](../assets/AST-2026-v002.md) | 13 | 1928 | 3457664 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-027 디자인 작업실 | PRM-027 v001 | [AST-2027 v004](../assets/AST-2027-v004.md) | 11 | 1692 | 3428596 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-028 미술 작업실 | PRM-028 v001 | [AST-2028 v004](../assets/AST-2028-v004.md) | 11 | 1432 | 3411824 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-029 공예 작업실 | PRM-029 v001 | [AST-2029 v001](../assets/AST-2029-v001.md) | 9 | 1256 | 3399892 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-030 촬영 스튜디오 | PRM-030 v001 | [AST-2030 v002](../assets/AST-2030-v002.md) | 10 | 1216 | 3394844 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-031 방송 스튜디오 | PRM-031 v001 | [AST-2031 v004](../assets/AST-2031-v004.md) | 11 | 1624 | 3420784 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-032 영상 편집실 | PRM-032 v001 | [AST-2032 v003](../assets/AST-2032-v003.md) | 12 | 2428 | 3440500 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-033 공연 무대 | PRM-033 v001 | [AST-2033 v002](../assets/AST-2033-v002.md) | 15 | 2580 | 3484428 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-034 전시실 | PRM-034 v001 | [AST-2034 v002](../assets/AST-2034-v002.md) | 10 | 1212 | 3395716 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-035 문화 활동실 | PRM-035 v001 | [AST-2035 v002](../assets/AST-2035-v002.md) | 10 | 1700 | 3441416 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-036 건축 작업 구역 | PRM-036 v001 | [AST-2036 v003](../assets/AST-2036-v003.md) | 9 | 1452 | 3435932 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-037 설비 작업 구역 | PRM-037 v001 | [AST-2037 v003](../assets/AST-2037-v003.md) | 9 | 1376 | 3413400 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-038 환경 조사 지점 | PRM-038 v001 | [AST-2038 v002](../assets/AST-2038-v002.md) | 10 | 1068 | 3376760 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-039 관측 지점 | PRM-039 v001 | [AST-2039 v004](../assets/AST-2039-v004.md) | 10 | 1648 | 3430856 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-040 재배지 | PRM-040 v001 | [AST-2040 v003](../assets/AST-2040-v003.md) | 12 | 2736 | 3607032 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-041 온실 | PRM-041 v001 | [AST-2041 v002](../assets/AST-2041-v002.md) | 10 | 2588 | 3562840 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-042 축사 | PRM-042 v001 | [AST-2042 v002](../assets/AST-2042-v002.md) | 10 | 1152 | 3389664 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-043 동물 관리실 | PRM-043 v001 | [AST-2043 v003](../assets/AST-2043-v003.md) | 10 | 1568 | 3434908 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-044 선박 갑판 | PRM-044 v001 | [AST-2044 v003](../assets/AST-2044-v003.md) | 12 | 1456 | 3405372 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-045 조타실 | PRM-045 v001 | [AST-2045 v003](../assets/AST-2045-v003.md) | 9 | 1236 | 3403492 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-046 부두 | PRM-046 v001 | [AST-2046 v003](../assets/AST-2046-v003.md) | 11 | 1280 | 3388544 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-047 체육관 | PRM-047 v001 | [AST-2047 v002](../assets/AST-2047-v002.md) | 7 | 1392 | 3411240 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-048 운동 지도실 | PRM-048 v001 | [AST-2048 v002](../assets/AST-2048-v002.md) | 8 | 908 | 3363064 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-049 경기 구역 | PRM-049 v001 | [AST-2049 v002](../assets/AST-2049-v002.md) | 8 | 1388 | 3412092 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-050 수사실 | PRM-050 v001 | [AST-2050 v004](../assets/AST-2050-v004.md) | 14 | 2104 | 3470176 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-051 증거 분석실 | PRM-051 v001 | [AST-2051 v004](../assets/AST-2051-v004.md) | 13 | 1508 | 3435132 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-052 법정 | PRM-052 v001 | [AST-2052 v001](../assets/AST-2052-v001.md) | 12 | 1560 | 3430524 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-053 물류 창고 | PRM-053 v001 | [AST-2053 v002](../assets/AST-2053-v002.md) | 11 | 1132 | 3396680 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-054 운송 조종 공간 | PRM-054 v001 | [AST-2054 v003](../assets/AST-2054-v003.md) | 10 | 1260 | 3406792 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-055 운송 거점 | PRM-055 v001 | [AST-2055 v002](../assets/AST-2055-v002.md) | 10 | 1852 | 3454400 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-056 금융 창구 | PRM-056 v001 | [AST-2056 v004](../assets/AST-2056-v004.md) | 16 | 3140 | 3540680 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-057 금융 상담실 | PRM-057 v001 | [AST-2057 v002](../assets/AST-2057-v002.md) | 10 | 1376 | 3412696 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-058 가정 수리 공간 | PRM-058 v001 | [AST-2058 v002](../assets/AST-2058-v002.md) | 9 | 1224 | 3393268 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-059 방문 학습 공간 | PRM-059 v001 | [AST-2059 v002](../assets/AST-2059-v002.md) | 9 | 960 | 3370004 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-060 서버실 | PRM-060 v001 | [AST-2060 v003](../assets/AST-2060-v003.md) | 11 | 2252 | 3528072 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-061 관제실 | PRM-061 v001 | [AST-2061 v004](../assets/AST-2061-v004.md) | 11 | 2076 | 3475632 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-062 거실 | PRM-062 v001 | [AST-2062 v002](../assets/AST-2062-v002.md) | 8 | 1272 | 3394780 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-063 주택 관리 공간 | PRM-063 v001 | [AST-2063 v004](../assets/AST-2063-v004.md) | 11 | 1396 | 3416700 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-064 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | [AST-2064 v002](../assets/AST-2064-v002.md) | 11 | 1532 | 3432096 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-070 불교 법당 — 스님 | PRM-070 v001 | [AST-2070 v003](../assets/AST-2070-v003.md) | 14 | 1164 | 3396196 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-071 천주교 성당 — 신부님 | PRM-071 v001 | [AST-2071 v002](../assets/AST-2071-v002.md) | 14 | 1760 | 3445180 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-065 군 행정실 | PRM-065 v001 | [AST-2065 v003](../assets/AST-2065-v003.md) | 13 | 2060 | 3462212 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-066 생활관 | PRM-066 v001 | [AST-2066 v002](../assets/AST-2066-v002.md) | 12 | 1616 | 3449836 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-067 장비 관리실 | PRM-067 v001 | [AST-2067 v003](../assets/AST-2067-v003.md) | 10 | 1584 | 3437080 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-068 출장 업무 공간 | PRM-068 v001 | [AST-2068 v002](../assets/AST-2068-v002.md) | 9 | 1136 | 3385068 | pass(nographics) | pass(공간 탐색 한정) |
| PAN-069 안내 집결 지점 | PRM-069 v001 | [AST-2069 v002](../assets/AST-2069-v002.md) | 11 | 1468 | 3418740 | pass(nographics) | pass(공간 탐색 한정) |

## 미검증·전달·비용

모션 감소 reducedMotion은 Inspector설정으로 제공하며 실제 런타임 전환은 미검증이다. Safari·Firefox·실제 모바일기기·하드웨어GPU성능/드로콜·외부HTTPS배포·화면낭독기는 미검증이다. 기본/변경 요청·오류·재시도·닫기·종료·동등 입력과 Unity→React 결과는 최종 실행 보고에 기록한 범위만 완료로 설명한다.

최종 ZIP·manifest·추출 HTTP검수는 별도 준비 중이다. Unity 편집 프로젝트와 Meshy/Blender 원본은 WebGL ZIP에 넣지 않으며, 이전 빌드·ZIP을 덮어쓰지 않는다.

로컬 실행:

```powershell
python -m http.server 8178 --bind 127.0.0.1 --directory unity/webgl/builds
```

[공간 실행](http://127.0.0.1:8178/workplaces-v005/) · [React 수신 예제](http://127.0.0.1:8178/workplaces-v005/receiver/). index.html 더블클릭은 검수 대상이 아니다. 압축 없는WebGL이므로 별도 압축 헤더는 불필요하고 wasm은application/wasm으로 제공한다. 번들 수신 예제의 licenses/를 함께 보존한다.

이번 Meshy 호출0회·소비 크레딧0, 유료 이미지 생성0회. Blender직접 제작·고정 모델/스크립트 재사용이며 직접 제작을Meshy생성으로 기록하지 않았다. 기존 모델의 과거 비용은 별도다. 현재 추가 유료 승인 예산/잔여 크레딧과 입력·캐시·출력 토큰 및 작업별 시간/비용 배분은 도구 미제공으로null/미측정이다.

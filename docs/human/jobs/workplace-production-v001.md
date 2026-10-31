# 71개 공간 제작 진행 기록 v001

> 현재 v006은71개 실제공간과 사무보조원 v002구현 범위의 검수가 완료됐다. 최종 ZIP 무결성과 새 추출본 HTTP2건도 통과했다. 다른 551개 직업 초안은별도다.

현재 상태: 실제 workplaces-v006 빌드와71개 공간 Unity Editor Play Mode 검수를 마쳤고, 최종 HTTP·직접 작업·통신 검수는 수집 중이다. 완성/미검증 범위를 분리하며 이전 빌드의 pass를 새 공간/새 버전에 승계하지 않는다.

[기계용 진행 원장](../../machine/catalog/workplace-production-v001.json) · [최종 대상 빌드 보고](../builds/workplaces-v006.md) · [등록 모델 전체 색인](../assets/workplace-models-v001.md) · [최신 후보 v004](workplace-common-assets-v004.md).

## 고정 범위·실제 수량

| 집계 | 범위·수량 |
|---|---|
| 원본 기준 |71개 공간 /262개 후보 /공통55개 /최초 기존 모델 참조17개 |
| 제작 지원 연결 포함 v004 |공통68개 /전용180개 /inventory-only14개 /추가 후보-공간92쌍 |
| 고정 현재 모델 |248개 구성 소품 버전 +71개 조립 버전 =319개 |
| 보존 전체 등록 |489버전 /319개 고유 에셋 ID |
| 최종 빌드 장면 수량 |71개 장면의805개 구성 인스턴스(프리팹/조립 부모 추가 집계 제외) |
| 전체 프로젝트 source 수량 |835개(최종805+보존 legacy OfficeAssistant.unity30) |

실제 수량·변환·현재/과거·빌드 포함·실행의 원장은 asset-usages.json과 scene-assemblies.json이다. 이 문서는 조회 결과이며 독립 사용 원장이 아니다. 최종 변환 버텍스 기반 지지면/접지476건0실패를 검사했다. 모델·공간·체험·통신 완료 범위를 구별한다.

## 공간별 최신 고정 버전과 검수

| 정확한 공간 | prompt | panorama | 현재 조립 고정 버전 | 구성 수량 | GLB 삼각형 | GLB 바이트 | Unity Play | 최종 HTTP | 체험/통신 |
|---|---|---|---|---:|---:|---:|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | [AST-020 v006](../assets/AST-020-v006.md) | 30 | 4308 | 3608352 | pass(nographics) | pass(공간 탐색) | 사무보조원 v002 구현·최종 검수 중 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | [AST-2002 v003](../assets/AST-2002-v003.md) | 17 | 2552 | 3503348 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | [AST-2003 v004](../assets/AST-2003-v004.md) | 23 | 3764 | 3597220 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | [AST-2004 v003](../assets/AST-2004-v003.md) | 9 | 2256 | 3474112 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | [AST-2005 v002](../assets/AST-2005-v002.md) | 14 | 1832 | 3453236 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 실험실 | PRM-006 v001 | PAN-006 v001 | [AST-2006 v002](../assets/AST-2006-v002.md) | 11 | 1552 | 3429852 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | [AST-2007 v004](../assets/AST-2007-v004.md) | 10 | 1700 | 3428396 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | [AST-2008 v003](../assets/AST-2008-v003.md) | 12 | 2732 | 3515952 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | [AST-2009 v002](../assets/AST-2009-v002.md) | 10 | 1804 | 3448788 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 병실 | PRM-010 v001 | PAN-010 v001 | [AST-2010 v004](../assets/AST-2010-v004.md) | 9 | 1604 | 3432332 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | [AST-2011 v003](../assets/AST-2011-v003.md) | 13 | 2432 | 3495312 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 교실 | PRM-012 v001 | PAN-012 v001 | [AST-2012 v002](../assets/AST-2012-v002.md) | 14 | 1872 | 3462752 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | [AST-2013 v002](../assets/AST-2013-v002.md) | 12 | 1420 | 3418360 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 강의실 | PRM-014 v001 | PAN-014 v001 | [AST-2014 v003](../assets/AST-2014-v003.md) | 12 | 1780 | 3444980 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | [AST-2015 v002](../assets/AST-2015-v002.md) | 10 | 1516 | 3421412 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | [AST-2016 v003](../assets/AST-2016-v003.md) | 10 | 1396 | 3415520 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | [AST-2017 v002](../assets/AST-2017-v002.md) | 9 | 1496 | 3421140 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | [AST-2018 v003](../assets/AST-2018-v003.md) | 10 | 1684 | 3438264 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | [AST-2019 v002](../assets/AST-2019-v002.md) | 11 | 1680 | 3445368 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | [AST-2020 v002](../assets/AST-2020-v002.md) | 10 | 1540 | 3429944 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | [AST-2021 v002](../assets/AST-2021-v002.md) | 12 | 1068 | 3387896 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | [AST-2022 v004](../assets/AST-2022-v004.md) | 13 | 1932 | 3449508 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | [AST-2023 v002](../assets/AST-2023-v002.md) | 9 | 1532 | 3424304 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 주방 | PRM-024 v001 | PAN-024 v001 | [AST-2024 v003](../assets/AST-2024-v003.md) | 9 | 1448 | 3416584 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 제과실 | PRM-025 v001 | PAN-025 v001 | [AST-2025 v002](../assets/AST-2025-v002.md) | 10 | 1524 | 3426072 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | [AST-2026 v002](../assets/AST-2026-v002.md) | 13 | 1928 | 3457664 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | [AST-2027 v004](../assets/AST-2027-v004.md) | 11 | 1692 | 3428596 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | [AST-2028 v004](../assets/AST-2028-v004.md) | 11 | 1432 | 3411824 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | [AST-2029 v001](../assets/AST-2029-v001.md) | 9 | 1256 | 3399892 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | [AST-2030 v002](../assets/AST-2030-v002.md) | 10 | 1216 | 3394844 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | [AST-2031 v004](../assets/AST-2031-v004.md) | 11 | 1624 | 3420784 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | [AST-2032 v003](../assets/AST-2032-v003.md) | 12 | 2428 | 3440500 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | [AST-2033 v002](../assets/AST-2033-v002.md) | 15 | 2580 | 3484428 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 전시실 | PRM-034 v001 | PAN-034 v001 | [AST-2034 v002](../assets/AST-2034-v002.md) | 10 | 1212 | 3395716 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | [AST-2035 v002](../assets/AST-2035-v002.md) | 10 | 1700 | 3441416 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | [AST-2036 v003](../assets/AST-2036-v003.md) | 9 | 1452 | 3435932 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | [AST-2037 v003](../assets/AST-2037-v003.md) | 9 | 1376 | 3413400 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | [AST-2038 v002](../assets/AST-2038-v002.md) | 10 | 1068 | 3376760 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | [AST-2039 v004](../assets/AST-2039-v004.md) | 10 | 1648 | 3430856 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 재배지 | PRM-040 v001 | PAN-040 v001 | [AST-2040 v003](../assets/AST-2040-v003.md) | 12 | 2736 | 3607032 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 온실 | PRM-041 v001 | PAN-041 v001 | [AST-2041 v002](../assets/AST-2041-v002.md) | 10 | 2588 | 3562840 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 축사 | PRM-042 v001 | PAN-042 v001 | [AST-2042 v002](../assets/AST-2042-v002.md) | 10 | 1152 | 3389664 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | [AST-2043 v003](../assets/AST-2043-v003.md) | 10 | 1568 | 3434908 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | [AST-2044 v003](../assets/AST-2044-v003.md) | 12 | 1456 | 3405372 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 조타실 | PRM-045 v001 | PAN-045 v001 | [AST-2045 v003](../assets/AST-2045-v003.md) | 9 | 1236 | 3403492 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 부두 | PRM-046 v001 | PAN-046 v001 | [AST-2046 v003](../assets/AST-2046-v003.md) | 11 | 1280 | 3388544 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 체육관 | PRM-047 v001 | PAN-047 v001 | [AST-2047 v002](../assets/AST-2047-v002.md) | 7 | 1392 | 3411240 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | [AST-2048 v002](../assets/AST-2048-v002.md) | 8 | 908 | 3363064 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | [AST-2049 v002](../assets/AST-2049-v002.md) | 8 | 1388 | 3412092 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | [AST-2050 v004](../assets/AST-2050-v004.md) | 14 | 2104 | 3470176 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | [AST-2051 v004](../assets/AST-2051-v004.md) | 13 | 1508 | 3435132 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 법정 | PRM-052 v001 | PAN-052 v001 | [AST-2052 v001](../assets/AST-2052-v001.md) | 12 | 1560 | 3430524 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | [AST-2053 v002](../assets/AST-2053-v002.md) | 11 | 1132 | 3396680 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | [AST-2054 v003](../assets/AST-2054-v003.md) | 10 | 1260 | 3406792 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | [AST-2055 v002](../assets/AST-2055-v002.md) | 10 | 1852 | 3454400 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | [AST-2056 v004](../assets/AST-2056-v004.md) | 16 | 3140 | 3540680 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | [AST-2057 v002](../assets/AST-2057-v002.md) | 10 | 1376 | 3412696 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | [AST-2058 v002](../assets/AST-2058-v002.md) | 9 | 1224 | 3393268 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | [AST-2059 v002](../assets/AST-2059-v002.md) | 9 | 960 | 3370004 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 서버실 | PRM-060 v001 | PAN-060 v001 | [AST-2060 v003](../assets/AST-2060-v003.md) | 11 | 2252 | 3528072 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | [AST-2061 v004](../assets/AST-2061-v004.md) | 11 | 2076 | 3475632 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 거실 | PRM-062 v001 | PAN-062 v001 | [AST-2062 v002](../assets/AST-2062-v002.md) | 8 | 1272 | 3394780 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | [AST-2063 v004](../assets/AST-2063-v004.md) | 11 | 1396 | 3416700 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | [AST-2064 v002](../assets/AST-2064-v002.md) | 11 | 1532 | 3432096 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | [AST-2070 v003](../assets/AST-2070-v003.md) | 14 | 1164 | 3396196 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | [AST-2071 v002](../assets/AST-2071-v002.md) | 14 | 1760 | 3445180 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | [AST-2065 v003](../assets/AST-2065-v003.md) | 13 | 2060 | 3462212 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | [AST-2066 v002](../assets/AST-2066-v002.md) | 12 | 1616 | 3449836 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | [AST-2067 v003](../assets/AST-2067-v003.md) | 10 | 1584 | 3437080 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | [AST-2068 v002](../assets/AST-2068-v002.md) | 9 | 1136 | 3385068 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | [AST-2069 v002](../assets/AST-2069-v002.md) | 11 | 1468 | 3418740 | pass(nographics) | pass(공간 탐색) | 미확정 직업 초안 자동 실행 안 함 |

## 시나리오·실행 근거·남은 작업

공용 업무 사무실은 career-experience-scenarios-v003 / career-net-253-office-documents v002 한 건 개정이다. 원래 v001과 다른 551개 초안/미선택 대안을 보존했다. [직접작업설계](office-assistant-direct-work-v002.md)와[공통통신문서](../integrations/workplace-runtime-protocol-v001.md)를 조회한다.

- 실제 v006 [빌드](../../machine/evidence/workplaces-v006/build-result.json), [Native71/71](../../machine/evidence/workplaces-v006/unity-editor-play-rooms.json), [HTTP71/71+공통2건](../../machine/evidence/workplaces-v006/http-webgl-rooms.json).
- [실제71쌍시각검수](../assets/workplace-browser-visual-review-v006.md), [현재319개별모델검수](../assets/workplace-current-model-coverage-v001.md), [476건지지면](../../machine/evidence/workplaces-model-review-v001/support-summary-v003.json).
- [사무보조원실제19건통과/제품 실패 0](../../machine/evidence/workplaces-v006/office-direct-http-acceptance.json), [전체모델/사용무결성](../../machine/evidence/workplaces-catalog-review-v001/v006-static-readiness-audit.json), [248필수후보누락0](../../machine/evidence/workplaces-catalog-review-v001/v006-required-candidate-coverage.json).

모션 감소의 실제 토글 즉시 전환과 900×600 키보드 문제 수정을 v006에서 검수했다. Native 업무 UI 전체, Safari/Firefox/실제모바일/하드웨어 GPU 성능·드로콜/화면낭독기/외부HTTPS는미검증이다. EX010 선택 연습과다른 551개 직업은 미구현이다. ZIP·manifest와 새 추출본 HTTP2건의 실제 검수/등록까지 완료했다.

## 실제 사용량·예산

이번 Meshy 호출0회·실제 크레딧0, 유료 이미지 생성0회. Blender직접 제작·교정과 기존 모델/스크립트 재사용이다. 과거 비용은 이번 비용에 합산하지 않는다. 현재 추가 승인 유료 예산과 잔여 크레딧은 미확인(null), 입력·캐시·출력 토큰과 작업별 시간/비용 배분은 도구 미제공으로 미측정이다. Unity 빌드 실행 시간을 전체 제작 시간으로 쓰지 않는다.

기존 원본·Blender·GLB·모델/조립/사용 revision·빌드·ZIP을 보존했다. 커밋·푸시·외부 배포는 하지 않는다.

[최종 원장·readiness 검토](../../machine/evidence/workplaces-catalog-review-v001/v006-final-readiness.json): 현재319개 모델,805개 배치, 원장·후보·소스·실제 이미지 해시와 문서 링크를 독립 대조했다. 패키지 추출 HTTP 검수는 별도 영수증을 따른다.

최종 전달: [workplaces-v006.zip](../../../unity/webgl/packages/workplaces-v006.zip), [manifest](../../../unity/webgl/packages/workplaces-v006.manifest.json), [실행 안내](../builds/workplaces-v006-run.md). 실제 30,156,167바이트·16파일이며 CRC/payload 해시와 새 추출본 부팅/React 연결2건이 통과했다([영수증](../../machine/evidence/workplaces-v006/package-integrity.json), [추출 HTTP](../../machine/evidence/workplaces-v006/package-http-boot.json)). ZIP 안 manifest는 생성 시점 스냅샷이며 최종 ZIP 해시와 영수증은 현재 원장에서 별도로 보존한다. Native GUI 업무 검수는 접근 승인 대기 시간 초과로 미검증이며, 기존 Native 장면71건 통과와 구별한다.

## 최신 공간 수정 — workplaces-v009

이전 본문 표는 v006 시점의 보존 기록이다. 최신 고정 모델과 검수는 [수정 보고](../builds/workplaces-v009.md)를 따른다. 현재71공간/818구성 인스턴스,327개 활성 모델 버전,528개 보존 등록 버전이다. 수정7공간만 새 HTTP21검사를 수행했다. Editor Play Mode와 나머지64공간의 새 HTTP실행은 미검증이며 기존 통과를 새 버전에 승계하지 않는다.

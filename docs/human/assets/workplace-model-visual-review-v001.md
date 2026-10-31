# 전체 공간 모델 시각 검토 v001

상태: 개요 방향·축소 검토 완료, 상세 부위별 웹 채색·필터링·실행 검수는 별도 미검증. 모델을 자동 ready로 변경하지 않았다.

[기계용 전체 검토 원장](../../machine/evidence/workplaces-model-review-v001/visual-review.json). 실제 Blender로 최종 GLB 326버전을 다시 열어 정면·측면·후면 978장을 렌더링했다. 현재 선택된 모델 302개 ID(신규 소품 231개·신규 공간 70개·사무실 조립 1개)를 아래에 빠짐없이 표시한다. 과거 보존 버전까지 포함한 렌더 수와 현재 모델 ID 수는 다르다.

수정: 받침 없이 떠 있던 의료 모니터·AV에 공통 카트를 추가했다. AST-005 발 원점 오프셋을 보정했고, 별도 캔버스 겹침·기록기/무전기/헤드폰/케이지 지지면·배관 밸브 미연결을 새 버전으로 교정했다. 사무실 AST-020 v004는 기존 30개 메시 이름과 4,308삼각형을 유지한다. 기존 원본·GLB·Blender 버전은 덮어쓰지 않았다.

검토 범위: 320px 방향별 원본 렌더와 약 106px 소품/160px 공간 축소 contact sheet의 외형·큰 부품 연결·후면 누락·의도하지 않은 큰 색 영역. 2샘플 렌더 노이즈가 있어 상세 색 번짐은 판정하지 않는다. 실제 Unity/WebGL·모바일·GPU 성능·드로콜은 이 보고서에서 검사하지 않았다.

CND-068의 목록 이름은 이동 보조 의자이나 모델은 열린 보행 보조 프레임이다. 참고 이미지의 전체 형태와 연결되지만 전문 장비 명칭·의자 좌판 필요 여부는 미검증이다.

이번 Meshy·유료 이미지 호출 0, 크레딧 0. Blender CLI 실제 실행 7회. 작업별 토큰 배분은 미측정이다.

## 현재 소품과 조립 모델 전체

| ID·버전 | 이름 | 종류 | 실제 최종 GLB 3방향 근거 |
|---|---|---|---|
| AST-020 v004 | PAN-001 일반 사무실 — 모니터 받침 정렬 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-020/v004/render-evidence.json) |
| AST-2002 v001 | 협업·기획 사무실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2002/v001/render-evidence.json) |
| AST-2003 v002 | 행정·문서 처리 사무실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2003/v002/render-evidence.json) |
| AST-2004 v002 | 민원·방문객 접수실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2004/v002/render-evidence.json) |
| AST-2005 v001 | 전문 상담 사무실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2005/v001/render-evidence.json) |
| AST-2006 v001 | 실험실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2006/v001/render-evidence.json) |
| AST-2007 v002 | 분석실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2007/v002/render-evidence.json) |
| AST-2008 v002 | 진료실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2008/v002/render-evidence.json) |
| AST-2009 v001 | 처치실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2009/v001/render-evidence.json) |
| AST-2010 v002 | 병실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2010/v002/render-evidence.json) |
| AST-2011 v002 | 의료 접수실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2011/v002/render-evidence.json) |
| AST-2012 v001 | 교실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2012/v001/render-evidence.json) |
| AST-2013 v001 | 교육 실습실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2013/v001/render-evidence.json) |
| AST-2014 v002 | 강의실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2014/v002/render-evidence.json) |
| AST-2015 v001 | 복지·심리 상담실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2015/v001/render-evidence.json) |
| AST-2016 v001 | 복지 활동실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2016/v001/render-evidence.json) |
| AST-2017 v001 | 요양실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2017/v001/render-evidence.json) |
| AST-2018 v001 | 생산 구역 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2018/v001/render-evidence.json) |
| AST-2019 v001 | 조립 구역 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2019/v001/render-evidence.json) |
| AST-2020 v001 | 정비 구역 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2020/v001/render-evidence.json) |
| AST-2021 v001 | 소매점 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2021/v001/render-evidence.json) |
| AST-2022 v002 | 서비스 창구 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2022/v002/render-evidence.json) |
| AST-2023 v001 | 미용실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2023/v001/render-evidence.json) |
| AST-2024 v001 | 주방 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2024/v001/render-evidence.json) |
| AST-2025 v001 | 제과실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2025/v001/render-evidence.json) |
| AST-2026 v001 | 식당 홀 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2026/v001/render-evidence.json) |
| AST-2027 v002 | 디자인 작업실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2027/v002/render-evidence.json) |
| AST-2028 v002 | 미술 작업실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2028/v002/render-evidence.json) |
| AST-2029 v001 | 공예 작업실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2029/v001/render-evidence.json) |
| AST-2030 v001 | 촬영 스튜디오 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2030/v001/render-evidence.json) |
| AST-2031 v002 | 방송 스튜디오 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2031/v002/render-evidence.json) |
| AST-2032 v003 | 영상 편집실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2032/v003/render-evidence.json) |
| AST-2033 v001 | 공연 무대 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2033/v001/render-evidence.json) |
| AST-2034 v001 | 전시실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2034/v001/render-evidence.json) |
| AST-2035 v001 | 문화 활동실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2035/v001/render-evidence.json) |
| AST-2036 v001 | 건축 작업 구역 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2036/v001/render-evidence.json) |
| AST-2037 v002 | 설비 작업 구역 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2037/v002/render-evidence.json) |
| AST-2038 v001 | 환경 조사 지점 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2038/v001/render-evidence.json) |
| AST-2039 v002 | 관측 지점 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2039/v002/render-evidence.json) |
| AST-2040 v001 | 재배지 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2040/v001/render-evidence.json) |
| AST-2041 v001 | 온실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2041/v001/render-evidence.json) |
| AST-2042 v001 | 축사 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2042/v001/render-evidence.json) |
| AST-2043 v002 | 동물 관리실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2043/v002/render-evidence.json) |
| AST-2044 v001 | 선박 갑판 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2044/v001/render-evidence.json) |
| AST-2045 v002 | 조타실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2045/v002/render-evidence.json) |
| AST-2046 v001 | 부두 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2046/v001/render-evidence.json) |
| AST-2047 v001 | 체육관 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2047/v001/render-evidence.json) |
| AST-2048 v001 | 운동 지도실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2048/v001/render-evidence.json) |
| AST-2049 v001 | 경기 구역 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2049/v001/render-evidence.json) |
| AST-2050 v002 | 수사실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2050/v002/render-evidence.json) |
| AST-2051 v002 | 증거 분석실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2051/v002/render-evidence.json) |
| AST-2052 v001 | 법정 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2052/v001/render-evidence.json) |
| AST-2053 v001 | 물류 창고 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2053/v001/render-evidence.json) |
| AST-2054 v002 | 운송 조종 공간 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2054/v002/render-evidence.json) |
| AST-2055 v001 | 운송 거점 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2055/v001/render-evidence.json) |
| AST-2056 v002 | 금융 창구 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2056/v002/render-evidence.json) |
| AST-2057 v001 | 금융 상담실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2057/v001/render-evidence.json) |
| AST-2058 v001 | 가정 수리 공간 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2058/v001/render-evidence.json) |
| AST-2059 v001 | 방문 학습 공간 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2059/v001/render-evidence.json) |
| AST-2060 v001 | 서버실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2060/v001/render-evidence.json) |
| AST-2061 v002 | 관제실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2061/v002/render-evidence.json) |
| AST-2062 v001 | 거실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2062/v001/render-evidence.json) |
| AST-2063 v002 | 주택 관리 공간 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2063/v002/render-evidence.json) |
| AST-2064 v001 | 기독교(개신교) 예배실 — 목사 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2064/v001/render-evidence.json) |
| AST-2065 v002 | 군 행정실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2065/v002/render-evidence.json) |
| AST-2066 v001 | 생활관 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2066/v001/render-evidence.json) |
| AST-2067 v001 | 장비 관리실 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2067/v001/render-evidence.json) |
| AST-2068 v001 | 출장 업무 공간 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2068/v001/render-evidence.json) |
| AST-2069 v001 | 안내 집결 지점 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2069/v001/render-evidence.json) |
| AST-2070 v001 | 불교 법당 — 스님 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2070/v001/render-evidence.json) |
| AST-2071 v001 | 천주교 성당 — 신부님 | diorama | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-2071/v001/render-evidence.json) |
| AST-1010 v001 | 테이블 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1010/v001/render-evidence.json) |
| AST-1011 v001 | 고정형 의자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1011/v001/render-evidence.json) |
| AST-1012 v001 | 노트북 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1012/v001/render-evidence.json) |
| AST-1013 v001 | 이동식 화이트보드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1013/v001/render-evidence.json) |
| AST-1014 v001 | 메모 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1014/v001/render-evidence.json) |
| AST-1015 v001 | 빈백 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1015/v001/render-evidence.json) |
| AST-1016 v001 | 운반 카트 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1016/v001/render-evidence.json) |
| AST-1017 v001 | PC 본체 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1017/v001/render-evidence.json) |
| AST-1019 v001 | 유선전화 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1019/v001/render-evidence.json) |
| AST-1020 v001 | 결재 도장 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1020/v001/render-evidence.json) |
| AST-1021 v001 | 인주 패드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1021/v001/render-evidence.json) |
| AST-1022 v001 | 서류철 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1022/v001/render-evidence.json) |
| AST-1023 v001 | 서비스 카운터 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1023/v001/render-evidence.json) |
| AST-1024 v001 | 번호표 발급기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1024/v001/render-evidence.json) |
| AST-1025 v001 | 연결 대기석 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1025/v001/render-evidence.json) |
| AST-1026 v001 | 안내 책자 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1026/v001/render-evidence.json) |
| AST-1027 v001 | 서류 파일 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1027/v001/render-evidence.json) |
| AST-1028 v001 | 선반 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1028/v001/render-evidence.json) |
| AST-1029 v001 | 천칭 장식 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1029/v001/render-evidence.json) |
| AST-1030 v001 | 녹색 램프 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1030/v001/render-evidence.json) |
| AST-1031 v001 | 실험·분석대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1031/v001/render-evidence.json) |
| AST-1032 v001 | 시험관대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1032/v001/render-evidence.json) |
| AST-1033 v001 | 비커 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1033/v001/render-evidence.json) |
| AST-1034 v001 | 피펫 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1034/v001/render-evidence.json) |
| AST-1035 v001 | 소형 저울 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1035/v001/render-evidence.json) |
| AST-1036 v001 | 세척대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1036/v001/render-evidence.json) |
| AST-1037 v001 | 장비함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1037/v001/render-evidence.json) |
| AST-1038 v001 | 분석 장비 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1038/v001/render-evidence.json) |
| AST-1039 v001 | 현미경 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1039/v001/render-evidence.json) |
| AST-1040 v001 | 부품 트레이 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1040/v001/render-evidence.json) |
| AST-1041 v001 | 진찰·처치 침대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1041/v001/render-evidence.json) |
| AST-1042 v001 | 의료 모니터 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1042/v001/render-evidence.json) |
| AST-1043 v001 | 작업등 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1043/v001/render-evidence.json) |
| AST-1044 v001 | 생활 침대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1044/v001/render-evidence.json) |
| AST-1045 v001 | 침대 옆 탁자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1045/v001/render-evidence.json) |
| AST-1046 v001 | 보호자 의자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1046/v001/render-evidence.json) |
| AST-1047 v001 | 이동식 식탁 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1047/v001/render-evidence.json) |
| AST-1048 v001 | 호출 장치 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1048/v001/render-evidence.json) |
| AST-1049 v001 | 서류 트레이 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1049/v001/render-evidence.json) |
| AST-1050 v001 | 학생 책상 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1050/v001/render-evidence.json) |
| AST-1051 v001 | 교탁 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1051/v001/render-evidence.json) |
| AST-1052 v001 | 독립형 칠판 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1052/v001/render-evidence.json) |
| AST-1053 v001 | 교재 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1053/v001/render-evidence.json) |
| AST-1054 v001 | 사물함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1054/v001/render-evidence.json) |
| AST-1055 v001 | 작업대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1055/v001/render-evidence.json) |
| AST-1056 v001 | 스툴 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1056/v001/render-evidence.json) |
| AST-1057 v001 | 교육용 조립 키트 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1057/v001/render-evidence.json) |
| AST-1058 v001 | 보관 상자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1058/v001/render-evidence.json) |
| AST-1059 v001 | 강연대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1059/v001/render-evidence.json) |
| AST-1060 v001 | 발표 화면 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1060/v001/render-evidence.json) |
| AST-1061 v001 | 작은 AV 장치 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1061/v001/render-evidence.json) |
| AST-1062 v001 | 편안한 의자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1062/v001/render-evidence.json) |
| AST-1063 v001 | 티슈 상자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1063/v001/render-evidence.json) |
| AST-1064 v001 | 상담 노트 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1064/v001/render-evidence.json) |
| AST-1066 v001 | 활동 교구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1066/v001/render-evidence.json) |
| AST-1067 v001 | 러그·바닥 매트 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1067/v001/render-evidence.json) |
| AST-1068 v001 | 이동 보조 의자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1068/v001/render-evidence.json) |
| AST-1069 v001 | 휠체어 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1069/v001/render-evidence.json) |
| AST-1070 v001 | 보조 손잡이 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1070/v001/render-evidence.json) |
| AST-1071 v001 | 소형 생산 기계 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1071/v001/render-evidence.json) |
| AST-1072 v001 | 짧은 컨베이어 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1072/v001/render-evidence.json) |
| AST-1073 v001 | 투입함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1073/v001/render-evidence.json) |
| AST-1074 v001 | 완성품 상자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1074/v001/render-evidence.json) |
| AST-1075 v001 | 제어 패널 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1075/v001/render-evidence.json) |
| AST-1076 v001 | 안전 가드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1076/v001/render-evidence.json) |
| AST-1077 v001 | 공구 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1077/v001/render-evidence.json) |
| AST-1078 v001 | 조립 중인 단순 제품 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1078/v001/render-evidence.json) |
| AST-1079 v001 | 바이스 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1079/v001/render-evidence.json) |
| AST-1080 v001 | 공구함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1080/v001/render-evidence.json) |
| AST-1081 v001 | 열린 기계 케이스 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1081/v001/render-evidence.json) |
| AST-1082 v001 | 단순 포장 상품 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1082/v001/render-evidence.json) |
| AST-1083 v001 | POS 기기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1083/v001/render-evidence.json) |
| AST-1084 v001 | 바구니 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1084/v001/render-evidence.json) |
| AST-1085 v001 | 미용 의자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1085/v001/render-evidence.json) |
| AST-1086 v001 | 독립형 거울 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1086/v001/render-evidence.json) |
| AST-1087 v001 | 세발대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1087/v001/render-evidence.json) |
| AST-1088 v001 | 조리대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1088/v001/render-evidence.json) |
| AST-1089 v001 | 가열 기구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1089/v001/render-evidence.json) |
| AST-1090 v001 | 냉장고 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1090/v001/render-evidence.json) |
| AST-1091 v001 | 조리도구 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1091/v001/render-evidence.json) |
| AST-1092 v001 | 접시 선반 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1092/v001/render-evidence.json) |
| AST-1093 v001 | 반죽 작업대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1093/v001/render-evidence.json) |
| AST-1094 v001 | 믹서 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1094/v001/render-evidence.json) |
| AST-1095 v001 | 오븐 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1095/v001/render-evidence.json) |
| AST-1096 v001 | 베이킹 트레이 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1096/v001/render-evidence.json) |
| AST-1097 v001 | 식힘 선반 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1097/v001/render-evidence.json) |
| AST-1098 v001 | 식기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1098/v001/render-evidence.json) |
| AST-1099 v001 | 배식 보조대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1099/v001/render-evidence.json) |
| AST-1100 v001 | 메뉴 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1100/v001/render-evidence.json) |
| AST-1101 v001 | 펜 태블릿 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1101/v001/render-evidence.json) |
| AST-1102 v001 | 시안 보드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1102/v001/render-evidence.json) |
| AST-1103 v001 | 재료 샘플 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1103/v001/render-evidence.json) |
| AST-1104 v001 | 이젤 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1104/v001/render-evidence.json) |
| AST-1105 v001 | 빈 캔버스 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1105/v001/render-evidence.json) |
| AST-1107 v001 | 팔레트 도구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1107/v001/render-evidence.json) |
| AST-1108 v001 | 손공구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1108/v001/render-evidence.json) |
| AST-1109 v001 | 카메라 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1109/v001/render-evidence.json) |
| AST-1110 v001 | 삼각대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1110/v001/render-evidence.json) |
| AST-1111 v001 | 조명 스탠드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1111/v001/render-evidence.json) |
| AST-1112 v001 | 작은 제품 촬영대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1112/v001/render-evidence.json) |
| AST-1113 v001 | 반사판 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1113/v001/render-evidence.json) |
| AST-1114 v001 | 보관 케이스 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1114/v001/render-evidence.json) |
| AST-1115 v001 | 방송 테이블 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1115/v001/render-evidence.json) |
| AST-1116 v001 | 마이크 암 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1116/v001/render-evidence.json) |
| AST-1117 v001 | 헤드폰 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1117/v001/render-evidence.json) |
| AST-1118 v001 | 소형 오디오 콘솔 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1118/v001/render-evidence.json) |
| AST-1119 v001 | 조명 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1119/v001/render-evidence.json) |
| AST-1120 v001 | 스피커 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1120/v001/render-evidence.json) |
| AST-1121 v001 | 미디어 보관함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1121/v001/render-evidence.json) |
| AST-1122 v001 | 낮은 무대판 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1122/v001/render-evidence.json) |
| AST-1123 v001 | 마이크 스탠드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1123/v001/render-evidence.json) |
| AST-1124 v001 | 전시대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1124/v001/render-evidence.json) |
| AST-1125 v001 | 추상 조형물 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1125/v001/render-evidence.json) |
| AST-1126 v001 | 독립형 액자 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1126/v001/render-evidence.json) |
| AST-1127 v001 | 벤치 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1127/v001/render-evidence.json) |
| AST-1128 v001 | 전시 조명 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1128/v001/render-evidence.json) |
| AST-1129 v001 | 미술 교구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1129/v001/render-evidence.json) |
| AST-1130 v001 | 낮은 비계 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1130/v001/render-evidence.json) |
| AST-1131 v001 | 부분 벽돌 구조 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1131/v001/render-evidence.json) |
| AST-1132 v001 | 자재 더미 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1132/v001/render-evidence.json) |
| AST-1133 v001 | 손수레 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1133/v001/render-evidence.json) |
| AST-1134 v001 | 안전 펜스 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1134/v001/render-evidence.json) |
| AST-1135 v002 | 노출 배관 모형 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1135/v002/render-evidence.json) |
| AST-1136 v001 | 짧은 사다리 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1136/v001/render-evidence.json) |
| AST-1137 v001 | 부품 상자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1137/v001/render-evidence.json) |
| AST-1138 v001 | 제어함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1138/v001/render-evidence.json) |
| AST-1139 v001 | 낮은 지형 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1139/v001/render-evidence.json) |
| AST-1140 v001 | 시료 용기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1140/v001/render-evidence.json) |
| AST-1141 v001 | 휴대 측정기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1141/v001/render-evidence.json) |
| AST-1143 v001 | 단순 식생 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1143/v001/render-evidence.json) |
| AST-1144 v001 | 삼각대 센서 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1144/v001/render-evidence.json) |
| AST-1145 v001 | 소형 관측 장치 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1145/v001/render-evidence.json) |
| AST-1146 v001 | 데이터 기록 기기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1146/v001/render-evidence.json) |
| AST-1147 v001 | 작은 재배 베드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1147/v001/render-evidence.json) |
| AST-1148 v001 | 농작물 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1148/v001/render-evidence.json) |
| AST-1149 v001 | 물뿌리개 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1149/v001/render-evidence.json) |
| AST-1150 v001 | 농기구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1150/v001/render-evidence.json) |
| AST-1151 v001 | 수확 상자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1151/v001/render-evidence.json) |
| AST-1152 v001 | 관수 관 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1152/v001/render-evidence.json) |
| AST-1153 v001 | 재배 테이블 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1153/v001/render-evidence.json) |
| AST-1154 v001 | 모종 트레이 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1154/v001/render-evidence.json) |
| AST-1155 v001 | 관수 설비 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1155/v001/render-evidence.json) |
| AST-1156 v001 | 환경 센서 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1156/v001/render-evidence.json) |
| AST-1157 v001 | 낮은 열린 구조 프레임 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1157/v001/render-evidence.json) |
| AST-1158 v001 | 낮은 우리 칸 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1158/v001/render-evidence.json) |
| AST-1159 v001 | 급이통 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1159/v001/render-evidence.json) |
| AST-1160 v001 | 물통 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1160/v001/render-evidence.json) |
| AST-1161 v001 | 깔짚 구역 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1161/v001/render-evidence.json) |
| AST-1162 v001 | 사료 통 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1162/v001/render-evidence.json) |
| AST-1163 v001 | 청소 도구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1163/v001/render-evidence.json) |
| AST-1164 v001 | 운반 케이지 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1164/v001/render-evidence.json) |
| AST-1165 v001 | 먹이 그릇 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1165/v001/render-evidence.json) |
| AST-1166 v001 | 작은 갑판 바닥 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1166/v001/render-evidence.json) |
| AST-1167 v001 | 짧은 난간 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1167/v001/render-evidence.json) |
| AST-1168 v001 | 구명환 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1168/v001/render-evidence.json) |
| AST-1169 v001 | 밧줄 코일 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1169/v001/render-evidence.json) |
| AST-1170 v001 | 계류 장치 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1170/v001/render-evidence.json) |
| AST-1171 v001 | 조타 장치 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1171/v001/render-evidence.json) |
| AST-1172 v001 | 계기 콘솔 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1172/v001/render-evidence.json) |
| AST-1173 v001 | 운항 좌석 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1173/v001/render-evidence.json) |
| AST-1174 v001 | 항해 화면 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1174/v001/render-evidence.json) |
| AST-1175 v001 | 통신 기기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1175/v001/render-evidence.json) |
| AST-1176 v001 | 부두 바닥 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1176/v001/render-evidence.json) |
| AST-1177 v001 | 작은 수면 가장자리 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1177/v001/render-evidence.json) |
| AST-1178 v001 | 계류 기둥 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1178/v001/render-evidence.json) |
| AST-1179 v001 | 일반 운동 매트 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1179/v001/render-evidence.json) |
| AST-1180 v001 | 작은 운동 기구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1180/v001/render-evidence.json) |
| AST-1181 v001 | 공 보관대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1181/v001/render-evidence.json) |
| AST-1182 v001 | 물병 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1182/v001/render-evidence.json) |
| AST-1183 v001 | 스트레칭 바 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1183/v001/render-evidence.json) |
| AST-1184 v001 | 낮은 스텝 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1184/v001/render-evidence.json) |
| AST-1185 v001 | 소형 아령 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1185/v001/render-evidence.json) |
| AST-1186 v001 | 자세 확인용 독립 거울 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1186/v001/render-evidence.json) |
| AST-1187 v001 | 짧은 코트 바닥 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1187/v001/render-evidence.json) |
| AST-1188 v001 | 작은 골대 한 쌍 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1188/v001/render-evidence.json) |
| AST-1189 v001 | 공 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1189/v001/render-evidence.json) |
| AST-1190 v001 | 빈 점수판 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1190/v001/render-evidence.json) |
| AST-1191 v001 | 관계 보드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1191/v001/render-evidence.json) |
| AST-1192 v001 | 밀봉 시료 상자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1192/v001/render-evidence.json) |
| AST-1193 v001 | 잠금 보관함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1193/v001/render-evidence.json) |
| AST-1194 v001 | 작은 판사 단상 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1194/v001/render-evidence.json) |
| AST-1195 v001 | 진술대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1195/v001/render-evidence.json) |
| AST-1196 v001 | 당사자 책상 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1196/v001/render-evidence.json) |
| AST-1197 v001 | 방청 의자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1197/v001/render-evidence.json) |
| AST-1198 v001 | 문서함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1198/v001/render-evidence.json) |
| AST-1199 v001 | 적재 선반 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1199/v001/render-evidence.json) |
| AST-1200 v001 | 팔레트 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1200/v001/render-evidence.json) |
| AST-1201 v001 | 수동 운반차 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1201/v001/render-evidence.json) |
| AST-1202 v001 | 운전석 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1202/v001/render-evidence.json) |
| AST-1203 v001 | 조작 콘솔 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1203/v001/render-evidence.json) |
| AST-1204 v001 | 보조 좌석 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1204/v001/render-evidence.json) |
| AST-1205 v001 | 안내판 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1205/v001/render-evidence.json) |
| AST-1206 v001 | 작은 계산기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1206/v001/render-evidence.json) |
| AST-1207 v001 | 간단한 가전제품 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1207/v001/render-evidence.json) |
| AST-1208 v001 | 공구 가방 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1208/v001/render-evidence.json) |
| AST-1209 v001 | 필기구 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1209/v001/render-evidence.json) |
| AST-1210 v001 | 서버 랙 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1210/v001/render-evidence.json) |
| AST-1211 v001 | 케이블 트레이 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1211/v001/render-evidence.json) |
| AST-1212 v001 | 관리 단말 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1212/v001/render-evidence.json) |
| AST-1213 v001 | 관제 콘솔 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1213/v001/render-evidence.json) |
| AST-1214 v001 | 보조 단말 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1214/v001/render-evidence.json) |
| AST-1215 v001 | 소파 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1215/v001/render-evidence.json) |
| AST-1216 v001 | 독립형 TV | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1216/v001/render-evidence.json) |
| AST-1217 v001 | 설비함 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1217/v001/render-evidence.json) |
| AST-1218 v001 | 점검 보드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1218/v001/render-evidence.json) |
| AST-1219 v001 | 일정 보드 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1219/v001/render-evidence.json) |
| AST-1220 v001 | 신발 정리대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1220/v001/render-evidence.json) |
| AST-1221 v001 | 여행 가방 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1221/v001/render-evidence.json) |
| AST-1222 v001 | 휴대 전화 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1222/v001/render-evidence.json) |
| AST-1223 v001 | 문서 파우치 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1223/v001/render-evidence.json) |
| AST-1224 v001 | 지도 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1224/v001/render-evidence.json) |
| AST-1225 v001 | 낮은 경계 기둥 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1225/v001/render-evidence.json) |
| AST-1244 v001 | 설교 강대상 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1244/v001/render-evidence.json) |
| AST-1245 v001 | 펼친 성경 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1245/v001/render-evidence.json) |
| AST-1246 v001 | 단순한 십자가 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1246/v001/render-evidence.json) |
| AST-1247 v001 | 예배용 긴 의자 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1247/v001/render-evidence.json) |
| AST-1248 v001 | 찬송가 책 거치대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1248/v001/render-evidence.json) |
| AST-1249 v001 | 작은 건반 악기 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1249/v001/render-evidence.json) |
| AST-1250 v001 | 낮은 불단 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1250/v001/render-evidence.json) |
| AST-1251 v001 | 단순화한 불상 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1251/v001/render-evidence.json) |
| AST-1252 v001 | 방석 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1252/v001/render-evidence.json) |
| AST-1253 v001 | 낮은 경전 독서대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1253/v001/render-evidence.json) |
| AST-1254 v001 | 목탁 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1254/v001/render-evidence.json) |
| AST-1255 v001 | 향로 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1255/v001/render-evidence.json) |
| AST-1256 v001 | 작은 연꽃 장식 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1256/v001/render-evidence.json) |
| AST-1257 v001 | 미사 제대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1257/v001/render-evidence.json) |
| AST-1258 v001 | 독서대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1258/v001/render-evidence.json) |
| AST-1259 v001 | 십자고상 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1259/v001/render-evidence.json) |
| AST-1260 v001 | 성작 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1260/v001/render-evidence.json) |
| AST-1261 v001 | 전례서 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1261/v001/render-evidence.json) |
| AST-1262 v001 | 촛대 | prop | [방향별 렌더](../../../docs/machine/evidence/workplaces-model-review-v001/views/AST-1262/v001/render-evidence.json) |

## 71개 공간의 현재 고정 참조

| 공간 | prompt | panorama | 조립 모델 |
|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | AST-020 v004 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | AST-2002 v001 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | AST-2003 v002 |
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | AST-2004 v002 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | AST-2005 v001 |
| 실험실 | PRM-006 v001 | PAN-006 v001 | AST-2006 v001 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | AST-2007 v002 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | AST-2008 v002 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | AST-2009 v001 |
| 병실 | PRM-010 v001 | PAN-010 v001 | AST-2010 v002 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | AST-2011 v002 |
| 교실 | PRM-012 v001 | PAN-012 v001 | AST-2012 v001 |
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | AST-2013 v001 |
| 강의실 | PRM-014 v001 | PAN-014 v001 | AST-2014 v002 |
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | AST-2015 v001 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | AST-2016 v001 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | AST-2017 v001 |
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | AST-2018 v001 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | AST-2019 v001 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | AST-2020 v001 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | AST-2021 v001 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | AST-2022 v002 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | AST-2023 v001 |
| 주방 | PRM-024 v001 | PAN-024 v001 | AST-2024 v001 |
| 제과실 | PRM-025 v001 | PAN-025 v001 | AST-2025 v001 |
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | AST-2026 v001 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | AST-2027 v002 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | AST-2028 v002 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | AST-2029 v001 |
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | AST-2030 v001 |
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | AST-2031 v002 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | AST-2032 v003 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | AST-2033 v001 |
| 전시실 | PRM-034 v001 | PAN-034 v001 | AST-2034 v001 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | AST-2035 v001 |
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | AST-2036 v001 |
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | AST-2037 v002 |
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | AST-2038 v001 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | AST-2039 v002 |
| 재배지 | PRM-040 v001 | PAN-040 v001 | AST-2040 v001 |
| 온실 | PRM-041 v001 | PAN-041 v001 | AST-2041 v001 |
| 축사 | PRM-042 v001 | PAN-042 v001 | AST-2042 v001 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | AST-2043 v002 |
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | AST-2044 v001 |
| 조타실 | PRM-045 v001 | PAN-045 v001 | AST-2045 v002 |
| 부두 | PRM-046 v001 | PAN-046 v001 | AST-2046 v001 |
| 체육관 | PRM-047 v001 | PAN-047 v001 | AST-2047 v001 |
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | AST-2048 v001 |
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | AST-2049 v001 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | AST-2050 v002 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | AST-2051 v002 |
| 법정 | PRM-052 v001 | PAN-052 v001 | AST-2052 v001 |
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | AST-2053 v001 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | AST-2054 v002 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | AST-2055 v001 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | AST-2056 v002 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | AST-2057 v001 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | AST-2058 v001 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | AST-2059 v001 |
| 서버실 | PRM-060 v001 | PAN-060 v001 | AST-2060 v001 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | AST-2061 v002 |
| 거실 | PRM-062 v001 | PAN-062 v001 | AST-2062 v001 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | AST-2063 v002 |
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | AST-2064 v001 |
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | AST-2070 v001 |
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | AST-2071 v001 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | AST-2065 v002 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | AST-2066 v001 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | AST-2067 v001 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | AST-2068 v001 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | AST-2069 v001 |

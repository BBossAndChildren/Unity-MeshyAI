# 전체 공간 공통·전용 후보 명세 v004

고정262개 후보와71개 공간을 보존한 제작 결과 조회 개정이다. 원본 v003의 전체 기획 후보에 실제 제작 과정에서 추가한 지원·배경 소품 연결을 합쳤다. 기존 원문 key_props에 없던 지원 추가를 원문 기획으로 기록하지 않는다.

기계용 기준: [workplace-asset-candidates-v004.json](../../machine/catalog/workplace-asset-candidates-v004.json). [보존된 v003](workplace-common-assets-v003.md)와 [원본 catalog](../../machine/catalog/workplace-asset-candidates-v003.json)는 변경하지 않았다.

| 집계 | 기준 v003 | 제작 지원 연결 포함 v004 |
|---|---:|---:|
| 공간 |71|71|
| 후보 정의 |262|262|
| 공통 후보 |55|68|
| 전용 후보 |189|180|
| 공간 후보 없는 inventory-only |18|14|
| 최초 기존 모델 참조 후보 |17|17(기준 당시 수치 보존)|
| 추가 후보-공간 연결 |0|92|

공통/전용은 서로 다른 고정 prompt_id/version의 연결 수로 계산한다. 후보 수·모델 수·배치 수·제작 완료·실행 검증을 혼동하지 않는다. 현재 모델 연결과 실제 사용은 아래 고정 에셋·canonical 원장 참조로 조회하며 후보의 planning_only·수량null은 실제 배치 수량을 복제하지 않는 계획 메타데이터다.

실제 수량·변환·장면·프리팹·빌드 포함·실행 근거의 원장은 asset-usages.json과 scene-assemblies.json이다. 이 문서의 표는 조회 결과이며 독립 사용 원장이 아니다. v005 최종 실행 검수 완료 전으로, 실제 준비된 범위와 미검증을 따로 표시한다. 552개 직업 시나리오 전체를 확정하지 않는다.

## 공간별 전체 후보

| 공간 | prompt | panorama | 전체 필요 후보 | 제작 지원 추가 |
|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | CND-001, CND-002, CND-003, CND-004, CND-005, CND-006, CND-007, CND-008, CND-009, CND-018, CND-065, CND-106, CND-142, CND-226, CND-229, CND-233, CND-234 | CND-018, CND-065, CND-106, CND-142, CND-226, CND-229, CND-233, CND-234 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | CND-001, CND-002, CND-010, CND-011, CND-012, CND-013, CND-014, CND-015, CND-016, CND-053, CND-065, CND-067, CND-106 | CND-053, CND-065, CND-067, CND-106 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | CND-001, CND-002, CND-003, CND-004, CND-005, CND-006, CND-016, CND-017, CND-018, CND-019, CND-020, CND-021, CND-022, CND-008, CND-009, CND-065 | CND-008, CND-009, CND-065 |
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | CND-001, CND-002, CND-003, CND-005, CND-023, CND-024, CND-025, CND-026, CND-065 | CND-065 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | CND-001, CND-002, CND-004, CND-010, CND-011, CND-027, CND-028, CND-029, CND-030, CND-053, CND-065 | CND-053, CND-065 |
| 실험실 | PRM-006 v001 | PAN-006 v001 | CND-001, CND-002, CND-031, CND-032, CND-033, CND-034, CND-035, CND-036, CND-037, CND-016, CND-056 | CND-016, CND-056 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | CND-001, CND-002, CND-004, CND-005, CND-037, CND-038, CND-039, CND-040, CND-003, CND-031 | CND-003, CND-031 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | CND-001, CND-002, CND-003, CND-004, CND-011, CND-016, CND-041, CND-042, CND-005, CND-037, CND-043 | CND-005, CND-037, CND-043 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | CND-001, CND-002, CND-009, CND-016, CND-036, CND-040, CND-041, CND-043, CND-037 | CND-037 |
| 병실 | PRM-010 v001 | PAN-010 v001 | CND-001, CND-002, CND-042, CND-044, CND-045, CND-046, CND-047, CND-048, CND-016 | CND-016 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | CND-001, CND-002, CND-003, CND-005, CND-006, CND-017, CND-018, CND-023, CND-024, CND-025, CND-049, CND-027, CND-065 | CND-027, CND-065 |
| 교실 | PRM-012 v001 | PAN-012 v001 | CND-001, CND-002, CND-011, CND-050, CND-051, CND-052, CND-053, CND-054 | 없음 |
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | CND-001, CND-002, CND-040, CND-055, CND-056, CND-057, CND-058, CND-028 | CND-028 |
| 강의실 | PRM-014 v001 | PAN-014 v001 | CND-001, CND-002, CND-010, CND-011, CND-059, CND-060, CND-061, CND-016 | CND-016 |
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | CND-001, CND-002, CND-010, CND-028, CND-062, CND-063, CND-064, CND-065, CND-067 | CND-067 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | CND-001, CND-002, CND-009, CND-010, CND-011, CND-013, CND-066, CND-067, CND-028 | CND-028 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | CND-001, CND-002, CND-009, CND-044, CND-045, CND-068, CND-069, CND-070, CND-067 | CND-067 |
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | CND-001, CND-002, CND-071, CND-072, CND-073, CND-074, CND-075, CND-076 | 없음 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | CND-001, CND-002, CND-028, CND-040, CND-055, CND-056, CND-077, CND-078, CND-016, CND-079, CND-080 | CND-016, CND-079, CND-080 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | CND-001, CND-002, CND-040, CND-043, CND-055, CND-079, CND-080, CND-081, CND-016, CND-077 | CND-016, CND-077 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | CND-001, CND-002, CND-009, CND-023, CND-028, CND-082, CND-083, CND-084, CND-058 | CND-058 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | CND-001, CND-002, CND-003, CND-005, CND-006, CND-009, CND-011, CND-017, CND-018, CND-023, CND-049, CND-027 | CND-027 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | CND-001, CND-002, CND-011, CND-016, CND-028, CND-085, CND-086, CND-087, CND-056 | CND-056 |
| 주방 | PRM-024 v001 | PAN-024 v001 | CND-001, CND-002, CND-036, CND-088, CND-089, CND-090, CND-091, CND-092, CND-098 | CND-098 |
| 제과실 | PRM-025 v001 | PAN-025 v001 | CND-001, CND-002, CND-058, CND-093, CND-094, CND-095, CND-096, CND-097, CND-028, CND-055 | CND-028, CND-055 |
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | CND-001, CND-002, CND-010, CND-011, CND-065, CND-098, CND-099, CND-100 | 없음 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | CND-001, CND-002, CND-004, CND-005, CND-049, CND-101, CND-102, CND-103, CND-003, CND-028, CND-055 | CND-003, CND-028, CND-055 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | CND-001, CND-002, CND-010, CND-028, CND-104, CND-105, CND-106, CND-107, CND-055, CND-056, CND-065 | CND-055, CND-056, CND-065 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | CND-001, CND-002, CND-028, CND-043, CND-055, CND-058, CND-079, CND-108, CND-016 | CND-016 |
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | CND-001, CND-002, CND-109, CND-110, CND-111, CND-112, CND-113, CND-114, CND-082 | CND-082 |
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | CND-001, CND-002, CND-109, CND-115, CND-116, CND-117, CND-118, CND-119, CND-004, CND-110 | CND-004, CND-110 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | CND-001, CND-002, CND-004, CND-005, CND-006, CND-117, CND-120, CND-121, CND-003, CND-018 | CND-003, CND-018 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | CND-001, CND-002, CND-011, CND-111, CND-120, CND-122, CND-123, CND-128 | CND-128 |
| 전시실 | PRM-034 v001 | PAN-034 v001 | CND-001, CND-002, CND-124, CND-125, CND-126, CND-127, CND-128 | 없음 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | CND-001, CND-002, CND-010, CND-011, CND-013, CND-028, CND-129 | 없음 |
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | CND-001, CND-002, CND-080, CND-130, CND-131, CND-132, CND-133, CND-134 | 없음 |
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | CND-001, CND-002, CND-055, CND-080, CND-135, CND-136, CND-137, CND-138, CND-077 | CND-077 |
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | CND-001, CND-002, CND-055, CND-139, CND-140, CND-141, CND-142, CND-143, CND-058 | CND-058 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | CND-001, CND-002, CND-114, CND-139, CND-144, CND-145, CND-146, CND-055, CND-127, CND-143 | CND-055, CND-127, CND-143 |
| 재배지 | PRM-040 v001 | PAN-040 v001 | CND-001, CND-002, CND-147, CND-148, CND-149, CND-150, CND-151, CND-152 | 없음 |
| 온실 | PRM-041 v001 | PAN-041 v001 | CND-001, CND-002, CND-016, CND-153, CND-154, CND-155, CND-156, CND-157 | 없음 |
| 축사 | PRM-042 v001 | PAN-042 v001 | CND-001, CND-002, CND-158, CND-159, CND-160, CND-161, CND-162, CND-163 | 없음 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | CND-001, CND-002, CND-028, CND-036, CND-055, CND-067, CND-164, CND-165, CND-040 | CND-040 |
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | CND-001, CND-002, CND-009, CND-166, CND-167, CND-168, CND-169, CND-170, CND-058 | CND-058 |
| 조타실 | PRM-045 v001 | PAN-045 v001 | CND-001, CND-002, CND-171, CND-172, CND-173, CND-174, CND-175, CND-045 | CND-045 |
| 부두 | PRM-046 v001 | PAN-046 v001 | CND-001, CND-002, CND-058, CND-133, CND-168, CND-176, CND-177, CND-178, CND-169 | CND-169 |
| 체육관 | PRM-047 v001 | PAN-047 v001 | CND-001, CND-002, CND-127, CND-179, CND-180, CND-181, CND-182 | 없음 |
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | CND-001, CND-002, CND-179, CND-183, CND-184, CND-185, CND-186, CND-182 | CND-182 |
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | CND-001, CND-002, CND-127, CND-187, CND-188, CND-189, CND-190 | 없음 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | CND-001, CND-002, CND-004, CND-005, CND-006, CND-009, CND-011, CND-017, CND-018, CND-049, CND-191, CND-003, CND-027, CND-028 | CND-003, CND-027, CND-028 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | CND-001, CND-002, CND-005, CND-006, CND-017, CND-018, CND-031, CND-039, CND-040, CND-192, CND-193, CND-016 | CND-016 |
| 법정 | PRM-052 v001 | PAN-052 v001 | CND-001, CND-002, CND-194, CND-195, CND-196, CND-197, CND-198 | 없음 |
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | CND-001, CND-002, CND-055, CND-058, CND-199, CND-200, CND-201 | 없음 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | CND-001, CND-002, CND-005, CND-175, CND-202, CND-203, CND-204, CND-045, CND-174 | CND-045, CND-174 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | CND-001, CND-002, CND-016, CND-023, CND-028, CND-058, CND-127, CND-205, CND-025 | CND-025 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | CND-001, CND-002, CND-005, CND-006, CND-011, CND-017, CND-018, CND-023, CND-024, CND-025, CND-049, CND-003 | CND-003 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | CND-001, CND-002, CND-009, CND-010, CND-011, CND-012, CND-027, CND-206 | 없음 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | CND-001, CND-002, CND-009, CND-040, CND-067, CND-207, CND-208, CND-016, CND-108 | CND-016, CND-108 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | CND-001, CND-002, CND-004, CND-011, CND-028, CND-053, CND-142, CND-209 | 없음 |
| 서버실 | PRM-060 v001 | PAN-060 v001 | CND-001, CND-002, CND-016, CND-037, CND-210, CND-211, CND-212, CND-114 | CND-114 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | CND-001, CND-002, CND-003, CND-005, CND-175, CND-213, CND-214, CND-045 | CND-045 |
| 거실 | PRM-062 v001 | PAN-062 v001 | CND-001, CND-002, CND-009, CND-010, CND-065, CND-067, CND-215, CND-216 | 없음 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | CND-001, CND-002, CND-004, CND-009, CND-028, CND-163, CND-217, CND-218, CND-005, CND-055, CND-080 | CND-005, CND-055, CND-080 |
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | CND-001, CND-002, CND-244, CND-245, CND-246, CND-247, CND-248, CND-249 | 없음 |
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | CND-001, CND-002, CND-250, CND-251, CND-252, CND-253, CND-254, CND-255, CND-256 | 없음 |
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | CND-001, CND-002, CND-247, CND-257, CND-258, CND-259, CND-260, CND-261, CND-262, CND-124 | CND-124 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | CND-001, CND-002, CND-004, CND-005, CND-006, CND-009, CND-011, CND-017, CND-018, CND-175, CND-219, CND-003, CND-028 | CND-003, CND-028 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | CND-001, CND-002, CND-010, CND-011, CND-044, CND-054, CND-220, CND-045, CND-221 | CND-045, CND-221 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | CND-001, CND-002, CND-016, CND-028, CND-055, CND-080, CND-114, CND-077 | CND-077 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | CND-001, CND-002, CND-010, CND-011, CND-012, CND-221, CND-222, CND-223, CND-142 | CND-142 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | CND-001, CND-002, CND-127, CND-205, CND-221, CND-224, CND-225, CND-142, CND-143 | CND-142, CND-143 |

<a id="cnd-001"></a>
## CND-001 — 둥근 바닥판

분류: common; 기준 공간 연결 71개 → 현재 71개. 모델 제작 상태와 별개인 후보 명세다.

둥근 바닥판의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-001 v002](../assets/AST-001-v002-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 기준 v003 기획 | 미정 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 교실 | PRM-012 v001 | PAN-012 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 강의실 | PRM-014 v001 | PAN-014 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 전시실 | PRM-034 v001 | PAN-034 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 재배지 | PRM-040 v001 | PAN-040 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 온실 | PRM-041 v001 | PAN-041 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 축사 | PRM-042 v001 | PAN-042 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조타실 | PRM-045 v001 | PAN-045 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 체육관 | PRM-047 v001 | PAN-047 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 법정 | PRM-052 v001 | PAN-052 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서버실 | PRM-060 v001 | PAN-060 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 거실 | PRM-062 v001 | PAN-062 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-012-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-013-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-014-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-018-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-026-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-033-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-034-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-035-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-036-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-040-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-041-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-042-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-045-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-047-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-048-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-049-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-052-workplace` revision 1 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-053-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-057-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-059-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-060-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-061-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-062-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-064-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-067-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-001 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-001-v002-scene` revision 3 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-001-v002-prototype` revision 1 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-001-v002-scene` revision 10 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-001-v002-scene` revision 10 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-001-v002-scene` revision 10 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-001-v002-scene` revision 10 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-012-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-013-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-014-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-033-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-035-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-042-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-048-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-049-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-052-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-053-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-057-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-059-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-060-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-061-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-067-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-001-v002-scene` revision 9 / AST-001 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-001-v002-scene` revision 9 / AST-001 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-002"></a>
## CND-002 — 바닥 표면

분류: common; 기준 공간 연결 71개 → 현재 71개. 모델 제작 상태와 별개인 후보 명세다.

바닥 표면의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-002 v001](../assets/AST-002-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 기준 v003 기획 | 미정 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 교실 | PRM-012 v001 | PAN-012 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 강의실 | PRM-014 v001 | PAN-014 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 전시실 | PRM-034 v001 | PAN-034 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 재배지 | PRM-040 v001 | PAN-040 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 온실 | PRM-041 v001 | PAN-041 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 축사 | PRM-042 v001 | PAN-042 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조타실 | PRM-045 v001 | PAN-045 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 체육관 | PRM-047 v001 | PAN-047 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 법정 | PRM-052 v001 | PAN-052 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서버실 | PRM-060 v001 | PAN-060 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 거실 | PRM-062 v001 | PAN-062 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-012-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-013-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-014-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-018-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-026-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-033-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-034-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-035-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-036-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-040-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-041-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-042-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-045-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-047-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-048-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-049-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-052-workplace` revision 1 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-053-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-057-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-059-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-060-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-061-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-062-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-064-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-067-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-002 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-002-v001-scene` revision 3 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-002-v001-prototype` revision 1 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-002-v001-scene` revision 10 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-002-v001-scene` revision 10 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-002-v001-scene` revision 10 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-002-v001-scene` revision 10 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-012-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-013-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-014-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-033-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-035-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-042-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-048-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-049-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-052-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-053-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-057-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-059-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-060-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-061-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-067-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-002-v001-scene` revision 9 / AST-002 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-002-v001-scene` revision 9 / AST-002 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-003"></a>
## CND-003 — 회전 사무의자

분류: common; 기준 공간 연결 7개 → 현재 13개. 모델 제작 상태와 별개인 후보 명세다.

회전 사무의자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-003 v001](../assets/AST-003-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-061-workplace` revision 4 / AST-003 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-003-v001-scene` revision 3 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-003-v001-prototype` revision 1 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-003-v001-scene` revision 10 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-003-v001-scene` revision 10 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-061-ast-003-v001-scene` revision 9 / AST-003 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-003-v001-scene` revision 9 / AST-003 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-004"></a>
## CND-004 — 업무 책상

분류: common; 기준 공간 연결 11개 → 현재 12개. 모델 제작 상태와 별개인 후보 명세다.

업무 책상의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-004 v001](../assets/AST-004-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-059-workplace` revision 2 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-004 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-004-v001-scene` revision 3 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-004-v001-prototype` revision 1 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-004-v001-scene` revision 10 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-004-v001-scene` revision 10 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-059-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-004-v001-scene` revision 9 / AST-004 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-004-v001-scene` revision 9 / AST-004 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-005"></a>
## CND-005 — 모니터

분류: common; 기준 공간 연결 14개 → 현재 16개. 모델 제작 상태와 별개인 후보 명세다.

모니터의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-005 v001](../assets/AST-005-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 기준 v003 기획 | 미정 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-061-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-005 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-005-v001-scene` revision 3 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-005-v001-prototype` revision 1 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-005-v001-scene` revision 10 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-005-v001-scene` revision 10 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-061-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-005-v001-scene` revision 9 / AST-005 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-005-v001-scene` revision 9 / AST-005 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-006"></a>
## CND-006 — 키보드

분류: common; 기준 공간 연결 9개 → 현재 9개. 모델 제작 상태와 별개인 후보 명세다.

키보드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-006 v001](../assets/AST-006-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-006 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-006 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-006 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-006 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-006 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-006 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-006 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-006 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-006-v001-scene` revision 3 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-006-v001-prototype` revision 1 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-006-v001-scene` revision 10 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-006-v001-scene` revision 9 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-006-v001-scene` revision 9 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-006-v001-scene` revision 9 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-006-v001-scene` revision 9 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-006-v001-scene` revision 9 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-006-v001-scene` revision 9 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-006-v001-scene` revision 9 / AST-006 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-006-v001-scene` revision 9 / AST-006 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-007"></a>
## CND-007 — 낮은 책상 스크린

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 책상 스크린의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-013 v001](../assets/AST-013-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-013 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-013-v001-scene` revision 3 / AST-013 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-013-v001-prototype` revision 1 / AST-013 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-013-v001-scene` revision 9 / AST-013 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-008"></a>
## CND-008 — 복합기

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

복합기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-009 v001](../assets/AST-009-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-009 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-009 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-009-v001-scene` revision 3 / AST-009 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-009-v001-prototype` revision 1 / AST-009 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-009-v001-scene` revision 10 / AST-009 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-009-v001-scene` revision 9 / AST-009 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-009"></a>
## CND-009 — 수납장

분류: common; 기준 공간 연결 13개 → 현재 14개. 모델 제작 상태와 별개인 후보 명세다.

수납장의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-015 v001](../assets/AST-015-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 기준 v003 기획 | 미정 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 거실 | PRM-062 v001 | PAN-062 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-057-workplace` revision 2 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-062-workplace` revision 2 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-015 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-015-v001-scene` revision 3 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-015-v001-prototype` revision 1 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-015-v001-scene` revision 10 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-057-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-015-v001-scene` revision 9 / AST-015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-015-v001-scene` revision 9 / AST-015 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-010"></a>
## CND-010 — 테이블

분류: common; 기준 공간 연결 12개 → 현재 12개. 모델 제작 상태와 별개인 후보 명세다.

테이블의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1010 v001](../assets/AST-1010-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |
| 강의실 | PRM-014 v001 | PAN-014 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 거실 | PRM-062 v001 | PAN-062 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-014-workplace` revision 3 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-026-workplace` revision 2 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-035-workplace` revision 2 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-057-workplace` revision 2 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-062-workplace` revision 2 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-1010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1010-v001-prototype` revision 1 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1010-v001-scene` revision 10 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-1010-v001-scene` revision 10 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-014-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-035-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-057-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-1010-v001-scene` revision 9 / AST-1010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-1010-v001-scene` revision 9 / AST-1010 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-011"></a>
## CND-011 — 고정형 의자

분류: common; 기준 공간 연결 18개 → 현재 18개. 모델 제작 상태와 별개인 후보 명세다.

고정형 의자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1011 v001](../assets/AST-1011-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 교실 | PRM-012 v001 | PAN-012 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 강의실 | PRM-014 v001 | PAN-014 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-012-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-014-workplace` revision 3 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-026-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-033-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-035-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-057-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-059-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-1011 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1011-v001-prototype` revision 1 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1011-v001-scene` revision 10 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-1011-v001-scene` revision 10 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-012-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-014-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-033-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-035-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-057-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-059-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-1011-v001-scene` revision 9 / AST-1011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-1011-v001-scene` revision 9 / AST-1011 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-012"></a>
## CND-012 — 노트북

분류: common; 기준 공간 연결 3개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

노트북의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1012 v001](../assets/AST-1012-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1012 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-057-workplace` revision 2 / AST-1012 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-1012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1012-v001-prototype` revision 1 / AST-1012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1012-v001-scene` revision 10 / AST-1012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-057-ast-1012-v001-scene` revision 9 / AST-1012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-1012-v001-scene` revision 9 / AST-1012 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-013"></a>
## CND-013 — 이동식 화이트보드

분류: common; 기준 공간 연결 3개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

이동식 화이트보드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1013 v002](../assets/AST-1013-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1013 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-1013 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-035-workplace` revision 2 / AST-1013 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1013-v001-prototype` revision 1 / AST-1013 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1013-v001-scene` revision 4 / AST-1013 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-1013-v001-scene` revision 3 / AST-1013 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-035-ast-1013-v001-scene` revision 3 / AST-1013 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1013-v002-prototype` revision 1 / AST-1013 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1013-v002-scene` revision 7 / AST-1013 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-1013-v002-scene` revision 7 / AST-1013 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-035-ast-1013-v002-scene` revision 7 / AST-1013 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-014"></a>
## CND-014 — 메모

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

메모의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1014 v001](../assets/AST-1014-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1014 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1014-v001-prototype` revision 1 / AST-1014 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1014-v001-scene` revision 10 / AST-1014 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-015"></a>
## CND-015 — 빈백

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

빈백의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_or_meshy_review / 기존 형태·스크립트 재사용 및 단순 도형 표현부터 검토하고 자유 곡면이 핵심일 때만 승인된 Meshy 범위 검토.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1015 v001](../assets/AST-1015-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1015-v001-prototype` revision 1 / AST-1015 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1015-v001-scene` revision 10 / AST-1015 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-016"></a>
## CND-016 — 운반 카트

분류: common; 기준 공간 연결 9개 → 현재 17개. 모델 제작 상태와 별개인 후보 명세다.

운반 카트의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 프레임, 적재면, 손잡이, 바퀴
형태·치수 미정 항목: 폭, 높이, 적재 단수, 바퀴 개수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1016 v001](../assets/AST-1016-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 기준 v003 기획 | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 온실 | PRM-041 v001 | PAN-041 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서버실 | PRM-060 v001 | PAN-060 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 강의실 | PRM-014 v001 | PAN-014 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-014-workplace` revision 3 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-041-workplace` revision 2 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-060-workplace` revision 3 / AST-1016 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-067-workplace` revision 3 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1016-v001-prototype` revision 1 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1016-v001-scene` revision 10 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-1016-v001-scene` revision 10 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-014-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-060-ast-1016-v001-scene` revision 9 / AST-1016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-067-ast-1016-v001-scene` revision 9 / AST-1016 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-017"></a>
## CND-017 — PC 본체

분류: common; 기준 공간 연결 7개 → 현재 7개. 모델 제작 상태와 별개인 후보 명세다.

PC 본체의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: PC 본체 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1017 v002](../assets/AST-1017-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-1017 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-1017 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-1017 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-1017 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-1017 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-1017 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-1017 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1017-v001-prototype` revision 1 / AST-1017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-1017-v001-scene` revision 4 / AST-1017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-1017-v001-scene` revision 3 / AST-1017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-1017-v001-scene` revision 3 / AST-1017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-1017-v001-scene` revision 3 / AST-1017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1017-v001-scene` revision 3 / AST-1017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-1017-v001-scene` revision 3 / AST-1017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-1017-v001-scene` revision 3 / AST-1017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1017-v002-prototype` revision 1 / AST-1017 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-1017-v002-scene` revision 7 / AST-1017 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-1017-v002-scene` revision 7 / AST-1017 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-1017-v002-scene` revision 7 / AST-1017 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-1017-v002-scene` revision 7 / AST-1017 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1017-v002-scene` revision 7 / AST-1017 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-1017-v002-scene` revision 7 / AST-1017 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-1017-v002-scene` revision 7 / AST-1017 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-018"></a>
## CND-018 — 마우스

분류: common; 기준 공간 연결 7개 → 현재 9개. 모델 제작 상태와 별개인 후보 명세다.

마우스의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-007 v001](../assets/AST-007-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-007 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-007 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-007 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-007 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-007 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-007 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-007 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-007 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-007-v001-scene` revision 3 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-007-v001-prototype` revision 1 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-007-v001-scene` revision 10 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-007-v001-scene` revision 9 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-007-v001-scene` revision 9 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-007-v001-scene` revision 9 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-007-v001-scene` revision 9 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-007-v001-scene` revision 9 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-007-v001-scene` revision 9 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-007-v001-scene` revision 9 / AST-007 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-007-v001-scene` revision 9 / AST-007 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-019"></a>
## CND-019 — 유선전화

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

유선전화의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 유선전화 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1019 v001](../assets/AST-1019-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-1019 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1019-v001-prototype` revision 1 / AST-1019 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-1019-v001-scene` revision 10 / AST-1019 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-020"></a>
## CND-020 — 결재 도장

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

결재 도장의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 결재 도장 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1020 v001](../assets/AST-1020-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-1020 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1020-v001-prototype` revision 1 / AST-1020 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-1020-v001-scene` revision 10 / AST-1020 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-021"></a>
## CND-021 — 인주 패드

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

인주 패드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 인주 패드 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1021 v001](../assets/AST-1021-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-1021 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1021-v001-prototype` revision 1 / AST-1021 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-1021-v001-scene` revision 10 / AST-1021 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-022"></a>
## CND-022 — 서류철

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

서류철의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1022 v001](../assets/AST-1022-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-1022 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1022-v001-prototype` revision 1 / AST-1022 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-1022-v001-scene` revision 10 / AST-1022 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-023"></a>
## CND-023 — 서비스 카운터

분류: common; 기준 공간 연결 6개 → 현재 6개. 모델 제작 상태와 별개인 후보 명세다.

서비스 카운터의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 서비스 카운터 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1023 v001](../assets/AST-1023-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-1023 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-1023 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-1023 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-1023 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-1023 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-1023 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1023-v001-prototype` revision 1 / AST-1023 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-1023-v001-scene` revision 10 / AST-1023 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-1023-v001-scene` revision 9 / AST-1023 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-1023-v001-scene` revision 9 / AST-1023 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-1023-v001-scene` revision 9 / AST-1023 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1023-v001-scene` revision 9 / AST-1023 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-1023-v001-scene` revision 9 / AST-1023 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-024"></a>
## CND-024 — 번호표 발급기

분류: common; 기준 공간 연결 3개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

번호표 발급기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 번호표 발급기 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1024 v001](../assets/AST-1024-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-1024 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-1024 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-1024 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1024-v001-prototype` revision 1 / AST-1024 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-1024-v001-scene` revision 10 / AST-1024 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-1024-v001-scene` revision 9 / AST-1024 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-1024-v001-scene` revision 9 / AST-1024 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-025"></a>
## CND-025 — 연결 대기석

분류: common; 기준 공간 연결 3개 → 현재 4개. 모델 제작 상태와 별개인 후보 명세다.

연결 대기석의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 연결 대기석 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1025 v002](../assets/AST-1025-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-1025 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-1025 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-1025 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-1025 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1025-v001-prototype` revision 1 / AST-1025 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-1025-v001-scene` revision 4 / AST-1025 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-1025-v001-scene` revision 3 / AST-1025 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1025-v001-scene` revision 3 / AST-1025 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-1025-v001-scene` revision 3 / AST-1025 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1025-v002-prototype` revision 1 / AST-1025 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-1025-v002-scene` revision 7 / AST-1025 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-1025-v002-scene` revision 7 / AST-1025 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1025-v002-scene` revision 7 / AST-1025 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-1025-v002-scene` revision 7 / AST-1025 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-026"></a>
## CND-026 — 안내 책자 거치대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

안내 책자 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1026 v002](../assets/AST-1026-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-1026 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1026-v001-prototype` revision 1 / AST-1026 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-1026-v001-scene` revision 4 / AST-1026 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1026-v002-prototype` revision 1 / AST-1026 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-1026-v002-scene` revision 7 / AST-1026 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-027"></a>
## CND-027 — 서류 파일

분류: common; 기준 공간 연결 2개 → 현재 5개. 모델 제작 상태와 별개인 후보 명세다.

서류 파일의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1027 v001](../assets/AST-1027-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-1027 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-1027 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-1027 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-1027 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-057-workplace` revision 2 / AST-1027 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1027-v001-prototype` revision 1 / AST-1027 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-1027-v001-scene` revision 10 / AST-1027 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-1027-v001-scene` revision 9 / AST-1027 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-1027-v001-scene` revision 9 / AST-1027 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-1027-v001-scene` revision 9 / AST-1027 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-057-ast-1027-v001-scene` revision 9 / AST-1027 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-028"></a>
## CND-028 — 선반

분류: common; 기준 공간 연결 13개 → 현재 19개. 모델 제작 상태와 별개인 후보 명세다.

선반의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1028 v001](../assets/AST-1028-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-013-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-035-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-059-workplace` revision 2 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-1028 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-067-workplace` revision 3 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1028-v001-prototype` revision 1 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-1028-v001-scene` revision 10 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-013-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-035-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-059-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-1028-v001-scene` revision 9 / AST-1028 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-067-ast-1028-v001-scene` revision 9 / AST-1028 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-029"></a>
## CND-029 — 천칭 장식

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

천칭 장식의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 천칭 장식 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1029 v002](../assets/AST-1029-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-1029 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1029-v001-prototype` revision 1 / AST-1029 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-1029-v001-scene` revision 4 / AST-1029 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1029-v002-prototype` revision 1 / AST-1029 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-1029-v002-scene` revision 7 / AST-1029 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-030"></a>
## CND-030 — 녹색 램프

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

녹색 램프의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1030 v001](../assets/AST-1030-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-1030 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1030-v001-prototype` revision 1 / AST-1030 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-1030-v001-scene` revision 10 / AST-1030 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-031"></a>
## CND-031 — 실험·분석대

분류: common; 기준 공간 연결 2개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

실험·분석대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1031 v001](../assets/AST-1031-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1031 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-1031 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-1031 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1031-v001-prototype` revision 1 / AST-1031 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1031-v001-scene` revision 9 / AST-1031 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-1031-v001-scene` revision 9 / AST-1031 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1031-v001-scene` revision 9 / AST-1031 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-032"></a>
## CND-032 — 시험관대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

시험관대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 시험관대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1032 v001](../assets/AST-1032-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1032 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1032-v001-prototype` revision 1 / AST-1032 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1032-v001-scene` revision 9 / AST-1032 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-033"></a>
## CND-033 — 비커

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

비커의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1033 v001](../assets/AST-1033-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1033 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1033-v001-prototype` revision 1 / AST-1033 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1033-v001-scene` revision 9 / AST-1033 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-034"></a>
## CND-034 — 피펫 거치대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

피펫 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1034 v001](../assets/AST-1034-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1034 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1034-v001-prototype` revision 1 / AST-1034 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1034-v001-scene` revision 9 / AST-1034 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-035"></a>
## CND-035 — 소형 저울

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

소형 저울의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 소형 저울 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1035 v001](../assets/AST-1035-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1035 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1035-v001-prototype` revision 1 / AST-1035 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1035-v001-scene` revision 9 / AST-1035 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-036"></a>
## CND-036 — 세척대

분류: common; 기준 공간 연결 4개 → 현재 4개. 모델 제작 상태와 별개인 후보 명세다.

세척대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1036 v001](../assets/AST-1036-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1036 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-1036 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-1036 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-1036 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1036-v001-prototype` revision 1 / AST-1036 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1036-v001-scene` revision 9 / AST-1036 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-1036-v001-scene` revision 9 / AST-1036 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1036-v001-scene` revision 9 / AST-1036 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-1036-v001-scene` revision 9 / AST-1036 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-037"></a>
## CND-037 — 장비함

분류: common; 기준 공간 연결 3개 → 현재 5개. 모델 제작 상태와 별개인 후보 명세다.

장비함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1037 v001](../assets/AST-1037-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서버실 | PRM-060 v001 | PAN-060 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1037 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-1037 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-1037 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-1037 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-060-workplace` revision 3 / AST-1037 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1037-v001-prototype` revision 1 / AST-1037 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1037-v001-scene` revision 9 / AST-1037 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-1037-v001-scene` revision 9 / AST-1037 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-1037-v001-scene` revision 9 / AST-1037 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-1037-v001-scene` revision 9 / AST-1037 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-060-ast-1037-v001-scene` revision 9 / AST-1037 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-038"></a>
## CND-038 — 분석 장비

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

분석 장비의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1038 v001](../assets/AST-1038-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-1038 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1038-v001-prototype` revision 1 / AST-1038 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-1038-v001-scene` revision 9 / AST-1038 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-039"></a>
## CND-039 — 현미경

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

현미경의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 현미경 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1039 v003](../assets/AST-1039-v003.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-1039 v003
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-1039 v003
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1039-v001-prototype` revision 1 / AST-1039 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-1039-v001-scene` revision 3 / AST-1039 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1039-v001-scene` revision 3 / AST-1039 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1039-v002-prototype` revision 1 / AST-1039 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1039-v003-prototype` revision 1 / AST-1039 v003
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-1039-v003-scene` revision 7 / AST-1039 v003
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1039-v003-scene` revision 7 / AST-1039 v003

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-040"></a>
## CND-040 — 부품 트레이

분류: common; 기준 공간 연결 7개 → 현재 8개. 모델 제작 상태와 별개인 후보 명세다.

부품 트레이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1040 v001](../assets/AST-1040-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 분석실 | PRM-007 v001 | PAN-007 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-007-workplace` revision 4 / AST-1040 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-1040 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-013-workplace` revision 2 / AST-1040 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1040 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-1040 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-1040 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-1040 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1040-v001-prototype` revision 1 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-007-ast-1040-v001-scene` revision 9 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-1040-v001-scene` revision 9 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-013-ast-1040-v001-scene` revision 9 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1040-v001-scene` revision 9 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1040-v001-scene` revision 9 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-1040-v001-scene` revision 9 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1040-v001-scene` revision 9 / AST-1040 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-1040-v001-scene` revision 9 / AST-1040 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-041"></a>
## CND-041 — 진찰·처치 침대

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

진찰·처치 침대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 프레임, 매트리스, 머리·발판, 선택 난간
형태·치수 미정 항목: 길이, 폭, 누운 높이, 난간·이동바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1041 v002](../assets/AST-1041-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-1041 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-1041 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1041-v001-prototype` revision 1 / AST-1041 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-1041-v001-scene` revision 3 / AST-1041 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-1041-v001-scene` revision 3 / AST-1041 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1041-v002-prototype` revision 1 / AST-1041 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-1041-v002-scene` revision 7 / AST-1041 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-1041-v002-scene` revision 7 / AST-1041 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-042"></a>
## CND-042 — 의료 모니터

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

의료 모니터의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1042 v001](../assets/AST-1042-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-1042 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-1042 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1042-v001-prototype` revision 1 / AST-1042 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-1042-v001-scene` revision 9 / AST-1042 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-1042-v001-scene` revision 9 / AST-1042 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-043"></a>
## CND-043 — 작업등

분류: common; 기준 공간 연결 3개 → 현재 4개. 모델 제작 상태와 별개인 후보 명세다.

작업등의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1043 v001](../assets/AST-1043-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 처치실 | PRM-009 v001 | PAN-009 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 진료실 | PRM-008 v001 | PAN-008 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-008-workplace` revision 3 / AST-1043 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-009-workplace` revision 2 / AST-1043 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-1043 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-1043 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1043-v001-prototype` revision 1 / AST-1043 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-008-ast-1043-v001-scene` revision 9 / AST-1043 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-009-ast-1043-v001-scene` revision 9 / AST-1043 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1043-v001-scene` revision 9 / AST-1043 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-1043-v001-scene` revision 9 / AST-1043 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-044"></a>
## CND-044 — 생활 침대

분류: common; 기준 공간 연결 3개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

생활 침대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 프레임, 매트리스, 머리·발판, 선택 난간
형태·치수 미정 항목: 길이, 폭, 누운 높이, 난간·이동바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1044 v002](../assets/AST-1044-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-1044 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-1044 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-1044 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1044-v001-prototype` revision 1 / AST-1044 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-1044-v001-scene` revision 3 / AST-1044 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-1044-v001-scene` revision 3 / AST-1044 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-1044-v001-scene` revision 3 / AST-1044 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1044-v002-prototype` revision 1 / AST-1044 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-1044-v002-scene` revision 7 / AST-1044 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-1044-v002-scene` revision 7 / AST-1044 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-1044-v002-scene` revision 7 / AST-1044 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-045"></a>
## CND-045 — 침대 옆 탁자

분류: common; 기준 공간 연결 2개 → 현재 6개. 모델 제작 상태와 별개인 후보 명세다.

침대 옆 탁자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 프레임, 매트리스, 머리·발판, 선택 난간
형태·치수 미정 항목: 길이, 폭, 누운 높이, 난간·이동바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1045 v001](../assets/AST-1045-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조타실 | PRM-045 v001 | PAN-045 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-1045 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-1045 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-045-workplace` revision 3 / AST-1045 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-1045 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-061-workplace` revision 4 / AST-1045 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-1045 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1045-v001-prototype` revision 1 / AST-1045 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-1045-v001-scene` revision 9 / AST-1045 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-1045-v001-scene` revision 9 / AST-1045 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-1045-v001-scene` revision 9 / AST-1045 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-1045-v001-scene` revision 9 / AST-1045 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-061-ast-1045-v001-scene` revision 9 / AST-1045 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-1045-v001-scene` revision 9 / AST-1045 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-046"></a>
## CND-046 — 보호자 의자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

보호자 의자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1046 v001](../assets/AST-1046-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-1046 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1046-v001-prototype` revision 1 / AST-1046 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-1046-v001-scene` revision 9 / AST-1046 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-047"></a>
## CND-047 — 이동식 식탁

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

이동식 식탁의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 이동식 식탁 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1047 v001](../assets/AST-1047-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-1047 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1047-v001-prototype` revision 1 / AST-1047 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-1047-v001-scene` revision 9 / AST-1047 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-048"></a>
## CND-048 — 호출 장치

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

호출 장치의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 호출 장치 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1048 v001](../assets/AST-1048-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 병실 | PRM-010 v001 | PAN-010 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-010-workplace` revision 4 / AST-1048 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1048-v001-prototype` revision 1 / AST-1048 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-010-ast-1048-v001-scene` revision 9 / AST-1048 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-049"></a>
## CND-049 — 서류 트레이

분류: common; 기준 공간 연결 5개 → 현재 5개. 모델 제작 상태와 별개인 후보 명세다.

서류 트레이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1049 v001](../assets/AST-1049-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서비스 창구 | PRM-022 v001 | PAN-022 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 금융 창구 | PRM-056 v001 | PAN-056 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-1049 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-022-workplace` revision 4 / AST-1049 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-1049 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-1049 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-056-workplace` revision 4 / AST-1049 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1049-v001-prototype` revision 1 / AST-1049 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-1049-v001-scene` revision 9 / AST-1049 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-022-ast-1049-v001-scene` revision 9 / AST-1049 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-1049-v001-scene` revision 9 / AST-1049 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-1049-v001-scene` revision 9 / AST-1049 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-056-ast-1049-v001-scene` revision 9 / AST-1049 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-050"></a>
## CND-050 — 학생 책상

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

학생 책상의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1050 v001](../assets/AST-1050-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교실 | PRM-012 v001 | PAN-012 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-012-workplace` revision 2 / AST-1050 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1050-v001-prototype` revision 1 / AST-1050 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-012-ast-1050-v001-scene` revision 9 / AST-1050 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-051"></a>
## CND-051 — 교탁

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

교탁의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1051 v001](../assets/AST-1051-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교실 | PRM-012 v001 | PAN-012 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-012-workplace` revision 2 / AST-1051 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1051-v001-prototype` revision 1 / AST-1051 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-012-ast-1051-v001-scene` revision 9 / AST-1051 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-052"></a>
## CND-052 — 독립형 칠판

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

독립형 칠판의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1052 v001](../assets/AST-1052-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교실 | PRM-012 v001 | PAN-012 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-012-workplace` revision 2 / AST-1052 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1052-v001-prototype` revision 1 / AST-1052 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-012-ast-1052-v001-scene` revision 9 / AST-1052 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-053"></a>
## CND-053 — 교재

분류: common; 기준 공간 연결 2개 → 현재 4개. 모델 제작 상태와 별개인 후보 명세다.

교재의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1053 v001](../assets/AST-1053-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교실 | PRM-012 v001 | PAN-012 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1053 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-1053 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-012-workplace` revision 2 / AST-1053 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-059-workplace` revision 2 / AST-1053 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1053-v001-prototype` revision 1 / AST-1053 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1053-v001-scene` revision 10 / AST-1053 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-1053-v001-scene` revision 10 / AST-1053 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-012-ast-1053-v001-scene` revision 9 / AST-1053 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-059-ast-1053-v001-scene` revision 9 / AST-1053 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-054"></a>
## CND-054 — 사물함

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

사물함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1054 v001](../assets/AST-1054-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교실 | PRM-012 v001 | PAN-012 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-012-workplace` revision 2 / AST-1054 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-1054 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1054-v001-prototype` revision 1 / AST-1054 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-012-ast-1054-v001-scene` revision 9 / AST-1054 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-1054-v001-scene` revision 9 / AST-1054 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-055"></a>
## CND-055 — 작업대

분류: common; 기준 공간 연결 9개 → 현재 14개. 모델 제작 상태와 별개인 후보 명세다.

작업대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1055 v001](../assets/AST-1055-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-013-workplace` revision 2 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-053-workplace` revision 2 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-1055 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-067-workplace` revision 3 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1055-v001-prototype` revision 1 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-013-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-053-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-1055-v001-scene` revision 9 / AST-1055 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-067-ast-1055-v001-scene` revision 9 / AST-1055 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-056"></a>
## CND-056 — 스툴

분류: common; 기준 공간 연결 2개 → 현재 5개. 모델 제작 상태와 별개인 후보 명세다.

스툴의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1056 v001](../assets/AST-1056-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 실험실 | PRM-006 v001 | PAN-006 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-006-workplace` revision 2 / AST-1056 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-013-workplace` revision 2 / AST-1056 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1056 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-1056 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-1056 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1056-v001-prototype` revision 1 / AST-1056 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-006-ast-1056-v001-scene` revision 9 / AST-1056 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-013-ast-1056-v001-scene` revision 9 / AST-1056 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1056-v001-scene` revision 9 / AST-1056 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-1056-v001-scene` revision 9 / AST-1056 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-1056-v001-scene` revision 9 / AST-1056 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-057"></a>
## CND-057 — 교육용 조립 키트

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

교육용 조립 키트의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 교육용 조립 키트 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1057 v001](../assets/AST-1057-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-013-workplace` revision 2 / AST-1057 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1057-v001-prototype` revision 1 / AST-1057 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-013-ast-1057-v001-scene` revision 9 / AST-1057 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-058"></a>
## CND-058 — 보관 상자

분류: common; 기준 공간 연결 6개 → 현재 9개. 모델 제작 상태와 별개인 후보 명세다.

보관 상자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1058 v001](../assets/AST-1058-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 교육 실습실 | PRM-013 v001 | PAN-013 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-013-workplace` revision 2 / AST-1058 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-1058 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-1058 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-1058 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-1058 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-1058 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-1058 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-053-workplace` revision 2 / AST-1058 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1058-v001-prototype` revision 1 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-013-ast-1058-v001-scene` revision 9 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-1058-v001-scene` revision 9 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1058-v001-scene` revision 9 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-1058-v001-scene` revision 9 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-1058-v001-scene` revision 9 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-1058-v001-scene` revision 9 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-1058-v001-scene` revision 9 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-053-ast-1058-v001-scene` revision 9 / AST-1058 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1058-v001-scene` revision 9 / AST-1058 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-059"></a>
## CND-059 — 강연대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

강연대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 강연대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1059 v001](../assets/AST-1059-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 강의실 | PRM-014 v001 | PAN-014 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-014-workplace` revision 3 / AST-1059 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1059-v001-prototype` revision 1 / AST-1059 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-014-ast-1059-v001-scene` revision 9 / AST-1059 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-060"></a>
## CND-060 — 발표 화면

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

발표 화면의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1060 v001](../assets/AST-1060-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 강의실 | PRM-014 v001 | PAN-014 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-014-workplace` revision 3 / AST-1060 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1060-v001-prototype` revision 1 / AST-1060 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-014-ast-1060-v001-scene` revision 9 / AST-1060 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-061"></a>
## CND-061 — 작은 AV 장치

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 AV 장치의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 작은 AV 장치 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1061 v001](../assets/AST-1061-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 강의실 | PRM-014 v001 | PAN-014 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-014-workplace` revision 3 / AST-1061 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1061-v001-prototype` revision 1 / AST-1061 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-014-ast-1061-v001-scene` revision 9 / AST-1061 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-062"></a>
## CND-062 — 편안한 의자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

편안한 의자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1062 v001](../assets/AST-1062-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-1062 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1062-v001-prototype` revision 1 / AST-1062 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-1062-v001-scene` revision 9 / AST-1062 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-063"></a>
## CND-063 — 티슈 상자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

티슈 상자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1063 v001](../assets/AST-1063-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-1063 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1063-v001-prototype` revision 1 / AST-1063 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-1063-v001-scene` revision 9 / AST-1063 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-064"></a>
## CND-064 — 상담 노트

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

상담 노트의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1064 v001](../assets/AST-1064-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-1064 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1064-v001-prototype` revision 1 / AST-1064 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-1064-v001-scene` revision 9 / AST-1064 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-065"></a>
## CND-065 — 화분

분류: common; 기준 공간 연결 3개 → 현재 10개. 모델 제작 상태와 별개인 후보 명세다.

화분의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 선택 화분, 줄기, 잎 묶음
형태·치수 미정 항목: 전체 높이, 수관 폭, 잎 반복 개수, 화분 비율
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-010 v001](../assets/AST-010-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 거실 | PRM-062 v001 | PAN-062 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 행정·문서 처리 사무실 | PRM-003 v001 | PAN-003 v001 | office-administration v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 민원·방문객 접수실 | PRM-004 v001 | PAN-004 v001 | office-public-reception v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 전문 상담 사무실 | PRM-005 v001 | PAN-005 v001 | office-professional-consultation v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 의료 접수실 | PRM-011 v001 | PAN-011 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-003-workplace` revision 4 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-004-workplace` revision 3 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-005-workplace` revision 2 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-011-workplace` revision 3 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-026-workplace` revision 2 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-010 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-062-workplace` revision 2 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-010-v001-scene` revision 3 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-010-v001-prototype` revision 1 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-010-v001-scene` revision 10 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-003-ast-010-v001-scene` revision 10 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-004-ast-010-v001-scene` revision 10 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-005-ast-010-v001-scene` revision 10 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-010-v001-scene` revision 9 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-011-ast-010-v001-scene` revision 9 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-010-v001-scene` revision 9 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-010-v001-scene` revision 9 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-010-v001-scene` revision 9 / AST-010 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-010-v001-scene` revision 9 / AST-010 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-066"></a>
## CND-066 — 활동 교구

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

활동 교구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 활동 교구 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1066 v001](../assets/AST-1066-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-1066 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1066-v001-prototype` revision 1 / AST-1066 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-1066-v001-scene` revision 9 / AST-1066 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-067"></a>
## CND-067 — 러그·바닥 매트

분류: common; 기준 공간 연결 4개 → 현재 7개. 모델 제작 상태와 별개인 후보 명세다.

러그·바닥 매트의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1067 v001](../assets/AST-1067-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 복지 활동실 | PRM-016 v001 | PAN-016 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 거실 | PRM-062 v001 | PAN-062 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 복지·심리 상담실 | PRM-015 v001 | PAN-015 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-1067 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-015-workplace` revision 2 / AST-1067 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-016-workplace` revision 3 / AST-1067 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-1067 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-1067 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-1067 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-062-workplace` revision 2 / AST-1067 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1067-v001-prototype` revision 1 / AST-1067 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-1067-v001-scene` revision 10 / AST-1067 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-015-ast-1067-v001-scene` revision 9 / AST-1067 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-016-ast-1067-v001-scene` revision 9 / AST-1067 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-1067-v001-scene` revision 9 / AST-1067 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-1067-v001-scene` revision 9 / AST-1067 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-1067-v001-scene` revision 9 / AST-1067 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-1067-v001-scene` revision 9 / AST-1067 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-068"></a>
## CND-068 — 이동 보조 의자

실제 제작 형상은 **보행 보조 프레임**이다. 원본 후보 CND-068 명칭 「이동 보조 의자」와 ID는 보존했다. PAN-017에 보이는 프레임·손잡이를 우선한 일반 모델링 판단이며, 이미지에 없는 좌석은 추가하지 않았다. 아래 기획 명세와 실제 제작 결과를 구별해 읽는다.

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

이동 보조 의자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1068 v001](../assets/AST-1068-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-1068 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1068-v001-prototype` revision 1 / AST-1068 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-1068-v001-scene` revision 9 / AST-1068 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-069"></a>
## CND-069 — 휠체어

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

휠체어의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 휠체어 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1069 v002](../assets/AST-1069-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-1069 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1069-v001-prototype` revision 1 / AST-1069 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-1069-v001-scene` revision 3 / AST-1069 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1069-v002-prototype` revision 1 / AST-1069 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-1069-v002-scene` revision 7 / AST-1069 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-070"></a>
## CND-070 — 보조 손잡이

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

보조 손잡이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1070 v001](../assets/AST-1070-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 요양실 | PRM-017 v001 | PAN-017 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-017-workplace` revision 2 / AST-1070 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1070-v001-prototype` revision 1 / AST-1070 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-017-ast-1070-v001-scene` revision 9 / AST-1070 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-071"></a>
## CND-071 — 소형 생산 기계

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

소형 생산 기계의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1071 v002](../assets/AST-1071-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-018-workplace` revision 3 / AST-1071 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1071-v001-prototype` revision 1 / AST-1071 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-1071-v001-scene` revision 3 / AST-1071 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1071-v002-prototype` revision 1 / AST-1071 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-1071-v002-scene` revision 7 / AST-1071 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-072"></a>
## CND-072 — 짧은 컨베이어

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

짧은 컨베이어의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 짧은 컨베이어 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1072 v001](../assets/AST-1072-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-018-workplace` revision 3 / AST-1072 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1072-v001-prototype` revision 1 / AST-1072 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-1072-v001-scene` revision 9 / AST-1072 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-073"></a>
## CND-073 — 투입함

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

투입함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 투입함 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1073 v001](../assets/AST-1073-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-018-workplace` revision 3 / AST-1073 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1073-v001-prototype` revision 1 / AST-1073 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-1073-v001-scene` revision 9 / AST-1073 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-074"></a>
## CND-074 — 완성품 상자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

완성품 상자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1074 v001](../assets/AST-1074-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-018-workplace` revision 3 / AST-1074 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1074-v001-prototype` revision 1 / AST-1074 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-1074-v001-scene` revision 9 / AST-1074 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-075"></a>
## CND-075 — 제어 패널

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

제어 패널의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1075 v001](../assets/AST-1075-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-018-workplace` revision 3 / AST-1075 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1075-v001-prototype` revision 1 / AST-1075 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-1075-v001-scene` revision 9 / AST-1075 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-076"></a>
## CND-076 — 안전 가드

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

안전 가드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1076 v001](../assets/AST-1076-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 생산 구역 | PRM-018 v001 | PAN-018 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-018-workplace` revision 3 / AST-1076 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1076-v001-prototype` revision 1 / AST-1076 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-018-ast-1076-v001-scene` revision 9 / AST-1076 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-077"></a>
## CND-077 — 공구 거치대

분류: common; 기준 공간 연결 1개 → 현재 4개. 모델 제작 상태와 별개인 후보 명세다.

공구 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1077 v001](../assets/AST-1077-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1077 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-1077 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-1077 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-067-workplace` revision 3 / AST-1077 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1077-v001-prototype` revision 1 / AST-1077 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1077-v001-scene` revision 9 / AST-1077 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1077-v001-scene` revision 9 / AST-1077 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-1077-v001-scene` revision 9 / AST-1077 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-067-ast-1077-v001-scene` revision 9 / AST-1077 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-078"></a>
## CND-078 — 조립 중인 단순 제품

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

조립 중인 단순 제품의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 조립 중인 단순 제품 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1078 v002](../assets/AST-1078-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1078 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1078-v001-prototype` revision 1 / AST-1078 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1078-v001-scene` revision 3 / AST-1078 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1078-v002-prototype` revision 1 / AST-1078 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1078-v002-scene` revision 7 / AST-1078 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-079"></a>
## CND-079 — 바이스

분류: common; 기준 공간 연결 2개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

바이스의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1079 v001](../assets/AST-1079-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1079 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-1079 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-1079 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1079-v001-prototype` revision 1 / AST-1079 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1079-v001-scene` revision 9 / AST-1079 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1079-v001-scene` revision 9 / AST-1079 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-1079-v001-scene` revision 9 / AST-1079 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-080"></a>
## CND-080 — 공구함

분류: common; 기준 공간 연결 4개 → 현재 6개. 모델 제작 상태와 별개인 후보 명세다.

공구함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1080 v001](../assets/AST-1080-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 조립 구역 | PRM-019 v001 | PAN-019 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-019-workplace` revision 2 / AST-1080 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-1080 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-036-workplace` revision 3 / AST-1080 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-1080 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-1080 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-067-workplace` revision 3 / AST-1080 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1080-v001-prototype` revision 1 / AST-1080 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-019-ast-1080-v001-scene` revision 9 / AST-1080 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1080-v001-scene` revision 9 / AST-1080 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-1080-v001-scene` revision 9 / AST-1080 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-1080-v001-scene` revision 9 / AST-1080 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-1080-v001-scene` revision 9 / AST-1080 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-067-ast-1080-v001-scene` revision 9 / AST-1080 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-081"></a>
## CND-081 — 열린 기계 케이스

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

열린 기계 케이스의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1081 v002](../assets/AST-1081-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 정비 구역 | PRM-020 v001 | PAN-020 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-020-workplace` revision 2 / AST-1081 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1081-v001-prototype` revision 1 / AST-1081 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1081-v001-scene` revision 3 / AST-1081 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1081-v002-prototype` revision 1 / AST-1081 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-020-ast-1081-v002-scene` revision 7 / AST-1081 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-082"></a>
## CND-082 — 단순 포장 상품

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

단순 포장 상품의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 단순 포장 상품 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1082 v001](../assets/AST-1082-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-1082 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-1082 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1082-v001-prototype` revision 1 / AST-1082 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-1082-v001-scene` revision 9 / AST-1082 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-1082-v001-scene` revision 9 / AST-1082 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-083"></a>
## CND-083 — POS 기기

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

POS 기기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1083 v001](../assets/AST-1083-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-1083 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1083-v001-prototype` revision 1 / AST-1083 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-1083-v001-scene` revision 9 / AST-1083 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-084"></a>
## CND-084 — 바구니

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

바구니의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1084 v001](../assets/AST-1084-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 소매점 | PRM-021 v001 | PAN-021 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-021-workplace` revision 2 / AST-1084 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1084-v001-prototype` revision 1 / AST-1084 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-021-ast-1084-v001-scene` revision 9 / AST-1084 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-085"></a>
## CND-085 — 미용 의자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

미용 의자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1085 v002](../assets/AST-1085-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-1085 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1085-v001-prototype` revision 1 / AST-1085 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-1085-v001-scene` revision 3 / AST-1085 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1085-v002-prototype` revision 1 / AST-1085 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-1085-v002-scene` revision 7 / AST-1085 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-086"></a>
## CND-086 — 독립형 거울

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

독립형 거울의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 거울 면, 테두리, 뒤쪽 지지대, 받침
형태·치수 미정 항목: 반사면 크기, 기울기, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1086 v001](../assets/AST-1086-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-1086 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1086-v001-prototype` revision 1 / AST-1086 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-1086-v001-scene` revision 9 / AST-1086 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-087"></a>
## CND-087 — 세발대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

세발대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1087 v001](../assets/AST-1087-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 미용실 | PRM-023 v001 | PAN-023 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-023-workplace` revision 2 / AST-1087 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1087-v001-prototype` revision 1 / AST-1087 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-023-ast-1087-v001-scene` revision 9 / AST-1087 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-088"></a>
## CND-088 — 조리대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

조리대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1088 v001](../assets/AST-1088-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-1088 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1088-v001-prototype` revision 1 / AST-1088 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1088-v001-scene` revision 9 / AST-1088 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-089"></a>
## CND-089 — 가열 기구

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

가열 기구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1089 v002](../assets/AST-1089-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-1089 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1089-v001-prototype` revision 1 / AST-1089 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1089-v001-scene` revision 3 / AST-1089 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1089-v002-prototype` revision 1 / AST-1089 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1089-v002-scene` revision 7 / AST-1089 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-090"></a>
## CND-090 — 냉장고

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

냉장고의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1090 v001](../assets/AST-1090-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-1090 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1090-v001-prototype` revision 1 / AST-1090 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1090-v001-scene` revision 9 / AST-1090 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-091"></a>
## CND-091 — 조리도구 거치대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

조리도구 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 조리도구 거치대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1091 v002](../assets/AST-1091-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-1091 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1091-v001-prototype` revision 1 / AST-1091 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1091-v001-scene` revision 3 / AST-1091 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1091-v002-prototype` revision 1 / AST-1091 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1091-v002-scene` revision 7 / AST-1091 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-092"></a>
## CND-092 — 접시 선반

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

접시 선반의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1092 v001](../assets/AST-1092-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-1092 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1092-v001-prototype` revision 1 / AST-1092 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1092-v001-scene` revision 9 / AST-1092 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-093"></a>
## CND-093 — 반죽 작업대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

반죽 작업대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1093 v001](../assets/AST-1093-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-1093 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1093-v001-prototype` revision 1 / AST-1093 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1093-v001-scene` revision 9 / AST-1093 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-094"></a>
## CND-094 — 믹서

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

믹서의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1094 v001](../assets/AST-1094-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-1094 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1094-v001-prototype` revision 1 / AST-1094 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1094-v001-scene` revision 9 / AST-1094 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-095"></a>
## CND-095 — 오븐

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

오븐의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1095 v002](../assets/AST-1095-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-1095 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1095-v001-prototype` revision 1 / AST-1095 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1095-v001-scene` revision 3 / AST-1095 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1095-v002-prototype` revision 1 / AST-1095 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1095-v002-scene` revision 7 / AST-1095 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-096"></a>
## CND-096 — 베이킹 트레이

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

베이킹 트레이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1096 v001](../assets/AST-1096-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-1096 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1096-v001-prototype` revision 1 / AST-1096 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1096-v001-scene` revision 9 / AST-1096 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-097"></a>
## CND-097 — 식힘 선반

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

식힘 선반의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1097 v001](../assets/AST-1097-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 제과실 | PRM-025 v001 | PAN-025 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-025-workplace` revision 2 / AST-1097 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1097-v001-prototype` revision 1 / AST-1097 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-025-ast-1097-v001-scene` revision 9 / AST-1097 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-098"></a>
## CND-098 — 식기

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

식기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 식기 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1098 v002](../assets/AST-1098-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주방 | PRM-024 v001 | PAN-024 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-024-workplace` revision 3 / AST-1098 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-026-workplace` revision 2 / AST-1098 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1098-v001-prototype` revision 1 / AST-1098 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1098-v001-scene` revision 3 / AST-1098 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-1098-v001-scene` revision 3 / AST-1098 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1098-v002-prototype` revision 1 / AST-1098 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-024-ast-1098-v002-scene` revision 7 / AST-1098 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-1098-v002-scene` revision 7 / AST-1098 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-099"></a>
## CND-099 — 배식 보조대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

배식 보조대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1099 v001](../assets/AST-1099-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-026-workplace` revision 2 / AST-1099 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1099-v001-prototype` revision 1 / AST-1099 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-1099-v001-scene` revision 9 / AST-1099 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-100"></a>
## CND-100 — 메뉴 거치대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

메뉴 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 메뉴 거치대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1100 v001](../assets/AST-1100-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 식당 홀 | PRM-026 v001 | PAN-026 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-026-workplace` revision 2 / AST-1100 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1100-v001-prototype` revision 1 / AST-1100 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-026-ast-1100-v001-scene` revision 9 / AST-1100 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-101"></a>
## CND-101 — 펜 태블릿

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

펜 태블릿의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1101 v003](../assets/AST-1101-v003.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-1101 v003
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1101-v001-prototype` revision 1 / AST-1101 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-1101-v001-scene` revision 3 / AST-1101 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1101-v002-prototype` revision 1 / AST-1101 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1101-v003-prototype` revision 1 / AST-1101 v003
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-1101-v003-scene` revision 7 / AST-1101 v003

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-102"></a>
## CND-102 — 시안 보드

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

시안 보드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1102 v001](../assets/AST-1102-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-1102 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1102-v001-prototype` revision 1 / AST-1102 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-1102-v001-scene` revision 9 / AST-1102 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-103"></a>
## CND-103 — 재료 샘플

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

재료 샘플의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 재료 샘플 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1103 v001](../assets/AST-1103-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 디자인 작업실 | PRM-027 v001 | PAN-027 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-027-workplace` revision 4 / AST-1103 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1103-v001-prototype` revision 1 / AST-1103 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-027-ast-1103-v001-scene` revision 9 / AST-1103 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-104"></a>
## CND-104 — 이젤

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

이젤의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 이젤 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1104 v002](../assets/AST-1104-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-1104 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1104-v001-prototype` revision 1 / AST-1104 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-1104-v001-scene` revision 3 / AST-1104 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1104-v002-prototype` revision 1 / AST-1104 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-1104-v002-scene` revision 7 / AST-1104 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-105"></a>
## CND-105 — 빈 캔버스

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

빈 캔버스의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 빈 캔버스 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1105 v001](../assets/AST-1105-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-1105 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1105-v001-prototype` revision 1 / AST-1105 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-1105-v001-scene` revision 9 / AST-1105 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-106"></a>
## CND-106 — 펜꽂이

분류: common; 기준 공간 연결 1개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

펜꽂이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 펜꽂이 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-012 v001](../assets/AST-012-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 협업·기획 사무실 | PRM-002 v001 | PAN-002 v001 | office-collaboration v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-012 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-002-workplace` revision 3 / AST-012 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-012-v001-scene` revision 3 / AST-012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-012-v001-prototype` revision 1 / AST-012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-002-ast-012-v001-scene` revision 10 / AST-012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-012-v001-scene` revision 9 / AST-012 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-012-v001-scene` revision 9 / AST-012 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-107"></a>
## CND-107 — 팔레트 도구

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

팔레트 도구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 팔레트 도구 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1107 v001](../assets/AST-1107-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 미술 작업실 | PRM-028 v001 | PAN-028 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-028-workplace` revision 4 / AST-1107 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1107-v001-prototype` revision 1 / AST-1107 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-028-ast-1107-v001-scene` revision 9 / AST-1107 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-108"></a>
## CND-108 — 손공구

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

손공구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1108 v001](../assets/AST-1108-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공예 작업실 | PRM-029 v001 | PAN-029 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-029-workplace` revision 1 / AST-1108 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-1108 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1108-v001-prototype` revision 1 / AST-1108 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-029-ast-1108-v001-scene` revision 9 / AST-1108 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-1108-v001-scene` revision 9 / AST-1108 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-109"></a>
## CND-109 — 카메라

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

카메라의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 카메라 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1109 v001](../assets/AST-1109-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-1109 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-1109 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1109-v001-prototype` revision 1 / AST-1109 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-1109-v001-scene` revision 9 / AST-1109 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-1109-v001-scene` revision 9 / AST-1109 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-110"></a>
## CND-110 — 삼각대

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

삼각대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 삼각대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1110 v002](../assets/AST-1110-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-1110 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-1110 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1110-v001-prototype` revision 1 / AST-1110 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-1110-v001-scene` revision 3 / AST-1110 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-1110-v001-scene` revision 3 / AST-1110 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1110-v002-prototype` revision 1 / AST-1110 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-1110-v002-scene` revision 7 / AST-1110 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-1110-v002-scene` revision 7 / AST-1110 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-111"></a>
## CND-111 — 조명 스탠드

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

조명 스탠드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1111 v001](../assets/AST-1111-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-1111 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-033-workplace` revision 2 / AST-1111 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1111-v001-prototype` revision 1 / AST-1111 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-1111-v001-scene` revision 9 / AST-1111 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-033-ast-1111-v001-scene` revision 9 / AST-1111 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-112"></a>
## CND-112 — 작은 제품 촬영대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 제품 촬영대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 작은 제품 촬영대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1112 v001](../assets/AST-1112-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-1112 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1112-v001-prototype` revision 1 / AST-1112 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-1112-v001-scene` revision 9 / AST-1112 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-113"></a>
## CND-113 — 반사판

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

반사판의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 반사판 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1113 v001](../assets/AST-1113-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-1113 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1113-v001-prototype` revision 1 / AST-1113 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-1113-v001-scene` revision 9 / AST-1113 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-114"></a>
## CND-114 — 보관 케이스

분류: common; 기준 공간 연결 3개 → 현재 4개. 모델 제작 상태와 별개인 후보 명세다.

보관 케이스의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1114 v001](../assets/AST-1114-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 촬영 스튜디오 | PRM-030 v001 | PAN-030 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 장비 관리실 | PRM-067 v001 | PAN-067 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 서버실 | PRM-060 v001 | PAN-060 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-030-workplace` revision 2 / AST-1114 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-1114 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-060-workplace` revision 3 / AST-1114 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-067-workplace` revision 3 / AST-1114 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1114-v001-prototype` revision 1 / AST-1114 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-030-ast-1114-v001-scene` revision 9 / AST-1114 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1114-v001-scene` revision 9 / AST-1114 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-060-ast-1114-v001-scene` revision 9 / AST-1114 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-067-ast-1114-v001-scene` revision 9 / AST-1114 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-115"></a>
## CND-115 — 방송 테이블

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

방송 테이블의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1115 v001](../assets/AST-1115-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-1115 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1115-v001-prototype` revision 1 / AST-1115 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-1115-v001-scene` revision 9 / AST-1115 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-116"></a>
## CND-116 — 마이크 암

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

마이크 암의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 마이크 암 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1116 v001](../assets/AST-1116-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-1116 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1116-v001-prototype` revision 1 / AST-1116 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-1116-v001-scene` revision 9 / AST-1116 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-117"></a>
## CND-117 — 헤드폰

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

헤드폰의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 헤드폰 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1117 v001](../assets/AST-1117-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-1117 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-1117 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1117-v001-prototype` revision 1 / AST-1117 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-1117-v001-scene` revision 9 / AST-1117 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-1117-v001-scene` revision 9 / AST-1117 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-118"></a>
## CND-118 — 소형 오디오 콘솔

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

소형 오디오 콘솔의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1118 v001](../assets/AST-1118-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-1118 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1118-v001-prototype` revision 1 / AST-1118 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-1118-v001-scene` revision 9 / AST-1118 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-119"></a>
## CND-119 — 조명

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

조명의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1119 v001](../assets/AST-1119-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 방송 스튜디오 | PRM-031 v001 | PAN-031 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-031-workplace` revision 4 / AST-1119 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1119-v001-prototype` revision 1 / AST-1119 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-031-ast-1119-v001-scene` revision 9 / AST-1119 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-120"></a>
## CND-120 — 스피커

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

스피커의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 스피커 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1120 v001](../assets/AST-1120-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-1120 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-033-workplace` revision 2 / AST-1120 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1120-v001-prototype` revision 1 / AST-1120 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-1120-v001-scene` revision 9 / AST-1120 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-033-ast-1120-v001-scene` revision 9 / AST-1120 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-121"></a>
## CND-121 — 미디어 보관함

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

미디어 보관함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1121 v001](../assets/AST-1121-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 영상 편집실 | PRM-032 v001 | PAN-032 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-032-workplace` revision 3 / AST-1121 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1121-v001-prototype` revision 1 / AST-1121 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-032-ast-1121-v001-scene` revision 9 / AST-1121 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-122"></a>
## CND-122 — 낮은 무대판

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 무대판의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1122 v001](../assets/AST-1122-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-033-workplace` revision 2 / AST-1122 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1122-v001-prototype` revision 1 / AST-1122 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-033-ast-1122-v001-scene` revision 9 / AST-1122 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-123"></a>
## CND-123 — 마이크 스탠드

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

마이크 스탠드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1123 v001](../assets/AST-1123-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-033-workplace` revision 2 / AST-1123 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1123-v001-prototype` revision 1 / AST-1123 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-033-ast-1123-v001-scene` revision 9 / AST-1123 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-124"></a>
## CND-124 — 전시대

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

전시대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 전시대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1124 v001](../assets/AST-1124-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전시실 | PRM-034 v001 | PAN-034 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-034-workplace` revision 2 / AST-1124 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-1124 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1124-v001-prototype` revision 1 / AST-1124 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-1124-v001-scene` revision 9 / AST-1124 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1124-v001-scene` revision 7 / AST-1124 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-125"></a>
## CND-125 — 추상 조형물

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

추상 조형물의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 추상 조형물 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_or_meshy_review / 기존 형태·스크립트 재사용 및 단순 도형 표현부터 검토하고 자유 곡면이 핵심일 때만 승인된 Meshy 범위 검토.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1125 v001](../assets/AST-1125-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전시실 | PRM-034 v001 | PAN-034 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-034-workplace` revision 2 / AST-1125 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1125-v001-prototype` revision 1 / AST-1125 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-1125-v001-scene` revision 9 / AST-1125 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-126"></a>
## CND-126 — 독립형 액자 거치대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

독립형 액자 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1126 v002](../assets/AST-1126-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전시실 | PRM-034 v001 | PAN-034 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-034-workplace` revision 2 / AST-1126 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1126-v001-prototype` revision 1 / AST-1126 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-1126-v001-scene` revision 3 / AST-1126 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1126-v002-prototype` revision 1 / AST-1126 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-1126-v002-scene` revision 7 / AST-1126 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-127"></a>
## CND-127 — 벤치

분류: common; 기준 공간 연결 5개 → 현재 6개. 모델 제작 상태와 별개인 후보 명세다.

벤치의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1127 v002](../assets/AST-1127-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전시실 | PRM-034 v001 | PAN-034 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 체육관 | PRM-047 v001 | PAN-047 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-034-workplace` revision 2 / AST-1127 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-1127 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-047-workplace` revision 2 / AST-1127 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-049-workplace` revision 2 / AST-1127 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-1127 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-1127 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1127-v001-prototype` revision 1 / AST-1127 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-1127-v001-scene` revision 3 / AST-1127 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1127-v001-scene` revision 3 / AST-1127 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-1127-v001-scene` revision 3 / AST-1127 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-049-ast-1127-v001-scene` revision 3 / AST-1127 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1127-v001-scene` revision 3 / AST-1127 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1127-v001-scene` revision 3 / AST-1127 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1127-v002-prototype` revision 1 / AST-1127 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-1127-v002-scene` revision 7 / AST-1127 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1127-v002-scene` revision 7 / AST-1127 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-1127-v002-scene` revision 7 / AST-1127 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-049-ast-1127-v002-scene` revision 7 / AST-1127 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1127-v002-scene` revision 7 / AST-1127 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1127-v002-scene` revision 7 / AST-1127 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-128"></a>
## CND-128 — 전시 조명

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

전시 조명의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1128 v001](../assets/AST-1128-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 전시실 | PRM-034 v001 | PAN-034 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공연 무대 | PRM-033 v001 | PAN-033 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-033-workplace` revision 2 / AST-1128 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-034-workplace` revision 2 / AST-1128 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1128-v001-prototype` revision 1 / AST-1128 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-033-ast-1128-v001-scene` revision 9 / AST-1128 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-034-ast-1128-v001-scene` revision 9 / AST-1128 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-129"></a>
## CND-129 — 미술 교구

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

미술 교구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 미술 교구 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1129 v001](../assets/AST-1129-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 문화 활동실 | PRM-035 v001 | PAN-035 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-035-workplace` revision 2 / AST-1129 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1129-v001-prototype` revision 1 / AST-1129 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-035-ast-1129-v001-scene` revision 9 / AST-1129 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-130"></a>
## CND-130 — 낮은 비계

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 비계의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1130 v001](../assets/AST-1130-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-036-workplace` revision 3 / AST-1130 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1130-v001-prototype` revision 1 / AST-1130 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-1130-v001-scene` revision 9 / AST-1130 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-131"></a>
## CND-131 — 부분 벽돌 구조

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

부분 벽돌 구조의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 부분 벽돌 구조 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1131 v002](../assets/AST-1131-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-036-workplace` revision 3 / AST-1131 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1131-v001-prototype` revision 1 / AST-1131 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-1131-v001-scene` revision 3 / AST-1131 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1131-v002-prototype` revision 1 / AST-1131 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-1131-v002-scene` revision 7 / AST-1131 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-132"></a>
## CND-132 — 자재 더미

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

자재 더미의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 자재 더미 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1132 v002](../assets/AST-1132-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-036-workplace` revision 3 / AST-1132 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1132-v001-prototype` revision 1 / AST-1132 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-1132-v001-scene` revision 3 / AST-1132 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1132-v002-prototype` revision 1 / AST-1132 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-1132-v002-scene` revision 7 / AST-1132 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-133"></a>
## CND-133 — 손수레

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

손수레의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 프레임, 적재면, 손잡이, 바퀴
형태·치수 미정 항목: 폭, 높이, 적재 단수, 바퀴 개수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1133 v001](../assets/AST-1133-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-036-workplace` revision 3 / AST-1133 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-1133 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1133-v001-prototype` revision 1 / AST-1133 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-1133-v001-scene` revision 9 / AST-1133 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-1133-v001-scene` revision 9 / AST-1133 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-134"></a>
## CND-134 — 안전 펜스

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

안전 펜스의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1134 v001](../assets/AST-1134-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 건축 작업 구역 | PRM-036 v001 | PAN-036 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-036-workplace` revision 3 / AST-1134 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1134-v001-prototype` revision 1 / AST-1134 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-036-ast-1134-v001-scene` revision 9 / AST-1134 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-135"></a>
## CND-135 — 노출 배관 모형

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

노출 배관 모형의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 선형 본체, 연결부, 고정부
형태·치수 미정 항목: 직경, 길이, 회전 반경, 구간 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1135 v002](../assets/AST-1135-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-1135 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1135-v001-prototype` revision 1 / AST-1135 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1135-v002-prototype` revision 1 / AST-1135 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-1135-v002-scene` revision 9 / AST-1135 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-136"></a>
## CND-136 — 짧은 사다리

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

짧은 사다리의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1136 v001](../assets/AST-1136-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-1136 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1136-v001-prototype` revision 1 / AST-1136 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-1136-v001-scene` revision 9 / AST-1136 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-137"></a>
## CND-137 — 부품 상자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

부품 상자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1137 v001](../assets/AST-1137-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-1137 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1137-v001-prototype` revision 1 / AST-1137 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-1137-v001-scene` revision 9 / AST-1137 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-138"></a>
## CND-138 — 제어함

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

제어함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1138 v002](../assets/AST-1138-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 설비 작업 구역 | PRM-037 v001 | PAN-037 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-037-workplace` revision 3 / AST-1138 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1138-v001-prototype` revision 1 / AST-1138 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-1138-v001-scene` revision 3 / AST-1138 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1138-v002-prototype` revision 1 / AST-1138 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-037-ast-1138-v002-scene` revision 7 / AST-1138 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-139"></a>
## CND-139 — 낮은 지형

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

낮은 지형의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1139 v001](../assets/AST-1139-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-1139 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-1139 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1139-v001-prototype` revision 1 / AST-1139 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-1139-v001-scene` revision 9 / AST-1139 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1139-v001-scene` revision 9 / AST-1139 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-140"></a>
## CND-140 — 시료 용기

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

시료 용기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1140 v001](../assets/AST-1140-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-1140 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1140-v001-prototype` revision 1 / AST-1140 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-1140-v001-scene` revision 9 / AST-1140 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-141"></a>
## CND-141 — 휴대 측정기

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

휴대 측정기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 휴대 측정기 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1141 v001](../assets/AST-1141-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-1141 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1141-v001-prototype` revision 1 / AST-1141 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-1141-v001-scene` revision 9 / AST-1141 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-142"></a>
## CND-142 — 업무용 가방

분류: common; 기준 공간 연결 2개 → 현재 5개. 모델 제작 상태와 별개인 후보 명세다.

업무용 가방의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-017 v001](../assets/AST-017-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-017 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-017 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-059-workplace` revision 2 / AST-017 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-017 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-017-v001-scene` revision 3 / AST-017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-017-v001-prototype` revision 1 / AST-017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-017-v001-scene` revision 9 / AST-017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-017-v001-scene` revision 9 / AST-017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-059-ast-017-v001-scene` revision 9 / AST-017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-017-v001-scene` revision 9 / AST-017 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-017-v001-scene` revision 9 / AST-017 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-143"></a>
## CND-143 — 단순 식생

분류: common; 기준 공간 연결 1개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

단순 식생의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 선택 화분, 줄기, 잎 묶음
형태·치수 미정 항목: 전체 높이, 수관 폭, 잎 반복 개수, 화분 비율
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_or_meshy_review / 기존 형태·스크립트 재사용 및 단순 도형 표현부터 검토하고 자유 곡면이 핵심일 때만 승인된 Meshy 범위 검토.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1143 v002](../assets/AST-1143-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 환경 조사 지점 | PRM-038 v001 | PAN-038 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-038-workplace` revision 2 / AST-1143 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-1143 v002
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-1143 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1143-v001-prototype` revision 1 / AST-1143 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-1143-v001-scene` revision 3 / AST-1143 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1143-v001-scene` revision 3 / AST-1143 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1143-v001-scene` revision 3 / AST-1143 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1143-v002-prototype` revision 1 / AST-1143 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-038-ast-1143-v002-scene` revision 7 / AST-1143 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1143-v002-scene` revision 7 / AST-1143 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1143-v002-scene` revision 7 / AST-1143 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-144"></a>
## CND-144 — 삼각대 센서

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

삼각대 센서의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 삼각대 센서 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1144 v003](../assets/AST-1144-v003.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-1144 v003
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1144-v001-prototype` revision 1 / AST-1144 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1144-v001-scene` revision 3 / AST-1144 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1144-v002-prototype` revision 1 / AST-1144 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1144-v003-prototype` revision 1 / AST-1144 v003
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1144-v003-scene` revision 7 / AST-1144 v003

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-145"></a>
## CND-145 — 소형 관측 장치

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

소형 관측 장치의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 소형 관측 장치 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1145 v001](../assets/AST-1145-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-1145 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1145-v001-prototype` revision 1 / AST-1145 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1145-v001-scene` revision 9 / AST-1145 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-146"></a>
## CND-146 — 데이터 기록 기기

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

데이터 기록 기기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1146 v001](../assets/AST-1146-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 관측 지점 | PRM-039 v001 | PAN-039 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-039-workplace` revision 4 / AST-1146 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1146-v001-prototype` revision 1 / AST-1146 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-039-ast-1146-v001-scene` revision 9 / AST-1146 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-147"></a>
## CND-147 — 작은 재배 베드

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 재배 베드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1147 v001](../assets/AST-1147-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 재배지 | PRM-040 v001 | PAN-040 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-040-workplace` revision 3 / AST-1147 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1147-v001-prototype` revision 1 / AST-1147 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1147-v001-scene` revision 9 / AST-1147 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-148"></a>
## CND-148 — 농작물

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

농작물의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 선택 화분, 줄기, 잎 묶음
형태·치수 미정 항목: 전체 높이, 수관 폭, 잎 반복 개수, 화분 비율
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_or_meshy_review / 기존 형태·스크립트 재사용 및 단순 도형 표현부터 검토하고 자유 곡면이 핵심일 때만 승인된 Meshy 범위 검토.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1148 v002](../assets/AST-1148-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 재배지 | PRM-040 v001 | PAN-040 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-040-workplace` revision 3 / AST-1148 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1148-v001-prototype` revision 1 / AST-1148 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1148-v001-scene` revision 3 / AST-1148 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1148-v002-prototype` revision 1 / AST-1148 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1148-v002-scene` revision 7 / AST-1148 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-149"></a>
## CND-149 — 물뿌리개

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

물뿌리개의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 물뿌리개 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1149 v002](../assets/AST-1149-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 재배지 | PRM-040 v001 | PAN-040 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-040-workplace` revision 3 / AST-1149 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1149-v001-prototype` revision 1 / AST-1149 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1149-v001-scene` revision 3 / AST-1149 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1149-v002-prototype` revision 1 / AST-1149 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1149-v002-scene` revision 7 / AST-1149 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-150"></a>
## CND-150 — 농기구

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

농기구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1150 v002](../assets/AST-1150-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 재배지 | PRM-040 v001 | PAN-040 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-040-workplace` revision 3 / AST-1150 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1150-v001-prototype` revision 1 / AST-1150 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1150-v001-scene` revision 3 / AST-1150 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1150-v002-prototype` revision 1 / AST-1150 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1150-v002-scene` revision 7 / AST-1150 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-151"></a>
## CND-151 — 수확 상자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

수확 상자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1151 v001](../assets/AST-1151-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 재배지 | PRM-040 v001 | PAN-040 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-040-workplace` revision 3 / AST-1151 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1151-v001-prototype` revision 1 / AST-1151 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1151-v001-scene` revision 9 / AST-1151 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-152"></a>
## CND-152 — 관수 관

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

관수 관의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 선형 본체, 연결부, 고정부
형태·치수 미정 항목: 직경, 길이, 회전 반경, 구간 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1152 v001](../assets/AST-1152-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 재배지 | PRM-040 v001 | PAN-040 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-040-workplace` revision 3 / AST-1152 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1152-v001-prototype` revision 1 / AST-1152 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-040-ast-1152-v001-scene` revision 9 / AST-1152 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-153"></a>
## CND-153 — 재배 테이블

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

재배 테이블의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1153 v001](../assets/AST-1153-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 온실 | PRM-041 v001 | PAN-041 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-041-workplace` revision 2 / AST-1153 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1153-v001-prototype` revision 1 / AST-1153 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-1153-v001-scene` revision 9 / AST-1153 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-154"></a>
## CND-154 — 모종 트레이

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

모종 트레이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1154 v002](../assets/AST-1154-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 온실 | PRM-041 v001 | PAN-041 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-041-workplace` revision 2 / AST-1154 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1154-v001-prototype` revision 1 / AST-1154 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-1154-v001-scene` revision 3 / AST-1154 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1154-v002-prototype` revision 1 / AST-1154 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-1154-v002-scene` revision 7 / AST-1154 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-155"></a>
## CND-155 — 관수 설비

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

관수 설비의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 선형 본체, 연결부, 고정부
형태·치수 미정 항목: 직경, 길이, 회전 반경, 구간 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1155 v001](../assets/AST-1155-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 온실 | PRM-041 v001 | PAN-041 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-041-workplace` revision 2 / AST-1155 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1155-v001-prototype` revision 1 / AST-1155 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-1155-v001-scene` revision 9 / AST-1155 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-156"></a>
## CND-156 — 환경 센서

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

환경 센서의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 환경 센서 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1156 v001](../assets/AST-1156-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 온실 | PRM-041 v001 | PAN-041 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-041-workplace` revision 2 / AST-1156 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1156-v001-prototype` revision 1 / AST-1156 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-1156-v001-scene` revision 9 / AST-1156 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-157"></a>
## CND-157 — 낮은 열린 구조 프레임

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 열린 구조 프레임의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1157 v001](../assets/AST-1157-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 온실 | PRM-041 v001 | PAN-041 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-041-workplace` revision 2 / AST-1157 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1157-v001-prototype` revision 1 / AST-1157 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-041-ast-1157-v001-scene` revision 9 / AST-1157 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-158"></a>
## CND-158 — 낮은 우리 칸

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 우리 칸의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1158 v001](../assets/AST-1158-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 축사 | PRM-042 v001 | PAN-042 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-042-workplace` revision 2 / AST-1158 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1158-v001-prototype` revision 1 / AST-1158 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-042-ast-1158-v001-scene` revision 9 / AST-1158 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-159"></a>
## CND-159 — 급이통

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

급이통의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 급이통 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1159 v001](../assets/AST-1159-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 축사 | PRM-042 v001 | PAN-042 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-042-workplace` revision 2 / AST-1159 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1159-v001-prototype` revision 1 / AST-1159 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-042-ast-1159-v001-scene` revision 9 / AST-1159 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-160"></a>
## CND-160 — 물통

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

물통의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1160 v001](../assets/AST-1160-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 축사 | PRM-042 v001 | PAN-042 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-042-workplace` revision 2 / AST-1160 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1160-v001-prototype` revision 1 / AST-1160 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-042-ast-1160-v001-scene` revision 9 / AST-1160 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-161"></a>
## CND-161 — 깔짚 구역

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

깔짚 구역의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1161 v001](../assets/AST-1161-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 축사 | PRM-042 v001 | PAN-042 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-042-workplace` revision 2 / AST-1161 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1161-v001-prototype` revision 1 / AST-1161 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-042-ast-1161-v001-scene` revision 9 / AST-1161 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-162"></a>
## CND-162 — 사료 통

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

사료 통의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1162 v001](../assets/AST-1162-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 축사 | PRM-042 v001 | PAN-042 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-042-workplace` revision 2 / AST-1162 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1162-v001-prototype` revision 1 / AST-1162 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-042-ast-1162-v001-scene` revision 9 / AST-1162 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-163"></a>
## CND-163 — 청소 도구

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

청소 도구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 청소 도구 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1163 v001](../assets/AST-1163-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 축사 | PRM-042 v001 | PAN-042 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-042-workplace` revision 2 / AST-1163 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-1163 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1163-v001-prototype` revision 1 / AST-1163 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-042-ast-1163-v001-scene` revision 9 / AST-1163 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-1163-v001-scene` revision 9 / AST-1163 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-164"></a>
## CND-164 — 운반 케이지

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

운반 케이지의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 운반 케이지 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1164 v001](../assets/AST-1164-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-1164 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1164-v001-prototype` revision 1 / AST-1164 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-1164-v001-scene` revision 9 / AST-1164 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-165"></a>
## CND-165 — 먹이 그릇

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

먹이 그릇의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1165 v001](../assets/AST-1165-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 동물 관리실 | PRM-043 v001 | PAN-043 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-043-workplace` revision 3 / AST-1165 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1165-v001-prototype` revision 1 / AST-1165 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-043-ast-1165-v001-scene` revision 9 / AST-1165 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-166"></a>
## CND-166 — 작은 갑판 바닥

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 갑판 바닥의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1166 v001](../assets/AST-1166-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-1166 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1166-v001-prototype` revision 1 / AST-1166 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-1166-v001-scene` revision 9 / AST-1166 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-167"></a>
## CND-167 — 짧은 난간

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

짧은 난간의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1167 v001](../assets/AST-1167-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-1167 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1167-v001-prototype` revision 1 / AST-1167 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-1167-v001-scene` revision 9 / AST-1167 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-168"></a>
## CND-168 — 구명환

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

구명환의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 구명환 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1168 v001](../assets/AST-1168-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-1168 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-1168 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1168-v001-prototype` revision 1 / AST-1168 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-1168-v001-scene` revision 9 / AST-1168 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-1168-v001-scene` revision 9 / AST-1168 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-169"></a>
## CND-169 — 밧줄 코일

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

밧줄 코일의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 선형 본체, 연결부, 고정부
형태·치수 미정 항목: 직경, 길이, 회전 반경, 구간 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1169 v001](../assets/AST-1169-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-1169 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-1169 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1169-v001-prototype` revision 1 / AST-1169 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-1169-v001-scene` revision 9 / AST-1169 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-1169-v001-scene` revision 9 / AST-1169 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-170"></a>
## CND-170 — 계류 장치

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

계류 장치의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1170 v001](../assets/AST-1170-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 선박 갑판 | PRM-044 v001 | PAN-044 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-044-workplace` revision 3 / AST-1170 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1170-v001-prototype` revision 1 / AST-1170 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-044-ast-1170-v001-scene` revision 9 / AST-1170 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-171"></a>
## CND-171 — 조타 장치

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

조타 장치의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1171 v001](../assets/AST-1171-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 조타실 | PRM-045 v001 | PAN-045 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-045-workplace` revision 3 / AST-1171 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1171-v001-prototype` revision 1 / AST-1171 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-1171-v001-scene` revision 9 / AST-1171 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-172"></a>
## CND-172 — 계기 콘솔

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

계기 콘솔의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1172 v001](../assets/AST-1172-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 조타실 | PRM-045 v001 | PAN-045 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-045-workplace` revision 3 / AST-1172 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1172-v001-prototype` revision 1 / AST-1172 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-1172-v001-scene` revision 9 / AST-1172 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-173"></a>
## CND-173 — 운항 좌석

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

운항 좌석의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1173 v002](../assets/AST-1173-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 조타실 | PRM-045 v001 | PAN-045 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-045-workplace` revision 3 / AST-1173 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1173-v001-prototype` revision 1 / AST-1173 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-1173-v001-scene` revision 3 / AST-1173 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1173-v002-prototype` revision 1 / AST-1173 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-1173-v002-scene` revision 7 / AST-1173 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-174"></a>
## CND-174 — 항해 화면

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

항해 화면의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1174 v001](../assets/AST-1174-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 조타실 | PRM-045 v001 | PAN-045 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-045-workplace` revision 3 / AST-1174 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-1174 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1174-v001-prototype` revision 1 / AST-1174 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-1174-v001-scene` revision 9 / AST-1174 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-1174-v001-scene` revision 9 / AST-1174 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-175"></a>
## CND-175 — 통신 기기

분류: common; 기준 공간 연결 4개 → 현재 4개. 모델 제작 상태와 별개인 후보 명세다.

통신 기기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 통신 기기 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1175 v001](../assets/AST-1175-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 조타실 | PRM-045 v001 | PAN-045 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 관제실 | PRM-061 v001 | PAN-061 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-045-workplace` revision 3 / AST-1175 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-1175 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-061-workplace` revision 4 / AST-1175 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-1175 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1175-v001-prototype` revision 1 / AST-1175 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-045-ast-1175-v001-scene` revision 9 / AST-1175 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-1175-v001-scene` revision 9 / AST-1175 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-061-ast-1175-v001-scene` revision 9 / AST-1175 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-1175-v001-scene` revision 9 / AST-1175 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-176"></a>
## CND-176 — 부두 바닥

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

부두 바닥의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1176 v001](../assets/AST-1176-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-1176 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1176-v001-prototype` revision 1 / AST-1176 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-1176-v001-scene` revision 9 / AST-1176 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-177"></a>
## CND-177 — 작은 수면 가장자리

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 수면 가장자리의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1177 v001](../assets/AST-1177-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-1177 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1177-v001-prototype` revision 1 / AST-1177 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-1177-v001-scene` revision 9 / AST-1177 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-178"></a>
## CND-178 — 계류 기둥

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

계류 기둥의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1178 v001](../assets/AST-1178-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 부두 | PRM-046 v001 | PAN-046 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-046-workplace` revision 3 / AST-1178 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1178-v001-prototype` revision 1 / AST-1178 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-046-ast-1178-v001-scene` revision 9 / AST-1178 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-179"></a>
## CND-179 — 일반 운동 매트

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

일반 운동 매트의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1179 v001](../assets/AST-1179-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 체육관 | PRM-047 v001 | PAN-047 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-047-workplace` revision 2 / AST-1179 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-048-workplace` revision 2 / AST-1179 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1179-v001-prototype` revision 1 / AST-1179 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-1179-v001-scene` revision 9 / AST-1179 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-048-ast-1179-v001-scene` revision 9 / AST-1179 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-180"></a>
## CND-180 — 작은 운동 기구

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 운동 기구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1180 v001](../assets/AST-1180-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 체육관 | PRM-047 v001 | PAN-047 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-047-workplace` revision 2 / AST-1180 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1180-v001-prototype` revision 1 / AST-1180 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-1180-v001-scene` revision 9 / AST-1180 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-181"></a>
## CND-181 — 공 보관대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

공 보관대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 공 보관대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1181 v002](../assets/AST-1181-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 체육관 | PRM-047 v001 | PAN-047 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-047-workplace` revision 2 / AST-1181 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1181-v001-prototype` revision 1 / AST-1181 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-1181-v001-scene` revision 3 / AST-1181 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1181-v002-prototype` revision 1 / AST-1181 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-1181-v002-scene` revision 7 / AST-1181 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-182"></a>
## CND-182 — 물병 거치대

분류: common; 기준 공간 연결 1개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

물병 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 물병 거치대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1182 v001](../assets/AST-1182-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 체육관 | PRM-047 v001 | PAN-047 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-047-workplace` revision 2 / AST-1182 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-048-workplace` revision 2 / AST-1182 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1182-v001-prototype` revision 1 / AST-1182 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-047-ast-1182-v001-scene` revision 9 / AST-1182 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-048-ast-1182-v001-scene` revision 9 / AST-1182 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-183"></a>
## CND-183 — 스트레칭 바

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

스트레칭 바의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1183 v001](../assets/AST-1183-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-048-workplace` revision 2 / AST-1183 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1183-v001-prototype` revision 1 / AST-1183 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-048-ast-1183-v001-scene` revision 9 / AST-1183 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-184"></a>
## CND-184 — 낮은 스텝

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 스텝의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 낮은 스텝 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1184 v001](../assets/AST-1184-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-048-workplace` revision 2 / AST-1184 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1184-v001-prototype` revision 1 / AST-1184 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-048-ast-1184-v001-scene` revision 9 / AST-1184 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-185"></a>
## CND-185 — 소형 아령

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

소형 아령의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 소형 아령 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1185 v001](../assets/AST-1185-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-048-workplace` revision 2 / AST-1185 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1185-v001-prototype` revision 1 / AST-1185 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-048-ast-1185-v001-scene` revision 9 / AST-1185 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-186"></a>
## CND-186 — 자세 확인용 독립 거울

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

자세 확인용 독립 거울의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 거울 면, 테두리, 뒤쪽 지지대, 받침
형태·치수 미정 항목: 반사면 크기, 기울기, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1186 v001](../assets/AST-1186-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 운동 지도실 | PRM-048 v001 | PAN-048 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-048-workplace` revision 2 / AST-1186 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1186-v001-prototype` revision 1 / AST-1186 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-048-ast-1186-v001-scene` revision 9 / AST-1186 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-187"></a>
## CND-187 — 짧은 코트 바닥

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

짧은 코트 바닥의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1187 v001](../assets/AST-1187-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-049-workplace` revision 2 / AST-1187 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1187-v001-prototype` revision 1 / AST-1187 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-049-ast-1187-v001-scene` revision 9 / AST-1187 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-188"></a>
## CND-188 — 작은 골대 한 쌍

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 골대 한 쌍의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기둥, 연결 부재, 받침 또는 고정부
형태·치수 미정 항목: 높이, 구간 길이, 기둥 간격, 반복 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1188 v001](../assets/AST-1188-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-049-workplace` revision 2 / AST-1188 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1188-v001-prototype` revision 1 / AST-1188 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-049-ast-1188-v001-scene` revision 9 / AST-1188 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-189"></a>
## CND-189 — 공

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

공의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 공 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1189 v001](../assets/AST-1189-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-049-workplace` revision 2 / AST-1189 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1189-v001-prototype` revision 1 / AST-1189 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-049-ast-1189-v001-scene` revision 9 / AST-1189 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-190"></a>
## CND-190 — 빈 점수판

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

빈 점수판의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1190 v001](../assets/AST-1190-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 경기 구역 | PRM-049 v001 | PAN-049 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-049-workplace` revision 2 / AST-1190 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1190-v001-prototype` revision 1 / AST-1190 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-049-ast-1190-v001-scene` revision 9 / AST-1190 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-191"></a>
## CND-191 — 관계 보드

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

관계 보드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1191 v002](../assets/AST-1191-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 수사실 | PRM-050 v001 | PAN-050 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-050-workplace` revision 4 / AST-1191 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1191-v001-prototype` revision 1 / AST-1191 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-1191-v001-scene` revision 3 / AST-1191 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1191-v002-prototype` revision 1 / AST-1191 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-050-ast-1191-v002-scene` revision 7 / AST-1191 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-192"></a>
## CND-192 — 밀봉 시료 상자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

밀봉 시료 상자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1192 v001](../assets/AST-1192-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-1192 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1192-v001-prototype` revision 1 / AST-1192 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1192-v001-scene` revision 9 / AST-1192 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-193"></a>
## CND-193 — 잠금 보관함

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

잠금 보관함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1193 v001](../assets/AST-1193-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 증거 분석실 | PRM-051 v001 | PAN-051 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-051-workplace` revision 4 / AST-1193 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1193-v001-prototype` revision 1 / AST-1193 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-051-ast-1193-v001-scene` revision 9 / AST-1193 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-194"></a>
## CND-194 — 작은 판사 단상

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 판사 단상의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1194 v001](../assets/AST-1194-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 법정 | PRM-052 v001 | PAN-052 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-052-workplace` revision 1 / AST-1194 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1194-v001-prototype` revision 1 / AST-1194 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-052-ast-1194-v001-scene` revision 9 / AST-1194 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-195"></a>
## CND-195 — 진술대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

진술대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1195 v001](../assets/AST-1195-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 법정 | PRM-052 v001 | PAN-052 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-052-workplace` revision 1 / AST-1195 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1195-v001-prototype` revision 1 / AST-1195 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-052-ast-1195-v001-scene` revision 9 / AST-1195 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-196"></a>
## CND-196 — 당사자 책상

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

당사자 책상의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1196 v001](../assets/AST-1196-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 법정 | PRM-052 v001 | PAN-052 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-052-workplace` revision 1 / AST-1196 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1196-v001-prototype` revision 1 / AST-1196 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-052-ast-1196-v001-scene` revision 9 / AST-1196 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-197"></a>
## CND-197 — 방청 의자

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

방청 의자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1197 v001](../assets/AST-1197-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 법정 | PRM-052 v001 | PAN-052 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-052-workplace` revision 1 / AST-1197 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1197-v001-prototype` revision 1 / AST-1197 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-052-ast-1197-v001-scene` revision 9 / AST-1197 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-198"></a>
## CND-198 — 문서함

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

문서함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1198 v001](../assets/AST-1198-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 법정 | PRM-052 v001 | PAN-052 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-052-workplace` revision 1 / AST-1198 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1198-v001-prototype` revision 1 / AST-1198 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-052-ast-1198-v001-scene` revision 9 / AST-1198 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-199"></a>
## CND-199 — 적재 선반

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

적재 선반의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1199 v001](../assets/AST-1199-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-053-workplace` revision 2 / AST-1199 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1199-v001-prototype` revision 1 / AST-1199 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-053-ast-1199-v001-scene` revision 9 / AST-1199 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-200"></a>
## CND-200 — 팔레트

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

팔레트의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 팔레트 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1200 v001](../assets/AST-1200-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-053-workplace` revision 2 / AST-1200 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1200-v001-prototype` revision 1 / AST-1200 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-053-ast-1200-v001-scene` revision 9 / AST-1200 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-201"></a>
## CND-201 — 수동 운반차

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

수동 운반차의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 프레임, 적재면, 손잡이, 바퀴
형태·치수 미정 항목: 폭, 높이, 적재 단수, 바퀴 개수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1201 v002](../assets/AST-1201-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 물류 창고 | PRM-053 v001 | PAN-053 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-053-workplace` revision 2 / AST-1201 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1201-v001-prototype` revision 1 / AST-1201 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-053-ast-1201-v001-scene` revision 3 / AST-1201 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1201-v002-prototype` revision 1 / AST-1201 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-053-ast-1201-v002-scene` revision 7 / AST-1201 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-202"></a>
## CND-202 — 운전석

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

운전석의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 운전석 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1202 v002](../assets/AST-1202-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-1202 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1202-v001-prototype` revision 1 / AST-1202 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-1202-v001-scene` revision 3 / AST-1202 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1202-v002-prototype` revision 1 / AST-1202 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-1202-v002-scene` revision 7 / AST-1202 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-203"></a>
## CND-203 — 조작 콘솔

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

조작 콘솔의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1203 v001](../assets/AST-1203-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-1203 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1203-v001-prototype` revision 1 / AST-1203 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-1203-v001-scene` revision 9 / AST-1203 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-204"></a>
## CND-204 — 보조 좌석

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

보조 좌석의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1204 v001](../assets/AST-1204-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 운송 조종 공간 | PRM-054 v001 | PAN-054 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-054-workplace` revision 3 / AST-1204 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1204-v001-prototype` revision 1 / AST-1204 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-054-ast-1204-v001-scene` revision 9 / AST-1204 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-205"></a>
## CND-205 — 안내판

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

안내판의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1205 v001](../assets/AST-1205-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 운송 거점 | PRM-055 v001 | PAN-055 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-055-workplace` revision 2 / AST-1205 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-1205 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1205-v001-prototype` revision 1 / AST-1205 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-055-ast-1205-v001-scene` revision 9 / AST-1205 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1205-v001-scene` revision 9 / AST-1205 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-206"></a>
## CND-206 — 작은 계산기

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 계산기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1206 v001](../assets/AST-1206-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 금융 상담실 | PRM-057 v001 | PAN-057 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-057-workplace` revision 2 / AST-1206 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1206-v001-prototype` revision 1 / AST-1206 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-057-ast-1206-v001-scene` revision 9 / AST-1206 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-207"></a>
## CND-207 — 간단한 가전제품

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

간단한 가전제품의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 간단한 가전제품 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1207 v001](../assets/AST-1207-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-1207 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1207-v001-prototype` revision 1 / AST-1207 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-1207-v001-scene` revision 9 / AST-1207 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-208"></a>
## CND-208 — 공구 가방

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

공구 가방의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1208 v001](../assets/AST-1208-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 가정 수리 공간 | PRM-058 v001 | PAN-058 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-058-workplace` revision 2 / AST-1208 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1208-v001-prototype` revision 1 / AST-1208 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-058-ast-1208-v001-scene` revision 9 / AST-1208 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-209"></a>
## CND-209 — 필기구

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

필기구의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기능 본체, 손잡이 또는 입력부
형태·치수 미정 항목: 주요 길이, 손잡이 두께, 선택 고정부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1209 v001](../assets/AST-1209-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 방문 학습 공간 | PRM-059 v001 | PAN-059 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-059-workplace` revision 2 / AST-1209 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1209-v001-prototype` revision 1 / AST-1209 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-059-ast-1209-v001-scene` revision 9 / AST-1209 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-210"></a>
## CND-210 — 서버 랙

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

서버 랙의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1210 v001](../assets/AST-1210-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 서버실 | PRM-060 v001 | PAN-060 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-060-workplace` revision 3 / AST-1210 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1210-v001-prototype` revision 1 / AST-1210 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-060-ast-1210-v001-scene` revision 9 / AST-1210 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-211"></a>
## CND-211 — 케이블 트레이

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

케이블 트레이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1211 v001](../assets/AST-1211-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 서버실 | PRM-060 v001 | PAN-060 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-060-workplace` revision 3 / AST-1211 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1211-v001-prototype` revision 1 / AST-1211 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-060-ast-1211-v001-scene` revision 9 / AST-1211 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-212"></a>
## CND-212 — 관리 단말

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

관리 단말의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1212 v001](../assets/AST-1212-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 서버실 | PRM-060 v001 | PAN-060 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-060-workplace` revision 3 / AST-1212 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1212-v001-prototype` revision 1 / AST-1212 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-060-ast-1212-v001-scene` revision 9 / AST-1212 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-213"></a>
## CND-213 — 관제 콘솔

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

관제 콘솔의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체 케이스, 기능부, 조작부, 지지부
형태·치수 미정 항목: 본체 치수, 조작 높이, 기능부 위치, 개방 케이스 여부
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1213 v001](../assets/AST-1213-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 관제실 | PRM-061 v001 | PAN-061 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-061-workplace` revision 4 / AST-1213 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1213-v001-prototype` revision 1 / AST-1213 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-061-ast-1213-v001-scene` revision 9 / AST-1213 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-214"></a>
## CND-214 — 보조 단말

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

보조 단말의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1214 v001](../assets/AST-1214-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 관제실 | PRM-061 v001 | PAN-061 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-061-workplace` revision 4 / AST-1214 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1214-v001-prototype` revision 1 / AST-1214 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-061-ast-1214-v001-scene` revision 9 / AST-1214 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-215"></a>
## CND-215 — 소파

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

소파의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1215 v002](../assets/AST-1215-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 거실 | PRM-062 v001 | PAN-062 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-062-workplace` revision 2 / AST-1215 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1215-v001-prototype` revision 1 / AST-1215 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-1215-v001-scene` revision 3 / AST-1215 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1215-v002-prototype` revision 1 / AST-1215 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-1215-v002-scene` revision 7 / AST-1215 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-216"></a>
## CND-216 — 독립형 TV

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

독립형 TV의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1216 v001](../assets/AST-1216-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 거실 | PRM-062 v001 | PAN-062 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-062-workplace` revision 2 / AST-1216 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1216-v001-prototype` revision 1 / AST-1216 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-062-ast-1216-v001-scene` revision 9 / AST-1216 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-217"></a>
## CND-217 — 설비함

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

설비함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1217 v002](../assets/AST-1217-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-1217 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1217-v001-prototype` revision 1 / AST-1217 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-1217-v001-scene` revision 3 / AST-1217 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1217-v002-prototype` revision 1 / AST-1217 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-1217-v002-scene` revision 7 / AST-1217 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-218"></a>
## CND-218 — 점검 보드

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

점검 보드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1218 v002](../assets/AST-1218-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 주택 관리 공간 | PRM-063 v001 | PAN-063 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-063-workplace` revision 4 / AST-1218 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1218-v001-prototype` revision 1 / AST-1218 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-1218-v001-scene` revision 3 / AST-1218 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1218-v002-prototype` revision 1 / AST-1218 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-063-ast-1218-v002-scene` revision 7 / AST-1218 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-219"></a>
## CND-219 — 일정 보드

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

일정 보드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1219 v002](../assets/AST-1219-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 군 행정실 | PRM-065 v001 | PAN-065 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-065-workplace` revision 3 / AST-1219 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1219-v001-prototype` revision 1 / AST-1219 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-1219-v001-scene` revision 3 / AST-1219 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1219-v002-prototype` revision 1 / AST-1219 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-065-ast-1219-v002-scene` revision 7 / AST-1219 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-220"></a>
## CND-220 — 신발 정리대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

신발 정리대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 신발 정리대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1220 v001](../assets/AST-1220-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-1220 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1220-v001-prototype` revision 1 / AST-1220 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-1220-v001-scene` revision 9 / AST-1220 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-221"></a>
## CND-221 — 여행 가방

분류: common; 기준 공간 연결 2개 → 현재 3개. 모델 제작 상태와 별개인 후보 명세다.

여행 가방의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1221 v001](../assets/AST-1221-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 생활관 | PRM-066 v001 | PAN-066 v001 | 미등록 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-066-workplace` revision 2 / AST-1221 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-1221 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-1221 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1221-v001-prototype` revision 1 / AST-1221 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-066-ast-1221-v001-scene` revision 9 / AST-1221 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-1221-v001-scene` revision 9 / AST-1221 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1221-v001-scene` revision 9 / AST-1221 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-222"></a>
## CND-222 — 휴대 전화

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

휴대 전화의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 화면, 선택 지지대·받침
형태·치수 미정 항목: 화면 비율, 전체 크기, 본체 두께, 거치 방식
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1222 v001](../assets/AST-1222-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-1222 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1222-v001-prototype` revision 1 / AST-1222 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-1222-v001-scene` revision 9 / AST-1222 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-223"></a>
## CND-223 — 문서 파우치

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

문서 파우치의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1223 v001](../assets/AST-1223-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 출장 업무 공간 | PRM-068 v001 | PAN-068 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-068-workplace` revision 2 / AST-1223 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1223-v001-prototype` revision 1 / AST-1223 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-068-ast-1223-v001-scene` revision 9 / AST-1223 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-224"></a>
## CND-224 — 지도 거치대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

지도 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 지도 거치대 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1224 v002](../assets/AST-1224-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-1224 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1224-v001-prototype` revision 1 / AST-1224 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1224-v001-scene` revision 3 / AST-1224 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1224-v002-prototype` revision 1 / AST-1224 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1224-v002-scene` revision 7 / AST-1224 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-225"></a>
## CND-225 — 낮은 경계 기둥

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 경계 기둥의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 낮은 경계 기둥 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-1225 v001](../assets/AST-1225-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 안내 집결 지점 | PRM-069 v001 | PAN-069 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-069-workplace` revision 2 / AST-1225 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1225-v001-prototype` revision 1 / AST-1225 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-069-ast-1225-v001-scene` revision 9 / AST-1225 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-226"></a>
## CND-226 — 낮은 서랍장

분류: noncommon; 기준 공간 연결 0개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 서랍장의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 외곽 프레임, 선반 또는 서랍, 선택 문·손잡이
형태·치수 미정 항목: 폭·깊이·높이, 단수, 칸 수, 문·잠금 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-008 v001](../assets/AST-008-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-008 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-008-v001-scene` revision 3 / AST-008 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-008-v001-prototype` revision 1 / AST-008 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-008-v001-scene` revision 9 / AST-008 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-227"></a>
## CND-227 — 추가 하단 급지함

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

추가 하단 급지함의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 추가 하단 급지함 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-228"></a>
## CND-228 — 식물 본체

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

식물 본체의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 선택 화분, 줄기, 잎 묶음
형태·치수 미정 항목: 전체 높이, 수관 폭, 잎 반복 개수, 화분 비율
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_or_meshy_review / 기존 형태·스크립트 재사용 및 단순 도형 표현부터 검토하고 자유 곡면이 핵심일 때만 승인된 Meshy 범위 검토.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-229"></a>
## CND-229 — 책

분류: noncommon; 기준 공간 연결 0개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

책의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-011 v001](../assets/AST-011-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-011-v001-scene` revision 3 / AST-011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-011-v001-prototype` revision 1 / AST-011 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-011-v001-scene` revision 9 / AST-011 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-230"></a>
## CND-230 — 종이 낱장

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

종이 낱장의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-231"></a>
## CND-231 — 문서 묶음

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

문서 묶음의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-232"></a>
## CND-232 — 머그컵

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

머그컵의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 용기 몸통, 선택 뚜껑, 손잡이 또는 칸막이
형태·치수 미정 항목: 폭·깊이·높이, 벽 두께, 뚜껑 개폐, 분할 칸 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-233"></a>
## CND-233 — 관절형 스탠드

분류: noncommon; 기준 공간 연결 0개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

관절형 스탠드의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-014 v001](../assets/AST-014-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-014 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-014-v001-scene` revision 3 / AST-014 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-014-v001-prototype` revision 1 / AST-014 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-014-v001-scene` revision 9 / AST-014 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-234"></a>
## CND-234 — 스탠드 옷걸이

분류: noncommon; 기준 공간 연결 0개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

스탠드 옷걸이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: [AST-016 v001](../assets/AST-016-v001-unity-office-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 공용 업무 사무실 | PRM-001 v001 | PAN-001 v001 | office-shared-work v001 | 실제 제작 지원 추가(원문 기획 아님) | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-001-office` revision 5 / AST-016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-016-v001-scene` revision 3 / AST-016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-office-assistant-ast-016-v001-prototype` revision 1 / AST-016 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-001-ast-016-v001-scene` revision 9 / AST-016 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-235"></a>
## CND-235 — 협업 테이블

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

협업 테이블의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-236"></a>
## CND-236 — 포스트잇

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

포스트잇의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-237"></a>
## CND-237 — 보드 화살표

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

보드 화살표의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 판면, 테두리, 지지대, 바닥 받침
형태·치수 미정 항목: 판면 크기, 표시 높이, 지지대 간격
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-238"></a>
## CND-238 — 번호표 종이

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

번호표 종이의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-239"></a>
## CND-239 — 안내 책자

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

안내 책자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-240"></a>
## CND-240 — 바닥 방향 화살표

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

바닥 방향 화살표의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 기반 면, 외곽 두께, 선택 표면 분할
형태·치수 미정 항목: 가로·세로, 두께, 모서리 반경, 타일·구획 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-241"></a>
## CND-241 — 뱅커 램프

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

뱅커 램프의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 등 본체, 연결 암, 독립 지지대, 받침
형태·치수 미정 항목: 높이, 암 길이, 헤드 방향, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-242"></a>
## CND-242 — 찻주전자

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

찻주전자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 찻주전자 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-243"></a>
## CND-243 — 쟁반

분류: inventory_only; 기준 공간 연결 0개 → 현재 0개. 모델 제작 상태와 별개인 후보 명세다.

쟁반의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 쟁반 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 반복·대칭·명확한 부품 구조를 매개변수화해 기존 Blender 모델·제작 스크립트 재사용 우선.
재사용 조건: 같은 후보명은 동일 완성 메시 확정이 아님. 실제 치수·구조·안전 기능을 비교하고 필요시 형상 버전 분리. 색상 의도만 다르면 UV 변형 후보.

현재 제작 모델 고정 참조: 실제 모델 연결 미등록/미검증.

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 등록된 공간 후보 없음(inventory-only) | 해당 없음 | 해당 없음 | 해당 없음 | 기획 목록 보존 | 미정 |

실제 사용 원장 고정 조회 참조:
- 실제 사용 이력 미등록/미검증. 후보를 제작 완료/미사용으로 단정하지 않는다.

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-244"></a>
## CND-244 — 설교 강대상

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

설교 강대상의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1244 v002](../assets/AST-1244-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-064-workplace` revision 2 / AST-1244 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1244-v001-prototype` revision 1 / AST-1244 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-1244-v001-scene` revision 3 / AST-1244 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1244-v002-prototype` revision 1 / AST-1244 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-1244-v002-scene` revision 7 / AST-1244 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-245"></a>
## CND-245 — 펼친 성경

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

펼친 성경의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1245 v001](../assets/AST-1245-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-064-workplace` revision 2 / AST-1245 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1245-v001-prototype` revision 1 / AST-1245 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-1245-v001-scene` revision 9 / AST-1245 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-246"></a>
## CND-246 — 단순한 십자가

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

단순한 십자가의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 세로 기둥, 가로 팔, 독립 받침
형태·치수 미정 항목: 팔 길이, 기둥 두께, 받침 폭
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1246 v001](../assets/AST-1246-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-064-workplace` revision 2 / AST-1246 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1246-v001-prototype` revision 1 / AST-1246 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-1246-v001-scene` revision 9 / AST-1246 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-247"></a>
## CND-247 — 예배용 긴 의자

분류: common; 기준 공간 연결 2개 → 현재 2개. 모델 제작 상태와 별개인 후보 명세다.

예배용 긴 의자의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 긴 좌판, 등받이, 양쪽 다리, 선택 책 거치대
형태·치수 미정 항목: 좌판 길이, 좌석 높이, 등받이 각도
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1247 v001](../assets/AST-1247-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | 미등록 | 기준 v003 기획 | 미정 |
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-064-workplace` revision 2 / AST-1247 v001
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-1247 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1247-v001-prototype` revision 1 / AST-1247 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-1247-v001-scene` revision 9 / AST-1247 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1247-v001-scene` revision 9 / AST-1247 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-248"></a>
## CND-248 — 찬송가 책 거치대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

찬송가 책 거치대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1248 v001](../assets/AST-1248-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-064-workplace` revision 2 / AST-1248 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1248-v001-prototype` revision 1 / AST-1248 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-1248-v001-scene` revision 9 / AST-1248 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-249"></a>
## CND-249 — 작은 건반 악기

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 건반 악기의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 작은 건반 악기 본체, 필요 지지부
형태·치수 미정 항목: 전체 크기, 주요 실루엣, 부품 분리
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1249 v001](../assets/AST-1249-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 기독교(개신교) 예배실 — 목사 | PRM-064 v002 | PAN-064 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-064-workplace` revision 2 / AST-1249 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1249-v001-prototype` revision 1 / AST-1249 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-064-ast-1249-v001-scene` revision 9 / AST-1249 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-250"></a>
## CND-250 — 낮은 불단

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 불단의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1250 v001](../assets/AST-1250-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-1250 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1250-v001-prototype` revision 1 / AST-1250 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-1250-v001-scene` revision 9 / AST-1250 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-251"></a>
## CND-251 — 단순화한 불상

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

단순화한 불상의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 정적 좌상, 좌대
형태·치수 미정 항목: 앉은 자세, 좌대 반경, 실루엣
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_or_meshy_review / 조형물 실루엣과 존중하는 정적 표현이 핵심. 단순 Blender 형태부터 검토하고 필요시 승인된 Meshy 범위 안에서 형태 생성 검토.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1251 v001](../assets/AST-1251-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-1251 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1251-v001-prototype` revision 1 / AST-1251 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-1251-v001-scene` revision 9 / AST-1251 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-252"></a>
## CND-252 — 방석

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

방석의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 좌면, 등받이 또는 쿠션, 다리 또는 받침
형태·치수 미정 항목: 좌석 높이, 폭, 깊이, 등받이·팔걸이·바퀴 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1252 v001](../assets/AST-1252-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-1252 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1252-v001-prototype` revision 1 / AST-1252 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-1252-v001-scene` revision 9 / AST-1252 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-253"></a>
## CND-253 — 낮은 경전 독서대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

낮은 경전 독서대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1253 v001](../assets/AST-1253-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-1253 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1253-v001-prototype` revision 1 / AST-1253 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-1253-v001-scene` revision 9 / AST-1253 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-254"></a>
## CND-254 — 목탁

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

목탁의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 받침 또는 손잡이
형태·치수 미정 항목: 직경, 높이, 종교별 고유 실루엣
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1254 v002](../assets/AST-1254-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-1254 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1254-v001-prototype` revision 1 / AST-1254 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-1254-v001-scene` revision 3 / AST-1254 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1254-v002-prototype` revision 1 / AST-1254 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-1254-v002-scene` revision 7 / AST-1254 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-255"></a>
## CND-255 — 향로

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

향로의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 받침 또는 손잡이
형태·치수 미정 항목: 직경, 높이, 종교별 고유 실루엣
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1255 v001](../assets/AST-1255-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-1255 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1255-v001-prototype` revision 1 / AST-1255 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-1255-v001-scene` revision 9 / AST-1255 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-256"></a>
## CND-256 — 작은 연꽃 장식

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

작은 연꽃 장식의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 받침 또는 손잡이
형태·치수 미정 항목: 직경, 높이, 종교별 고유 실루엣
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1256 v001](../assets/AST-1256-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 불교 법당 — 스님 | PRM-070 v001 | PAN-070 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-070-workplace` revision 3 / AST-1256 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1256-v001-prototype` revision 1 / AST-1256 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-070-ast-1256-v001-scene` revision 9 / AST-1256 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-257"></a>
## CND-257 — 미사 제대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

미사 제대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1257 v001](../assets/AST-1257-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-1257 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1257-v001-prototype` revision 1 / AST-1257 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1257-v001-scene` revision 9 / AST-1257 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-258"></a>
## CND-258 — 독서대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

독서대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 상판, 지지 프레임, 다리 또는 하부장
형태·치수 미정 항목: 상판 가로·세로, 작업 높이, 두께, 하부장·서랍 유무
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1258 v002](../assets/AST-1258-v002.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-1258 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1258-v001-prototype` revision 1 / AST-1258 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1258-v001-scene` revision 3 / AST-1258 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1258-v002-prototype` revision 1 / AST-1258 v002
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1258-v002-scene` revision 7 / AST-1258 v002

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-259"></a>
## CND-259 — 십자고상

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

십자고상의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 십자가 프레임, 정적 인체 조형, 독립 받침
형태·치수 미정 항목: 인체 실루엣, 십자가 비율, 독립 지지대
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_or_meshy_review / 조형물 실루엣과 존중하는 정적 표현이 핵심. 단순 Blender 형태부터 검토하고 필요시 승인된 Meshy 범위 안에서 형태 생성 검토.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1259 v001](../assets/AST-1259-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-1259 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1259-v001-prototype` revision 1 / AST-1259 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1259-v001-scene` revision 9 / AST-1259 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-260"></a>
## CND-260 — 성작

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

성작의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 받침 또는 손잡이
형태·치수 미정 항목: 직경, 높이, 종교별 고유 실루엣
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1260 v001](../assets/AST-1260-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-1260 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1260-v001-prototype` revision 1 / AST-1260 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1260-v001-scene` revision 9 / AST-1260 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-261"></a>
## CND-261 — 전례서

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

전례서의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 표지 또는 바탕, 종이 블록, 선택 제본·거치부
형태·치수 미정 항목: 가로·세로, 두께, 펼침 각도, 묶음 수
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1261 v001](../assets/AST-1261-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-1261 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1261-v001-prototype` revision 1 / AST-1261 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1261-v001-scene` revision 9 / AST-1261 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

<a id="cnd-262"></a>
## CND-262 — 촛대

분류: noncommon; 기준 공간 연결 1개 → 현재 1개. 모델 제작 상태와 별개인 후보 명세다.

촛대의 역할을 높은 3/4 시점과 축소 표시에서도 실루엣으로 구분.
구성: 본체, 받침 또는 손잡이
형태·치수 미정 항목: 직경, 높이, 종교별 고유 실루엣
기획 치수: 미정(null) / 장면 축척·기존 재사용본 치수 확인 후 결정
도구 검토: blender_direct / 대칭·반복·명확한 부품을 Blender로 구성하고 공통 부품을 재사용.
재사용 조건: 종교 상징의 의미와 형상을 구분. 단순 십자가와 십자고상을 동일 모델로 합치지 않음. 긴 의자 공통 프레임은 검토 가능하나 종교별 장식은 별도.

현재 제작 모델 고정 참조: [AST-1262 v001](../assets/AST-1262-v001.md).

| 전체 후보 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 연결 근거 | 계획 수량 |
|---|---|---|---|---|---|
| 천주교 성당 — 신부님 | PRM-071 v001 | PAN-071 v001 | 미등록 | 기준 v003 기획 | 미정 |

실제 사용 원장 고정 조회 참조:
- [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) / `pan-071-workplace` revision 2 / AST-1262 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-ast-1262-v001-prototype` revision 1 / AST-1262 v001
- [asset-usages.json](../../machine/catalog/asset-usages.json) / `use-workplaces-pan-071-ast-1262-v001-scene` revision 9 / AST-1262 v001

모델별 상세 부품·실제 치수·색상 칸·검수·전체 Unity/Blender 사용 수량은 각 고정 에셋 명세와 위 원장의 최신/과거 revision에서 조회한다. 이번 유료 Meshy·이미지 생성 호출0·크레딧0, 기존 비용은 별도, 토큰 배분은 미측정이다.

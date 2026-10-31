# 기존3물건 체험 재사용 판단 v001

최신 지시의 “더 나아지는 경우 개선하고 아니면 그대로 사용”에 따라 이전30개 소스를 검토했습니다. 이번 검토에서는30개를 유지하고 추가 변경은 하지 않았습니다. 기존의 구체적 업무 흐름과 상태·revision·비동기 처리를 보존하는 편이 실익이 큽니다. 검토 자체로 실제 실행 검수 상태를 승격하지 않습니다.

운동·수사·운송·재무·수리의 새10개는 관찰·드래그 분류·순서·눈금·문서 인계가 구별됩니다. 은행출납은 전표와 영수증이 같은 폼이어도 다른 산출물의 금액·요청번호를 대조하므로 유지합니다. 이전 파일럿10개는 사진 산출물,조립/구성판,눈금과타이머,관찰과대화 등 실제동작을 재사용합니다. 사무실10개는 문서 준비→출력→보관/인계 범위의 체험으로 유지하며,이 공통 출력 흐름이 각 직업의 전체업무나모든특수상황을완성한것으로표현하지않습니다.

|공간|직업|고정 시나리오·버전|현재3단계|판단|
|---|---|---|---|---|
|PAN-048|물리치료사|career-net-369-experience @ v002|inspect → sequence → tune|유지|
|PAN-049|운동경기심판|career-net-391-experience @ v002|sequence → inspect → form|유지|
|PAN-050|경찰관|career-net-359-experience @ v002|sort → sequence → form|유지|
|PAN-051|범죄과학수사관|career-net-10064-experience @ v002|form → inspect → sort|유지|
|PAN-052|검사|career-net-199-experience @ v002|sort → inspect → form|유지|
|PAN-054|버스운전기사|career-net-372-experience @ v002|inspect → schedule → form|유지|
|PAN-055|택배원|career-net-371-experience @ v002|form → sort → sequence|유지|
|PAN-056|은행출납사무원|career-net-255-experience @ v002|sort → form → form|유지|
|PAN-057|증권분석가|career-net-239-experience @ v002|inspect → tune → form|유지|
|PAN-058|컴퓨터설치·수리원|career-net-466-experience @ v002|inspect → sort → assemble|유지|
|PAN-002|행사기획자|career-net-951-experience @ v002|form → schedule → form|유지|
|PAN-019|가구조립 및 검사원|career-net-1152-experience @ v002|sort → tune → assembly|유지|
|PAN-035|사서|career-net-268-experience @ v002|inspect → dialogue → sort|유지|
|PAN-027|광고디자이너|career-net-285-experience @ v002|inspect → poster → form|유지|
|PAN-053|물류관리사|career-net-215-experience @ v002|sort → load → sequence|유지|
|PAN-041|원예기술자|career-net-963-experience @ v002|plant → tune → timer|유지|
|PAN-025|제과사 및 제빵사|career-net-172-experience @ v002|tune → tray → timer|유지|
|PAN-030|사진작가|career-net-310-experience @ v002|stage → tune → photo|유지|
|PAN-031|방송연출가|career-net-301-experience @ v002|cable → tune → timer|유지|
|PAN-020|방송장비(H/W)설치 및 수리원|career-net-1147-experience @ v002|inspect → repair → sort|유지|
|PAN-001|국제무역사무원|career-net-208-experience @ v002|table → print → handoff|유지|
|PAN-001|데이터 라벨러|career-net-10118-experience @ v002|sort → print → handoff|유지|
|PAN-001|법률사무원|career-net-252-experience @ v002|table → print → handoff|유지|
|PAN-001|베타테스터|career-net-1432-experience @ v002|table → print → handoff|유지|
|PAN-001|빅 데이터 전문가|career-net-10032-experience @ v002|table → print → handoff|유지|
|PAN-001|사이버교육운영자|career-net-462-experience @ v002|schedule → print → handoff|유지|
|PAN-001|속기사|career-net-459-experience @ v002|field → print → handoff|유지|
|PAN-001|시장 및 여론조사전문가|career-net-230-experience @ v002|table → print → handoff|유지|
|PAN-001|전문비서|career-net-378-experience @ v002|schedule → print → handoff|유지|
|PAN-001|회계사무원|career-net-258-experience @ v002|table → print → handoff|유지|

[항목별 판단 근거·남은범위](../../machine/catalog/career-prior-workflow-audit-v001.json)에 전체30개를 기록했습니다. 원본·이전 빌드·다른 에이전트 소스를 변경하지 않았습니다. 최종 빌드의 프레이밍·입력·오류·재시도·특수 분기·통신 검수는 별도 실행 기록을 확인해야 합니다.


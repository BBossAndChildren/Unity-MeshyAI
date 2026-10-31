# 직업체험 시나리오 구현용 요청 v002

아래 요청에서 대상 시나리오를 정한 뒤 새 구현 채팅에 사용한다. 이 파일은 구현 완료 결과물이 아니다.

```text
D:\github\Unity-MeshyAI의 파노라마 기반 직업체험을 구현해줘.

먼저 로컬 AGENTS.md와 다음 최신 자료를 읽어줘.
- docs/human/jobs/panorama-career-experience-spec-v002.md
- docs/human/jobs/career-experience-scenarios-v002.md
- docs/machine/catalog/career-experience-scenarios-v002.json
- docs/machine/catalog/career-minigame-types-v001.json
- docs/machine/catalog/panorama-career-experience-layouts-v002.json
- docs/machine/catalog/occupation-place-competency-reference-v001.json
- 기존 assets.json, scene-assemblies.json, builds.json과 실제 사용 이력

대상 시나리오: career-net-253-office-documents
위 ID는 최초 사무실 예시다. 다른 직업을 구현할 때는 v002에 존재하는 시나리오 ID로 바꾼다.

대상 하나를 실제 3D 장면에서 플레이 가능하게 구현하고 검증한 뒤 결과를 먼저 보고해줘. 기존 구현과 Unity 프로젝트가 있으면 먼저 조사해 재사용·보완하고, 같은 기능을 다른 위치에 중복 작성하거나 다른 세션 결과를 덮어쓰지 마.

파노라마 → 공통/비공통 에셋 → 대상 직업 → 물건 3개 → 기본 게임과 특수 분기의 연결을 따라간다. 원본 업무·핵심역량과 게임 각색을 구별하고, 원본과 기존 직업 ID·버전을 보존해줘. 파노라마 이미지 위의 버튼만 누르는 방식이 아니라 실제 3D 물건을 선택해서 조작하는 장면을 만든다.

전체 552개는 기획 초안이다. 기본 연습 데이터는 엔진 확인용이며 모든 전문 문제의 완성본이 아니다. 대상의 professional_context·source_basis와 원본을 읽고, 직업에 맞는 과제와 모델을 구체화한다. 원본 장소 밖 제안·장비 변형 요구·needs_subject_selection을 확인하고, 종교 전통이나 전문 업무의 정답을 추정해 확정하지 마. 꼭 필요한 주제 선택이나 내용 확인은 구체적인 대안을 제시해 물어봐.

기존 첫 사무실 사례에는 별도의 상세 명세와 구현 프롬프트가 있으므로 이를 우선한다. 그 외 직업은 시나리오의 steps·configuration·special_variants·review_issues를 확인하고 3D 바인딩과 직업별 문제 데이터를 보완한다. 아직 명세뿐인 20종을 구현 완료 모듈이라고 가정하지 마.

단계 선행 조건, 요청 revision 변경, 중복 클릭, 오답·재시도, 완료 후 입력, 전체 초기화, 키보드·터치 대체 조작을 구현하고 실제로 확인한다. 바뀐 요청에 과거 정답·완료 이벤트가 통과하지 않아야 한다. 특수 상황은 해당 시나리오 물건 3개와 UI를 재사용한다.

원본 모델·색상 팔레트·공용 재질·삼각형 예산과 버전 규칙을 유지한다. 상호작용 변형으로 모델 파일이 바뀌면 새 버전으로 보존하고, 파노라마와 모든 사용 후보·실제 사용처 명세를 갱신한다. 실제 사용의 원장은 기존 계약대로 유지한다.

Unity 편집 프로젝트와 WebGL 전달 결과를 분리하고, Unity/웹에서 실제 확인한 것만 실행 검증 완료로 보고한다. 설치나 모듈이 없으면 준비 가능한 부분을 끝내고 미검증 범위를 밝힌다. 추가 유료 Meshy·이미지 생성은 이 프롬프트만으로 승인된 것으로 해석하지 말고, 기존 승인 범위가 실제 적용되는지 확인해줘.

결과 보고에는 플레이 방법·프로젝트와 빌드 경로·실제 모델 버전·사용 수량·삼각형·비용·검수 근거·미검증 항목을 포함한다. 목표는 대상 시나리오 하나의 실행 완료이며 552개 전체 구현 완료를 주장하지 마.
```

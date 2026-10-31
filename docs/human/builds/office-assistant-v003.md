# office-assistant-v003 — 사무보조원 3D 체험
# 사무보조원 3D 직업체험 — 실행과 편집

권장 실행본은 `office-assistant-v003`이다. 다른 551개 직업은 생성·구현하지 않았다.

저장소 루트에서 서버 실행:

```powershell
python -m http.server 8173 --bind 127.0.0.1 --directory unity/webgl/builds
```

브라우저에서 <http://127.0.0.1:8173/office-assistant-v003/>를 연다. `index.html` 더블클릭 실행은 검증 대상이 아니다. 빌드는 압축하지 않아 별도 압축 헤더가 필요 없으며 `.wasm`은 `application/wasm`으로 제공한다. 외부 배포 URL은 아직 없다.

1. 3D 모니터에서 자료·날짜, 부수, 보관처를 질문하고 요청 요약을 전송해 동료 확인을 받는다.
2. 문서 날짜 11월 1일을 11월 2일로 고치고 저장한다.
3. 사무실로 돌아가 복합기에서 DOC-001 최신 저장 revision과 2부를 골라 출력한다.
4. 뒤쪽 수납장의 회의자료 칸에 보관하고 제목·날짜·부수·위치를 정확히 요약해 동료 확인을 받는다.

R 또는 전체 초기화에서 기본 2부 / 변경 요청 연습을 고른다. 변경 연습에서는 저장 직후 요청 r2가 되어 3부로 바뀌고 확인이 해제된다. 모니터에서 다시 확인한 다음 출력한다. EX-008 인계는 필수, EX-010 이력 복구 연습은 미구현이다.

마우스 클릭·터치로 실제 물건 표면을 선택한다. 8픽셀 넘는 드래그는 카메라 회전이며 선택으로 처리하지 않는다. 수납장 가운데는 업무석에 가릴 수 있으므로 드러난 위쪽·옆면을 선택하거나 카메라를 돌린다. UI 라벨은 네 번째 조작 물건이 아니다. 배경 모니터는 선택 대상이 아니다.

키보드는 1·2·3 또는 닫힌 UI의 Tab으로 물건을 고르고 Enter로 연다. UI 안에서는 Tab·↑↓로 초점을 옮기고 Enter·Space로 누른다. Esc로 UI를 닫고 ←→↑↓로 카메라 회전, +−로 확대한다. P는 일시정지·계속, R은 초기화 대화상자다. 일시정지는 출력도 멈춘다. 시간 경쟁·적성 진단 점수는 없다.

Unity Hub에서 `unity/projects/OfficeAssistant-v001`을 Unity 6000.3.26f1으로 연다. `Assets/Scenes/OfficeAssistant.unity`를 열고 Play한다. WebGL Build Support가 필요하며 외부 유료 서비스나 런타임 GLB 로더 의존성은 없다. 메뉴 `Office Experience/Prepare Scene`은 프로젝트의 이 체험 장면을 다시 구성하므로 수동 편집 전 별도 보존한다. 빌드 메뉴는 기존 index.html이 있으면 덮어쓰지 않는다. CLI에서 새 build_id를 지정한다:

```powershell
& $UnityEditor -batchmode -quit -nographics -projectPath (Resolve-Path unity/projects/OfficeAssistant-v001) -executeMethod OfficeBuild.Build -buildTarget WebGL -officeBuildId office-assistant-v004 -logFile office-build-v004.log
```

`$UnityEditor`는 설치된 Unity.exe 경로로 지정한다. 전달 ZIP은 소스·Blender·Unity 편집 프로젝트를 포함하지 않으며 site/ 아래에 전체 실행본을 넣었다. 프로젝트 Assets·Packages·ProjectSettings와 .meta는 별도로 보존한다.
## 빌드·검증 근거
- Unity 6000.3.26f1 / WebGL Development Build. 51288640바이트, 48.78초, 빌드 오류 0·경고 0.
- 편집 프로젝트: `unity/projects/OfficeAssistant-v001`
- 출력: `unity/webgl/builds/office-assistant-v003`
- 소스 커밋: `308507ce0429cc85106035ee3fac367db6756c1d`; 작업 트리는 기존 변경 포함 dirty. 최종 소스 해시 목록 `docs/machine/evidence/office-assistant-v001/source-files-sha256.json`. 커밋만으로 재현 가능하다고 주장하지 않는다.
- 참고: PAN-001 v001 / PRM-001 v001 / office-shared-work v001. 기존 직업·장소 사실 검증·기획 승인 상태는 변경하지 않았다.
- 구성: AST-020 v003 원본 GLB를 Blender에서 다시 열어 Unity FBX 적용본으로 변환. 메시·팔레트·모델 원본 보존.
- 모델 집계: 17개 구성 에셋 버전, 30개 인스턴스, 4,308삼각형. 새 3D 물체 0개. 목표 5,000 대비 692삼각형 여유. UI 글자/화면 경계는 모델 메시 예산과 분리.
- 모델 공용 재질 1개, PNG 1장(v001, 2508×2508), 원본·Unity 복사본 SHA-256 일치. UI 폰트는 별도 OFL 폰트. 모델에 문서 글자나 새 이미지 텍스처를 넣지 않았다.

| 에셋 버전 | 수량 | 삼각형/개 | 장면 합계 |
|---|---:|---:|---:|
| AST-001 v002 | 1 | 220 | 220 |
| AST-002 v001 | 1 | 108 | 108 |
| AST-003 v001 | 2 | 792 | 1584 |
| AST-004 v001 | 2 | 60 | 120 |
| AST-005 v001 | 2 | 48 | 96 |
| AST-006 v001 | 2 | 12 | 24 |
| AST-007 v001 | 2 | 12 | 24 |
| AST-008 v001 | 2 | 84 | 168 |
| AST-009 v001 | 1 | 144 | 144 |
| AST-010 v001 | 3 | 308 | 924 |
| AST-011 v001 | 3 | 72 | 216 |
| AST-012 v001 | 2 | 76 | 152 |
| AST-013 v001 | 2 | 12 | 24 |
| AST-014 v001 | 2 | 96 | 192 |
| AST-015 v001 | 1 | 60 | 60 |
| AST-016 v001 | 1 | 168 | 168 |
| AST-017 v001 | 1 | 84 | 84 |

AST-020 v003은 위 구성의 소스 컨테이너이며 추가 수량·삼각형으로 합산하지 않는다. 프리팹 정의도 장면 인스턴스와 중복 합산하지 않는다. 전체 후보·각 에셋 실제 사용 조회는 [AST-001-v002-unity-office-v001](../assets/AST-001-v002-unity-office-v001.md), [AST-002-v001-unity-office-v001](../assets/AST-002-v001-unity-office-v001.md), [AST-003-v001-unity-office-v001](../assets/AST-003-v001-unity-office-v001.md), [AST-004-v001-unity-office-v001](../assets/AST-004-v001-unity-office-v001.md), [AST-005-v001-unity-office-v001](../assets/AST-005-v001-unity-office-v001.md), [AST-006-v001-unity-office-v001](../assets/AST-006-v001-unity-office-v001.md), [AST-007-v001-unity-office-v001](../assets/AST-007-v001-unity-office-v001.md), [AST-008-v001-unity-office-v001](../assets/AST-008-v001-unity-office-v001.md), [AST-009-v001-unity-office-v001](../assets/AST-009-v001-unity-office-v001.md), [AST-010-v001-unity-office-v001](../assets/AST-010-v001-unity-office-v001.md), [AST-011-v001-unity-office-v001](../assets/AST-011-v001-unity-office-v001.md), [AST-012-v001-unity-office-v001](../assets/AST-012-v001-unity-office-v001.md), [AST-013-v001-unity-office-v001](../assets/AST-013-v001-unity-office-v001.md), [AST-014-v001-unity-office-v001](../assets/AST-014-v001-unity-office-v001.md), [AST-015-v001-unity-office-v001](../assets/AST-015-v001-unity-office-v001.md), [AST-016-v001-unity-office-v001](../assets/AST-016-v001-unity-office-v001.md), [AST-017-v001-unity-office-v001](../assets/AST-017-v001-unity-office-v001.md), [AST-020-v003-unity-office-v001](../assets/AST-020-v003-unity-office-v001.md)에 보존했다.

## 실제 실행 결과

Unity Editor Play Mode(렌더링 없는 batchmode)에서 실제 Awake·Update·출력 타이머·일시정지·완료·초기화를 실행했고 세 MeshCollider의 노출 표면에 레이가 닿았다. WebGL 화면은 실제 Chrome/HTTP/SwiftShader에서 검사했다.

| 실제 WebGL UI 사례 | 결과 |
|---|---|
| actual_unity_scene | pass |
| camera_drag_not_click | pass |
| sequence_violation | pass |
| missing_request_information | pass |
| date_error_and_retry | pass |
| copies_file_revision_errors | pass |
| printing_duplicate_click_and_pause | pass |
| classification_error | pass |
| handoff_required_and_base_complete | pass |
| completed_reclick | pass |
| full_reset | pass |
| keyboard_request_change_reconfirmation | pass |
| changed_request_3_copies | pass |
| emulated_touch_selection_and_dialogue | pass |
| reset_during_print | pass |

WebGL 안에서 동일 C# 판정 코드의 독립 검증 10건도 통과했다. 브라우저 오류 0개. 마우스 경로·키보드 요청 재확인/출력·에뮬레이션 터치 선택/질문/수정 저장을 실행했다. 상태를 건너뛰는 테스트용 완료 명령은 사용하지 않았다.

근거: `docs/machine/evidence/office-assistant-v001/webgl-ui-acceptance.json`, `unity-editor-play.json`, `unity-csharp-acceptance.json`, `unity-scene.json`, `blender-reimport.json`, `final-model-measurements.json`, `palette-audit.json`, `office-assistant-v003-build-result.json` 및 화면 캡처. 브라우저 테스트 드라이버는 프로젝트 `Tests/webgl-smoke.cjs`.

검토 중 v001의 후면 카메라를 수정하고 v003의 표지·키보드 초점을 보완했다. 중간 검사 시 수납장 중심 가림, 너무 빠른 자동 Tab 입력, 검사 드라이버의 부수 증가 횟수 착오를 기록하고 검사 좌표·입력 간격·기대값을 바로잡았다. 중간 실패 기록 attempt01~03은 보존했고 최종 결과와 혼동하지 않는다.

## 미구현·미검증

- EX-010 기록 복구 연습은 미구현이다. 표시한 편집 이력만으로 EX-010 완료를 주장하지 않는다.
- MG-001·003·005·008 및 EX-007·008은 이 사무실 시나리오 범위만 구현했다. 나머지 14종과 일반화된 20종 전체는 완료가 아니다. 다른 551개 직업은 변경하지 않았다.
- 실제 모바일 기기, Safari·Firefox, GPU별 성능·드로콜·모든 확대/축소 상태, 보조기기/화면낭독기, 외부 HTTPS 배포 URL은 미검증이다. 작은 960×600 뷰포트 렌더와 에뮬레이션 터치는 별도 범위다.
- 원본 직업·장소 사실 확인과 사용자 기획 승인은 실행 검증과 별개이며 기존 미검증/승인 대기 상태를 유지한다.
- 유료 Meshy·이미지 생성 호출 0, 이번 Meshy 크레딧 0. 모델별 토큰 배분은 미측정이다.

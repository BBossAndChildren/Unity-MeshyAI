# 사무보조원 3D 직업체험 — 실행과 편집

권장 실행본은 `office-assistant-v005`이다. 다른 551개 직업은 생성·구현하지 않았다.

저장소 루트에서 서버 실행:

```powershell
python -m http.server 8173 --bind 127.0.0.1 --directory unity/webgl/builds
```

브라우저에서 <http://127.0.0.1:8173/office-assistant-v005/>를 연다. `index.html` 더블클릭 실행은 검증 대상이 아니다. 빌드는 압축하지 않아 별도 압축 헤더가 필요 없으며 `.wasm`은 `application/wasm`으로 제공한다. 외부 배포 URL은 아직 없다.

1. 3D 모니터에서 자료·날짜, 부수, 보관처를 질문하고 요청 요약을 전송해 동료 확인을 받는다.
2. 문서 날짜 11월 1일을 11월 2일로 고치고 저장한다.
3. 사무실로 돌아가 복합기에서 DOC-001 최신 저장 revision과 2부를 골라 출력한다.
4. 뒤쪽 수납장의 회의자료 칸에 보관하고 제목·날짜·부수·위치를 정확히 요약해 동료 확인을 받는다.

R 또는 전체 초기화에서 기본 2부 / 변경 요청 연습을 고른다. 변경 연습에서는 저장 직후 요청 r2가 되어 3부로 바뀌고 확인이 해제된다. 모니터에서 다시 확인한 다음 출력한다. EX-008 인계는 필수, EX-010 이력 복구 연습은 미구현이다.

마우스 클릭·터치로 실제 물건 표면을 선택한다. 8픽셀 넘는 드래그는 카메라 회전이며 선택으로 처리하지 않는다. 수납장 가운데는 업무석에 가릴 수 있으므로 드러난 위쪽·옆면을 선택하거나 카메라를 돌린다. UI 라벨은 네 번째 조작 물건이 아니다. 배경 모니터는 선택 대상이 아니다.

키보드는 1·2·3 또는 닫힌 UI의 Tab으로 물건을 고르고 Enter로 연다. UI 안에서는 Tab·↑↓로 초점을 옮기고 Enter·Space로 누른다. Esc로 UI를 닫고 ←→↑↓로 카메라 회전, +−로 확대한다. P는 일시정지·계속, R은 초기화 대화상자다. 일시정지는 출력도 멈춘다. 시간 경쟁·적성 진단 점수는 없다.

Unity Hub에서 `unity/projects/OfficeAssistant-v001`을 Unity 6000.3.26f1으로 연다. `Assets/Scenes/OfficeAssistant.unity`를 열고 Play한다. WebGL Build Support가 필요하며 외부 유료 서비스나 런타임 GLB 로더 의존성은 없다. 메뉴 `Office Experience/Prepare Scene`은 프로젝트의 이 체험 장면을 다시 구성하므로 수동 편집 전 별도 보존한다. 빌드 메뉴는 기존 index.html이 있으면 덮어쓰지 않는다. CLI에서 새 build_id를 지정한다:

```powershell
& $UnityEditor -batchmode -quit -nographics -projectPath (Resolve-Path unity/projects/OfficeAssistant-v001) -executeMethod OfficeBuild.Build -buildTarget WebGL -officeBuildId office-assistant-v006 -logFile office-build-v004.log
```

`$UnityEditor`는 설치된 Unity.exe 경로로 지정한다. 전달 ZIP은 소스·Blender·Unity 편집 프로젝트를 포함하지 않으며 site/ 아래에 전체 실행본을 넣었다. 프로젝트 Assets·Packages·ProjectSettings와 .meta는 별도로 보존한다.

물건 선택 시 확대·종이 팝업으로 전환하며 Esc로 전체 사무실로 복귀한다. 검증 상세는 `docs/human/builds/office-assistant-v005.md`.

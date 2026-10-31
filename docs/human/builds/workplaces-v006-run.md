# Unity-MeshyAI workplaces-v006 실행 안내

71개 파노라마를 참고해 만든 71개 실제 3D 공간을 선택하고 탐색하는 Unity WebGL 결과물입니다. 사무보조원 직접 작업 체험 1개와 Unity↔React 기록 수신 예제를 포함합니다. 다른 직업 551개 초안의 체험 구현을 뜻하지 않습니다. 사무 체험의 기본2부 출력·요청 변경3부 출력·분류·인계를 구현했으며, 선택되지 않은 이력 복구 연습(EX-010)은 미구현입니다.

## 로컬 실행

ZIP 전체를 한 폴더에 풉니다. Python 3가 있으면 이 README가 있는 폴더에서 다음 명령을 실행합니다.

```powershell
python -m http.server 8000 --bind 127.0.0.1
```

브라우저에서 http://127.0.0.1:8000/site/ 를 엽니다. 사무 체험의 요청·이벤트·결과·중단 원장을 함께 보려면 http://127.0.0.1:8000/site/receiver/ 를 엽니다. index.html을 더블클릭하는 file:// 실행은 지원하지 않습니다. 첫 로드에는 약 58 MB의 전송과 WebAssembly 초기화가 필요합니다.

## 조작

- 공간 탐색: 왼쪽 목록의 공간을 선택합니다. 드래그 또는 방향키로 회전하고, 휠 또는 +/−로 확대합니다. P/Esc로 일시정지합니다.
- 사무 체험: 공용 업무 사무실에서 시작합니다. 모니터·복합기·수납장 3개를 실제 클릭/터치하거나 안내된 키보드 조작으로 선택합니다. 문서 필드 편집·인쇄 설정·문서 묶음 분류·인계를 직접 수행합니다.
- 작업 화면의 닫기/Esc는 초안과 진행을 유지하며 공간으로 복귀합니다. 전체 종료는 종료 동작을 사용합니다. 초기화는 확인 후 새 실행을 시작합니다.
- React 예제는 같은 origin의 Unity iframe에서 받은 이벤트를 ID로 중복 제거하고 순서대로 표시합니다. 통신 미확인을 성공으로 기록하지 않습니다. 새로고침 전 실행과 새 실행의 원장을 구분합니다.

## 서버 설정

Build/와 receiver/를 포함한 site/ 전체 경로를 보존합니다. .wasm은 application/wasm, .js는 JavaScript, .data는 application/octet-stream으로 제공합니다. 이 빌드는 Unity 전송 압축을 사용하지 않아 별도 gzip/Brotli Content-Encoding 설정이 필요하지 않습니다. 모든 경로는 같은 origin에서 서비스합니다. React와 글꼴은 패키지에 포함되어 있습니다.

## 확인한 환경과 범위

Windows Chrome에서 HTTP로 실제 Unity WebGL을 실행했습니다. 1440×900 및 900×600 표시, 71개 공간의 진입·표시·회전과 각 장면의 실제 삼각형·재질·텍스처를 확인했습니다. 터치는 Chrome 에뮬레이션으로 검사했습니다. 자세한 결과·판정·남은 항목은 BUILD.md 및 manifest.json의 evidence 경로를 참고합니다.

물리 모바일 기기, Safari/Firefox, 하드웨어 GPU별 성능, HTTPS 외부 서버는 미검증입니다. 화면 움직임 줄이기 옵션은 시작·일시정지 화면에서 설정합니다. 기본 전환 시간은 편집 프로젝트의 OfficeDirectExperience / Transition Seconds에서 조정합니다. 로컬 생성본과 이번 ZIP은 외부에 배포하지 않았습니다.

## 편집용 원본

이 ZIP에는 실행 사이트만 포함합니다. 편집용 Unity 프로젝트는 정식 저장소의 unity/projects/OfficeAssistant-v001에 있고, Blender/GLB 원본·버전·제작 기록과 전체 사용 후보/배치 이력은 저장소의 docs 및 meshy/models에 보존되어 있습니다. BUILD.md와 manifest.json의 저장소 상대 경로는 D:/github/Unity-MeshyAI 기준입니다.

글꼴 출처·SIL OFL은 licenses/에, React·ReactDOM·scheduler 라이선스는 site/receiver/licenses/에 포함합니다.

Unity Editor의 업무 GUI 직접 조작은 앱 접근 승인 시간 초과로 미검증입니다. 네이티브 장면·메시 검수와 실제 WebGL 업무 GUI 검수는 각각 별도 보고서로 제공합니다.

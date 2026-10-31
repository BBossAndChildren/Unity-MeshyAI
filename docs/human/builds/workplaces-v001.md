# workplaces-v001 — 대표 공간 중간 검증 빌드

기존 사무실과 새 대표 공간4개를 선택해 탐색하는 실제 Unity WebGL 중간 빌드다. 71개 전체 전달 완료본이 아니며 직접 작업형 개선·공통 응답 프로토콜 완성본으로 해석하지 않는다.

프로젝트: `unity/projects/OfficeAssistant-v001`. 출력: `unity/webgl/builds/workplaces-v001`. 기존 office-assistant-v001~v005와 ZIP은 덮어쓰지 않았다.

## 실제 빌드

| 항목 | 값 |
|---|---|
| Unity | 6000.3.26f1 |
| 결과 | Succeeded |
| 일시 | 2026-10-31T05:29:33.2601891+09:00 |
| Unity 보고 크기 | 51596909바이트 |
| 오류·경고 | 0 / 0 |
| Unity 빌드 시간 | 50.2167987초 |
| 소스 HEAD | `308507ce0429cc85106035ee3fac367db6756c1d` |
| 소스 상태 | 기존·이번 미커밋 변경 포함, 원본 보존 |
| 외부 의존성 | 설치된 Unity WebGL 지원, 신규 유료 서비스 없음 |

[실제 빌드 근거](../../machine/evidence/workplaces-v001/build-result.json). 빌드 시간은 모델링·작성·검수 전체 시간이 아니다.

## 포함 공간·정량 근거

| 공간 | 실제 Unity 장면 | 삼각형 | 메시 | 재질·텍스처 | 근거 |
|---|---|---:|---:|---|---|
| 공용 업무 사무실(PAN-001) | `Assets/Scenes/OfficeAssistant.unity` | 4308(기존 GLB/Unity 기록) | 30(기존 기록) | 1 / 1(기존 기록) | 기존 v005 장면 재사용; 이번 중간 웹 보고의 공간별 pass 대상에서 제외 |
| PAN-002 | `Assets/Scenes/Workplaces/PAN-002.unity` | 2552 | 72 | 1 / 1 | [PAN-002-unity-scene.json](../../machine/evidence/workplaces-v001/PAN-002-unity-scene.json) |
| PAN-003 | `Assets/Scenes/Workplaces/PAN-003.unity` | 3764 | 68 | 1 / 1 | [PAN-003-unity-scene.json](../../machine/evidence/workplaces-v001/PAN-003-unity-scene.json) |
| PAN-004 | `Assets/Scenes/Workplaces/PAN-004.unity` | 2136 | 32 | 1 / 1 | [PAN-004-unity-scene.json](../../machine/evidence/workplaces-v001/PAN-004-unity-scene.json) |
| PAN-005 | `Assets/Scenes/Workplaces/PAN-005.unity` | 1832 | 58 | 1 / 1 | [PAN-005-unity-scene.json](../../machine/evidence/workplaces-v001/PAN-005-unity-scene.json) |

개별 구성 에셋의 수량·실제 위치는 위 Unity 조사 JSON과 asset-usages 원장 등록 후 각 에셋 명세에서 조회한다. 조립 부모와 구성 소품은 중복 합산하지 않는다.

## 이번 실제 HTTP 실행 검수

[Chrome HTTP 실행 보고](../../machine/evidence/workplaces-v001/http-webgl-acceptance-attempt003.json). 실행 환경은 Windows·Chrome·SwiftShader다. 공간별 실제 표시·삼각형·공용 재질/텍스처 수를 대조했고 마우스 공간 선택과 카메라 드래그를 수행했다.

| 사례 | 결과 |
|---|---|
| PAN-002_entry_geometry_palette | pass |
| PAN-003_entry_geometry_palette | pass |
| PAN-004_entry_geometry_palette | pass |
| PAN-005_entry_geometry_palette | pass |
| camera_drag | pass |

이 pass는 기록된 진입·표시·정량·드래그 범위다. 대표 공간이 통과했다고 다른66개 신규 공간에 pass를 복사하지 않는다. Unity Editor에서 장면을 생성·조사한 것과 Play Mode 실행 검수는 구별한다.

첫 HTTP 연결 실패와 별도 터치 시도 타임아웃 기록도 같은 evidence 폴더에 보존했다. 이 결과로 실제 모바일 또는 터치 입력 통과를 주장하지 않는다. 직접 체험의 자유 입력·분류 드래그·종료 프로토콜·React 통합·실제 모바일·브라우저별 성능·드로콜·외부 HTTPS 배포는 이 빌드에서 미검증이다.

## 실행

저장소 루트에서 다음을 실행한 뒤 [로컬 실행](http://127.0.0.1:8178/workplaces-v001/)을 연다.

```powershell
python -m http.server 8178 --bind 127.0.0.1 --directory unity/webgl/builds
```

`index.html` 더블클릭 실행은 검수 대상이 아니다. 빌드는 압축하지 않았으므로 별도 압축 헤더가 필요 없고 `.wasm`은 `application/wasm`으로 제공한다. 왼쪽 공간 목록에서 탐색 가능한 방을 고르고 드래그·방향키로 회전, 휠·+/−로 확대한다.

이 중간 빌드의 전달 ZIP은 아직 등록하지 않았다. 최종 전체 빌드의 ZIP·manifest·실행 안내는 별도 고유 build_id로 보존한다. 이번 Meshy·유료 이미지 생성 호출0, 크레딧0. 토큰·비용 배분과 승인 잔여 크레딧은 미측정/미확인이다.

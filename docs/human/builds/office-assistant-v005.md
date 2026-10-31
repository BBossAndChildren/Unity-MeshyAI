# 사무보조원 v005 — 선택한 물건 확대·종이 팝업

물건을 고르면 선택한 실제 3D 모델로 카메라가 부드럽게 가까워지고, 해당 작업을 종이·팝업 화면에서 수행한다. 모니터는 요청 메시지와 문서 편집, 복합기는 출력 설정과 나오는 용지, 수납장은 분류함과 인계 카드를 표시한다. Esc 또는 돌아가기로 전체 사무실과 30개 메시를 복원한다.

실행: <http://127.0.0.1:8173/office-assistant-v005/>

```powershell
python -m http.server 8173 --bind 127.0.0.1 --directory unity/webgl/builds
```

실제 물건의 노출된 표면을 클릭·터치하거나 1·2·3과 Enter로 연다. 팝업에서는 Tab·↑↓·Enter, P 일시정지, R 전체 초기화를 사용할 수 있다. 확대한 상태에서는 뒤쪽 사무실 클릭·드래그를 막는다. 초기 화면의 드래그·화살표·휠 카메라 조작은 유지한다.

편집 프로젝트는 `unity/projects/OfficeAssistant-v001`, 장면은 `Assets/Scenes/OfficeAssistant.unity`, 출력은 `unity/webgl/builds/office-assistant-v005`, 전달 ZIP은 `unity/webgl/packages/office-assistant-v005.zip`이다. 이전 v001~v003 실행본·ZIP·검증 기록은 보존했다.

## 구현·검증 범위

- Unity 6000.3.26f1, 실제 WebGL Development Build. 신규 외부 의존성 없음. v004 중간본의 프레임 잔상은 배경 전용 카메라의 전체 화면 지우기로 수정했다. 이 카메라는 메시·콜라이더가 없는 표시용이며 조작 물건을 늘리지 않는다.
- 기존 3개 상호작용 물건·콜라이더를 재사용했다. 복제 모델·NPC·새 3D 용지를 추가하지 않았다. 문서·용지·폴더는 화면 UI이다.
- 전체 로드 장면은 17개 구성 에셋 버전·30개 메시·4,308삼각형, 공용 재질 1개·palette.png 1장(2508×2508)이다. 모델 FBX·팔레트 해시는 v003과 동일하다. 조립 부모·프리팹 정의는 중복 집계하지 않는다.
- 확대 중에는 선택 모델 1개만 표시한다. 모니터 48, 복합기 144, 수납장 60삼각형이며 닫으면 전체 4,308삼각형의 사무실로 돌아간다. 원본 메시·재질·색상은 변경하지 않았다.
- Chrome/HTTP/SwiftShader에서 실제 3D 선택·카메라 확대·원상 복귀·팝업, 기본 2부·변경 3부, 날짜·파일·부수·분류 오류, 인계, 출력 중 중복 클릭·일시정지, 완료 후 재클릭·초기화를 실행했다. 키보드 경로와 에뮬레이션 터치도 확인했다.
- EX-010 복구 연습은 계속 미구현이다. 실제 모바일 기기, Safari/Firefox, 하드웨어 GPU 성능·드로콜, 화면낭독기, 외부 HTTPS 배포는 미검증이다. 다른 551개 직업과 나머지 유형은 확장하지 않았다.
- 이번 Meshy·유료 이미지 생성 호출 0, 크레딧 0. 실제 토큰 배분은 도구 미제공으로 null/미측정이다.

## 실행 근거

실제 WebGL UI 16건, WebGL 내부 C# 독립 사례 10건 통과. Unity Editor Play Mode도 실제 실행했다. 빌드 오류 0·경고 0, 13.0초.

| WebGL UI 사례 | 결과 |
|---|---|
| actual_unity_scene | pass |
| camera_drag_not_click | pass |
| sequence_violation | pass |
| selected_item_closeup_and_popup | pass |
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

근거: `docs/machine/evidence/office-assistant-v005/unity-scene.json`, `unity-editor-play.json`, `webgl-ui-acceptance.json`, `office-assistant-v005-build-result.json`과 캡처. 원본 GLB 재가져오기·UV 검사는 파일 해시가 같은 [이전 최종 검수](office-assistant-v003.md)의 근거를 재사용했다.

[모니터 확대](../../machine/evidence/office-assistant-v005/monitor-questions.png) · [복합기 용지](../../machine/evidence/office-assistant-v005/copier-printing-paper.png) · [수납장 팝업](../../machine/evidence/office-assistant-v005/cabinet-popup.png)

개별 에셋 전체 후보와 실제 사용 이력은 [이전 보고의 18개 개별 명세 링크](office-assistant-v003.md)를 유지하고 각 명세에 v005 최신 원장 revision 3을 덧붙였다. 원장은 `docs/machine/catalog/asset-usages.json`이며 최신 수량만 합산한다.

# office-ten-v007 — 모니터 안 한글 문서 미리보기

컴퓨터를 가리던 큰 종이 사각형을 제거하고 기존 AST-005-0 모니터의 검은 화면 안에 문서를 표시합니다. 오른쪽에서 수정한 내용이 즉시 모니터에 반영되고 긴 한글 문장은 줄바꿈됩니다. 모니터 테두리와 받침대는 가리지 않습니다. 기존 의자 방향과 작업 패널 투명도는 유지합니다.

## 실제 확인

- Unity6000.3.26f1 빌드 성공, 오류0·경고0. 원본17소품/30배치/4308모델삼각형과 공용모델재질1개/팔레트PNG1장은 유지했습니다. 동적 UI폰트 글자 메시는 모델 측정과 구분합니다.
- 실제 HTTP208사례에서 물리모니터 선택, 화면 안 한글 표시·모니터 면 안 배치, 한글 문장 입력/줄바꿈/수정, Esc후글자숨김·30모델복귀, 재열기 초안유지4건을 확인했습니다.
- 실제 KoreanUI.otf 문자표에서 현대 한글11172자가 모두 있는지 검사했습니다. 별도 OS폰트 설치 없이 기존 내장폰트를 재사용합니다.
- 사무실 전체10종/공통17건 검수는 기존v003 증거로 보존합니다. 이번 빌드의 전체업무 재검수로 복제하지 않습니다. 물리 OS/모바일 IME조합입력은 별도 인증한 것이 아니며 실제 CUA입력기로 완성형 한글 문장 입력을 확인했습니다.

[실행](http://127.0.0.1:8178/office-ten-v007/) · [ZIP](../../../unity/webgl/packages/office-ten-v007.zip)

[실제 화면·입력 검수](../../machine/evidence/office-ten-v007/browser/visual-qa.json) · [모니터 화면](../../machine/evidence/office-ten-v007/browser/monitor-preview.jpg) · [한글 입력 화면](../../machine/evidence/office-ten-v007/browser/korean-live.jpg) · [폰트 검사](../../machine/evidence/office-ten-v007/korean-font-coverage.json) · [소스 보존](../../machine/evidence/office-ten-v007/built-source-index.json)

## 전달·출처

편집 프로젝트 unity/projects/OfficeAssistant-v001, 장면 Assets/Scenes/OfficeTen.unity. 실제 모니터 화면 원본 명세는 meshy/models/blender/AST-020/v001/processing/build_office.py의 monitor 함수이며 표시 면0.48×0.28m를 실제 FBX bounds 단위에 맞춰 사용합니다. 모델·팔레트와 기존 빌드/ZIP을 보존했습니다. 새 모델/유료호출0, 실측토큰미제공null.

실제 빌드 소스 308507ce0429cc85106035ee3fac367db6756c1d에 미커밋 변경을 포함하며58개 파일 보존 기록이 있습니다. 빌드 중 다른 작업이 변경한 별도 workplace-registry의 정확한 컴파일본은 미검증으로 표시했습니다. 이 사무실 런타임은 해당 공간 목록을 사용하지 않으며 업무코드/프로토콜/직업JSON 불변 해시와 실제 산출물 실행을 확인했습니다. Packages는 변경하지 않았습니다.

ZIP의 site 폴더에서 python -m http.server 8080 실행 후 /receiver/ 또는 /를 여세요. manifest는18개 고정에셋·팔레트1개를 해소합니다. 폰트라이선스와 React/ReactDOM/scheduler 라이선스를 포함하며 모델/Unity편집 원본은 포함하지 않습니다. Unity6 TextMesh 공식API: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TextMesh.html


## ZIP 재실행 검증 완료

ZIP을 별도 폴더에 다시 풀어 HTTP로 실행하고, 실제 모니터 선택과 화면 안 한글 미리보기 표시를 확인했습니다. ZIP CRC와 site 파일 12개의 SHA-256도 모두 일치합니다.

- ZIP: 29,301,582바이트
- SHA-256: `6c544074718d45cd0702085e13a60b459010f4b4955eaa3d6d547e7435f2a507`
- [압축 해제본 실제 실행 기록](../../machine/evidence/office-ten-v007/browser/package-http.json)
- [압축 해제본 실제 화면](../../machine/evidence/office-ten-v007/browser/package-monitor.jpg)

v007 원본 실행에서는 모니터 미리보기와 한글 입력·수정·줄바꿈·닫기/재열기를 확인했습니다. ZIP 재실행에서는 초기값으로 모니터 열기·화면 안 한글 표시를 확인했습니다. 전체 10종 업무의 새 회귀검수나 물리 키보드의 OS별 IME 조합 검증을 뜻하지 않습니다.

## 알려진 한글 입력 문제 — 사용자 보고

2026-10-31 사용자가 v007을 ChatGPT/IAB에서 실행했을 때 실제 한글 입력이 되지 않는 문제를 직접 보고했습니다. 이전 검수는 완성형 한글 문자열을 삽입한 방식으로 입력·표시를 확인한 결과이며, OS 입력기의 한글 조합이 동작한다는 증거는 아닙니다.

기존 완성형 문자열 입력·수정·줄바꿈 검수 결과와 원본 증거는 당시 확인한 범위로 보존합니다. 사용자 환경의 한글 입력 문제는 이와 구분하여 알려진 문제로 기록하며, 별도 OS·모바일 IME 조합 입력의 정상 동작을 주장하지 않습니다.

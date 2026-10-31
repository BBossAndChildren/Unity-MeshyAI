# office-ten-v003 — 사무실 직업체험10종

기존 사무실 AST-020 v006을 재사용한 신규10종의 기본 업무입니다. 모니터에서 고유 문제를 처리하고 복합기로 최신 결과물을 출력한 다음 수납장에 분류·인계합니다. 기존 사무보조원253과71공간 빌드는 보존했습니다.

| 직업 ID | 직업 | 업무 |
|---|---|---|
| career-net-208 | 국제무역사무원 | 포장명세와 상업송장 수량 맞추기 |
| career-net-10118 | 데이터 라벨러 | 고객문의 문장에 라벨 붙이기 |
| career-net-252 | 법률사무원 | 가상 접수표와 첨부표지 대조하기 |
| career-net-1432 | 베타테스터 | 경계값 테스트에서 오류 보고서 작성하기 |
| career-net-10032 | 빅 데이터 전문가 | 중복 기록을 제거하고 요약 집계하기 |
| career-net-462 | 사이버교육운영자 | 실시간 수업 운영표 배치하기 |
| career-net-459 | 속기사 | 가상 발언 기록의 전사문 교정하기 |
| career-net-230 | 시장 및 여론조사전문가 | 설문 표본 할당표 맞추기 |
| career-net-378 | 전문비서 | 이동 시간을 고려해 회의 일정 배치하기 |
| career-net-258 | 회계사무원 | 영수증과 지출 장부 대조하기 |

## 실행과 전달

- [전달 ZIP](../../../unity/webgl/packages/office-ten-v003.zip)
- [현재 로컬 React 직업 선택·시작](http://127.0.0.1:8178/office-ten-v003/receiver/) · [단독 실행](http://127.0.0.1:8178/office-ten-v003/)
- Unity 편집 프로젝트: unity/projects/OfficeAssistant-v001, 장면 Assets/Scenes/OfficeTen.unity.
- WebGL 출력: unity/webgl/builds/office-ten-v003. ZIP에는 site 전체·manifest.json·BUILD.md·README.md·라이선스를 넣었습니다. 편집 프로젝트와 모델 원본은 별도입니다.

## 실제 확인

Unity6000.3.26f1 실제 빌드 성공, 오류0·경고0, 엔진 보고 55926530bytes. 17개 소품 버전·30인스턴스·4308삼각형, 공용 흰색 재질1개·팔레트PNG1장(2508×2508)입니다. 부모조립을 중복 합산하지 않습니다. 새 모델·유료 Meshy·이미지 호출0, 실측 토큰은 제공되지 않아 null입니다.

- Native Play Mode10종: 시나리오 선택·형상·3물건 연결. batchmode-nographics이므로 네이티브 업무 GUI는 미검증입니다.
- 실제 HTTP WebGL10종: 직업별 편집, 실제 드래그, 오류 복구, 출력 용지, 분류·인계·900×600화면. 원본 이벤트에서 시도·실수·반복 집계도 대조했습니다.
- Unity→React 공통17건: 10종 시작/종료, 제어오류 비가산, 늦은 리스너·중복·재전달, 종료 응답 제한시간·재시도, 반복 오류 판정, 출력 중 초기화·종료와3초 지연 관찰. 공통 사례를 모든 직업의 개별 통과로 복제하지 않습니다.
- 추가2건: 462 단일 터치 에뮬레이션·키보드 분류. 459는900화면 Tab/ShiftTab/Esc 초안 유지도 확인했습니다.
- 요청 객체를 게임 이벤트로 수집한 검수 하네스 관찰1건은 원본 실패로 보존했습니다. 실제 eventId/type/sequence가 있는144개 이벤트를 별도로 검사해 buildId·재전달 원문 일치를 확인했습니다.

## 증거와 한계

- [검수 요약](../../machine/evidence/office-ten-v003/acceptance-summary.json)
- [Native 선택·형상](../../machine/evidence/office-ten-v003/unity-editor-play.json)
- [첫5종 HTTP](../../machine/evidence/office-ten-v003/browser-first5/acceptance.json) · [나머지5종 HTTP](../../machine/evidence/office-ten-v003/browser-last5/last-five-actual-http.json)
- [공통 통신 결과](../../machine/evidence/office-ten-v003/browser-common/protocol-http-acceptance.json)
- [실제 포함 소스57개 보존 색인](../../machine/evidence/office-ten-v003/built-source-index.json)
- [사용 원장](../../machine/catalog/asset-usages.json) · [직업별 명세](../jobs/office-ten-experiences-v004.md)

물리 모바일 장치·네이티브 업무 GUI는 미검증입니다. 힌트UI·요청 변경·미선택 특수분기는 이번 범위에 없습니다. 분류 결과는 대상칸 안 문서명·부수와 원본의 목적지 참조로 표시하며 별도3D종이 이동은 구현하지 않았습니다. 가상 교육 문제로 직업 적성·전문 자격을 진단하지 않습니다. Unity 시작 로그 SearchDatabase 엔진 예외는 보존했고 실제 빌드와 선택 검수는 성공했습니다.

v001 드래그 실패·v002 동일 오류 반복 집계 실패 중간본을 보존했습니다. 최종 v003은 해당 재현을 다시 통과했습니다. 다른 채팅의 별도10종 작업도 보존했습니다. 이후 공유 소스 변경과 이 빌드의 실제 포함 소스는57개 보존본으로 구별합니다.


## 전달본 최종 확인

ZIP 29211801bytes, SHA-256 56d5e6697f8f15db9599bc76a6a22d864e63341e305f8146d7ab767d952700c7. 전체12개 site파일 해시·ZIP CRC가 일치하고18개 에셋·팔레트1개 참조를 해소했습니다. 새 폴더에 압축해제한 실제 HTTP에서 React직업선택208·시작응답·3D모니터열기·종료응답2건을 확인했습니다. [패키지 실행 증거](../../machine/evidence/office-ten-v003/package-http/package-http-boot.json) · [계약·링크 등1885개 검사](../../machine/evidence/office-ten-v003/final-contract-review.json). BUILD.md와 manifest의 저장소 자료 참조는 정식 저장소 기준이며 ZIP단독 실행 절차는 README.md에 있습니다.

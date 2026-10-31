# 직업 기본 체험 10개 — career-pilot-v007

물류관리사에서 보이는 칸 안에 놓아도 1단계가 실패하던 배치 판정을 수정했다. 실제 포인터가 놓인 목적지 칸에 맞춰지고, 목적지 이름·다음 단계 안내와 선택 후 4·5·6키 배치를 추가했다. 점유된 칸으로 다시 배치할 때 선택이 바뀌던 문제도 수정했다. [재현·수정 보고](logistics-placement-fix-v001.md).

Unity 6000.3.26f1 실제 WebGL 빌드 성공, 오류 0·경고 0, 출력 56569394바이트. 1~3단계 가장자리 드롭·오답 거절·재배치·최종 completed 응답을 실제 HTTP Chrome에서 확인했다. 새 v007에서 10직업의 30작업면·10최종완료와 공통 입력/생명주기 27건을 통과했다. 물류 표적 검수 9건도 별도로 통과했다. ZIP 무결성과 압축 해제 HTTP 검수는 외부 최종 검수 기록에 남긴다.

## 실행

ZIP의 site/를 HTTP 서버로 제공하고 receiver/를 연다. 단독 화면은 index.html이다. file:// 더블클릭은 지원하지 않는다. 로컬 실행 주소는 http://127.0.0.1:8178/career-pilot-v007/receiver/ 이며 외부 공개 배포는 하지 않았다.

물류관리사 1단계에서 A는 북부, B는 동부, C는 남부 칸에 놓고 저장한다. 저장 후 닫기·Esc로 복귀하여 2. 팔레트를 선택한다. 2단계 저장 후 3. 수동 운반차에서 배송 순서를 완료한다. 화면 위 체험 종료·기록 받기로 최종 결과를 받을 수 있다.

## 포함 범위와 출처

기존 10개 가상 기본 직업과 사무 보조 비교 장면을 포함한다. 공식 등록 프로젝트는 unity/projects/OfficeAssistant-v001, 실제 고정 빌드·편집 사본은 unity/projects/CareerPilotTen-v001이다. 동일 모델 ID·버전·GUID를 보존한 같은 논리 프로젝트의 빌드 사본이며 독립 에셋 등록이 아니다. 원래 프로젝트의 다른 병행 변경과 같다고 주장하지 않는다. 소스 커밋 308507ce0429cc85106035ee3fac367db6756c1d 이후 미커밋 상태이며 실제 입력 30파일 해시는 [source snapshot](../../machine/evidence/career-pilot-v007/source-snapshot-after-build.json)에 기록했다.

고정 에셋 78버전(구성 67·조립 source 11), 실제 구성 배치 141개, 11공간, 최대 4,308삼각형, 공용 palette.png v001 한 장과 공용 재질을 재사용했다. 조립 부모를 배치 수량에 중복 합산하지 않았다. 에셋·Blender·GLB·팔레트 신규 수정 0, Meshy 호출·크레딧 0, 실제 대화 토큰·순수 노력시간은 미측정 null이다. 라이선스는 site/licenses에 포함한다.

## 검증 한계

이번 수정은 교육용 UI 배치와 안내다. 실제 화물 물리 적재, 전문 자격·업무 정확성 판정을 뜻하지 않는다. Windows Chrome SwiftShader에서 실행했고 실물 모바일 기기·다른 브라우저·Native GUI는 미검증이다. 이전 Native 장면 검수는 과거 v005 증거로만 남기며 v007 실행 pass로 복사하지 않는다. 모델 파일이 바뀌지 않아 Blender 재실행도 하지 않았다. 선택형 특수 분기·나머지 직업 전체 구현을 포함하지 않는다.

## 전달 최종 검사

실제11공간 HTTP 표시와 장면이동1건, ZIP 전체16파일 CRC·바이트·해시와 압축해제 파일일치, 별도 압축해제 HTTP의 단독화면·터치배치 저장·React 결과수신3건을 통과했다. [패키지 무결성](../../machine/evidence/career-pilot-v007/package-integrity.json), [압축해제 실행](../../machine/evidence/career-pilot-v007/package-http-r002/package-http-acceptance.json).

[ZIP](../../../unity/webgl/packages/career-pilot-v007.zip): 29420575바이트, SHA-256 `f611d31f7fd4d06175fff79220f035f938aa924a03c912a83034416529aa2f87`. ZIP안 BUILD.md는 패키징 시점의 불변 스냅샷이며 이 단락의 후속 검수 결과는 저장소 원장에 추가했다.

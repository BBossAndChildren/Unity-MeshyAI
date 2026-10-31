# 직업 체험 전달 v002

이번 전달은 테스트 링크 하나와 ZIP 두 개입니다. 이전 v001 전달 자료는 보존합니다.

1. [테스팅 화면](http://127.0.0.1:8212/career-suite-test-v009/): 공간·직업 선택, 과정 기록, 효과음 108종의 확보 상태와 34종 미리듣기.
2. 실제 연동용 `career-suite-integration-v005.zip`: 외부 프론트에서 ID로 시작하는 WebGL, 효과음 파일, 배경색 설정, AI 선택용 카탈로그.
3. `career-integration-listing-v004.zip`: 전체 체험 설명·ID, 효과음 목록·연결 상태, 프론트/백엔드 어댑터·연동 규격·검수 기록.

두 ZIP의 `UPDATES.md`는 [업데이트 및 적용 안내](career-suite-update-v002.md)와 동일합니다. 최종 ZIP 경로·해시·검수 결과는 아래 전달 확정 기록으로 추가합니다.

## 내용과 범위

71개 공간, 552개 시나리오 ID, 공간별 555개 체험 조합을 포함합니다. 성직자 체험의 등록된 세 공간은 각각 유지합니다. [전체 설명 JSON](../../machine/catalog/career-experience-descriptions-v001.json), [CSV](../../machine/catalog/career-experience-descriptions-v001.csv), [사람용 설명 목록](../jobs/career-experience-descriptions-v001.md)에서 실제 입력·분류·배치·조절·인계 작업을 확인할 수 있습니다.

효과음은 요청된 108종 중 34종의 실제 파일을 포함합니다. 30종은 게임 동작 소스에 연결되고, 4종은 미리듣기·재사용 자료입니다. 74종은 미생성이며, 최신 추가 비용 없음 지시 이후 유료 생성·업그레이드는 수행하지 않았습니다. 실제 재생 검수와 파일·소스 연결 상태는 별도 기록합니다.

추가 471개 기본 미션과 원래 모든 전문 업무의 완성은 구분합니다. 원래 특수분기 554건, 전체 555개 조합의 완주 검수, 실제 서비스 인증·저장·lease·복구는 미완료 또는 미검증입니다. 기존 [실행 한계](career-suite-runtime-review-v001.md)를 함께 확인합니다.

## 실행

로컬 테스트 링크는 이 컴퓨터의 서버가 실행되는 동안 사용할 수 있습니다. ZIP은 압축을 풀고 HTTP 서버로 실행합니다. ZIP 루트에서 `node site/frontend/server.mjs --root .`를 실행한 뒤 `http://localhost:8194/site/frontend/integration-example.html?roomId=PAN-050`을 열면 동봉 React 예제와 로컬 저장 ACK 수신기를 확인할 수 있습니다. 로컬 수신기는 실제 운영 백엔드가 아닙니다.

프론트는 정확한 `buildId + roomId + scenarioId + scenarioVersion`을 사용합니다. 배경색은 React `backgroundColor` 또는 `client.setPresentation({ backgroundColor: '#F4F1EA' })`로 지정합니다. 효과음은 첫 게임 화면 조작 후 브라우저에서 활성화되며 API 키 없이 동봉 파일을 재생합니다.

Unity 편집 프로젝트와 원본 모델은 전달 WebGL ZIP에 포함하지 않습니다. 모델·팔레트는 변경하지 않았고, 427개 고정 에셋 버전과 73개 실제 장면에 놓인 구성품 1,101개를 재사용합니다. 기존 형상·Blender 검수는 재실행하지 않았습니다. 이번 Meshy·이미지 생성 호출과 크레딧은 0, 실제 토큰 사용량은 미측정입니다.

## 이번 빌드에서 실제 확인한 범위

테스트 v009: 경찰관 PAN-050의 3개 실제 물건 선택, 카드 드래그 여섯 번, 한국어 필드 입력, 전체 세 업무 완료(제출 3회·실수 0회·재시도 0회), 배치 상태 보존·저장 결과 글자 간격·일시정지/종료 정리·로컬 원본 37개 수신을 확인했습니다. [검수 근거](../../machine/evidence/career-suite-test-v009/audio-pan050-ui/summary-v001.json).

실제 연동 v005: React 시작/종료, 전체 캔버스 배경색과 방 전환 유지, 불투명한 패널 가독성, 실제 효과음과 종료 취소, 로컬 원본 29개/ACK 29개를 확인했습니다. [검수 근거](../../machine/evidence/career-suite-integration-v005/react-audio/actual-react-audio-background.json). 색상은 GPU 렌더링에서 한 채널 1의 반올림 차이가 있을 수 있습니다.

34개 효과음 파일 전체의 Web Audio 디코드·시작·종료는 중간 v003에서 확인했고, 최종 빌드와의 파일·재생기 동일성을 검증했습니다. 모든 555개 업무의 완주나 모든 효과음의 업무별 재생 검수를 뜻하지 않습니다. 기존 v006의 71개 방 대표 시작 검수는 이전 버전의 별도 근거로 보존합니다.

## 전달 확정

- [테스팅 실행](http://127.0.0.1:8212/career-suite-test-v009/)
- [실제 연동용 WebGL ZIP](../../../unity/webgl/packages/career-suite-integration-v005.zip): 31,267,874바이트, SHA-256 1e0e6c4c9cad4ccc5bf1ebec0b4dd1c0b878c7db16c2e20906193f0b976298f9.
- [별도 리스팅·프론트/백엔드 자료 ZIP](../../../unity/webgl/packages/career-integration-listing-v004.zip)

실제 연동 ZIP의 CRC와 압축 해제한 77개 파일의 바이트를 대조했습니다. 추출본을 HTTP에서 직접 실행해 React 시작/종료, 물건 3개 연결, 전체 크림색 배경, 원본 이벤트 5개/ACK 5개와 콘솔 오류 0개를 확인했습니다. [추출본 실행 증거](../../machine/evidence/career-suite-integration-v005/react-extracted-zip/actual-react-iframe.json).

리스팅에는 555개 체험 설명 JSON/CSV, 효과음 108종 전체 상태·해시·사용 위치, 프론트/백엔드 어댑터·타입, 원본 검수 기록과 UPDATES.md가 포함됩니다. 실제 효과음 바이너리는 WebGL ZIP에 있어 리스팅 ZIP에 중복하지 않습니다.

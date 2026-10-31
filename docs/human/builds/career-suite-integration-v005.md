# career-suite-integration-v005

Unity 6000.3.26f1 WebGL 빌드 성공: 47,970,006바이트, 오류 0건·경고 0건. 빌드 시각: 2026-10-31T17:10:15.8264875+09:00.

71개 공간, 73개 장면, 552개 시나리오 ID / 555개 공간별 조합, 고정 에셋 427버전. 기존 모델과 팔레트를 재사용했습니다.

[전달 안내](career-suite-v002.md), [업데이트 및 사용법](career-suite-update-v002.md), [기존 실행 한계](career-suite-runtime-review-v001.md)를 확인하세요.

소스 기준 커밋은 308507ce0429cc85106035ee3fac367db6756c1d이며 미커밋 변경이 있습니다. 재현 기준은 docs/machine/evidence/career-suite-integration-v005/built-source.json 및 보존된 실제 스냅샷입니다. 빌드 자체 성공과 실제 브라우저 검증 범위는 구분합니다.

555개 전체 완주, 원래 특수분기 554건, 실제 운영 인증·저장·lease 연동은 완료·검증되지 않았습니다. 과거 빌드의 검수 결과를 이번 빌드 전체 성공으로 승계하지 않습니다.

HTTP 서버와 WebAssembly/WebGL2 지원 브라우저가 필요합니다. 포함된 로컬 ACK 예제는 Node.js 22 이상에서 실행합니다. .wasm MIME은 application/wasm, .data는 application/octet-stream으로 제공합니다. 외부 자격증명이나 유료 런타임 생성 API는 필요하지 않습니다.

효과음 34종과 555개 실제 작업 설명이 동봉됩니다. 효과음 74종은 미생성입니다. 이번 모델·이미지 생성 호출과 Meshy 크레딧은 0이며 실제 토큰은 미측정입니다.

## 실제 검수

React 시작/종료, 크림색·파란색 전체 캔버스 배경, 불투명 안내 패널, PAN-050→PAN-051 방 전환 후 표시 설정 유지, 실제 효과음 시작/종료와 종료 후 반복음 취소·늦은 이전 실행 음 차단을 확인했습니다. 원본 이벤트 29개·로컬 ACK 29개·전송 대기 0개. 전체 업무 완주 및 운영 백엔드 검증과 구별합니다. 파란색 #DCECF4는 캡처에서 #DBECF4로 한 채널 1의 반올림 차이가 있습니다.

[실제 연동 검수](../../machine/evidence/career-suite-integration-v005/react-audio/actual-react-audio-background.json), [전체 배경 픽셀 검수](../../machine/evidence/career-suite-integration-v005/react-audio/background-coverage-samples-v002.json).

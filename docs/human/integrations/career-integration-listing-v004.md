# 직업체험 리스팅·연동 전달 v004

최종 전달은 테스트 보기와 ZIP 두 개다. 이전 빌드·ZIP은 보존했다.

- [테스트 보기](http://127.0.0.1:8212/career-suite-test-v009/) — 현재 로컬 서버이며 외부 배포 주소가 아니다.
- [실제 WebGL ZIP](../../../unity/webgl/packages/career-suite-integration-v005.zip): 31,267,874바이트, SHA-256 `1e0e6c4c9cad4ccc5bf1ebec0b4dd1c0b878c7db16c2e20906193f0b976298f9`.
- [리스팅 ZIP](../../../unity/webgl/packages/career-integration-listing-v004.zip): 4,351,947바이트·221개 파일, SHA-256 `ce0750ef66a01c7ece096de36f42c5b1690bea6c4d466781dbe7523b66126ac8`.
- [전체 업데이트·적용 지침](../builds/career-suite-update-v002.md), [최신 실행 안내](../builds/career-suite-v002.md).

리스팅은 실행 WebGL을 포함하지 않는 별도 자료다. 71개 방·552개 시나리오 ID·555개 방/시나리오/버전 조합, 각 항목의 `jobs` 문자열 배열과 현재 수행하는 업무 `description`, 단계·물건 연결을 JSON·CSV로 제공한다. 해당 배포의 `buildId + roomId + scenarioId + scenarioVersion`을 전부 대조한다. 성직자의 세 공간은 각각 다른 조합·설명이다. 원본 전체 목록은 [기계용 JSON](../../machine/catalog/career-experience-descriptions-v001.json)과 [CSV](../../machine/catalog/career-experience-descriptions-v001.csv)다.

ZIP의 `frontend/`는 v003 클라이언트·타입·로컬 저장 수신기·React 예제·오디오 재생기다. `builds/`에는 최종 v009/v005의 지원 목록과 AI 선택 목록이 있다. `audio/`에는108종의 상태·프롬프트·해시·전체 파일 목록·555개 소스 사용 후보를 제공한다. 실제 MP3는 별도 WebGL ZIP의 `site/audio/`에 있다. 파일34개 중30개가 업무 소스에 연결되고4개는 라이브러리용이다. 발행 키10개에는 파일이 없어 대체음을 내지 않는다. 나머지74종은 미생성이다.

기존32개는 동일 바이트로 재사용했다. 승인받아012·013을 각각 처음 생성한 보고 비용10크레딧은 최신 추가 비용 없음 지시 이전 이력이며, 이후 생성·업그레이드는 하지 않았다. 실제 청구서와 계정의 상업 사용권은 독립 확인하지 않았다. 모델·이미지 생성은0회이고 팔레트·모델 형상은 바꾸지 않았다.

최종 테스트 v009의 PAN-050/359@v002는 실제 물건3개 선택·카드6회드래그·한국어입력으로3단계를 마쳤다. 시도3/실수0/재시도0/복귀4, 원본37개와 오디오 종료 후 활성0을 확인했다. 목적지 강조·배치 표시의 닫기/재열기 유지·저장 제목/본문 표시도 검사했다. 최종 생산 v005는 실제 React·효과음·종료 취소·이전 실행 거부·전체 캔버스 배경과 방 전환 유지·원본29개/로컬ACK29개를 확인했다. 추출한 실제 ZIP도 HTTP에서 시작·물건3개 연결·작업 전 종료와 원본5개/ACK5개를 확인했다. 크림 배경은 픽셀값이 일치했고 파랑은 빨강 채널1/255 렌더 반올림이 있었다. 엄격 RGB 실패 원본과 별도 전체영역 적용 통과를 함께 보존했다.

전체34개 라이브러리 디코드·재생 검사는 중간 v003에만 귀속한다. 그 중간 빌드의 전체 캔버스 배경 실패도 보존했다. 이전71개 공간 API 검사와 이전 완주 기록을 최신555개 전체 완주로 승계하지 않는다. 원래 전문 업무·554개 특수분기·모든555개 완주·모든 입력 방식·실제 서비스 인증/lease/fence/복구는 미완료 또는 미검증이다. 로컬 ACK는 운영 백엔드 검증이 아니다.

정적 검토에서 최종 두 빌드의555조합·직업 배열·설명이 일치하고34개 파일 해시·프론트9개 파일·컴파일 스냅샷20개 대상 소스가 일치했다. ZIP의 CRC와221개 전체 파일 바이트를 검사했다. [외부 ZIP 검토 기록](../../machine/evidence/career-integration-listing-v004-zip-review.json), [427개 모델 전체 사용 조회](../assets/career-asset-reuse-report-v003.md)를 참고한다.

최종 기본 별칭은 production-supported-manifest.json→integration-v005, test-supported-manifest.json→test-v009이며, 같은 역할의 AI 목록 기본 별칭도 최종555행이다. 이전 목록은 earlier-builds/에 격리했다. 전달 전 검토에서 발견한 별칭 오류의 ZIP·검토 기록은 pre-review로 보존했고 사용자 전달물은 수정된 위 최종 SHA만 사용한다.

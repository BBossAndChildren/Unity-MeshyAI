# office-ten-v008 — 웹 한글 입력 브리지

일반 웹 Chrome에서 한글 조합·입력을 문서 초안과 실제 모니터 표시로 전달하도록 브라우저 입력 브리지와 초점을 수정했습니다. 기존17소품·30배치·4308모델삼각형·팔레트1장과 10개 직업의 업무 데이터는 유지합니다.

## 실제 확인 범위

Unity6000.3.26f1 빌드 성공, 오류0·경고0,56,378,716바이트,49.290초. [Chrome 원본 관측](../../machine/evidence/office-ten-v008/browser/chrome-proof.json)과 [범위 요약](../../machine/evidence/office-ten-v008/browser/input-scope-summary.json)은 관측7상태이며 독립7개 검수 통과를 뜻하지 않습니다. CDP imeSetComposition/insertText를 사용했고 compositionstart/update는 trusted, 관측한 end는 untrusted(trustedStarts1/trustedEnds0)였습니다. 실제 OS 키보드·모바일IME 인증은 아닙니다.

- 한글 조합과 완성형 입력이 초안·모니터에 반영되고, 조합 중 Enter/Esc가 패널을 닫지 않았습니다.
- PR과 커서·Backspace 편집 중 일시정지·run 변경이 없었습니다. Esc 닫기 후30렌더러/브라우저입력0개, 재열기 초안 유지, 숫자50/12/600 및 Tab→canvas를 관측했습니다.
- 마지막 Enter 제출은 사용자 중단으로 결과가 확인되지 않아 미검증입니다. 전체10업무·공통17 검수는 v003의 역사적 증거입니다. 이번 resize/IAB전용/실물모바일 pass를 주장하지 않습니다. 사용자의 웹 기준 완료 지시에 따라 IAB 전용 검수는 중단했습니다.

[화면](../../machine/evidence/office-ten-v008/browser/chrome-korean-preview.png) · [소스 보존](../../machine/evidence/office-ten-v008/built-source-index.json) · [글꼴·팔레트 동일 해시](../../machine/evidence/office-ten-v008/font-palette-reuse.json). 소스62개 중61개 동일, 장면의 protocol 생성 ID와 buildId가 바뀌었으며 원본을 보존했습니다. ProjectSettings21개는 사전 기준이 없어 빌드 후 보존만 했습니다. 글꼴 cmap는 v007 실측의 동일 바이트 재사용입니다. 새 모델/유료 호출0,실측토큰미제공null.

## 실행·전달

[웹 실행](http://127.0.0.1:8178/office-ten-v008/) · [전달 ZIP](../../../unity/webgl/packages/office-ten-v008.zip). ZIP의 site를 웹서버에서 실행하세요: python -m http.server 8080. /receiver/는 React 수신 화면이며 v007과 동일 바이트를 재사용합니다. 프로젝트는 unity/projects/OfficeAssistant-v001, 장면 Assets/Scenes/OfficeTen.unity, 소스커밋 308507ce0429cc85106035ee3fac367db6756c1d 및 보존된 미커밋 소스입니다. KoreanUI와 React/ReactDOM/scheduler 라이선스를 ZIP에 포함합니다. 별도 OS폰트 설치가 필요하지 않습니다. ZIP 추출본 실제 HTTP 검수는 root가 이어서 수행하며 아직 미검증입니다.


## ZIP 바이트 검증

CRC와 site12파일의 archive/추출후SHA-256 모두 일치했습니다. ZIP 29313477바이트, SHA-256 cb013448e9b363d185e2187d8f896774af2149324d439b961e2a34734e997807. [검사기록](../../machine/evidence/office-ten-v008/package-inspection.json). [추출본](http://127.0.0.1:8178/package-check-office-ten-v008/site/) 실제HTTP GUI는 root 후속검수대기입니다.


Chrome extracted-ZIP HTTP verification: PASS. Native text input and Korean monitor mirroring confirmed. Evidence: [docs/machine/evidence/office-ten-v008/browser/package-http.json](../../machine/evidence/office-ten-v008/browser/package-http.json).

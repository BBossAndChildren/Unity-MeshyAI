# office-ten-v006 — 메모 투명도와 의자 방향 수정

메모 패널 배경 alpha0.70(30% 투명), 문서 미리보기 alpha0.78(22% 투명)을 적용했습니다. 글자·입력칸·실제 출력 용지의 표시값은 유지합니다. 의자 AST-003-0/1을 월드 수직축으로180도 돌려 각각 책상 AST-004-0/1을 향하게 했고 실제Unity facing_dot가 두 쌍 모두1.0입니다. 의자 원본은 등받이가 local+Y에 있어 앞쪽이 local-Y인 제작 근거를 확인했습니다.

Unity6000.3.26f1 실제 빌드 성공, 오류0·경고0. 기존17소품·30배치·4308삼각형, 공용재질1개·PNG1장(2508²)입니다. 모델·팔레트 원본과 이전 빌드/ZIP은 보존했습니다. 새 모델·Meshy·이미지 유료 호출0, 실측토큰미제공null. 소스커밋 308507ce0429cc85106035ee3fac367db6756c1d에 미커밋 변경이 있으며 실제 포함58개 소스는 별도 고정 보존했습니다.

[실행](http://127.0.0.1:8178/office-ten-v006/) · [전달 ZIP](../../../unity/webgl/packages/office-ten-v006.zip)

실제HTTP에서 홈 화면의 두 의자 방향과 메모 대비, 물리 모니터 선택·문서 메모 투명도·입력칸 가독성, Esc후30렌더러 복귀를 확인했습니다. 초기 framebuffer좌표 클릭1회는 DPR1.25 보정 전 배경에 닿았으며 CSS좌표 보정 후 실제 표면 선택을 확인했습니다.

[현재 화면 검수](../../machine/evidence/office-ten-v006/browser/visual-qa.json) · [의자 방향 실측](../../machine/evidence/office-ten-v006/chair-facing.json) · [소스58개](../../machine/evidence/office-ten-v006/built-source-index.json) · [원본업무 불변 해시](../../machine/evidence/office-ten-v006/bounded-review.json)

변경 범위는 UI와 두 의자 배치입니다. Session/Protocol/업무JSON 해시는 v003과 같습니다. v003의 전체업무10종·공통17건 증거는 [기존 보고서](office-ten-v003.md)에 보존하며 새 빌드의 재실행 통과로 복제하지 않습니다. 이번 검사에서 네이티브 업무GUI/물리 모바일/모든 직업 전체업무를 새로 확인하지 않았습니다.

편집 프로젝트 unity/projects/OfficeAssistant-v001, 장면 Assets/Scenes/OfficeTen.unity. ZIP은 site 전체, 해소된18에셋·팔레트1개 manifest, 실행안내와 폰트/React 라이선스를 포함합니다. site 폴더에서 python -m http.server 8080으로 실행 후 /receiver/ 또는 /를 여세요. 모델·Blender·Unity편집 원본은 ZIP에 넣지 않습니다.


최종 ZIP 29284326bytes, SHA-256 1fa8b147d9187e2888135d2ad71b4d51020d6a6d95c0b3f451180588c53699c3. CRC·12개 site파일 해시 및 새 폴더 압축해제 실제HTTP 실행을 확인했습니다. [패키지 실행 근거](../../machine/evidence/office-ten-v006/browser/package-http.json) · [홈 화면](../../machine/evidence/office-ten-v006/browser/home.jpg) · [문서 메모 화면](../../machine/evidence/office-ten-v006/browser/work.jpg).

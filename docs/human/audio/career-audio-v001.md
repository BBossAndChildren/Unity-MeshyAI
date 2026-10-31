# 직업체험 기존 효과음 연결 v001

사용자 제작 작업의 기존 효과음만 재사용한다. 현재 원본 작업의 108개 노드 중 32개는 생성 완료, 76개는 `not_run`이다. 이 문서는 소스 연결 준비 기록이며 최종 음향 전달·실제 청취 완료를 뜻하지 않는다.

- 원본: [생성 목록](../../machine/catalog/sound-effects-v001.json), [후보 108종](../../machine/catalog/sound-effects-candidates-v001.json), [기존 ElevenLabs 작업](https://elevenlabs.io/app/flows/cqhiqr5xhqK1tFjd2AbD).
- 현재 파일: [런타임 manifest](../../../web/career-audio/v001/audio-manifest.json), [108종 출처·전체 사용 후보](../../machine/catalog/career-audio-runtime-v001.json), [555조합 물건별 상세](../../machine/catalog/career-audio-use-map-v001.json), [사람용 전체 사용표](career-audio-use-map-v001.md).
- 원본·기존 처리본 보존. processed MP3 32개 369,170바이트를 동일 바이트로 복사했고 SHA-256 전부 일치했다. WAV/MP3 재인코딩 없음.
- 이번 생성 호출·재생성·생성 크레딧은 0. 과거 32회 생성의 커넥터 보고값은 231크레딧, 2.31 price_cents USD이며 실제 청구서 검증은 하지 않았다. 토큰의 효과음별 배분은 미측정이다.
- 계정의 사용 권리·상업 사용 조건은 독립 검증하지 않았다. 사람 목소리/내레이션/TTS/새 음성 복제는 생성하지 않았다.

파일 경로는 manifest URL을 기준으로 해석한다. 정식 소스 `web/career-audio/v001/` 전체를 사이트의 `audio/`로 복사하며 `src=clips/<key>.mp3`다. 최대 동시 4음원·루프2개, gain·cooldownMs는 초기 소스 설정이고 최종 실제 청취 보정은 미검증이다. 없는 효과음을 비슷한 이름의 효과음으로 바꾸지 않는다. 새 빌드 포함·브라우저 재생·작업 의미 적합성은 각각 별도 검증해야 한다.

| ID / 버전 | 키 / 이름 | 상태 | 초 / 바이트 | 처리본 SHA-256 |
|---|---|---|---|---|
| SFX-001 / v001 | ui_click / 버튼 클릭 | 파일 준비·재생 미검증 | 0.03746 / 1714 | a706c3255e5a801e777a2f6b028ddabcc9f8fe8f804d52c91cb9aba81f265e8e |
| SFX-002 / v001 | ui_focus / 초점 이동 | 파일 준비·재생 미검증 | 0.339002 / 6312 | 1a0c5d58635025f2b45477227b8b4e2078a18f8b5af2316e7429ae713744bc63 |
| SFX-003 / v001 | object_select / 물건 선택 | 파일 준비·재생 미검증 | 0.48 / 8820 | 6e87d33eed34026181c0527e9e1238411ddf5118fea9138f6019aeb4cb3656b5 |
| SFX-004 / v001 | view_open / 확대 및 작업 화면 열기 | 파일 준비·재생 미검증 | 0.341633 / 6730 | 1b01d139df7207e9a0963f4bb5cca9b3cb68df2d00a39cc1be7be3a22989ca59 |
| SFX-005 / v001 | view_close / 닫기 및 공간 복귀 | 파일 준비·재생 미검증 | 0.48 / 8820 | 16966559e70e7a7688216a8f5a57ca79caacc3982da23eca65b629ce48628343 |
| SFX-006 / v001 | tab_switch / 탭과 페이지 전환 | 파일 준비·재생 미검증 | 0.48 / 8820 | 6228d5d042724ef224161df32b9a91afc427ae63793780476bfedd690c92cd47 |
| SFX-007 / v001 | toggle / 체크 및 토글 | 파일 준비·재생 미검증 | 0.392721 / 7566 | 3bfeaf9657637df399c038564705d4cbe8dc3b6a2e4fd06738f92748bcb17e0f |
| SFX-008 / v001 | field_edit / 필드 입력 피드백 | 파일 준비·재생 미검증 | 0.48 / 8820 | df4d9ef8d8e414231840d106fd127b9909590b517ccb9865acb497270bdb2fff |
| SFX-009 / v001 | drag_pick / 항목 집기 | 파일 준비·재생 미검증 | 0.48 / 8820 | 1af534cefd977ff5784c86af599f9dc0ce664871baf934b2a727f75cc3f5f001 |
| SFX-010 / v001 | drag_drop / 항목 놓기 | 파일 준비·재생 미검증 | 0.239864 / 5058 | 561fa1aa4e4452bb57ef8388444614a32079f6afd06452921e85cbb93a7dbe61 |
| SFX-011 / v001 | snap / 스냅 결합 | 파일 준비·재생 미검증 | 0.376349 / 7148 | 3c0bab61c6e004d6159256dfb51c7cc00badfa950f8bb9d01344cf50f290cc69 |
| SFX-012 / v001 | rotate_tick / 회전과 눈금 틱 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-013 / v001 | slider_tick / 수치 증감 틱 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-014 / v001 | save / 저장 확정 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-015 / v001 | undo / 되돌리기 및 복원 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-016 / v001 | step_done / 업무 단계 완료 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-017 / v001 | mission_done / 미션 최종 완료 | 파일 준비·재생 미검증 | 1.052109 / 18015 | 2d438d06e006e457bf7d792d452595f87bf0dc68478913daf27c9133972ca451 |
| SFX-018 / v001 | validation / 수정 필요 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-019 / v001 | blocked / 선행 조건 잠금 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-020 / v001 | retry / 재시도 시작 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-021 / v001 | hint / 도움말 표시 | 파일 준비·재생 미검증 | 0.434694 / 7984 | b9f890434cfd7666a9eec4dab8c6bc3e066079efb2a0a4f3ac8ce21fdc09f88e |
| SFX-022 / v001 | request_change / 요청 변경 알림 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-023 / v001 | handoff_send / 인계 및 메시지 전송 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-024 / v001 | handoff_ack / 상대 확인 수신 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-025 / v001 | pause / 일시정지 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-026 / v001 | resume / 재개 | 파일 준비·재생 미검증 | 0.48 / 8820 | 7b1039df11558cf8c4997d2ad631315510ab188532944094b26dd5071b16cf35 |
| SFX-027 / v001 | reset / 전체 초기화 확정 | 파일 준비·재생 미검증 | 0.448594 / 8402 | fa6c6c782f67ff18a833b2e0c4891632146ca619433ea7e1d6fdbac78479e3c5 |
| SFX-028 / v001 | exit / 중도 종료 확인 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-029 / v001 | priority / 긴급 업무 알림 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-030 / v001 | safety / 안전 주의 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-031 / v001 | anomaly / 이상 신호 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-032 / v001 | recovery / 기록 복구 확정 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-033 / v001 | paper_turn / 종이와 책장 넘김 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-034 / v001 | paper_stack / 문서 묶음 집기와 내려놓기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-035 / v001 | folder / 파일과 폴더 여닫기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-036 / v001 | drawer_open / 서랍과 수납장 열기 | 파일 준비·재생 미검증 | 0.447778 / 8402 | a64ac553b26d4e4429f0a3a5898b1e55e49581b6e0cd3fadfddacbb4ee036838 |
| SFX-037 / v001 | drawer_close / 서랍과 수납장 닫기 | 파일 준비·재생 미검증 | 0.423175 / 7984 | d187cfa844de733c99017ad95bfb07dd3ac3ad1daa56de33646b5bb4a52e5ad9 |
| SFX-038 / v001 | file_place / 분류함 보관 | 파일 준비·재생 미검증 | 0.409932 / 7566 | aead671379a564c82de2d51ac704bb1d57def6f2d0b8b38e40e17859ce20bd99 |
| SFX-039 / v001 | card_move / 카드와 메모 이동 | 파일 준비·재생 미검증 | 0.48 / 8820 | 03d50e9e1e631705651a81b5292e1db0e2d0261b8fc813bec95d53900c31c94d |
| SFX-040 / v001 | writing / 필기와 마커 | 파일 준비·재생 미검증 | 1.48 / 24702 | 015d4db570a28a38a4a8a167b0bba48803551003c55cc73923ce909c29d14b74 |
| SFX-041 / v001 | keyboard / 키보드 타건 | 파일 준비·재생 미검증 | 1.48 / 24702 | ccf609ef79249d471ff9b1c4899f5d44dea02bdf66efe2ee9eee66e5673875f8 |
| SFX-042 / v001 | mouse / 물리 마우스 클릭 | 파일 준비·재생 미검증 | 0.112358 / 2968 | 137dc71aace5debb5b4847252ca11bf23ca59314357a65d77461c302f84a5e2a |
| SFX-043 / v001 | printer_start / 복합기 시작과 급지 | 파일 준비·재생 미검증 | 0.558118 / 10074 | bf790e47c8f6d6a1f5de23f04edbb04a75c2c0fd2ff5aa7f67b4e01f0d800a14 |
| SFX-044 / v001 | printer_run / 복합기 작동 | 파일 준비·재생 미검증 | 2.98 / 48944 | 534dc3d0298fa001afa59cb6d7c4cafd0e35cc62398cd1dfd2e6f3c4c80867ca |
| SFX-045 / v001 | printer_sheet / 용지 한 장 배출 | 파일 준비·재생 미검증 | 0.367732 / 7148 | 845afaa76d7e722a92da30d3fe1d6492b07c103c3a48ab157e3cbf83fb4da70b |
| SFX-046 / v001 | printer_stop / 복합기 정지 | 파일 준비·재생 미검증 | 0.443515 / 7984 | d46f4b25c78072e967a337ed57d6c984de67fe463ac1ebda7e52940bddaa6173 |
| SFX-047 / v001 | phone_ring / 전화 수신 | 파일 준비·재생 미검증 | 2.23 / 36823 | e8ccd2bdd32dc6619587e21100c804bcaac3c278b25d6a76d72b2efcf957111a |
| SFX-048 / v001 | phone_pick / 수화기 들기와 놓기 | 파일 준비·재생 미검증 | 1.338095 / 22612 | 29b3f07091fc08c6bea3bfa97b720b9386281c6f03bd77102f0ab75d404978b9 |
| SFX-049 / v001 | radio / 통신 송수신 클릭 | 파일 준비·재생 미검증 | 0.48 / 8820 | 1d1bbf1a826b175d3155ca3e138e110c933e973e0ce0c2fa0490be728936ad81 |
| SFX-050 / v001 | part_pick / 작은 부품과 공구 집기 | 파일 준비·재생 미검증 | 0.37449 / 7148 | 39b847def9f735733f93881826b41074ee1568a74cc3de996b913445ad4d4842 |
| SFX-051 / v001 | part_fit / 부품 결합 | 파일 준비·재생 미검증 | 0.240227 / 5058 | a184a164c1ce3005f09824ccec172b3118bdcbc5a1139588818f6a768b8adfef |
| SFX-052 / v001 | part_remove / 부품 분리 | 파일 준비·재생 미검증 | 0.401293 / 7566 | 332abdbaef1de10af6e676d777cddb7d68e04c9c18f5dfdbcd0627d4a63be0c4 |
| SFX-053 / v001 | screw / 나사 조임과 풀기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-054 / v001 | tool_tap / 공구와 재료 접촉 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-055 / v001 | vise / 바이스 조절 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-056 / v001 | cable_in / 케이블 삽입 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-057 / v001 | cable_out / 케이블 분리 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-058 / v001 | switch / 기기 스위치와 레버 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-059 / v001 | dial / 기계 다이얼 눈금 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-060 / v001 | measure / 측정값 확정 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-061 / v001 | motor / 소형 기기 작동 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-062 / v001 | guard_latch / 안전 가드 잠금 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-063 / v001 | box_handle / 상자 집기와 놓기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-064 / v001 | pack_rustle / 포장재 바스락 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-065 / v001 | cart_move / 운반차 바퀴 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-066 / v001 | load_set / 팔레트 적재 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-067 / v001 | pos_key / POS 버튼 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-068 / v001 | scan_beep / 상품 스캔 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-069 / v001 | receipt / 영수증 출력 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-070 / v001 | glass_set / 유리 용기 접촉 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-071 / v001 | liquid_pour / 액체 붓기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-072 / v001 | scale / 저울 버튼과 확정음 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-073 / v001 | case_latch / 시료와 장비 케이스 잠금 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-074 / v001 | medical_pulse / 가상 의료 모니터 펄스 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-075 / v001 | call / 호출 장치 알림 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-076 / v001 | mixer_start / 믹서 시작과 정지 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-077 / v001 | mixer_run / 믹서 회전 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-078 / v001 | tray_set / 베이킹 트레이 놓기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-079 / v001 | oven_door / 오븐 문 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-080 / v001 | timer_done / 타이머 완료 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-081 / v001 | cook / 가열과 조리 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-082 / v001 | dish_set / 식기와 그릇 놓기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-083 / v001 | soil / 흙과 모종 심기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-084 / v001 | water / 물주기와 관수 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-085 / v001 | harvest / 작물 수확과 상자 담기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-086 / v001 | wash / 세척 물 흐름 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-087 / v001 | shutter / 카메라 셔터 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-088 / v001 | record / 녹화 시작과 정지 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-089 / v001 | stand / 스탠드 위치 조절 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-090 / v001 | fader / 오디오 페이더 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-091 / v001 | pen_stroke / 펜 태블릿과 붓 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-092 / v001 | beat / 박자와 타이밍 기준음 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-093 / v001 | cue / 방송과 무대 큐 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-094 / v001 | brick_set / 벽돌과 자재 결합 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-095 / v001 | rope / 밧줄 취급 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-096 / v001 | ball / 공 접촉과 튀김 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-097 / v001 | equipment_place / 운동과 돌봄 도구 놓기 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-098 / v001 | amb_office / 조용한 사무실과 상담실 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-099 / v001 | amb_lab / 연구실과 장비실 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-100 / v001 | amb_factory / 작업장과 생산 현장 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-101 / v001 | amb_store / 매장과 물류 공간 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-102 / v001 | amb_kitchen / 주방과 제빵실 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-103 / v001 | amb_green / 온실과 야외 농장 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-104 / v001 | amb_studio / 스튜디오와 공연장 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-105 / v001 | amb_care / 의료와 돌봄 공간 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-106 / v001 | amb_public / 도서관과 교육·전시 공간 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-107 / v001 | amb_port / 항만과 선박 | 미생성(not_run) | 미측정 / 없음 | 없음 |
| SFX-108 / v001 | amb_worship / 예배 공간 | 미생성(not_run) | 미측정 / 없음 | 없음 |

전체 후보와 과거 생성 문구·노드·generation ID·검수 근거는 버전 고정 원본 목록을 보존하고 새 런타임 목록에서 연결했다. 소리의 파일 포함은 특정 직업이 그 기기를 실제 조작한다는 증거가 아니다. 예를 들어 출력 전 준비만 구현한 3D프린팅 사례에 프린터 작동음을 붙여 실제 출력으로 표시하지 않는다.

현재 전체 대상은 71개 논리 방·552개 고유 시나리오·555개 방/시나리오/버전 조합이다. 공통 소리도 같은 음원을 공유하며 직업마다 중복 생성하지 않는다. 후보 연결은 실제 플레이 이벤트 원장과 별개다. 전체 원래 전문 업무·554개 미구현 특수 분기는 음향 추가로 완료되지 않는다.

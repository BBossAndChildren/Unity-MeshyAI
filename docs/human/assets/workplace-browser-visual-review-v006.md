# WebGL v006 실제 화면 시각 검토

실제 새 HTTP 캡처 71쌍(1440×900·900×600, 원본 142장)을 모두 확인했다. 전체 화면 시트 18장으로 배치·UI 잘림을 검토하고, 원본 픽셀을 다시 샘플링하지 않은 장면 확대본 71쌍을 별도로 열어 부위별 색 영역·경계 번짐·실루엣·눈에 보이는 지지를 확인했다. v005의 통과 판정을 복사하지 않았다.

이 표시 범위에서 의도하지 않은 팔레트 색 번짐, 예상 밖 원색 덩어리, 재질 틴트 불일치, 주요 메시 누락, 공간 잘림, 주요 지지물 소실은 발견하지 못했다. 목재/크림 표면, 청록 좌석·수납장, 검은 전자기기, 보라/분홍 부위와 의도된 노랑/청록 강조를 공간마다 실제 확인했다. 71개 런타임 기록 모두 공용 재질 1개·이미지 1개·2508×2508이다. 가져온 팔레트 픽셀은 원본과 동일하고 Point 필터·밉맵/압축/크기 변경 비활성화가 기록되어 있다. 실제 성공한 빌더는 등록된 이미지와 흰색 재질 틴트를 검사하며, 공용 재질 YAML도 (1,1,1,1)이다. 현재319개 GLB의 해시와 기본 색 계수(1,1,1,1)도 다시 확인했다.

작은 가시성 한계는 남긴다. 어두운 배경 위의 가는 검은 트러스·풍향 센서 선(PAN033/034/039/041)은 특히900px에서 대비가 낮다. 작은 흰 접시·도구의 흰 작업대 대비, 단추·문자·안테나, 가려진 후면·밑면은 이 브라우저 두 화면만으로 각각 인증하지 않는다. 이러한 부위는 개별 구성요소의 세 방향 증거와 구분한다. 다른 카메라 확대·하드웨어 GPU·모바일, 전문 장비 기능·세부 도상 정확성은 이 시각 검토의 통과 범위가 아니다. 열린 차단급 시각 문제는 없다.

현재319개 모델 증거는 구성요소248개(신규231·재사용17)와 공간 조립71개이며, 방향 이미지957장과 현재 전용 축소 시트30장이다. 전체 배치805개와 지지 검토 부분집합476개를 혼동하지 않는다. 누적483 렌더 버전에는 비현재 보존164버전이 포함된다. 모델·소스·참조는 변경하지 않았다.

v005에서 보인 COM·제작 방식 캡션은 v006 실제 선택 화면에서 바닥 표면·회전 사무의자 등 제품 이름으로 정리됐다. 새 움직임 줄이기 버튼과 경로 버튼은 양쪽 화면 크기의 사무실 패널 안에 배치된다. 입력 이벤트와 기능 통과는 별도 실제 기능 검사 원장을 사용한다.

[공간별 관찰·해시·근거](../../machine/evidence/workplaces-v006/visual-review/screenshot-review.json) · [12개 실제 공간 개요](../../machine/evidence/workplaces-v006/visual-review/actual-http-12-room-overview.jpg) · [현재319 모델 증거](../../machine/evidence/workplaces-model-review-v001/current-final-319/coverage.json)

| 공간 | 실제 확인한 색 영역 |
|---|---|
| PAN-001 공용 업무 사무실 | Tan desk/chair surfaces, cream drawers/paper/platform, green partitions and foliage, dark screens/peripherals, gold desk lamps. |
| PAN-002 협업·기획 사무실 | Teal seats/cart, dark laptop frames, grey writing surface with purple frame, purple mat and intentional yellow beanbag. |
| PAN-003 행정·문서 처리 사무실 | Tan desks/chair backs, dark monitors/PCs, green filing cabinet, cream printer, purple folder and pink eraser remain separate regions. |
| PAN-004 민원·방문객 접수실 | Teal counter/seats and brochure pockets, tan top, purple kiosk housing/seat legs, dark monitor and kiosk foot. |
| PAN-005 전문 상담 사무실 | Tan tables/shelf, teal chairs, separate mint/purple/yellow book spines, pale-blue books, yellow balance pans. |
| PAN-006 실험실 | Cream worktop/sink/cabinet tops, teal cabinet/cart bodies, dark equipment faces, pastel tube pieces and intentional yellow stool. |
| PAN-007 분석실 | Cream/teal analysis cabinets, black microscope barrel and white foot, mint tray frame, dark computer frame/peripherals. |
| PAN-008 진료실 | White bed/pillow/lamp, teal bed frame/cart/cabinet, dark casters/screens, tan desk and teal visitor seat. |
| PAN-009 처치실 | White mattress/lamp/sink rims, teal bed frame/cabinets/carts, dark casters and cabinet handles. |
| PAN-010 병실 | Tan head/footboards, white pillow/panel/monitor frame, purple mattress, teal monitor cart and green armchair. |
| PAN-011 의료 접수실 | Teal counter and linked seats, tan top, purple tray/kiosk/seat legs, dark electronics and separate book-spine strips. |
| PAN-012 교실 | Green chalkboard within wood frame, tan desks, teal chair backs/lockers, pale books and purple desk legs. |
| PAN-013 교육 실습실 | Tan workbenches/shelf, teal lower shelves and kit bases, black legs, deliberate yellow stool seats and kit pieces. |
| PAN-014 강의실 | Grey projection surface with dark stand, cream projector with dark lens, teal cart/seats, tan lectern/tables. |
| PAN-015 복지·심리 상담실 | Green upholstered chairs, tan legs/table/shelf, purple rug, pale notebook/tissues and green plant. |
| PAN-016 복지 활동실 | Purple board frame/mat, grey writing surface, teal chairs, green cabinet, tan furniture, intentionally mixed pastel activity pieces. |
| PAN-017 요양실 | Tan bed/rails, purple bedding/mat, white pillow, green cabinet, teal wheelchair seat, dark wheel frame and grey hubs. |
| PAN-018 생산 구역 | Cream machine body, dark access panel and conveyor rollers, teal controls/bin, yellow guard frames and warning cap. |
| PAN-019 조립 구역 | Tan bench/pegboard/shelf, teal trays/car chassis/cart, dark wheels/vice/tool heads, yellow toy body and stool. |
| PAN-020 정비 구역 | Tan bench/pegboard/toolbox body, teal cart/tray/lower shelf, dark vice/open-case interior, cream lamp and case rim. |
| PAN-021 소매점 | Tan counter/shelves, grey shelf back, teal basket/counter/POS screen, green storage, ochre packages with pale labels. |
| PAN-022 서비스 창구 | Teal counter/seats, tan top, purple paper tray, dark monitor/PC, green cabinet and separate mint/purple/yellow files. |
| PAN-023 미용실 | Pink salon chair, cream armrests, dark pedestal/basin interior, pale basin rim, teal cart and grey mirror within wood frame. |
| PAN-024 주방 | Cream worktops/dishes, teal cabinets, green refrigerator, dark burners/oven door, tan utensil rack with pale utensil heads. |
| PAN-025 제과실 | Green mixer with cream bowl, dark oven face/burners, pale rack trays with dark posts/casters, tan shelf and teal tray/lower shelf. |
| PAN-026 식당 홀 | Tan tables/lectern, teal seats/counter cabinets, cream buffet top and white dishes/cups, green plant in pale pot. |
| PAN-027 디자인 작업실 | Dark monitor/tablet frame, teal tablet face, white stylus, purple tray, mint/purple sample board and separate pale swatches. |
| PAN-028 미술 작업실 | Tan easel/ledge, grey mounted and spare canvases, yellow stool, green plant, tan work surface and small pastel palette patches. |
| PAN-029 공예 작업실 | Tan bench/shelf/tool handles, dark vice/tool heads, teal cart/tray, cream lamp and ochre storage box. |
| PAN-030 촬영 스튜디오 | Dark camera/tripod/light stands/case, teal lens face, grey reflector/light faces, cream case catches and tan table. |
| PAN-031 방송 스튜디오 | Teal counter and camera lens, tan top, dark microphone/headphones/camera/mixer, purple headphone band, grey light faces. |
| PAN-032 영상 편집실 | Dark monitors/speakers/peripherals, grey speaker rings, purple headphone band, tan desk/chair/shelf. |
| PAN-033 공연 무대 | Tan stage and teal audience seats, dark truss/microphone/speakers/light stands, grey light panels and speaker rings. |
| PAN-034 전시실 | Purple sculptures with teal upper facets on cream plinths, grey display boards within tan frames, tan bench and dark truss. |
| PAN-035 문화 활동실 | Grey board/purple frame, teal chairs, tan table/shelf, separated pale palette dabs and dark tool tips. |
| PAN-036 건축 작업 구역 | Tan scaffold decks/brick forms/timber/toolbox, pale scaffold uprights, teal handcart, yellow safety rail and dark bars/toolbox lid. |
| PAN-037 설비 작업 구역 | Pale vertical pipes and ladder, teal connecting pipe/cabinet/tray, tan valve/bench/pegboard, dark tool heads. |
| PAN-038 환경 조사 지점 | Soft green terrain/foliage, tan table and bag, teal lower shelf, small yellow meter, pale vial and ochre box. |
| PAN-039 관측 지점 | Yellow sensor housing on dark tripod, white weather collars/pale mast with dark wind arms, tan bench/table, teal laptop face, dark case. |
| PAN-040 재배지 | Green crops/watering can, brown soil and wood planter walls, teal tub, dark irrigation/spade/rake heads and tan handles. |
| PAN-041 온실 | Cream greenhouse frame, teal tank/cart, green seedlings in dark trays, tan benches with purple legs and pale weather sensor collars. |
| PAN-042 축사 | Tan pen rails, intentional yellow bedding pads, teal trough/tank/bucket, cream silo and pale cleaning-tool heads. |
| PAN-043 동물 관리실 | Cream sink/cage frames, dark cage bars and bowl interiors, teal lower shelf/bowl/tray, yellow bowl rim and purple mat. |
| PAN-044 선박 갑판 | Pale railings and deck, tan ring/rope, dark capstans, green storage and ochre box; no water-color patch on deck. |
| PAN-045 조타실 | Pink helm chair, dark base/readout borders/radio, teal readouts, cream monitor frame, tan wheel and pale bedside top. |
| PAN-046 부두 | Deliberate cyan water strip, pale dock slab, tan life ring/rope, dark bollards with yellow caps, teal cart and ochre boxes. |
| PAN-047 체육관 | Dark ball rack/bench top, orange balls, tan bench, cyan mat and teal bottles with dark caps. |
| PAN-048 운동 지도실 | Grey mirror with tan frame, dark dumbbells, cyan mat/step, tan exercise bar and teal bottles with dark caps. |
| PAN-049 경기 구역 | Green court with white lines/goals/ball, tan benches, teal scoreboard face, purple support and dark scoreboard base. |
| PAN-050 수사실 | Green cabinet, purple board/tray, grey board face, dark monitor/PC/peripherals, tan desk and distinct colored files. |
| PAN-051 증거 분석실 | Cream laboratory tops, teal cabinets/cart/tray, dark microscope/monitor/PC/case, pale catches and mint screen/tray areas. |
| PAN-052 법정 | Tan judge bench/platform/desks, teal seats, purple desk legs and cream drawers with dark handles. |
| PAN-053 물류 창고 | Tan shelves/pallet/bench, ochre boxes with pale labels, teal lower shelf and intentional yellow pallet-jack forks with dark handle. |
| PAN-054 운송 조종 공간 | Pink driver seat, dark monitor/readout borders/radio, teal readouts and passenger chair, cream monitor housings and tan/cream support. |
| PAN-055 운송 거점 | Teal counter/seats/cart/sign face, tan top/bench/shelf, ochre parcel boxes, purple sign/seat supports and dark bench legs. |
| PAN-056 금융 창구 | Teal counters/seats, tan tops/chair backs, dark electronics, purple tray/kiosk/seat supports; tray edge and monitor remain separate. |
| PAN-057 금융 상담실 | Teal chairs/laptop face, tan table, green cabinet, dark calculator/laptop frame and separate mint/purple/yellow file spines. |
| PAN-058 가정 수리 공간 | Purple repair mat, teal washer door/cart/tray, cream washer casing, dark tool heads and toolbox lid, green cabinet. |
| PAN-059 방문 학습 공간 | Tan table/shelf/bag, teal chairs/book cover, dark pen and cream notebook page edges. |
| PAN-060 서버실 | Dark rack faces and cases, teal tiny indicators/laptop/cart/cabinet, grey rack surfaces and intentional yellow/teal cable lines. |
| PAN-061 관제실 | Cream console/terminal housings and support tops, dark monitor/radio/readout borders, teal readouts and tan office chair. |
| PAN-062 거실 | Cream sofa with tan feet, purple rug, tan coffee table, dark TV, green cabinet and plant. |
| PAN-063 주택 관리 공간 | Grey board with purple frame, teal cabinet/tray/bucket, green storage, tan work surfaces, dark monitor/toolbox lid. |
| PAN-064 기독교(개신교) 예배실 — 목사 | Tan pews/pulpit/cross, white book pages, pale inset cross on pulpit, dark keyboard frame with separate white/black keys. |
| PAN-065 군 행정실 | Tan desk/chair, teal visitor chair/board face, purple board frame, green cabinet, dark monitor/radio/PC and pale handles. |
| PAN-066 생활관 | Tan bed frames/benches, purple bedding/luggage, white pillows, teal lockers/chair and cream bedside surface. |
| PAN-067 장비 관리실 | Tan shelf/pegboard/bench/toolbox body, teal cart/lower shelf, dark equipment cases/tool heads and pale handles/catches. |
| PAN-068 출장 업무 공간 | Purple luggage with teal strips, dark laptop/case, teal screen/phone/chair, tan table/bag and cream paper stack. |
| PAN-069 안내 집결 지점 | Tan rope-barrier posts/bench/board frame/bag, pale ropes, grey board, teal sign, purple sign support/luggage and green foliage. |
| PAN-070 불교 법당 — 스님 | Gold Buddha on tan altar, deliberate pink cushions/lotus, cream incense bowl, tan drum/mallet and pale book rest. |
| PAN-071 천주교 성당 — 신부님 | Tan pews/pulpit/altar/cross, white altar cloth, gold chalice/candlesticks, pale figure on cross and teal book cover. |

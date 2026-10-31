# 사이버교육운영자 직접작업 구현 인계

시나리오 career-net-462-experience v002. 제작 범위는 사용자 요청의 신규 사무실10개 중 한 건이다. 현재는 설계 준비 완료/새 런타임 실행 미검증이다.

모니터 AST-005 v001, 복합기 AST-009 v001, 수납장 AST-015 v001의 기존 형상/콜라이더를 같은 프로젝트 안에서 재사용한다. PAN001/AST020v006 구성은 유지한다. 세 물건의 UI 외 네 번째 조작 물건은 만들지 않는다.

가상 온라인 수업 운영: 실시간강의10:00, 질의응답10:30, 다시보기공개11:00. 세 운영 카드를 알맞은 시간 슬롯에 배치합니다. 운영표 r1을2부 출력해 수업운영함에 보관합니다.

{
  "scenario_id": "career-net-462-experience",
  "version": "v002",
  "occupation_id": "career-net-462",
  "name": "사이버교육운영자",
  "title": "실시간 수업 운영표 배치하기",
  "request": "가상 온라인 수업 운영: 실시간강의10:00, 질의응답10:30, 다시보기공개11:00. 세 운영 카드를 알맞은 시간 슬롯에 배치합니다. 운영표 r1을2부 출력해 수업운영함에 보관합니다.",
  "help": "요청 원문과 자료를 대조하세요. 저장·출력·보관은 순서대로 진행하며 화면을 닫아도 초안은 유지됩니다.",
  "steps": [
    {
      "step_id": "prepare",
      "object_id": "monitor",
      "work_item_id": "EDU-06",
      "title": "실시간 수업 운영표 배치하기",
      "instruction": "가상 온라인 수업 운영: 실시간강의10:00, 질의응답10:30, 다시보기공개11:00. 세 운영 카드를 알맞은 시간 슬롯에 배치합니다. 운영표 r1을2부 출력해 수업운영함에 보관합니다.",
      "kind": "schedule",
      "fields": [],
      "items": [
        {
          "id": "lecture",
          "label": "실시간강의",
          "target": "10:00"
        },
        {
          "id": "questions",
          "label": "질의응답",
          "target": "10:30"
        },
        {
          "id": "replay",
          "label": "다시보기공개",
          "target": "11:00"
        }
      ],
      "destinations": [
        "10:00",
        "10:30",
        "11:00"
      ],
      "receipt_label": "온라인 수업 운영표",
      "seconds": 0
    },
    {
      "step_id": "print",
      "object_id": "copier",
      "work_item_id": "EDU-06",
      "title": "최신 결과물 출력",
      "instruction": "모니터에서 저장한 EDU-06 문서 r1을 2부 출력하세요. 출력 중 설정 변경·중복 시작은 잠깁니다.",
      "kind": "print",
      "fields": [
        {
          "id": "document_id",
          "label": "출력 문서 ID",
          "initial": "OLD-DRAFT",
          "expected": "EDU-06"
        },
        {
          "id": "revision",
          "label": "출력 revision",
          "initial": "0",
          "expected": "1"
        },
        {
          "id": "copies",
          "label": "출력 부수",
          "initial": "1",
          "expected": "2"
        }
      ],
      "items": [],
      "destinations": [],
      "receipt_label": "온라인 수업 운영표",
      "seconds": 2
    },
    {
      "step_id": "file",
      "object_id": "cabinet",
      "work_item_id": "EDU-06",
      "title": "보관 및 인계",
      "instruction": "출력 묶음을 수업운영 칸으로 옮기고 문서명과 부수를 인계하세요.",
      "kind": "handoff",
      "fields": [
        {
          "id": "title",
          "label": "인계 문서명",
          "initial": "초안",
          "expected": "온라인 수업 운영표"
        },
        {
          "id": "copies",
          "label": "인계 부수",
          "initial": "0",
          "expected": "2"
        }
      ],
      "items": [
        {
          "id": "EDU-06",
          "label": "온라인 수업 운영표 2부",
          "target": "수업운영"
        }
      ],
      "destinations": [
        "수업운영",
        "재확인",
        "이전자료"
      ],
      "receipt_label": "온라인 수업 운영표",
      "seconds": 0
    }
  ]
}

닫기·초안 유지·카메라 복귀·키보드/터치·출력 중 잠금/초기화/종료와 새 시나리오 ID별 실제 React 수신을 독립적으로 검증한다. 과거 사무보조원 pass를 승계하지 않는다.

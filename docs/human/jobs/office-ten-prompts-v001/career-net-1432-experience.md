# 베타테스터 직접작업 구현 인계

시나리오 career-net-1432-experience v002. 제작 범위는 사용자 요청의 신규 사무실10개 중 한 건이다. 현재는 설계 준비 완료/새 런타임 실행 미검증이다.

모니터 AST-005 v001, 복합기 AST-009 v001, 수납장 AST-015 v001의 기존 형상/콜라이더를 같은 프로젝트 안에서 재사용한다. PAN001/AST020v006 구성은 유지한다. 세 물건의 UI 외 네 번째 조작 물건은 만들지 않는다.

가상 쇼핑앱 사양: 주문액50000원 이상은 배송비0원. 테스트기록: T01 주문49000/표시3000, T02 주문50000/표시3000, T03 주문51000/표시0. 실패 테스트와 기대값, 재현 절차를 기록합니다. 보고서 r1을1부 출력해 수정요청함에 보관합니다. 재현 절차는「주문50000 → 배송비 조회」형식으로 기록하세요.

{
  "scenario_id": "career-net-1432-experience",
  "version": "v002",
  "occupation_id": "career-net-1432",
  "name": "베타테스터",
  "title": "경계값 테스트에서 오류 보고서 작성하기",
  "request": "가상 쇼핑앱 사양: 주문액50000원 이상은 배송비0원. 테스트기록: T01 주문49000/표시3000, T02 주문50000/표시3000, T03 주문51000/표시0. 실패 테스트와 기대값, 재현 절차를 기록합니다. 보고서 r1을1부 출력해 수정요청함에 보관합니다. 재현 절차는「주문50000 → 배송비 조회」형식으로 기록하세요.",
  "help": "요청 원문과 자료를 대조하세요. 저장·출력·보관은 순서대로 진행하며 화면을 닫아도 초안은 유지됩니다.",
  "steps": [
    {
      "step_id": "prepare",
      "object_id": "monitor",
      "work_item_id": "TST-04",
      "title": "경계값 테스트에서 오류 보고서 작성하기",
      "instruction": "가상 쇼핑앱 사양: 주문액50000원 이상은 배송비0원. 테스트기록: T01 주문49000/표시3000, T02 주문50000/표시3000, T03 주문51000/표시0. 실패 테스트와 기대값, 재현 절차를 기록합니다. 보고서 r1을1부 출력해 수정요청함에 보관합니다. 재현 절차는「주문50000 → 배송비 조회」형식으로 기록하세요.",
      "kind": "table",
      "fields": [
        {
          "id": "failed_case",
          "label": "실패 테스트 ID",
          "initial": "T01",
          "expected": "T02"
        },
        {
          "id": "expected_fee",
          "label": "실패 테스트 기대 배송비(원)",
          "initial": "3000",
          "expected": "0"
        },
        {
          "id": "reproduction",
          "label": "재현 절차",
          "initial": "주문49000 → 배송비 조회",
          "expected": "주문50000 → 배송비 조회"
        }
      ],
      "items": [],
      "destinations": [],
      "receipt_label": "배송비 경계값 오류 보고서",
      "seconds": 0
    },
    {
      "step_id": "print",
      "object_id": "copier",
      "work_item_id": "TST-04",
      "title": "최신 결과물 출력",
      "instruction": "모니터에서 저장한 TST-04 문서 r1을 1부 출력하세요. 출력 중 설정 변경·중복 시작은 잠깁니다.",
      "kind": "print",
      "fields": [
        {
          "id": "document_id",
          "label": "출력 문서 ID",
          "initial": "OLD-DRAFT",
          "expected": "TST-04"
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
          "expected": "1"
        }
      ],
      "items": [],
      "destinations": [],
      "receipt_label": "배송비 경계값 오류 보고서",
      "seconds": 2
    },
    {
      "step_id": "file",
      "object_id": "cabinet",
      "work_item_id": "TST-04",
      "title": "보관 및 인계",
      "instruction": "출력 묶음을 수정요청 칸으로 옮기고 문서명과 부수를 인계하세요.",
      "kind": "handoff",
      "fields": [
        {
          "id": "title",
          "label": "인계 문서명",
          "initial": "초안",
          "expected": "배송비 경계값 오류 보고서"
        },
        {
          "id": "copies",
          "label": "인계 부수",
          "initial": "0",
          "expected": "1"
        }
      ],
      "items": [
        {
          "id": "TST-04",
          "label": "배송비 경계값 오류 보고서 1부",
          "target": "수정요청"
        }
      ],
      "destinations": [
        "수정요청",
        "재확인",
        "이전자료"
      ],
      "receipt_label": "배송비 경계값 오류 보고서",
      "seconds": 0
    }
  ]
}

닫기·초안 유지·카메라 복귀·키보드/터치·출력 중 잠금/초기화/종료와 새 시나리오 ID별 실제 React 수신을 독립적으로 검증한다. 과거 사무보조원 pass를 승계하지 않는다.

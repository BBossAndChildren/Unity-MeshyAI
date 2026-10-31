# office-assistant-v001 — 사무보조원 3D 체험
중간 빌드다. 최종 전달·사용성 검증은 [office-assistant-v003](office-assistant-v003.md)을 사용한다. v001은 후면 시작 시점, v002는 안내 표지 개선 전이다. 이전 결과를 덮어쓰지 않았다.
## 빌드·검증 근거
- Unity 6000.3.26f1 / WebGL Development Build. 51282514바이트, 162.17초, 빌드 오류 0·경고 0.
- 편집 프로젝트: `unity/projects/OfficeAssistant-v001`
- 출력: `unity/webgl/builds/office-assistant-v001`
- 소스 커밋: `308507ce0429cc85106035ee3fac367db6756c1d`; 작업 트리는 기존 변경 포함 dirty. 최종 소스 해시 목록 `docs/machine/evidence/office-assistant-v001/source-files-sha256.json`. 커밋만으로 재현 가능하다고 주장하지 않는다.
- 참고: PAN-001 v001 / PRM-001 v001 / office-shared-work v001. 기존 직업·장소 사실 검증·기획 승인 상태는 변경하지 않았다.
- 구성: AST-020 v003 원본 GLB를 Blender에서 다시 열어 Unity FBX 적용본으로 변환. 메시·팔레트·모델 원본 보존.
- 모델 집계: 17개 구성 에셋 버전, 30개 인스턴스, 4,308삼각형. 새 3D 물체 0개. 목표 5,000 대비 692삼각형 여유. UI 글자/화면 경계는 모델 메시 예산과 분리.
- 모델 공용 재질 1개, PNG 1장(v001, 2508×2508), 원본·Unity 복사본 SHA-256 일치. UI 폰트는 별도 OFL 폰트. 모델에 문서 글자나 새 이미지 텍스처를 넣지 않았다.

| 에셋 버전 | 수량 | 삼각형/개 | 장면 합계 |
|---|---:|---:|---:|
| AST-001 v002 | 1 | 220 | 220 |
| AST-002 v001 | 1 | 108 | 108 |
| AST-003 v001 | 2 | 792 | 1584 |
| AST-004 v001 | 2 | 60 | 120 |
| AST-005 v001 | 2 | 48 | 96 |
| AST-006 v001 | 2 | 12 | 24 |
| AST-007 v001 | 2 | 12 | 24 |
| AST-008 v001 | 2 | 84 | 168 |
| AST-009 v001 | 1 | 144 | 144 |
| AST-010 v001 | 3 | 308 | 924 |
| AST-011 v001 | 3 | 72 | 216 |
| AST-012 v001 | 2 | 76 | 152 |
| AST-013 v001 | 2 | 12 | 24 |
| AST-014 v001 | 2 | 96 | 192 |
| AST-015 v001 | 1 | 60 | 60 |
| AST-016 v001 | 1 | 168 | 168 |
| AST-017 v001 | 1 | 84 | 84 |

AST-020 v003은 위 구성의 소스 컨테이너이며 추가 수량·삼각형으로 합산하지 않는다. 프리팹 정의도 장면 인스턴스와 중복 합산하지 않는다. 전체 후보·각 에셋 실제 사용 조회는 [AST-001-v002-unity-office-v001](../assets/AST-001-v002-unity-office-v001.md), [AST-002-v001-unity-office-v001](../assets/AST-002-v001-unity-office-v001.md), [AST-003-v001-unity-office-v001](../assets/AST-003-v001-unity-office-v001.md), [AST-004-v001-unity-office-v001](../assets/AST-004-v001-unity-office-v001.md), [AST-005-v001-unity-office-v001](../assets/AST-005-v001-unity-office-v001.md), [AST-006-v001-unity-office-v001](../assets/AST-006-v001-unity-office-v001.md), [AST-007-v001-unity-office-v001](../assets/AST-007-v001-unity-office-v001.md), [AST-008-v001-unity-office-v001](../assets/AST-008-v001-unity-office-v001.md), [AST-009-v001-unity-office-v001](../assets/AST-009-v001-unity-office-v001.md), [AST-010-v001-unity-office-v001](../assets/AST-010-v001-unity-office-v001.md), [AST-011-v001-unity-office-v001](../assets/AST-011-v001-unity-office-v001.md), [AST-012-v001-unity-office-v001](../assets/AST-012-v001-unity-office-v001.md), [AST-013-v001-unity-office-v001](../assets/AST-013-v001-unity-office-v001.md), [AST-014-v001-unity-office-v001](../assets/AST-014-v001-unity-office-v001.md), [AST-015-v001-unity-office-v001](../assets/AST-015-v001-unity-office-v001.md), [AST-016-v001-unity-office-v001](../assets/AST-016-v001-unity-office-v001.md), [AST-017-v001-unity-office-v001](../assets/AST-017-v001-unity-office-v001.md), [AST-020-v003-unity-office-v001](../assets/AST-020-v003-unity-office-v001.md)에 보존했다.

빌드 성공·보존된 중간 실행본이다. 필수 사례 전체 실행 pass를 이 빌드에 기록하지 않는다. 최종 v003 결과를 자동 승계하지 않는다.

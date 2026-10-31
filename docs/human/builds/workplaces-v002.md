# workplaces-v002 — 전체 공간 중간 빌드

71개 실제 3D 공간을 포함하는 Unity WebGL 중간 빌드다. 모델·시나리오·통신·실행 검수의 완료 범위를 구별한다. 후속 수정 빌드와 이전 결과물을 별도 build_id로 보존한다.

| 항목 | 실제 기록 |
|---|---|
| Unity | 6000.3.26f1 |
| 실제 빌드 결과 | Succeeded |
| 일시 | 2026-10-31T05:59:28.9262553+09:00 |
| 크기 | 54175122바이트(Unity 보고) |
| 오류·경고 | 0 / 1 |
| Unity 빌드 실행 시간 | 110.60367199999999초 |
| 소스 HEAD | `308507ce0429cc85106035ee3fac367db6756c1d` + 미커밋 변경 |
| 프로젝트 | `unity/projects/OfficeAssistant-v001` |
| 출력 | `unity/webgl/builds/workplaces-v002` |
| 포함 에셋 버전 집합 | 319버전(조립 부모와 구성 소품은 삼각형 합계에서 중복 집계하지 않음) |

[빌드 근거](../../machine/evidence/workplaces-v002/build-result.json), [실제 고정 공간·에셋 참조](../../machine/evidence/workplaces-v002/registry-source.json). 전체 직업 시나리오 초안·미선택 대안을 자동 확정하지 않았다.

개별 공간 Unity 조사 JSON은 같은 evidence 폴더의 PAN-001~PAN-071-unity-scene.json이다. 이 조사는 실제 배치·메시·삼각형·재질·팔레트 확인이며 Unity Editor Play/HTTP WebGL 실행 통과를 자동 의미하지 않는다. 실제 실행 보고가 없는 항목은 미검증이다.

검수 상태: 현재 이 문서에서 실행 pass를 등록하지 않는다. 새 빌드에 과거 대표 공간·이전 빌드의 pass를 승계하지 않는다. 최종 전달 ZIP은 후속 최종 빌드 ID로 분리하며 이 중간본 package_path는 null이다.

로컬 HTTP 실행:

```powershell
python -m http.server 8178 --bind 127.0.0.1 --directory unity/webgl/builds
```

[실행 주소](http://127.0.0.1:8178/workplaces-v002/). index.html 더블클릭은 검수 대상이 아니다. 압축 없는 WebGL 출력이며 wasm은 application/wasm으로 제공한다. 신규 유료 서비스·런타임 GLB 로더 의존성은 없다. Unity 편집 프로젝트와 원본 모델은 전달 WebGL과 분리했다.

이번 Meshy·유료 이미지 생성 호출0회, 이번 크레딧0. 과거 생성 비용은 이번 비용과 별도다. 입력·캐시·출력 토큰과 작업별 시간·과금 배분·승인 잔여 예산은 미측정/미확인(null)이다.

# 전체71개 공간 실행본

현재71공간 전달 기준: [workplaces-v006](../../docs/human/builds/workplaces-v006.md) — 현재319모델(248소품+71조립),805배치, 실제Native/HTTP71/71·시각71쌍·사무보조원구현범위 통과. v005이하는보존중간본이며 다른551직업초안은별도다.

현재 전체 공간 빌드는 `workplaces-v005`이며 구체적인 실제 검수 범위는 [빌드 보고](../../docs/human/builds/workplaces-v005.md)를 따른다. 편집 프로젝트는 `unity/projects/OfficeAssistant-v001`, 출력은 `unity/webgl/builds/workplaces-v005`로 분리한다. 과거 office-assistant 데모와 workplaces 중간본은 보존했다.

```powershell
python -m http.server 8178 --bind 127.0.0.1 --directory unity/webgl/builds
```

[공간 실행](http://127.0.0.1:8178/workplaces-v005/) · [React수신 예제](http://127.0.0.1:8178/workplaces-v005/receiver/). 최종ZIP/manifest/추출 실행 확인은 빌드 보고의 실제 완료 상태를 참조한다.

---

# WebGL 배포 영역

- builds/<build_id>/: index.html과 WebGL 종속 파일 전체.
- packages/<build_id>.zip: 전달 패키지.
- 편집용 Unity 프로젝트는 별도 ../projects/에 둡니다.
- 빌드와 ZIP은 로컬 생성물로 Git에서 제외합니다.

[전달 절차](../../docs/human/guides/webgl-delivery.md)

사무보조원 최종 실행본: `builds/office-assistant-v003/`. 전달 ZIP: `packages/office-assistant-v003.zip`. 실행 방법·검증 범위는 `docs/human/builds/office-assistant-v003.md`. 이전 v001/v002 빌드는 보존된 중간 결과다.

최신 추천 실행본: `builds/office-assistant-v005/`. 물건 확대·종이 팝업을 제공하며 이전 빌드는 보존한다. 전달 ZIP: `packages/office-assistant-v005.zip`.

## 최신 공간 보강 workplaces-v009

[검수 보고](../../docs/human/builds/workplaces-v009.md), `builds/workplaces-v009/`, `packages/workplaces-v009.zip`. 실제 Unity WebGL21검사 통과; 게임 전체/다른 장치/Editor Play Mode는 이번 변경에서 미검증.

<!-- spatial-diversity-v011 -->
- 최신 공간 디테일: `builds/workplaces-v011`, `packages/workplaces-v011.zip`; 69변경+교회/성당보존, 전체71공간HTTP검수. 전체 직업 미니게임 완료와 구분.

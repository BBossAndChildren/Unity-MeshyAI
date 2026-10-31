# React 공간 명세 조회 및 Unity 연결

작성일: 2026-10-31. 현재 구현은 [React 예제](../../../web/scene-browser/README.md)에서 관리한다. 이 안내는 사람이 자료를 찾고 화면을 사용하는 방법이며, 에셋·배치·검수의 별도 원장을 만들지 않는다.

## 화면 사용

현재 로컬 실행 주소: [공간 명세 조회](http://127.0.0.1:5174/). 로컬 개발 서버가 실행 중일 때만 접근할 수 있다.

1. 검색창에 공간 이름·분류·PRM 또는 PAN ID를 입력한다.
2. 목록에서 공간을 선택한다. `?scene=PRM-009`처럼 주소로도 특정 명세를 열 수 있다.
3. 등록된 참고 이미지, 공간 설명, 핵심 소품, 배치 의도와 상세 제작 프롬프트를 확인한다.
4. **소품 상세 명세 불러오기**를 누르면 해당 장면에 연결된 소품 후보가 표시된다. 후보를 펼쳐 구성 부품·제작 방식·재사용 조건을 확인한다.
5. **전체 원본 명세 · 사용 후보 및 실제 사용 이력**을 펼치면 후보의 전체 공간 연결과 기록된 실제 사용 근거를 조회할 수 있다. 원본 명세의 기록 시점과 최신 배치 원장을 구분한다.
6. **호출 코드 보기**로 React에서 Unity에 전달할 메시지 형식을 확인한다.

현재 조회 대상은 **71개 공간, 참고 이미지 71장, 소품 후보 262종**이다. 종교시설은 PRM-064 v002 기독교(개신교) 예배실 — 목사, PRM-070 v001 불교 법당 — 스님, PRM-071 v001 천주교 성당 — 신부님으로 구분한다. 후보 수는 완성 모델 수가 아니다.

PAN-001에는 AST-020 v003의 실제 GLB 검수 수치(4,308삼각형·30개 배치·3,608,484바이트)를 표시한다. 다른 공간의 계획 소품 수량은 임의로 확정하지 않는다.

## 원본과 화면 데이터

| 자료 | 기준 위치 | 역할 |
|---|---|---|
| 공간 상세 명세 | [panorama-prompts-v002.json](../../machine/catalog/panorama-prompts-v002.json) | 고정 PRM ID·버전, 설명·배치·프롬프트 |
| 참고 이미지 | [panoramas.json](../../machine/catalog/panoramas.json) | PAN ID·버전, 실제 원본 경로·해시 |
| 소품 후보 상세 | [workplace-asset-candidates-v003.json](../../machine/catalog/workplace-asset-candidates-v003.json) | 장면별 후보 ID, 부품·재사용·전체 사용 후보 |
| 이미지 제작 기록 | [panorama-generation-v001.json](../../machine/catalog/panorama-generation-v001.json) | 참고 이미지 제작·검토 기록 |
| 실제 등록 모델 | [assets.json](../../machine/catalog/assets.json) | 실제 AST ID·버전과 결과물 경로 |
| Blender/GLB 조립 이력 | [scene-assemblies.json](../../machine/catalog/scene-assemblies.json) | 조립 revision과 실제 배치·검수 근거 |
| React 공간 조회 스냅샷 | [scenes.json](../../../web/scene-browser/public/scenes.json) | 화면에서 사용할 공간 목록·이미지·명세 연결 |
| React 소품 조회 스냅샷 | [asset-specs.json](../../../web/scene-browser/public/asset-specs.json) | 버튼 클릭 시 읽는 소품 상세 |

PRM은 기획 명세 ID, PAN은 등록 참고 이미지 ID, AST는 실제 모델 ID다. 표시 이름이나 숫자가 같다는 이유로 연결하지 않고 원본 참조를 따른다. 이미지 등록·시각 검토·모델 제작·실제 배치·Unity 실행·사용자 승인은 별개다.

화면 스냅샷은 원본 catalog를 대체하지 않는다. 최신 실제 사용은 원장의 최신 revision을 조회한다. Unity 사용의 원장은 등록된 경우 asset-usages.json이며 Blender 배치를 Unity 실행으로 기록하지 않는다.

## 실행 및 갱신

처음 실행할 때 `web/scene-browser` 폴더에서 다음 명령을 사용한다.

```powershell
npm ci
npm run dev
```

출력된 localhost 주소를 연다. 5174는 현재 세션의 포트이며 실행 환경에 따라 달라질 수 있다.

원본 명세·이미지 목록을 변경한 뒤 저장소 루트에서 다음 순서로 갱신한다.

```powershell
python -X utf8 web/scene-browser/scripts/sync_catalog.py
npm --prefix web/scene-browser run build
```

[동기화 스크립트](../../../web/scene-browser/scripts/sync_catalog.py)는 원본 catalog를 수정하지 않고, 등록 이미지의 SHA-256을 확인해 화면용 이미지와 두 JSON 스냅샷을 갱신한다. 현재 React의 Unity 연결 설정과 모델 메타데이터는 보존하므로 모델 버전·검수 수치가 바뀌면 실제 원장을 대조해 별도로 갱신한다. 입력 catalog 버전이 바뀌면 스크립트의 고정 출처도 확인한다. 자동 훅은 설치하지 않았다.

`npm run build`의 결과는 React 정적 배포본이며 Unity WebGL 빌드가 아니다.

## Unity 호출 및 공유 구조

목표 구조는 **React 명세 조회 화면 + Unity 공용 실행기 하나 + 공용 Addressables 에셋 + 공간별 콘텐츠**다. React의 명세 선택만으로 Unity를 다운로드하지 않으며 실행 버튼으로 로딩을 시작한다. 공간을 바꿀 때 실행기를 새로 만들지 않고 장면 ID와 콘텐츠 버전을 전달한다.

```javascript
// 아래 콘텐츠 버전을 실제로 발행하고 Unity 허용 목록에 등록한 후 사용한다.
unityInstance.SendMessage(
  'SceneBridge',
  'OpenScene',
  JSON.stringify({
    sceneId: 'PAN-001',
    contentVersion: 'v001',
    requestId: crypto.randomUUID()
  })
);
```

콘텐츠 버전은 Blender 에셋 버전과 별개다. 예시의 v001은 실제 발행 완료를 뜻하지 않는다. Unity 쪽 브리지는 허용된 ID·버전에 해당하는 Addressables 장면만 로드하고 ready/loaded/error 응답을 React로 전달한다.

실제 연결 파일과 설정 절차:

- [React 호출부](../../../web/scene-browser/src/unity.js)
- [React 화면](../../../web/scene-browser/src/main.jsx)
- [Unity 수신부](../../../web/scene-browser/unity-example/SceneBridge.cs)
- [Unity → 브라우저 응답](../../../web/scene-browser/unity-example/SceneEvents.jslib)
- [빌드 URL 설정 예시](../../../web/scene-browser/public/unity-config.example.json)
- [Unity 프로젝트 준비·Addressables·배포 헤더·연결 순서](../../../web/scene-browser/README.md)

## 확인한 범위

71개 공간의 상세 명세·등록 이미지 대응과 원본 해시, 262개 소품 후보 ID 참조, React production build를 확인했다. 브라우저에서 검색·장면 전환·상세 프롬프트·PRM-063 이미지 및 소품 후보 로딩을 확인했다. SendMessage 계약은 fake player로 검사했다.

Unity 프로젝트·WebGL 실행기·Addressables 번들은 준비되지 않았다. C# 컴파일, Unity 장면 전환, 캐시·메모리 및 다운로드 절감량은 **미검증**이다. 실행 버튼은 연결 전 비활성화 상태다. Meshy 호출·크레딧은 이번 조회 화면 작업에서 0이며 실제 대화 토큰은 도구 미제공으로 미측정이다.

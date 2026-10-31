# React 장면 명세·Unity 연결 예제

## 지금 실행

이 폴더에서 `npm ci`, `npm run dev`를 실행하고 출력된 localhost 주소를 연다. 현재 세션에서는 http://127.0.0.1:5174/ 에서 실행 중이다. `npm run build`는 React 정적 배포 파일을 dist/에 만든다. Unity를 빌드하는 명령이 아니다.

검색 → 장면 선택 → 명세 확인 → 호출 코드 보기를 사용할 수 있다. URL의 `?scene=PRM-001`로 명세를 직접 선택한다. 검색·선택은 Unity 다운로드를 시작하지 않는다. 실제 Unity 실행은 연결 후 두 실행 버튼으로 수행한다.

public/scenes.json은 panorama-prompts-v002.json의 71개 실제 항목과 PAN-001 AST-020 v003 검수 기록을 읽어 만든 조회용 스냅샷이다. 종교시설은 PRM-064 v002 개신교 예배실, PRM-070 v001 불교 법당, PRM-071 v001 천주교 성당으로 분리되었으며 등록된 PAN-064/PAN-070/PAN-071 v001 이미지를 연결했다. PRM은 기획 명세 ID이고 PAN은 등록 이미지/공간 연결 ID이며 서로 대체하지 않는다. 원장 변경 시 이 스냅샷도 갱신해야 한다. 공용 에셋 사용처나 직업별 후보 원장을 대체하지 않는다.

## 정확한 호출 계약

```javascript
// Unity 콘텐츠를 아래 버전으로 실제 발행하고 SceneBridge에 등록한 뒤 사용.
// v001은 설명용 콘텐츠 버전이며 Blender 모델 v003과 별개다.
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

src/unity.js가 실제 SendMessage 호출을 담당한다. src/main.jsx가 검색·선택·공용 실행기 시작·명령 전송·Unity 응답 표시를 담당한다. 명세 화면의 '미빌드' 값은 현재 실행할 콘텐츠 버전이 없음을 뜻하며 실제 Unity 로딩 키가 아니다.

## Unity에 연결하는 순서

1. Unity 프로젝트에 Addressables를 설치한다. unity-example/SceneBridge.cs를 Assets/Scripts/에, SceneEvents.jslib를 Assets/Plugins/WebGL/에 복사한다. 이 예제 폴더 자체는 Unity 프로젝트가 아니다.
2. 작은 Bootstrap 장면을 만든다. 루트 GameObject 하나에 SceneBridge를 붙인다. 이 오브젝트 이름은 Awake에서 SceneBridge가 된다. Bootstrap만 기본 플레이어 시작 장면에 포함한다. 브리지는 하나만 둔다.
3. 실제 PAN-001 Unity 콘텐츠 장면을 만든다. 콘텐츠 장면에는 SceneBridge를 추가하지 않는다. 공용 카메라를 Bootstrap에 두면 콘텐츠 장면의 중복 카메라·AudioListener를 제거한다.
4. PAN-001 장면을 Addressable로 등록한다. 예시 주소는 `spaces/PAN-001/v001`이다. SceneBridge Inspector의 Allowed Scenes에 sceneId=`PAN-001`, contentVersion=`v001`, addressableKey=`spaces/PAN-001/v001`을 등록한다. React는 임의 URL/키를 넘기지 않고 이 허용 목록을 사용한다.
5. 공용 팔레트·재질·가구를 명시적 공유 Addressables 그룹으로 분리하고 Analyze 중복 의존성을 검사한다. Bootstrap/Resources에 같은 콘텐츠를 중복 포함하지 않는다. 같은 에셋을 각 공간용 폴더에 복사하지 않는다. 공용 코드/C# 타입은 실행기 빌드에 포함해야 하며 새 코드가 필요한 업데이트는 콘텐츠만 교체할 수 없다.
6. Addressables Web 타깃 콘텐츠를 빌드하고 RemoteLoadPath가 가리키는 서버에 catalog와 bundle을 게시한다. WebGL 실행기를 빌드해 public/unity/ 아래에 빌드 폴더 구조를 보존해 배치한다. public/unity/는 Git에서 제외했다.
7. public/unity-config.example.json의 파일명을 실제 Unity 출력 loader/data/framework/wasm 파일명으로 교체한다. Unity 생성 index.html의 config를 기준으로 하며 `.br`는 Brotli 예시일 뿐이다. 서버의 Content-Encoding/Content-Type과 CORS를 실제 빌드 설정에 맞춘다. Vite 개발 서버의 기본 정적 제공만으로 Brotli 응답 헤더가 올바르다고 가정하지 않는다. 다른 도메인의 콘텐츠는 CORS 설정이 필요하다.
8. 위 설정 객체를 public/scenes.json의 unity 필드에 넣고 enabled=true로 한다. PAN-001 항목에 contentVersion=`v001`, unityReady=true를 기록한다. 이는 배포 연결 설정이지 catalog의 승인/검수 상태 변경이 아니다. 실제 발행·연결 후에만 바꾼다.
9. React에서 'Unity 실행기 시작' → 브리지 ready 수신 → '이 공간 실행' 순서로 테스트한다. Unity는 이전 Addressable 장면을 unload한 후 새 장면을 additive로 로드한다. Bootstrap은 유지한다. 로딩 실패 시 화면이 빈 Bootstrap일 수 있으며 오류를 표시하고 재시도한다. 실행기를 장면마다 다시 만들지 않는다.

Unity 응답은 `.jslib`가 `window`의 `unity-scene-event` CustomEvent로 전달한다. type은 ready/loaded/error이며, 장면 응답의 requestId는 요청과 같아야 한다. React는 전환 중 중복 클릭을 차단하고 과거 요청 응답을 무시한다. 120초 응답 시간 초과는 UI 대기만 종료하며 Unity 내부 작업을 취소하지 않는다. 동일 페이지 단일 실행기 예제이며 다중 동시 플레이어는 지원하지 않는다. 컴포넌트를 제거할 때 런타임도 끝내려면 quitUnity()를 await한 후 canvas를 제거한다. Unity 초기화 실패 후 재시작은 페이지를 새로고침한다.

## 검증 범위

- React production build 통과, npm lockfile 보존.
- 실제 브라우저 검색(협업), 명세 변경, PAN-001 재선택, 호출 코드 표시 확인.
- SendMessage의 오브젝트/메서드/JSON 계약은 Node에서 fake player로 검사. 실제 Unity 실행 검증과 다르다.
- Unity 프로젝트·WebGL 실행기·Addressables 번들 없음. C# 컴파일, Unity 전환·캐시·메모리·다운로드 절감량은 미검증이다. UI 실행 버튼은 disabled로 유지했다.
- Meshy 유료 호출 0회/0크레딧. 작업별 실제 대화 토큰은 도구 미제공으로 null(미측정). 모델·기획 승인 상태 변경 없음, 커밋·푸시 없음.

공식 API: [Unity 브라우저 연결](https://docs.unity3d.com/cn/6000.0/Manual/web-templates-build-configuration.html), [Addressables LoadSceneAsync](https://docs.unity3d.com/kr/Packages/com.unity.addressables%401.21/api/UnityEngine.AddressableAssets.Addressables.LoadSceneAsync.html), [UnloadSceneAsync](https://docs.unity3d.com/kr/Packages/com.unity.addressables%401.21/api/UnityEngine.AddressableAssets.Addressables.UnloadSceneAsync.html).

종교 3종 최신 상세 명세의 배치 의도와 전체 프롬프트도 화면에서 확인할 수 있다. 이미지 해시는 원본 catalog와 대조했다. 명세 반영은 모델 제작·Unity 검증 완료를 의미하지 않는다.

## 전체 명세 동기화

71개 전체 장면에 등록된 참고 이미지(원본 SHA-256 확인), 공간 설명, 핵심 소품, 배치 의도, 전체 프롬프트, 이미지 검토 기록을 연결했다. 최신 workplace-asset-candidates-v003.json의 262개 후보 명세를 별도 asset-specs.json으로 내보내고 장면별 required_candidate_ids로 조회한다. 상세는 버튼 클릭 시 지연 로딩한다. 원본 명세 전체에 사용 후보와 실제 사용 근거를 보존하며 계획 후보를 완료 모델로 승격하지 않는다. 후보 문서의 사용 기록은 해당 문서 시점의 스냅샷이며 최신 실제 배치는 scene-assemblies 원장을 기준으로 한다.

재동기화: 저장소 루트에서 `python -X utf8 web/scene-browser/scripts/sync_catalog.py` 실행 후 앱 폴더에서 `npm run build`. 스크립트는 원본 catalog를 수정하지 않으며 현재 React의 Unity 연결 설정과 모델 메타데이터를 유지한다. 입력 목록 버전이 바뀌면 스크립트의 고정 출처도 확인해야 한다.

검증: 71개 상세/이미지 대응 및 해시, 262개 후보 ID 참조, React production build 확인. 브라우저 PRM-063 실제 이미지 로딩과 개별 후보 8개 표시 확인. Meshy 호출 0, 크레딧 0. 실제 대화 토큰 null(도구 미제공). Unity 빌드 및 실행 검증은 수행하지 않았다.

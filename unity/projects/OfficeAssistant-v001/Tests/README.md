# 게임 검증 재실행

이 폴더는 게임의 수용 사례를 명시적으로 실행하는 도구다. 에이전트 규칙 검사나 자동 시작 훅은 설치하지 않는다.

Unity Editor Play Mode 검증은 저장소 루트에서 다음과 같이 실행한다. 러너가 결과를 쓰고 Unity를 종료하므로 `-quit`를 함께 넣지 않는다.

```powershell
& $UnityEditor -batchmode -nographics -projectPath (Resolve-Path unity/projects/OfficeAssistant-v001) -executeMethod OfficeEditorPlay.Run -logFile office-editor-play.log
```

실제 WebGL UI 검증은 HTTP 서버와 Playwright가 필요하다. Playwright는 별도 작업 폴더에 설치하고 `PLAYWRIGHT_MODULE`에 설치된 모듈 경로를 지정할 수 있다. `CHROME_PATH`는 Chrome 실행 파일 경로이며 생략하면 Windows의 기본 Chrome 설치 경로를 사용한다.

```powershell
node unity/projects/OfficeAssistant-v001/Tests/webgl-smoke.cjs office-assistant-v005
```

서버 주소는 `http://127.0.0.1:8173/`이며 실행 결과는 `docs/machine/evidence/office-assistant-v005/webgl-ui-acceptance.json`과 캡처에 기록한다. 재실행 전 기존 검증 보고를 보존한다. 물건 표면 클릭·UI 입력과 키보드 입력을 사용하며, 게임 상태를 완료로 강제 변경하지 않는다. WebGL C# 독립 사례 검증은 별도 세션을 사용해 플레이어 상태를 변경하지 않는다.

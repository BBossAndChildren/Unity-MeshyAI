# AST-001 v001 — COM-01 둥근 모서리 바닥판 베타

- 생성일: 2026-10-31 (Asia/Seoul)
- 도구: Meshy CLI 0.4.0 / text-to-3d preview / meshy-t2 smart-topology
- 작업 ID: `01a18d7c-b098-7005-b332-8069df276312`
- 실제 소비: 5크레딧. 유료 생성 1회, 재생성 없음.
- 요청 설정·전체 프롬프트: [request.json](request.json)
- 원본: [model.glb](model.glb), 440삼각형, 8,656바이트.
- 사용 조건: Meshy 계정에 적용되는 라이선스 조건은 별도 확인 필요. CC0 등으로 추정하지 않음.
- 디자인 참고: PAN-001 v001의 바닥판. 이미지 자체를 API에 업로드하지 않고 텍스트로 생성.

요청은 비어 있는 둥근 모서리 정사각형 바닥판, 평평한 윗면·아랫면, 얇은 두께였다. 결과는 원형에 가까운 슬래브였고 요청 면 수 400보다 실제 면 수가 많았다. 원본은 보존했다. Blender에서 원본 정점을 둥근 정사각형으로 변형하고 평면화 및 볼록 외피 복구를 수행했다. 별도 수작업 모델을 Meshy 결과로 가장하지 않았다.

CLI 다운로드는 완료 JSON 및 파일을 기록한 뒤 Windows 종료 assertion을 출력했다. 다운로드 성공 여부는 종료 코드만으로 판단하지 않고 실제 GLB의 Blender 로드로 확인했다.

## 미리보기

- [Meshy 원본](previews/meshy.png)
- [Blender 후처리](previews/blender.png)
- [실제 웹 표시](previews/web.jpg)

상세 결과: [베타 검수 보고](../../../../../docs/human/assets/AST-001-v001.md)

# 원본 이미지 목록

사무실 v2 참고 이미지 5장(PAN-001~PAN-005, v001)이 등록되었습니다. [등록 상세](office-v2-registration.md)

사무실 파노라마 5장은 공간 구성·가구·소품 배치를 확인하는 참고용입니다. 파노라마 이미지의 신규 생성·재생성이나 이미지 전체를 하나의 3D 모델로 생성하는 작업은 대상에 포함하지 않습니다. 향후 생성 대상은 개별 가구·소품이며, 배치할 때 이 이미지를 참고합니다.

| 분류 | 보관 위치 | 전체 목록 |
|---|---|---|
| 파노라마 | images/original/panoramas/ | [panoramas.json](../../machine/catalog/panoramas.json) |
| 에셋 제작용 이미지 | images/original/assets/ | [asset-images.json](../../machine/catalog/asset-images.json) |

목록에는 ID·버전·이름·파일 경로·원본 해시·이미지 크기·출처·사용 조건·용도를 기록합니다. 파노라마에는 투영 형식도 기록합니다.
파일 경로는 저장소 루트 기준입니다. 실제 파일이 제공되기 전에 가짜 항목이나 빈 이미지 파일을 등록하지 않습니다.

등록 순서:
1. 에셋 이미지는 IMG-001, 파노라마는 PAN-001처럼 ID를 부여합니다.
2. 해당 분류의 <image_id>/<version>/ 폴더에 원본을 저장합니다.
3. 파일의 SHA-256과 실제 이미지 크기를 확인해 해당 JSON 목록에 등록합니다.
4. 모델 제작에 사용한 경우 assets.json의 source_images에 이미지 ID·버전 참조를 추가합니다.

어떤 모델에서 사용했는지는 assets.json의 source_images를 검색합니다.
상세 필드 규칙은 [AGENTS.md](../../../AGENTS.md)를 따릅니다.

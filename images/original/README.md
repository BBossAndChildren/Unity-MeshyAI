# 원본 이미지

```text
original/
  panoramas/<image_id>/<version>/   파노라마 원본 (PAN-001 등)
  assets/<image_id>/<version>/      에셋 제작용 원본 이미지 (IMG-001 등)
```

원본은 그대로 보존하고 변경 시 새 버전으로 등록합니다.
에셋 이미지는 [asset-images.json](../../docs/machine/catalog/asset-images.json), 파노라마는 [panoramas.json](../../docs/machine/catalog/panoramas.json)에 등록합니다.
모델 제작에 사용하면 assets.json의 source_images에서 이미지 ID와 버전을 참조합니다.
이 이미지들은 제작·참고 자료이며 공용 채색 텍스처 color1/color2와 별도로 관리합니다.

사무실 v2 참고 이미지 5장(PAN-001~PAN-005, v001)이 등록되었습니다. [이미지 목록 안내](../../docs/human/images/README.md)

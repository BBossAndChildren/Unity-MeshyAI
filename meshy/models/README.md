# 모델 저장 영역

```text
models/
  original/<asset_id>/<version>/   원본·README.md·previews/
  blender/<asset_id>/<version>/    Blender 수정본 .blend
    exports/                      실제 사용할 모델
  textures/
    color1.jpg                    기본 채색용 공용 팔레트
    color2.jpg                    강조·원색용 보조 팔레트
```

모델은 color1으로 기본 채색하고, 필요한 부분에만 color2를 추가합니다.
원본을 보존하며 Unity에는 exports/의 실제 사용본을 적용합니다.
[텍스처 안내](textures/README.md)

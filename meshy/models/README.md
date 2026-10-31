# 모델 저장 영역

```text
models/
  original/<에셋 ID>/<버전>/       Meshy 결과 또는 직접 제작 source.blend·제작 기록·미리보기
  blender/<에셋 ID>/<버전>/
    model.blend                  수정본
    exports/model.glb            최종 실제 사용본
    processing/                  재사용 제작·후처리 스크립트
    inspection.json              GLB·삼각형·용량·웹 검수 기록
  textures/
    color1.jpg                   기본색 원본 보존
    color2.jpg                   강조색 원본 보존
    palettes/<팔레트 버전>/
      palette.png                실제 사용하는 정사각형 한 장
      mapping.json               원본 칸과 UV 대응표
```

실제 모델은 공용 PNG 한 장과 공용 재질을 사용합니다. 원본 파일·수정본·내보내기 결과를 구분합니다.
[팔레트 안내](textures/README.md) · [제작 기준 요약](../../docs/human/guides/web-lowpoly.md)

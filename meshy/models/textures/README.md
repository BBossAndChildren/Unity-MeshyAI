# 팔레트 원본과 최종 공용 텍스처

| 원본 | 역할 |
|---|---|
| [color1.jpg](color1.jpg) | 피부·옷·몸통·지형 등 넓은 기본 면의 파스텔 색 |
| [color2.jpg](color2.jpg) | 강조선·눈·입·작은 장식·포인트의 원색·대비색 |

두 원본은 그대로 보존합니다. 실제 모델에는 두 원본 칸을 함께 담은 정사각형 PNG 한 장을 사용합니다.

```text
textures/
  color1.jpg
  color2.jpg
  palettes/<버전>/
    palette.png    색 변화 없이 합친 최종 공용 텍스처
    mapping.json   원본·행·열·최종 UV 대응표
```

보간·색상 보정·손실 압축 없이 원본 칸을 재배치하고 글자·격자선·무늬·그림자를 추가하지 않습니다.
기본 면은 color1 출처 칸, 강조 영역은 color2 출처 칸을 UV로 선택합니다. 색상 수를 4개로 제한하지 않습니다.
Unity에는 최종 PNG를 Assets/Shared/Textures/<팔레트 버전>/에 동일 바이트로 복사해 공유합니다.

[원본 목록](../../../docs/machine/catalog/shared-textures.json) · [최종 팔레트 목록](../../../docs/machine/catalog/palettes.json) · [제작 기준 요약](../../../docs/human/guides/web-lowpoly.md)

현재 최종 PNG와 대응표는 아직 생성되지 않았습니다.

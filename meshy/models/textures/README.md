# 공용 텍스처 사용 기준

| 파일 | 역할 | 사용 기준 |
|---|---|---|
| [color1.jpg](color1.jpg) | 기본 채색 | 모든 모델의 일반적인 채색에 우선 사용 |
| [color2.jpg](color2.jpg) | 강조·원색 | 강조 부분이나 선명한 원색이 필요할 때만 보조로 사용 |

두 파일은 사용자가 제공한 원본입니다. 임의 색상 변경·교체·추가 텍스처 제작을 하지 않습니다.
기본 에셋은 color1만 참조하고, color2가 필요한 에셋은 두 파일을 참조하며 accent_reason에 이유를 적습니다.
모델별 텍스처를 만들지 않고 공용 팔레트에 UV와 재질을 맞춥니다.
Unity에서는 사용한 파일을 Assets/Shared/Textures/에 동일 바이트로 한 번씩 복사해 공유합니다.

[기계용 텍스처 목록](../../../docs/machine/catalog/shared-textures.json)

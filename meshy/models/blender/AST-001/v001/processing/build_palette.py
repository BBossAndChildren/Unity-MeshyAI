"""Rearrange original decoded pixels without interpolation or recoloring."""
from pathlib import Path
from PIL import Image
import hashlib, json
ROOT = Path(__file__).resolve().parents[6]
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
out = ROOT/'meshy/models/textures/palettes/v001'
out.mkdir(parents=True, exist_ok=True)
if (out/'palette.png').exists(): raise SystemExit('Existing palette preserved; use a new version.')
images = [Image.open(ROOT/f'meshy/models/textures/color{i}.jpg').convert('RGB') for i in (1,2)]
assert images[0].size == images[1].size == (1254,1254)
w=1254; size=2*w
atlas=Image.new('RGB',(size,size))
for j,img in enumerate(images):
    atlas.paste(img,(j*w,0)); atlas.paste(img,(j*w,w))
atlas.save(out/'palette.png',optimize=True)
cells=[]; sources=[]
for k,img in enumerate(images):
    tid=f'color{k+1}'; sources.append(dict(texture_id=tid,sha256=sha(ROOT/f'meshy/models/textures/{tid}.jpg'),width=w,height=w))
    for row in range(16):
        for col in range(16):
            x0=round(col*w/16); x1=round((col+1)*w/16)
            y0=round(row*w/16); y1=round((row+1)*w/16)
            x=(x0+x1)//2; y=(y0+y1)//2
            cells.append(dict(texture_id=tid,row=row,column=col,source_rect_px=[x0,y0,x1-x0,y1-y0],source_sample_px=[x,y],target_rect_px=[k*w+x0,y0,x1-x0,y1-y0],uv_center=[(k*w+x+.5)/size,1-(y+.5)/size],rgb=list(img.getpixel((x,y)))))
mapping=dict(schema_version=3,palette_version='v001',palette_sha256=sha(out/'palette.png'),width=size,height=size,sources=sources,cells=cells,layout_note='Top-left color1, top-right color2; bottom half exact duplicates for square layout. No resampling.',pixel_preservation_verified=all(atlas.crop((k*w,0,(k+1)*w,w)).tobytes()==im.tobytes() for k,im in enumerate(images)))
(out/'mapping.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2),encoding='utf-8')
catalog=ROOT/'docs/machine/catalog/palettes.json'; data=json.loads(catalog.read_text(encoding='utf-8-sig'))
assert not any(p['version']=='v001' for p in data['palettes'])
data['palettes'].append(dict(version='v001',path=(out/'palette.png').relative_to(ROOT).as_posix(),mapping_path=(out/'mapping.json').relative_to(ROOT).as_posix(),width=size,height=size,sha256=sha(out/'palette.png'),source_texture_ids=['color1','color2']))
catalog.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print(json.dumps({'resolution':size,'bytes':(out/'palette.png').stat().st_size,'original_pixels_preserved':mapping['pixel_preservation_verified']}))

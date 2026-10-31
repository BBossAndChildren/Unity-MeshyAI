"""Export eight physically separated usable props from one generated scene.
Original geometric component membership is recorded per exported asset.
"""
import bpy,json,math,copy,importlib.util
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parents[6]
spec=importlib.util.spec_from_file_location('e',R/'meshy/models/blender/AST-2064/v003/processing/enrich_worship.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e);s=e.s
e.SCRIPT=Path(__file__).relative_to(R).as_posix();OUT=R/'docs/machine/evidence/shared-decor-v001'
render_original=e.render;e.render=lambda *a,**k:None
GROUPS=[(3007,'넓은 잎 화분',[3,4,5,6,7,8,9,10,11,12,13,14],.82,'plant'),(3008,'짜임 바구니',[0],.27,'basket'),(3009,'접어 세운 패브릭',[1],.45,'textile'),(3010,'가지 장식 꽃병',[2],.72,'branches'),(3011,'고리형 조형 소품',[15],.32,'sculpture'),(3012,'얕은 도자기 그릇',[16],.08,'bowl'),(3013,'잎 가지 꽃병',[17,18,19,20]+list(range(22,33)),.8,'ivy'),(3014,'곡선 손잡이 피처',[21],.38,'pitcher')]
records=[]
for number,name,indices,height,kind in GROUPS:
    bpy.ops.wm.open_mainfile(filepath=str(OUT/'separated-source.blend'));keep=[f'Kit component {i:02}'for i in indices]
    for o in list(bpy.context.scene.objects):
        if o.type!='MESH' or o.name not in keep:bpy.data.objects.remove(o,do_unlink=True)
    obs=e.meshes();lo,hi=e.bounds(obs);base=Vector(((lo[0]+hi[0])/2,(lo[1]+hi[1])/2,lo[2]));scale=height/(hi[2]-lo[2])
    # Reset the shared material after opening a file, then assign original cells.
    s.MATERIAL=obs[0].data.materials[0]
    for o in obs:
        bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.transform_apply(location=True,rotation=True,scale=True);o.select_set(False)
        for v in o.data.vertices:v.co=(v.co-base)*scale
        o.data.update();s.paint(o,'green' if kind in ['plant','ivy'] and '03' not in o.name and '17' not in o.name else 'cream')
    bpy.ops.object.select_all(action='DESELECT')
    for o in obs:o.select_set(True)
    bpy.context.view_layer.objects.active=obs[0];bpy.ops.object.join();o=bpy.context.object;o.name=name
    mod=o.modifiers.new('Reusable prop budget','DECIMATE');mod.ratio=510/max(1,e.triangles([o]));bpy.ops.object.modifier_apply(modifier=mod.name)
    mod=o.modifiers.new('Stable triangles','TRIANGULATE');bpy.ops.object.modifier_apply(modifier=mod.name);s.paint(o,'cream');o.data.update()
    for p in o.data.polygons:
        z=p.center.z
        color='green' if kind in ['plant','ivy'] and z>height*.28 else 'wood' if kind=='basket' else 'teal' if kind=='textile' else 'cream' if kind in ['plant','ivy','bowl','sculpture'] else 'teal'
        e.uvcolor(o,p,color)
    if kind in ['plant','ivy']:
        # Thin source stems may disappear under voxel reduction. Restore actual
        # connections locally rather than leaving disconnected floating leaves.
        for x,y,z in [(-.15,0,height*.73),(.12,.02,height*.82),(0,.04,height*.9)]:s.rod('Reinforced branch',(0,0,height*.2),(x,y,z),.009,'green',5)
    if kind=='branches':
        for x,y,z in [(-.18,.02,.83),(.17,.02,.91),(0,-.02,1.02)]:
            s.rod('Display branch',(0,0,height*.57),(x,y,z),.010,'wood',5)
            s.rod('Display twig',(x*.65,y,z*.86),(x+.08,y+.04,z-.04),.007,'wood',5)
    aid=f'AST-{number}';entry,report=e.save(aid,'v001',name,'prop','hybrid',0)
    entry['preview_path']=None;entry['source_pack_ref']={'pack_id':'shared-decor-kit-001','version':'v001','source_path':'meshy/models/original/DECOR-KIT-001/v001/source.glb','component_indices':indices,'meshy_task_id':'01a18fda-e5ad-74bc-8d17-aa1aab00c500'}
    entry['generation_reason']='Split one Meshy multi-prop scene by inspected components, normalize individual origins/dimensions and locally repair thin stems; batch charge20 not allocated across props.'
    cat=s.read('assets');cat['assets'][-1]=entry;s.write(e.CAT/'assets.json',cat)
    records.append(dict(asset_ref={'asset_id':aid,'version':'v001'},name=name,component_indices=indices,triangles=report['scene_triangles'],dimensions_m=report['dimensions_m'],origin='floor contact center',front='Blender -Y; rotational props have no required front',placement_status='library_only_not_placed',visual_status='unverified'))
    readme=R/entry['production_record_path'];readme.write_text(readme.read_text('utf-8')+'\n원본 묶음: DECOR-KIT-001 v001 / task01a18fda-e5ad-74bc-8d17-aa1aab00c500. 묶음 전체20크레딧이며 개별 소품 배분 미측정. 이 소품의 추가 유료 호출0. 실제 배치 미등록/미검증.\n','utf-8')
s.reset()
for index,row in enumerate(records):
    objs,a=e.import_asset(row['asset_ref']['asset_id'],'v001');root=bpy.data.objects.new('Contact '+str(index),None);bpy.context.collection.objects.link(root)
    for o in objs:
        if o.parent is None:o.parent=root
    root.location=((index%4-1.5)*1.0,(index//4)*1.15,0)
render_original(OUT/'contact.png',(5,-8,7),1000)
cat=s.read('assets')
for row in records:
    a=next(a for a in cat['assets'] if a['asset_id']==row['asset_ref']['asset_id']and a['version']=='v001');a['preview_path']='docs/machine/evidence/shared-decor-v001/contact.png'
s.write(e.CAT/'assets.json',cat);s.write(OUT/'split-manifest.json',dict(schema_version=3,pack_id='shared-decor-kit-001',version='v001',meshy_task_id='01a18fda-e5ad-74bc-8d17-aa1aab00c500',consumed_credits=20,credit_allocation_per_prop=None,source_preserved=True,props=records,unity_runtime_status='unverified',note='Reusable source library; no automatic placement or runtime pass.'))
print('DECOR_PROPS_EXPORTED',len(records),flush=True)

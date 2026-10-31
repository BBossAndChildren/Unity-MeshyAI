"""Church/cathedral repair and enrichment; preserve all previous fixed versions.
Run in Blender. Meshy flower source is retained; no new image texture is made.
"""
import bpy, json, math, copy, datetime, importlib.util, sys
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[6]
SCRIPT=Path(__file__).relative_to(ROOT).as_posix()
SHARED='meshy/models/blender/AST-1010/v001/processing/build_shared.py'
spec=importlib.util.spec_from_file_location('shared',ROOT/SHARED)
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
CAT=ROOT/'docs/machine/catalog'
EVIDENCE=ROOT/'docs/machine/evidence/worship-enrichment-v001'
F=.296
NEW=[]
def now():return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat()
def rel(p):return p.relative_to(ROOT).as_posix()
def meshes():return [o for o in bpy.context.scene.objects if o.type=='MESH']
def bounds(obs):
    bpy.context.view_layer.update()
    pts=[o.matrix_world@Vector(c) for o in obs for c in o.bound_box]
    return [min(p[k] for p in pts) for k in range(3)],[max(p[k] for p in pts) for k in range(3)]
def triangles(obs):return sum(len(p.vertices)-2 for o in obs for p in o.data.polygons)
def box(n,p,d,c='wood',b=0):return s.box(n,p,d,c,b)
def ck(ok,why):return dict(status='pass' if ok else 'fail',evidence=why,reason=None)
def uvcolor(o,p,color):
    row,col=s.COLORS[color]
    cell=next(c for c in s.MAPPING['cells'] if c['texture_id']=='color1' and c['row']==row and c['column']==col)
    for i in p.loop_indices:o.data.uv_layers.active.data[i].uv=cell['uv_center']
def import_asset(aid,version):
    assets=s.read('assets')['assets'];a=next(a for a in assets if a['asset_id']==aid and a['version']==version)
    before=set(bpy.context.scene.objects);bpy.ops.import_scene.gltf(filepath=str(ROOT/a['runtime_path']))
    objs=[o for o in bpy.context.scene.objects if o not in before]
    for o in objs:
        if o.type=='MESH':
            o.data.materials.clear();o.data.materials.append(s.MATERIAL)
            for p in o.data.polygons:p.material_index=0
    return objs,a
def render(path,direction=(6,-9,7),size=1000):
    obs=meshes();lo,hi=bounds(obs);center=(Vector(lo)+Vector(hi))*.5;span=max(Vector(hi)-Vector(lo))
    scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=32;scene.cycles.use_denoising=True
    scene.render.resolution_x=size;scene.render.resolution_y=size;scene.render.resolution_percentage=100
    scene.world=bpy.data.worlds.new('Warm neutral presentation');scene.world.use_nodes=True
    scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.72,.70,.65,1)
    scene.world.node_tree.nodes['Background'].inputs[1].default_value=.7
    for pos,power in [((-3,-4,6),900),((4,2,5),650)]:
        bpy.ops.object.light_add(type='AREA',location=center+Vector(pos));lamp=bpy.context.object;lamp.data.energy=power;lamp.data.size=5
        lamp.rotation_euler=(center-lamp.location).to_track_quat('-Z','Y').to_euler()
    bpy.ops.object.camera_add(location=center+Vector(direction));cam=bpy.context.object
    cam.rotation_euler=(center-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=span*1.22
    scene.camera=cam;scene.view_settings.view_transform='Standard';scene.render.image_settings.file_format='PNG'
    path.parent.mkdir(parents=True,exist_ok=True);scene.render.filepath=str(path);bpy.ops.render.render(write_still=True)
    for o in list(bpy.context.scene.objects):
        if o.type in ['CAMERA','LIGHT']:bpy.data.objects.remove(o,do_unlink=True)
def save(aid,v,name,kind,method,credits=0,props=None,placements=None):
    out=ROOT/f'meshy/models/blender/{aid}/{v}';src=ROOT/f'meshy/models/original/{aid}/{v}'
    if (out/'model.blend').exists():raise RuntimeError('Existing version preserved '+str(out))
    (out/'exports').mkdir(parents=True,exist_ok=True);(src/'previews').mkdir(parents=True,exist_ok=True)
    bpy.ops.object.select_all(action='DESELECT')
    for o in bpy.context.scene.objects:
        if o.type in ['MESH','EMPTY']:o.select_set(True)
    bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'));bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
    glb=out/'exports/model.glb';bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
    bpy.ops.export_scene.fbx(filepath=str(out/'exports'/('room.fbx' if kind=='diorama' else 'model.fbx')),use_selection=True,add_leaf_bones=False,bake_anim=False,axis_forward='-Z',axis_up='Y',path_mode='STRIP',use_custom_props=True)
    if placements:s.write(out/'placements.json',placements)
    s.reset();bpy.ops.import_scene.gltf(filepath=str(glb));obs=meshes();tri=triangles(obs)
    materials={m for o in obs for m in o.data.materials};textures={n.image for m in materials for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image}
    centers=[c['uv_center'] for c in s.MAPPING['cells']]
    uvok=all(o.data.uv_layers.active and all(any(abs(l.uv.x-u)<1e-5 and abs(l.uv.y-v)<1e-5 for u,v in centers) for l in o.data.uv_layers.active.data) for o in obs)
    lo,hi=bounds(obs)
    if props is None:props=[dict(name=name,triangles_per_instance=tri,instance_count=1,total_triangles=tri)]
    assert sum(p['total_triangles'] for p in props)==tri,(aid,tri,props)
    assert tri<=(5000 if kind=='diorama' else 1000),(aid,tri)
    report=dict(schema_version=3,asset_id=aid,version=v,kind=kind,target_web_environment='Unity WebGL workplaces-v007; execution pending',props=props,scene_triangles=tri,material_count=len(materials),texture_count=len(textures),palette_resolution=[2508,2508],glb_bytes=glb.stat().st_size,dimensions_m=[hi[k]-lo[k] for k in range(3)],checks=dict(scene_budget=ck(tri<=(5000 if kind=='diorama' else 1000),'Final GLB reopened in actual Blender; repeated instances included'),palette_uv=ck(uvok,'Every loop matches original shared palette cell center'),shared_material=ck(len(materials)==len(textures)==1,'Final GLB material/texture inspection'),visual_layout=dict(status='unverified',evidence=None,reason='Actual multi-view review pending'),web_display=dict(status='unverified',evidence=None,reason='Actual new Unity WebGL execution pending')),remaining_issues=['New version needs actual multi-view and WebGL review; no historical pass inherited.'])
    s.write(out/'inspection.json',report)
    entry=dict(asset_id=aid,version=v,name=name,source_path=rel(src/'source.blend'),blender_path=rel(out/'model.blend'),runtime_path=rel(glb),preview_path=rel(src/'previews/front.png'),unity_path=None,kind=kind,palette_version='v001',accent_reason=None,unity_palette_path=None,inspection_path=rel(out/'inspection.json'),processing_paths=[SCRIPT,SHARED],status='in_progress',generation_method=method,generation_reason='Meshy organic floral silhouette, locally reduced and mapped to shared palette.' if method=='meshy' else 'Reuse precise existing shapes; symmetric frames, wood detailing, seating direction and geometric ornament built locally.',production_record_path=rel(src/'README.md'),meshy_credits_used=credits)
    catalog=s.read('assets');assert not any(a['asset_id']==aid and a['version']==v for a in catalog['assets']);catalog['assets'].append(entry);s.write(CAT/'assets.json',catalog)
    (src/'README.md').write_text(f'# {aid} {v} — {name}\n\n{now()}\n\n제작 방식: {method}. 이번 Meshy 실제 소비 {credits}크레딧; 작업 '+('01a18fd2-fc65-7137-9987-8b397806fae9 (text-to-3d preview)' if credits else '이 에셋의 유료 호출 없음')+f'.\n\n이전 버전과 원본 보존. 최종 GLB 실제 재열기: {tri}삼각형, 공용 palette v001 PNG 한 장·재질 한 개. 새 이미지 텍스처 없음. 제작 스크립트: {SCRIPT}.\n\n가상 설계 치수이며 실측 치수가 아니다. 입력·캐시·출력 토큰과 모델별 시간·금액 배분 미측정. 실제 Unity/WebGL 및 다방향 시각 검수는 inspection.json과 후속 증거를 조회한다.\n',encoding='utf-8')
    render(src/'previews/front.png',size=1000 if kind=='diorama' else 640)
    NEW.append(entry);print('PRODUCED',aid,v,tri,flush=True)
    return entry,report
def flower():
    s.reset();bpy.ops.import_scene.gltf(filepath=str(ROOT/'meshy/models/original/AST-3001/v001/source.glb'))
    obs=meshes();lo,hi=bounds(obs);source_tri=triangles(obs);print('FLOWER_SOURCE',source_tri,lo,hi,flush=True)
    bpy.ops.object.select_all(action='DESELECT')
    for o in obs:o.select_set(True)
    bpy.context.view_layer.objects.active=obs[0];bpy.ops.object.join();o=bpy.context.object;o.name='Lily arrangement - Meshy silhouette'
    bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
    lo,hi=bounds([o]);scale=.76/(hi[2]-lo[2]);center=Vector(((lo[0]+hi[0])/2,(lo[1]+hi[1])/2,lo[2]))
    for vert in o.data.vertices:vert.co=(vert.co-center)*scale
    # Dense Meshy preview has many tiny disconnected islands. Voxel-union first
    # avoids per-island decimation minima; local work incurs no second API charge.
    mod=o.modifiers.new('Unify floral silhouette','REMESH');mod.mode='VOXEL';mod.voxel_size=.014;mod.use_smooth_shade=True
    bpy.ops.object.modifier_apply(modifier=mod.name)
    mod=o.modifiers.new('Web silhouette budget','DECIMATE');mod.ratio=650/max(1,triangles([o]));bpy.ops.object.modifier_apply(modifier=mod.name)
    mod=o.modifiers.new('Stable final triangles','TRIANGULATE');bpy.ops.object.modifier_apply(modifier=mod.name)
    s.paint(o,'green');o.data.update()
    for p in o.data.polygons:
        c=p.center;z=c.z;r=math.hypot(c.x,c.y)
        color='cream' if z<.24 else 'white' if z>.47 and p.normal.z>-.25 else 'green'
        if z>.56 and r<.045:color='yellow'
        uvcolor(o,p,color)
    save('AST-3001','v002','백합 꽃꽂이 화분','prop','meshy',20)
    s.write(EVIDENCE/'meshy-usage.json',dict(schema_version=3,task_id='01a18fd2-fc65-7137-9987-8b397806fae9',resource='text-to-3d',mode='preview',calls=1,consumed_credits=20,source_triangles=source_tri,source_preserved=True,paid_refine_calls=0,paid_remesh_calls=0,chat_tokens=None,token_measurement_note='Tool does not expose attributable input/cache/output token usage.'))
def pew():
    s.reset();import_asset('AST-1247','v001')
    for o in meshes():
        if o.name.startswith('Book rest'):o.location.y=.32
    box('Seat cushion',(0,-.015,.495),(1.79,.38,.035),'teal',.012)
    for x in [-.55,.55]:
        box('Hymnal cover',(x,.32,.740),(.18,.12,.055),'purple')
        box('Hymnal pages',(x,.32,.740),(.161,.105,.040),'cream')
    save('AST-1247','v002','예배용 긴 의자','prop','blender_direct')
def cross():
    s.reset()
    box('Stepped plinth',(0,0,.06),(.42,.36,.12),'wood',.025)
    box('Cross upright',(0,0,1.08),(.155,.115,2.04),'wood',.012)
    box('Cross arm',(0,0,1.54),(1.02,.115,.155),'wood',.012)
    box('Inset upright',(0,-.059,1.08),(.035,.008,1.93),'yellow')
    box('Inset arm',(0,-.059,1.54),(.92,.008,.035),'yellow')
    save('AST-1246','v002','단순한 십자가','prop','blender_direct')
def stage():
    s.reset();box('Sanctuary platform',(0,0,.08),(3.5,1.7,.16),'wood',.03)
    box('Entry step',(0,-.95,.04),(2.7,.25,.08),'wood',.02)
    box('Stage carpet',(0,0,.164),(1.28,1.58,.008),'purple')
    for x in [-.63,.63]:box('Carpet border',(x,0,.17),(.025,1.56,.006),'yellow')
    for x in [-1.5,-1.0,-.5,.5,1,1.5]:box('Wood seam',(x,0,.162),(.008,1.63,.003),'soil')
    save('AST-3002','v001','예배 단상과 계단','prop','blender_direct')
def runner():
    s.reset();box('Aisle runner',(0,0,.008),(.66,2.58,.016),'purple')
    for x in [-.30,.30]:box('Woven gold border',(x,0,.017),(.025,2.54,.003),'yellow')
    for y in [-1.05,-.7,-.35,0,.35,.7,1.05]:
        o=box('Geometric lozenge',(0,y,.018),(.075,.075,.003),'yellow');o.rotation_euler.z=math.pi/4
    save('AST-3003','v001','금색 테두리 통로 러너','prop','blender_direct')
def window():
    s.reset()
    box('Panel base',(0,0,.035),(.80,.23,.07),'wood',.02)
    for x in [-.34,.34]:box('Arched window side',(x,0,.83),(.055,.08,1.6),'wood')
    for i in range(12):
        a=math.pi*i/12;b=math.pi*(i+1)/12
        s.rod('Arched frame',(.34*math.cos(a),0,1.6+.34*math.sin(a)),(.34*math.cos(b),0,1.6+.34*math.sin(b)),.03,'wood',6)
    for x in [-.215,0,.215]:
        for iz in range(4):box('Colored glass tile',(x,.012,.26+iz*.34),(.205,.018,.325),['teal','cream','yellow','pink'][(iz+int((x+.22)*10))%4])
    box('Window mullion',(0,-.025,.87),(.025,.035,1.52),'wood')
    for z in [.1,.44,.78,1.12,1.47]:box('Window horizontal lead',(0,-.025,z),(.66,.035,.018),'wood')
    for x in [-.22,0,.22]:box('Arch infill',(x,.012,1.57),(.19,.018,.16 if x else .38),'cream')
    save('AST-3004','v001','기하무늬 아치 창 패널','prop','blender_direct')
def stool():
    s.reset();box('Cushioned seat',(0,0,.48),(.48,.34,.085),'dark',.025)
    for x in [-.18,.18]:
        for y in [-.10,.10]:box('Stool leg',(x,y,.22),(.045,.045,.44),'wood')
    save('AST-3005','v001','건반 연주용 의자','prop','blender_direct')
def pulpit():
    s.reset();import_asset('AST-1244','v002')
    for o in meshes():
        if o.name.startswith('Reading top'):o.rotation_euler.x=math.radians(-12)
    for x in [-.195,.195]:box('Raised panel molding',(x,-.182,.64),(.035,.02,.70),'wood',.006)
    for z in [.30,.98]:box('Panel trim',(0,-.182,z),(.43,.02,.035),'wood',.006)
    for x in [-.28,.28]:box('Lower plinth',(x,0,.10),(.035,.40,.065),'wood')
    s.rod('Gooseneck microphone',(0.25,.04,1.22),(.25,.10,1.50),.012,'dark',6)
    s.rod('Microphone head',(.25,.10,1.50),(.16,.07,1.54),.022,'dark',8)
    save('AST-1244','v003','설교 강대상','prop','blender_direct')
def room(number):
    aid=f'AST-{2000+number}';v='v003';old=ROOT/f'meshy/models/blender/{aid}/v002/placements.json'
    placement=json.loads(old.read_text('utf-8'));items=copy.deepcopy(placement['instances'])
    for i in items:
        if i['asset_id']=='AST-1247':i['version']='v002';i['rotation_euler_blender_deg']=[0,0,180];i['rotation_z_rad']=math.pi
        if number==64 and i['asset_id']=='AST-1246':i['version']='v002'
        if number==64 and i['asset_id']=='AST-1244':i['version']='v003'
        if number==64 and i['asset_id'] in ['AST-1244','AST-1245','AST-1246']:i['position_blender_m'][2]+=.16
        if number==71 and i['asset_id'] in ['AST-1257','AST-1259','AST-1260','AST-1261','AST-1262','AST-1124']:i['position_blender_m'][2]+=.16
        if number==64 and i['asset_id']=='AST-1245':i['rotation_euler_blender_deg']=[12,0,180];i['rotation_z_rad']=math.pi
    def add(aid,p,rot=0,scale=(1,1,1)):
        items.append(dict(asset_id=aid,version='v001',candidate_id=None,instance_id=f'{aid}-{len(items):03}',position_blender_m=list(p),rotation_euler_blender_deg=[0,0,rot],rotation_z_rad=math.radians(rot),scale=list(scale)))
    add('AST-3002',(0,1.25,F));add('AST-3003',(0,-1.0,F))
    for x in [-1.45,1.45]:add('AST-3004',(x,2.2,F))
    for x in [-1.28,1.28]:add('AST-3001',(x,1.72,F+.16),scale=(.75,.75,.75))
    for i in items:
        if i['asset_id']=='AST-3001':i['version']='v002'
    if number==64:add('AST-3005',(-1.8,.65,F))
    s.reset();props={};facing=[]
    for i in items:
        objs,a=import_asset(i['asset_id'],i['version']);root=bpy.data.objects.new(i['instance_id'],None);bpy.context.collection.objects.link(root)
        for o in objs:
            if o.parent is None:o.parent=root
        root.location=i['position_blender_m'];root.rotation_euler=[math.radians(v) for v in i['rotation_euler_blender_deg']];root.scale=i['scale'];bpy.context.view_layer.update()
        obs=[o for o in objs if o.type=='MESH'];i['component_mesh_count']=len(obs)
        key=(a['asset_id'],a['version']);tri=triangles(obs)
        if key not in props:props[key]=dict(name=a['name'],asset_ref=dict(asset_id=key[0],version=key[1]),triangles_per_instance=tri,instance_count=0,total_triangles=0)
        props[key]['instance_count']+=1;props[key]['total_triangles']+=tri
        if a['asset_id']=='AST-1247':
            front=(root.matrix_world.to_3x3()@Vector((0,-1,0))).normalized();target=(Vector((0,1.1,F))-root.location).normalized();dot=front.dot(target)
            seat=next(o for o in obs if o.name.startswith('Seat') and not o.name.startswith('Seat cushion'))
            back=next(o for o in obs if o.name.startswith('Back'));delta=(root.location+front*.5)-root.location
            facing.append(dict(instance_id=root.name,front_vector=list(front),target_dot=dot,pass_facing=dot>.5,seat_center=list(seat.matrix_world.translation),back_center=list(back.matrix_world.translation)))
    placement['instances']=items;placement['change_reason']='Fix eight reversed pews, move hymn rest behind seat; enrich sanctuary while preserving aisle and original symbols.'
    assets=s.read('assets')['assets'];oldasset=next(a for a in assets if a['asset_id']==aid and a['version']=='v002')
    entry,report=save(aid,v,oldasset['name'],'diorama','blender_direct',props=list(props.values()),placements=placement)
    assembly=s.read('scene-assemblies');previous=max((a for a in assembly['assemblies'] if a['assembly_id']==f'pan-{number:03}-workplace'),key=lambda a:a['revision']);row=copy.deepcopy(previous)
    row.update(revision=previous['revision']+1,recorded_at=now(),assembly_asset_ref=dict(asset_id=aid,version=v),placements_path=f'meshy/models/blender/{aid}/{v}/placements.json',inspection_path=entry['inspection_path'],component_counts=report['props'],change_reason=placement['change_reason'])
    assembly['assemblies'].append(row);s.write(CAT/'scene-assemblies.json',assembly)
    s.write(EVIDENCE/f'PAN-{number:03}-facing.json',dict(schema_version=3,checked_at=now(),source_final_glb=entry['runtime_path'],pews=facing,all_facing_sanctuary=all(f['pass_facing'] for f in facing)))
    # Final GLB reopened for independent reverse and overhead views.
    render(ROOT/f'meshy/models/original/{aid}/{v}/previews/back.png',direction=(-6,9,7))
    render(ROOT/f'meshy/models/original/{aid}/{v}/previews/top.png',direction=(0,-.01,12))
if __name__=='__main__':
    flower();pew();cross();stage();runner();window();stool();pulpit();room(64);room(71)
    s.write(EVIDENCE/'production.json',dict(schema_version=3,checked_at=now(),assets=[dict(asset_id=a['asset_id'],version=a['version']) for a in NEW],meshy_calls=1,meshy_credits=20))

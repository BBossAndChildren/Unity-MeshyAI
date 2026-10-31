"""PAN-001 v001 only. Reuses chair/base GLBs and palette; deterministic props and assembly."""
import bpy, math, json, hashlib
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parents[6]
MAP=json.loads((R/'meshy/models/textures/palettes/v001/mapping.json').read_text('utf-8'))
REF={'catalog':'panoramas','image_id':'PAN-001','version':'v001'}
SCRIPT='meshy/models/blender/AST-020/v001/processing/build_office.py'
COL={'cream':(13,0),'wood':(3,3),'orange':(3,7),'green':(6,10),'dark':(15,12),'black':(15,14),'white':(15,0),'yellow':(4,7),'soil':(12,13)}
def cell(role):
 row,col=COL[role];return next(c for c in MAP['cells'] if c['texture_id']=='color1' and c['row']==row and c['column']==col)
def reset():
 bpy.ops.wm.read_factory_settings(use_empty=True)
def mat():
 m=bpy.data.materials.new('SharedPalette_v001');m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(1,1,1,1);p.inputs['Roughness'].default_value=.8
 t=m.node_tree.nodes.new('ShaderNodeTexImage');t.image=bpy.data.images.load(str(R/'meshy/models/textures/palettes/v001/palette.png'));t.image.pack();t.interpolation='Closest';m.node_tree.links.new(t.outputs['Color'],p.inputs['Base Color']);return m
def paint(o,role):
 o.data.materials.clear();o.data.materials.append(M);uv=o.data.uv_layers.active or o.data.uv_layers.new(name='PaletteUV')
 for l in uv.data:l.uv=cell(role)['uv_center']
 return o
def box(n,p,d,c='cream'):
 bpy.ops.mesh.primitive_cube_add(size=1,location=p);o=bpy.context.object;o.name=n;o.dimensions=d;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True);return paint(o,c)
def cyl(n,p,r,h,c='dark',v=8,r2=None):
 bpy.ops.mesh.primitive_cone_add(vertices=v,radius1=r,radius2=r if r2 is None else r2,depth=h,location=p);o=bpy.context.object;o.name=n;return paint(o,c)
def rod(n,a,b,r=.025,c='dark',v=6):
 a,b=Vector(a),Vector(b);o=cyl(n,(a+b)/2,r,(b-a).length,c,v);o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler();return o
def join():
 obs=[o for o in bpy.context.scene.objects if o.type=='MESH'];bpy.ops.object.select_all(action='DESELECT')
 for o in obs:o.select_set(True)
 bpy.context.view_layer.objects.active=obs[0];bpy.ops.object.join();o=bpy.context.object
 # Keep palette UVs; unify material slots.
 o.data.materials.clear();o.data.materials.append(M)
 for p in o.data.polygons:p.material_index=0
 mod=o.modifiers.new('Triangulate','TRIANGULATE');bpy.ops.object.modifier_apply(modifier=mod.name);return o
def render(path,span=2,target=(0,0,.5)):
 s=bpy.context.scene;s.render.engine='CYCLES';s.cycles.samples=8;s.render.resolution_x=640;s.render.resolution_y=480;s.render.resolution_percentage=100
 s.world=bpy.data.worlds.new('World');s.world.use_nodes=True;s.world.node_tree.nodes['Background'].inputs[0].default_value=(.8,.77,.70,1);s.world.node_tree.nodes['Background'].inputs[1].default_value=.7
 bpy.ops.object.light_add(type='AREA',location=(-3,-4,7));bpy.context.object.data.energy=650;bpy.context.object.data.size=5
 bpy.ops.object.camera_add(location=Vector(target)+Vector((span,-span,span*.85)));cam=bpy.context.object;cam.rotation_euler=(Vector(target)-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=span*1.65;s.camera=cam;s.render.filepath=str(path);bpy.ops.render.render(write_still=True)
def check(a,version,kind,props):
 out=R/f'meshy/models/blender/{a}/{version}';glb=out/'exports/model.glb';reset();bpy.ops.import_scene.gltf(filepath=str(glb))
 obs=[o for o in bpy.context.scene.objects if o.type=='MESH'];tri=sum(len(p.vertices)-2 for o in obs for p in o.data.polygons);mats={m for o in obs for m in o.data.materials};imgs={n.image for m in mats for n in m.node_tree.nodes if n.type=='TEX_IMAGE'}
 uvok=all(any(abs(l.uv.x-c['uv_center'][0])<1e-5 and abs(l.uv.y-c['uv_center'][1])<1e-5 for c in MAP['cells']) for o in obs for l in o.data.uv_layers.active.data)
 def ck(ok,msg):return dict(status='pass' if ok else 'fail',evidence=msg,reason=None)
 report=dict(schema_version=3,asset_id=a,version=version,kind=kind,target_web_environment='Independent Three.js GLB viewer; Unity not tested',props=props or [dict(name=a,triangles_per_instance=tri,instance_count=1,total_triangles=tri)],scene_triangles=tri,material_count=len(mats),texture_count=len(imgs),palette_resolution=[2508,2508],glb_bytes=glb.stat().st_size,checks={'triangle_budget':ck(tri<= (5000 if kind=='diorama' else 1000),'Final GLB reimport, instances included'),'palette_uv':ck(uvok,'GLB reimport UV centers'),'shared_material':ck(len(mats)==len(imgs)==1,'Reimport material/image nodes'),'web_display':dict(status='unverified',evidence=None,reason='Pending scene browser check')},remaining_issues=['Unity project absent; Unity/WebGL and physical mobile device unverified','Full preserved palette dominates GLB bytes'],palette_mapping_path='meshy/models/textures/palettes/v001/mapping.json')
 (out/'inspection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf-8');return report
def save(a,name,kind='prop',props=None):
 out=R/f'meshy/models/blender/{a}/v001';src=R/f'meshy/models/original/{a}/v001'
 assert not (out/'model.blend').exists(),'Preserve existing version'
 (out/'exports').mkdir(parents=True,exist_ok=True);(src/'previews').mkdir(parents=True,exist_ok=True)
 bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'));bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'));bpy.ops.export_scene.gltf(filepath=str(out/'exports/model.glb'),export_format='GLB',use_selection=True)
 report=check(a,'v001',kind,props)
 render(src/'previews/front.png',6 if kind=='diorama' else 1.7,(0,0,.7 if kind=='diorama' else .5))
 (src/'README.md').write_text(f'# {name}\nBlender direct, 2026-10-31. PAN-001 v001 directly inspected. Repeated symmetric structures use primitives; no Meshy call, credits 0, task ID not applicable.\nScript: {SCRIPT}\nPalette v001 unchanged; region assignments in script. Raw editable source preserved. Rights follow user-provided references; not independently verified.\n', 'utf-8')
 return dict(asset_id=a,version='v001',name=name,source_path=str((src/'source.blend').relative_to(R)).replace('\\','/'),blender_path=str((out/'model.blend').relative_to(R)).replace('\\','/'),runtime_path=str((out/'exports/model.glb').relative_to(R)).replace('\\','/'),preview_path=str((src/'previews/front.png').relative_to(R)).replace('\\','/'),unity_path=None,kind=kind,palette_version='v001',accent_reason=None,unity_palette_path=None,inspection_path=str((out/'inspection.json').relative_to(R)).replace('\\','/'),processing_paths=[SCRIPT],status='in_progress',generation_method='blender_direct',generation_reason='Repeatable symmetric office objects and exact layout; reuse existing palette and models.',production_record_path=str((src/'README.md').relative_to(R)).replace('\\','/'),meshy_credits_used=0,source_images=[REF]),report
def desk():
 box('Top',(0,0,.76),(1.65,.75,.07),'wood')
 for x in [-.75,.75]:
  for y in [-.29,.29]:box('Leg',(x,y,.37),(.045,.045,.74))
def monitor():
 box('Frame',(0,0,.39),(.54,.045,.34),'dark');box('Screen',(0,-.025,.39),(.48,.008,.28),'black');box('Stand',(0,0,.16),(.045,.04,.18),'dark');box('Foot',(0,-.015,.055),(.25,.15,.025),'dark')
def drawers():
 box('Cabinet',(0,0,.32),(.43,.53,.64))
 for z in [.12,.33,.54]:
  box('Drawer',(0,-.274,z),(.39,.025,.18));box('Handle',(0,-.294,z),(.14,.025,.035),'orange')
def plant():
 cyl('Pot',(0,0,.14),.14,.28,'cream',8,r2=.18);cyl('Soil',(0,0,.285),.155,.012,'soil')
 for i in range(7):
  a=i*2.399;rod('Stem',(0,0,.28),(.12*math.cos(a),.12*math.sin(a),.5),.009,'green',5)
  bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=1,location=(.12*math.cos(a),.12*math.sin(a),.53+(i%3)*.07));o=bpy.context.object;o.name='Leaf';o.scale=(.09,.07,.22);o.rotation_euler=(.4*math.sin(a),.4*math.cos(a),a);paint(o,'green')
def printer():
 box('Body',(0,0,.48),(.7,.65,.85));box('Top',(0,0,.94),(.68,.62,.09),'dark');box('Scanner',(0,.10,1.02),(.52,.30,.08),'dark');box('Output',(0,-.334,.73),(.48,.025,.13),'black')
 for z in [.2,.4,.6]:box('Tray',(0,-.34,z),(.62,.03,.17));box('Grip',(0,-.36,z),(.18,.02,.03),'dark')
 box('Control',(.30,-.40,.89),(.26,.18,.05),'dark');box('Display',(.30,-.40,.921),(.18,.12,.012),'yellow')
def cabinet():
 box('Cabinet',(0,0,.50),(1.2,.48,1),'green')
 for z in [.26,.73]:box('Drawer',(0,-.25,z),(1.12,.03,.43),'green');box('Handle',(0,-.28,z),(.22,.035,.045))
def lamp():
 cyl('Base',(0,0,.02),.11,.04,'yellow');rod('Arm',(0,0,.04),(-.04,0,.42),.018,'yellow');rod('Arm',(-.04,0,.42),(-.27,0,.59),.018,'yellow');cyl('Shade',(-.29,0,.55),.12,.14,'yellow',8,r2=.045)
def rack():
 cyl('Foot',(0,0,.035),.24,.07,'wood');rod('Pole',(0,0,.07),(0,0,1.65),.035,'wood')
 for z in [1.1,1.4]:
  for i in range(3):
   a=i*math.tau/3;rod('Hook',(0,0,z),(.23*math.cos(a),.23*math.sin(a),z+.14),.025,'wood')
def bag():
 box('Bag',(0,0,.18),(.32,.10,.30),'soil');box('Flap',(0,-.06,.26),(.32,.025,.13),'wood')
 for x in [-.10,.10]:rod('Handle',(x,0,.33),(x,0,.48),.013,'soil')
 rod('Handle',(-.10,0,.48),(.10,0,.48),.013,'soil')
def books():
 for i,c in enumerate(['green','orange','cream']):box('Pages',(0,0,.03+i*.06),(.24,.18,.04),'white');box('Cover',(0,0,.055+i*.06),(.26,.20,.012),c)
def pens():
 cyl('Cup',(0,0,.055),.045,.11,'yellow',8)
 for i in range(3):rod('Pen',((i-1)*.025,0,.06),((i-1)*.03,.01,.20),.007,'dark',5)
BUILD=[('AST-004','업무 책상',desk),('AST-005','모니터',monitor),('AST-006','키보드',lambda:box('Keyboard',(0,0,.015),(.42,.14,.03),'dark')),('AST-007','마우스',lambda:box('Mouse',(0,0,.02),(.07,.11,.04),'dark')),('AST-008','책상 아래 서랍장',drawers),('AST-009','복합기',printer),('AST-010','화분',plant),('AST-011','책 묶음',books),('AST-012','펜꽂이',pens),('AST-013','낮은 책상 스크린',lambda:box('Screen',(0,0,.23),(1.72,.055,.46),'green')),('AST-014','관절 스탠드',lamp),('AST-015','뒤쪽 수납장',cabinet),('AST-016','옷걸이',rack),('AST-017','업무용 가방',bag)]
catalog=json.loads((R/'docs/machine/catalog/assets.json').read_text('utf-8'));new=[];reports={}
for a,n,f in BUILD:
 reset();M=mat();f();join();entry,rep=save(a,n);new.append(entry);reports[(a,'v001')]=rep
reset();M=mat();placements=[]
lookup={(a['asset_id'],a['version']):a for a in catalog['assets']+new}
def place(a,p,scale=(1,1,1),version='v001',rot=0):
 before=set(bpy.context.scene.objects);bpy.ops.import_scene.gltf(filepath=str(R/lookup[(a,version)]['runtime_path']));obs=[o for o in bpy.context.scene.objects if o not in before and o.type=='MESH'];idx=sum(x['asset_id']==a for x in placements)
 for o in obs:
  # Apply placement around asset origin, preserving source local transforms.
  bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
  for v in o.data.vertices:
   x,y,z=v.co;x*=scale[0];y*=scale[1];z*=scale[2];v.co=(x*math.cos(rot)-y*math.sin(rot)+p[0],x*math.sin(rot)+y*math.cos(rot)+p[1],z+p[2])
  o.name=f'{a}_{idx}';o.data.materials.clear();o.data.materials.append(M)
 placements.append(dict(asset_id=a,version=version,instance_id=f'{a}-{idx}',position_blender_m=p,scale=scale,rotation_z_rad=rot))
place('AST-001',(0,0,0),(3,2.6,1.8),'v002');place('AST-002',(0,-.30,.29),(2.4,1.8,1))
for x in [-.9,.9]:
 place('AST-004',(x,.05,.30));place('AST-003',(x,-.85,.30));place('AST-005',(x,.19,1.10));place('AST-006',(x,-.14,1.10));place('AST-007',(x+.34,-.18,1.10));place('AST-008',(x-.48,.03,.30));place('AST-011',(x-.55,.23,1.10));place('AST-012',(x+.55,.25,1.10));place('AST-014',(x+.56,.48,1.10));place('AST-013',(x,.47,1.08))
place('AST-009',(-2.15,.60,.30));place('AST-015',(.65,1.75,.30));place('AST-016',(2.05,1.65,.30));place('AST-017',(2.05,1.43,1.16));place('AST-010',(0,.12,1.10));place('AST-010',(.98,1.75,1.30));place('AST-010',(2,-1.2,.30),(1.65,1.65,1.65));place('AST-011',(.30,1.75,1.30))
out=R/'meshy/models/blender/AST-020/v001';(out/'processing').mkdir(parents=True,exist_ok=True)
props=[]
for key in sorted({(p['asset_id'],p['version']) for p in placements}):
 rep=reports.get(key) or json.loads((R/lookup[key]['inspection_path']).read_text('utf-8'));q=sum((p['asset_id'],p['version'])==key for p in placements);t=rep['scene_triangles'];props.append(dict(name=lookup[key]['name'],asset_ref=dict(asset_id=key[0],version=key[1]),triangles_per_instance=t,instance_count=q,total_triangles=t*q))
(out/'placements.json').write_text(json.dumps(dict(schema_version=3,panorama_ref=REF,coordinate_system='Blender Z-up meters',instances=placements),ensure_ascii=False,indent=2),'utf-8')
join();entry,rep=save('AST-020','PAN-001 일반 사무실 조립',kind='diorama',props=props);assert rep['scene_triangles']==sum(p['total_triangles'] for p in props);assert rep['scene_triangles']<=5000;new.append(entry)
# Reload at registration time to preserve other sessions' additions.
path=R/'docs/machine/catalog/assets.json';catalog=json.loads(path.read_text('utf-8'));assert not {(a['asset_id'],a['version']) for a in new}&{(a['asset_id'],a['version']) for a in catalog['assets']};catalog['assets']+=new;path.write_text(json.dumps(catalog,ensure_ascii=False,indent=2),'utf-8')
print('OFFICE_COMPLETE',rep['scene_triangles'],rep['glb_bytes'],len(placements),flush=True)

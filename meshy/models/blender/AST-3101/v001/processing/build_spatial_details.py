"""Data-driven production for 69 scene-specific diorama enrichments.
Preserve originals, fixed component versions, palette cells and game bindings.
"""
import bpy,json,math,copy,datetime,sys,importlib.util,os,time
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parents[6];SCRIPT=Path(__file__).relative_to(R).as_posix();HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('s',R/'meshy/models/blender/AST-1010/v001/processing/build_shared.py');s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
spec=importlib.util.spec_from_file_location('plan',HERE/'spatial_plan.py');plan=importlib.util.module_from_spec(spec);spec.loader.exec_module(plan)
CAT=R/'docs/machine/catalog';EV=R/'docs/machine/evidence/spatial-diversity-v001';EV.mkdir(parents=True,exist_ok=True)
CATALOG=s.read('assets');LOOKUP={(a['asset_id'],a['version']):a for a in CATALOG['assets']};BASE=copy.deepcopy(CATALOG);CREATED=[];VARIANTS=[];BOUNDS={}
COLORS={k:('color1',*v)for k,v in s.COLORS.items()};COLORS.update(walnut=('color1',12,7),navy=('color1',9,12),sage=('color1',6,10),rose=('color1',1,10),ochre=('color1',4,11),burgundy=('color1',0,12),steel=('color1',15,7),gold=('color1',4,12),signal_red=('color2',1,8),signal_blue=('color2',10,8),safety_yellow=('color2',5,6),signal_green=('color2',7,7))
CELLS={(c['texture_id'],c['row'],c['column']):c for c in s.MAPPING['cells']};UVSET={(round(c['uv_center'][0],5),round(c['uv_center'][1],5))for c in s.MAPPING['cells']}
ACCENT_UVSET={(round(c['uv_center'][0],5),round(c['uv_center'][1],5))for c in s.MAPPING['cells']if c['texture_id']=='color2'}
def now():return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat()
def write(p,x):
 p=Path(p);p.parent.mkdir(parents=True,exist_ok=True)
 if p==CAT/'assets.json'and p.exists():
  # Preserve unrelated concurrent catalog updates; only merge this task's rows.
  disk=json.loads(p.read_text('utf-8'));ours={(a['asset_id'],a['version']):a for a in x['assets']if a.get('produced_by_task')=='spatial-diversity-v001'};merged=[]
  for a in disk['assets']:
   key=(a['asset_id'],a['version']);merged.append(ours.pop(key,a));LOOKUP[key]=merged[-1]
  merged+=list(ours.values());x['assets']=merged
 temp=p.with_name(p.name+f'.spatial-{os.getpid()}.tmp')
 for attempt in range(4):
  try:temp.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n',encoding='utf-8');os.replace(temp,p);return
  except OSError:
   if attempt==3:raise
   time.sleep(.25*(attempt+1))
def meshes():return [o for o in bpy.context.scene.objects if o.type=='MESH']
def tris(obs):return sum(len(p.vertices)-2 for o in obs for p in o.data.polygons)
def bounds(obs):
 bpy.context.view_layer.update();pts=[o.matrix_world@Vector(v)for o in obs for v in o.bound_box]
 return [min(p[k]for p in pts)for k in range(3)],[max(p[k]for p in pts)for k in range(3)]
def paint(o,color):
 key=COLORS[color]if isinstance(color,str)else color;uv=CELLS[key]['uv_center'];o.data.materials.clear();o.data.materials.append(s.MATERIAL);layer=o.data.uv_layers.active or o.data.uv_layers.new(name='PaletteUV')
 for loop in layer.data:loop.uv=uv
 for p in o.data.polygons:p.material_index=0
 o['palette_source'],o['palette_row'],o['palette_column']=key;o['background_detail']=True
 return o
s.paint=paint
def box(n,p,d,c='cream',b=0):return s.box(n,p,d,c,b)
def rod(n,a,b,r=.02,c='dark',v=6):return s.rod(n,a,b,r,c,v)
def cyl(n,p,r,h,c='cream',v=10,top=None):return s.cyl(n,p,r,h,c,v,top)
def import_asset(aid,v):
 a=LOOKUP[(aid,v)];before=set(bpy.context.scene.objects);bpy.ops.import_scene.gltf(filepath=str(R/a['runtime_path']));obs=[o for o in bpy.context.scene.objects if o not in before]
 for o in obs:
  if o.type=='MESH':o.data.materials.clear();o.data.materials.append(s.MATERIAL)
 return obs
def version(aid):return 'v'+str(max([int(v[1:])for k,v in LOOKUP if k==aid]+[0])+1).zfill(3)
def save(aid,v,name,kind='prop',method='blender_direct',props=None,placements=None,source_ref=None,credit=0):
 out=R/f'meshy/models/blender/{aid}/{v}';src=R/f'meshy/models/original/{aid}/{v}';assert not(out/'model.blend').exists(),out
 (out/'exports').mkdir(parents=True,exist_ok=True);src.mkdir(parents=True,exist_ok=True);bpy.ops.object.select_all(action='DESELECT')
 for o in bpy.context.scene.objects:
  if o.type in ['MESH','EMPTY']:o.select_set(True)
 bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'));bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
 glb=out/'exports/model.glb';bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
 bpy.ops.export_scene.fbx(filepath=str(out/'exports'/('room.fbx'if kind=='diorama'else'model.fbx')),use_selection=True,add_leaf_bones=False,bake_anim=False,axis_forward='-Z',axis_up='Y',path_mode='STRIP',use_custom_props=True)
 if placements:write(out/'placements.json',placements)
 s.reset();bpy.ops.import_scene.gltf(filepath=str(glb));obs=meshes();tri=tris(obs);lo,hi=bounds(obs);BOUNDS[(aid,v)]=(lo,hi)
 mats={m for o in obs for m in o.data.materials};imgs={n.image for m in mats for n in m.node_tree.nodes if n.type=='TEX_IMAGE'and n.image};uvok=all(o.data.uv_layers.active and all((round(l.uv.x,5),round(l.uv.y,5))in UVSET for l in o.data.uv_layers.active.data)for o in obs)
 assert tri<=(5000 if kind=='diorama'else 1000),(aid,v,tri);assert len(mats)==len(imgs)==1 and uvok
 if props is None:props=[dict(name=name,triangles_per_instance=tri,instance_count=1,total_triangles=tri)]
 assert sum(p['total_triangles']for p in props)==tri
 ck=lambda b,n:dict(status='pass'if b else'fail',evidence=n,reason=None)
 report=dict(schema_version=3,asset_id=aid,version=v,kind=kind,target_web_environment='New Unity WebGL spatial revision; runtime pending',props=props,scene_triangles=tri,material_count=1,texture_count=1,palette_resolution=[2508,2508],glb_bytes=glb.stat().st_size,dimensions_m=[hi[k]-lo[k]for k in range(3)],bounds_blender_m={'min':lo,'max':hi},checks={'scene_budget':ck(True,'Actual final GLB Blender reimport, repeated instances once'),'component_budget':ck(all(p['triangles_per_instance']<=1000 for p in props),'Component fixed final GLB counts'),'palette_uv':ck(uvok,'Exact original palette cell centers'),'shared_material':ck(True,'One model material and one shared palette PNG'),'visual_layout':{'status':'unverified','evidence':None,'reason':'Actual final Unity WebGL visual review pending'},'web_display':{'status':'unverified','evidence':None,'reason':'No runtime pass inherited'}},remaining_issues=['Actual new Unity/WebGL, screenshot review and gameplay binding smoke pending.'])
 write(out/'inspection.json',report)
 accent=any((round(l.uv.x,5),round(l.uv.y,5))in ACCENT_UVSET for o in obs for l in o.data.uv_layers.active.data)
 entry=dict(asset_id=aid,version=v,name=name,source_path=src.relative_to(R).as_posix()+'/source.blend',blender_path=out.relative_to(R).as_posix()+'/model.blend',runtime_path=glb.relative_to(R).as_posix(),preview_path=None,unity_path=None,kind=kind,palette_version='v001',accent_reason='Small safety/status/identity marks use original color2 palette cells.'if accent else None,unity_palette_path=None,inspection_path=out.relative_to(R).as_posix()+'/inspection.json',processing_paths=[SCRIPT,'meshy/models/blender/AST-1010/v001/processing/build_shared.py'],status='in_progress',generation_method=method,generation_reason='Curated spatial identity; reuse fixed original geometry, precise repeated details in Blender; organic source only when actually reused.',production_record_path=src.relative_to(R).as_posix()+'/README.md',meshy_credits_used=credit)
 if source_ref:entry['source_asset_ref']=source_ref
 entry['produced_by_task']='spatial-diversity-v001'
 assert(aid,v)not in LOOKUP;LOOKUP[(aid,v)]=entry;CATALOG['assets'].append(entry);CREATED.append(entry);write(CAT/'assets.json',CATALOG)
 (src/'README.md').write_text(f'# {aid} {v} — {name}\n\n{now()}\n\n방식 {method}. 원본·기존 버전 보존. 최종 GLB 실제 재열기 {tri}삼각형. 공용 palette v001 PNG 한 장·공용 재질. 원색/안전 표시만 원본 color2 칸을 참조. 새 이미지 텍스처 없음.\n\n스크립트 {SCRIPT}. 출처 {source_ref}. 가상 설계 치수·실측 아님. 이번 직접 제작/재사용 추가 Meshy 비용0; 자연 원본 묶음20크레딧은 개별 소품으로 중복 배분하지 않으며 도구가 개별 배분을 제공하지 않으면 null이다. 입력·캐시·출력 토큰 및 금액 배분 미측정. 검수의 실제 범위는 inspection.json과 최종 빌드 증거를 따른다.\n',encoding='utf-8')
 print('SAVED',aid,v,tri,flush=True);return entry,report
def standing_panel(width=1.1,height=1.5,color='cream'):
 box('Panel',(0,0,height/2+.08),(width,.07,height),color)
 for x in [-width*.36,width*.36]:box('Panel foot',(x,0,.035),(.12,.40,.07),'dark')
def clock(x=0,z=1.2):
 o=cyl('Clock face',(x,-.058,z),.18,.018,'white',16);o.rotation_euler.x=math.pi/2
 rod('Clock hand',(x,-.073,z),(x+.09,-.073,z+.07),.008,'dark',4);rod('Clock hand',(x,-.073,z),(x-.035,-.073,z+.12),.006,'dark',4)
def pegboard():
 standing_panel(1.15,1.32,'ochre')
 for x in [-.36,-.12,.12,.36]:
  rod('Tool shank',(x,-.07,.61),(x,-.07,1.12),.018,'dark');box('Tool grip',(x,-.07,.62),(.075,.05,.16),'navy',.01)
  for z in [.89,1.13]:box('Peg',(x,-.07,z),(.025,.04,.025),'cream')
def art(kind='art'):
 standing_panel(1.05,1.4,'walnut');box('Canvas',(0,-.047,.88),(.88,.018,1.08),'cream')
 for x,z,w,h,c in [(-.22,1.04,.27,.48,'sage'),(.20,.76,.32,.35,'ochre'),(.02,1.18,.28,.24,'rose')]:box('Abstract geometric work',(x,-.061,z),(w,.008,h),c)
def books():
 box('Book shelf bottom',(0,0,.025),(.74,.25,.05),'walnut')
 for j in range(7):
  x=(j-3)*.085;h=.22+(j%3)*.035;box('Book cover',(x,0,.05+h/2),(.07,.18,h),['sage','navy','ochre','rose'][j%4]);box('Book spine band',(x,-.096,.11),(.058,.008,.018),'cream')
def papers():
 for i in range(3):box('Paper stack',(-.17+i*.17,.04,.025+i*.003),(.14,.19,.025),'white')
 box('Pen tray',(0,-.13,.018),(.43,.07,.035),'navy')
 for i in range(3):rod('Pen',(-.16+i*.12,-.13,.042),(-.08+i*.12,-.13,.042),.008,'dark',5)
def cubby():
 for z in [.06,.52,.98]:box('Cubbies shelf',(0,0,z),(1.05,.35,.045),'wood')
 for x in [-.51,0,.51]:box('Cubbies divider',(x,0,.52),(.035,.35,.96),'wood')
 for j,(x,z)in enumerate([(-.25,.22),(.25,.22),(-.25,.68),(.25,.68)]):
  box('Storage bin',(x,-.015,z),(.42,.29,.25),['sage','ochre','navy','rose'][j]);box('Bin handle',(x,-.167,z+.05),(.09,.012,.035),'cream')
def curtain():
 for x in [-.48,.48]:rod('Curtain upright',(x,0,.04),(x,0,1.75),.02,'cream');box('Curtain foot',(x,0,.025),(.12,.38,.05),'dark')
 rod('Curtain rail',(-.5,0,1.75),(.5,0,1.75),.025,'cream')
 for j in range(9):box('Pleated privacy fabric',((j-4)*.10,.02 if j%2 else-.02,1.0),(.108,.035,1.32),'teal')
def bottles():
 box('Vanity tray',(0,0,.02),(.62,.30,.04),'cream')
 for j in range(4):
  x=(j-1.5)*.13;cyl('Bottle',(x,0,.14),.045,.22,['rose','teal','cream','navy'][j],8);cyl('Bottle cap',(x,0,.264),.026,.035,'dark',6)
def coatrack():
 for x in [-.45,.45]:box('Coat rack upright',(x,0,.65),(.045,.055,1.3),'walnut');box('Coat rack foot',(x,0,.025),(.14,.40,.05),'walnut')
 box('Coat rack beam',(0,0,1.25),(1.0,.07,.07),'walnut')
 for x in [-.3,0,.3]:rod('Hook',(x,0,1.25),(x,-.12,1.18),.016,'dark');box('Hanging cloth',(x,-.10,.87),(.20,.055,.48),'sage',.02)
def labvials():
 box('Sample rack',(0,0,.05),(.63,.28,.10),'cream')
 for x in [-.24,-.08,.08,.24]:
  cyl('Lab vial',(x,0,.16),.035,.22,'teal',8);cyl('Vial lid',(x,0,.28),.041,.024,'signal_blue',8)
def lamp():
 cyl('Lamp foot',(0,0,.035),.19,.07,'walnut',12);rod('Lamp pole',(0,0,.07),(0,0,1.18),.025,'walnut');cyl('Lamp shade',(0,0,1.23),.28,.37,'cream',12,top=.17)
def jars():
 for j in range(4):
  x=(j-1.5)*.15;cyl('Storage jar',(x,0,.10),.062,.20,['cream','sage','ochre','teal'][j],10);cyl('Jar lid',(x,0,.214),.067,.028,'walnut',10)
def bread():
 box('Baking tray',(0,0,.015),(.70,.45,.03),'steel')
 for x in [-.21,0,.21]:
  box('Bread loaf',(x,0,.095),(.18,.32,.15),'wood',.045)
  for y in [-.08,0,.08]:box('Bread score',(x,y,.173),(.12,.018,.007),'cream')
def backdrop():
 for x in [-.65,.65]:rod('Backdrop support',(x,.15,.03),(x,.15,1.8),.025,'dark');box('Backdrop foot',(x,0,.03),(.18,.60,.06),'dark')
 box('Seamless backdrop',(0,.14,1.0),(1.35,.035,1.55),'cream');box('Backdrop sweep',(0,-.12,.12),(1.35,.55,.035),'cream')
def acoustic():
 standing_panel(1.15,1.5,'dark')
 for x in [-.42,-.14,.14,.42]:
  for z in [.38,.68,.98,1.28]:box('Absorber block',(x,-.07,z),(.25,.10,.25),'navy'if int(z*10)%2 else'steel')
def stagecurtain():
 for x in [-.70,.70]:rod('Curtain frame',(x,0,.04),(x,0,1.85),.03,'dark');box('Stage frame foot',(x,0,.03),(.18,.42,.06),'dark')
 rod('Curtain beam',(-.73,0,1.85),(.73,0,1.85),.035,'dark')
 for x in [-.62,-.50,.50,.62]:box('Stage drape',(x,0,1.04),(.14,.08,1.58),'burgundy')
 for x in [-.4,0,.4]:cyl('Stage lamp',(x,-.03,1.78),.07,.13,'dark',8).rotation_euler.x=math.pi/2
def cones():
 for x in [-.35,0,.35]:
  box('Cone foot',(x,0,.018),(.26,.26,.035),'dark');cyl('Safety cone',(x,0,.19),.095,.34,'signal_red',8,top=.02);cyl('Cone white band',(x,0,.22),.06,.05,'white',8,top=.047)
def pipe():
 standing_panel(1.05,1.52,'cream')
 for x in [-.32,.32]:rod('Upright pipe',(x,-.09,.10),(x,-.09,1.38),.045,'teal',8)
 rod('Pipe connector',(-.32,-.09,1.38),(.32,-.09,1.38),.045,'teal',8)
 for x,z in [(-.32,.75),(.32,1.04)]:
  o=cyl('Valve face',(x,-.16,z),.095,.035,'signal_red',10);o.rotation_euler.x=math.pi/2
  rod('Valve cross',(x-.07,-.185,z),(x+.07,-.185,z),.013,'cream',5)
def hay():
 for x,z in [(-.23,.16),(.23,.16),(0,.45)]:
  box('Hay bale',(x,0,z),(.43,.36,.28),'ochre',.025)
  for y in [-.11,.11]:box('Bale twine',(x,y,z+.143),(.43,.012,.006),'walnut')
def nautical():
 for x in [-.42,.42]:
  cyl('Mooring post',(x,0,.23),.075,.46,'dark',10);cyl('Post collar',(x,0,.35),.09,.045,'safety_yellow',10)
 for z in [.10,.15,.20]:
  for j in range(10):
   a=j*math.tau/10;b=(j+1)*math.tau/10;rod('Coiled rope',(.22*math.cos(a),-.25+.14*math.sin(a),z),(.22*math.cos(b),-.25+.14*math.sin(b),z),.016,'wood',5)
def gymrack():
 cubby()
 for x in [-.3,0,.3]:cyl('Bottle on gym rack',(x,0,1.10),.04,.19,'teal',8)
def legal():
 standing_panel(1.3,1.65,'walnut')
 for x in [-.52,0,.52]:box('Wood molding',(x,-.06,.9),(.035,.03,1.36),'wood')
 o=cyl('Abstract circular medallion',(0,-.08,1.23),.17,.022,'gold',12);o.rotation_euler.x=math.pi/2
 rod('Balanced motif',(-.12,-.10,1.23),(.12,-.10,1.23),.014,'cream',5)
def wayfinding():
 standing_panel(.75,1.35,'navy');box('Direction arrow shaft',(-.04,-.048,1.03),(.35,.018,.07),'safety_yellow')
 o=box('Direction arrow head',(.18,-.048,1.03),(.14,.018,.14),'safety_yellow');o.rotation_euler.y=math.pi/4
 for z in [.53,.72]:box('Information strip',(0,-.05,z),(.53,.018,.06),'cream')
def server():
 standing_panel(1.1,1.5,'steel')
 for x in [-.3,-.1,.1,.3]:rod('Cable run',(x,-.065,.16),(x,-.065,1.4),.022,'navy',6)
 for z in [.4,.9,1.3]:box('Cable tie',(0,-.09,z),(.75,.025,.028),'safety_yellow')
def notice():
 standing_panel(1.1,1.45,'sage')
 for j in range(6):box('Notice paper',((j%3-1)*.29,-.05,.68+(j//3)*.37),(.23,.012,.28),'white');cyl('Colored notice pin',((j%3-1)*.29,-.067,.80+(j//3)*.37),.018,.012,'signal_red',6).rotation_euler.x=math.pi/2
def temple():
 standing_panel(1.1,1.30,'walnut')
 for x in [-.42,-.21,0,.21,.42]:box('Lattice upright',(x,-.052,.8),(.025,.035,1.05),'wood')
 for z in [.30,.55,.80,1.05,1.30]:box('Lattice crossbar',(0,-.054,z),(.98,.035,.025),'wood')
def lantern():
 box('Lantern base',(0,0,.04),(.35,.32,.08),'walnut')
 for x in [-.13,.13]:
  for y in [-.11,.11]:rod('Lantern pillar',(x,y,.08),(x,y,.55),.018,'walnut')
 box('Lantern light core',(0,0,.32),(.21,.19,.38),'ochre');box('Lantern roof',(0,0,.57),(.39,.35,.07),'walnut')
def blanket():
 for z in [.025,.055,.085]:box('Folded textile',(0,0,z),(.48,.34,.03),'rose',.009)
 for x in [-.18,-.06,.06,.18]:box('Woven blanket stripe',(x,0,.103),(.025,.33,.008),'cream')
def patterns(style):
 if style=='planks':
  for x in [i*.35 for i in range(-7,8)]:box('Plank seam',(x,0,.003),(.012,4.4,.003),'walnut')
 elif style in ['grid','paving','squares']:
  spacing=.55 if style!='paving'else .9
  for i in range(-4,5):box('Grout X',(i*spacing,0,.003),(.012,4.4,.003),'cream')
  for i in range(-3,4):box('Grout Y',(0,i*.6,.003),(5.3,.012,.003),'cream')
  if style=='squares':
   for x,y in [(-1.65,-1.2),(-.55,0),(.55,1.2),(1.65,0)]:box('Geometric color tile',(x,y,.003),(.5,.54,.003),'ochre')
 elif style=='hazard':
  for x in [-1.75,1.75]:box('Work zone stripe',(x,0,.003),(.045,3.5,.004),'safety_yellow')
  for y in [-1.8,1.8]:box('Work zone end',(0,y,.003),(3.55,.045,.004),'safety_yellow')
 elif style=='path':
  for j in range(8):box('Path stone',((j%2-.5)*.42,(j//2-1.5)*.75,.005),(.35,.56,.01),'wood',.025)
 elif style=='court':
  for x in [-2,2]:box('Court outer line',(x,0,.003),(.04,3.7,.004),'white')
  for y in [-1.85,0,1.85]:box('Court line',(0,y,.003),(4.04,.04,.004),'white')
 else:
  for j in range(8):
   a=j*math.tau/8;o=box('Lotus geometric petal',(.4*math.cos(a),.4*math.sin(a)-1.15,.004),(.34,.15,.005),'rose');o.rotation_euler.z=a
def simple(name):
 if name=='display':
  for z in [.08,.43,.78]:box('Retail display shelf',(0,0,z),(.85,.35,.05),'wood')
  for x in [-.4,.4]:box('Display upright',(x,.13,.43),(.05,.06,.85),'wood')
  for j in range(6):box('Display package',((j%3-1)*.24,0,.20+(j//3)*.36),(.18,.22,.20),['sage','rose','ochre'][j%3])
 elif name in ['swatches','learning','evidence','status','labwall','glasspanel','windshield']:
  standing_panel(1.2,1.45,'navy'if name in ['status','windshield']else'cream')
  for j in range(6):box(name+' panel insert',((j%3-1)*.32,-.05,.58+(j//3)*.48),(.26,.016,.33),(['signal_blue','teal','navy']if name in ['status','windshield']else['sage','ochre','rose'])[j%3])
 elif name in ['crates','cases']:
  for x,z in [(-.22,.16),(.22,.16),(0,.44)]:
   box('Stacked case',(x,0,z),(.40,.35,.28),'walnut'if name=='crates'else'navy',.015);box('Case label',(x,-.18,z+.02),(.10,.014,.05),'cream')
 elif name in ['towels','media']:
  for j in range(4):box(name+str(j),(0,0,.04+j*.06),(.48,.30,.055),['cream','teal','cream','rose'][j],.01)
 elif name in ['parts','food','paint','brochures']:
  box('Organizer tray',(0,0,.025),(.6,.36,.05),'navy')
  for j in range(6):cyl(name+' item',((j%3-1)*.17,(j//3-.5)*.16,.11),.05,.15,['cream','sage','ochre'][j%3],6)
 elif name=='tires':
  for z in [.10,.28]:cyl('Tire',(0,0,z),.24,.16,'dark',12);cyl('Wheel inset',(0,0,z+.083),.12,.005,'steel',10)
 elif name in ['hazardposts','woodfence']:
  for x in [-.55,.55]:box('Fence post',(x,0,.43),(.07,.08,.86),'walnut'if name=='woodfence'else'steel')
  for z in [.30,.66]:box('Fence beam',(0,0,z),(1.2,.065,.055),'walnut'if name=='woodfence'else'safety_yellow')
 elif name in ['signal','flags']:
  for x in [-.30,.30]:
   cyl('Signal base',(x,0,.02),.1,.04,'dark',8);rod('Signal pole',(x,0,.03),(x,0,.85),.018,'cream');box('Signal flag',(x+.09,0,.75),(.18,.025,.16),'signal_red'if x<0 else'safety_yellow')
 elif name=='pendant':
  for x in [-.55,.55]:rod('Overhead upright',(x,0,.02),(x,0,1.8),.025,'dark');box('Light foot',(x,0,.025),(.16,.4,.05),'dark')
  rod('Light beam',(-.55,0,1.8),(.55,0,1.8),.025,'dark');cyl('Pendant shade',(0,0,1.65),.20,.20,'ochre',12,top=.05)
 elif name=='trellis':
  for x in [-.55,.55]:rod('Trellis upright',(x,0,0),(x,0,1.4),.03,'cream')
  for z in [.3,.6,.9,1.2]:rod('Trellis crossbar',(-.55,0,z),(.55,0,z),.018,'cream')
 elif name=='kitchenwall':
  standing_panel(1.2,1.6,'cream');box('Range hood',(0,-.1,1.45),(.75,.33,.18),'steel');box('Hood flue',(0,0,1.66),(.2,.16,.25),'steel')
 elif name=='benches':
  for x in [-.45,.45]:box('Bench support',(x,0,.20),(.08,.26,.4),'wood')
  box('Bench seat',(0,0,.43),(1.12,.34,.06),'wood')
 elif name=='lotus':
  for j in range(8):
   a=j*math.tau/8;o=box('Offering lotus petal',(.12*math.cos(a),.12*math.sin(a),.05),(.14,.07,.045),'rose',.025);o.rotation_euler.z=a
  cyl('Lotus center',(0,0,.085),.045,.055,'ochre',8)
 else:raise ValueError(name)
RECIPES={'woodscreen':lambda:standing_panel(1.2,1.5,'walnut'),'clock':lambda:(standing_panel(),clock()),'clocks':lambda:(standing_panel(1.5,1.4,'navy'),clock(-.45),clock(),clock(.45)),'pegboard':pegboard,'art':art,'galleryart':art,'books':books,'papers':papers,'cubby':cubby,'curtain':curtain,'bottles':bottles,'coatrack':coatrack,'labvials':labvials,'lamp':lamp,'jars':jars,'bread':bread,'backdrop':backdrop,'acoustic':acoustic,'stagecurtain':stagecurtain,'cones':cones,'pipe':pipe,'hay':hay,'nautical':nautical,'gymrack':gymrack,'legal':legal,'wayfinding':wayfinding,'server':server,'notice':notice,'temple':temple,'lantern':lantern,'blanket':blanket}
REUSE={'vase':('AST-3010','v001'),'pitcher':('AST-3014','v001'),'sculpture':('AST-3011','v001'),'basket':('AST-3008','v001'),'bowl':('AST-3012','v001'),'plant':('AST-010','v001'),'tree':('AST-3161','v001'),'bush':('AST-3162','v001'),'rocks':('AST-3163','v001'),'grass':('AST-3164','v001')}
TABLETOP={'books','papers','labvials','bottles','jars','bread','parts','food','paint','brochures','blanket','towels','media','pitcher','sculpture','basket','bowl','lotus'}
def make_components():
 templates=sorted({n for _,_,ns in plan.SCENES.values()for n in ns}-set(REUSE));refs={}
 for j,n in enumerate(templates):
  aid=f'AST-{3101+j}'
  if(aid,'v001')in LOOKUP:refs[n]=(aid,'v001');continue
  partial=R/f'meshy/models/blender/{aid}/v001/inspection.json'
  if partial.exists():
   rep=json.loads(partial.read_text('utf-8'));src=f'meshy/models/original/{aid}/v001';out=f'meshy/models/blender/{aid}/v001';entry=dict(asset_id=aid,version='v001',name='공간 디테일 — '+n,source_path=src+'/source.blend',blender_path=out+'/model.blend',runtime_path=out+'/exports/model.glb',preview_path=None,unity_path=None,kind='prop',palette_version='v001',accent_reason='Original color2 accents; see fixed UVs.'if n in ['food','signal','flags','cones','hazardposts','status','wayfinding']else None,unity_palette_path=None,inspection_path=out+'/inspection.json',processing_paths=[SCRIPT,'meshy/models/blender/AST-1010/v001/processing/build_shared.py'],status='in_progress',generation_method='blender_direct',generation_reason='Recover completed measured export after transient catalog-write failure; model files preserved.',production_record_path=src+'/README.md',meshy_credits_used=0,produced_by_task='spatial-diversity-v001');CATALOG['assets'].append(entry);LOOKUP[(aid,'v001')]=entry;CREATED.append(entry);write(CAT/'assets.json',CATALOG);(R/entry['production_record_path']).write_text(f'# {aid} v001\n\n실제 완성 GLB 재열기 {rep["scene_triangles"]}삼각형. 모델 생성·검수 완료 뒤 목록 쓰기 일시 오류로 보존 파일에서 등록 복구. 기존 모델은 덮어쓰지 않았다. Blender 직접 제작·Meshy0크레딧. 실행·시각 검수는 아직 미검증. 스크립트 {SCRIPT}.\n',encoding='utf-8');refs[n]=(aid,'v001');continue
  s.reset();(RECIPES[n]if n in RECIPES else lambda:simple(n))();a,rep=save(aid,'v001','공간 디테일 — '+n);refs[n]=(aid,'v001')
 floors={}
 for n,(cell,style,chair)in plan.THEMES.items():
  prior=next((a for a in CATALOG['assets']if a.get('floor_theme')==n),None)
  if prior:floors[n]=(prior['asset_id'],prior['version']);continue
  aid='AST-002';v=version(aid);s.reset();import_asset(aid,'v001')
  for o in meshes():paint(o,('color1',*cell))
  a,rep=save(aid,v,'바닥 표면 — '+n,source_ref={'asset_id':aid,'version':'v001'});a['floor_theme']=n;write(CAT/'assets.json',CATALOG);floors[n]=(aid,v)
  VARIANTS.append(dict(base_asset_ref={'asset_id':aid,'version':'v001'},variant_id='spatial-'+n,state='materialized',palette_version='v001',regions=[dict(part_id='floor',selector='all mesh faces',role='base',cell_ref={'texture_id':'color1','row':cell[0],'column':cell[1]})],result_asset_ref={'asset_id':aid,'version':v}))
 pattern_refs={}
 for j,style in enumerate(sorted({x[1]for x in plan.THEMES.values()})):
  aid='AST-3180';v='v'+str(j+1).zfill(3)
  if(aid,v)in LOOKUP:pattern_refs[style]=(aid,v);continue
  s.reset();patterns(style);save(aid,v,'바닥 무늬 — '+style);pattern_refs[style]=(aid,v)
 chair_refs={}
 for n in sorted({x[2]for x in plan.THEMES.values()}):
  prior=next((a for a in CATALOG['assets']if a.get('spatial_chair_theme')==n),None)
  if prior:chair_refs[n]=(prior['asset_id'],prior['version']);continue
  aid='AST-1011';v=version(aid);s.reset();import_asset(aid,'v001')
  for o in meshes():
   if o.name.startswith(('Seat','Backrest')):paint(o,n)
  a,_=save(aid,v,'고정형 의자 — '+n,source_ref={'asset_id':aid,'version':'v001'});a['spatial_chair_theme']=n;write(CAT/'assets.json',CATALOG);chair_refs[n]=(aid,v);cell=COLORS[n]
  VARIANTS.append(dict(base_asset_ref={'asset_id':aid,'version':'v001'},variant_id='spatial-'+n,state='materialized',palette_version='v001',regions=[dict(part_id='seat-back',selector='objects starting Seat or Backrest; all faces',role='base',cell_ref=dict(texture_id=cell[0],row=cell[1],column=cell[2]))],result_asset_ref=dict(asset_id=aid,version=v)))
 # Reconstruct recipes on resume too; completed fixed variants are not remade.
 VARIANTS.clear()
 for n,key in floors.items():
  cell=plan.THEMES[n][0];VARIANTS.append(dict(base_asset_ref={'asset_id':'AST-002','version':'v001'},variant_id='spatial-'+n,state='materialized',palette_version='v001',regions=[dict(part_id='floor',selector='all mesh faces',role='base',cell_ref={'texture_id':'color1','row':cell[0],'column':cell[1]})],result_asset_ref={'asset_id':key[0],'version':key[1]}))
 for n,key in chair_refs.items():
  cell=COLORS[n];VARIANTS.append(dict(base_asset_ref={'asset_id':'AST-1011','version':'v001'},variant_id='spatial-'+n,state='materialized',palette_version='v001',regions=[dict(part_id='seat-back',selector='objects starting Seat or Backrest; all faces',role='base',cell_ref={'texture_id':cell[0],'row':cell[1],'column':cell[2]})],result_asset_ref={'asset_id':key[0],'version':key[1]}))
 return refs,floors,pattern_refs,chair_refs
def overlap(a,b,margin=.04):return all(min(a[1][k],b[1][k])-max(a[0][k],b[0][k])>margin for k in range(3))
def top_surface(obs):
 clusters={}
 for o in obs:
  normalmat=o.matrix_world.to_3x3().inverted().transposed()
  for p in o.data.polygons:
   normal=(normalmat@p.normal).normalized()
   if normal.z<.95:continue
   pts=[o.matrix_world@o.data.vertices[i].co for i in p.vertices];z=sum(p.z for p in pts)/len(pts);key=round(z,2);area=p.area*abs(o.matrix_world.to_scale().x*o.matrix_world.to_scale().y)
   clusters.setdefault(key,[0,[]]);clusters[key][0]+=area;clusters[key][1]+=pts
 if not clusters:return None
 z,(area,pts)=max(clusters.items(),key=lambda x:x[1][0])
 if area<.08:return None
 return z,(min(p.x for p in pts),max(p.x for p in pts),min(p.y for p in pts),max(p.y for p in pts))
def attach(item,office=False):
 obs=import_asset(item['asset_id'],item['version']);root=bpy.data.objects.new(item['instance_id'],None);bpy.context.collection.objects.link(root)
 for o in obs:
  if o.parent is None:o.parent=root
 root.location=item['position_blender_m'];root.scale=item['scale'];root.rotation_euler=[math.radians(x)for x in item.get('rotation_euler_blender_deg',[0,0,math.degrees(item.get('rotation_z_rad',0))])];bpy.context.view_layer.update();ms=[o for o in obs if o.type=='MESH']
 if office:
  bpy.ops.object.select_all(action='DESELECT')
  for o in ms:o.select_set(True)
  bpy.context.view_layer.objects.active=ms[0]
  if len(ms)>1:bpy.ops.object.join()
  obj=bpy.context.object;world=obj.matrix_world.copy();obj.parent=None;obj.matrix_world=world;bpy.ops.object.transform_apply(location=True,rotation=True,scale=True);bpy.data.objects.remove(root,do_unlink=True);obj.name=item['instance_id'];root=obj;ms=[obj]
 item['component_mesh_count']=len(ms);return root,ms
def produce_room(room,refs,floors,patterns_ref,chairs):
 number=int(room['roomId'][4:]);theme,intent,details=plan.SCENES[number];office=number==1;aid=room['assetId'];v=version(aid);old=room['assetVersion'];p=R/f'meshy/models/blender/{aid}/{old}/placements.json';pl=json.loads(p.read_text('utf-8'));items=copy.deepcopy(pl['instances']);s.reset();solids=[];surfaces=[];currenttri=0;decisions=[]
 for i in items:
  if i['asset_id']=='AST-002':i['asset_id'],i['version']=floors[theme]
  if i['asset_id']=='AST-1011':i['asset_id'],i['version']=chairs[plan.THEMES[theme][2]]
  root,ms=attach(i,office);currenttri+=tris(ms);name=LOOKUP[(i['asset_id'],i['version'])]['name']
  if i['asset_id']not in ['AST-001','AST-002']:
   b=bounds(ms);solids.append((b,i['instance_id']))
   if any(x in name for x in ['책상','테이블','작업대','조리대','탁자','카운터']):
    surf=top_surface(ms)
    if surf:surfaces.append((surf,i['instance_id']))
 # Ground decoration has no solid-volume occupation and is counted once.
 key=patterns_ref[plan.THEMES[theme][1]];i=dict(asset_id=key[0],version=key[1],candidate_id=None,instance_id=f'{key[0]}-{len(items):03}',position_blender_m=[0,-.38 if office else 0,.297],scale=[.84,.77,1]if office else[1,1,1],rotation_euler_blender_deg=[0,0,0],rotation_z_rad=0,detail_role='floor_pattern');root,ms=attach(i,office);currenttri+=tris(ms);items.append(i)
 candidates=[(-2.15,1.9),(-.9,2.12),(.35,2.12),(1.7,2.12),(2.10,.75),(-2.12,.65),(-2.1,-1.6),(2.1,-1.6),(0,1.8),(1.9,-.7),(-1.9,-.7)]
 for detail in details:
  key=REUSE.get(detail,refs.get(detail));a=LOOKUP[key];rep=json.loads((R/a['inspection_path']).read_text('utf-8'));tri=rep['scene_triangles']
  if currenttri+tri>5000:decisions.append({'detail':detail,'status':'not_added','reason':'5000 triangle budget'});continue
  # Organic source is used sparingly, at the scale of an actual room accent.
  scale=.85 if detail=='tree'else .7 if detail=='bush'else .45 if detail in ['vase','pitcher','sculpture','basket','bowl']else .7 if detail in TABLETOP else .75
  before=set(bpy.context.scene.objects);obs=import_asset(*key);root=bpy.data.objects.new(f'{key[0]}-{len(items):03}',None);bpy.context.collection.objects.link(root)
  for o in obs:
   if o.parent is None:o.parent=root
  ms=[o for o in obs if o.type=='MESH'];root.scale=[scale]*3;root.location=(0,0,0);bpy.context.view_layer.update();lo,hi=bounds(ms);chosen=None;support=None
  trials=[]
  if detail in TABLETOP:
   for(z,(xmin,xmax,ymin,ymax)),sid in surfaces:
    if z<.45:continue
    for fx,fy in [(.15,.20),(.85,.20),(.15,.75),(.85,.75),(.50,.50)]:trials.append(((xmin+(xmax-xmin)*fx,ymin+(ymax-ymin)*fy,z+.007-lo[2]),sid,(xmin,xmax,ymin,ymax)))
  else:trials=[((x,y,.296-lo[2]),None,None)for x,y in candidates]
  for pos,sid,limits in trials:
   root.location=pos;bpy.context.view_layer.update();b=bounds(ms)
   if b[0][0]<-2.77 or b[1][0]>2.77 or b[0][1]<-2.37 or b[1][1]>2.37:continue
   if limits and(b[0][0]<limits[0]+.01 or b[1][0]>limits[1]-.01 or b[0][1]<limits[2]+.01 or b[1][1]>limits[3]-.01):continue
   if any(overlap(b,other,.025)for other,oid in solids if oid!=sid):continue
   chosen=list(pos);support=sid;break
  if chosen is None:
   for o in list(bpy.context.scene.objects):
    if o not in before:bpy.data.objects.remove(o,do_unlink=True)
   decisions.append({'detail':detail,'status':'not_added','reason':'No collision-free supported position'});continue
  if office:
   bpy.ops.object.select_all(action='DESELECT')
   for o in ms:o.select_set(True)
   bpy.context.view_layer.objects.active=ms[0]
   if len(ms)>1:bpy.ops.object.join()
   obj=bpy.context.object;world=obj.matrix_world.copy();obj.parent=None;obj.matrix_world=world;bpy.ops.object.transform_apply(location=True,rotation=True,scale=True);name=root.name;bpy.data.objects.remove(root,do_unlink=True);obj.name=name;ms=[obj];root=obj
  item=dict(asset_id=key[0],version=key[1],candidate_id=None,instance_id=root.name,position_blender_m=chosen,rotation_euler_blender_deg=[0,0,0],rotation_z_rad=0,scale=[scale]*3,component_mesh_count=len(ms),detail_role=detail,support_instance_id=support)
  items.append(item);solids.append((bounds(ms),root.name));currenttri+=tri;decisions.append({'detail':detail,'status':'added','instance_id':root.name,'support_instance_id':support})
 props={}
 for i in items:
  key=(i['asset_id'],i['version']);a=LOOKUP[key];tri=json.loads((R/a['inspection_path']).read_text('utf-8'))['scene_triangles']
  if key not in props:props[key]=dict(name=a['name'],asset_ref=dict(asset_id=key[0],version=key[1]),triangles_per_instance=tri,instance_count=0,total_triangles=0)
  props[key]['instance_count']+=1;props[key]['total_triangles']+=tri
 pl.update(instances=items,art_direction={'theme':theme,'intent':intent,'detail_decisions':decisions},change_reason='User authorized distinct character/detail for remaining69 spaces; existing game targets and placements preserved.')
 entry,report=save(aid,v,room['name'],'diorama','hybrid'if any(i['asset_id']in ['AST-3161','AST-3162','AST-3163','AST-3164','AST-3010','AST-3011','AST-3012','AST-3014','AST-3008']for i in items)else'blender_direct',props=list(props.values()),placements=pl,source_ref={'asset_id':aid,'version':old})
 if office:
  # Office bindings require the three exact mesh names on renderers/colliders.
  names={o.name for o in meshes()};assert {'AST-005-0','AST-009-0','AST-015-0'}<=names,names
 room.update(assetVersion=v,sourceFbxPath=f'meshy/models/blender/{aid}/{v}/exports/room.fbx',scenePath=f'Assets/Scenes/Workplaces/{room["roomId"]}-detail-v010.unity',triangles=report['scene_triangles'],instances=len(items))
 return entry,report,pl
def main():
 reg=json.loads((R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json').read_text('utf-8'))
 if not(EV/'registry-before.json').exists():write(EV/'registry-before.json',reg);write(EV/'asset-catalog-before.json',BASE)
 refs,floors,patterns_ref,chairs=make_components();assemblies=s.read('scene-assemblies');results=json.loads((EV/'production-progress.json').read_text('utf-8'))['rooms']if(EV/'production-progress.json').exists()else[];completed={x['room_id']:x for x in results}
 for room in reg['rooms']:
  number=int(room['roomId'][4:])
  if number not in plan.SCENES:continue
  if room['roomId']in completed:
   row=completed[room['roomId']];a=row['asset_ref'];room.update(assetVersion=a['version'],sourceFbxPath=f'meshy/models/blender/{a["asset_id"]}/{a["version"]}/exports/room.fbx',scenePath=f'Assets/Scenes/Workplaces/{room["roomId"]}-detail-v010.unity',triangles=row['triangles'],instances=row['instances']);continue
  recovered=next((a for a in CATALOG['assets']if a['asset_id']==room['assetId']and a.get('produced_by_task')=='spatial-diversity-v001'and a['kind']=='diorama'),None)
  if recovered:
   entry=recovered;rep=json.loads((R/entry['inspection_path']).read_text('utf-8'));pl=json.loads((R/f'meshy/models/blender/{entry["asset_id"]}/{entry["version"]}/placements.json').read_text('utf-8'));room.update(assetVersion=entry['version'],sourceFbxPath=f'meshy/models/blender/{entry["asset_id"]}/{entry["version"]}/exports/room.fbx',scenePath=f'Assets/Scenes/Workplaces/{room["roomId"]}-detail-v010.unity',triangles=rep['scene_triangles'],instances=len(pl['instances']))
  else:entry,rep,pl=produce_room(room,refs,floors,patterns_ref,chairs)
  previous=max((a for a in assemblies['assemblies']if a['assembly_asset_ref']['asset_id']==room['assetId']),key=lambda a:a['revision'])
  prompt_ref=previous.get('prompt_ref',{'catalog':'panorama-prompts-v002','prompt_id':room['promptId'],'version':room['promptVersion']});panorama_ref=previous.get('panorama_ref',{'catalog':'panoramas','image_id':room['roomId'],'version':'v001'})
  row=copy.deepcopy(previous);row.update(revision=previous['revision']+1,recorded_at=now(),prompt_ref=prompt_ref,panorama_ref=panorama_ref,assembly_asset_ref={'asset_id':entry['asset_id'],'version':entry['version']},placements_path=f'meshy/models/blender/{entry["asset_id"]}/{entry["version"]}/placements.json',inspection_path=entry['inspection_path'],component_counts=rep['props'],change_reason=pl['change_reason']);assemblies['assemblies'].append(row)
  results.append(dict(room_id=room['roomId'],name=room['name'],asset_ref={'asset_id':entry['asset_id'],'version':entry['version']},art_direction=pl['art_direction'],triangles=rep['scene_triangles'],instances=len(pl['instances']),prompt_ref=prompt_ref,panorama_ref=panorama_ref))
  write(EV/'production-progress.json',dict(schema_version=3,rooms=results,created=[{'asset_id':a['asset_id'],'version':a['version']}for a in CREATED]));write(CAT/'assets.json',CATALOG);write(CAT/'scene-assemblies.json',assemblies)
 reg['buildId']='workplaces-v010';current=set()
 for room in reg['rooms']:
  current.add((room['assetId'],room['assetVersion']));p=R/f'meshy/models/blender/{room["assetId"]}/{room["assetVersion"]}/placements.json'
  for i in json.loads(p.read_text('utf-8'))['instances']:current.add((i['asset_id'],i['version']))
 reg['assets']=[dict(assetId=k[0],version=k[1],name=LOOKUP[k]['name'])for k in sorted(current)];write(R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json',reg)
 variants=s.read('asset-color-variants')if(CAT/'asset-color-variants.json').exists()else dict(schema_version=3,variants=[]);variants['variants']+=VARIANTS;write(CAT/'asset-color-variants.json',variants)
 write(EV/'production.json',dict(schema_version=3,rooms=results,created=[{'asset_id':a['asset_id'],'version':a['version']}for a in CATALOG['assets']if a.get('produced_by_task')=='spatial-diversity-v001'],used_detail_refs={k:{'asset_id':v[0],'version':v[1]}for k,v in {**refs,**REUSE}.items()},meshy_credit_scope='Nature source batch20 this task; source decor reuse prior20 not charged again.',runtime_status='unverified'))
 print('SPATIAL_PRODUCED',len(results),len(CREATED),flush=True)
if __name__=='__main__':main()

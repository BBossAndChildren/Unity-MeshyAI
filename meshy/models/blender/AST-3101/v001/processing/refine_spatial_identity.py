"""Refine semantic panels and give sparse scenes supported detail displays.
Uses the completed first pass; no additional paid service calls.
"""
import bpy,json,math,copy,importlib.util
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parents[6];spec=importlib.util.spec_from_file_location('p',Path(__file__).with_name('build_spatial_details.py'));p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p);p.SCRIPT=Path(__file__).relative_to(R).as_posix()
data=json.loads((p.EV/'production.json').read_text('utf-8'));reg=json.loads((R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json').read_text('utf-8'));refs={k:(v['asset_id'],v['version'])for k,v in data['used_detail_refs'].items()};replacements={}
def brochure():
 p.box('Brochure holder',(0,0,.025),(.60,.30,.05),'navy')
 for j in range(4):
  x=(j-1.5)*.13;p.box('Folded information sheet',(x,.02,.17),(.11,.055,.28),'cream');p.box('Cover color band',(x,-.012,.19),(.10,.009,.055),['sage','rose','navy','ochre'][j])
def labwall():
 for x in [-.55,.55]:p.box('Clean supply cabinet side',(x,0,.77),(.06,.30,1.46),'white')
 for z in [.055,.50,.98,1.50]:p.box('Clean supply shelf',(0,0,z),(1.15,.31,.05),'white')
 p.box('Cabinet back',(0,.13,.78),(1.1,.025,1.43),'navy')
 for j in range(6):
  x=(j%3-1)*.31;z=.64+(j//3)*.49;p.cyl('Supply bottle',(x,-.02,z),.055,.22,'cream',8);p.cyl('Supply bottle cap',(x,-.02,z+.12),.048,.025,'signal_blue',8)
def evidence():
 p.standing_panel(1.2,1.45,'walnut')
 centers=[]
 for j in range(6):
  x=(j%3-1)*.32;z=.53+(j//3)*.51;centers.append((x,-.065,z));p.box('Fictional evidence card',(x,-.048,z),(.24,.015,.30),'cream');p.box('Geometric photo placeholder',(x,-.059,z+.025),(.18,.009,.13),'steel')
 for a,b in [(0,4),(1,3),(2,4),(3,5)]:p.rod('Relationship string',centers[a],centers[b],.004,'signal_red',4)
def learning():
 p.standing_panel(1.2,1.45,'cream')
 for j in range(3):
  x=(j-1)*.34;o=p.cyl('Learning circular shape',(x,-.07,1.1),.11,.025,['rose','teal','ochre'][j],10);o.rotation_euler.x=math.pi/2
 for z in [.50,.70]:
  p.rod('Counting rail',(-.48,-.09,z),(.48,-.09,z),.012,'walnut',6)
  for j in range(5):p.cyl('Counting bead',((j-2)*.18,-.09,z),.045,.065,['rose','teal','ochre'][j%3],8).rotation_euler.x=math.pi/2
def glasspanel():
 for x in [-.55,.55]:p.box('Privacy frame upright',(x,0,.77),(.045,.065,1.5),'cream');p.box('Privacy frame foot',(x,0,.025),(.1,.39,.05),'dark')
 p.box('Frosted privacy panel',(0,0,.91),(1.05,.035,1.12),'teal');p.box('Privacy lower stripe',(0,-.022,.63),(1.04,.01,.05),'white')
def windshield():
 for x in [-.55,0,.55]:p.box('Window mullion',(x,0,.84),(.045,.07,1.35),'dark')
 for z in [.19,1.50]:p.box('Bridge window frame',(0,0,z),(1.15,.08,.055),'dark')
 for x in [-.275,.275]:p.box('Forward blue glazing',(x,.012,.84),(.50,.025,1.25),'teal')
 for x in [-.4,.4]:p.box('Window base foot',(x,0,.035),(.12,.38,.07),'dark')
def galleryart():
 p.standing_panel(1.05,1.4,'walnut');p.box('Gallery canvas',(0,-.05,.87),(.88,.018,1.07),'cream')
 o=p.cyl('Relief circle',(-.15,-.083,1.1),.18,.025,'ochre',16);o.rotation_euler.x=math.pi/2
 for x,z,a in [(.17,.72,25),(-.08,.59,-20)]:o=p.box('Raised geometric stroke',(x,-.08,z),(.36,.028,.20),'sage');o.rotation_euler.y=math.radians(a)
def woodscreen():
 for x in [-.5,.5]:p.box('Wood screen foot',(x,0,.035),(.13,.40,.07),'walnut')
 for j in range(11):p.box('Warm timber slat',((j-5)*.105,0,.80),(.055,.07,1.45),'walnut')
for key,fn in [('brochures',brochure),('labwall',labwall),('evidence',evidence),('learning',learning),('glasspanel',glasspanel),('windshield',windshield),('galleryart',galleryart),('woodscreen',woodscreen)]:
 aid=refs[key][0];v=p.version(aid);p.s.reset();fn();old=refs[key];p.save(aid,v,'공간 디테일 — '+key,source_ref={'asset_id':old[0],'version':old[1]});replacements[key]=(aid,v);refs[key]=(aid,v)
# Only sparse rooms receive an extra supported freestanding display; this is
# not a blanket layer of identical furnishings throughout every scene.
fallback_keys=set()
for row in data['rooms']:
 if sum(d['status']=='added'for d in row['art_direction']['detail_decisions'])<2:
  fallback_keys.update(d['detail']for d in row['art_direction']['detail_decisions']if d['status']=='not_added'and d['detail']in p.TABLETOP)
stand_refs={}
for key in sorted(fallback_keys):
 aid,old=refs[key];v=p.version(aid);p.s.reset();obs=p.import_asset(aid,old)
 for o in obs:
  if o.parent is None:o.location.z+=.80
 p.box('Display tabletop',(0,0,.78),(.78,.48,.04),'wood')
 for x in [-.31,.31]:
  for y in [-.17,.17]:p.box('Display support leg',(x,y,.385),(.04,.04,.77),'dark')
 p.save(aid,v,'전시 선반 — '+key,method='hybrid'if key in ['pitcher','bowl','sculpture','basket','vase']else'blender_direct',source_ref={'asset_id':aid,'version':old});stand_refs[key]=(aid,v)
before=copy.deepcopy(data);assemblies=p.s.read('scene-assemblies');changed=[]
for row in data['rooms']:
 room=next(x for x in reg['rooms']if x['roomId']==row['room_id']);aid=room['assetId'];old=room['assetVersion'];pl=json.loads((R/f'meshy/models/blender/{aid}/{old}/placements.json').read_text('utf-8'));items=pl['instances'];decisions=pl['art_direction']['detail_decisions'];sparse=sum(d['status']=='added'for d in decisions)<2
 if not any(i.get('detail_role')in replacements for i in items)and not sparse:continue
 p.s.reset();solids=[]
 for i in items:
  if i.get('detail_role')in replacements:i['asset_id'],i['version']=replacements[i['detail_role']]
  root,ms=p.attach(i,room['roomId']=='PAN-001')
  if i['asset_id']not in ['AST-001','AST-002','AST-3180']:solids.append(p.bounds(ms))
 current=sum(json.loads((R/p.LOOKUP[(i['asset_id'],i['version'])]['inspection_path']).read_text('utf-8'))['scene_triangles']for i in items)
 if sparse:
  for key in [d['detail']for d in list(decisions)if d['status']=='not_added'and d['detail']in stand_refs]:
   ref=stand_refs[key];tri=json.loads((R/p.LOOKUP[ref]['inspection_path']).read_text('utf-8'))['scene_triangles']
   if current+tri>5000:continue
   obs=p.import_asset(*ref);root=bpy.data.objects.new(f'{ref[0]}-{len(items):03}',None);bpy.context.collection.objects.link(root)
   for o in obs:
    if o.parent is None:o.parent=root
   ms=[o for o in obs if o.type=='MESH'];root.scale=(.7,.7,.7);root.location=(0,0,0);lo,hi=p.bounds(ms);chosen=None
   for x,y in [(-2.1,1.85),(2.1,1.85),(-2.0,-1.5),(2,-1.5),(-2.05,.6),(2.05,.6),(0,2.1),(1.5,-1.5),(-1.5,-1.5)]:
    root.location=(x,y,.296-lo[2]);b=p.bounds(ms)
    if b[0][0]<-2.75 or b[1][0]>2.75 or b[0][1]<-2.36 or b[1][1]>2.36 or any(p.overlap(b,s,.025)for s in solids):continue
    chosen=list(root.location);solids.append(b);break
   if chosen:
    items.append(dict(asset_id=ref[0],version=ref[1],candidate_id=None,instance_id=root.name,position_blender_m=chosen,rotation_euler_blender_deg=[0,0,0],rotation_z_rad=0,scale=[.7,.7,.7],component_mesh_count=len(ms),detail_role=key,support_instance_id=None));current+=tri;decisions.append(dict(detail=key,status='added',instance_id=root.name,support_instance_id=None,reason='Dedicated self-supported display after tabletop fit rejection'))
   else:
    for o in obs:bpy.data.objects.remove(o,do_unlink=True)
    bpy.data.objects.remove(root,do_unlink=True)
   if sum(d['status']=='added'for d in decisions)>=2:break
 props={}
 for i in items:
  key=(i['asset_id'],i['version']);a=p.LOOKUP[key];tri=json.loads((R/a['inspection_path']).read_text('utf-8'))['scene_triangles']
  if key not in props:props[key]=dict(name=a['name'],asset_ref={'asset_id':key[0],'version':key[1]},triangles_per_instance=tri,instance_count=0,total_triangles=0)
  props[key]['instance_count']+=1;props[key]['total_triangles']+=tri
 v=p.version(aid);entry,rep=p.save(aid,v,room['name'],'diorama',method='hybrid',props=list(props.values()),placements=pl,source_ref={'asset_id':aid,'version':old});previous=max((a for a in assemblies['assemblies']if a['assembly_asset_ref']['asset_id']==aid),key=lambda a:a['revision']);asm=copy.deepcopy(previous);asm.update(revision=previous['revision']+1,recorded_at=p.now(),assembly_asset_ref={'asset_id':aid,'version':v},placements_path=f'meshy/models/blender/{aid}/{v}/placements.json',inspection_path=entry['inspection_path'],component_counts=rep['props'],change_reason='Distinct functional panel geometry and supported displays for otherwise sparse rooms; no paid regeneration.');assemblies['assemblies'].append(asm);room.update(assetVersion=v,sourceFbxPath=f'meshy/models/blender/{aid}/{v}/exports/room.fbx',triangles=rep['scene_triangles'],instances=len(items));row.update(asset_ref={'asset_id':aid,'version':v},triangles=rep['scene_triangles'],instances=len(items),art_direction=pl['art_direction']);changed.append(room['roomId']);p.write(p.CAT/'scene-assemblies.json',assemblies)
keys=set()
for room in reg['rooms']:
 keys.add((room['assetId'],room['assetVersion']));pl=json.loads((R/f'meshy/models/blender/{room["assetId"]}/{room["assetVersion"]}/placements.json').read_text('utf-8'));keys.update((i['asset_id'],i['version'])for i in pl['instances'])
reg['assets']=[dict(assetId=k[0],version=k[1],name=p.LOOKUP[k]['name'])for k in sorted(keys)];p.write(p.EV/'production-phase1.json',before);data['used_detail_refs'].update({k:{'asset_id':v[0],'version':v[1]}for k,v in replacements.items()});data['created']=[{'asset_id':a['asset_id'],'version':a['version']}for a in p.CATALOG['assets']if a.get('produced_by_task')=='spatial-diversity-v001'];data['semantic_refined_room_ids']=changed;p.write(p.EV/'production.json',data);p.write(R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json',reg);p.write(p.CAT/'assets.json',p.CATALOG);print('REFINED_SPATIAL',len(changed),flush=True)

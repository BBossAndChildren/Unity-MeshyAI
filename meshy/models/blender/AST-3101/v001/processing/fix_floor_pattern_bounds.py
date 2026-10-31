"""Repair floor seams using new fixed versions; preserve v010 and prior models.

One production repair only; not an agent hook or installed checking system.
Reuses the shared palette/model/export pipeline and reopens every final GLB.
"""
import bpy,copy,importlib.util,json,math
from pathlib import Path
from mathutils import Matrix,Vector

HERE=Path(__file__).parent
spec=importlib.util.spec_from_file_location('p',HERE/'build_spatial_details.py')
p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p)
R=p.R;p.SCRIPT=Path(__file__).relative_to(R).as_posix()
EV=p.EV;REG=R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json'
CHECKPOINT=EV/'floor-pattern-repair-progress.json'
state=json.loads(CHECKPOINT.read_text('utf-8'))if CHECKPOINT.exists()else dict(schema_version=3,patterns=[],rooms=[])
reg=json.loads(REG.read_text('utf-8'));data=json.loads((EV/'production.json').read_text('utf-8'))
for source,target in [(REG,EV/'registry-before-floor-repair.json'),(EV/'production.json',EV/'production-before-floor-repair.json')]:
 if not target.exists():target.write_bytes(source.read_bytes())
assemblies=p.s.read('scene-assemblies')

def next_version(aid,minimum=1):
 versions=[int(v[1:])for k,v in p.LOOKUP if k==aid]
 base=R/f'meshy/models/blender/{aid}'
 if base.exists():versions += [int(d.name[1:])for d in base.iterdir()if d.is_dir()and d.name.startswith('v')and d.name[1:].isdigit()]
 return f'v{max([minimum-1]+versions)+1:03}'

def fixed_pattern(style):
 if style=='planks':
  for i in range(-6,7):p.box('Plank seam',(i*.35,0,.003),(.012,3.8,.003),'walnut')
 elif style in ['grid','paving','squares']:
  spacing=.9 if style=='paving'else .55
  for i in range(-2,3)if style=='paving'else range(-4,5):p.box('Grout X',(i*spacing,0,.003),(.012,3.8,.003),'cream')
  for i in range(-2,3)if style=='paving'else range(-3,4):p.box('Grout Y',(0,i*(.9 if style=='paving'else .6),.003),(4.5 if style=='paving'else 4.6,.012,.003),'cream')
  if style=='squares':
   for x,y in [(-1.65,-1.2),(-.55,0),(.55,1.2),(1.65,0)]:p.box('Geometric color tile',(x,y,.003),(.5,.54,.003),'ochre')
 else:raise ValueError(style)

old_patterns=[a for a in p.CATALOG['assets']if a['asset_id']=='AST-3180'and int(a['version'][1:])<=8]
for a in old_patterns:
 style=a['name'].split(' — ')[-1];ins=json.loads((R/a['inspection_path']).read_text('utf-8'));b=ins['bounds_blender_m']
 outside=b['min'][0]<-2.30001 or b['max'][0]>2.30001 or b['min'][1]<-1.90001 or b['max'][1]>1.90001
 if not outside:continue
 prior=next((x for x in state['patterns']if x['old_asset_ref']==dict(asset_id=a['asset_id'],version=a['version'])),None)
 if prior:continue
 assert style in ['planks','grid','paving','squares'],(style,b)
 v=next_version('AST-3180',10);p.s.reset();fixed_pattern(style)
 entry,rep=p.save('AST-3180',v,'바닥 무늬 — '+style,source_ref=dict(asset_id=a['asset_id'],version=a['version']))
 b=rep['bounds_blender_m'];assert b['min'][0]>=-2.30001 and b['max'][0]<=2.30001 and b['min'][1]>=-1.90001 and b['max'][1]<=1.90001,b
 entry.update(floor_pattern_style=style,floor_pattern_repair='v011-safe-extent')
 p.write(p.CAT/'assets.json',p.CATALOG)
 state['patterns'].append(dict(style=style,old_asset_ref=dict(asset_id=a['asset_id'],version=a['version']),asset_ref=dict(asset_id='AST-3180',version=v),bounds_blender_m=b,triangles=rep['scene_triangles']))
 p.write(CHECKPOINT,state)

replacement={(x['old_asset_ref']['asset_id'],x['old_asset_ref']['version']):(x['asset_ref']['asset_id'],x['asset_ref']['version'])for x in state['patterns']}
orientation_path=EV/'orientation-corrections-v011.json'
assert orientation_path.exists(),'Wait for confirmed local-axis orientation recipe before room assembly.'
orientation=json.loads(orientation_path.read_text('utf-8'))
corrections={}
for correction in orientation['corrections']:
 assert correction.get('status','confirmed')=='confirmed',correction
 corrections.setdefault(correction['room_id'],{})[correction['instance_id']]=correction

# The actual v010 capture/GLB showed a free-standing straight ladder with no
# wall or rear support. Preserve v001 and reuse its existing named front frame.
ladder_old=('AST-1136','v001');ladder_state=state.get('ladder_repair')
if not ladder_state:
 assert ladder_old in p.LOOKUP
 p.s.reset();p.import_asset(*ladder_old);front=p.meshes();lo,hi=p.bounds(front)
 height=hi[2]-lo[2];width=hi[0]-lo[0]
 tilt=Matrix.Rotation(math.radians(-8),4,'X')@Matrix.Translation((0,0,-lo[2]))
 for o in front:o.matrix_world=tilt@o.matrix_world
 lo2,hi2=p.bounds(front);vertical=Matrix.Diagonal((1,1,height/(hi2[2]-lo2[2]),1))@Matrix.Translation((0,0,-lo2[2]))
 for o in front:o.matrix_world=vertical@o.matrix_world
 hinge_y=height*math.sin(math.radians(8));rear_y=.52
 for x in [-.25,.25]:
  p.rod('Rear support leg',(x,rear_y,.025),(x,hinge_y,height-.04),.020,'steel',8)
  p.box('Rear foot pad',(x,rear_y,.015),(.04,.07,.03),'dark')
  p.box('Front foot pad',(x,0,.015),(.04,.07,.03),'dark')
  z=.68;front_y=z*math.tan(math.radians(8));back_y=rear_y+(hinge_y-rear_y)*(z-.025)/(height-.065)
  p.rod('Open position spreader',(x,front_y,z),(x,back_y,z),.012,'steel',6)
 p.rod('Rear lower cross brace',(-.25,.46,.30),(.25,.46,.30),.014,'steel',8)
 p.rod('Top hinge',(-.25,hinge_y,height-.04),(.25,hinge_y,height-.04),.018,'steel',8)
 v=next_version('AST-1136');entry,rep=p.save('AST-1136',v,'자립형 A형 짧은 사다리',source_ref=dict(asset_id=ladder_old[0],version=ladder_old[1]))
 b=rep['bounds_blender_m'];assert abs(b['min'][2])<.0001 and abs(rep['dimensions_m'][2]-height)<.001 and abs(rep['dimensions_m'][0]-width)<.01
 ladder_state=dict(old_asset_ref=dict(asset_id=ladder_old[0],version=ladder_old[1]),asset_ref=dict(asset_id='AST-1136',version=v),triangles=rep['scene_triangles'],bounds_blender_m=b,front_tilt_deg=8,preserved_width_m=width,preserved_height_m=height,source_basis='Actual v010 PAN-037 capture and v001 GLB Rail2/Rung6 with no wall or rear support.')
 state['ladder_repair']=ladder_state;p.write(CHECKPOINT,state)
ladder_ref=(ladder_state['asset_ref']['asset_id'],ladder_state['asset_ref']['version'])
def covers_latest_recipe(row):
 applied={x['instance_id']:x['rotation_euler_blender_deg'] for x in row.get('orientation_changes',[])}
 return all(applied.get(i)==c['rotation_euler_blender_deg'] for i,c in corrections.get(row['room_id'],{}).items())
# A later evidence-backed direction recipe may arrive during an earlier pass.
# Preserve that model version and rebuild only the rooms missing new corrections.
state['rooms']=[x for x in state['rooms'] if covers_latest_recipe(x)]
completed={x['room_id']:x for x in state['rooms']}
for room in reg['rooms']:
 rid=room['roomId']
 if rid in completed:
  row=completed[rid];room.update(assetVersion=row['asset_ref']['version'],sourceFbxPath=row['source_fbx_path'],scenePath=row['scene_path'],triangles=row['triangles'],instances=row['instances']);continue
 aid,old=room['assetId'],room['assetVersion'];pl=json.loads((R/f'meshy/models/blender/{aid}/{old}/placements.json').read_text('utf-8'))
 if not any((i['asset_id'],i['version'])in replacement for i in pl['instances'])and rid not in corrections and rid!='PAN-037':continue
 p.s.reset();changes=[];direction_changes=[];ladder_ms=None;other_solids=[]
 for i in pl['instances']:
  before=(i['asset_id'],i['version'])
  if before in replacement:
   after=replacement[before];i['asset_id'],i['version']=after;changes.append(dict(instance_id=i['instance_id'],old_asset_ref=dict(asset_id=before[0],version=before[1]),asset_ref=dict(asset_id=after[0],version=after[1])))
  if rid=='PAN-037'and before==ladder_old:
   i['asset_id'],i['version']=ladder_ref;i['position_blender_m'][2]=.296
  correction=corrections.get(rid,{}).get(i['instance_id'])
  if correction:
   old_rotation=i.get('rotation_euler_blender_deg',[0,0,math.degrees(i.get('rotation_z_rad',0))]);new_rotation=correction['rotation_euler_blender_deg']
   assert len(new_rotation)==3 and all(math.isfinite(a)for a in new_rotation)
   i['rotation_euler_blender_deg']=new_rotation;i['rotation_z_rad']=math.radians(new_rotation[2])
   direction_changes.append(dict(instance_id=i['instance_id'],old_rotation_euler_blender_deg=old_rotation,rotation_euler_blender_deg=new_rotation,reason=correction['reason']))
  _,ms=p.attach(i,rid=='PAN-001')
  if rid=='PAN-037':
   if (i['asset_id'],i['version'])==ladder_ref:ladder_ms=ms
   elif i['asset_id']not in ['AST-001','AST-002','AST-3180']:other_solids.append((i['instance_id'],p.bounds(ms)))
 assert len(direction_changes)==len(corrections.get(rid,{})),(rid,'Missing confirmed orientation instance')
 if rid=='PAN-037':
  assert ladder_ms;lb=p.bounds(ladder_ms);assert abs(lb[0][2]-.296)<.0001
  overlaps=[n for n,b in other_solids if p.overlap(lb,b,.005)];assert not overlaps,('A-frame support collision',overlaps)
  state['ladder_placement_check']=dict(room_id=rid,bounds_blender_world_m=dict(min=lb[0],max=lb[1]),ground_plane_m=.296,ground_contact_error_m=abs(lb[0][2]-.296),overlap_threshold_m=.005,overlaps=overlaps,compared_instances=[n for n,b in other_solids])
 props={}
 for i in pl['instances']:
  k=(i['asset_id'],i['version']);a=p.LOOKUP[k];tri=json.loads((R/a['inspection_path']).read_text('utf-8'))['scene_triangles']
  if k not in props:props[k]=dict(name=a['name'],asset_ref=dict(asset_id=k[0],version=k[1]),triangles_per_instance=tri,instance_count=0,total_triangles=0)
  props[k]['instance_count']+=1;props[k]['total_triangles']+=tri
 pl.update(change_reason='Actual v010 WebGL exposed paving lines beyond base; new fixed pattern geometry is bounded inside conservative 4.6 x 3.8m area. Confirmed local-axis orientation corrections are applied from the recorded recipe; remaining placements and game bindings preserved.',floor_pattern_repair=dict(build_id='workplaces-v011',changes=changes,unscaled_pattern_bounds_m=[[-2.3,-1.9],[2.3,1.9]]))
 if direction_changes:pl['orientation_repair']=dict(recipe_path=orientation_path.relative_to(R).as_posix(),changes=direction_changes)
 if rid=='PAN-037':pl['ladder_support_repair']=dict(component_repair=ladder_state,placement_check=state['ladder_placement_check'])
 v=next_version(aid);parent=p.LOOKUP[(aid,old)]
 entry,rep=p.save(aid,v,room['name'],'diorama',method=parent['generation_method'],props=list(props.values()),placements=pl,source_ref=dict(asset_id=aid,version=old))
 if rid=='PAN-001':assert {'AST-005-0','AST-009-0','AST-015-0'}<={o.name for o in p.meshes()}
 previous=max((a for a in assemblies['assemblies']if a['assembly_asset_ref']['asset_id']==aid),key=lambda a:a['revision']);asm=copy.deepcopy(previous)
 asm.update(revision=previous['revision']+1,recorded_at=p.now(),assembly_asset_ref=dict(asset_id=aid,version=v),placements_path=f'meshy/models/blender/{aid}/{v}/placements.json',inspection_path=entry['inspection_path'],component_counts=rep['props'],change_reason=pl['change_reason'])
 assemblies['assemblies'].append(asm);p.write(p.CAT/'scene-assemblies.json',assemblies)
 room.update(assetVersion=v,sourceFbxPath=f'meshy/models/blender/{aid}/{v}/exports/room.fbx',scenePath=f'Assets/Scenes/Workplaces/{rid}-detail-v011.unity',triangles=rep['scene_triangles'],instances=len(pl['instances']))
 state['rooms'].append(dict(room_id=rid,asset_ref=dict(asset_id=aid,version=v),source_fbx_path=room['sourceFbxPath'],scene_path=room['scenePath'],triangles=rep['scene_triangles'],instances=len(pl['instances']),art_direction=pl['art_direction'],pattern_changes=changes,orientation_changes=direction_changes))
 p.write(CHECKPOINT,state)

latest={r['room_id']:r for r in state['rooms']}
for row in data['rooms']:
 if row['room_id']in latest:
  r=latest[row['room_id']];row.update(asset_ref=r['asset_ref'],triangles=r['triangles'],instances=r['instances'],art_direction=r['art_direction'])
data['floor_pattern_repair_rooms']=sorted(latest)
data['floor_pattern_repair_evidence_path']='docs/machine/evidence/spatial-diversity-v001/floor-pattern-repair.json'
data['created']=[dict(asset_id=a['asset_id'],version=a['version'])for a in p.CATALOG['assets']if a.get('produced_by_task')=='spatial-diversity-v001']
keys=set()
for r in reg['rooms']:
 keys.add((r['assetId'],r['assetVersion']));pl=json.loads((R/f'meshy/models/blender/{r["assetId"]}/{r["assetVersion"]}/placements.json').read_text('utf-8'));keys.update((i['asset_id'],i['version'])for i in pl['instances'])
reg['assets']=[dict(assetId=k[0],version=k[1],name=p.LOOKUP[k]['name'])for k in sorted(keys)];reg['buildId']='workplaces-v011'
p.write(REG,reg);p.write(EV/'production.json',data);p.write(p.CAT/'assets.json',p.CATALOG)
evidence=dict(schema_version=3,build_id='workplaces-v011',checked_at=p.now(),status='actual_blender_glb_reimport_pass_runtime_unverified',source_build_id='workplaces-v010',cause='Actual WebGL paving seam endpoints extended beyond floor base; three confirmed orientations and unsupported ladder also repaired.',pattern_repairs=state['patterns'],repaired_rooms=state['rooms'],orientation_recipe_path=orientation_path.relative_to(R).as_posix(),ladder_repair=ladder_state,ladder_placement_check=state.get('ladder_placement_check'),preserved_pattern_styles=['path','court','hazard','lotus'],source_audit_v010_path='docs/machine/evidence/spatial-diversity-v001/source-audit-v010.json',runtime_status='unverified',additional_paid_calls=0)
p.write(EV/'floor-pattern-repair.json',evidence)
print('FLOOR_PATTERN_REPAIRED',len(state['patterns']),len(state['rooms']),flush=True)

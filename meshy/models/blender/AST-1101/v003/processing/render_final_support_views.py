"""Final GLB presentation renders and actual-vertex support evidence.
A reusable model postprocessing artifact; no hooks, checks in app flows or model rewrites.
"""
import bpy,json,math,datetime,copy
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[6]
E=ROOT/'docs/machine/evidence/workplaces-model-review-v001'
assets=json.loads((ROOT/'docs/machine/catalog/assets.json').read_text('utf8'))['assets'];lookup={(a['asset_id'],a['version']):a for a in assets}
progress=json.loads((ROOT/'docs/machine/catalog/workplace-production-v001.json').read_text('utf8'))
baseline=json.loads((E/'systematic-support-bounds.json').read_text('utf8'))
prior_reports=[json.loads((E/n).read_text('utf8')) for n in ['comprehensive-support-production.json','final-contact-production.json','floor-and-stylus-production.json']]
changed_ids={x['asset_ref']['asset_id'] for report in prior_reports for x in report['prop_replacements']}
props=[max((a for a in assets if a['asset_id']==aid),key=lambda a:a['version']) for aid in sorted(changed_ids)]
rooms=[lookup[(x['assembly_asset_ref']['asset_id'],x['assembly_asset_ref']['version'])] for x in progress['scenes']]
# Render exactly the final references; existing immutable evidence is reused.
render=ROOT/'meshy/models/blender/AST-2002/v001/processing/render_review_views.py'
source=render.read_text('utf8');exec(compile(source[:source.index('for asset in TARGETS:')],str(render),'exec'))
for asset in props+rooms:produce(asset)

def bounds(obs):
 pts=[o.matrix_world@v.co for o in obs for v in o.data.vertices]
 return dict(min=[min(p[k] for p in pts) for k in range(3)],max=[max(p[k] for p in pts) for k in range(3)])
def part(o):return dict(name=o.name,triangles=sum(len(p.vertices)-2 for p in o.data.polygons),**bounds([o]))
result=dict(schema_version=3,environment='Actual Blender final GLB reimport, transformed mesh vertices (not object-box corners)',measured_at=datetime.datetime.now().astimezone().isoformat(),rooms=[],prop_models=[],special_contacts=[])
for a in props:
 bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=str(ROOT/a['runtime_path']));bpy.context.view_layer.update();obs=[o for o in bpy.context.scene.objects if o.type=='MESH']
 result['prop_models'].append(dict(asset_ref=dict(asset_id=a['asset_id'],version=a['version']),parts=[part(o) for o in obs]))
 # Real inventory from the final export, avoiding inherited old part lists.
 inspection_path=ROOT/a['inspection_path'];inspection=json.loads(inspection_path.read_text('utf8'));mapping=json.loads((ROOT/'meshy/models/textures/palettes/v001/mapping.json').read_text('utf8'))['cells'];regions=[]
 for o in obs:
  cells=[]
  for cell in mapping:
   u,v=cell['uv_center']
   if any(abs(loop.uv.x-u)<1e-5 and abs(loop.uv.y-v)<1e-5 for loop in o.data.uv_layers.active.data):cells.append(copy.deepcopy(cell))
  regions.append(dict(name=o.name,triangles=sum(len(p.vertices)-2 for p in o.data.polygons),palette_regions=cells,source='Actual final GLB parts and UV loops'))
 inspection['part_regions']=regions;inspection['checks']['parts_inventory']=dict(status='pass',evidence='Actual final GLB mesh parts, UV loops and current palette cells',reason=None);inspection_path.write_text(json.dumps(inspection,ensure_ascii=False,indent=2)+'\n','utf8')
for row in progress['scenes']:
 ref=row['assembly_asset_ref'];a=lookup[(ref['asset_id'],ref['version'])];data=json.loads(((ROOT/a['blender_path']).parent/'placements.json').read_text('utf8'))
 bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=str(ROOT/a['runtime_path']));bpy.context.view_layer.update();items=[]
 for inst in data['instances']:
  root=bpy.data.objects.get(inst['instance_id']);assert root is not None,inst['instance_id'];obs=[root] if root.type=='MESH' else [o for o in root.children_recursive if o.type=='MESH'];assert obs
  items.append(dict(**copy.deepcopy(inst),bounds=bounds(obs),parts=[part(o) for o in obs]))
 number=int(row['prompt_ref']['prompt_id'].split('-')[1])
 if number==64:
  n=Vector((0,-math.sin(math.radians(12)),math.cos(math.radians(12))))
  pulpit=next(i for i in items if i.get('candidate_id')=='CND-244');book=next(i for i in items if i.get('candidate_id')=='CND-245')
  topobs=[o for o in bpy.data.objects[pulpit['instance_id']].children_recursive if o.type=='MESH' and o.name.startswith('Reading top')];bookobs=[o for o in bpy.data.objects[book['instance_id']].children_recursive if o.type=='MESH'];top=max(n.dot(o.matrix_world@v.co) for o in topobs for v in o.data.vertices);low=min(n.dot(o.matrix_world@v.co) for o in bookobs for v in o.data.vertices)
  result['special_contacts'].append(dict(prompt_id='PRM-064',contact='Book lower surface to inclined pulpit top, common 12 degree normal',normal_gap_m=low-top))
 result['rooms'].append(dict(prompt_ref=row['prompt_ref'],name=row['name'],asset_ref=ref,instances=items));print('FINAL_VERTEX_ROOM',number,flush=True)
(E/'support-verification-v003.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n','utf8')
print('FINAL_VERTEX_EVIDENCE_COMPLETE',len(props),len(result['rooms']),flush=True)

"""Align PAN-001 components; keep object transforms editable and previous versions intact."""
import bpy,json,math
from pathlib import Path
from mathutils import Matrix,Vector
R=Path(__file__).resolve().parents[6]
previous=R/'meshy/models/blender/AST-020/v001'
# Reuse material, palette, rendering and GLB inspection functions without rebuilding props.
exec((previous/'processing/build_office.py').read_text('utf-8').split('BUILD=[')[0])
out=R/'meshy/models/blender/AST-020/v003';src=R/'meshy/models/original/AST-020/v003'
assert not (out/'model.blend').exists()
(out/'exports').mkdir(parents=True,exist_ok=True);(src/'previews').mkdir(parents=True,exist_ok=True)
data=json.loads((previous/'placements.json').read_text('utf-8'));catalog=json.loads((R/'docs/machine/catalog/assets.json').read_text('utf-8'));lookup={(a['asset_id'],a['version']):a for a in catalog['assets']}
reset();M=mat();changes=[];objects=[]
for inst in data['instances']:
 a=inst['asset_id'];idx=int(inst['instance_id'].split('-')[-1]);p=inst['position_blender_m'][:];deg=0
 x=[-.88,.88][min(idx,1)]
 if a=='AST-002':p=[0,-.38,.288]
 elif a=='AST-004':p=[x,0,.296]
 elif a=='AST-003':p=[x,-.86,.296];deg=180
 elif a=='AST-005':p=[x,.12,1.091]
 elif a=='AST-006':p=[x,-.20,1.091]
 elif a=='AST-007':p=[x+.33,-.20,1.091]
 elif a=='AST-008':p=[-1.43 if idx==0 else 1.43,.03,.296]
 elif a=='AST-011':p=[x-.57,.10,1.091] if idx<2 else [.23,1.60,1.288]
 elif a=='AST-012':p=[x+.56,-.07,1.091]
 elif a=='AST-014':p=[x+.60,.22,1.091]
 elif a=='AST-013':p=[x,.32,1.056]
 elif a=='AST-009':p=[-2.18,.60,.233]
 elif a=='AST-015':p=[.65,1.60,.288]
 elif a=='AST-016':p=[2.10,1.60,.288];deg=30
 elif a=='AST-017':p=[2.10,1.39,1.048]
 elif a=='AST-010':p=[[0,.06,1.091],[1.00,1.60,1.288],[2.12,-1.15,.296]][idx]
 old=dict(position=inst['position_blender_m'],rotation_z_deg=math.degrees(inst['rotation_z_rad']))
 inst['position_blender_m']=[round(v,4) for v in p];inst['rotation_z_rad']=math.radians(deg);inst['rotation_euler_blender_deg']=[0,0,deg]
 changes.append(dict(instance_id=inst['instance_id'],before=old,after=dict(position=p,rotation_z_deg=deg)))
 before=set(bpy.context.scene.objects);bpy.ops.import_scene.gltf(filepath=str(R/lookup[(a,inst['version'])]['runtime_path']));bpy.context.view_layer.update()
 obs=[o for o in bpy.context.scene.objects if o not in before and o.type=='MESH']
 for o in obs:
  # Bake import coordinate conversion only. Placement remains a real Blender transform.
  world=o.matrix_world.copy();o.data=o.data.copy();o.data.transform(world);o.parent=None;o.matrix_world=Matrix.Identity(4)
  o.rotation_mode='XYZ';o.location=p;o.rotation_euler=(0,0,math.radians(deg));o.scale=inst['scale'];o.name=inst['instance_id'];o['asset_id']=a;o['asset_version']=inst['version'];o['instance_id']=inst['instance_id'];o.data.materials.clear();o.data.materials.append(M)
  for poly in o.data.polygons:poly.material_index=0
  objects.append(o)
bpy.ops.object.select_all(action='DESELECT')
for o in objects:o.select_set(True)
bpy.context.view_layer.objects.active=objects[0];bpy.context.view_layer.update()
# Editable assembly is intentionally not joined: each instance has meaningful position/rotation.
bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'));bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
bpy.ops.export_scene.gltf(filepath=str(out/'exports/model.glb'),export_format='GLB',use_selection=True)
props=json.loads((previous/'inspection.json').read_text('utf-8'))['props'];rep=check('AST-020','v003','diorama',props);assert rep['scene_triangles']==4308
data['alignment_rules']=['Workstation centers X = -0.88,+0.88m','Chair forward +Y toward monitor; chair Z rotation 180deg','Monitor/keyboard/chair centerline aligned','Tabletop support plane Z=1.091m','Desk lamps kept inside tabletop Y range','Drawer cabinets positioned at outer sides','No per-instance geometry/color changes']
(out/'placements.json').write_text(json.dumps(data,ensure_ascii=False,indent=2),'utf-8');(out/'transform-changes.json').write_text(json.dumps(dict(schema_version=3,coordinate_system='Blender Z-up meters, Euler XYZ degrees',changes=changes),ensure_ascii=False,indent=2),'utf-8')
render(src/'previews/front.png',6,(0,0,.7))
(src/'README.md').write_text('# PAN-001 alignment v003\nBlender assembly adjustment, 2026-10-31. Existing props reused unchanged. Meshy calls/credits 0. No task ID. Source asset rights unchanged.\nEditable per-instance transforms preserved in model.blend; placements.json and transform-changes.json record Blender Z-up positions and rotations. Reuses v001 production helper functions and palette v001.\n','utf-8')
entry=dict(lookup[('AST-020','v001')]);entry.update(version='v003',name='PAN-001 일반 사무실 — 위치·회전 정렬',source_path='meshy/models/original/AST-020/v003/source.blend',blender_path='meshy/models/blender/AST-020/v003/model.blend',runtime_path='meshy/models/blender/AST-020/v003/exports/model.glb',preview_path='meshy/models/original/AST-020/v003/previews/front.png',inspection_path='meshy/models/blender/AST-020/v003/inspection.json',production_record_path='meshy/models/original/AST-020/v003/README.md',processing_paths=['meshy/models/blender/AST-020/v003/processing/align_office.py','meshy/models/blender/AST-020/v001/processing/build_office.py'],generation_reason='Reuse all props; align positions, functional facing and editable instance transforms.')
p=R/'docs/machine/catalog/assets.json';cat=json.loads(p.read_text('utf-8'));assert not any(a['asset_id']=='AST-020' and a['version']=='v003' for a in cat['assets']);cat['assets'].append(entry);p.write_text(json.dumps(cat,ensure_ascii=False,indent=2),'utf-8')
print('ALIGNED',rep['scene_triangles'],rep['glb_bytes'],flush=True)

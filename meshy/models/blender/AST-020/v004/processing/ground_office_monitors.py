"""Preserve office v003, ground both unchanged monitor meshes in v004.

Retains all 30 stable instance/mesh names, counts, palette and other transforms.
"""
import bpy,json,copy,datetime,hashlib,importlib.util
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[6]
SCRIPT=Path(__file__).relative_to(ROOT).as_posix()
SUPPORT='meshy/models/blender/AST-1010/v001/processing/build_shared.py'
spec=importlib.util.spec_from_file_location('shared',ROOT/SUPPORT);s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
old=ROOT/'meshy/models/blender/AST-020/v003';out=ROOT/'meshy/models/blender/AST-020/v004';src=ROOT/'meshy/models/original/AST-020/v004'
assert not (out/'model.blend').exists(),'Existing version preserved'
before_hash=hashlib.sha256((old/'model.blend').read_bytes()).hexdigest()
placements=json.loads((old/'placements.json').read_text('utf-8'));report=json.loads((old/'inspection.json').read_text('utf-8'))
bpy.ops.wm.open_mainfile(filepath=str(old/'model.blend'))
meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
assert len(meshes)==30
changes=[]
for inst in placements['instances']:
    if inst['asset_id']!='AST-005':continue
    obj=next(o for o in meshes if o.name==inst['instance_id'])
    old_z=obj.location.z;obj.location.z-=.0425;inst['position_blender_m'][2]-=.0425
    changes.append(dict(instance_id=obj.name,position_z_before=old_z,position_z_after=obj.location.z,reason='Source monitor foot bottom is .0425m above source origin; align foot with unchanged desk support plane z=1.091m.'))
assert len(changes)==2
(out/'exports').mkdir(parents=True,exist_ok=True);(src/'previews').mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action='DESELECT')
for obj in meshes:obj.select_set(True)
bpy.context.view_layer.objects.active=meshes[0]
bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'));bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
glb=out/'exports/model.glb'
bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
bpy.ops.export_scene.fbx(filepath=str(out/'exports/office.fbx'),use_selection=True,object_types={'MESH'},axis_forward='-Z',axis_up='Y',apply_unit_scale=True,bake_anim=False,path_mode='STRIP',use_mesh_modifiers=True)
placements['supersedes_asset_ref']={'asset_id':'AST-020','version':'v003'}
placements['alignment_rules']=placements.get('alignment_rules',[])+['v004: AST-005-0 and AST-005-1 translated z=-.0425m only; both feet contact existing desk tops.']
s.write(out/'placements.json',placements);s.write(out/'transform-changes.json',dict(schema_version=3,changes=changes))
bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=str(glb))
meshes=[o for o in bpy.context.scene.objects if o.type=='MESH'];triangles=sum(len(poly.vertices)-2 for o in meshes for poly in o.data.polygons)
assert len(meshes)==30 and triangles==4308
assert sorted(o.name for o in meshes)==sorted(i['instance_id'] for i in placements['instances'])
materials={m for o in meshes for m in o.data.materials};images={n.image for m in materials for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image}
centers=[c['uv_center'] for c in s.MAPPING['cells']]
uvok=all(o.data.uv_layers.active and all(any(abs(l.uv.x-u)<1e-5 and abs(l.uv.y-v)<1e-5 for u,v in centers) for l in o.data.uv_layers.active.data) for o in meshes)
contacts=[]
for o in meshes:
    if not o.name.startswith('AST-005-'):continue
    minimum=min((o.matrix_world@Vector(c)).z for c in o.bound_box)
    contacts.append(dict(instance_id=o.name,foot_bottom_z_m=minimum,support_plane_z_m=1.091,gap_m=minimum-1.091))
assert all(abs(c['gap_m'])<.00001 for c in contacts)
ck=lambda value,why:dict(status='pass' if value else 'fail',evidence=why,reason=None)
unverified=lambda why:dict(status='unverified',evidence=None,reason=why)
report.update(version='v004',scene_triangles=triangles,material_count=len(materials),texture_count=len(images),glb_bytes=glb.stat().st_size,target_web_environment='Unity WebGL new office scene, execution pending',checks=dict(scene_budget=ck(triangles<=5000,'Final GLB reopened in actual Blender; 30 instances, 4308 triangles'),palette_uv=ck(uvok,'Final GLB loop UV matches fixed palette mapping'),shared_material=ck(len(materials)==len(images)==1,'Final GLB materials and texture nodes'),monitor_support=ck(all(abs(c['gap_m'])<.00001 for c in contacts),'Actual final-GLB world bounds compared with unchanged support plane 1.091m'),visual_front_side_back=unverified('New version final views pending'),web_display=unverified('New Unity/WebGL execution pending')),remaining_issues=['Original v003 other transforms and dimensions intentionally preserved; new visual/runtime checks required.'],monitor_support_contacts=contacts)
s.write(out/'inspection.json',report);s.render_preview(src/'previews/front.png')
now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat()
catalog=s.read('assets');base=next(a for a in catalog['assets'] if a['asset_id']=='AST-020' and a['version']=='v003');entry=copy.deepcopy(base)
rel=lambda p:p.relative_to(ROOT).as_posix()
entry.update(version='v004',name='PAN-001 일반 사무실 — 모니터 받침 정렬',source_path=rel(src/'source.blend'),blender_path=rel(out/'model.blend'),runtime_path=rel(glb),preview_path=rel(src/'previews/front.png'),unity_path=None,unity_palette_path=None,inspection_path=rel(out/'inspection.json'),processing_paths=[SCRIPT,SUPPORT]+base['processing_paths'],production_record_path=rel(src/'README.md'),generation_reason='Reuse exact v003 office model; move unchanged monitor instances down by .0425m so their feet touch desk surfaces.',status='in_progress')
entry.pop('unity_application',None);catalog['assets'].append(entry);s.write(ROOT/'docs/machine/catalog/assets.json',catalog)
assemblies=s.read('scene-assemblies');previous=[a for a in assemblies['assemblies'] if a['assembly_id']=='pan-001-office'];last=max(previous,key=lambda a:a['revision']);assembly=copy.deepcopy(last)
assembly.update(revision=last['revision']+1,recorded_at=now,assembly_asset_ref={'asset_id':'AST-020','version':'v004'},placements_path=rel(out/'placements.json'),inspection_path=rel(out/'inspection.json'),aggregation_basis='Original 30 component mesh instances counted once; assembly parent excluded.',change_reason='Ground existing two monitor feet; v003 and earlier files preserved.')
assemblies['assemblies'].append(assembly);s.write(ROOT/'docs/machine/catalog/scene-assemblies.json',assemblies)
progress=s.read('workplace-production-v001')
for row in progress['scenes']:
    if row['prompt_ref']['prompt_id']=='PRM-001':
        row.update(production_status='assembled_runtime_unverified',assembly_asset_ref={'asset_id':'AST-020','version':'v004'},evidence_paths=[rel(out/'inspection.json'),rel(out/'placements.json')]);row['checks']['final_glb']='pass'
progress['updated_at']=now;s.write(ROOT/'docs/machine/catalog/workplace-production-v001.json',progress)
(src/'README.md').write_text('# PAN-001 office v004 — monitor support alignment\n\n2026-10-31. Blender direct assembly repair, Meshy/image calls 0, credits 0. Preserves v003 and all individual prop files. Only AST-005-0/1 move down .0425m. Both feet contact original desks at Blender Z=1.091m. All 30 stable mesh instance names retained, final reimport 4308 triangles.\n\nScript: '+SCRIPT+'. Reused original v003 editable .blend, placements, palette v001 and exact component geometries. GLB/FBX are new version derivatives. Runtime WebGL and full visual checks pending; status in_progress. No independent rights verification.\n','utf-8')
assert hashlib.sha256((old/'model.blend').read_bytes()).hexdigest()==before_hash
print('OFFICE_REPAIRED',triangles,len(meshes),contacts,flush=True)

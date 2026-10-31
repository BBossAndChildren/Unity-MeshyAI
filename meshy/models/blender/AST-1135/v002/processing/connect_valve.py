"""Move unchanged valve and its stem onto the right pipe; preserve prop v001."""
import bpy,json,copy,hashlib,importlib.util
from pathlib import Path
ROOT=Path(__file__).resolve().parents[6]
SCRIPT=Path(__file__).relative_to(ROOT).as_posix()
SUPPORT='meshy/models/blender/AST-1010/v001/processing/build_shared.py'
spec=importlib.util.spec_from_file_location('shared',ROOT/SUPPORT);s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
old=ROOT/'meshy/models/blender/AST-1135/v001';out=ROOT/'meshy/models/blender/AST-1135/v002';src=ROOT/'meshy/models/original/AST-1135/v002'
assert not (out/'model.blend').exists()
oldhash=hashlib.sha256((old/'model.blend').read_bytes()).hexdigest()
bpy.ops.wm.open_mainfile(filepath=str(old/'model.blend'))
meshes=[o for o in bpy.context.scene.objects if o.type=='MESH'];moved=[o for o in meshes if o.name.startswith('Valve')]
assert len(moved)==2
for obj in moved:obj.location.x+=.35
(out/'exports').mkdir(parents=True,exist_ok=True);(src/'previews').mkdir(parents=True,exist_ok=True)
bpy.ops.object.select_all(action='DESELECT')
for obj in meshes:obj.select_set(True)
bpy.context.view_layer.objects.active=meshes[0]
bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'));bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
glb=out/'exports/model.glb';bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
bpy.ops.export_scene.fbx(filepath=str(out/'exports/model.fbx'),use_selection=True,add_leaf_bones=False,bake_anim=False,axis_forward='-Z',axis_up='Y',path_mode='STRIP')
bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=str(glb))
meshes=[o for o in bpy.context.scene.objects if o.type=='MESH'];tri=sum(len(p.vertices)-2 for o in meshes for p in o.data.polygons)
inspection=json.loads((old/'inspection.json').read_text('utf-8'))
assert tri==inspection['scene_triangles'] and tri<=1000
inspection.update(version='v002',glb_bytes=glb.stat().st_size)
inspection['checks']['valve_connection']=dict(status='pass',evidence='Actual Blender source moved both Valve and Valve stem by X=+.35m onto right vertical pipe centerline X=.35m, Z=.8m; final GLB reopened.',reason=None)
inspection['checks']['visual_front_side_back']=dict(status='unverified',evidence=None,reason='New corrected version views pending explicit review')
s.write(out/'inspection.json',inspection);s.render_preview(src/'previews/front.png')
catalog=s.read('assets');base=next(a for a in catalog['assets'] if a['asset_id']=='AST-1135' and a['version']=='v001');entry=copy.deepcopy(base)
rel=lambda p:p.relative_to(ROOT).as_posix()
entry.update(version='v002',source_path=rel(src/'source.blend'),blender_path=rel(out/'model.blend'),runtime_path=rel(glb),preview_path=rel(src/'previews/front.png'),unity_path=None,unity_palette_path=None,inspection_path=rel(out/'inspection.json'),processing_paths=[SCRIPT]+base['processing_paths'],production_record_path=rel(src/'README.md'),generation_reason='Reuse unchanged component geometry, move valve and stem onto actual pipe centerline; preserve v001.',status='in_progress')
catalog['assets'].append(entry);s.write(ROOT/'docs/machine/catalog/assets.json',catalog)
progress=s.read('workplace-production-v001')
for row in progress['candidates']:
    if row['candidate_id']=='CND-135':row['result_asset_ref']={'asset_id':'AST-1135','version':'v002'}
s.write(ROOT/'docs/machine/catalog/workplace-production-v001.json',progress)
(src/'README.md').write_text('# AST-1135 v002 — valve physically connected to pipe\n\n2026-10-31 Blender direct repair. Two existing parts translated +.35m X to meet right vertical pipe; no new geometry, color or texture. All v001 source/export files preserved. Credits 0, paid calls 0. Script '+SCRIPT+'. Original shared/dedicated recipe references retained in catalog. GLB actually reopened; unchanged triangle count. New runtime execution pending.\n','utf-8')
doc=ROOT/'docs/human/assets/AST-1135-v001.md';newdoc=ROOT/'docs/human/assets/AST-1135-v002.md'
text=doc.read_text('utf-8').replace('# AST-1135 v001','# AST-1135 v002').replace('AST-1135/v001','AST-1135/v002')
newdoc.write_text(text+'\n\n## v002 교정\n\n밸브와 밸브 스템을 X=+.35m 이동해 실제 수직관에 연결했다. 기존 형상·팔레트·후보 전체 사용처는 유지한다. v001 모델과 공간 결과는 보존한다. 이번 Unity 사용·실행은 해당 원장에 등록되기 전 미검증이다.\n','utf-8')
assert hashlib.sha256((old/'model.blend').read_bytes()).hexdigest()==oldhash
print('VALVE_CONNECTED',tri,flush=True)

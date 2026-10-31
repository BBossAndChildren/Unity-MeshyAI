import bpy, json, hashlib
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parents[6]
P=R/'unity/projects/OfficeAssistant-v001'
E=R/'docs/machine/evidence/office-assistant-v001'
E.mkdir(parents=True,exist_ok=True)
out=P/'Assets/Meshy/AST-020/v003'
out.mkdir(parents=True,exist_ok=True)
assert not (out/'office.fbx').exists(), 'Existing Unity derivative is preserved; choose a new output before exporting again.'
source=R/'meshy/models/blender/AST-020/v003/exports/model.glb'
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(source))
bpy.context.view_layer.update()
objects=[]
for o in bpy.context.scene.objects:
 if o.type!='MESH': continue
 o.data.calc_loop_triangles()
 corners=[o.matrix_world@Vector(c) for c in o.bound_box]
 objects.append(dict(name=o.name,parent=o.parent.name if o.parent else None,triangles=len(o.data.loop_triangles),position_blender_m=list(o.location),bounds_blender_min=[min(v[i] for v in corners) for i in range(3)],bounds_blender_max=[max(v[i] for v in corners) for i in range(3)]))
report=dict(schema_version=3,source_path=str(source.relative_to(R)).replace('\\','/'),source_sha256=hashlib.sha256(source.read_bytes()).hexdigest(),environment=bpy.app.version_string,method='Actual Blender import of final GLB; all mesh instances counted once, assembly parent excluded',objects=objects,scene_triangles=sum(o['triangles'] for o in objects),material_count=len(bpy.data.materials),images=[dict(name=i.name,size=list(i.size)) for i in bpy.data.images])
(E/'blender-reimport.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),'utf-8')
assert report['scene_triangles']<=5000
# FBX is a Unity import derivative; source GLB/blend and geometry remain untouched.
bpy.ops.export_scene.fbx(filepath=str(out/'office.fbx'),use_selection=False,object_types={'MESH'},axis_forward='-Z',axis_up='Y',apply_unit_scale=True,bake_anim=False,path_mode='STRIP',use_mesh_modifiers=True)
print('OFFICE_EXPORT',report['scene_triangles'],len(objects),flush=True)

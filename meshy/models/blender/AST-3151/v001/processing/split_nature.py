"""One Meshy scene -> connected components -> reusable individual props.
Source is never overwritten. Inspect the component sheet before final grouping.
"""
import bpy,json,math,importlib.util
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[6]
spec=importlib.util.spec_from_file_location('enrich',ROOT/'meshy/models/blender/AST-2064/v003/processing/enrich_worship.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
s=e.s
OUT=ROOT/'docs/machine/evidence/nature-kit-v001';OUT.mkdir(parents=True,exist_ok=True)
s.reset();bpy.ops.import_scene.gltf(filepath=str(OUT/'clustered-source.glb'))
obs=e.meshes();bpy.ops.object.select_all(action='DESELECT')
for o in obs:o.select_set(True)
bpy.context.view_layer.objects.active=obs[0];bpy.ops.object.join();o=bpy.context.object;bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
source_tri=e.triangles([o]);print('SOURCE_TRIANGLES',source_tri,flush=True)
mod=o.modifiers.new('Unify nearby original surfaces','REMESH');mod.mode='VOXEL';mod.voxel_size=.024;mod.use_smooth_shade=True;bpy.ops.object.modifier_apply(modifier=mod.name)
bpy.ops.object.mode_set(mode='EDIT');bpy.ops.mesh.select_all(action='SELECT');bpy.ops.mesh.separate(type='LOOSE');bpy.ops.object.mode_set(mode='OBJECT')
components=[]
for idx,o in enumerate(e.meshes()):
    if len(o.data.polygons)<20:bpy.data.objects.remove(o,do_unlink=True);continue
    o.name=f'Kit component {len(components):02}';lo,hi=e.bounds([o]);s.paint(o,'cream')
    components.append(dict(name=o.name,faces=len(o.data.polygons),bounds_min=lo,bounds_max=hi,center=[(lo[k]+hi[k])/2 for k in range(3)]))
s.write(OUT/'components.json',dict(schema_version=3,source_task_id='01a1903b-862f-704e-8b44-ffc3db8279c6',source_triangles=source_tri,components=components,consumed_credits=20))
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'separated-source.blend'))
# Final preview supplied by actual per-prop/Unity review; avoid costly source render.
print('SEPARATED_COMPONENTS',len(components),flush=True)

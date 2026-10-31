"""Four source sets, one Meshy task; preserve source and split in Blender."""
import bpy,json,importlib.util
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parents[6];spec=importlib.util.spec_from_file_location('prod',R/'meshy/models/blender/AST-3101/v001/processing/build_spatial_details.py');p=importlib.util.module_from_spec(spec);spec.loader.exec_module(p);p.SCRIPT=Path(__file__).relative_to(R).as_posix()
groups=[(3161,'잎이 넓은 작은 나무',[1,2],1.6),(3162,'둥근 수관 나무',[4],1.2),(3163,'둥근 강돌 무리',[0],.28),(3164,'넓은 잎 풀 포기',[3],.32)];out=R/'docs/machine/evidence/nature-kit-v001';rows=[]
for aid,name,ids,height in groups:
 bpy.ops.wm.open_mainfile(filepath=str(out/'separated-source.blend'));keep={f'Kit component {i:02}'for i in ids}
 for o in list(bpy.context.scene.objects):
  if o.type!='MESH'or o.name not in keep:bpy.data.objects.remove(o,do_unlink=True)
 obs=p.meshes();p.s.MATERIAL=obs[0].data.materials[0];lo,hi=p.bounds(obs);base=Vector(((lo[0]+hi[0])/2,(lo[1]+hi[1])/2,lo[2]));scale=height/(hi[2]-lo[2])
 bpy.ops.object.select_all(action='DESELECT')
 for o in obs:
  bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.transform_apply(location=True,rotation=True,scale=True);o.select_set(False)
  for v in o.data.vertices:v.co=(v.co-base)*scale
 for o in obs:o.select_set(True)
 bpy.context.view_layer.objects.active=obs[0];bpy.ops.object.join();o=bpy.context.object;o.name=name
 mod=o.modifiers.new('Web silhouette budget','DECIMATE');mod.ratio=450/max(1,p.tris([o]));bpy.ops.object.modifier_apply(modifier=mod.name);mod=o.modifiers.new('Final triangles','TRIANGULATE');bpy.ops.object.modifier_apply(modifier=mod.name);p.paint(o,'green');o.data.update()
 for face in o.data.polygons:
  color='walnut'if aid in[3161,3162]and face.center.z<height*.36 else 'steel'if aid==3163 else 'sage'
  if face.center.z<height*.035:color='walnut'
  uv=p.CELLS[p.COLORS[color]]['uv_center']
  for i in face.loop_indices:o.data.uv_layers.active.data[i].uv=uv
 if aid==3161:p.rod('Canopy trunk connection',(0,0,height*.30),(0,0,height*.65),.035,'walnut',6)
 entry,rep=p.save(f'AST-{aid}','v001',name,method='hybrid',credit=None);entry['source_pack_ref']={'pack_id':'nature-kit-001','version':'v001','source_path':'meshy/models/original/NATURE-KIT-001/v001/source.glb','task_id':'01a1903b-862f-704e-8b44-ffc3db8279c6','component_indices':ids,'batch_consumed_credits':20,'allocated_credits':None};entry['generation_reason']='Split inspected sets from one Meshy scene; original preserved, local silhouette reduction and original palette cells. Actual batch cost20, per-prop allocation unavailable.';p.LOOKUP[(entry['asset_id'],'v001')]=entry
 rows.append(dict(asset_ref={'asset_id':entry['asset_id'],'version':'v001'},name=name,triangles=rep['scene_triangles'],dimensions_m=rep['dimensions_m'],component_indices=ids))
p.write(p.CAT/'assets.json',p.CATALOG);p.write(out/'split-manifest.json',dict(schema_version=3,pack_id='nature-kit-001',version='v001',source_task_id='01a1903b-862f-704e-8b44-ffc3db8279c6',consumed_credits=20,allocated_credits=None,props=rows,source_preserved=True,visual_status='unverified',runtime_status='unverified'));print('NATURE_EXPORTED',len(rows),flush=True)

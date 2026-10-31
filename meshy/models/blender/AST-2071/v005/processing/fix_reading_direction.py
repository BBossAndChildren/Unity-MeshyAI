"""Apply the same measured reading-slope repair to the cathedral lectern."""
import bpy,json,math,copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[6]
spec=importlib.util.spec_from_file_location('e',R/'meshy/models/blender/AST-2064/v003/processing/enrich_worship.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e);s=e.s;e.SCRIPT=Path(__file__).relative_to(R).as_posix();e.render=lambda *a,**k:None
s.reset();e.import_asset('AST-1258','v002')
for o in e.meshes():
    if o.name.startswith('Reading top'):o.rotation_euler.x=math.radians(-12)
e.save('AST-1258','v003','독서대','prop','blender_direct')
pl=json.loads((R/'meshy/models/blender/AST-2071/v004/placements.json').read_text('utf-8'));s.reset();props={}
for i in pl['instances']:
    if i['asset_id']=='AST-1258':i['version']='v003'
    obs,a=e.import_asset(i['asset_id'],i['version']);root=bpy.data.objects.new(i['instance_id'],None);bpy.context.collection.objects.link(root)
    for o in obs:
        if o.parent is None:o.parent=root
    root.location=i['position_blender_m'];root.rotation_euler=[math.radians(v)for v in i['rotation_euler_blender_deg']];root.scale=i['scale'];bpy.context.view_layer.update()
    tri=e.triangles([o for o in obs if o.type=='MESH']);key=(i['asset_id'],i['version']);i['component_mesh_count']=len([o for o in obs if o.type=='MESH'])
    if key not in props:props[key]=dict(name=a['name'],asset_ref=dict(asset_id=key[0],version=key[1]),triangles_per_instance=tri,instance_count=0,total_triangles=0)
    props[key]['instance_count']+=1;props[key]['total_triangles']+=tri
entry,report=e.save('AST-2071','v005','천주교 성당 — 신부님','diorama','hybrid',0,props=list(props.values()),placements=pl)
assembly=s.read('scene-assemblies');row=copy.deepcopy(max([x for x in assembly['assemblies']if x['assembly_id']=='pan-071-workplace'],key=lambda x:x['revision']));row.update(revision=row['revision']+1,recorded_at=e.now(),assembly_asset_ref={'asset_id':'AST-2071','version':'v005'},placements_path='meshy/models/blender/AST-2071/v005/placements.json',inspection_path=entry['inspection_path'],component_counts=report['props'],change_reason='Lectern slope faces the reader standing behind the lectern, consistent with church reading-direction repair.');assembly['assemblies'].append(row);s.write(e.CAT/'scene-assemblies.json',assembly)
cat=s.read('assets')
for a in cat['assets']:
    if (a['asset_id'],a['version'])in[('AST-1258','v003'),('AST-2071','v005')]:a['preview_path']=None
s.write(e.CAT/'assets.json',cat)

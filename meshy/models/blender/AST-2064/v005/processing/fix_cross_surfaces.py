"""Replace coplanar crossing boxes with a single extruded cross silhouette."""
import bpy,bmesh,json,math,copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[6]
spec=importlib.util.spec_from_file_location('e',R/'meshy/models/blender/AST-2064/v003/processing/enrich_worship.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e);s=e.s
e.SCRIPT=Path(__file__).relative_to(R).as_posix();s.COLORS['walnut']=(12,8);s.COLORS['gold']=(4,12)
# Final corrected room is reviewed in the actual Unity WebGL build below.
# No nonexistent render path is left registered while that check is pending.
e.render=lambda *a,**k:None
def extruded_cross(name,width,shaft,bottom,top,bar_z,bar_height,front,back,color):
    a=shaft/2;w=width/2;l=bar_z-bar_height/2;h=bar_z+bar_height/2
    poly=[(-a,bottom),(a,bottom),(a,l),(w,l),(w,h),(a,h),(a,top),(-a,top),(-a,h),(-w,h),(-w,l),(-a,l)]
    verts=[(x,y,z) for y in [front,back] for x,z in poly];n=len(poly);faces=[tuple(range(n-1,-1,-1)),tuple(range(n,2*n))]+[(i,(i+1)%n,(i+1)%n+n,i+n) for i in range(n)]
    mesh=bpy.data.meshes.new(name);mesh.from_pydata(verts,[],faces);mesh.update();obj=bpy.data.objects.new(name,mesh);bpy.context.collection.objects.link(obj);s.paint(obj,color)
    bm=bmesh.new();bm.from_mesh(mesh);bmesh.ops.recalc_face_normals(bm,faces=bm.faces[:]);bm.to_mesh(mesh);bm.free()
s.reset();e.box('Stepped plinth',(0,0,.06),(.42,.36,.12),'walnut',.025)
extruded_cross('Single joined wooden cross',1.02,.155,.06,2.10,1.54,.155,-.0575,.0575,'walnut')
extruded_cross('Single joined inset cross',.92,.035,.115,2.045,1.54,.035,-.065,-.058,'gold')
a,report=e.save('AST-1246','v004','단순한 십자가','prop','blender_direct')
pl=json.loads((R/'meshy/models/blender/AST-2064/v004/placements.json').read_text('utf-8'));s.reset();props={}
for i in pl['instances']:
    if i['asset_id']=='AST-1246':i['version']='v004'
    obs,a=e.import_asset(i['asset_id'],i['version']);root=bpy.data.objects.new(i['instance_id'],None);bpy.context.collection.objects.link(root)
    for o in obs:
        if o.parent is None:o.parent=root
    root.location=i['position_blender_m'];root.rotation_euler=[math.radians(v) for v in i['rotation_euler_blender_deg']];root.scale=i['scale'];bpy.context.view_layer.update()
    tri=e.triangles([o for o in obs if o.type=='MESH']);key=(i['asset_id'],i['version']);i['component_mesh_count']=len([o for o in obs if o.type=='MESH'])
    if key not in props:props[key]=dict(name=a['name'],asset_ref=dict(asset_id=key[0],version=key[1]),triangles_per_instance=tri,instance_count=0,total_triangles=0)
    props[key]['instance_count']+=1;props[key]['total_triangles']+=tri
entry,report=e.save('AST-2064','v005','기독교(개신교) 예배실 — 목사','diorama','hybrid',0,props=list(props.values()),placements=pl)
assembly=s.read('scene-assemblies');row=copy.deepcopy(max([x for x in assembly['assemblies'] if x['assembly_id']=='pan-064-workplace'],key=lambda x:x['revision']));row.update(revision=row['revision']+1,recorded_at=e.now(),assembly_asset_ref={'asset_id':'AST-2064','version':'v005'},placements_path='meshy/models/blender/AST-2064/v005/placements.json',inspection_path=entry['inspection_path'],component_counts=report['props'],change_reason='Remove coplanar cross/gold intersections that produced dark depth-fighting artifacts; extrude a single cross silhouette.')
assembly['assemblies'].append(row);s.write(e.CAT/'scene-assemblies.json',assembly)
cat=s.read('assets')
for a in cat['assets']:
    if (a['asset_id'],a['version']) in [('AST-1246','v004'),('AST-2064','v005')]:a['preview_path']=None
s.write(e.CAT/'assets.json',cat)

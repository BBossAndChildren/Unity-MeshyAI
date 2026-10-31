"""Two counseling chairs face each other around the shared table, PAN-015."""
import bpy,json,math,copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[6];spec=importlib.util.spec_from_file_location('e',R/'meshy/models/blender/AST-2064/v003/processing/enrich_worship.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e);s=e.s;e.SCRIPT=Path(__file__).relative_to(R).as_posix();e.render=lambda *a,**k:None
registry=json.loads((R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json').read_text('utf-8'));room=next(x for x in registry['rooms']if x['roomId']=='PAN-015');old=room['assetVersion'];v='v'+str(int(old[1:])+1).zfill(3);pl=json.loads((R/f'meshy/models/blender/AST-2015/{old}/placements.json').read_text('utf-8'));s.reset();props={};repairs=[]
for i in pl['instances']:
    if i['asset_id']=='AST-1062':
        angle=75 if i['position_blender_m'][0]<0 else -75;repairs.append(dict(instance_id=i['instance_id'],old_angle=i['rotation_euler_blender_deg'][2],new_angle=angle));i['rotation_euler_blender_deg'][2]=angle;i['rotation_z_rad']=math.radians(angle)
    obs,a=e.import_asset(i['asset_id'],i['version']);root=bpy.data.objects.new(i['instance_id'],None);bpy.context.collection.objects.link(root)
    for o in obs:
        if o.parent is None:o.parent=root
    root.location=i['position_blender_m'];root.rotation_euler=[math.radians(v)for v in i['rotation_euler_blender_deg']];root.scale=i['scale'];bpy.context.view_layer.update();tri=e.triangles([o for o in obs if o.type=='MESH']);key=(i['asset_id'],i['version'])
    if key not in props:props[key]=dict(name=a['name'],asset_ref=dict(asset_id=key[0],version=key[1]),triangles_per_instance=tri,instance_count=0,total_triangles=0)
    props[key]['instance_count']+=1;props[key]['total_triangles']+=tri
entry,report=e.save('AST-2015',v,room['name'],'diorama','blender_direct',0,props=list(props.values()),placements=pl);cat=s.read('assets');cat['assets'][-1]['preview_path']=None;s.write(e.CAT/'assets.json',cat)
assembly=s.read('scene-assemblies');row=copy.deepcopy(max([x for x in assembly['assemblies']if x['assembly_id']=='pan-015-workplace'],key=lambda x:x['revision']));row.update(revision=row['revision']+1,recorded_at=e.now(),assembly_asset_ref={'asset_id':'AST-2015','version':v},placements_path=f'meshy/models/blender/AST-2015/{v}/placements.json',inspection_path=entry['inspection_path'],component_counts=report['props'],change_reason='Reference PAN-015 shows paired counseling chairs facing inward around a shared table; correct outward splay.');assembly['assemblies'].append(row);s.write(e.CAT/'scene-assemblies.json',assembly)
room.update(assetVersion=v,sourceFbxPath=f'meshy/models/blender/AST-2015/{v}/exports/room.fbx');s.write(R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json',registry);s.write(e.EVIDENCE/'counseling-seat-repairs.json',dict(schema_version=3,panorama_ref={'image_id':'PAN-015','version':'v001'},repairs=repairs))

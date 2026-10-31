"""Repair the seven additional seats proven to face away from their tables."""
import bpy,json,math,copy,importlib.util
from pathlib import Path
R=Path(__file__).resolve().parents[6]
spec=importlib.util.spec_from_file_location('e',R/'meshy/models/blender/AST-2064/v003/processing/enrich_worship.py');e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e);s=e.s;e.SCRIPT=Path(__file__).relative_to(R).as_posix();e.render=lambda *a,**k:None
registry=json.loads((R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json').read_text('utf-8'))
survey=json.loads((R/'docs/machine/evidence/worship-enrichment-v001/seating-survey.json').read_text('utf-8'));fixed=[]
for number in [2,16,35,66]:
    room=next(r for r in registry['rooms']if r['roomId']==f'PAN-{number:03}');aid=room['assetId'];old=room['assetVersion'];v='v'+str(int(old[1:])+1).zfill(3)
    pl=json.loads((R/f'meshy/models/blender/{aid}/{old}/placements.json').read_text('utf-8'));flagged={r['instance_id']for r in survey['seating_instances']if r['room_id']==room['roomId']and r.get('review_flag','').startswith('faces_away')};s.reset();props={}
    for i in pl['instances']:
        if i['instance_id']in flagged:
            old_angle=i['rotation_euler_blender_deg'][2];i['rotation_euler_blender_deg'][2]=(old_angle+180)%360;i['rotation_z_rad']=math.radians(i['rotation_euler_blender_deg'][2]);fixed.append(dict(room_id=room['roomId'],instance_id=i['instance_id'],old_z_deg=old_angle,new_z_deg=i['rotation_euler_blender_deg'][2]))
        obs,a=e.import_asset(i['asset_id'],i['version']);root=bpy.data.objects.new(i['instance_id'],None);bpy.context.collection.objects.link(root)
        for o in obs:
            if o.parent is None:o.parent=root
        root.location=i['position_blender_m'];root.rotation_euler=[math.radians(v)for v in i['rotation_euler_blender_deg']];root.scale=i['scale'];bpy.context.view_layer.update()
        tri=e.triangles([o for o in obs if o.type=='MESH']);key=(i['asset_id'],i['version']);i['component_mesh_count']=len([o for o in obs if o.type=='MESH'])
        if key not in props:props[key]=dict(name=a['name'],asset_ref=dict(asset_id=key[0],version=key[1]),triangles_per_instance=tri,instance_count=0,total_triangles=0)
        props[key]['instance_count']+=1;props[key]['total_triangles']+=tri
    entry,report=e.save(aid,v,room['name'],'diorama','blender_direct',0,props=list(props.values()),placements=pl)
    cat=s.read('assets');cat['assets'][-1]['preview_path']=None;s.write(e.CAT/'assets.json',cat)
    assembly=s.read('scene-assemblies');row=copy.deepcopy(max([x for x in assembly['assemblies']if x['assembly_id']==f'pan-{number:03}-workplace'],key=lambda x:x['revision']));row.update(revision=row['revision']+1,recorded_at=e.now(),assembly_asset_ref={'asset_id':aid,'version':v},placements_path=f'meshy/models/blender/{aid}/{v}/placements.json',inspection_path=entry['inspection_path'],component_counts=report['props'],change_reason='Measured Seat/Back direction points away from nearest intended table; rotate flagged actual seat instances180 degrees without changing geometry.');assembly['assemblies'].append(row);s.write(e.CAT/'scene-assemblies.json',assembly)
    room.update(assetVersion=v,sourceFbxPath=f'meshy/models/blender/{aid}/{v}/exports/room.fbx',scenePath=f'Assets/Scenes/Workplaces/PAN-{number:03}-{v}.unity')
registry['buildId']='workplaces-v008';s.write(R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json',registry);s.write(e.EVIDENCE/'additional-seat-repairs.json',dict(schema_version=3,repairs=fixed,verified_before_by='Actual GLB Seat/Back survey',after_status='Fresh final-GLB survey and WebGL required'))

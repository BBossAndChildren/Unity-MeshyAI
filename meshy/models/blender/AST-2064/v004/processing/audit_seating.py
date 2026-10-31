"""Read-only actual-GLB seating direction survey across current room registry.
Geometric suggestions are not automatic correctness claims for arbitrary layouts.
"""
import bpy,json,math,datetime
from pathlib import Path
from mathutils import Vector,Euler,Matrix
R=Path(__file__).resolve().parents[6]
C=R/'docs/machine/catalog'
assets=json.loads((C/'assets.json').read_text('utf-8'))['assets'];lookup={(a['asset_id'],a['version']):a for a in assets}
registry=json.loads((R/'unity/projects/OfficeAssistant-v001/Assets/Resources/workplace-registry.json').read_text('utf-8'))
cache={};results=[]
def center(o):return sum((o.matrix_world@Vector(v) for v in o.bound_box),Vector())/8
def geometry(aid,v):
    key=(aid,v)
    if key in cache:return cache[key]
    bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=str(R/lookup[key]['runtime_path']))
    obs=[o for o in bpy.context.scene.objects if o.type=='MESH'];seat=next((o for o in obs if o.name.lower().startswith('seat') and 'cushion' not in o.name.lower()),None);back=next((o for o in obs if o.name.lower().startswith('back')),None)
    if seat is None:seat=next((o for o in obs if o.name.lower().startswith(('cushion','seat cushion'))),None)
    if aid=='AST-003':
        points=[o.matrix_world@v.co for o in obs for v in o.data.vertices]
        backpts=[p for p in points if p.z>.75 and abs(p.x)<.25];seatpts=[p for p in points if .49<p.z<.60 and abs(p.x)<.28]
        if backpts and seatpts:
            front=sum(seatpts,Vector())/len(seatpts)-sum(backpts,Vector())/len(backpts);front.z=0;cache[key]=list(front.normalized());return cache[key]
    if seat is None or back is None:cache[key]=None;return None
    a,b=center(seat),center(back);front=a-b;front.z=0
    cache[key]=list(front.normalized()) if front.length>.01 else None;return cache[key]
for room in registry['rooms']:
    if room['roomId']=='PAN-001':continue
    p=R/room['sourceFbxPath'];p=p.parent.parent/'placements.json';items=json.loads(p.read_text('utf-8'))['instances']
    tables=[i for i in items if any(w in lookup[(i['asset_id'],i['version'])]['name'] for w in ['책상','테이블','작업대','강대상','제대','강의대','교탁'])]
    for i in items:
        name=lookup[(i['asset_id'],i['version'])]['name']
        if not any(w in name for w in ['의자','좌석','소파']):continue
        front=geometry(i['asset_id'],i['version']);row=dict(room_id=room['roomId'],asset_ref={'asset_id':i['asset_id'],'version':i['version']},instance_id=i['instance_id'],name=name,inspection_status='no_named_seat_back_geometry' if front is None else 'measured_geometry')
        if front:
            rot=Euler([math.radians(v) for v in i['rotation_euler_blender_deg']]).to_matrix();f=rot@Vector(front);pos=Vector(i['position_blender_m']);targets=tables
            if i['asset_id']=='AST-1247':targets=[t for t in tables if t['asset_id'] in ['AST-1244','AST-1257']]
            if targets:
                target=min(targets,key=lambda t:(Vector(t['position_blender_m'])-pos).length);d=Vector(target['position_blender_m'])-pos;d.z=0;dot=f.dot(d.normalized())
                row.update(front_vector=list(f),target_instance_id=target['instance_id'],target_dot=dot,distance_m=d.length,review_flag='faces_away_from_nearest_work_surface' if dot<-.35 else 'not_flagged_by_nearest_surface_heuristic')
        results.append(row)
out=R/'docs/machine/evidence/worship-enrichment-v001/seating-survey.json';out.parent.mkdir(parents=True,exist_ok=True)
out.write_text(json.dumps(dict(schema_version=3,checked_at=datetime.datetime.now().astimezone().isoformat(),rooms_scanned=70,seating_instances=results,limitations=['Heuristic nearest surface is not definitive for waiting areas, multi-seat tables or counseling.','Named actual mesh seat/back vectors measured; no guarantee every semantic error is found.','PAN-001 legacy direct scene excluded from this independent GLB survey.']),ensure_ascii=False,indent=2)+'\n','utf-8')
print('SEAT_SURVEY',len(results),sum(r.get('review_flag','').startswith('faces_away') for r in results),flush=True)

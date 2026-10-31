"""Local visual repair of the first simplification, no further paid calls."""
import bpy,bmesh,math,json,copy,importlib.util
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[6]
BASE=ROOT/'meshy/models/blender/AST-2064/v003/processing/enrich_worship.py'
spec=importlib.util.spec_from_file_location('enrich',BASE);e=importlib.util.module_from_spec(spec);spec.loader.exec_module(e)
s=e.s
SCRIPT=Path(__file__).relative_to(ROOT).as_posix()
e.SCRIPT=SCRIPT
def render(path,direction=(6,-9,7),size=800):
    lo,hi=e.bounds(e.meshes());center=(Vector(lo)+Vector(hi))*.5;span=max(Vector(hi)-Vector(lo));scene=bpy.context.scene
    scene.render.engine='CYCLES';scene.cycles.samples=12;scene.cycles.use_denoising=True
    scene.render.resolution_x=min(size,800);scene.render.resolution_y=min(size,800);scene.render.resolution_percentage=100
    scene.world=bpy.data.worlds.new('Neutral daylight');scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[1].default_value=.55
    for offset,power in [((-3,-4,6),500),((4,2,5),350)]:
        bpy.ops.object.light_add(type='AREA',location=center+Vector(offset));light=bpy.context.object;light.data.energy=power;light.data.size=5;light.rotation_euler=(center-light.location).to_track_quat('-Z','Y').to_euler()
    bpy.ops.object.camera_add(location=center+Vector(direction));camera=bpy.context.object;camera.rotation_euler=(center-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.type='ORTHO';camera.data.ortho_scale=span*1.22;scene.camera=camera
    scene.view_settings.view_transform='AgX';scene.render.image_settings.file_format='PNG';path.parent.mkdir(parents=True,exist_ok=True);scene.render.filepath=str(path);bpy.ops.render.render(write_still=True)
    for o in list(bpy.context.scene.objects):
        if o.type in ['CAMERA','LIGHT']:bpy.data.objects.remove(o,do_unlink=True)
e.render=render
s.COLORS.update(walnut=(12,8),deepteal=(7,12),burgundy=(0,12),navy=(9,12),gold=(4,12))
def recolor(aid,old,v,mode):
    s.reset();e.import_asset(aid,old)
    for o in e.meshes():
        # Color classification uses the actual UV of each polygon, not a tint.
        for p in o.data.polygons:
            uv=o.data.uv_layers.active.data[p.loop_indices[0]].uv
            nearest=min(s.MAPPING['cells'],key=lambda c:(uv.x-c['uv_center'][0])**2+(uv.y-c['uv_center'][1])**2)
            cell=(nearest['row'],nearest['column'])
            color=None
            if aid=='AST-1247':
                color='deepteal' if o.name.startswith('Seat cushion') and mode=='church' else 'burgundy' if o.name.startswith('Seat cushion') else 'burgundy' if o.name.startswith('Hymnal cover') else 'cream' if o.name.startswith('Hymnal pages') else 'walnut'
            elif aid in ['AST-1244','AST-1246']:color='walnut' if cell==s.COLORS['wood'] else 'gold' if cell==s.COLORS['yellow'] else None
            elif aid=='AST-3002':color='burgundy' if 'carpet' in o.name.lower() and 'border' not in o.name.lower() else 'gold' if 'border' in o.name.lower() else 'walnut'
            elif aid=='AST-3003':color=('deepteal' if mode=='church' else 'burgundy') if 'Aisle runner' in o.name else 'gold'
            elif aid=='AST-3004':color='gold' if 'frame' in o.name.lower() or 'lead' in o.name.lower() or 'mullion' in o.name.lower() else 'navy' if cell in [s.COLORS['pink'],s.COLORS['teal']] else 'cream'
            if color:e.uvcolor(o,p,color)
    a=next(a for a in s.read('assets')['assets'] if a['asset_id']==aid and a['version']==old)
    e.save(aid,v,a['name'],'prop','blender_direct')
def slats():
    s.reset()
    e.box('Acoustic panel foot',(0,0,.03),(.74,.22,.06),'walnut')
    for x in [-.30,-.20,-.10,0,.10,.20,.30]:e.box('Vertical wood slat',(x,0,.91),(.055,.075,1.76),'walnut')
    e.save('AST-3006','v001','목재 세로살 배경 패널','prop','blender_direct')

def flower():
    s.reset();e.import_asset('AST-3001','v002');o=e.meshes()[0]
    # Preserve the generated pot and lower leaf silhouette, remove the damaged
    # upper fragments. Geometric petals restore readable flowers at web scale.
    bm=bmesh.new();bm.from_mesh(o.data)
    bmesh.ops.delete(bm,geom=[v for v in bm.verts if v.co.z>.49],context='VERTS')
    seen=set();groups=[]
    for v in bm.verts:
        if v in seen:continue
        group=[];todo=[v];seen.add(v)
        while todo:
            a=todo.pop();group.append(a)
            for edge in a.link_edges:
                b=edge.other_vert(a)
                if b not in seen:seen.add(b);todo.append(b)
        groups.append(group)
    remove=[v for g in groups if len(g)<10 for v in g]
    if remove:bmesh.ops.delete(bm,geom=remove,context='VERTS')
    bm.to_mesh(o.data);bm.free();s.paint(o,'green');o.data.update()
    for p in o.data.polygons:e.uvcolor(o,p,'cream' if p.center.z<.24 else 'green')
    for index,(x,y,z) in enumerate([(-.14,-.07,.54),(.13,-.04,.61),(0,.13,.68)]):
        s.rod('Lily stem',(x*.3,y*.3,.29),(x,y,z),.012,'green',5)
        for k in range(5):
            a=k*math.tau/5+index*.4
            # A six-vertex curved diamond petal, eight triangles, with thickness.
            verts=[(0,0,0),(.09,-.043,.022),(.18,0,.08),(.09,.043,.022),(.08,0,.035),(.08,0,.008)]
            faces=[(0,1,4),(1,2,4),(2,3,4),(3,0,4),(1,0,5),(2,1,5),(3,2,5),(0,3,5)]
            mesh=bpy.data.meshes.new('Faceted lily petal');mesh.from_pydata(verts,[],faces);mesh.update()
            petal=bpy.data.objects.new('White lily petal',mesh);bpy.context.collection.objects.link(petal);petal.location=(x,y,z);petal.rotation_euler.z=a;s.paint(petal,'white')
        s.cyl('Gold lily center',(x,y,z+.015),.027,.035,'yellow',6)
    a,report=e.save('AST-3001','v003','백합 꽃꽂이 화분','prop','hybrid',0)
    a['generation_reason']='Reuse Meshy pot/foliage silhouette; locally repair isolated fragments and model readable lily petals. Original single paid task cost20; this refinement costs0.'
    a['source_asset_ref']={'asset_id':'AST-3001','version':'v002'}
    cat=s.read('assets');cat['assets'][-1]=a;s.write(e.CAT/'assets.json',cat)
    return a

def room(n):
    aid=f'AST-{2000+n}';old=ROOT/f'meshy/models/blender/{aid}/v003/placements.json';pl=json.loads(old.read_text('utf-8'));items=pl['instances']
    s.reset();props={}
    for i in items:
        if i['asset_id']=='AST-3001':i['version']='v003'
        replacements={'AST-1247':'v003' if n==64 else 'v004','AST-3002':'v002','AST-3003':'v002' if n==64 else 'v003','AST-3004':'v002','AST-1244':'v004','AST-1246':'v003'}
        if i['asset_id'] in replacements:i['version']=replacements[i['asset_id']]
        if i['asset_id']=='AST-3004':
            i['position_blender_m'][1]=2.24
            if n==64:i['asset_id']='AST-3006';i['version']='v001'
        if i['asset_id'].startswith('AST-300'):i['candidate_id']=f'CND-{262+int(i["asset_id"].split("-")[1])-3000:03}'
        objs,a=e.import_asset(i['asset_id'],i['version']);root=bpy.data.objects.new(i['instance_id'],None);bpy.context.collection.objects.link(root)
        for o in objs:
            if o.parent is None:o.parent=root
        root.location=i['position_blender_m'];root.rotation_euler=[math.radians(v) for v in i['rotation_euler_blender_deg']];root.scale=i['scale'];bpy.context.view_layer.update()
        tri=e.triangles([o for o in objs if o.type=='MESH']);key=(i['asset_id'],i['version']);i['component_mesh_count']=len([o for o in objs if o.type=='MESH'])
        if key not in props:props[key]=dict(name=a['name'],asset_ref={'asset_id':key[0],'version':key[1]},triangles_per_instance=tri,instance_count=0,total_triangles=0)
        props[key]['instance_count']+=1;props[key]['total_triangles']+=tri
    cat=s.read('assets');prev=next(a for a in cat['assets'] if a['asset_id']==aid and a['version']=='v003')
    entry,report=e.save(aid,'v004',prev['name'],'diorama','hybrid',0,props=list(props.values()),placements=pl)
    assembly=s.read('scene-assemblies');row=copy.deepcopy(max([r for r in assembly['assemblies'] if r['assembly_id']==f'pan-{n:03}-workplace'],key=lambda r:r['revision']))
    row.update(revision=row['revision']+1,recorded_at=e.now(),assembly_asset_ref={'asset_id':aid,'version':'v004'},placements_path=f'meshy/models/blender/{aid}/v004/placements.json',inspection_path=entry['inspection_path'],component_counts=report['props'],change_reason='Visual repair: remove isolated Meshy simplification fragments and restore readable lily petals locally; no additional paid call.')
    assembly['assemblies'].append(row);s.write(e.CAT/'scene-assemblies.json',assembly)
    e.render(ROOT/f'meshy/models/original/{aid}/v004/previews/back.png',(-6,9,7))
    e.render(ROOT/f'meshy/models/original/{aid}/v004/previews/top.png',(0,-.01,12))
flower();recolor('AST-1247','v002','v003','church');recolor('AST-1247','v002','v004','cathedral')
recolor('AST-1244','v003','v004','church');recolor('AST-1246','v002','v003','church')
recolor('AST-3002','v001','v002','church');recolor('AST-3003','v001','v002','church');recolor('AST-3003','v001','v003','cathedral')
recolor('AST-3004','v001','v002','cathedral');slats();room(64);room(71)

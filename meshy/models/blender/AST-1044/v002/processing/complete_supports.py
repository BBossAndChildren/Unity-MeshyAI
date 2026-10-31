"""Systematic physical-support production pass, preserving current versions.

Uses CURRENT authoritative placements and fixed actual GLBs. Floor alignment
uses transformed bounds, including rotated objects. Loose sets remain loose.
No hooks, CI, paid calls, or runtime validation machinery are installed.
"""
import bpy,json,copy,math,datetime,importlib.util
from pathlib import Path
from mathutils import Vector,Matrix,Euler

ROOT=Path(__file__).resolve().parents[6]
SCRIPT=Path(__file__).relative_to(ROOT).as_posix()
SUPPORT='meshy/models/blender/AST-1010/v001/processing/build_shared.py'
spec=importlib.util.spec_from_file_location('shared',ROOT/SUPPORT);s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
CAT=ROOT/'docs/machine/catalog';EVIDENCE=ROOT/'docs/machine/evidence/workplaces-model-review-v001'
F=.296
catalog=s.read('assets');assets={(a['asset_id'],a['version']):a for a in catalog['assets']}
progress=s.read('workplace-production-v001');assemblies=s.read('scene-assemblies')
baseline=copy.deepcopy(progress)
NEW=[];room_results=[];prop_results=[]

def now():return datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat()
def rel(path):return path.relative_to(ROOT).as_posix()
def meshes():return [o for o in bpy.context.scene.objects if o.type=='MESH']
def bounds(objects):
    points=[o.matrix_world@Vector(c) for o in objects for c in o.bound_box]
    return dict(min=[min(v[k] for v in points) for k in range(3)],max=[max(v[k] for v in points) for k in range(3)])
def names(prefix):return [o for o in meshes() if o.name.startswith(prefix)]
def shift(prefix,axis,amount):
    for o in names(prefix):o.location[axis]+=amount
def box(name,p,size,color='cream'):return s.box(name,p,size,color)
def rod(name,a,b,r=.025,color='dark'):return s.rod(name,a,b,r,color)

def edit_prop(aid):
    n=int(aid.split('-')[1]);s.MATERIAL=meshes()[0].data.materials[0]
    if n in [1013,1191,1218,1219]:
        for o in names('Writing surface'):o.scale.x*=1.025;o.scale.z*=1.05
    elif n==1017:shift('Power button',1,.01)
    elif n==1025:
        for x in [-.53,0,.53]:rod('Seat support',(x,0,.35),(x,0,.46),.035,'dark')
        for x in [-.62,.62]:rod('Leg cross member',(x,-.17,.33),(x,.17,.33),.035,'dark')
    elif n==1026:rod('Upper pocket support',(0,0,.8),(0,0,1.12),.035,'purple')
    elif n==1029:shift('Scale pan',2,.0075)
    elif n==1039:shift('Focus knob',0,-.01)
    elif n==1041:box('Mattress support',(0,0,.595),(.70,1.75,.04),'teal')
    elif n==1044:
        for x in [-.35,.35]:
            for y in [-.70,.70]:box('Bed leg',(x,y,.10),(.07,.07,.20),'wood')
    elif n==1069:
        # Replace the inherited chair legs with an actual wheel-supported frame.
        for o in names('Leg'):bpy.data.objects.remove(o,do_unlink=True)
        rod('Rear axle',(-.32,.12,.30),(.32,.12,.30),.025,'dark')
        for sign in [-1,1]:
            x=sign*.18
            rod('Seat axle support',(x,.12,.30),(x,.12,.44),.025,'dark')
            rod('Arm support',(sign*.24,0,.44),(sign*.31,0,.69),.022,'dark')
            rod('Caster fork',(x,-.18,.42),(sign*.31,-.30,.14),.022,'dark')
            rod('Footplate support',(sign*.15,-.18,.42),(sign*.15,-.42,.13),.022,'dark')
        for o in names('Rear wheel'):o.scale.x*=.30/.29;o.scale.y*=.30/.29
    elif n==1071:shift('Warning lamp',2,-.02);shift('Control panel',1,.01)
    elif n==1078:
        for x in [-.14,.14]:rod('Wheel axle',(x,-.16,.06),(x,.16,.06),.018,'dark')
    elif n==1081:shift('Circuit board',2,-.035)
    elif n in [1085,1173,1202]:
        sx,sy,sz=(1.1,1.1,1.2) if n==1202 else (1,1,1.1) if n==1173 else (1,1,1)
        for sign in [-1,1]:rod('Arm support',(sign*.28*sx,0,.50*sz),(sign*.33*sx,0,.69*sz),.025*min(sx,sy),'cream')
        rod('Footrest support',(0,-.18*sy,.49*sz),(0,-.45*sy,.28*sz),.025*min(sx,sy),'dark')
    elif n in [1089,1095]:
        sz=1.5 if n==1095 else 1
        for x in [-.20,.20]:rod('Door handle mount',(x,-.325,.66*sz),(x,-.37,.66*sz),.018,'cream')
        shift('Burner',2,-.005*sz)
    elif n==1091:
        # A self-supported tall utensil rack replaces an unexplained elevated root.
        for o in names('Post'):o.location.z=.85;o.scale.z*=1.7/.75
        shift('Crossbar',2,.95);shift('Utensil head',2,.95)
        for o in names('Utensil grip'):o.location.z=.57+.95;o.scale.z*=.36/.29
    elif n==1104:
        for o in names('Canvas'):o.location.y=-.05;o.location.z=.9175
    elif n in [1110,1144]:
        rod('Tripod hub',(0,0,.98),(0,0,1.05),.03,'dark')
        if n==1144:
            for prefix in ['Meter','Readout','Probe']:shift(prefix,2,-.015)
    elif n in [1126,1224]:
        for o in names('Foot'):o.location.x*=1.125
    elif n==1127:
        for x in [-.58,.58]:rod('Seat cross support',(x,-.20,.40),(x,.22,.40),.03,'dark')
    elif n==1131:
        for o in names('Brick'):o.scale.x*=.23/.22;o.scale.z*=.13/.12
    elif n==1132:
        for o in names('Timber'):o.location.z+=.005;o.scale.z*=.13/.11
    elif n in [1138,1217]:shift('Indicator',1,.01225*(1.2 if n==1217 else 1))
    elif n in [1143,1148,1154]:
        for o in names('Leaf'):o.scale.x*=1.3;o.scale.y*=1.3
    elif n==1149:rod('Handle lower bridge',(-.17,0,.12),(-.10,0,.12),.022,'green')
    elif n==1181:
        for z in [.2,.6,1.0]:
            for x in [-.5,.5]:rod('Rack end brace',(x,-.15,z),(x,.15,z),.02,'dark')
            box('Ball shelf',(0,0,z+.0175),(.95,.32,.025),'dark')
    elif n==1201:box('Fork chassis',(0,.17,.10),(.55,.14,.12),'yellow')
    elif n==1215:
        for x in [-.60,.60]:
            for y in [-.22,.22]:box('Sofa leg',(x,y,.07),(.07,.07,.14),'wood')
    elif n in [1244,1258]:
        shift('Cross upright',1,.006 if n==1258 else .0075)
        shift('Cross arm',1,.006 if n==1258 else .0075)
    else:raise RuntimeError('No explicit physical repair for '+aid)

def preview(path):
    objects=meshes();b=bounds(objects);lo=Vector(b['min']);hi=Vector(b['max']);center=(lo+hi)/2;span=max(hi-lo)*1.45+.15
    scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=2;scene.cycles.use_denoising=False
    scene.render.resolution_x=320;scene.render.resolution_y=320;scene.render.resolution_percentage=100
    scene.world=bpy.data.worlds.new('Support review world');scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[1].default_value=.7
    bpy.ops.object.light_add(type='AREA',location=center+Vector((-3,-4,6))*max(span,.2));lamp=bpy.context.object;lamp.data.energy=500*max(span,.2)**2;lamp.data.size=5*max(span,.2);lamp.rotation_euler=(center-lamp.location).to_track_quat('-Z','Y').to_euler()
    bpy.ops.object.camera_add(location=center+Vector((span,-span,span*.8)));camera=bpy.context.object;camera.rotation_euler=(center-camera.location).to_track_quat('-Z','Y').to_euler();camera.data.type='ORTHO';camera.data.ortho_scale=span;scene.camera=camera;scene.render.filepath=str(path);scene.render.image_settings.file_format='PNG';bpy.ops.render.render(write_still=True)

def finalize(aid,version,base,kind,component_counts=None,placements=None):
    out=ROOT/f'meshy/models/blender/{aid}/{version}';src=ROOT/f'meshy/models/original/{aid}/{version}'
    assert not (out/'model.blend').exists(),'Preserve existing model version '+aid+' '+version
    objects=meshes();triangles=sum(len(p.vertices)-2 for o in objects for p in o.data.polygons)
    assert triangles<=(1000 if kind=='prop' else 5000),(aid,triangles)
    (out/'exports').mkdir(parents=True,exist_ok=True);(src/'previews').mkdir(parents=True,exist_ok=True)
    bpy.ops.object.select_all(action='DESELECT')
    for o in bpy.context.scene.objects:o.select_set(o.type in ['MESH','EMPTY'])
    bpy.context.view_layer.objects.active=objects[0]
    bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'));bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
    glb=out/'exports/model.glb';bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
    fbxname='office.fbx' if aid=='AST-020' else 'room.fbx' if kind=='diorama' else 'model.fbx'
    bpy.ops.export_scene.fbx(filepath=str(out/'exports'/fbxname),use_selection=True,add_leaf_bones=False,bake_anim=False,axis_forward='-Z',axis_up='Y',path_mode='STRIP')
    bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=str(glb));bpy.context.view_layer.update();objects=meshes()
    measured=sum(len(p.vertices)-2 for o in objects for p in o.data.polygons);assert measured==triangles
    materials={m for o in objects for m in o.data.materials};images={n.image for m in materials for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image};assert len(materials)==len(images)==1
    centers=[c['uv_center'] for c in s.MAPPING['cells']]
    uvok=all(o.data.uv_layers.active and all(any(abs(l.uv.x-u)<1e-5 and abs(l.uv.y-v)<1e-5 for u,v in centers) for l in o.data.uv_layers.active.data) for o in objects);assert uvok
    b=bounds(objects);inspection=copy.deepcopy(json.loads((ROOT/base['inspection_path']).read_text('utf8')))
    ck=lambda why:dict(status='pass',evidence=why,reason=None)
    inspection.update(asset_id=aid,version=version,kind=kind,scene_triangles=measured,material_count=1,texture_count=1,glb_bytes=glb.stat().st_size,dimensions_m=[b['max'][i]-b['min'][i] for i in range(3)],props=component_counts or [dict(name=base['name'],triangles_per_instance=measured,instance_count=1,total_triangles=measured)],target_web_environment='New Unity WebGL build; execution pending',checks=dict(triangle_budget=ck('Actual final GLB Blender reimport, every instance included'),palette_uv=ck('All final GLB UV loops match the unchanged fixed palette'),shared_material=ck('Final GLB one material and one image'),support_production=ck('Explicit physical support production; transformed floor/surface gaps recorded in support-changes.json'),visual_front_side_back=dict(status='unverified',evidence=None,reason='New versions require additive directional view review'),web_display=dict(status='unverified',evidence=None,reason='New build must be executed independently')),remaining_issues=['New version needs directional and target-WebGL verification; no ready promotion.'])
    s.write(out/'inspection.json',inspection);preview(src/'previews/front.png')
    entry=copy.deepcopy(base);entry.update(version=version,source_path=rel(src/'source.blend'),blender_path=rel(out/'model.blend'),runtime_path=rel(glb),preview_path=rel(src/'previews/front.png'),unity_path=None,unity_palette_path=None,inspection_path=rel(out/'inspection.json'),production_record_path=rel(src/'README.md'),processing_paths=[SCRIPT,SUPPORT]+[x for x in base['processing_paths'] if x not in [SCRIPT,SUPPORT]],status='in_progress',generation_method='blender_direct',generation_reason='Reuse current fixed model geometry and authoritative placements; correct measured physical support gaps and connect explicitly defined structural parts.',meshy_credits_used=0);entry.pop('unity_application',None)
    (src/'README.md').write_text(f'# {aid} {version} — systematic support correction\n\n2026-10-31 Blender direct production, zero Meshy/image calls and credits. Reuses {base["asset_id"]} {base["version"]}; all old source/model/export bytes preserved. Script {SCRIPT}. Palette v001 and source colors unchanged; new support parts use the same color1 cells, no tint or extra textures. Actual final GLB reopened: {measured} triangles, one material, one image.\n\nCurrent physical changes are explicit in support-changes.json. Virtual design coordinates are not real-world measurements. No specialist equipment validation. New Unity and WebGL execution pending; status in_progress.\n','utf8')
    s.write(out/'asset-entry.json',dict(schema_version=3,asset=entry))
    if placements:s.write(out/'placements.json',placements)
    assets[(aid,version)]=entry;NEW.append(entry)
    return entry,inspection

REPAIRS=[1013,1017,1025,1026,1029,1039,1041,1044,1069,1071,1078,1081,1085,1089,1091,1095,1104,1110,1126,1127,1131,1132,1138,1143,1144,1148,1149,1154,1173,1181,1191,1201,1202,1215,1217,1218,1219,1224,1244,1258]
replacements={}
for n in REPAIRS:
    aid=f'AST-{n}';base=max((a for a in catalog['assets'] if a['asset_id']==aid),key=lambda a:a['version']);version=f'v{int(base["version"][1:])+1:03}'
    bpy.ops.wm.open_mainfile(filepath=str(ROOT/base['blender_path']));edit_prop(aid)
    entry,inspection=finalize(aid,version,base,'prop');replacements[(aid,base['version'])]=entry
    record=dict(asset_ref={'asset_id':aid,'version':version},supersedes={'asset_id':aid,'version':base['version']},reason='Explicit structural support repair in edit_prop('+aid+'); loose semantic sets remain independent.',triangles=inspection['scene_triangles'])
    s.write((ROOT/entry['blender_path']).parent/'support-changes.json',dict(schema_version=3,changes=[record]));prop_results.append(record)
    for row in progress['candidates']:
        if row['candidate_id']==f'CND-{n-1000:03}':row['result_asset_ref']={'asset_id':aid,'version':version}
    print('SUPPORTED_PROP',aid,version,inspection['scene_triangles'],flush=True)

def reconstruct(items,office=False):
    s.reset();material=s.MATERIAL;groups={}
    for inst in items:
        a=assets[(inst['asset_id'],inst['version'])];before=set(bpy.context.scene.objects);bpy.ops.import_scene.gltf(filepath=str(ROOT/a['runtime_path']));bpy.context.view_layer.update();imported=[o for o in bpy.context.scene.objects if o not in before];objects=[o for o in imported if o.type=='MESH']
        if office:
            assert len(objects)==1
            o=objects[0];world=o.matrix_world.copy();o.data=o.data.copy();o.data.transform(world);o.parent=None;o.matrix_world=Matrix.Identity(4);o.name=inst['instance_id'];root=o
            for empty in imported:
                if empty.type=='EMPTY':bpy.data.objects.remove(empty,do_unlink=True)
        else:
            root=bpy.data.objects.new(inst['instance_id'],None);bpy.context.collection.objects.link(root)
            for o in imported:
                if o.parent is None:o.parent=root
        root.location=inst['position_blender_m'];root.scale=inst['scale'];root.rotation_euler=[math.radians(x) for x in inst.get('rotation_euler_blender_deg',[0,0,math.degrees(inst.get('rotation_z_rad',0))])]
        for o in objects:
            o.data.materials.clear();o.data.materials.append(material)
            for p in o.data.polygons:p.material_index=0
        groups[inst['instance_id']]=(root,objects)
    bpy.context.view_layer.update();return groups

for row in baseline['scenes']:
    number=int(row['prompt_ref']['prompt_id'].split('-')[1]);ref=row['assembly_asset_ref'];base=assets[(ref['asset_id'],ref['version'])];folder=(ROOT/base['blender_path']).parent;data=json.loads((folder/'placements.json').read_text('utf8'));items=copy.deepcopy(data['instances']);changes=[]
    for inst in items:
        replacement=replacements.get((inst['asset_id'],inst['version']))
        if replacement:
            old=inst['version'];inst['version']=replacement['version'];changes.append(dict(instance_id=inst['instance_id'],kind='structural_asset_replacement',before=old,after=inst['version']))
    # Explicit extra support for previously unexplained raised equipment.
    if number==61:
        items.append(dict(asset_id='AST-1045',version='v001',candidate_id='CND-045',instance_id=f'AST-1045-{len(items):03}',position_blender_m=[1.75,.8,F],rotation_euler_blender_deg=[0,0,0],rotation_z_rad=0,scale=[1,1,1]));changes.append(dict(kind='added_radio_support',asset_ref={'asset_id':'AST-1045','version':'v001'}))
    if number==71:
        items.append(dict(asset_id='AST-1124',version='v001',candidate_id='CND-124',instance_id=f'AST-1124-{len(items):03}',position_blender_m=[0,1.8,F],rotation_euler_blender_deg=[0,0,0],rotation_z_rad=0,scale=[.55,.55,.8125]));changes.append(dict(kind='added_crucifix_pedestal',asset_ref={'asset_id':'AST-1124','version':'v001'},height_m=.65))
    groups=reconstruct(items,number==1)
    def move(inst,delta,reason):
        if abs(delta)<=1e-6:return
        root,objects=groups[inst['instance_id']];before=inst['position_blender_m'][2];root.location.z+=delta;inst['position_blender_m'][2]+=delta;bpy.context.view_layer.update();changes.append(dict(instance_id=inst['instance_id'],kind='z_alignment',before=before,after=inst['position_blender_m'][2],delta_m=delta,reason=reason))
    def bottom(inst):return bounds(groups[inst['instance_id']][1])['min'][2]
    def set_bottom(inst,target,reason):move(inst,target-bottom(inst),reason)
    for inst in items:
        aid=inst['asset_id'];candidate=inst.get('candidate_id');rootz=inst['position_blender_m'][2]
        if aid in ['AST-001','AST-002'] or candidate=='CND-139':continue
        if candidate=='CND-067' or rootz<=F+.0001 or number==71 and candidate=='CND-262':
            gap=bottom(inst)-F
            if abs(gap)>.0050001:set_bottom(inst,F,'Actual transformed lowest point aligned to floor; intentional low-terrain embedding excluded.')
    # Known support planes from actual source parts, not model origins.
    for inst in items:
        c=inst.get('candidate_id');aid=inst['asset_id'];root,objects=groups[inst['instance_id']]
        if number==2 and c=='CND-014':
            old=root.location.y;root.location.y=1.5225;inst['position_blender_m'][1]=1.5225;changes.append(dict(instance_id=inst['instance_id'],kind='wall_mount_y',before=old,after=1.5225,reason='Memo rear face contacts writing-surface front.'))
        elif number==5 and c=='CND-053':set_bottom(inst,F+(.6075 if inst['position_blender_m'][2]<F+.9 else 1.1075),'Actual shelf top; remove previous slight penetration.')
        elif number==24 and c=='CND-091':move(inst,F-inst['position_blender_m'][2],'New taller rack has actual legs to floor; upper utensils retain previous world height.')
        elif number==25 and c=='CND-094':set_bottom(inst,F+.88,'Mixer base on actual workbench top.')
        elif number in [30,31] and c=='CND-109':
            trip=next(i for i in items if i.get('candidate_id')=='CND-110');mounts=[o for o in groups[trip['instance_id']][1] if o.name.startswith('Mount')];set_bottom(inst,bounds(mounts)['max'][2],'Camera base on actual tripod mount after tripod floor alignment.')
        elif number==44 and c=='CND-168':set_bottom(inst,F+.18,'Rotated ring bottom contacts deck rather than penetrating it.')
        elif number==54 and c=='CND-005':
            old=list(inst['position_blender_m']);root.location.x=0;root.location.y=.65;inst['position_blender_m'][0]=0;inst['position_blender_m'][1]=.65;changes.append(dict(instance_id=inst['instance_id'],kind='support_xy',before=old,after=inst['position_blender_m'][:],reason='Extra monitor previously outside console footprint; now on console front work surface without overlap with rear screens.'))
        elif number==60 and c=='CND-211':set_bottom(inst,F+2,'Cable tray rests on actual rack tops.')
        elif number==60 and c=='CND-212':set_bottom(inst,F+.8675,'Management laptop lower face on cart tray, not embedded in it.')
        elif number==61 and c in ['CND-214','CND-175']:set_bottom(inst,F+.6175,'Auxiliary terminal/radio base on actual bedside support top.')
        elif number==64 and c=='CND-245':
            # Reading surface and book share the actual 12 degree slope.
            local_min=bottom(inst)-inst['position_blender_m'][2]
            angles=[12,0,0];root.rotation_euler=[math.radians(x) for x in angles];inst['rotation_euler_blender_deg']=angles;inst['rotation_z_rad']=0
            target=F+1.177+(.033-local_min)/math.cos(math.radians(12));move(inst,target-inst['position_blender_m'][2],'Open book aligned to inclined pulpit surface by normal, not horizontal AABB.')
        elif number==67 and c=='CND-114':set_bottom(inst,F+.6075,'Equipment case on actual shelf top rather than intersecting it.')
    bpy.context.view_layer.update()
    # Remaining small raised-object gaps: horizontal contact with actual mesh
    # support tops. Large/vertical/intentional supports are handled above.
    excluded={'CND-014','CND-048','CND-139','CND-245'}
    for inst in items:
        if inst.get('candidate_id') in excluded or inst['asset_id'] in ['AST-001','AST-002','AST-017']:continue
        if inst['position_blender_m'][2]<=F+.0201:continue
        own=bounds(groups[inst['instance_id']][1]);low=own['min'][2];support=[]
        for other in items:
            if other['instance_id']==inst['instance_id']:continue
            for obj in groups[other['instance_id']][1]:
                b=bounds([obj])
                if b['max'][2]>low+.005:continue
                if all(min(b['max'][k],own['max'][k])-max(b['min'][k],own['min'][k])>.005 for k in [0,1]):support.append(b['max'][2])
        if support:
            top=max(support);gap=low-top
            if .0050001<gap<=.050001:set_bottom(inst,top,'Measured small horizontal support gap; source/current placements retained otherwise.')
    # Source props/poses without any physical change retain their existing files.
    if not changes:continue
    aid=base['asset_id'];version=f'v{1+max(int(a["version"][1:]) for a in assets.values() if a["asset_id"]==aid):03}'
    counts={}
    for inst in items:
        key=(inst['asset_id'],inst['version']);counts[key]=counts.get(key,0)+1
    component_counts=[]
    for key,qty in counts.items():
        a=assets[key];tri=json.loads((ROOT/a['inspection_path']).read_text('utf8'))['scene_triangles'];component_counts.append(dict(name=a['name'],asset_ref={'asset_id':key[0],'version':key[1]},triangles_per_instance=tri,instance_count=qty,total_triangles=tri*qty))
    data.update(instances=items,supersedes_asset_ref=ref,support_repair_scope='Current authoritative placements preserved; explicit structural replacements and measured support corrections only.')
    entry,inspection=finalize(aid,version,base,'diorama',component_counts,data);assert sum(p['total_triangles'] for p in component_counts)==inspection['scene_triangles']
    out=(ROOT/entry['blender_path']).parent;s.write(out/'support-changes.json',dict(schema_version=3,changes=changes))
    assembly_id='pan-001-office' if number==1 else f'pan-{number:03}-workplace';prior=[a for a in assemblies['assemblies'] if a['assembly_id']==assembly_id];assembly=copy.deepcopy(max(prior,key=lambda x:x['revision']))
    assembly.update(revision=1+max(a['revision'] for a in prior),recorded_at=now(),assembly_asset_ref={'asset_id':aid,'version':version},placements_path=rel(out/'placements.json'),inspection_path=rel(out/'inspection.json'),component_counts=component_counts,change_reason='Comprehensive physical support alignment and explicitly connected structural parts, old versions preserved.');assemblies['assemblies'].append(assembly)
    live=next(x for x in progress['scenes'] if x['prompt_ref']==row['prompt_ref']);live.update(assembly_asset_ref={'asset_id':aid,'version':version},production_status='assembled_runtime_unverified',build_id=None,evidence_paths=[rel(out/'inspection.json'),rel(out/'placements.json'),rel(out/'support-changes.json')]);live['checks'].update(final_glb='pass',unity_editor='unverified',webgl='unverified')
    room_results.append(dict(prompt_ref=row['prompt_ref'],name=row['name'],asset_ref={'asset_id':aid,'version':version},changes=changes,scene_triangles=inspection['scene_triangles']))
    print('SUPPORTED_ROOM',number,aid,version,inspection['scene_triangles'],len(changes),flush=True)

# One final catalog publication after all actual new files are present.
catalog['assets'].extend(NEW);progress['updated_at']=now()
s.write(CAT/'assets.json',catalog);s.write(CAT/'scene-assemblies.json',assemblies);s.write(CAT/'workplace-production-v001.json',progress)
s.write(EVIDENCE/'comprehensive-support-production.json',dict(schema_version=3,recorded_at=now(),production_script=SCRIPT,source_bounds_path='docs/machine/evidence/workplaces-model-review-v001/systematic-support-bounds.json',prop_replacements=prop_results,rooms=room_results,changed_prop_count=len(prop_results),changed_room_count=len(room_results),paid_calls=0,meshy_credits_used=0,remaining_checks=['New final GLB directional/manual review and Unity/WebGL execution must be recorded independently.']))
print('COMPREHENSIVE_SUPPORTS_COMPLETE',len(prop_results),len(room_results),flush=True)

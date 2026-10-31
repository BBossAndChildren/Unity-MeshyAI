"""Same brief, palette, export checks and cameras; two distinct production routes."""
import bpy,bmesh,math,json,time,sys
from pathlib import Path
from mathutils import Vector
R=Path(__file__).resolve().parents[6]
mapping=json.loads((R/'meshy/models/textures/palettes/v001/mapping.json').read_text(encoding='utf-8'))
def cell(row,col):return next(c for c in mapping['cells'] if c['texture_id']=='color1' and c['row']==row and c['column']==col)
colors={'cushion':cell(3,7),'frame':cell(15,12),'wheel':cell(15,14)}
def material():
    m=bpy.data.materials.new('SharedPalette_v001');m.use_nodes=True;p=m.node_tree.nodes.get('Principled BSDF');p.inputs['Base Color'].default_value=(1,1,1,1);p.inputs['Roughness'].default_value=.8
    t=m.node_tree.nodes.new('ShaderNodeTexImage');t.image=bpy.data.images.load(str(R/'meshy/models/textures/palettes/v001/palette.png'));t.image.pack();t.interpolation='Closest';t.extension='EXTEND';m.node_tree.links.new(t.outputs['Color'],p.inputs['Base Color']);return m
def paint(o,m,role):
    o.data.materials.clear();o.data.materials.append(m)
    uv=o.data.uv_layers.active or o.data.uv_layers.new(name='PaletteUV')
    for p in o.data.polygons:
        c=colors[role(p) if callable(role) else role]
        for i in p.loop_indices:uv.data[i].uv=c['uv_center']
    for a in list(o.data.color_attributes):o.data.color_attributes.remove(a)
def box(name,loc,dim,bevel=0,segments=1,role='frame',rot=(0,0,0)):
    bpy.ops.mesh.primitive_cube_add(size=1,location=loc);o=bpy.context.object;o.name=name;o.dimensions=dim;bpy.ops.object.transform_apply(location=False,rotation=False,scale=True)
    if bevel:
        mod=o.modifiers.new('RoundedEdges','BEVEL');mod.width=bevel;mod.segments=segments;bpy.ops.object.modifier_apply(modifier=mod.name)
    o.rotation_euler=rot;o['palette_role']=role;return o
def cylinder(name,loc,radius,depth,vertices=8,role='frame',rot=(0,0,0)):
    bpy.ops.mesh.primitive_cylinder_add(vertices=vertices,radius=radius,depth=depth,location=loc,rotation=rot);o=bpy.context.object;o.name=name;o['palette_role']=role;return o
def beam(name,a,b,width,depth):
    a,b=Vector(a),Vector(b);o=box(name,(a+b)/2,(width,depth,(b-a).length));o.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler();return o
def finish(version,method,start,partcounts,source_triangles=None):
    out=R/f'meshy/models/blender/AST-003/{version}';src=R/f'meshy/models/original/AST-003/{version}'
    for p in [out/'exports',src/'previews']:p.mkdir(parents=True,exist_ok=True)
    if (out/'model.blend').exists() and '--revise' not in sys.argv:raise RuntimeError('Version exists: preserve it')
    meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
    bpy.ops.object.select_all(action='DESELECT')
    for o in meshes:o.select_set(True)
    bpy.context.view_layer.objects.active=meshes[0];bpy.ops.object.join();o=bpy.context.object;o.name='COM-04_Chair_'+method
    # Collapse identical material slots after joining so the GLB has one primitive.
    m=o.data.materials[0];o.data.materials.clear();o.data.materials.append(m)
    for p in o.data.polygons:p.material_index=0
    tri=o.modifiers.new('Triangulate','TRIANGULATE');bpy.ops.object.modifier_apply(modifier=tri.name)
    bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
    glb=out/'exports/model.glb';bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
    bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=str(glb))
    obs=[o for o in bpy.context.scene.objects if o.type=='MESH'];count=sum(len(p.vertices)-2 for o in obs for p in o.data.polygons)
    mats={m.name for o in obs for m in o.data.materials if m};imgs={n.image.name for o in obs for m in o.data.materials if m.use_nodes for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image}
    valid=[c['uv_center'] for c in colors.values()]
    uvok=all(any(abs(l.uv.x-u)<1e-6 and abs(l.uv.y-v)<1e-6 for u,v in valid) for o in obs for l in o.data.uv_layers.active.data)
    bm=bmesh.new()
    for o in obs:bm.from_mesh(o.data)
    bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=1e-6)
    boundary=sum(e.is_boundary for e in bm.edges); nonmanifold=sum(not e.is_manifold for e in bm.edges);bm.free()
    def ck(ok,txt):return dict(status='pass' if ok else 'fail',evidence=txt,reason=None)
    report=dict(schema_version=3,asset_id='AST-003',version=version,kind='prop',generation_method=method,target_web_environment='Local Three.js browser, not Unity WebGL',props=[dict(name='COM-04 swivel office chair',triangles_per_instance=count,instance_count=1,total_triangles=count)],scene_triangles=count,material_count=len(mats),texture_count=len(imgs),palette_resolution=[2508,2508],glb_bytes=glb.stat().st_size,checks=dict(prop_budget=ck(count<=1000,'Final GLB reimport'),palette_uv=ck(uvok,'All reimported UVs reference approved color1 cells'),shared_material=ck(len(mats)==len(imgs)==1,'Final GLB reimport'),geometric_edges=ck(nonmanifold==0,f'{boundary} boundary edges; {nonmanifold} nonmanifold edges after coordinate weld'),web_display=dict(status='unverified',evidence=None,reason='Pending browser inspection'),diorama_budget=dict(status='not_applicable',evidence=None,reason='One prop')),remaining_issues=['Unity and physical device performance unverified','Full-resolution shared palette dominates transfer size'],part_counts=partcounts,source_triangles=source_triangles,palette_cells=colors,processing_seconds=round(time.perf_counter()-start,3))
    (out/'inspection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8');print('CHAIR_RESULT',version,json.dumps({k:report[k] for k in ['scene_triangles','glb_bytes','processing_seconds','checks']}))
    scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=24;scene.render.resolution_x=720;scene.render.resolution_y=720;scene.render.resolution_percentage=100
    scene.world=bpy.data.worlds.new('ComparisonWorld');scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.75,.75,.75,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=.6
    bpy.ops.object.light_add(type='AREA',location=(-3,-4,5));bpy.context.object.data.energy=400;bpy.context.object.data.size=4
    bpy.ops.object.camera_add();cam=bpy.context.object;cam.data.type='ORTHO';cam.data.ortho_scale=1.65;scene.camera=cam
    for label,pos in [('front',(2,-3,1.8)),('rear',(-2,3,1.8)),('side',(3,0,1.3))]:
        cam.location=pos;cam.rotation_euler=(Vector((0,0,.57))-cam.location).to_track_quat('-Z','Y').to_euler();scene.render.filepath=str(src/f'previews/{label}.png');bpy.ops.render.render(write_still=True)

def direct():
    start=time.perf_counter();bpy.ops.wm.read_factory_settings(use_empty=True)
    # Front is -Y; five spokes and ten caster wheels are explicit, editable parts.
    box('Seat',(0,-.015,.535),(.52,.48,.10),.045,2,'cushion')
    back=box('Backrest',(0,.205,.86),(.48,.095,.53),.045,2,'cushion',(math.radians(-8),0,0))
    # Gently wrap the outer edges forward and narrow the upper shoulders.
    for v in back.data.vertices:
        v.co.y-=.035*(abs(v.co.x)/.24)**2
        if v.co.z>0:v.co.x*=1-.10*(v.co.z/.265)
    box('BackSupport',(0,.21,.60),(.10,.075,.24),role='frame')
    for x in [-.30,.30]:
        box('ArmPad',(x,-.005,.745),(.075,.36,.055),.022,1,'frame')
        box('ArmSupport',(x,.07,.625),(.035,.05,.23),role='frame')
    cylinder('LiftColumn',(0,0,.32),.035,.34,10)
    cylinder('ColumnSleeve',(0,0,.20),.053,.14,8)
    cylinder('SeatMechanism',(0,0,.47),.075,.035,8)
    for i in range(5):
        a=2*math.pi*i/5-math.pi/2;direction=Vector((math.cos(a),math.sin(a),0));end=direction*.32
        beam('Spoke_%d'%i,(direction.x*.035,direction.y*.035,.16),(end.x,end.y,.10),.045,.055)
        cylinder('CasterStem_%d'%i,(end.x,end.y,.08),.018,.065,6)
        tangent=Vector((-direction.y,direction.x,0))
        for side in [-1,1]:
            pos=end+tangent*(side*.022);pos.z=.045
            o=cylinder('Caster_%d_%d'%(i,side),pos,.045,.025,6,'wheel');o.rotation_euler=tangent.to_track_quat('Z','Y').to_euler()
    src=R/'meshy/models/original/AST-003/v001';src.mkdir(parents=True,exist_ok=True);bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'))
    m=material();parts={}
    for o in list(bpy.context.scene.objects):
        if o.type=='MESH':paint(o,m,o['palette_role']);parts[o.name]=sum(len(p.vertices)-2 for p in o.data.polygons)
    finish('v001','blender_direct',start,parts)

def meshy():
    start=time.perf_counter();bpy.ops.wm.read_factory_settings(use_empty=True);bpy.ops.import_scene.gltf(filepath=str(R/'meshy/models/original/AST-003/v002/model.glb'))
    obs=[o for o in bpy.context.scene.objects if o.type=='MESH']
    for o in obs:
        bpy.context.view_layer.objects.active=o;o.select_set(True);bpy.ops.object.transform_apply(location=True,rotation=True,scale=True)
    before=sum(len(p.vertices)-2 for o in obs for p in o.data.polygons)
    points=[v.co for o in obs for v in o.data.vertices];lo=[min(v[i] for v in points) for i in range(3)];hi=[max(v[i] for v in points) for i in range(3)];scale=1.15/(hi[2]-lo[2])
    for o in obs:
        for v in o.data.vertices:v.co=Vector(((v.co.x-(lo[0]+hi[0])/2)*scale,(v.co.y-(lo[1]+hi[1])/2)*scale,(v.co.z-lo[2])*scale))
    high=[v.co.y for o in obs for v in o.data.vertices if v.co.z>.85];flip=sum(high)/len(high)<0
    if flip:
        for o in obs:
            for v in o.data.vertices:v.co.x*=-1;v.co.y*=-1
    m=material()
    for o in obs:
        o.data.update()
        def region(p):
            c=sum((o.data.vertices[i].co for i in p.vertices),Vector())/len(p.vertices)
            if c.z>.70 and c.y>.08:return 'cushion'
            if .49<c.z<.62 and abs(c.x)<.29:return 'cushion'
            if .60<c.z<=.70 and c.y>.15 and abs(c.x)<.23:return 'cushion'
            return 'wheel' if c.z<.13 else 'frame'
        paint(o,m,region)
    finish('v002','meshy',start,{'semantic_parts':'Single Meshy mesh; spatial UV assignment, no reliable named part separation'},before)
if '--meshy-only' in sys.argv:meshy()
else:direct();meshy()

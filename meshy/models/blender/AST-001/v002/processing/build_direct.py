"""Deterministic rounded prism: direct Blender comparison and COM-02 surface."""
import bpy, bmesh, math, json, time
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[6]
mapping=json.loads((ROOT/'meshy/models/textures/palettes/v001/mapping.json').read_text(encoding='utf-8'))
def make(asset,version,name,half,radius,height,bevel,row,col):
    started=time.perf_counter()
    out=ROOT/f'meshy/models/blender/{asset}/{version}'
    src=ROOT/f'meshy/models/original/{asset}/{version}'
    for p in [out/'exports',src/'previews']: p.mkdir(parents=True,exist_ok=True)
    if (out/'model.blend').exists(): raise RuntimeError('Version already exists; preserve it.')
    bpy.ops.wm.read_factory_settings(use_empty=True)
    verts=[]; faces=[]
    rings=[(bevel,0),(0,bevel),(0,height-bevel),(bevel,height)] if bevel else [(0,0),(0,height)]
    for inset,z in rings:
        for cx,cy,start in [(1,1,0),(-1,1,90),(-1,-1,180),(1,-1,270)]:
            for step in range(7):
                a=math.radians(start+step*15)
                verts.append((cx*(half-radius)+(radius-inset)*math.cos(a),cy*(half-radius)+(radius-inset)*math.sin(a),z))
    n=28
    faces.append(tuple(reversed(range(n))))
    for ring in range(len(rings)-1):
        for i in range(n):
            j=(i+1)%n; faces.append((ring*n+i,ring*n+j,(ring+1)*n+j,(ring+1)*n+i))
    faces.append(tuple((len(rings)-1)*n+i for i in range(n)))
    mesh=bpy.data.meshes.new(name); mesh.from_pydata(verts,[],faces); mesh.update()
    obj=bpy.data.objects.new(name,mesh); bpy.context.collection.objects.link(obj); obj.select_set(True); bpy.context.view_layer.objects.active=obj
    bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'))
    mod=obj.modifiers.new('Triangulate','TRIANGULATE'); bpy.ops.object.modifier_apply(modifier=mod.name)
    cell=next(c for c in mapping['cells'] if c['texture_id']=='color1' and c['row']==row and c['column']==col)
    uv=mesh.uv_layers.new(name='PaletteUV')
    for loop in uv.data: loop.uv=cell['uv_center']
    mat=bpy.data.materials.new('SharedPalette_v001'); mat.use_nodes=True
    p=mat.node_tree.nodes.get('Principled BSDF'); p.inputs['Base Color'].default_value=(1,1,1,1); p.inputs['Roughness'].default_value=.8
    tex=mat.node_tree.nodes.new('ShaderNodeTexImage'); tex.image=bpy.data.images.load(str(ROOT/'meshy/models/textures/palettes/v001/palette.png')); tex.image.pack(); tex.interpolation='Closest'; tex.extension='EXTEND'; mat.node_tree.links.new(tex.outputs['Color'],p.inputs['Base Color']); mesh.materials.append(mat)
    bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
    glb=out/'exports/model.glb'; bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
    bpy.ops.wm.read_factory_settings(use_empty=True); bpy.ops.import_scene.gltf(filepath=str(glb))
    objects=[o for o in bpy.context.scene.objects if o.type=='MESH']
    count=sum(len(p.vertices)-2 for o in objects for p in o.data.polygons)
    closed=True
    for o in objects:
        bm=bmesh.new(); bm.from_mesh(o.data); bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=1e-6); closed &= all(e.is_manifold for e in bm.edges); bm.free()
    mats={m.name for o in objects for m in o.data.materials if m}
    imgs={n.image.name for m in bpy.data.materials if m.use_nodes for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image}
    uvok=all(abs(l.uv.x-cell['uv_center'][0])<1e-6 and abs(l.uv.y-cell['uv_center'][1])<1e-6 for o in objects for l in o.data.uv_layers.active.data)
    def passed(ok,evidence):return dict(status='pass' if ok else 'fail',evidence=evidence,reason=None)
    report=dict(schema_version=3,asset_id=asset,version=version,kind='prop',target_web_environment='Local Three.js browser; not Unity WebGL',props=[dict(name=name,triangles_per_instance=count,instance_count=1,total_triangles=count)],scene_triangles=count,material_count=len(mats),texture_count=len(imgs),palette_resolution=[2508,2508],glb_bytes=glb.stat().st_size,checks=dict(prop_budget=passed(count<=1000,'Final GLB reimport'),closed_mesh=passed(closed,'Geometric edge manifold check after normal-split weld'),palette_uv=passed(uvok,'Reimported UVs match source cell center'),shared_material=passed(len(mats)==len(imgs)==1,'Reimported material and texture nodes'),web_display=dict(status='unverified',evidence=None,reason='Pending browser check'),diorama_budget=dict(status='not_applicable',evidence=None,reason='Individual prop')),remaining_issues=['Unity not tested','Full source palette texture remains large'],generation_method='blender_direct',meshy_task_id=None,consumed_credits=0,processing_seconds_before_render=round(time.perf_counter()-started,3),dimensions_m=[half*2,half*2,height],palette_selection=cell)
    (out/'inspection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
    scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=24;scene.render.resolution_x=800;scene.render.resolution_y=600;scene.render.resolution_percentage=100
    scene.world=bpy.data.worlds.new('Preview');scene.world.use_nodes=True;scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.65,.65,.65,1);scene.world.node_tree.nodes['Background'].inputs[1].default_value=.7
    bpy.ops.object.camera_add(location=(3,-4,3));cam=bpy.context.object;cam.rotation_euler=(Vector((0,0,.08))-cam.location).to_track_quat('-Z','Y').to_euler();cam.data.type='ORTHO';cam.data.ortho_scale=3.6;scene.camera=cam
    bpy.ops.object.light_add(type='AREA',location=(-3,-4,6));bpy.context.object.data.energy=450;bpy.context.object.data.size=5
    scene.render.filepath=str(src/'previews/blender.png');bpy.ops.render.render(write_still=True)
    print('DIRECT_RESULT',asset,version,count,report['processing_seconds_before_render'],glb.stat().st_size,closed,uvok)
make('AST-001','v002','COM-01 Rounded Base Direct',1,.20,.16,.012,13,0)
# COM-02 is a reusable solid surface inset. Assemble on the base at Z=.16;
# thickness prevents coincident coplanar surfaces and allows a clean underside.
make('AST-002','v001','COM-02 Floor Surface',.96,.18,.008,0,3,5)

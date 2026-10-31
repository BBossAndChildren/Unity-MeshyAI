"""Import actual Meshy mesh, reshape radial slab, palette UV, export and reimport."""
import bpy, math, json
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[6]
OUT=ROOT/'meshy/models/blender/AST-001/v001'
OUT.mkdir(parents=True,exist_ok=True); (OUT/'exports').mkdir(exist_ok=True)
bpy.ops.wm.read_factory_settings(use_empty=True)
bpy.ops.import_scene.gltf(filepath=str(ROOT/'meshy/models/original/AST-001/v001/model.glb'))
objs=[o for o in bpy.context.scene.objects if o.type=='MESH']
assert len(objs)==1
o=objs[0]; o.name='COM-01_RoundedBase'
bpy.context.view_layer.objects.active=o; o.select_set(True)
bpy.ops.object.transform_apply(location=False,rotation=True,scale=True)
before=sum(len(p.vertices)-2 for p in o.data.polygons)
coords=[v.co.copy() for v in o.data.vertices]
lo=[min(v[i] for v in coords) for i in range(3)]; hi=[max(v[i] for v in coords) for i in range(3)]
# Meshy supplied a radial slab. Preserve topology, deform radial perimeter to
# superellipse (rounded square), flatten top/bottom, normalize to 2 x 2 x .16 m.
for v in o.data.vertices:
    x=(v.co.x-(lo[0]+hi[0])/2)/(hi[0]-lo[0])*2
    y=(v.co.y-(lo[1]+hi[1])/2)/(hi[1]-lo[1])*2
    r=math.hypot(x,y); a=math.atan2(y,x)
    target=(abs(math.cos(a))**8+abs(math.sin(a))**8)**(-1/8)
    if r>.8: r=1.0
    v.co.x=r*target*math.cos(a); v.co.y=r*target*math.sin(a)
    z=(v.co.z-lo[2])/(hi[2]-lo[2])
    v.co.z=(0 if z<.15 else 1 if z>.85 else z)*.16
o.location=(0,0,0)
bpy.ops.object.mode_set(mode='EDIT'); bpy.ops.mesh.select_all(action='SELECT')
bpy.ops.mesh.remove_doubles(threshold=.0001)
bpy.ops.mesh.convex_hull(delete_unused=True, use_existing_faces=False)
bpy.ops.mesh.normals_make_consistent(inside=False)
bpy.ops.mesh.dissolve_limited(angle_limit=math.radians(.25))
bpy.ops.object.mode_set(mode='OBJECT')
tri=o.modifiers.new('ExportTriangles','TRIANGULATE'); bpy.ops.object.modifier_apply(modifier=tri.name)
for p in o.data.polygons: p.use_smooth=False
mapping=json.loads((ROOT/'meshy/models/textures/palettes/v001/mapping.json').read_text())
cell=next(c for c in mapping['cells'] if c['texture_id']=='color1' and c['row']==13 and c['column']==0)
uv=o.data.uv_layers.active or o.data.uv_layers.new(name='PaletteUV')
for loop in uv.data: loop.uv=cell['uv_center']
mat=bpy.data.materials.new('SharedPalette_v001'); mat.use_nodes=True
bsdf=mat.node_tree.nodes.get('Principled BSDF'); bsdf.inputs['Base Color'].default_value=(1,1,1,1); bsdf.inputs['Roughness'].default_value=.8
tex=mat.node_tree.nodes.new('ShaderNodeTexImage'); tex.image=bpy.data.images.load(str(ROOT/'meshy/models/textures/palettes/v001/palette.png')); tex.interpolation='Closest'; tex.extension='EXTEND'
mat.node_tree.links.new(tex.outputs['Color'],bsdf.inputs['Base Color'])
o.data.materials.clear(); o.data.materials.append(mat)
for a in list(o.data.color_attributes): o.data.color_attributes.remove(a)
tex.image.pack()
bpy.ops.wm.save_as_mainfile(filepath=str(OUT/'model.blend'))
glb=OUT/'exports/rounded-base.glb'
bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True,export_texcoords=True,export_normals=True,export_materials='EXPORT',export_image_format='AUTO')
# Reimport the exported result; report measured counts, not requested counts.
bpy.ops.wm.read_factory_settings(use_empty=True); bpy.ops.import_scene.gltf(filepath=str(glb))
meshes=[a for a in bpy.context.scene.objects if a.type=='MESH']
count=sum(sum(len(p.vertices)-2 for p in a.data.polygons) for a in meshes)
materials={m.name for a in meshes for m in a.data.materials if m}
images={n.image.name for a in meshes for m in a.data.materials if m and m.use_nodes for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image}
checks={}
def check(key,ok,evidence): checks[key]=dict(status='pass' if ok else 'fail',evidence=evidence,reason=None)
check('prop_budget',count<=1000,f'Reimported GLB: {count} triangles')
check('palette_material',len(materials)==1 and len(images)==1,'Reimported material and image nodes counted')
check('palette_uv',all(abs(l.uv.x-cell['uv_center'][0])<1e-6 and abs(l.uv.y-cell['uv_center'][1])<1e-6 for a in meshes for l in a.data.uv_layers.active.data),'Reimported Blender UV centers match color1 row13 col0')
check('original_palette_pixels',mapping['pixel_preservation_verified'],'build_palette.py compared decoded original pixels')
import bmesh
closed=True
for a in meshes:
    bm=bmesh.new(); bm.from_mesh(a.data); bmesh.ops.remove_doubles(bm,verts=list(bm.verts),dist=1e-6); closed=closed and all(e.is_manifold for e in bm.edges); bm.free()
check('closed_mesh',closed,'Reimported geometric connectivity checked after welding coincident export normal splits at 1e-6 m')
checks['web_display']=dict(status='unverified',evidence=None,reason='Browser check pending')
checks['diorama_budget']=dict(status='not_applicable',evidence=None,reason='Single prop beta')
report=dict(schema_version=3,asset_id='AST-001',version='v001',kind='prop',target_web_environment='Local WebGL browser preview (not Unity WebGL)',props=[dict(name='COM-01 Rounded Base',triangles_per_instance=count,instance_count=1,total_triangles=count)],scene_triangles=count,material_count=len(materials),texture_count=len(images),palette_resolution=[mapping['width'],mapping['height']],glb_bytes=glb.stat().st_size,checks=checks,remaining_issues=['Browser verification pending','Unity integration not performed'],source_triangles=before,mesh_correction='Deformed original Meshy radial slab into exponent-8 rounded square; flattened surfaces. Original preserved.',palette_selection=cell)
(OUT/'inspection.json').write_text(json.dumps(report,ensure_ascii=False,indent=2),encoding='utf-8')
print('BETA_METRICS',json.dumps({'source_triangles':before,'final_triangles':count,'glb_bytes':glb.stat().st_size,'checks':checks}))
# Render only a preview; camera/lights are excluded from the saved asset.
scene=bpy.context.scene; scene.render.engine='CYCLES'; scene.cycles.samples=24
scene.render.resolution_x=800; scene.render.resolution_y=600; scene.render.resolution_percentage=100
scene.world=bpy.data.worlds.new('PreviewWorld'); scene.world.use_nodes=True; scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.65,.65,.65,1); scene.world.node_tree.nodes['Background'].inputs[1].default_value=.7
bpy.ops.object.camera_add(location=(3,-4,3)); cam=bpy.context.object; cam.rotation_euler=(Vector((0,0,.08))-cam.location).to_track_quat('-Z','Y').to_euler(); cam.data.type='ORTHO'; cam.data.ortho_scale=3.6; scene.camera=cam
bpy.ops.object.light_add(type='AREA',location=(-3,-4,6)); bpy.context.object.data.energy=450; bpy.context.object.data.shape='DISK'; bpy.context.object.data.size=5
scene.render.filepath=str(ROOT/'meshy/models/original/AST-001/v001/previews/blender.png'); bpy.ops.render.render(write_still=True)

"""Additive final-GLB presentation views for manual review, no model mutation.

Run with Blender --background --threads 2 --python ... -- [asset IDs].
Images are review evidence, never model textures or execution-pass claims.
"""
import bpy, json, hashlib, math, sys, datetime
from pathlib import Path
from mathutils import Vector

ROOT=Path(__file__).resolve().parents[6]
OUT=ROOT/'docs/machine/evidence/workplaces-model-review-v001'
SCRIPT=Path(__file__).relative_to(ROOT).as_posix()
ARGS=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
ASSETS=json.loads((ROOT/'docs/machine/catalog/assets.json').read_text('utf-8'))['assets']
TARGETS=[a for a in ASSETS if (int(a['asset_id'].split('-')[1])>=1000 if not ARGS else a['asset_id'] in ARGS or a['asset_id']+'@'+a['version'] in ARGS)]

def digest(path):return hashlib.sha256(path.read_bytes()).hexdigest()

def produce(asset):
    aid,version=asset['asset_id'],asset['version'];directory=OUT/'views'/aid/version
    done=directory/'render-evidence.json'
    if done.exists():return
    source=ROOT/asset['runtime_path'];source_hash=digest(source)
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(source))
    meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
    corners=[o.matrix_world@Vector(v) for o in meshes for v in o.bound_box]
    lo=Vector([min(v[i] for v in corners) for i in range(3)]);hi=Vector([max(v[i] for v in corners) for i in range(3)])
    center=(lo+hi)*.5;span=max(hi-lo)
    scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=2;scene.cycles.use_denoising=False
    scene.render.resolution_x=320;scene.render.resolution_y=320;scene.render.resolution_percentage=100
    scene.render.image_settings.file_format='PNG';scene.render.film_transparent=False
    scene.world=bpy.data.worlds.new('Neutral review world');scene.world.use_nodes=True
    scene.world.node_tree.nodes['Background'].inputs[0].default_value=(.34,.34,.34,1)
    scene.world.node_tree.nodes['Background'].inputs[1].default_value=.8
    # Broad illumination from both sides makes back-facing components visible.
    for offset,power in [((-2,-3,5),350),((2,3,5),300)]:
        bpy.ops.object.light_add(type='AREA',location=center+Vector(offset)*max(span,.2))
        lamp=bpy.context.object;lamp.data.energy=power*max(span,.2)**2;lamp.data.size=max(span,.2)*4
        lamp.rotation_euler=(center-lamp.location).to_track_quat('-Z','Y').to_euler()
    bpy.ops.object.camera_add();camera=bpy.context.object;camera.data.type='ORTHO';camera.data.ortho_scale=span*1.35+.1;scene.camera=camera
    views=[]
    for name,direction in [('front',(0,-1,.65)),('side',(1,0,.65)),('back',(0,1,.65))]:
        camera.location=center+Vector(direction).normalized()*(span*3+1)
        camera.rotation_euler=(center-camera.location).to_track_quat('-Z','Y').to_euler()
        directory.mkdir(parents=True,exist_ok=True);image=directory/(name+'.png');scene.render.filepath=str(image)
        bpy.ops.render.render(write_still=True)
        views.append(dict(name=name,path=image.relative_to(ROOT).as_posix(),sha256=digest(image),width=320,height=320))
    assert digest(source)==source_hash,'Final GLB changed unexpectedly'
    evidence=dict(schema_version=3,asset_id=aid,version=version,kind=asset['kind'],runtime_path=asset['runtime_path'],runtime_sha256=source_hash,script_path=SCRIPT,rendered_at=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat(),blender_version=bpy.app.version_string,source_final_glb_reopened=True,source_unchanged=True,rendered_views=views,triangles=sum(len(poly.vertices)-2 for obj in meshes for poly in obj.data.polygons),aabb_blender_m=dict(min=list(lo),max=list(hi)),manual_visual_status='unverified',note='Actual Blender renders of final GLB. Rendering does not itself establish visual quality, Unity or WebGL pass.')
    done.write_text(json.dumps(evidence,ensure_ascii=False,indent=2)+'\n','utf-8')
    print('REVIEW_VIEWS',aid,version,flush=True)

for asset in TARGETS:produce(asset)

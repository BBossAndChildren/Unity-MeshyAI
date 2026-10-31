"""Editable shared prop production recipes. Run with Blender --background --python.

No paid service, source-image generation, hook, or external deployment. Each
recipe owns an explicit candidate and preserves existing registered versions.
"""
import bpy
import math
import json
import sys
import hashlib
import datetime
from pathlib import Path
from mathutils import Vector

ROOT = Path(__file__).resolve().parents[6]
SCRIPT = Path(__file__).relative_to(ROOT).as_posix()
CAT = ROOT / 'docs/machine/catalog'
PAL = ROOT / 'meshy/models/textures/palettes/v001/palette.png'
MAPPING = json.loads(PAL.with_name('mapping.json').read_text('utf-8'))
COLORS = {'cream': (13, 0), 'wood': (3, 3), 'orange': (3, 7),
          'green': (6, 10), 'dark': (15, 12), 'black': (15, 14),
          'white': (15, 0), 'yellow': (4, 7), 'purple': (10, 8),
          'teal': (7, 8), 'pink': (1, 5), 'soil': (12, 13)}
MATERIAL = None
SUPPORTING_SCRIPTS = []

def read(name):
    return json.loads((CAT / (name + '.json')).read_text('utf-8-sig'))

def write(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + '\n', 'utf-8')

def reset():
    global MATERIAL
    bpy.ops.wm.read_factory_settings(use_empty=True)
    MATERIAL = bpy.data.materials.new('SharedPalette_v001')
    MATERIAL.use_nodes = True
    shader = MATERIAL.node_tree.nodes.get('Principled BSDF')
    shader.inputs['Base Color'].default_value = (1, 1, 1, 1)
    shader.inputs['Roughness'].default_value = .8
    texture = MATERIAL.node_tree.nodes.new('ShaderNodeTexImage')
    texture.image = bpy.data.images.load(str(PAL)); texture.image.pack()
    texture.interpolation = 'Closest'
    MATERIAL.node_tree.links.new(texture.outputs['Color'], shader.inputs['Base Color'])

def paint(obj, color):
    row, col = COLORS[color]
    cell = next(c for c in MAPPING['cells'] if c['texture_id'] == 'color1' and c['row'] == row and c['column'] == col)
    obj.data.materials.clear(); obj.data.materials.append(MATERIAL)
    layer = obj.data.uv_layers.active or obj.data.uv_layers.new(name='PaletteUV')
    for loop in layer.data: loop.uv = cell['uv_center']
    obj['palette_source'] = 'color1'; obj['palette_row'] = row; obj['palette_column'] = col
    return obj

def box(name, pos, size, color='cream', bevel=0):
    bpy.ops.mesh.primitive_cube_add(size=1, location=pos)
    obj = bpy.context.object; obj.name = name; obj.dimensions = size
    bpy.ops.object.transform_apply(location=False, rotation=False, scale=True)
    if bevel:
        mod = obj.modifiers.new('Rounded edges', 'BEVEL'); mod.width = bevel; mod.segments = 1
        bpy.ops.object.modifier_apply(modifier=mod.name)
    return paint(obj, color)

def cyl(name, pos, radius, height, color='dark', vertices=8, top=None):
    bpy.ops.mesh.primitive_cone_add(vertices=vertices, radius1=radius,
        radius2=radius if top is None else top, depth=height, location=pos)
    obj=bpy.context.object; obj.name=name
    return paint(obj,color)

def rod(name, a, b, radius=.025, color='dark', vertices=6):
    a,b=Vector(a),Vector(b)
    obj=cyl(name,(a+b)/2,radius,(b-a).length,color,vertices)
    obj.rotation_euler=(b-a).to_track_quat('Z','Y').to_euler()
    return obj

def sphere(name,pos,size,color='yellow'):
    bpy.ops.mesh.primitive_uv_sphere_add(segments=12, ring_count=6, radius=1,location=pos)
    obj=bpy.context.object; obj.name=name; obj.scale=size
    for p in obj.data.polygons:p.use_smooth=True
    return paint(obj,color)

def wheel(pos,r=.06):
    obj=cyl('Wheel',pos,r,.045,'dark',8);obj.rotation_euler.x=math.pi/2
    return obj

def legs(xs=(-.65,.65),ys=(-.32,.32),height=.7,color='purple'):
    for x in xs:
        for y in ys:rod('Leg',(x,y,0),(x,y,height),.035,color)

def table():
    box('Rounded table top',(0,0,.75),(1.65,.9,.09),'wood',.12)
    legs()

def chair():
    box('Seat',(0,0,.46),(.48,.48,.08),'teal',.035)
    box('Backrest',(0,.205,.76),(.48,.07,.53),'teal',.035)
    legs((-.18,.18),(-.18,.18),.43,'cream')

def laptop():
    box('Keyboard base',(0,0,.018),(.34,.25,.035),'dark',.008)
    box('Key field',(0,.025,.038),(.28,.12,.008),'black')
    box('Touch pad',(0,-.07,.038),(.08,.05,.008),'cream')
    screen=box('Hinged display',(0,.11,.14),(.34,.025,.24),'dark',.008)
    screen.rotation_euler.x=math.radians(-12)
    face=box('Display face',(0,.091,.14),(.30,.008,.20),'teal')
    face.rotation_euler.x=math.radians(-12)

def whiteboard():
    box('Writing surface',(0,0,1.25),(1.5,.055,.85),'white',.035)
    for x in [-.79,.79]:box('Frame upright',(x,0,1.25),(.055,.08,.94),'purple')
    for z in [.78,1.72]:box('Frame rail',(0,0,z),(1.6,.08,.055),'purple')
    for x in [-.67,.67]:
        box('Stand',(x,0,.42),(.055,.065,.75),'purple')
        box('Caster beam',(x,0,.075),(.08,.48,.055),'purple')
        for y in [-.19,.19]:wheel((x,y,.055),.055)
    box('Marker ledge',(0,-.07,.77),(1.3,.12,.035),'purple')

def note():
    box('Memo',(0,0,.003),(.12,.12,.006),'yellow')

def beanbag():
    sphere('Beanbag shell',(0,0,.30),(.48,.45,.34),'yellow')
    sphere('Back bolster',(0,.23,.47),(.42,.22,.33),'yellow')

def cart():
    for z in [.14,.49,.84]:box('Tray',(0,0,z),(.7,.43,.055),'teal',.015)
    for x in [-.31,.31]:
        for y in [-.17,.17]:
            rod('Post',(x,y,.12),(x,y,.93),.024,'teal');wheel((x,y,.06))
    rod('Handle',(-.31,.17,.93),(.31,.17,.93),.025,'teal')

def pc():
    box('Tower',(0,0,.23),(.21,.43,.46),'dark',.015)
    box('Drive',(0,-.22,.33),(.15,.012,.03),'black')
    cyl('Power button',(.06,-.229,.40),.012,.008,'white',8).rotation_euler.x=math.pi/2
    for z in [.10,.14,.18]:box('Vent',(0,-.22,z),(.13,.008,.012),'black')

def phone():
    box('Telephone base',(0,0,.045),(.24,.20,.09),'cream',.015)
    box('Handset',(-.07,0,.12),(.07,.23,.05),'dark',.018)
    for x in [.01,.05,.09]:
        for y in [-.055,-.015,.025]:box('Key',(x,y,.095),(.025,.025,.012),'dark')

def stamp():
    box('Stamp base',(0,0,.025),(.085,.06,.05),'wood')
    cyl('Grip',(0,0,.09),.024,.10,'dark')

def inkpad():
    box('Case',(0,0,.015),(.14,.10,.03),'dark')
    box('Ink surface',(0,0,.033),(.12,.08,.012),'pink')

def binder():
    box('Folder',(0,0,.025),(.26,.32,.05),'purple')
    box('Spine',(-.125,0,.03),(.025,.32,.07),'dark')
    box('Pages',(.01,0,.026),(.22,.30,.038),'white')

def counter():
    box('Counter body',(0,0,.48),(1.65,.65,.96),'teal')
    box('Countertop',(0,0,1.01),(1.8,.78,.10),'wood',.035)
    box('Visitor shelf',(0,-.42,.76),(1.7,.25,.055),'cream')

def ticket():
    box('Base',(0,0,.045),(.38,.36,.09),'dark',.025)
    box('Pedestal',(0,0,.57),(.17,.16,1.05),'cream')
    box('Display housing',(0,-.03,1.18),(.41,.19,.32),'purple',.025)
    box('Touch screen',(0,-.13,1.20),(.32,.012,.20),'teal')
    box('Ticket slot',(0,-.135,1.055),(.17,.015,.025),'black')

def waiting():
    rod('Cross beam',(-.8,0,.35),(.8,0,.35),.045)
    for x in [-.53,0,.53]:
        box('Seat',(x,-.05,.46),(.46,.46,.07),'teal',.025)
        box('Back',(x,.16,.73),(.46,.07,.50),'teal',.025)
    legs((-.62,.62),(-.17,.17),.35)

def brochure():
    box('Foot',(0,0,.025),(.4,.30,.05),'cream')
    rod('Stand',(0,0,.05),(0,0,.85),.035,'purple')
    for z in [.6,.82,1.04]:
        box('Sloping pocket',(0,0,z),(.38,.08,.23),'teal')
        box('Pocket lip',(0,-.06,z-.08),(.38,.06,.065),'cream')

def file():
    for x,c in [(-.09,'teal'),(0,'purple'),(.09,'yellow')]:
        box('File',(x,0,.16),(.065,.25,.32),c)
        box('Spine label',(x,-.13,.22),(.035,.008,.10),'white')

def shelf():
    for x in [-.57,.57]:box('Side',(x,0,.8),(.06,.38,1.6),'wood')
    for z in [.08,.58,1.08,1.57]:box('Shelf',(0,0,z),(1.2,.40,.055),'wood')
    box('Back',(0,.19,.8),(1.2,.03,1.6),'cream')

def scales():
    box('Base',(0,0,.025),(.35,.18,.05),'wood')
    rod('Pillar',(0,0,.05),(0,0,.6),.023,'yellow')
    rod('Beam',(-.22,0,.55),(.22,0,.55),.018,'yellow')
    for x in [-.21,.21]:
        rod('Suspension',(x,0,.55),(x,0,.28),.009,'yellow')
        cyl('Scale pan',(x,0,.26),.12,.025,'yellow',10)

def banker():
    cyl('Foot',(0,0,.025),.12,.05,'wood',10)
    rod('Stem',(0,0,.05),(0,0,.39),.02,'wood')
    obj=cyl('Shade',(0,0,.43),.09,.29,'green',10);obj.rotation_euler.y=math.pi/2

def labbench():
    box('Worktop',(0,0,.86),(1.7,.72,.08),'cream')
    for x in [-.57,.57]:box('Storage module',(x,0,.42),(.5,.65,.84),'teal')
    for x in [-.57,.57]:
        for z in [.22,.62]:box('Handle',(x,-.34,z),(.17,.03,.025),'dark')

def sink():
    box('Cabinet',(0,0,.4),(.82,.6,.8),'teal')
    box('Counter',(0,0,.83),(.90,.68,.06),'cream')
    box('Basin bottom',(0,0,.80),(.53,.4,.025),'dark')
    for x in [-.30,.30]:box('Basin rim',(x,0,.86),(.05,.48,.06),'white')
    for y in [-.22,.22]:box('Basin rim',(0,y,.86),(.6,.04,.06),'white')
    rod('Faucet',(0,.25,.84),(0,.25,1.12),.025,'dark')
    rod('Spout',(0,.25,1.12),(0,.02,1.12),.025,'dark')

def equipment():
    box('Equipment case',(0,0,.5),(.8,.45,1),'cream',.025)
    for x in [-.2,.2]:
        box('Door',(x,-.24,.50),(.36,.025,.9),'teal')
        box('Handle',(x*.35,-.27,.52),(.035,.03,.19),'dark')

def microscope():
    box('Foot',(0,0,.03),(.26,.30,.06),'cream',.02)
    rod('Arm',(0,.10,.05),(0,.10,.37),.045,'cream')
    box('Stage',(0,-.01,.23),(.22,.20,.028),'dark')
    rod('Optical barrel',(0,.06,.42),(0,-.07,.31),.04,'dark')
    rod('Eyepiece',(0,.06,.42),(0,.13,.48),.025,'dark')
    cyl('Focus knob',(.08,.10,.29),.04,.05,'dark').rotation_euler.y=math.pi/2

def tray():
    box('Tray floor',(0,0,.012),(.38,.28,.024),'cream')
    for x in [-.19,.19]:box('Side lip',(x,0,.04),(.025,.30,.07),'teal')
    for y in [-.14,.14]:box('End lip',(0,y,.04),(.38,.025,.07),'teal')

def medicalbed():
    box('Mattress',(0,0,.68),(.75,1.85,.14),'cream',.04)
    box('Base',(0,0,.53),(.70,1.75,.10),'teal')
    for x in [-.28,.28]:
        for y in [-.7,.7]:rod('Leg',(x,y,.09),(x,y,.5),.035,'cream');wheel((x,y,.07))
    box('Pillow',(0,.64,.79),(.56,.36,.09),'white',.025)

def medmonitor():
    box('Housing',(0,0,.23),(.42,.16,.34),'cream',.02)
    box('Readout',(0,-.087,.25),(.33,.012,.23),'dark')
    box('Foot',(0,0,.035),(.3,.22,.07),'cream')
    for x in [-.11,0,.11]:box('Control',(x,-.09,.09),(.045,.018,.025),'teal')

def worklight():
    cyl('Base',(0,0,.035),.22,.07,'cream',10)
    rod('Stand',(0,0,.07),(0,0,1.35),.026,'cream')
    rod('Arm',(0,0,1.35),(-.35,0,1.65),.025,'cream')
    cyl('Lamp head',(-.35,0,1.59),.19,.09,'cream',10)
    cyl('Light face',(-.35,0,1.54),.15,.014,'white',10)

def bed():
    box('Frame',(0,0,.25),(.95,1.9,.18),'wood')
    box('Mattress',(0,0,.42),(.9,1.85,.18),'cream',.035)
    box('Blanket',(0,-.3,.525),(.88,1.15,.055),'purple')
    box('Pillow',(0,.63,.56),(.65,.37,.12),'white',.03)
    for y in [-.97,.97]:box('End board',(0,y,.5),(1,.07,.8),'wood')

def bedside():
    box('Body',(0,0,.28),(.43,.4,.56),'wood')
    box('Top',(0,0,.59),(.48,.45,.055),'cream')
    for z in [.17,.42]:box('Drawer',(0,-.21,z),(.39,.02,.2),'cream');box('Grip',(0,-.23,z),(.12,.025,.02),'dark')

def documenttray():
    for z in [.025,.115]:
        box('Shelf',(0,0,z),(.28,.34,.025),'purple')
        for x in [-.14,.14]:box('Side',(x,0,z+.03),(.018,.34,.07),'purple')
    box('Back',(0,.16,.10),(.29,.02,.2),'purple')

def book():
    box('Pages',(0,0,.025),(.22,.28,.045),'white')
    for z in [.002,.05]:box('Cover',(0,0,z),(.23,.29,.008),'teal')
    box('Spine',(-.115,0,.026),(.012,.29,.055),'teal')

def locker():
    box('Case',(0,0,.90),(.88,.46,1.8),'cream')
    for x in [-.22,.22]:
        box('Door',(x,-.24,.92),(.41,.025,1.7),'teal')
        box('Handle',(x+.12,-.265,.9),(.03,.025,.17),'dark')
        for z in [1.45,1.5,1.55]:box('Vent',(x,-.26,z),(.22,.008,.012),'dark')

def workbench():
    box('Worktop',(0,0,.83),(1.6,.72,.10),'wood',.025)
    legs((-.65,.65),(-.27,.27),.78,'dark')
    box('Lower shelf',(0,0,.23),(1.4,.57,.05),'teal')

def stool():
    cyl('Seat',(0,0,.49),.24,.07,'yellow',12)
    for i in range(4):
        a=i*math.tau/4
        rod('Leg',(.21*math.cos(a),.21*math.sin(a),.02),(.14*math.cos(a),.14*math.sin(a),.46),.025,'cream')

def storagebox():
    box('Box',(0,0,.17),(.46,.34,.34),'yellow',.015)
    box('Lid',(0,0,.35),(.49,.37,.035),'wood')
    box('Label',(0,-.177,.2),(.18,.008,.08),'white')

def rug():
    box('Rug',(0,0,.012),(2.3,1.8,.024),'purple',.12)

def vise():
    box('Base',(0,0,.045),(.3,.22,.09),'teal')
    box('Fixed jaw',(0,.06,.16),(.26,.065,.20),'dark')
    box('Moving jaw',(0,-.10,.16),(.26,.065,.20),'dark')
    rod('Lead screw',(0,-.26,.11),(0,.10,.11),.025,'cream')
    rod('Handle',(-.10,-.25,.11),(.10,-.25,.11),.014,'cream')

def toolbox():
    box('Box',(0,0,.13),(.46,.25,.26),'orange',.02)
    box('Lid',(0,0,.27),(.47,.26,.04),'dark')
    for x in [-.11,.11]:rod('Handle riser',(x,0,.29),(x,0,.37),.018,'dark')
    rod('Handle',(-.11,0,.37),(.11,0,.37),.02,'dark')
    for x in [-.14,.14]:box('Latch',(x,-.14,.23),(.04,.015,.07),'cream')

def camera():
    box('Body',(0,0,.12),(.29,.13,.20),'dark',.02)
    obj=cyl('Lens',(0,-.11,.12),.075,.13,'dark',12);obj.rotation_euler.x=math.pi/2
    obj=cyl('Glass',(0,-.18,.12),.058,.012,'teal',12);obj.rotation_euler.x=math.pi/2
    box('Viewfinder',(0,0,.245),(.1,.09,.05),'dark')

def lightstand():
    rod('Pole',(0,0,.08),(0,0,1.6),.025,'dark')
    for i in range(3):
        a=i*math.tau/3
        rod('Tripod leg',(0,0,.3),(.35*math.cos(a),.35*math.sin(a),.035),.02,'dark')
    box('Light panel',(0,0,1.65),(.55,.10,.42),'dark')
    box('Diffuser',(0,-.058,1.65),(.49,.012,.36),'white')

def case():
    box('Case',(0,0,.18),(.6,.37,.36),'dark',.035)
    for x in [-.19,.19]:box('Buckle',(x,-.20,.23),(.05,.025,.10),'cream')
    rod('Handle',(-.12,0,.42),(.12,0,.42),.02,'cream')
    for x in [-.12,.12]:rod('Handle post',(x,0,.34),(x,0,.42),.018,'cream')

def headphones():
    for x in [-.12,.12]:
        sphere('Ear cushion',(x,0,.12),(.035,.085,.10),'dark')
        rod('Band side',(x,0,.12),(x,0,.30),.018,'purple')
    rod('Headband',(-.12,0,.30),(.12,0,.30),.023,'purple')

def speaker():
    box('Enclosure',(0,0,.22),(.27,.23,.44),'dark',.02)
    for z,rad in [(.15,.085),(.33,.04)]:
        obj=cyl('Driver',(0,-.123,z),rad,.016,'black',12);obj.rotation_euler.x=math.pi/2
        sphere('Driver cap',(0,-.137,z),(rad*.32,.012,rad*.32),'cream')

def bench():
    for y in [-.14,0,.14]:box('Seat slat',(0,y,.45),(1.45,.11,.065),'wood',.012)
    for z in [.68,.85]:box('Back slat',(0,.22,z),(1.45,.055,.13),'wood',.012)
    for x in [-.58,.58]:
        rod('Back support',(x,.20,.1),(x,.20,.94),.028,'dark')
        rod('Front leg',(x,-.18,.02),(x,-.18,.43),.035,'dark')

def handcart():
    box('Loading plate',(0,-.12,.055),(.48,.39,.07),'teal')
    for x in [-.2,.2]:rod('Frame',(x,.06,.10),(x,.06,1.02),.028,'teal');wheel((x,.06,.10),.10)
    for z in [.4,.7,1.02]:rod('Crossbar',(-.2,.06,z),(.2,.06,z),.023,'teal')

def terrain():
    sphere('Low terrain',(0,0,0),(.95,.75,.20),'green')

def cleaning():
    cyl('Bucket',(0,0,.15),.14,.30,'teal',10,top=.18)
    rod('Mop pole',(.25,0,.03),(.25,0,1.25),.018,'wood')
    box('Mop head',(.25,0,.025),(.32,.13,.05),'cream')
    rod('Broom pole',(-.28,0,.12),(-.28,0,1.28),.018,'wood')
    box('Bristles',(-.28,0,.09),(.22,.07,.18),'yellow')

def lifebuoy():
    bpy.ops.mesh.primitive_torus_add(major_segments=16, minor_segments=6, major_radius=.23,minor_radius=.065,location=(0,0,.065))
    obj=bpy.context.object;obj.name='Life ring';paint(obj,'orange')

def radio():
    box('Radio',(0,0,.14),(.13,.07,.28),'dark',.012)
    rod('Antenna',(-.04,0,.27),(-.04,0,.48),.008,'dark')
    box('Screen',(0,-.04,.20),(.09,.012,.07),'teal')
    for z in [.07,.10,.13]:box('Speaker slot',(0,-.04,z),(.08,.01,.01),'black')

def exercise_mat():
    box('Exercise mat',(0,0,.017),(1.8,.65,.034),'teal',.07)

def sign():
    box('Foot',(0,0,.025),(.55,.4,.05),'dark')
    rod('Stand',(0,0,.05),(0,0,1.18),.03,'purple')
    box('Sign panel',(0,0,1.34),(.85,.07,.46),'cream',.025)
    box('Inset',(0,-.043,1.34),(.73,.012,.34),'teal')

def suitcase():
    box('Shell',(0,0,.32),(.43,.25,.58),'purple',.04)
    for x in [-.13,.13]:wheel((x,0,.045),.045);rod('Handle rail',(x,0,.60),(x,0,.86),.013,'dark')
    rod('Grip',(-.13,0,.86),(.13,0,.86),.022,'dark')
    for x in [-.12,0,.12]:box('Raised rib',(x,-.13,.34),(.025,.016,.4),'teal')

def pew():
    box('Seat',(0,0,.44),(2.1,.48,.08),'wood',.025)
    box('Back',(0,.22,.75),(2.1,.07,.61),'wood',.02)
    for x in [-.94,.94]:box('End panel',(x,0,.42),(.09,.59,.84),'wood',.02)
    box('Book rest',(0,-.32,.69),(1.8,.14,.045),'wood')

RECIPES={10:table,11:chair,12:laptop,13:whiteboard,14:note,15:beanbag,16:cart,17:pc,
19:phone,20:stamp,21:inkpad,22:binder,23:counter,24:ticket,25:waiting,26:brochure,
27:file,28:shelf,29:scales,30:banker,31:labbench,36:sink,37:equipment,39:microscope,
40:tray,41:medicalbed,42:medmonitor,43:worklight,44:bed,45:bedside,49:documenttray,
53:book,54:locker,55:workbench,56:stool,58:storagebox,67:rug,79:vise,80:toolbox,
109:camera,111:lightstand,114:case,117:headphones,120:speaker,127:bench,133:handcart,
139:terrain,163:cleaning,168:lifebuoy,175:radio,179:exercise_mat,205:sign,221:suitcase,247:pew}

def render_preview(path):
    meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
    corners=[o.matrix_world@Vector(c) for o in meshes for c in o.bound_box]
    lo=Vector([min(v[i] for v in corners) for i in range(3)])
    hi=Vector([max(v[i] for v in corners) for i in range(3)])
    center=(lo+hi)/2;span=max(hi-lo)*1.5+.25
    scene=bpy.context.scene;scene.render.engine='CYCLES';scene.cycles.samples=8
    scene.render.resolution_x=512;scene.render.resolution_y=512;scene.render.resolution_percentage=100
    scene.world=bpy.data.worlds.new('Preview world');scene.world.use_nodes=True
    scene.world.node_tree.nodes['Background'].inputs[1].default_value=.65
    bpy.ops.object.light_add(type='AREA',location=center+Vector((-3,-4,6)))
    bpy.context.object.data.energy=550;bpy.context.object.data.size=5
    bpy.ops.object.camera_add(location=center+Vector((span,-span,span*.8)))
    camera=bpy.context.object;camera.rotation_euler=(center-camera.location).to_track_quat('-Z','Y').to_euler()
    camera.data.type='ORTHO';camera.data.ortho_scale=span;scene.camera=camera
    scene.render.image_settings.file_format='PNG';scene.render.filepath=str(path)
    bpy.ops.render.render(write_still=True)

def produce(number):
    candidates=read('workplace-asset-candidates-v003')['candidates']
    candidate=next(c for c in candidates if c['candidate_id']==f'CND-{number:03}')
    aid=f'AST-{1000+number}';version='v001'
    dst=ROOT/f'meshy/models/blender/{aid}/{version}';src=ROOT/f'meshy/models/original/{aid}/{version}'
    if (dst/'inspection.json').exists():
        print('PRESERVED',aid,flush=True);return
    if (src/'source.blend').exists() or (dst/'model.blend').exists():
        raise RuntimeError(f'Partial {aid} exists: preserve and inspect before retry')
    reset();RECIPES[number]();objects=[o for o in bpy.context.scene.objects if o.type=='MESH']
    bpy.ops.object.select_all(action='DESELECT')
    for obj in objects:
        obj.select_set(True);bpy.context.view_layer.objects.active=obj
        mod=obj.modifiers.new('Final triangulation','TRIANGULATE');bpy.ops.object.modifier_apply(modifier=mod.name)
    corners=[o.matrix_world@Vector(c) for o in objects for c in o.bound_box]
    dimensions=[max(v[i] for v in corners)-min(v[i] for v in corners) for i in range(3)]
    parts=[dict(part_id=o.name,triangles=len(o.data.polygons),palette_source=o['palette_source'],row=o['palette_row'],column=o['palette_column']) for o in objects]
    if sum(p['triangles'] for p in parts)>1000:raise RuntimeError(f'{aid} exceeds prop budget')
    (dst/'exports').mkdir(parents=True,exist_ok=True);(src/'previews').mkdir(parents=True,exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'))
    bpy.ops.wm.save_as_mainfile(filepath=str(dst/'model.blend'))
    glb=dst/'exports/model.glb'
    bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
    bpy.ops.export_scene.fbx(filepath=str(dst/'exports/model.fbx'),use_selection=True,add_leaf_bones=False,bake_anim=False,axis_forward='-Z',axis_up='Y',path_mode='STRIP',use_custom_props=True)
    reset();bpy.ops.import_scene.gltf(filepath=str(glb))
    objects=[o for o in bpy.context.scene.objects if o.type=='MESH']
    triangles=sum(len(p.vertices)-2 for o in objects for p in o.data.polygons)
    materials={m for o in objects for m in o.data.materials}
    images={n.image for m in materials for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image}
    expected=[c['uv_center'] for c in MAPPING['cells'] if c['texture_id']=='color1']
    uvok=all(o.data.uv_layers.active and all(any(abs(l.uv.x-u)<1e-5 and abs(l.uv.y-v)<1e-5 for u,v in expected) for l in o.data.uv_layers.active.data) for o in objects)
    check=lambda value,evidence:dict(status='pass' if value else 'fail',evidence=evidence,reason=None)
    unverified=lambda why:dict(status='unverified',evidence=None,reason=why)
    report=dict(schema_version=3,asset_id=aid,version=version,kind='prop',target_web_environment='Unity room browser; per-room HTTP execution pending',props=[dict(name=candidate['name'],triangles_per_instance=triangles,instance_count=1,total_triangles=triangles)],scene_triangles=triangles,material_count=len(materials),texture_count=len(images),palette_resolution=[MAPPING['width'],MAPPING['height']],glb_bytes=glb.stat().st_size,dimensions_m=dimensions,part_regions=parts,checks=dict(prop_budget=check(triangles<=1000,'Final GLB reopened in Blender'),palette_uv=check(uvok,'Every reimported UV loop matches a color1 source cell center'),shared_material=check(len(materials)==1 and len(images)==1,'Final GLB material/image nodes'),visual_front_side_back=unverified('Preview produced; explicit front/side/back review pending'),web_display=unverified('HTTP runtime display pending'),unity=unverified('Not imported into Unity yet')),remaining_issues=['Per-part visual color/layout review pending.','Unity, WebGL, reduced display and actual mobile execution not yet checked.'],generation_method='blender_direct',meshy_credits_used=0)
    write(dst/'inspection.json',report)
    render_preview(src/'previews/front.png')
    rel=lambda p:p.relative_to(ROOT).as_posix()
    entry=dict(asset_id=aid,version=version,name=candidate['name'],source_path=rel(src/'source.blend'),blender_path=rel(dst/'model.blend'),runtime_path=rel(glb),preview_path=rel(src/'previews/front.png'),unity_path=None,kind='prop',palette_version='v001',accent_reason=None,unity_palette_path=None,inspection_path=rel(dst/'inspection.json'),processing_paths=[SCRIPT]+SUPPORTING_SCRIPTS,status='in_progress',generation_method='blender_direct',generation_reason='Explicit parameterized parts, repeated or symmetric construction; preserve editable part names, reuse shared palette and production functions.',production_record_path=rel(src/'README.md'),meshy_credits_used=0)
    source=f'# {aid} {version} — {candidate["name"]}\n\nBlender 직접 제작. Meshy 호출·작업 ID 없음, 이번 크레딧 0. 제작일 2026-10-31.\n\n후보 {candidate["candidate_id"]}, recipe {RECIPES[number].__name__}. 정확한 부품 구성·치수는 inspection.json의 part_regions/dimensions_m. 미터 단위 디자인 치수이며 실물 측정값이 아니다.\n\n형태 특성: 반복·대칭·명확한 부품 구조. 공용 팔레트 v001·color1 출처만 UV로 사용. color2 미사용. 스크립트 {SCRIPT}. 기존 기본 도형·rod·팔레트 처리 패턴을 재사용한다. 원본과 수정본을 별도 보존한다.\n\n사용 조건은 프로젝트 제공 자료 기준이며 외부 권리 독립 검증 없음. 최종 GLB 실제 Blender 재가져오기 후 삼각형·UV·재질 검사. 전체 방향·실제 웹 표시는 미검증. 이 모델을 ready로 표시하지 않는다.\n\n다음 개선: 공간 안 실제 크기·배치·색상을 검수하고 상호작용에 필요한 피벗·콜라이더를 구체화한다. 토큰·작업별 인건 시간은 미측정.\n'
    (src/'README.md').write_text(source,'utf-8')
    catalog=read('assets');assert not any(a['asset_id']==aid and a['version']==version for a in catalog['assets'])
    catalog['assets'].append(entry);write(CAT/'assets.json',catalog)
    full=candidate['full_scene_candidates']
    lines=[f'# {aid} {version} — {candidate["name"]}','','후보 '+candidate['candidate_id']+'. 상태: in_progress. 실제 원본·Blender·GLB·FBX와 미리보기를 제작했다. 웹 검수 미검증.','',f'제작 기록: [{aid} README](../../../{rel(src/"README.md")}).',f'검사: [{aid} inspection](../../../{rel(dst/"inspection.json")}).',f'재사용 스크립트: `{SCRIPT}`. Blender 직접 제작이며 유료 호출 0·이번 크레딧 0. color1만 사용, color2 사유 해당 없음.','',f'디자인 치수(Blender x/y/z 미터): {dimensions}. 부품: '+', '.join(p['part_id'] for p in parts)+'.',f'최종 재가져온 GLB {triangles}삼각형, {len(materials)}재질, {len(images)}텍스처, {glb.stat().st_size}바이트. 팔레트 v001 유지.','','## 전체 적용 후보 — 고정 v003 조회','','| 공간 | prompt ID·버전 | panorama ID·버전 | context ID·버전 | 수량 |','|---|---|---|---|---|']
    for s in full:
        pr=s['prompt_ref'];pan=s.get('panorama_ref');contexts=s.get('context_refs',[])
        lines.append(f'| {s["name"]} | {pr["prompt_id"]} {pr["version"]} | '+(f'{pan["image_id"]} {pan["version"]}' if pan else '미등록')+' | '+(', '.join(f'{c["context_id"]} {c["version"]}' for c in contexts) or '미등록')+' | 미정 |')
    lines+=['','## 실제 사용 이력','','실제 사용 이력 미등록/미검증. 이 표는 asset-usages.json·scene-assemblies.json 조회로 갱신하며 독립 배치 원장으로 사용하지 않는다. 후보 공간 수와 실제 배치 수량을 혼동하지 않는다.','','## 검수와 남은 일','','GLB를 실제 Blender로 다시 열어 삼각형·UV·공용 재질/이미지를 검사했다. 전체 방향·축소 상태·부위별 색상·Unity·HTTP WebGL 실행은 미검증. 기존 사무실 실행 pass를 승계하지 않는다.']
    doc=ROOT/f'docs/human/assets/{aid}-{version}.md';doc.write_text('\n'.join(lines)+'\n','utf-8')
    progress=read('workplace-production-v001')
    for row in progress['candidates']:
        if row['candidate_id']==candidate['candidate_id']:
            row.update(result_asset_ref={'asset_id':aid,'version':version},status='model_produced_web_unverified',document_path=rel(doc),inspection_path=rel(dst/'inspection.json'))
    progress['updated_at']=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat()
    write(CAT/'workplace-production-v001.json',progress)
    print('PRODUCED',aid,candidate['candidate_id'],triangles,glb.stat().st_size,flush=True)

if __name__=='__main__':
    args=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
    numbers=[int(x) for x in args] if args else sorted(RECIPES)
    for number in numbers:produce(number)

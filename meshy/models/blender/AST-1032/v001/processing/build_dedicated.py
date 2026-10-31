"""Explicit dedicated workplace prop recipes; shared palette and shape helpers.

Every candidate below has a named physical construction. No default box for
unknown candidates; the caller must request a recipe that actually exists.
"""
import bpy, math, importlib.util, sys
from pathlib import Path
from mathutils import Vector
ROOT=Path(__file__).resolve().parents[6]
SUPPORT='meshy/models/blender/AST-1010/v001/processing/build_shared.py'
spec=importlib.util.spec_from_file_location('shared',ROOT/SUPPORT)
s=importlib.util.module_from_spec(spec);spec.loader.exec_module(s)
s.SCRIPT=Path(__file__).relative_to(ROOT).as_posix();s.SUPPORTING_SCRIPTS=[SUPPORT]
box,cyl,rod,sphere=s.box,s.cyl,s.rod,s.sphere

def instance(fn,pos=(0,0,0),scale=(1,1,1),rotation=0):
    before=set(bpy.context.scene.objects);fn()
    a=math.radians(rotation)
    for obj in set(bpy.context.scene.objects)-before:
        x,y,z=obj.location;x*=scale[0];y*=scale[1];z*=scale[2]
        obj.location=(x*math.cos(a)-y*math.sin(a)+pos[0],x*math.sin(a)+y*math.cos(a)+pos[1],z+pos[2])
        obj.scale=Vector(obj.scale)*Vector(scale);obj.rotation_euler.z+=a

def ico(name,pos,scale,color='green'):
    bpy.ops.mesh.primitive_ico_sphere_add(subdivisions=1,radius=1,location=pos)
    obj=bpy.context.object;obj.name=name;obj.scale=scale;return s.paint(obj,color)

def tubes():
    box('Rack',(0,0,.06),(.38,.16,.12),'cream')
    for x in [-.12,-.04,.04,.12]:cyl('Tube',(x,0,.16),.021,.22,'teal',6)

def beaker():
    cyl('Beaker',(0,0,.09),.07,.18,'cream',10)
    cyl('Liquid',(0,0,.185),.057,.008,'teal',10)
    rod('Spout',(.04,0,.18),(.085,0,.19),.018,'cream')

def pipettes():
    box('Foot',(0,0,.015),(.24,.12,.03),'cream')
    rod('Rack',(0,0,.03),(0,0,.31),.017,'dark')
    rod('Rail',(-.1,0,.31),(.1,0,.31),.014,'dark')
    for x in [-.08,0,.08]:rod('Pipette',(x,-.02,.11),(x,-.02,.34),.012,'white');cyl('Grip',(x,-.02,.30),.019,.07,'teal',6)

def balance():
    box('Instrument',(0,0,.045),(.26,.25,.09),'cream',.015)
    cyl('Weighing pan',(0,.02,.105),.095,.025,'dark',12)
    box('Readout',(0,-.13,.05),(.16,.014,.04),'teal')

def analyzer():
    box('Analysis cabinet',(0,0,.57),(1.25,.65,1.14),'cream',.025)
    box('Sample chamber',(-.23,-.34,.64),(.55,.03,.70),'dark')
    box('Chamber window',(-.23,-.36,.67),(.40,.02,.45),'teal')
    box('Readout',(.37,-.34,.88),(.30,.025,.23),'teal')
    box('Sample drawer',(.37,-.35,.37),(.32,.04,.22),'cream')

def armchair():
    box('Cushion',(0,0,.43),(.62,.58,.19),'green',.06)
    box('Back',(0,.23,.72),(.65,.18,.55),'green',.06)
    for x in [-.32,.32]:box('Arm',(x,0,.60),(.15,.62,.24),'green',.045)
    s.legs((-.22,.22),(-.2,.2),.34,'wood')

def overbed():
    box('Table top',(0,0,.9),(.8,.48,.055),'wood',.025)
    rod('Side post',(.32,0,.08),(.32,0,.88),.035,'cream')
    rod('Base rail',(-.3,0,.07),(.35,0,.07),.03,'cream')
    for x in [-.27,.27]:
        rod('Foot',(x,-.22,.06),(x,.22,.06),.022,'cream')
        for y in [-.2,.2]:s.wheel((x,y,.045),.045)

def callbutton():
    box('Wall-free call panel',(0,0,.06),(.12,.07,.12),'cream',.012)
    cyl('Call button',(0,-.04,.075),.023,.012,'orange',10).rotation_euler.x=math.pi/2

def studentdesk():instance(s.table,scale=(.48,.58,.87))
def teacherdesk():
    box('Desk body',(0,0,.43),(1.2,.55,.86),'wood')
    box('Desk top',(0,0,.91),(1.32,.66,.10),'cream',.02)
def blackboard():
    box('Board',(0,0,1.22),(2.1,.08,1.03),'green')
    for x in [-1.08,1.08]:box('Frame',(x,0,1.22),(.06,.12,1.15),'wood')
    for z in [.66,1.79]:box('Rail',(0,0,z),(2.2,.12,.06),'wood')
    for x in [-.85,.85]:rod('Post',(x,0,.05),(x,0,.70),.035,'wood');rod('Foot',(x,-.25,.05),(x,.25,.05),.035,'wood')

def kit():
    box('Assembly board',(0,0,.025),(.48,.34,.05),'teal')
    for x in [-.13,.13]:
        for y in [-.08,.08]:cyl('Connection peg',(x,y,.10),.035,.15,'yellow',6)
    rod('Cross member',(-.13,-.08,.19),(.13,.08,.19),.022,'wood')

def lectern():
    box('Foot',(0,0,.035),(.6,.45,.07),'wood')
    box('Body',(0,0,.55),(.36,.3,.98),'wood')
    obj=box('Reading top',(0,0,1.07),(.65,.46,.06),'wood');obj.rotation_euler.x=math.radians(12)
def presentation():
    box('Screen',(0,0,1.25),(2,.06,1.2),'white')
    rod('Stand',(0,0,.10),(0,0,.65),.03,'dark')
    for x in [-.7,.7]:rod('Foot',(0,0,.15),(x,0,.03),.022,'dark')
def av():
    box('Projector',(0,0,.065),(.36,.28,.13),'cream',.015)
    cyl('Lens',(.08,-.15,.065),.045,.025,'dark',10).rotation_euler.x=math.pi/2
def tissues():
    box('Tissue box',(0,0,.055),(.23,.13,.11),'cream',.012)
    box('Slot',(0,0,.115),(.13,.025,.008),'dark')
    box('Tissue',(0,0,.15),(.10,.012,.08),'white')
def notebook():instance(s.book,scale=(.85,.85,.6))
def activity():
    box('Activity board',(0,0,.02),(.45,.4,.04),'cream')
    for i,color in enumerate(['yellow','teal','purple']):
        cyl('Sorting cup',((i-1)*.13,.09,.07),.045,.10,color,8)
        ico('Sorting piece',((i-1)*.13,-.09,.07),(.045,.045,.045),color)
def walker():
    for x in [-.28,.28]:
        for y in [-.23,.23]:rod('Leg',(x,y,.03),(x,y,.86),.022,'cream')
        rod('Hand grip',(x,-.23,.86),(x,.23,.86),.03,'green')
    rod('Front rail',(-.28,.23,.72),(.28,.23,.72),.022,'cream')
def wheelchair():
    instance(s.chair,scale=(1,1,.95))
    for x in [-.31,.31]:
        obj=cyl('Rear wheel',(x,.12,.30),.29,.035,'dark',12);obj.rotation_euler.y=math.pi/2
        obj=cyl('Push rim',(x*1.08,.12,.30),.23,.012,'cream',12);obj.rotation_euler.y=math.pi/2
        s.wheel((x,-.30,.07),.07)
        rod('Armrest',(x,-.18,.69),(x,.22,.69),.025,'dark')
    box('Footplate',(0,-.42,.12),(.38,.2,.035),'dark')
def rail():
    for x in [-.6,.6]:cyl('Foot',(x,0,.025),.09,.05,'cream');rod('Post',(x,0,.05),(x,0,.9),.025,'cream')
    rod('Handrail',(-.65,0,.9),(.65,0,.9),.035,'wood')
def machine():
    box('Machine',(0,0,.7),(1.1,.8,1.4),'cream',.025)
    box('Cabinet window',(0,-.415,.86),(.64,.025,.7),'dark')
    box('Workpiece',(0,-.44,.65),(.24,.03,.20),'teal')
    box('Control panel',(.43,-.44,.95),(.18,.06,.4),'teal')
    cyl('Warning lamp',(0,0,1.49),.08,.14,'yellow',8)
def conveyor():
    s.legs((-.72,.72),(-.23,.23),.65,'cream')
    box('Belt',(0,0,.69),(1.65,.6,.08),'dark')
    for x in [-.76,-.55,-.33,-.11,.11,.33,.55,.76]:
        obj=cyl('Roller',(x,0,.70),.052,.62,'cream',8);obj.rotation_euler.x=math.pi/2
def hopper():
    box('Bin bottom',(0,0,.06),(.56,.43,.12),'teal')
    for x in [-.29,.29]:box('Bin side',(x,0,.22),(.045,.48,.38),'teal')
    for y in [-.22,.22]:box('Bin end',(0,y,.22),(.56,.045,.38),'teal')
def productbox():instance(s.storagebox,scale=(1.4,1.3,1.2))
def panel():
    box('Foot',(0,0,.03),(.45,.38,.06),'dark')
    rod('Stand',(0,0,.06),(0,0,.95),.05,'cream')
    obj=box('Control console',(0,0,1.03),(.5,.32,.10),'cream');obj.rotation_euler.x=math.radians(20)
    for x in [-.14,0,.14]:cyl('Control button',(x,-.05,1.10),.025,.025,'teal',8)
def guard():
    for x in [-.7,.7]:rod('Upright',(x,0,.02),(x,0,1.1),.025,'yellow')
    for z in [.2,1.1]:rod('Rail',(-.7,0,z),(.7,0,z),.025,'yellow')
    for x in [-.5,-.25,0,.25,.5]:rod('Guard bar',(x,0,.2),(x,0,1.1),.012,'dark')
def toolrack():
    box('Peg board',(0,0,.8),(1.3,.06,.8),'wood')
    for x in [-.5,-.25,0,.25,.5]:
        rod('Tool handle',(x,-.05,.5),(x,-.05,.83),.022,'teal')
        box('Tool head',(x,-.05,.88),(.12,.04,.055),'dark')
    for x in [-.55,.55]:rod('Frame',(x,0,.05),(x,0,1.23),.025,'dark')
def product():
    box('Chassis',(0,0,.07),(.4,.22,.12),'teal')
    for x in [-.14,.14]:
        for y in [-.14,.14]:s.wheel((x,y,.06),.06)
    box('Body module',(0,.02,.17),(.18,.17,.13),'yellow')
def openedcase():
    box('Base',(0,0,.04),(.56,.42,.08),'cream')
    for x in [-.29,.29]:box('Side',(x,0,.22),(.035,.44,.44),'cream')
    box('Back',(0,.22,.22),(.56,.035,.44),'cream')
    cyl('Motor',(-.1,0,.18),.12,.26,'dark',10).rotation_euler.y=math.pi/2
    box('Circuit board',(.14,0,.13),(.15,.28,.03),'green')
def package():
    box('Package',(0,0,.12),(.18,.12,.24),'yellow',.01)
    box('Front label',(0,-.065,.14),(.12,.012,.12),'white')
def pos():
    box('Register base',(0,0,.06),(.36,.28,.12),'dark',.01)
    rod('Screen stem',(0,.07,.12),(0,.07,.32),.03,'dark')
    box('Screen',(0,.05,.36),(.32,.035,.22),'dark')
    box('Readout',(0,.025,.36),(.27,.01,.17),'teal')
def basket():
    instance(hopper,scale=(.8,.8,.6))
    for x in [-.23,.23]:rod('Handle side',(x,0,.24),(x,0,.46),.014,'wood')
    rod('Handle',(-.23,0,.46),(.23,0,.46),.018,'wood')
def salonchair():
    cyl('Base',(0,0,.035),.32,.07,'dark',12)
    rod('Hydraulic post',(0,0,.07),(0,0,.43),.06,'cream')
    box('Seat',(0,0,.5),(.58,.55,.14),'pink',.04)
    box('Back',(0,.23,.81),(.58,.13,.56),'pink',.04)
    for x in [-.33,.33]:rod('Arm',(x,-.2,.69),(x,.22,.69),.035,'cream')
    box('Footrest',(0,-.45,.26),(.4,.18,.04),'dark')
def mirror():
    for x in [-.4,.4]:box('Frame',(x,0,.95),(.055,.08,1.8),'wood')
    for z in [.06,1.84]:box('Frame',(0,0,z),(.85,.08,.055),'wood')
    box('Mirror face',(0,0,.95),(.74,.035,1.72),'cream')
    for x in [-.33,.33]:rod('Foot',(x,-.25,.04),(x,.25,.04),.025,'wood')
def hairbasin():
    box('Pedestal',(0,0,.35),(.43,.45,.7),'dark')
    cyl('Bowl',(0,0,.80),.37,.23,'cream',12,top=.40)
    cyl('Inset',(0,0,.923),.30,.012,'dark',12)
    rod('Tap',(0,.24,.9),(0,.24,1.03),.02,'cream')
def kitchencounter():instance(s.labbench)
def cooker():
    box('Stove',(0,0,.42),(.75,.65,.84),'cream')
    box('Hob',(0,0,.86),(.78,.68,.05),'dark')
    for x in [-.19,.19]:
        for y in [-.17,.17]:cyl('Burner',(x,y,.90),.11,.02,'black',12)
    box('Oven window',(0,-.335,.42),(.5,.02,.38),'black')
    box('Door handle',(0,-.37,.66),(.45,.04,.035),'cream')
def fridge():
    box('Cabinet',(0,0,.9),(.75,.63,1.8),'green',.045)
    for z,h in [(.55,1.02),(1.42,.6)]:
        box('Door',(0,-.33,z),(.70,.035,h),'green',.025)
        box('Handle',(-.24,-.37,z),(.035,.035,.25),'dark')
def utensils():
    for x in [-.5,.5]:rod('Post',(x,0,0),(x,0,.75),.024,'wood')
    rod('Crossbar',(-.5,0,.75),(.5,0,.75),.025,'wood')
    for x in [-.36,-.12,.12,.36]:
        rod('Utensil grip',(x,0,.70),(x,0,.41),.014,'dark')
        cyl('Utensil head',(x,0,.32),.075,.025,'cream',10).rotation_euler.x=math.pi/2
def plateshelf():instance(s.shelf,scale=(.8,1,.75))
def kneading():instance(s.workbench,scale=(1.1,1.1,1))
def mixer():
    box('Base',(0,0,.035),(.38,.28,.07),'green',.02)
    box('Motor post',(.12,0,.28),(.12,.24,.50),'green',.025)
    box('Mixer head',(0,0,.48),(.37,.25,.17),'green',.035)
    cyl('Bowl',(-.075,0,.18),.14,.25,'cream',12,top=.17)
    rod('Mixer shaft',(-.075,0,.25),(-.075,0,.44),.016,'dark')
def oven():
    instance(cooker,scale=(1,1,1.5))
    box('Upper oven window',(0,-.34,1.04),(.5,.02,.35),'black')
def bakingtray():instance(s.tray,scale=(1.1,1.1,.35))
def coolingrack():
    for z in [.13,.42,.71,1.0]:box('Rack shelf',(0,0,z),(.65,.48,.025),'cream')
    for x in [-.3,.3]:
        for y in [-.21,.21]:rod('Post',(x,y,.08),(x,y,1.08),.018,'dark');s.wheel((x,y,.055),.055)
def dishware():
    for x in [-.15,.15]:
        cyl('Plate',(x,0,.018),.12,.025,'white',12)
    cyl('Cup',(0,.23,.065),.055,.13,'cream',10)
def serving():instance(s.labbench,scale=(1.2,1,1))
def menustand():
    instance(s.lectern if hasattr(s,'lectern') else lectern,scale=(.8,.8,1))
    instance(s.book,pos=(0,0,1.1),scale=(1.4,1.2,.6))
def pentablet():
    box('Tablet',(0,0,.014),(.34,.25,.028),'dark',.015)
    box('Drawing area',(0,0,.032),(.27,.20,.008),'teal')
    rod('Pen',(.16,-.1,.045),(.16,.1,.045),.008,'cream')
def designboard():
    box('Design board',(0,0,.48),(.7,.06,.96),'wood')
    for x,c in [(-.18,'purple'),(.18,'teal')]:box('Sample panel',(x,-.036,.5),(.25,.012,.6),c)
def materialsamples():
    for i,c in enumerate(['wood','cream','teal','purple']):box('Material swatch',((i-1.5)*.10,0,.02),(.085,.15,.04),c)
def easel():
    for x in [-.37,.37]:rod('Side',(x,-.14,.02),(x*.2,0,1.45),.025,'wood')
    rod('Rear leg',(0,.42,.02),(0,0,1.35),.025,'wood')
    box('Canvas rest',(0,-.10,.46),(.85,.12,.045),'wood')
    box('Canvas',(0,0,.93),(.72,.04,.87),'cream')
def canvas():box('Blank canvas',(0,0,.40),(.65,.04,.8),'cream')
def artistpalette():
    cyl('Palette board',(0,0,.018),.15,.035,'wood',12)
    for i,c in enumerate(['purple','teal','yellow','pink']):
        a=i*math.tau/4;cyl('Paint patch',(.1*math.cos(a),.1*math.sin(a),.04),.025,.01,c,8)
def handtools():
    rod('Hammer handle',(-.08,-.15,.025),(-.08,.12,.025),.02,'wood')
    box('Hammer head',(-.08,.13,.035),(.17,.06,.06),'dark')
    rod('Screwdriver',(.11,-.15,.025),(.11,.14,.025),.012,'dark')
    rod('Driver grip',(.11,-.15,.025),(.11,-.02,.025),.025,'teal')
def tripod():
    for i in range(3):
        a=i*math.tau/3;rod('Leg',(0,0,1.0),(.35*math.cos(a),.35*math.sin(a),.02),.02,'dark')
    cyl('Mount',(0,0,1.05),.07,.07,'dark',8)
def shootingtable():instance(s.table,scale=(.7,.85,.8))
def reflector():
    obj=cyl('Reflector',(0,0,.7),.46,.035,'white',16);obj.rotation_euler.x=math.pi/2
    rod('Stand',(0,0,.05),(0,0,.4),.022,'dark')
    for x in [-.3,.3]:rod('Foot',(0,0,.1),(x,0,.02),.02,'dark')
def broadcastdesk():instance(s.counter,scale=(1.3,1,.75))
def micarm():
    cyl('Clamp',(0,0,.02),.045,.04,'dark',8)
    rod('Arm',(0,0,.04),(.20,0,.42),.015,'dark')
    rod('Arm',(.20,0,.42),(.45,0,.35),.015,'dark')
    cyl('Microphone',(.45,0,.29),.035,.16,'dark',10)
def console():
    box('Audio console',(0,0,.055),(.55,.37,.11),'dark',.015)
    for x in [-.2,-.1,0,.1,.2]:
        box('Fader rail',(x,-.04,.115),(.012,.18,.008),'black')
        box('Fader',(x,-.02,.127),(.04,.035,.02),'cream')
        cyl('Knob',(x,.12,.125),.019,.025,'teal',8)
def studio_light():instance(s.lightstand,scale=(1.1,1.1,1.2))
def mediacabinet():instance(s.shelf,scale=(.8,1,.65))
def stage():box('Low stage',(0,0,.13),(2.7,1.65,.26),'wood',.06)
def micstand():
    cyl('Base',(0,0,.025),.22,.05,'dark',10)
    rod('Pole',(0,0,.05),(0,0,1.1),.02,'dark')
    rod('Boom',(0,0,1.1),(-.32,0,1.25),.016,'dark')
    rod('Microphone',(-.32,0,1.25),(-.46,0,1.31),.028,'dark',8)
def pedestal():box('Display plinth',(0,0,.4),(.65,.65,.8),'cream')
def sculpture():
    cyl('Plinth',(0,0,.04),.28,.08,'cream',12)
    ico('Sculpture',(0,0,.44),(.27,.20,.4),'purple')
    ico('Crown',(.14,0,.78),(.16,.15,.18),'teal')
def displayframe():
    for x in [-.45,.45]:rod('Support',(x,0,.03),(x,0,1.6),.025,'wood')
    box('Frame',(0,0,1.03),(.95,.08,1.0),'wood')
    box('Art surface',(0,-.05,1.03),(.81,.015,.86),'cream')
    for x in [-.4,.4]:rod('Foot',(x,-.23,.03),(x,.23,.03),.022,'dark')
def exhibitionlight():
    for x in [-.6,.6]:rod('Pole',(x,0,.03),(x,0,1.9),.02,'dark')
    rod('Track',(-.6,0,1.9),(.6,0,1.9),.025,'dark')
    for x in [-.4,0,.4]:cyl('Spot',(x,0,1.82),.065,.13,'dark',8)
def artkit():instance(artistpalette);instance(handtools,pos=(.3,0,0),scale=(.6,.6,.6))
def scaffold():
    for x in [-.7,.7]:
        for y in [-.27,.27]:rod('Upright',(x,y,.03),(x,y,1.6),.025,'cream')
        rod('Cross brace',(x,-.27,.1),(x,.27,1.5),.016,'dark')
    for z in [.65,1.3]:box('Platform',(0,0,z),(1.5,.65,.07),'wood')
def bricks():
    for row in range(4):
        for column in range(4):box('Brick',((column-1.5)*.23+(row%2)*.10,0,.065+row*.13),(.22,.15,.12),'wood')
def lumber():
    for layer in range(3):
        for col in range(3):box('Timber',((col-1)*.17,0,.06+layer*.13),(.15,.9,.11),'wood')
def pipes():
    for x in [-.35,.35]:rod('Pipe',(x,0,.05),(x,0,1.4),.09,'cream',10)
    rod('Cross pipe',(-.35,0,1.3),(.35,0,1.3),.09,'teal',10)
    obj=cyl('Valve',(0,-.1,.8),.13,.035,'orange',10);obj.rotation_euler.x=math.pi/2
    rod('Valve stem',(0,-.1,.8),(0,0,.8),.035,'dark')
def ladder():
    for x in [-.25,.25]:rod('Rail',(x,0,.02),(x,0,1.5),.025,'cream')
    for z in [.2,.45,.7,.95,1.2,1.45]:rod('Rung',(-.25,0,z),(.25,0,z),.024,'cream')
def partsbox():instance(hopper,scale=(.7,.7,.7))
def controlbox():
    instance(s.equipment,scale=(.65,.7,1.3))
    for z in [.6,.8,1.0]:cyl('Indicator',(0,-.195,z),.025,.012,'yellow',8).rotation_euler.x=math.pi/2
def vial():
    cyl('Sample vial',(0,0,.065),.04,.13,'cream',8)
    cyl('Cap',(0,0,.14),.043,.025,'teal',8)
def meter():
    box('Meter',(0,0,.075),(.15,.09,.15),'yellow',.018)
    box('Readout',(0,-.05,.09),(.10,.012,.055),'dark')
    rod('Probe',(.1,0,0),(.1,0,.28),.009,'dark')
def vegetation():
    for i in range(4):
        a=i*math.tau/4;ico('Leaf',(.12*math.cos(a),.12*math.sin(a),.25),(.10,.09,.25),'green')
    cyl('Stem',(0,0,.14),.018,.28,'wood',6)
def sensortripod():instance(tripod,scale=(.8,.8,1));instance(meter,pos=(0,0,1.1))
def weather():
    rod('Mast',(0,0,0),(0,0,1.5),.025,'cream')
    for z in [.8,.9,1.0]:cyl('Sensor shield',(0,0,z),.12,.035,'white',10)
    rod('Anemometer',(-.24,0,1.48),(.24,0,1.48),.015,'dark')
    for x in [-.24,.24]:ico('Wind cup',(x,0,1.5),(.07,.07,.05),'dark')
def recorder():instance(s.laptop,scale=(.8,.8,.8))
def raisedbed():
    box('Soil',(0,0,.10),(1.15,.7,.20),'soil')
    for x in [-.61,.61]:box('Border',(x,0,.15),(.07,.8,.30),'wood')
    for y in [-.38,.38]:box('Border',(0,y,.15),(1.2,.06,.30),'wood')
def crops():
    for x in [-.20,0,.20]:
        for y in [-.18,.18]:instance(vegetation,pos=(x,y,0),scale=(.5,.5,.55))
def watering():
    cyl('Can',(0,0,.15),.14,.30,'green',10)
    rod('Spout',(.10,0,.10),(.34,0,.33),.035,'green')
    rod('Handle',(-.17,0,.10),(-.17,0,.35),.02,'green')
    rod('Handle top',(-.17,0,.35),(0,0,.35),.02,'green')
def farmtools():
    for x in [-.14,.14]:rod('Tool handle',(x,0,.12),(x,0,1.1),.02,'wood')
    box('Spade',(-.14,0,.11),(.18,.035,.22),'dark')
    rod('Rake head',(.05,0,.13),(.25,0,.13),.02,'dark')
    for x in [.05,.1,.15,.2,.25]:rod('Rake tine',(x,0,.13),(x,-.09,.13),.009,'dark')
def harvest():instance(hopper,scale=(1.1,1.1,.7))
def irrigationpipe():
    rod('Pipe',(-.65,0,.025),(.65,0,.025),.02,'dark')
    for x in [-.4,0,.4]:rod('Drip branch',(x,0,.025),(x,.35,.025),.012,'dark')
def growtable():instance(s.table,scale=(1,.8,1))
def seedlings():
    box('Tray',(0,0,.025),(.5,.35,.05),'dark')
    for x in [-.16,0,.16]:
        for y in [-.09,.09]:instance(vegetation,pos=(x,y,.05),scale=(.25,.25,.25))
def irrigation():
    cyl('Water tank',(0,0,.5),.30,1.0,'teal',12)
    rod('Outlet',(.25,0,.12),(.6,0,.12),.025,'dark')
    box('Pump',(.55,0,.16),(.2,.2,.25),'green')
def envsensor():instance(weather,scale=(.6,.6,.7))
def frame():
    for x in [-.8,.8]:
        for y in [-.5,.5]:rod('Post',(x,y,0),(x,y,1.65),.03,'cream')
    for y in [-.5,.5]:rod('Roof rail',(-.8,y,1.65),(.8,y,1.65),.03,'cream')
    for x in [-.8,0,.8]:rod('Roof brace',(x,-.5,1.65),(x,.5,1.65),.025,'cream')
def livestockpen():
    for x in [-.65,.65]:
        for y in [-.45,.45]:rod('Fence post',(x,y,0),(x,y,.8),.04,'wood')
    for z in [.3,.65]:
        for y in [-.45,.45]:rod('Fence rail',(-.65,y,z),(.65,y,z),.03,'wood')
        for x in [-.65,.65]:rod('Fence end',(x,-.45,z),(x,.45,z),.03,'wood')
def feedtrough():instance(hopper,scale=(1.7,.6,.6))
def watertub():cyl('Water tub',(0,0,.18),.30,.36,'teal',12);cyl('Water surface',(0,0,.365),.26,.01,'teal',12)
def bedding():box('Bedding zone',(0,0,.02),(1.1,.75,.04),'yellow')
def feedbin():cyl('Feed bin',(0,0,.35),.25,.7,'cream',10);cyl('Lid',(0,0,.72),.27,.045,'wood',10)
def cage():
    box('Floor',(0,0,.035),(.55,.38,.07),'cream')
    for x in [-.26,.26]:
        for y in [-.17,.17]:rod('Corner',(x,y,.07),(x,y,.45),.018,'dark')
    box('Roof',(0,0,.47),(.55,.38,.05),'cream')
    for x in [-.2,-.1,0,.1,.2]:rod('Door bar',(x,-.18,.07),(x,-.18,.45),.009,'dark')
    for y in [-.1,0,.1]:
        for x in [-.26,.26]:rod('Side bar',(x,y,.07),(x,y,.45),.009,'dark')
def bowls():
    for x,c in [(-.16,'teal'),(.16,'yellow')]:cyl('Bowl',(x,0,.06),.12,.12,c,10,top=.15);cyl('Inset',(x,0,.124),.105,.008,'dark',10)
def deck():box('Deck',(0,0,.09),(2.2,1.6,.18),'wood',.1)
def railing():
    for x in [-.7,0,.7]:rod('Stanchion',(x,0,.01),(x,0,.65),.023,'cream')
    for z in [.3,.65]:rod('Rail',(-.72,0,z),(.72,0,z),.022,'cream')
def rope():
    for i in range(3):
        bpy.ops.mesh.primitive_torus_add(major_segments=12,minor_segments=4,major_radius=.12+i*.025,minor_radius=.012,location=(0,0,.015))
        obj=bpy.context.object;obj.name='Rope coil';s.paint(obj,'wood')
def bollard():
    box('Foot',(0,0,.025),(.35,.24,.05),'dark')
    for x in [-.09,.09]:cyl('Post',(x,0,.15),.06,.25,'dark',8)
    rod('Crossbar',(-.19,0,.28),(.19,0,.28),.045,'dark')
def wheelhelm():
    rod('Column',(0,0,0),(0,0,.75),.055,'wood')
    bpy.ops.mesh.primitive_torus_add(major_segments=12,minor_segments=4,major_radius=.25,minor_radius=.025,location=(0,-.04,.8),rotation=(math.pi/2,0,0));s.paint(bpy.context.object,'wood')
    for i in range(6):
        a=i*math.tau/6;rod('Spoke',(0,-.04,.8),(.34*math.cos(a),-.04,.8+.34*math.sin(a)),.018,'wood')
def instruments():
    box('Console',(0,0,.48),(1.0,.48,.96),'cream')
    box('Panel',(0,-.05,1.0),(1.02,.58,.09),'dark')
    for x in [-.3,0,.3]:box('Readout',(x,-.08,1.055),(.23,.31,.018),'teal')
def helmseat():instance(s.salonchair if hasattr(s,'salonchair') else salonchair,scale=(1,1,1.1))
def navscreen():instance(s.medmonitor,scale=(1.6,1.1,1.3))
def dockfloor():box('Dock paving',(0,0,.025),(2.8,1.5,.05),'cream')
def wateredge():box('Water edge',(0,0,.015),(2.3,.8,.03),'teal')
def quaypost():cyl('Mooring post',(0,0,.24),.11,.48,'dark',10);cyl('Cap',(0,0,.5),.15,.05,'yellow',10)
def gymbench():
    box('Cushion',(0,0,.46),(1.2,.35,.10),'dark',.035)
    s.legs((-.45,.45),(-.12,.12),.41,'cream')
def ballrack():
    for x in [-.5,.5]:rod('Frame',(x,0,0),(x,0,1.15),.025,'dark')
    for z in [.2,.6,1.0]:
        for y in [-.15,.15]:rod('Rail',(-.5,y,z),(.5,y,z),.018,'dark')
    for i in range(3):ico('Ball',((i-1)*.3,0,.76),(.13,.13,.13),'orange')
def bottles():
    box('Tray',(0,0,.025),(.45,.23,.05),'wood')
    for x in [-.13,0,.13]:cyl('Bottle',(x,0,.15),.042,.25,'teal',8);cyl('Cap',(x,0,.285),.03,.035,'dark',8)
def stretchbar():
    for x in [-.65,.65]:rod('Post',(x,0,0),(x,0,1.0),.03,'cream')
    rod('Bar',(-.7,0,1.0),(.7,0,1.0),.035,'wood')
def step():box('Step',(0,0,.11),(.85,.4,.22),'teal',.04)
def dumbbells():
    for y in [-.13,.13]:
        rod('Grip',(-.1,y,.06),(.1,y,.06),.018,'cream')
        for x in [-.13,.13]:cyl('Weight',(x,y,.06),.06,.07,'dark',8).rotation_euler.y=math.pi/2
def exercisemirror():instance(mirror,scale=(1.25,1,1))
def court():
    box('Court surface',(0,0,.015),(3.8,2.3,.03),'green')
    for y in [-1.05,1.05]:box('Sideline',(0,y,.034),(3.6,.025,.008),'white')
    for x in [-1.8,0,1.8]:box('Line',(x,0,.034),(.025,2.1,.008),'white')
def goals():
    for base in [-1.6,1.6]:
        for y in [-.4,.4]:rod('Goal post',(base,y,0),(base,y,.55),.025,'white')
        rod('Crossbar',(base,-.4,.55),(base,.4,.55),.025,'white')
        for y in [-.4,.4]:rod('Net support',(base,y,.55),(base+(-.2 if base<0 else .2),y,.02),.014,'white')
def ball():ico('Ball',(0,0,.12),(.12,.12,.12),'white')
def scoreboard():instance(s.sign,scale=(1.2,1,1.1))
def relationboard():instance(s.whiteboard,scale=(1.1,1,.95))
def sealedbox():instance(s.case,scale=(.8,.8,.7));box('Seal',(0,-.15,.23),(.045,.012,.13),'yellow')
def lockedcabinet():instance(s.locker,scale=(.8,1,1))
def judgedais():
    box('Platform',(0,0,.10),(2.4,1.2,.2),'wood')
    box('Bench',(0,0,.7),(1.9,.65,1.0),'wood')
    box('Top',(0,0,1.24),(2.05,.8,.08),'wood')
def witness():instance(lectern,scale=(.85,.85,.95))
def partytable():instance(s.table,scale=(1.2,1,1))
def gallerychair():instance(s.chair,scale=(.9,.9,1))
def documentsafe():instance(s.bedside,scale=(1.2,1.1,1.5))
def pallet():
    for y in [-.32,0,.32]:box('Runner',(0,y,.07),(1.0,.11,.14),'wood')
    for x in [-.4,-.2,0,.2,.4]:box('Deck board',(x,0,.16),(.16,.8,.05),'wood')
def jack():
    for x in [-.2,.2]:box('Fork',(x,-.15,.065),(.13,.8,.07),'yellow');s.wheel((x,-.45,.045),.045)
    rod('Handle',(0,.23,.1),(0,.23,.95),.03,'dark')
    rod('Grip',(-.18,.23,.95),(.18,.23,.95),.03,'dark')
def driveseat():instance(salonchair,scale=(1.1,1.1,1.2))
def driveconsole():instance(instruments,scale=(1.3,1.2,1))
def passenger():instance(s.chair,scale=(1.1,1.1,1.1))
def calculator():
    box('Calculator',(0,0,.015),(.12,.18,.03),'dark',.01)
    box('Readout',(0,.055,.033),(.09,.04,.006),'teal')
    for x in [-.035,0,.035]:
        for y in [-.055,-.02,.015]:box('Key',(x,y,.035),(.024,.024,.01),'cream')
def washer():
    box('Washing machine',(0,0,.43),(.65,.60,.86),'cream',.02)
    obj=cyl('Door rim',(0,-.32,.37),.22,.045,'dark',16);obj.rotation_euler.x=math.pi/2
    obj=cyl('Drum window',(0,-.35,.37),.17,.014,'teal',16);obj.rotation_euler.x=math.pi/2
    box('Readout',(.15,-.312,.75),(.20,.016,.07),'dark')
def toolbag():instance(s.toolbox,scale=(.9,.9,.9))
def pen():rod('Pen',(0,-.1,.01),(0,.1,.01),.009,'dark',6)
def serverrack():
    box('Server case',(0,0,1.0),(.65,.65,2.0),'dark')
    for z in [.2,.45,.7,.95,1.2,1.45,1.7]:
        box('Server',(0,-.34,z),(.58,.025,.17),'black')
        box('Handle',(-.23,-.36,z),(.025,.015,.09),'cream')
        box('Status lamp',(.20,-.36,z),(.035,.012,.025),'teal')
def cabletray():
    for y in [-.12,.12]:rod('Cable rail',(-1,y,.05),(1,y,.05),.02,'yellow')
    for x in [-1,-.5,0,.5,1]:rod('Rung',(x,-.12,.05),(x,.12,.05),.012,'dark')
    for y in [-.05,.05]:rod('Cable',(-1,y,.07),(1,y,.07),.01,'teal')
def terminal():instance(s.laptop,scale=(1.1,1.1,1.1))
def controlconsole():
    instance(instruments,scale=(1.5,1,1))
    for x in [-.5,0,.5]:instance(s.medmonitor,pos=(x,.10,1.05),scale=(1,1,1))
def auxiliary():instance(s.medmonitor,scale=(1,1,.9))
def sofa():
    box('Base',(0,0,.26),(1.65,.65,.35),'cream',.06)
    for x in [-.42,.42]:box('Seat cushion',(x,-.06,.47),(.77,.56,.15),'cream',.04)
    box('Back',(0,.27,.73),(1.65,.18,.57),'cream',.05)
    for x in [-.8,.8]:box('Arm',(x,0,.55),(.17,.7,.37),'cream',.04)
def television():
    box('TV frame',(0,0,.75),(1.25,.07,.75),'dark',.02)
    box('Screen',(0,-.04,.75),(1.15,.012,.65),'teal')
    for x in [-.4,.4]:rod('Foot',(x,0,.37),(x,-.15,.05),.02,'dark')
def facilities():instance(controlbox,scale=(1.4,1.2,1.2))
def inspectionboard():instance(s.whiteboard,scale=(.8,1,.9))
def schedule():instance(relationboard,scale=(.9,1,.9))
def shoerack():
    for z in [.12,.40]:box('Shelf',(0,0,z),(.8,.35,.04),'wood')
    for x in [-.4,.4]:box('Side',(x,0,.25),(.04,.35,.5),'wood')
def mobile():box('Phone',(0,0,.008),(.075,.15,.016),'dark',.007);box('Screen',(0,0,.018),(.062,.127,.006),'teal')
def pouch():box('Document pouch',(0,0,.02),(.27,.20,.04),'dark',.015);box('Flap',(0,.07,.047),(.27,.06,.014),'cream')
def mapstand():instance(displayframe,scale=(1.2,1,.9))
def boundary():
    for x in [-.45,.45]:cyl('Boundary post',(x,0,.27),.065,.54,'wood',8)
    rod('Rope',(-.45,0,.45),(.45,0,.45),.018,'cream')
def pulpit():
    instance(lectern,scale=(1.2,1.1,1.1))
    box('Cross upright',(0,-.18,.65),(.035,.015,.25),'cream')
    box('Cross arm',(0,-.18,.70),(.15,.015,.035),'cream')
def openbook():
    for x,angle in [(-.12,-8),(.12,8)]:
        obj=box('Open page',(x,0,.025),(.24,.30,.03),'cream');obj.rotation_euler.y=math.radians(angle)
    box('Spine',(0,0,.016),(.025,.31,.035),'wood')
def cross():
    box('Base',(0,0,.025),(.30,.24,.05),'wood')
    box('Upright',(0,0,.74),(.08,.07,1.45),'wood')
    box('Crossbar',(0,0,1.05),(.66,.07,.08),'wood')
def hymnstand():instance(lectern,scale=(.65,.7,.9))
def keyboardinstrument():
    box('Keyboard',(0,0,.78),(1.05,.32,.10),'dark')
    for i in range(16):box('White key',((i-7.5)*.055,-.06,.84),(.05,.20,.025),'white')
    s.legs((-.43,.43),(-.10,.10),.73,'dark')
def altarbase():
    box('Base',(0,0,.1),(1.8,.85,.2),'wood')
    box('Altar',(0,0,.5),(1.5,.65,.65),'wood')
    box('Top',(0,0,.86),(1.8,.85,.10),'wood')
def buddha():
    cyl('Lotus base',(0,0,.06),.34,.12,'yellow',12)
    ico('Folded legs',(0,0,.24),(.34,.22,.18),'yellow')
    ico('Robe torso',(0,0,.49),(.20,.15,.31),'yellow')
    ico('Head',(0,0,.85),(.13,.12,.16),'yellow')
    ico('Hair knot',(0,0,1.01),(.065,.06,.055),'wood')
    for x in [-.22,.22]:rod('Folded arm',(x,0,.60),(x*.35,-.14,.40),.055,'yellow',8)
def cushion():box('Meditation cushion',(0,0,.06),(.48,.44,.12),'pink',.07)
def sutrastand():instance(lectern,scale=(.9,.85,.38))
def woodfish():
    ico('Wooden fish drum',(0,0,.11),(.16,.12,.11),'wood')
    rod('Mallet',(.20,-.12,.04),(.20,.13,.04),.018,'wood')
def incense():
    cyl('Bowl',(0,0,.10),.16,.16,'wood',10,top=.19)
    cyl('Ash',(0,0,.184),.15,.008,'cream',10)
    for x in [-.04,0,.04]:rod('Incense stick',(x,0,.18),(x,0,.46),.004,'wood')
def lotus():
    for i in range(6):
        a=i*math.tau/6;ico('Petal',(.09*math.cos(a),.09*math.sin(a),.06),(.09,.05,.055),'pink')
    cyl('Flower core',(0,0,.09),.035,.045,'yellow',8)
def massaltar():
    instance(altarbase,scale=(1.1,1,1))
    box('Altar cloth',(0,0,.925),(1.95,.90,.02),'white')
def readingstand():instance(pulpit,scale=(.85,.8,1))
def crucifix():
    instance(cross)
    ico('Figure head',(0,-.06,1.17),(.052,.035,.07),'cream')
    rod('Figure torso',(0,-.06,.84),(0,-.06,1.08),.042,'cream',8)
    for x in [-.25,.25]:rod('Extended arm',(0,-.06,1.05),(x,-.06,1.09),.018,'cream')
    for x in [-.035,.035]:rod('Leg',(x,-.06,.84),(0,-.06,.57),.019,'cream')
def chalice():
    cyl('Foot',(0,0,.012),.075,.025,'yellow',10)
    rod('Stem',(0,0,.025),(0,0,.16),.018,'yellow')
    cyl('Cup',(0,0,.215),.03,.11,'yellow',10,top=.085)
def liturgy():instance(s.book,scale=(1.15,1.15,1.2))
def candle():
    cyl('Foot',(0,0,.025),.11,.05,'yellow',10)
    rod('Stand',(0,0,.05),(0,0,.42),.025,'yellow')
    cyl('Cup',(0,0,.43),.075,.04,'yellow',10)
    cyl('Wax',(0,0,.55),.035,.22,'cream',10)

RECIPES={32:tubes,33:beaker,34:pipettes,35:balance,38:analyzer,46:armchair,47:overbed,48:callbutton,
50:studentdesk,51:teacherdesk,52:blackboard,57:kit,59:lectern,60:presentation,61:av,62:armchair,63:tissues,64:notebook,66:activity,
68:walker,69:wheelchair,70:rail,71:machine,72:conveyor,73:hopper,74:productbox,75:panel,76:guard,77:toolrack,78:product,81:openedcase,
82:package,83:pos,84:basket,85:salonchair,86:mirror,87:hairbasin,88:kitchencounter,89:cooker,90:fridge,91:utensils,92:plateshelf,
93:kneading,94:mixer,95:oven,96:bakingtray,97:coolingrack,98:dishware,99:serving,100:menustand,101:pentablet,102:designboard,103:materialsamples,
104:easel,105:canvas,107:artistpalette,108:handtools,110:tripod,112:shootingtable,113:reflector,115:broadcastdesk,116:micarm,
118:console,119:studio_light,121:mediacabinet,122:stage,123:micstand,124:pedestal,125:sculpture,126:displayframe,128:exhibitionlight,
129:artkit,130:scaffold,131:bricks,132:lumber,134:guard,135:pipes,136:ladder,137:partsbox,138:controlbox,140:vial,141:meter,143:vegetation,
144:sensortripod,145:weather,146:recorder,147:raisedbed,148:crops,149:watering,150:farmtools,151:harvest,152:irrigationpipe,153:growtable,
154:seedlings,155:irrigation,156:envsensor,157:frame,158:livestockpen,159:feedtrough,160:watertub,161:bedding,162:feedbin,164:cage,165:bowls,
166:deck,167:railing,169:rope,170:bollard,171:wheelhelm,172:instruments,173:helmseat,174:navscreen,176:dockfloor,177:wateredge,178:quaypost,
180:gymbench,181:ballrack,182:bottles,183:stretchbar,184:step,185:dumbbells,186:exercisemirror,187:court,188:goals,189:ball,190:scoreboard,
191:relationboard,192:sealedbox,193:lockedcabinet,194:judgedais,195:witness,196:partytable,197:gallerychair,198:documentsafe,
199:s.shelf,200:pallet,201:jack,202:driveseat,203:driveconsole,204:passenger,206:calculator,207:washer,208:toolbag,209:pen,210:serverrack,
211:cabletray,212:terminal,213:controlconsole,214:auxiliary,215:sofa,216:television,217:facilities,218:inspectionboard,219:schedule,
220:shoerack,222:mobile,223:pouch,224:mapstand,225:boundary,244:pulpit,245:openbook,246:cross,248:hymnstand,249:keyboardinstrument,
250:altarbase,251:buddha,252:cushion,253:sutrastand,254:woodfish,255:incense,256:lotus,257:massaltar,258:readingstand,259:crucifix,260:chalice,261:liturgy,262:candle}

if __name__=='__main__':
    args=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
    s.RECIPES.update(RECIPES)
    for number in ([int(x) for x in args] if args else sorted(RECIPES)):s.produce(number)

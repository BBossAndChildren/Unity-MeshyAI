"""Reference-informed room assembly. No missing-candidate substitute meshes.

Explicit layouts use Blender Z-up meters; candidate reuse is resolved to fixed
asset versions and all instances are counted in the final GLB budget.
"""
import bpy
import json
import math
import sys
import importlib.util
import datetime
from pathlib import Path
from mathutils import Vector, Matrix

ROOT=Path(__file__).resolve().parents[6]
SCRIPT=Path(__file__).relative_to(ROOT).as_posix()
SHARED='meshy/models/blender/AST-1010/v001/processing/build_shared.py'
spec=importlib.util.spec_from_file_location('shared',ROOT/SHARED)
shared=importlib.util.module_from_spec(spec);spec.loader.exec_module(shared)
CAT=ROOT/'docs/machine/catalog'
F=.296

def p(candidate,x,y,z=F,rotation=0,scale=(1,1,1),euler=None):
    return dict(candidate_id=f'CND-{candidate:03}',position=[x,y,z],rotation=rotation,scale=list(scale),euler=euler)

LAYOUTS={
2:[p(10,0,-.15),p(11,-1.1,-.1,rotation=-90),p(11,1.1,-.1,rotation=90),p(11,0,-1.05,rotation=180),
   p(12,-.36,-.1,F+.80,rotation=15),p(12,.38,-.1,F+.80,rotation=-12),p(13,-.35,1.55),
   p(14,-.65,1.50,F+1.22,euler=[90,0,0]),p(14,.0,1.50,F+1.4,euler=[90,0,0]),
   p(15,1.5,1.25),p(16,1.9,-.25),p(65,-1.9,1.0),p(67,0,-.2,F+.01),p(53,.25,-.3,F+.80),p(106,-.10,-.1,F+.8)],
3:[p(4,-1,-.45),p(4,1,.65),p(3,-1,-1.35,rotation=180),p(3,1,-.25,rotation=180),
   p(5,-1,-.31,F+.795),p(5,1,.79,F+.795),p(6,-1,-.65,F+.795),p(6,1,.45,F+.795),
   p(18,-.65,-.65,F+.795),p(18,1.35,.45,F+.795),p(17,-.42,-.35),p(17,1.57,.75),
   p(19,-1.5,-.35,F+.795),p(19,.5,.75,F+.795),p(20,-1,-.45,F+.795),p(21,-.75,-.45,F+.795),
   p(22,1.45,.5,F+.795),p(16,-2,.9),p(9,-.5,1.8),p(8,1.7,1.75),p(65,-2,1.7)],
4:[p(23,0,.1),p(3,0,1.0),p(5,.2,.25,F+1.065),p(24,-1.8,-.65),p(25,.3,-1.6),p(26,1.9,.7),p(65,1.75,1.75)],
5:[p(4,-.8,1.3),p(10,-.2,-.8),p(11,-.9,-1.5,rotation=180),p(11,.5,-1.5,rotation=180),
   p(11,-.9,0),p(27,-1.1,1.3,F+.795),p(28,1.65,1.5),p(29,1.65,1.45,F+1.6),
   p(30,-1.4,1.35,F+.795),p(65,1.9,-.9),p(53,1.4,1.45,F+.6),p(53,1.7,1.45,F+1.1)],
}

# The reference review fixes the relative working zones below. Measurements are
# virtual design dimensions, not asserted measurements of the source images.
LAYOUTS.update({
6:[p(31,0,-.4),p(36,-1.15,1.5),p(37,1.5,1.45),p(32,-.45,-.3,F+.90),p(33,.12,-.4,F+.90),p(34,.53,-.3,F+.90),p(35,-.5,-.65,F+.90),p(16,1.9,-.6),p(56,0,-1.4)],
7:[p(31,-.8,-.65),p(38,-.8,1.0),p(4,1.0,-.4),p(5,1.0,-.3,F+.795),p(3,1,-1.25,rotation=180),p(37,1.8,1.5),p(39,-.7,-.6,F+.90),p(40,-1.25,-.65,F+.90)],
8:[p(4,-1,-.65),p(5,-1,-.50,F+.795),p(11,-1.0,-1.5,rotation=180),p(11,-1.0,.15),p(41,1.05,.45),p(42,.6,1.5,F+.95),p(16,1.95,-.95),p(37,-1.5,1.5),p(43,1.8,1.6)],
9:[p(41,0,-.25),p(43,.8,1.3),p(36,-1.6,1.2),p(37,1.7,1.5),p(16,-1.5,-1.0),p(16,1.5,-1.0),p(40,-1.5,-1,F+.87)],
10:[p(44,0,.1),p(45,-.95,.7),p(46,-1.8,-.25),p(47,1.35,-.35),p(48,-.65,.75,F+.9),p(42,1.15,1.15,F+.65)],
11:[p(23,0,.30),p(5,.1,.4,F+1.065),p(25,-.25,-1.55),p(24,1.95,-.85),p(49,-.6,.32,F+1.065),p(27,.5,.35,F+1.065),p(65,-1.9,.9)],
12:[p(50,-1,-1.0),p(50,.25,-1),p(50,-1,.25),p(50,.25,.25),p(11,-1,-1.55,rotation=180),p(11,.25,-1.55,rotation=180),p(11,-1,-.3,rotation=180),p(11,.25,-.3,rotation=180),p(51,1.2,1.2),p(52,-.4,1.85),p(53,-1,-.95,F+.69),p(54,1.9,-.4)],
13:[p(55,-1,-.8,scale=(.7,.8,1)),p(55,.8,-.8,scale=(.7,.8,1)),p(55,0,1.0),p(56,-1,-1.5),p(56,.8,-1.5),p(57,-1,-.8,F+.88),p(57,.8,-.8,F+.88),p(58,-1.8,1.25),p(28,1.8,1.2)],
14:[p(59,-1.65,1.3),p(60,.1,1.65),p(61,1.8,.9,F+.55),p(10,-.8,-.6),p(10,1,-.6),p(11,-1.2,-1.3,rotation=180),p(11,-.45,-1.3,rotation=180),p(11,.7,-1.3,rotation=180),p(11,1.4,-1.3,rotation=180)],
15:[p(62,-1.0,-.4,rotation=-25),p(62,1.0,-.4,rotation=25),p(10,0,-.65,scale=(.6,.6,.55)),p(63,.1,-.65,F+.45),p(64,-.2,-.7,F+.45),p(28,0,1.5),p(65,-1.9,1.3),p(67,0,-.5,F+.01)],
16:[p(10,-.8,-.7),p(11,-1.7,-.7,rotation=-90),p(11,.1,-.7,rotation=90),p(66,-.8,-.7,F+.80),p(67,1.2,.6,F+.01,scale=(.8,.8,1)),p(28,-1,1.45),p(13,1.7,1.7)],
17:[p(44,-.5,.15),p(45,-1.5,.65),p(68,.9,-1.0),p(69,1.7,.1),p(70,1.0,1.7),p(9,-1.5,1.7),p(67,-.8,-1.3,F+.01,scale=(.7,.5,1))],
18:[p(71,0,.6),p(72,-1.7,-.4,rotation=90,scale=(.7,.7,1)),p(72,1.5,-.4,rotation=90,scale=(.7,.7,1)),p(73,-2,1),p(74,1.6,1.3),p(75,0,-1.1),p(76,-1.3,1.25,rotation=90),p(76,1.3,1.25,rotation=90)],
19:[p(55,-.3,-.5),p(77,-.2,1.3),p(28,1.8,1.25),p(40,-.8,-.5,F+.88),p(78,-.1,-.5,F+.88),p(79,.35,-.4,F+.88),p(80,1.8,-.5),p(16,-1.9,.2)],
20:[p(55,-.4,.75),p(77,-.4,1.7),p(79,-1,.75,F+.88),p(40,.05,.75,F+.88),p(81,0,-.9),p(80,1.6,.8),p(16,-1.9,-.6)],
21:[p(28,-1.5,.5,rotation=-90),p(28,.1,1.65),p(82,-1.5,.15,F+.62),p(82,-1.5,.65,F+1.12),p(82,-.2,1.6,F+.62),p(23,1.3,-.4,scale=(.8,.8,.85)),p(83,1.25,-.4,F+.91),p(84,2,-1.2),p(58,.2,-1.4)],
22:[p(23,0,.1),p(5,.25,.25,F+1.065),p(11,-.55,-1.1,rotation=180),p(11,.55,-1.1,rotation=180),p(49,-.55,.15,F+1.065),p(27,.55,.15,F+1.065),p(9,-1.5,1.5)],
23:[p(85,0,-.3),p(86,-.2,1.4),p(87,1.6,1.1),p(16,1.6,-.8),p(56,-1.5,-.5)],
24:[p(88,0,-1.0),p(89,1.4,1.4),p(90,-1.8,1.25),p(36,-.3,1.4),p(91,1.25,1.8,F+.95),p(92,1.9,-.75),p(98,0,-1.0,F+.90)],
25:[p(93,-.3,-.7),p(94,-1.8,.7,F+.85),p(55,-1.8,.7,scale=(.55,.8,1)),p(95,1.5,1.25),p(96,-.3,-.7,F+.89),p(97,1.8,-.6),p(28,-.4,1.65)],
26:[p(10,-1.15,-.9,scale=(.75,.8,1)),p(10,1.15,-.9,scale=(.75,.8,1)),p(10,-1.15,.6,scale=(.75,.8,1)),p(11,-1.15,-1.6,rotation=180),p(11,1.15,-1.6,rotation=180),p(11,-1.15,-.1,rotation=180),p(98,-1.15,-.9,F+.8),p(98,1.15,-.9,F+.8),p(99,.8,1.7),p(100,2.1,.1)],
})

LAYOUTS.update({
27:[p(4,-.8,-.5),p(3,-.8,-1.4,rotation=180),p(5,-.8,-.3,F+.795),p(101,-.7,-.65,F+.795),p(102,1.3,1.6),p(103,1.15,-.55,F+.88),p(55,1.2,-.5,scale=(.7,.8,1)),p(28,-1.6,1.5)],
28:[p(104,0,-.4),p(105,0,-.43,F+.50),p(55,-1.4,.4,rotation=90,scale=(.7,.8,1)),p(106,-1.4,.15,F+.88),p(107,-1.4,.55,F+.88),p(56,.4,-1.2),p(28,1.5,1.4),p(65,-1.7,1.7)],
29:[p(55,-.3,-.5),p(79,.1,-.5,F+.88),p(108,-.6,-.5,F+.88),p(28,1.5,1.4),p(58,-1.8,-1.0),p(16,-1.7,1.0)],
30:[p(110,-.4,-1),p(109,-.4,-1,F+1.08),p(111,-1.9,.3,rotation=-35),p(111,1.6,1.2,rotation=35),p(112,.1,.8),p(113,1.7,-1.1,rotation=-30),p(114,-1.8,-1.3),p(82,.1,.8,F+.64)],
31:[p(115,-.2,-.15),p(116,-.5,-.2,F+.83),p(117,.1,-.2,F+.83),p(109,-1.8,-1.1,F+1.05),p(110,-1.8,-1.1),p(118,1.6,.7,F+.79),p(4,1.6,.7,rotation=90,scale=(.7,.8,1)),p(119,-1.6,1.6),p(119,1.6,1.6)],
32:[p(4,0,.4,scale=(1.3,1,1)),p(3,0,-.65,rotation=180),p(5,-.45,.55,F+.795),p(5,.45,.55,F+.795),p(6,0,.12,F+.795),p(18,.4,.12,F+.795),p(120,-1.1,.5,F+.795),p(120,1.1,.5,F+.795),p(117,.7,.15,F+.795),p(121,-1.9,1.45)],
33:[p(122,0,.5),p(123,0,.4,F+.26),p(120,-1.9,.6),p(120,1.9,.6),p(128,0,1.7),p(11,-1,-1.1,rotation=180),p(11,0,-1.1,rotation=180),p(11,1,-1.1,rotation=180),p(11,-1,-1.8,rotation=180),p(11,0,-1.8,rotation=180),p(11,1,-1.8,rotation=180)],
34:[p(124,0,-.3),p(125,0,-.3,F+.8),p(124,-1.7,.5,scale=(.65,.65,.65)),p(125,-1.7,.5,F+.52,scale=(.5,.5,.5)),p(126,-1.5,1.6),p(126,1.4,1.6),p(127,0,-1.65),p(128,0,1.9)],
35:[p(10,0,-.3),p(11,-1.1,-.3,rotation=-90),p(11,1.1,-.3,rotation=90),p(11,-.5,-1.1,rotation=180),p(11,.5,-1.1,rotation=180),p(129,-.3,-.3,F+.80),p(28,-1.3,1.5),p(13,1.2,1.6)],
36:[p(130,-1.4,1),p(131,0,.9),p(131,.4,.9,rotation=90),p(132,1.5,.6),p(133,-1.1,-1.1),p(134,1.8,-.9,rotation=90)],
37:[p(55,-1,-.8),p(135,.2,1.2),p(77,-1,1.8),p(136,1.5,.2),p(137,1.6,-1.1),p(138,1.8,1.4),p(80,-1.6,-1.5)],
38:[p(139,0,.1,scale=(1.5,1.4,1)),p(140,-1,-.5,F+.9),p(141,-.7,-.5,F+.9),p(142,.9,-1.0),p(143,-1.8,1.4),p(143,1.7,1.1),p(55,-1,-.5,scale=(.65,.7,1)),p(58,1.5,.2)],
39:[p(139,-.9,.6),p(144,0,-.5),p(145,1.2,.7),p(146,.8,-1.15,F+.5),p(114,.8,-1.15),p(127,-1.6,-1.1),p(143,-1.8,1.5)],
40:[p(147,-1.1,-.7),p(147,1.0,-.7),p(147,-1.1,.9),p(148,-1.1,-.7,F+.21),p(148,1,-.7,F+.21),p(148,-1.1,.9,F+.21),p(149,1.7,1.4),p(150,2,0),p(151,0,-1.7),p(152,0,.1)],
41:[p(153,-1.0,-.6,scale=(.9,.8,1)),p(153,1,-.6,scale=(.9,.8,1)),p(154,-1,-.6,F+.8),p(154,1,-.6,F+.8),p(155,-1.7,1.4),p(156,1.7,1.3),p(157,0,.8),p(16,1.9,-1.4)],
42:[p(158,-.9,-.3),p(158,.8,-.3),p(159,0,-1.1),p(160,1.8,-.7),p(161,-.9,-.3,F+.01),p(161,.8,-.3,F+.01),p(162,-1.8,1.4),p(163,1.7,1.4)],
43:[p(55,0,-.7,scale=(.9,.9,1)),p(36,-1.3,1.3),p(28,1.4,1.5),p(164,1.8,-.6),p(164,1.8,-.6,F+.52,scale=(.8,.8,.8)),p(165,-.6,-1.7),p(40,.1,-.7,F+.88)],
44:[p(166,0,0,scale=(2.1,2.5,1)),p(167,-1.8,.3,F+.18,rotation=90,scale=(1.5,1,1)),p(167,1.8,.3,F+.18,rotation=90,scale=(1.5,1,1)),p(167,0,1.85,F+.18,scale=(2.5,1,1)),p(168,-1.8,-.7,F+.3,euler=[90,0,90]),p(169,-.9,-.5,F+.18),p(170,1.0,1.2,F+.18),p(170,-1,1.2,F+.18),p(58,.8,-1.0,F+.18)],
45:[p(171,0,-.4),p(172,-1,.9,rotation=-15),p(172,1,.9,rotation=15),p(173,0,-1.25),p(174,-1,1,F+1.1),p(175,1.5,-.65,F+.7),p(45,1.5,-.65)],
46:[p(176,-.3,.5,scale=(1.7,1.5,1)),p(177,0,-1.6,scale=(2.3,1,1)),p(178,-1,-1.0),p(178,1,-1.0),p(168,1.8,-.9,euler=[90,0,0]),p(169,-1.9,-.6),p(133,1.3,.5),p(58,-.7,1.2),p(58,.1,1.2)],
47:[p(179,0,-.3),p(180,1.5,-.8),p(181,-1.4,1.0),p(182,1.5,1.4),p(127,-1.4,-1.2)],
48:[p(179,0,-.5),p(183,1.2,1.4),p(184,1.5,-1.1),p(185,-1.4,-1.0),p(186,-1.6,1.2),p(182,1.8,.4)],
49:[p(187,0,0),p(188,0,0),p(189,0,0,F+.04),p(190,0,1.75),p(127,-1.0,-1.65),p(127,1.0,-1.65)],
})

LAYOUTS.update({
50:[p(4,-.4,-.5),p(3,-.4,-1.4,rotation=180),p(5,-.4,-.32,F+.795),p(6,-.4,-.7,F+.795),p(191,-.5,1.65),p(27,-1,-.5,F+.795),p(9,1.7,.7),p(28,1.7,1.7)],
51:[p(31,-.4,-.75),p(31,-.5,1.0),p(39,-.5,-.65,F+.9),p(192,.2,-.65,F+.9),p(193,1.7,1.5),p(40,-.9,1.0,F+.9),p(16,1.8,-.9)],
52:[p(194,0,1.4),p(195,-1.7,.7),p(196,-1,-.4,scale=(.7,.8,1)),p(196,1,-.4,scale=(.7,.8,1)),p(197,-1,-1.1,rotation=180),p(197,1,-1.1,rotation=180),p(197,-1,-1.8,rotation=180),p(197,0,-1.8,rotation=180),p(197,1,-1.8,rotation=180),p(198,1.9,.8)],
53:[p(199,-1.5,.7),p(199,1.2,1.5),p(58,-1.7,.65,F+.65),p(58,-1.3,.65,F+1.15),p(58,1.1,1.4,F+.65),p(200,-.2,-1.2),p(58,-.2,-1.2,F+.20),p(201,1.5,-.8),p(55,-.1,.3,scale=(.6,.7,1))],
54:[p(202,0,-.6),p(203,0,.8),p(174,-.5,1,F+1.06),p(174,.5,1,F+1.06),p(175,1.5,.6,F+.7),p(204,1.6,-1),p(45,1.5,.6)],
55:[p(23,0,.1),p(58,-.5,.1,F+1.065),p(58,.5,.1,F+1.065),p(16,1.6,-.9),p(25,-.5,-1.6),p(205,-1.9,.7),p(28,1.6,1.5)],
56:[p(23,-1,.6,scale=(.8,.8,1)),p(23,1,.6,scale=(.8,.8,1)),p(5,-1,.75,F+1.065),p(5,1,.75,F+1.065),p(3,-1,1.45),p(3,1,1.45),p(24,-1.9,-.9),p(25,.1,-1.6),p(49,-.6,.6,F+1.065)],
57:[p(10,0,-.3),p(11,-.5,-1.1,rotation=180),p(11,.5,-1.1,rotation=180),p(11,0,.5),p(27,-.3,-.3,F+.80),p(206,.35,-.3,F+.80),p(9,-.3,1.65)],
58:[p(207,-.8,.9),p(108,0,-1.2),p(208,1.4,-.7),p(40,.1,-.6),p(16,1.7,1.2),p(9,-1.8,-.7)],
59:[p(4,0,-.3,scale=(.85,1,1)),p(11,-.6,-1.1,rotation=180),p(11,.6,-1.1,rotation=180),p(53,0,-.3,F+.795),p(209,.45,-.3,F+.795),p(28,-1.4,1.4),p(142,1.6,.6)],
60:[p(210,-1.4,.8),p(210,-.55,.8),p(210,.55,1.5),p(210,1.4,1.5),p(211,0,.8,F+2.08,scale=(1.4,1,1)),p(212,1.2,-.8,F+.83),p(16,1.2,-.8),p(114,-1.5,-1.1)],
61:[p(213,0,.65),p(214,-1.7,-.25,F+.8),p(214,1.7,-.25,F+.8),p(3,0,-.7,rotation=180),p(45,-1.7,-.25),p(45,1.7,-.25),p(175,1.75,.8,F+.8)],
62:[p(215,-.5,1.1),p(10,0,-.45,scale=(.7,.7,.55)),p(216,.5,-1.65,rotation=180),p(9,1.8,1.1),p(67,-.1,-.5,F+.01),p(65,-1.9,.3)],
63:[p(4,-.3,-.8),p(5,-.3,-.65,F+.795),p(217,-1.8,1.1),p(218,1.5,1.5),p(80,1.7,-.8),p(163,-1.8,-.8),p(55,.1,1.4,scale=(.7,.8,1))],
64:[p(244,0,1.1),p(245,0,1.1,F+1.23),p(246,0,1.95),p(247,-1.2,-.4,scale=(.8,1,1)),p(247,1.2,-.4,scale=(.8,1,1)),p(247,-1.2,-1.5,scale=(.8,1,1)),p(247,1.2,-1.5,scale=(.8,1,1)),p(248,1.9,1.0),p(249,-1.8,1.3)],
65:[p(4,-.5,-.6),p(3,-.5,-1.5,rotation=180),p(5,-.5,-.45,F+.795),p(6,-.5,-.8,F+.795),p(219,.6,1.6),p(175,1.9,.4,F+1.02),p(9,1.75,.4),p(28,-1.5,1.5)],
66:[p(44,-1.25,.3),p(44,1.25,.3),p(45,0,.7),p(54,-1.3,1.7,scale=(.7,1,.9)),p(54,1.3,1.7,scale=(.7,1,.9)),p(220,-.9,-1.4),p(220,1.3,-1.4),p(221,.2,-1.2)],
67:[p(28,-1.3,1.5),p(28,1.3,1.5),p(55,0,-.5),p(77,.1,1.5),p(80,1.8,-.7),p(114,-1.4,-1.1),p(114,-1.3,1.5,F+.6),p(16,-1.9,.2)],
68:[p(10,0,-.3,scale=(.85,.85,1)),p(11,0,-1.1,rotation=180),p(12,-.3,-.2,F+.80),p(222,.35,-.3,F+.80),p(223,.1,-.55,F+.80),p(221,-1.3,-.6),p(142,1.3,.1)],
69:[p(224,0,1.35),p(205,1.9,.8),p(127,-1.3,-.8),p(142,1.4,-.9),p(225,-.2,-1.7),p(225,1.5,-1.7),p(225,-1.8,.7),p(143,-1.7,1.5)],
70:[p(250,0,1.2),p(251,0,1.2,F+.91),p(252,-1.1,-.35),p(252,0,-.35),p(252,1.1,-.35),p(252,-1.1,-1.3),p(252,0,-1.3),p(252,1.1,-1.3),p(253,0,.5),p(254,.8,.55),p(255,-.7,1.15,F+.91),p(256,.65,1.15,F+.91)],
71:[p(257,0,1.1),p(258,-1.9,1.0),p(259,0,1.8,F+.65),p(260,-.4,1.0,F+.95),p(261,.35,1.0,F+.95),p(262,-1.3,1.35,F+.1),p(262,1.3,1.35,F+.1),p(247,-1.2,-.6,scale=(.8,1,1)),p(247,1.2,-.6,scale=(.8,1,1)),p(247,-1.2,-1.6,scale=(.8,1,1)),p(247,1.2,-1.6,scale=(.8,1,1))],
})

# Secondary objects from the exact required-candidate list remain explicit,
# including desktop peripherals and visitor seating behind service counters.
LAYOUTS[8]=[item for item in LAYOUTS[8] if not(item['candidate_id']=='CND-011' and item['position'][1]>.1)]
SUPPLEMENTS={
8:[p(3,-1,.15)],9:[p(9,-1.7,1.6,scale=(.65,.8,1))],
11:[p(3,0,1.25),p(6,.1,.05,F+1.065),p(17,1.3,.45),p(18,.55,.05,F+1.065)],
13:[p(40,.1,1,F+.88)],16:[p(9,1.8,-1.1,scale=(.8,.8,.7))],19:[p(56,-.3,-1.3)],20:[p(43,1.9,1.5)],
21:[p(9,-.2,-.8,scale=(.6,.8,1))],22:[p(3,0,1.2),p(6,.25,.05,F+1.065),p(17,1.3,.5),p(18,.65,.05,F+1.065)],
23:[p(11,-1.8,-1.3),p(28,1.75,1.7,scale=(.6,.8,.8))],25:[p(58,-1.9,-1.4)],26:[p(65,1.8,1.7)],27:[p(49,-1.35,-.5,F+.795)],
28:[p(10,-1.4,-1.2,scale=(.6,.6,.55))],29:[p(43,-1.8,1.7)],33:[p(111,-1.8,1.5),p(111,1.8,1.5)],36:[p(80,1.8,-1.5)],
43:[p(67,0,-.7,F+.01,scale=(.8,.5,1))],44:[p(9,-1.2,1.2,F+.18,scale=(.7,.8,.7))],
50:[p(11,-1.6,-1.2,rotation=180),p(17,.2,-.4),p(18,0,-.7,F+.795),p(49,-1,-.5,F+.795)],
51:[p(5,-.4,1.05,F+.90),p(6,-.4,.8,F+.90),p(17,.6,1),p(18,0,.8,F+.90)],
54:[p(5,-1,.9,F+1.05)],55:[p(127,1.1,-1.6)],
56:[p(6,-1,.4,F+1.065),p(6,1,.4,F+1.065),p(11,0,-.55,rotation=180),p(17,1.9,.6),p(18,-.6,.4,F+1.065)],
57:[p(12,0,-.1,F+.8)],58:[p(67,0,-.8,F+.01,scale=(.65,.6,1))],60:[p(37,-2.2,-.7,scale=(.6,.9,1.4))],
61:[p(5,.7,.6,F+1.1)],63:[p(9,1.8,.1,scale=(.7,.7,.8)),p(28,1.7,1.7,scale=(.6,.8,1))],
65:[p(11,1.5,-1.1),p(17,.2,-.5),p(18,-.15,-.8,F+.795)],66:[p(10,0,-.8,scale=(.5,.5,.7)),p(11,0,-1.6)],
69:[p(221,1.9,-1.1)]}
for number,items in SUPPLEMENTS.items():LAYOUTS[number].extend(items)


# v002 repair pass: preserve every v001 source/export, align physical support.
# CND-016 upper tray solid surface: z=.84+.055/2=.8675 (handle is higher).
for number in [8,10]:
    for item in LAYOUTS[number]:
        if item['candidate_id']=='CND-042':
            if number==8:item['position']=[-.1,1.5,F+.8675]
            else:item['position'][2]=F+.8675
    LAYOUTS[number].append(p(16,-.1 if number==8 else 1.15,1.5 if number==8 else 1.15))
for item in LAYOUTS[14]:
    if item['candidate_id']=='CND-061':item['position'][2]=F+.8675
LAYOUTS[14].append(p(16,1.8,.9))
# A case handle crosses its lid; use the existing workbench as a solid support.
for item in LAYOUTS[39]:
    if item['candidate_id']=='CND-146':item['position'][2]=F+.484-.0004
    if item['candidate_id']=='CND-114':item['position']=[1.8,-.9,F]
LAYOUTS[39].append(p(55,.8,-1.15,scale=(.65,.8,.55)))
# Actual bedside-table top from final GLB AABB: .6174999475m.
for number in [45,54]:
    for item in LAYOUTS[number]:
        if item['candidate_id']=='CND-175':item['position'][2]=F+.6175
# The CND-104 easel legitimately includes its main mounted canvas; CND-105
# is a spare, resting on the floor and leaning against the rear shelf.
for item in LAYOUTS[28]:
    if item['candidate_id']=='CND-105':
        item['position']=[1.3,1.08,F];item['euler']=[-10,0,0]
# Existing AST-005 foot lower face is .0425m above its source origin.
# Align to the actual support plane rather than copying the origin-to-top gap.
monitor_support={3:.795,4:1.06,7:.795,8:.795,11:1.06,22:1.06,27:.795,
32:.795,50:.795,51:.90,54:1.064,56:1.06,61:1.064,63:.795,65:.795}
for number,height in monitor_support.items():
    for item in LAYOUTS[number]:
        if item['candidate_id']=='CND-005':item['position'][2]=F+height-.0425
# Navigation displays rest on the instrument console rather than hovering.
for number in [45,54]:
    for item in LAYOUTS[number]:
        if item['candidate_id']=='CND-174':item['position'][2]=F+1.064
REPAIR_NUMBERS=[3,4,7,8,10,11,14,22,27,28,32,39,45,50,51,54,56,61,63,65]


# v003: the bedside call panel mounts on the front face of the rear headboard.
# Bed44 root Y=.1 + board center .97 - half thickness .035 = Y1.035.
# Call panel local rear face Y=.035; root Y1.0 therefore contacts Y1.035.
for item in LAYOUTS[10]:
    if item['candidate_id']=='CND-048':item['position']=[-.32,1.0,F+.72]
REPAIR_NUMBERS=[10]

def resolve():
    catalog=shared.read('assets')['assets'];lookup={(a['asset_id'],a['version']):a for a in catalog}
    candidates=shared.read('workplace-asset-candidates-v003')['candidates'];resolved={}
    for c in candidates:
        n=int(c['candidate_id'].split('-')[1]);key=(f'AST-{1000+n}','v001')
        if key in lookup:resolved[c['candidate_id']]=lookup[key]
        elif c['existing_asset_candidates']:
            # Prefer direct existing source over paid comparison or historical base.
            old=c['existing_asset_candidates'][0]['asset_ref'];key=(old['asset_id'],old['version'])
            if key in lookup:resolved[c['candidate_id']]=lookup[key]
    return resolved

def produce(number):
    aid=f'AST-{2000+number}';version='v003';scene=next(s for s in shared.read('workplace-asset-candidates-v003')['scenes'] if s['prompt_ref']['prompt_id']==f'PRM-{number:03}')
    out=ROOT/f'meshy/models/blender/{aid}/{version}';src=ROOT/f'meshy/models/original/{aid}/{version}'
    if (out/'inspection.json').exists():print('PRESERVED',aid,flush=True);return
    if (out/'model.blend').exists():raise RuntimeError('Partial room preserved: inspect before retry')
    mapping=resolve();items=[p(1,0,0,0,scale=(3,2.6,1.8)),p(2,0,0,.288,scale=(2.85,2.45,1))]+LAYOUTS[number]
    missing=set(scene['required_candidate_ids'])-{x['candidate_id'] for x in items}
    if missing:raise RuntimeError(f'Missing required candidates {missing}')
    if any(x['candidate_id'] not in mapping for x in items):raise RuntimeError('Unproduced candidate: no placeholders permitted')
    shared.reset();material=shared.MATERIAL;placements=[]
    for idx,item in enumerate(items):
        asset=mapping[item['candidate_id']];before=set(bpy.context.scene.objects)
        bpy.ops.import_scene.gltf(filepath=str(ROOT/asset['runtime_path']))
        imported=[o for o in bpy.context.scene.objects if o not in before]
        meshes=[o for o in imported if o.type=='MESH']
        root=bpy.data.objects.new(f'{asset["asset_id"]}-{idx:03}',None);bpy.context.collection.objects.link(root)
        for obj in imported:
            if obj.parent is None:obj.parent=root
        root.location=item['position'];root.scale=item['scale']
        angles=item['euler'] or [0,0,item['rotation']]
        root.rotation_euler=[math.radians(x) for x in angles]
        for obj in meshes:
            obj.data.materials.clear();obj.data.materials.append(material)
            for poly in obj.data.polygons:poly.material_index=0
        placements.append(dict(asset_id=asset['asset_id'],version=asset['version'],candidate_id=item['candidate_id'],instance_id=root.name,position_blender_m=item['position'],rotation_euler_blender_deg=angles,rotation_z_rad=math.radians(item['rotation']),scale=item['scale'],component_mesh_count=len(meshes)))
    meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
    for obj in bpy.context.scene.objects:obj.select_set(True)
    total=sum(len(poly.vertices)-2 for obj in meshes for poly in obj.data.polygons)
    if total>5000:raise RuntimeError(f'Room {number} needs optimization: {total} triangles')
    (out/'exports').mkdir(parents=True,exist_ok=True);(src/'previews').mkdir(parents=True,exist_ok=True)
    bpy.ops.wm.save_as_mainfile(filepath=str(src/'source.blend'));bpy.ops.wm.save_as_mainfile(filepath=str(out/'model.blend'))
    glb=out/'exports/model.glb';bpy.ops.export_scene.gltf(filepath=str(glb),export_format='GLB',use_selection=True)
    bpy.ops.export_scene.fbx(filepath=str(out/'exports/room.fbx'),use_selection=True,add_leaf_bones=False,bake_anim=False,axis_forward='-Z',axis_up='Y',path_mode='STRIP')
    shared.write(out/'placements.json',dict(schema_version=3,prompt_ref=scene['prompt_ref'],panorama_ref=scene['panorama_ref'],coordinate_system='Blender Z-up meters',instances=placements))
    shared.reset();bpy.ops.import_scene.gltf(filepath=str(glb))
    meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
    measured=sum(len(poly.vertices)-2 for obj in meshes for poly in obj.data.polygons)
    materials={m for obj in meshes for m in obj.data.materials};textures={n.image for m in materials for n in m.node_tree.nodes if n.type=='TEX_IMAGE' and n.image}
    centers=[c['uv_center'] for c in shared.MAPPING['cells']]
    uvok=all(o.data.uv_layers.active and all(any(abs(loop.uv.x-u)<1e-5 and abs(loop.uv.y-v)<1e-5 for u,v in centers) for loop in o.data.uv_layers.active.data) for o in meshes)
    counts={}
    for instance in placements:
        key=(instance['asset_id'],instance['version']);counts[key]=counts.get(key,0)+1
    assets=shared.read('assets')['assets'];lookup={(a['asset_id'],a['version']):a for a in assets}
    props=[]
    for key,quantity in counts.items():
        a=lookup[key];inspection=json.loads((ROOT/a['inspection_path']).read_text('utf-8'))
        tri=inspection['scene_triangles'];props.append(dict(name=a['name'],asset_ref=dict(asset_id=key[0],version=key[1]),triangles_per_instance=tri,instance_count=quantity,total_triangles=tri*quantity))
    if sum(x['total_triangles'] for x in props)!=measured:raise RuntimeError('Component/assembly GLB counts differ')
    unverified=lambda why:dict(status='unverified',evidence=None,reason=why)
    ck=lambda ok,why:dict(status='pass' if ok else 'fail',evidence=why,reason=None)
    report=dict(schema_version=3,asset_id=aid,version=version,kind='diorama',target_web_environment='Unity WebGL room browser, HTTP execution pending',props=props,scene_triangles=measured,material_count=len(materials),texture_count=len(textures),palette_resolution=[2508,2508],glb_bytes=glb.stat().st_size,checks=dict(scene_budget=ck(measured<=5000,'Actual final GLB Blender reimport; every repeated placement included'),component_budget=ck(all(x['triangles_per_instance']<=1000 for x in props),'Component final GLB measurements'),palette_uv=ck(uvok,'Every final GLB UV matches shared mapping'),shared_material=ck(len(materials)==len(textures)==1,'Final GLB nodes'),visual_layout=unverified('Preview produced; detailed silhouette, part-color and collision review pending'),web_display=unverified('Unity HTTP runtime pending')),remaining_issues=['Space assembly produced; visual/runtime verification and interaction are separate.','Unapproved scenario drafts not automatically selected.'])
    shared.write(out/'inspection.json',report);shared.render_preview(src/'previews/front.png')
    rel=lambda path:path.relative_to(ROOT).as_posix()
    entry=dict(asset_id=aid,version=version,name=scene['name'],source_path=rel(src/'source.blend'),blender_path=rel(out/'model.blend'),runtime_path=rel(glb),preview_path=rel(src/'previews/front.png'),unity_path=None,kind='diorama',palette_version='v001',accent_reason=None,unity_palette_path=None,inspection_path=rel(out/'inspection.json'),processing_paths=[SCRIPT,SHARED],status='in_progress',generation_method='blender_direct',generation_reason='Reuse fixed individual assets; explicit reference-informed spatial relationships and quantities.',production_record_path=rel(src/'README.md'),meshy_credits_used=0,source_images=[scene['panorama_ref']])
    catalog=shared.read('assets');catalog['assets'].append(entry);shared.write(CAT/'assets.json',catalog)
    now=datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9))).isoformat()
    assemblies=shared.read('scene-assemblies');assemblies['assemblies'].append(dict(assembly_id=f'pan-{number:03}-workplace',revision=1+max((a['revision'] for a in assemblies['assemblies'] if a['assembly_id']==f'pan-{number:03}-workplace'),default=0),recorded_at=now,environment='blender_and_independent_glb',assembly_asset_ref={'asset_id':aid,'version':version},panorama_ref=scene['panorama_ref'],prompt_ref=scene['prompt_ref'],placements_path=rel(out/'placements.json'),inspection_path=rel(out/'inspection.json'),component_counts=props,aggregation_basis='Components only; assembly parent excluded from quantity and triangle sum.'))
    shared.write(CAT/'scene-assemblies.json',assemblies)
    (src/'README.md').write_text(f'# {aid} {version} — {scene["name"]}\n\n2026-10-31 Blender 직접 조립. Meshy·이미지 생성 0회, 이번 크레딧 0. 기존 구성 에셋의 과거 생성 비용은 이번 비용에 합산하지 않는다.\n\n기준 파노라마 {scene["panorama_ref"]["image_id"]} {scene["panorama_ref"]["version"]}, {scene["prompt_ref"]["prompt_id"]} {scene["prompt_ref"]["version"]}.\n공간 의도: {scene["layout_intent"]}. 배치·수량은 placements.json, 구성 부품·실측 삼각형은 inspection.json.\n\n스크립트: {SCRIPT}, {SHARED}. 원본·Blender 수정본·실제 GLB·FBX·미리보기를 구분해 보존. 공용 palette v001 원본 색 유지. 독립 정답 버튼 체험이나 파노라마 스카이박스가 아니다.\n\n디자인 치수·배치는 가상 공간용이며 실물 실측이 아니다. 원본 참고 자료 권리의 외부 독립 검증 없음. 최종 GLB 재가져오기 검사를 수행했으며 Unity·웹·전체 방향·부위별 색상은 미검증.\n','utf-8')
    progress=shared.read('workplace-production-v001')
    for row in progress['scenes']:
        if row['prompt_ref']==scene['prompt_ref']:row.update(production_status='assembled_runtime_unverified',assembly_asset_ref={'asset_id':aid,'version':version},evidence_paths=[rel(out/'inspection.json'),rel(out/'placements.json')]);row['checks']['final_glb']='pass'
    progress['updated_at']=now;shared.write(CAT/'workplace-production-v001.json',progress)
    print('ASSEMBLED',aid,measured,glb.stat().st_size,flush=True)

if __name__=='__main__':
    args=sys.argv[sys.argv.index('--')+1:] if '--' in sys.argv else []
    for number in ([int(x) for x in args] if args else REPAIR_NUMBERS):produce(number)


if __name__=='__main__':
    # Reopen the final GLB and independently compare actual world-space parts.
    from mathutils import Vector
    out=ROOT/'meshy/models/blender/AST-2010/v003'
    bpy.ops.wm.read_factory_settings(use_empty=True)
    bpy.ops.import_scene.gltf(filepath=str(out/'exports/model.glb'))
    bpy.context.view_layer.update()
    def within(obj,prefix):
        node=obj
        while node:
            if node.name.startswith(prefix):return True
            node=node.parent
        return False
    def bounds(obj):
        corners=[obj.matrix_world@Vector(c) for c in obj.bound_box]
        return dict(min=[min(p[i] for p in corners) for i in range(3)],max=[max(p[i] for p in corners) for i in range(3)])
    meshes=[o for o in bpy.context.scene.objects if o.type=='MESH']
    bed=[(o,bounds(o)) for o in meshes if within(o,'AST-1044-')]
    panel=[(o,bounds(o)) for o in meshes if within(o,'AST-1048-')]
    assert panel and bed
    board=max(bed,key=lambda pair:pair[1]['max'][1])[1]
    panel_min=[min(b['min'][i] for o,b in panel) for i in range(3)]
    panel_max=[max(b['max'][i] for o,b in panel) for i in range(3)]
    gap=board['min'][1]-panel_max[1]
    within_face=all(panel_min[i]>=board['min'][i]-1e-5 and panel_max[i]<=board['max'][i]+1e-5 for i in [0,2])
    assert abs(gap)<1e-5 and within_face,(gap,within_face,board,panel_min,panel_max)
    evidence=dict(schema_version=3,asset_ref={'asset_id':'AST-2010','version':'v003'},environment='Actual Blender final GLB reimport',call_panel_world_bounds_m=dict(min=panel_min,max=panel_max),headboard_world_bounds_m=board,rear_face_to_headboard_gap_m=gap,within_headboard_face=within_face)
    shared.write(out/'call-panel-mount.json',evidence)
    inspection=json.loads((out/'inspection.json').read_text('utf8'))
    inspection['checks']['call_panel_mount']=dict(status='pass',evidence='meshy/models/blender/AST-2010/v003/call-panel-mount.json',reason=None)
    shared.write(out/'inspection.json',inspection)
    print('CALL_PANEL_MOUNT',gap,within_face,flush=True)

#############################
#           CHARACTER       #
#############################

default l_name = "Lucy"
define l = DynamicCharacter(
    'l_name',
    what_prefix='"',
    what_suffix='"',
    ctc="ctc",
    ctc_position="fixed",
    namebox_background=Frame("gui/namebox/lucy.png", gui.namebox_borders),
    image="lucy"
)

default p_name = "Paimon"
define p = DynamicCharacter(
    'p_name',
    what_prefix='"',
    what_suffix='"',
    image='paimon',
    namebox_background=Frame("gui/namebox/paimon.png", gui.namebox_borders),
    ctc="ctc",
    ctc_position="fixed"
)

define narrator = Character(
    ctc="ctc",
    ctc_position="fixed")

init python:
    def eyewarp(x):
        return x**1.33

#############################
#           IMAGES          #
#############################
image bg highway:
    im.Blur("images/bg/highway.jpg", 2.5)

image paimon = ("images/bg/Paimon.webp")


#############################
#       TRANSITIONS         #
#############################

# Transform that blurs the background when opening screens.
transform withBlur:
    blur 30
transform noBlur:
    blur 0

transform tcommon:
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 0.95 alpha 0.0
        xcenter 0.5 yoffset -20
        easein .25 yoffset 0 zoom 1.00 alpha 1.0
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter 0.5 zoom 1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03
    on hide:
        easein .25 zoom 0.95 alpha 0.0 yoffset -20


#############################
#        TRANSITIONS        #
#############################
# define config.say_attribute_transition = Dissolve(.25, alpha=True)
# define config.say_attribute_transition_layer = "master"
# init:
#     $ fastdiv = {"master" : wipeleft}

define wipeleft = ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64)
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64),
    True])
    
define long_dissolve = MultipleTransition([
    False, Dissolve(1.5),
    Solid("#000"), Pause(1.5),
    Solid("#000"), Dissolve(1.5),
    True])

define eye_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/eyes.png", .5, ramplen=128, reverse=True, time_warp=eyewarp),
    Solid("#000"), Pause(1),
    Solid("#000"), ImageDissolve("images/transitions/eyes.png", .5 ,ramplen=128, time_warp=eyewarp),
    True])

define wipeleft_menu = ImageDissolve("images/transitions/wipeleft.png", 0.10, ramplen=64)
define wipeleft_menu_reverse = ImageDissolve("images/transitions/wipeleft.png", 0.10, reverse=True, ramplen=64)
define wipeleft_menu_afterLoad = MultipleTransition([
    False, ImageDissolve("images/transitions/wipeleft.png", 0.10, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/wipeleft.png", 0.10, ramplen=64),
    True])

image camera_flash:
    Solid("#ffffff2c")
    pause 0.1
    Solid("#00000000")

#############################
#           AUDIO           #
#############################
define audio.merrygoround2 = "<loop 24.162>audio/bgm/merrygoround2.mp3"

image lucy_eyes:
    "images/characters/lucy/face/eyes_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/lucy/face/eyes_closed.png"
    .10
    repeat

image lucy_eyes_look:
    "images/characters/lucy/face/eyes_look.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/lucy/face/eyes_closed.png"
    .10
    repeat

image lucy_eyes_anxious:
    "images/characters/lucy/face/eyes_anxious.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/lucy/face/eyes_closed.png"
    .10
    repeat

layeredimage lucy:

    group base: #body
        attribute l_base1 default:
            "lucy 1l_1r"
        attribute l_base2:
            "lucy 2l_2r"
        attribute l_base3:
            "lucy 1l_2r"
        attribute l_base4:
            "lucy 2l_1r"

    group water:
        attribute l_sweat:
            "images/characters/lucy/face/sweat.png"
        attribute l_cry:
            "images/characters/lucy/face/cry.png"

    group eyes:
        attribute l_eyes default:
            "lucy_eyes"
        attribute l_eyes_look:
            "lucy_eyes_look"
        attribute l_eyes_closed:
            "images/characters/lucy/face/eyes_closed.png"
        attribute l_eyes_closedhappy:
            "images/characters/lucy/face/eyes_closedhappy.png"
        attribute l_eyes_anxious:
            "lucy_eyes_anxious"

    group brows:
        attribute l_brow default:
            "images/characters/lucy/face/brow_normal.png"
        attribute l_brow_sad:
            "images/characters/lucy/face/brow_sad.png"
        attribute l_brow_serious:
            "images/characters/lucy/face/brow_serious.png"

    group mouth:
        attribute l_mouth default:
            "images/characters/lucy/face/mouth_smile.png"
        attribute l_mouth_open:
            "images/characters/lucy/face/mouth_open.png"
        attribute l_mouth_slightopen:
            "images/characters/lucy/face/mouth_slightopen.png"
        attribute l_mouth_serious:
            "images/characters/lucy/face/mouth_serious.png"


image lucy 1l_1r = Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/1l.png", (0, 0), "images/characters/lucy/1r.png")
image lucy 2l_2r = Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/2l.png", (0, 0), "images/characters/lucy/2r.png")
image lucy 1l_2r = Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/1l.png", (0, 0), "images/characters/lucy/2r.png")
image lucy 2l_1r = Composite((960, 960), (0, 0), "images/characters/lucy/lucy_head.png", (0, 0), "images/characters/lucy/2l.png", (0, 0), "images/characters/lucy/1r.png")
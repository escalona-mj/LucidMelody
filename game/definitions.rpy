# init -1 python: 
#     def callback_builder(character_sprite_basename):
#         def char_callback(event, **kwargs):
#             if event == "show_done":
#                 renpy.show(character_sprite_basename + " l_talk")
#             elif event == "slow_done":
#                 renpy.show(character_sprite_basename + " -l_talk")
#                 renpy.restart_interaction()
#         return char_callback

#############################
#           CHARACTER       #
#############################

default mcName = ""
define dhannica = DynamicCharacter(
    'mcName',
    what_prefix='"',
    what_suffix='"',
    ctc="ctc",
    ctc_position="fixed",
    namebox_background=Frame("gui/namebox/lucy.png", gui.namebox_borders),
    image="dhannica"
)

define alec = DynamicCharacter(
    'mcName',
    what_prefix='"',
    what_suffix='"',
    ctc="ctc",
    ctc_position="fixed",
    namebox_background=Frame("gui/namebox/lucy.png", gui.namebox_borders),
    image="alec"
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
    blur 10
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

image dhannica_blink:
    "images/characters/dhannica/face/eyes_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/dhannica/face/eyes_closed.png"
    .10
    repeat

layeredimage dhannica:

    group base: #body
        attribute base default:
            "images/characters/dhannica/base.png"

    group eyes:
        attribute d_blink default:
            "dhannica_blink"
        attribute d_eyeclose:
            "images/characters/dhannica/face/eyes_closed.png"

    group brows:
        attribute d_brow default:
            "images/characters/dhannica/face/brow_normal.png"

    group accesories:
        attribute glasses default:
            "images/characters/dhannica/face/glasses.png"

image alec_blink:
    "images/characters/alec/face/eyes_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/alec/face/eyes_closed.png"
    .10
    repeat

layeredimage alec:

    group base: #body
        attribute base default:
            "images/characters/alec/base.png"

    group eyes:
        attribute a_blink default:
            "alec_blink"
        attribute a_eyeclose:
            "images/characters/alec/face/eyes_closed.png"

    group brows:
        attribute a_brow default:
            "images/characters/alec/face/brow_normal.png"

#blue 014d81
#pantone 6463b1
#pink eb7e8a
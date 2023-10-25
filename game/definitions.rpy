# init -1 python: 
#     def callback_builder(character_sprite_basename):
#         def char_callback(event, **kwargs):
#             if event == "show_done":
#                 renpy.show(character_sprite_basename + " talk")
#             elif event == "slow_done":
#                 renpy.show(character_sprite_basename + " -talk")
#                 renpy.restart_interaction()
#         return char_callback

init python:
    class DisableSkip():
        def start():
            _skipping = False #disable skip
            config.skipping = False # if skipping, stop it
            config.allow_skipping = False #prevents from skipping
        def stop():
            _skipping = True
            config.allow_skipping = True


#############################
#           CHARACTER       #
#############################

define dhannica_i = Character(
    '[Main]',
    ctc="ctc",
    ctc_position="nestled",
    what_prefix='{i}',
    what_suffix='{/i}',
    color='#ff9b9b'
)

define alec_i = Character(
    '[Main]',
    ctc="ctc",
    ctc_position="nestled",
    what_prefix='{i}',
    what_suffix='{/i}',
    color='#21a733'
)

define speak = Character(
    what_prefix='"',
    what_suffix='"',
    ctc="ctc",
    ctc_position="nestled"
)

default mcNamegirl = ""
define dhannica = DynamicCharacter(
    'mcNamegirl',
    kind=speak,
    color='#ff9b9b',
    image="dhannica"
)

define girlMom = Character(
    'Mom',
    kind=speak,
)

default mcNameboy = ""
define alec = DynamicCharacter(
    'mcNameboy',
    kind=speak,
    color='#21a733',
    image="alec"
)

default n_name = "Nick"
define nick = DynamicCharacter(
    'n_name',
    kind=speak,
    color='#4076ff',
    image='nick'
)

define narrator = Character(
    ctc="ctc",
    ctc_position='nestled'
)

define d_singer = Character(
    'Singer',
    kind=speak,
    color='#fff'
    )

#############################
#           IMAGES          #
#############################
image bg highway:
    im.Blur("images/bg/highway.jpg", 2.5)

image bg dhannica room:
    im.Blur("images/bg/dhannica_room.png", 2.5)

image bg stage:
    im.Blur("images/bg/stage.jpg", 2.5)

image bg living room:
    im.Blur("images/bg/livingroom.jpg", 2.5)

image bg school:
    im.Blur("images/bg/school.jpg", 2.5)
#############################
#       TRANSFORMS          #
#############################

# Transform that blurs the background when opening screens.
transform withBlur:
    blur 0
    easein .25 blur 30
transform noBlur:
    blur 30
    easein .25 blur 0

transform appear(x):
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03 zoom 0.95 alpha 0.0 xalign x
        easein .25 zoom 1.0 alpha 1.0
    on replace:
        alpha 1.0
        parallel:
            easein .25 xalign x zoom 1.0 ypos 1.03
    on hide:
        easein .25 zoom 0.95 alpha 0.0

transform appear_center:
    appear(0.5)
transform appear_left:
    appear(0.25)
transform appear_right:
    appear(0.75)

transform dizzy:
    subpixel True
    truecenter
    ease 0.2 zoom 1.2
    parallel:
        choice:
            ease_quad 1.0 xoffset 5 yoffset 10
        choice:
            ease_quad 1.0 xoffset -5 yoffset 10
        choice:
            ease_quad 1.0 xoffset 5 yoffset -10
        choice:
            ease_quad 1.0 xoffset -5 yoffset -10
        repeat
    parallel:
        choice:
            ease_quad 5.0 rotate 2
        choice:
            ease_quad 5.0 rotate 4
        choice:
            ease_quad 5.0 rotate -2
        choice:
            ease_quad 5.0 rotate -4
        repeat
    parallel:
        choice:
            ease 0.3 zoom 1.15
            ease 1.0 zoom 1.2
        choice:
            ease 0.2 zoom 1.15
            ease 1.0 zoom 1.2
        choice:
            ease 0.9 zoom 1.15
            ease 1.0 zoom 1.2
        repeat
    parallel:
        ease_quad 1.0 blur 0
        ease_quad 1.0 blur 10
        repeat

#############################
#        TRANSITIONS        #
#############################

init python:
    def eyewarp(x):
        return x**1.33

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

define eye_close = ImageDissolve("images/transitions/eyes.png", 0.25, ramplen=128, reverse=True, time_warp=eyewarp)

define eye_open = ImageDissolve("images/transitions/eyes.png", 0.25 ,ramplen=128, time_warp=eyewarp)

define eye_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/eyes.png", 0.25, ramplen=128, reverse=True),
    Solid("#000"), Pause(0.5),
    Solid("#000"), ImageDissolve("images/transitions/eyes.png", 0.25 ,ramplen=128),
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
define audio.titlescreen = "audio/bgm/titlescreen.mp3"
define audio.merrygoround2 = "<loop 24.162>audio/bgm/merrygoround2.mp3"

define audio.alarm = "audio/sfx/alarm.mp3"
define audio.alarmloop = "<from 0.160 to 1.113>audio/sfx/alarm.mp3"
define audio.cheer = "audio/sfx/cheer.ogg"
define audio.doorclose = "audio/sfx/doorclose.mp3"
define audio.phone_notif = "audio/sfx/phone_notif.ogg"
define audio.stomachgrowl = "audio/sfx/stomachgrowl.ogg"
define audio.thump = "audio/sfx/thump.mp3"



#############################
#      LAYERED IMAGES       #
#############################

###### DHANNICA ######

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
        attribute blink default:
            "dhannica_blink"
        attribute eyeclose:
            "images/characters/dhannica/face/eyes_closed.png"

    group brows:
        attribute brow default:
            "images/characters/dhannica/face/brow_normal.png"

    group accesories:
        attribute glasses default:
            "images/characters/dhannica/face/glasses.png"

###### ALEC ######

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
        attribute blink default:
            "alec_blink"
        attribute eyeclose:
            "images/characters/alec/face/eyes_closed.png"

    group brows:
        attribute brow default:
            "images/characters/alec/face/brow_normal.png"

###### NICK ######

image nick_blink:
    "images/characters/nick/face/eyes_normal.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/characters/nick/face/eyes_closed.png"
    .10
    repeat

layeredimage nick:

    group base: #body
        attribute base default:
            "images/characters/nick/base.png"

    group eyes:
        attribute blink default:
            "nick_blink"
        attribute eyeclose:
            "images/characters/nick/face/eyes_closed.png"

    group brows:
        attribute brow default:
            "images/characters/nick/face/brow_normal.png"

#blue 014d81
#pantone 6463b1
#pink eb7e8a
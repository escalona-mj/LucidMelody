##########################################################################################################
#                                               FUNCTIONS                                                #
##########################################################################################################
init python: 
    def narrator_beep(event, **kwargs):
        if event == "show" or event == "show_done":
            renpy.sound.play("audio/voice/narrator.ogg", channel="voice", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="voice")
        return narrator_beep

    def dhannica_beep(event, **kwargs):
        if event == "show" or event == "show_done":
            renpy.sound.play("audio/voice/dhannica.ogg", channel="voice", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="voice")
        return dhannica_beep

    def alec_beep(event, **kwargs):
        if event == "show" or event == "show_done":
            renpy.sound.play("audio/voice/alec.ogg", channel="voice", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="voice")
        return alec_beep

    class DisableSkip():
        def start():
            global _game_menu_screen
            _game_menu_screen = None
            config.skipping = False # if skipping, stop it
            config.allow_skipping = False #prevents from skipping
        def stop():
            global _game_menu_screen
            _game_menu_screen = 'emptymenu'
            config.allow_skipping = True


##########################################################################################################
#                                               CHARACTERS                                               #
##########################################################################################################
define narrator = Character(ctc="ctc", ctc_position='fixed', callback=narrator_beep)
define speak = Character(what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", callback=narrator_beep)

#thought MC
define dhannica_i = Character('[Main]', ctc="ctc", ctc_position="fixed", what_prefix='{i}', what_suffix='{/i}', color='#ff9b9b', image="dhannica")
define nick_i = Character('[Main]', ctc="ctc", ctc_position="fixed", what_prefix='{i}', what_suffix='{/i}', color='#4076ff')

#characters
default mcNamegirl = ""
define dhannica = DynamicCharacter('mcNamegirl', kind=speak, color='#ff9b9b', image="dhannica", callback=dhannica_beep)
define offscr_dhannica = DynamicCharacter('mcNamegirl', kind=dhannica, image="offscr_dhannica")

default mcNameboy = ""
define nick = DynamicCharacter('mcNameboy', kind=speak, color='#4076ff', image='nick')
define offscr_nick = DynamicCharacter('mcNameboy', kind=nick, image='offscr_nick')

default a_name = "Alec"
define alec = DynamicCharacter('a_name', kind=speak, color='#21a733', image="alec", callback=alec_beep)
define offscr_alec = DynamicCharacter('a_name', kind=alec, image="offscr_alec")

#side characters
define girlMom = Character('Mom', kind=speak)
define d_singer = Character('Singer',kind=speak)
define prof = Character('Prof', kind=speak)
define unknown_guy = Character('???', kind=speak, image="unknown_guy")

######################################################################################################
#                                               IMAGES                                               #
######################################################################################################
image bg highway:
    im.Blur("images/bg/highway.jpg", 2.5)

image bg dhannica room:
    im.Blur("images/bg/dhannica_room.png", 2.5)

image bg stage:
    im.Blur("images/bg/stage.png", 2.5)

image bg living room:
    im.Blur("images/bg/livingroom.png", 2.5)

image bg school:
    im.Blur("images/bg/school.jpg", 2.5)

image bg busstop:
    im.Blur("images/bg/busstop.png", 2.5)

image bg busstop_no_bus:
    im.Blur("images/bg/busstop_no_bus.png", 2.5)

image bg bus:
    im.Blur("images/bg/bus.png", 2.5)

image bg school hallway:
    im.Blur("images/bg/schoolhallway.png", 2.5)

image bg classroom:
    im.Blur("images/bg/classroom.png", 2.5)


image mom = "images/characters/mom.png"

image camera_flash:
    Solid("#ffffff2c")
    pause 0.1
    Solid("#00000000")

##########################################################################################################
#                                               TRANSFORMS                                               #
##########################################################################################################

# Transform that blurs the background when opening screens.
transform withBlur:
    blur 0
    blur 30
transform noBlur:
    blur 30
    blur 0

transform dialogue_withBlur:
    blur 0
    easein .25 blur 30
transform dialogue_noBlur:
    blur 30
    easein .25 blur 0

# character transforms
transform trans(x):
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

transform trans1:
    trans(0.0)
transform trans2:
    trans(0.25)
transform trans3:
    trans(0.50)
transform trans4:
    trans(0.75)
transform trans5:
    trans(1.0)

# camera transforms
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
    # parallel:
    #     choice:
    #         ease 0.3 zoom 1.15
    #         ease 1.0 zoom 1.2
    #     choice:
    #         ease 0.2 zoom 1.15
    #         ease 1.0 zoom 1.2
    #     choice:
    #         ease 0.9 zoom 1.15
    #         ease 1.0 zoom 1.2
    #     repeat
    parallel:
        ease_quad 1.0 blur 0
        ease_quad 1.0 blur 10
        repeat

transform reset_dizzy:
    parallel:
        ease_quad 1.0 xoffset 0
    parallel:
        ease_quad 1.0 yoffset 0
    parallel:
        ease_quad 1.0 blur 0
    parallel:
        ease_quad 1.0 rotate 0
    parallel:
        ease_quad 1.0 zoom 1.0


#APPARENTLY, YOU CAN USE ATL TRANSFORMATIONS AS TRANSITIONS
transform scenefade(new_widget, old_widget):
    delay 1.5
    contains:
        pause 0.5
        new_widget
        subpixel True
        truecenter
        zoom 1.03 alpha 0.0
        easein 1.0 alpha 1.0 zoom 1.0
    contains:
        old_widget
        subpixel True
        truecenter
        zoom 1.0 alpha 1.0
        easein 0.5 zoom 1.03 alpha 0.0
        pause 1.0

transform scenefadehold(new_widget, old_widget):
    delay 2.5
    contains:
        pause 1.5
        new_widget
        subpixel True
        truecenter
        zoom 1.03 alpha 0.0
        easein 1.0 alpha 1.0 zoom 1.0
    contains:
        old_widget
        subpixel True
        truecenter
        zoom 1.0 alpha 1.0
        easein 0.5 zoom 1.03 alpha 0.0
        pause 1.5

transform scenedissolve(new_widget, old_widget):
    delay 0.6
    contains:
        new_widget
        subpixel True
        truecenter
        zoom 1.03 alpha 0.0
        easein 0.5 alpha 1.0 zoom 1.0
    contains:
        old_widget
        subpixel True
        truecenter
        zoom 1.0 alpha 1.0
        easein 0.5 alpha 0.0 zoom 1.03


###########################################################################################################
#                                               TRANSITIONS                                               #
###########################################################################################################
# define config.say_attribute_transition = Dissolve(.25, alpha=True)
# define config.say_attribute_transition_layer = "master"

init -10 python:
    def eyewarp(x):
        return x**1.33
    # $ fastdiv = {"master" : wipeleft}
    
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

#####################################################################################################
#                                               AUDIO                                               #
#####################################################################################################
#BGM
define audio.titlescreen = "audio/bgm/titlescreen.mp3"
define audio.merrygoround2 = "<loop 24.162>audio/bgm/merrygoround2.mp3"
define audio.bgm1 = "audio/bgm/bgm1.mp3"

#SFX
define audio.alarm = "audio/sfx/alarm.mp3"
define audio.alarmloop = "<from 0.160 to 1.113>audio/sfx/alarm.mp3"
define audio.doorclose = "audio/sfx/doorclose.mp3"
define audio.phone_notif = "audio/sfx/phone_notif.ogg"
define audio.stomachgrowl = "audio/sfx/stomachgrowl.ogg"
define audio.thump = "audio/sfx/thump.mp3"
define audio.busopen = "audio/sfx/bus_open.ogg"

#AMBIENT
define audio.cheer = "audio/sfx/cheer.ogg"
define audio.birds = "audio/ambient/birds.ogg"
define audio.busengine = "audio/ambient/bus_engine.ogg" 

###########################################################################################################
#                                               SIDE IMAGES                                               #
###########################################################################################################

image side dhannica = LayeredImageMask("dhannica",
    Transform(crop=(310, 120, 300, 300)),
    background="gui/side_image/dhannica_bg_sideImage.png",
    mask="gui/side_image/mask_sideImage.png",
    foreground="gui/side_image/fg_sideImage.png")

image side offscr_dhannica = LayeredImageMask("dhannica",
    Transform(crop=(310, 120, 300, 300)),
    background="gui/side_image/offscr_dhannica_bg.png",
    mask="gui/side_image/offscr_mask.png",
    foreground="gui/side_image/offscr_fg.png")

image side nick = LayeredImageMask("nick",
    Transform(crop=(340, 25, 330, 300)),
    background="gui/side_image/nick_bg_sideImage.png",
    mask="gui/side_image/mask_sideImage.png",
    foreground="gui/side_image/fg_sideImage.png")

image side offscr_nick = LayeredImageMask("nick",
    Transform(crop=(340, 25, 330, 300)),
    background="gui/side_image/offscr_nick_bg.png",
    mask="gui/side_image/offscr_mask.png",
    foreground="gui/side_image/offscr_fg.png")

image side offscr_alec = LayeredImageMask("alec",
    Transform(crop=(365, 80, 300, 300)),
    background="gui/side_image/offscr_alec_bg.png",
    mask="gui/side_image/offscr_mask.png",
    foreground="gui/side_image/offscr_fg.png")

image side unknown_guy = "gui/side_image/unknown_guy_sideImage.png"

##############################################################################################################
#                                               LAYERED IMAGES                                               #
##############################################################################################################

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
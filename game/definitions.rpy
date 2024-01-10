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

    def dhannica_i_beep(event, **kwargs):
        if event == "show" or event == "show_done":
            renpy.sound.play("audio/voice/dhannica.ogg", channel="voice", loop=True, relative_volume=0.25)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="voice")
        return dhannica_beep

    def alec_beep(event, **kwargs):
        if event == "show" or event == "show_done":
            renpy.sound.play("audio/voice/alec.ogg", channel="voice", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="voice")
        return alec_beep

    def nick_beep(event, **kwargs):
        if event == "show" or event == "show_done":
            renpy.sound.play("audio/voice/nick.ogg", channel="voice", loop=True)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="voice")
        return nick_beep
    
    def nick_i_beep(event, **kwargs):
        if event == "show" or event == "show_done":
            renpy.sound.play("audio/voice/nick.ogg", channel="voice", loop=True, relative_volume=0.25)
        elif event == "slow_done" or event == "end":
            renpy.sound.stop(channel="voice")
        return nick_i_beep
    
    class DisableSkip():
        def start():
            store._game_menu_screen = None
            config.skipping = False # if skipping, stop it
            store._skipping = False #prevents from skipping
        def stop():
            store._game_menu_screen = 'emptymenu'
            store._skipping = True

    class DreamScene():
        def start(label):
            # Check if the dream scene has already been seen
            seen_label = getattr(persistent, "seen_" + label, False)

            if not _in_replay:
                if seen_label:
                    renpy.call_screen("confirm", 
                                    "It looks like you've already seen this dream.\nWould you like to skip this scene?",
                                    yes_action=Jump(label + ".end_dream"),
                                    no_action=Return())

            #declare that we are now in a dream
            store.current_scene = "dream"
            renpy.show("black_bars", layer="dream")


            if not config.developer:
                renpy.block_rollback()
                store._skipping = False

            if _in_replay:
                store.Main = persistent.playername
                store._game_menu_screen = 'emptymenu'

        def stop(label):
            # Mark the dream scene as seen
            setattr(persistent, "seen_" + label, True)
            renpy.save_persistent()

            #leave the dream
            store.current_scene = None
            renpy.hide("black_bars", layer="dream")

            if not config.developer:
                renpy.block_rollback()
                
            store._skipping = True
            
            #delete the dream history to make it more authentic like she forgor
            store._history_list = []

            if _in_replay:
                renpy.end_replay()

##########################################################################################################
#                                               CHARACTERS                                               #
##########################################################################################################
define narrator = Character(ctc="ctc", ctc_position='fixed')
define speak = Character(what_prefix='"', what_suffix='"', ctc="ctc", ctc_position="fixed", callback=narrator_beep)

#characters
define dhannica = Character('[Main]', kind=speak, color='#ff9b9b', image="dhannica", callback=dhannica_beep, namebox_background=Frame("gui/namebox/dhannica_namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define dhannica_i = Character('[Main]', ctc="ctc", ctc_position="fixed", what_prefix='{i}(', what_suffix='){/i}', color='#ff9b9b', image="dhannica", callback=dhannica_i_beep, namebox_background=Frame("gui/namebox/dhannica_namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define phone_dhannica = Character('[Main]', kind=dhannica, image="dhannica", what_font="fonts/JetBrainsMono-Regular.ttf", what_size=31, namebox_background=Frame("gui/namebox/dhannica_namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))

default n_name = ""
define nick = Character('[n_name]', kind=speak, color='#4076ff', image='nick', callback=nick_beep, namebox_background=Frame("gui/namebox/nick_namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))

default a_name = "Alec"
define alec = Character('[a_name]', kind=speak, color='#21a733', image="alec", callback=alec_beep, namebox_background=Frame("gui/namebox/alec_namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))
define phone_alec = Character('[a_name]', kind=alec, image="alec", what_font="fonts/JetBrainsMono-Regular.ttf", what_size=31, namebox_background=Frame("gui/namebox/alec_namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign))

#side characters
define girlMom = Character('Mom', kind=speak)
define d_singer = Character('Singer',kind=speak)
define prof = Character('Prof', kind=speak)
define unknown = Character('???', kind=speak)
define nurse = Character('Nurse', kind=speak)
define doctor = Character('Doctor', kind=speak)
define everyone = Character('Everyone', kind=speak)

define block = Character(None, advance=False)

######################################################################################################
#                                               IMAGES                                               #
######################################################################################################
image bg highway:
    im.Blur("images/bg/highway.jpg", 1.5)

image bg dhannica room:
    im.Blur("images/bg/dhannica_room.png", 1.5)

image bg stage:
    im.Blur("images/bg/stage.png", 1.5)

image bg living room:
    im.Blur("images/bg/livingroom.png", 1.5)

image bg school:
    im.Blur("images/bg/school.jpg", 1.5)

image bg busstop:
    im.Blur("images/bg/busstop.png", 1.5)

image bg busstop_no_bus:
    im.Blur("images/bg/busstop_no_bus.png", 1.5)

image bg bus:
    im.Blur("images/bg/bus.png", 1.5)

image bg school hallway:
    im.Blur("images/bg/schoolhallway.jpg", 1.5)

image bg classroom:
    im.Blur("images/bg/classroom.png", 1.5)

image bg classroom2:
    im.Blur("images/bg/classroom2.png", 1.5)
    
image bg clinic:
    im.Blur("images/bg/clinic.jpg", 1.5)

image bg hospital:
    im.Blur("images/bg/hospital.jpg", 1.5)

image black_bars = "gui/black_bars.png"

image mom = "images/characters/mom.png"

image camera_flash:
    Solid("#ffffff2c")
    pause 0.1
    Solid("#00000000")


transform cloud2:
    xoffset -1920
    linear 200 xoffset 0
    repeat

transform cloud1:
    xoffset -1920
    linear 50 xoffset 0
    repeat

image menu_bg = Composite(
    (1920, 1080),
    (0, 0), "gui/menu/sky1.png",
    (0, 0), At("gui/menu/clouds2.png", cloud2),
    (0, 0), At("gui/menu/clouds1.png", cloud1),
    (0, 700), "gui/menu/grasshill.png",
    (0, 0), "menu_particle",
    (-2, 825), "gui/menu/grassblur.png"
    )

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
transform blur_fade(new_widget, old_widget):
    delay 1.5
    contains:
        pause 0.5
        new_widget
        subpixel True
        truecenter
        alpha 0.0 blur 30
        easein 1.0 alpha 1.0 blur 0
    contains:
        old_widget
        subpixel True
        truecenter
        alpha 1.0 blur 0
        easein 0.5 alpha 0.0 blur 30
        pause 1.0

transform blur_fadehold(new_widget, old_widget):
    delay 2.5
    contains:
        pause 1.5
        new_widget
        subpixel True
        truecenter
        alpha 0.0 blur 30
        easein 1.0 alpha 1.0 blur 0
    contains:
        old_widget
        subpixel True
        truecenter
        alpha 1.0 blur 0
        easein 0.5 alpha 0.0 blur 30
        pause 1.5

transform blur_dissolve(new_widget, old_widget):
    delay 0.6
    contains:
        new_widget
        subpixel True
        truecenter
        alpha 0.0 blur 30
        easein 0.5 alpha 1.0 blur 0
    contains:
        old_widget
        subpixel True
        truecenter
        alpha 1.0 blur 0
        easein 0.5 alpha 0.0 blur 30


###########################################################################################################
#                                               TRANSITIONS                                               #
###########################################################################################################

init -10 python:
    def eyewarp(x):
        return x**1.33

init +1:
    $ dissolve = {"master" : dissolve}

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
define audio.meet = "<loop 04.024>audio/bgm/meet.ogg"
define audio.into_a_dream = "<loop 0>audio/bgm/into_a_dream.ogg"

#SFX
define audio.alarm = "audio/sfx/alarm.ogg"
define audio.alarmloop = "<from 0.880 to 2.855>audio/sfx/alarm.ogg"
define audio.doorclose = "audio/sfx/doorclose.mp3"
define audio.phone_notif = "audio/sfx/phone_notif.ogg"
define audio.stomachgrowl = "audio/sfx/stomachgrowl.ogg"
define audio.thump = "audio/sfx/thump.mp3"
define audio.busopen = "audio/sfx/bus_open.ogg"
define audio.knock = "audio/sfx/knock.ogg"
define audio.page = "audio/sfx/page.ogg"

#AMBIENT
define audio.cheer = "audio/sfx/cheer.ogg"
define audio.birds = "audio/ambient/birds.ogg"
define audio.busengine = "audio/ambient/bus_engine.ogg" 
define audio.classroom = "audio/ambient/classroom.ogg"
define audio.schoolhallway = "audio/ambient/hallway.ogg"
define audio.hospital = "audio/ambient/hospital.ogg"
define audio.night = "audio/ambient/night.ogg"

###########################################################################################################
#                                               SIDE IMAGES                                               #
###########################################################################################################

image side dhannica = LayeredImageMask("dhannica",
    Transform(crop=(364, 140, 300, 300), zoom=1.5),
    background="gui/side_image/dhannica_bg_sideImage.png",
    mask="gui/side_image/newMask_sideImage.png")

image side nick = LayeredImageMask("nick",
    Transform(crop=(390, 60, 300, 300), zoom=1.5),
    background="gui/side_image/nick_bg_sideImage.png",
    mask="gui/side_image/newMask_sideImage.png")

image side alec = LayeredImageMask("alec",
    Transform(crop=(415, 130, 300, 300), zoom=1.5),
    background="gui/side_image/alec_bg_sideImage.png",
    mask="gui/side_image/newMask_sideImage.png")

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

image dhannica_blink_look:
    "images/characters/dhannica/face/eyes_look.png"
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

    group body: #body
        attribute body default:
            "images/characters/dhannica/base.png"

    group eyes:
        attribute blink default:
            "dhannica_blink"
        attribute eyelook:
            "dhannica_blink_look"
        attribute eyeclose:
            "images/characters/dhannica/face/eyes_closed.png"
        attribute eyehappy:
            "images/characters/dhannica/face/eyes_closed2.png"

    group brows:
        attribute brow default:
            "images/characters/dhannica/face/brow_normal.png"
        attribute browsad:
            "images/characters/dhannica/face/brow_worried.png"
        attribute browangy:
            "images/characters/dhannica/face/brow_angy.png"

    group lips:
        attribute neutral default:
            "images/characters/dhannica/face/lips.png"
        attribute sad:
            "images/characters/dhannica/face/lips_sad.png"

    group misc:
        attribute tear:
            "images/characters/dhannica/face/tear.png"
        attribute sweat:
            "images/characters/dhannica/face/sweat.png"

    group accesories:
        attribute glasses default:
            "images/characters/dhannica/face/glasses.png"
        attribute no_glasses:
            Null()

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

image alec_blink_look:
    "images/characters/alec/face/eyes_look.png"
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

    group body: #body
        attribute body default:
            "images/characters/alec/base.png"

    group eyes:
        attribute blink default:
            "alec_blink"
        attribute eyelook:
            "alec_blink_look"
        attribute eyeclose:
            "images/characters/alec/face/eyes_closed.png"
        attribute eyehappy:
            "images/characters/alec/face/eyes_closed2.png"

    group brows:
        attribute brow default:
            "images/characters/alec/face/brow_normal.png"
        attribute browsad:
            "images/characters/alec/face/brow_worried.png"

    group lips:
        attribute neutral default:
            "images/characters/alec/face/lips.png"
        attribute smile:
            "images/characters/alec/face/lips_smile.png"

    group misc:
        attribute sweat:
            "images/characters/alec/face/sweat.png"


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

image nick_blink_look:
    "images/characters/nick/face/eyes_look.png"
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

    group body: #body
        attribute body default:
            "images/characters/nick/base.png"

    group eyes:
        attribute blink default:
            "nick_blink"
        attribute eyelook:
            "nick_blink_look"
        attribute eyeclose:
            "images/characters/nick/face/eyes_closed.png"

    group brows:
        attribute brow default:
            "images/characters/nick/face/brow_normal.png"
        attribute browsus:
            "images/characters/nick/face/brow_sideeye.png"

    group lips:
        attribute neutral default:
            "images/characters/nick/face/lips.png"
        attribute smile:
            "images/characters/nick/face/lips_smile.png"
        attribute smirk:
            "images/characters/nick/face/lips_smirk.png"

layeredimage dhannica_phone:
    zoom 1.5

    group screens:
        attribute screen_off default:
            "images/misc/phone/lock_phone.png"
        attribute lockscreen:
            "images/misc/phone/lock_screen_notime.png"
        attribute lockscreen_time:
            "images/misc/phone/lock_screen_time.png"
        attribute lockscreen_lucid_time:
            "images/misc/phone/lock_screen_lucid_time.png"
        attribute stream_app:
            "images/misc/phone/stream_appsplash.png"
        attribute vid_cat:
            "images/misc/phone/cat1.png"
        attribute vid_cat2:
            "images/misc/phone/cat2.png"

    attribute hand default:
        "images/misc/phone/hand.png"


#blue 014d81
#pantone 6463b1
#pink eb7e8a
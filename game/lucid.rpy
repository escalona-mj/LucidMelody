transform reverse_cloud2:
    xoffset 0
    linear 200 xoffset -1920
    repeat

transform reverse_cloud1:
    xoffset 0
    linear 50 xoffset -1920
    repeat

image reverse_menu_particle = SnowBlossom("gui/menu/particle.png", count=10, xspeed=(-100,-250), yspeed=(150,90), fast=True, horizontal=False)

image lucid_menu_bg = Composite(
    (1920, 1080),
    (0, 0), "gui/menu/sky1.png",
    (0, 0), At("gui/menu/clouds2.png", reverse_cloud2),
    (0, 0), At("gui/menu/clouds1.png", reverse_cloud1),
    (0, 700), "gui/menu/grasshill.png",
    (0, 0), "reverse_menu_particle",
    (-2, 825), "gui/menu/grassblur.png"
    )

label enter_lucid:
    $ _skipping = False
    $ _game_menu_screen = None
    $ renpy.suspend_rollback(True)
    scene black
    stop music fadeout 1.0
    with blur_fade
    $ renpy.pause(0.5, hard=True)
    camera at withBlur
    play music into_a_dream
    show lucid_menu_bg:
        matrixcolor SaturationMatrix(0.0)
    show expression "gui/lucid/confirm_overlay.png" as overlay:
        alpha 0.75
    show expression "gui/lucid/grout.png" as grout at pulse onlayer front:
        alpha 0.5

    if persistent.seen_lucid == False:
        label lucid_tutorial:
            $ persistent.seen_lucid = True
            $ renpy.save_persistent()
            call screen dialog_lucid("Welcome to Lucid Somnambulism", "Lucid Somnambulism is a state of dreamlike, surreal atmosphere where you have control over the character's dream.")
            call screen dialog_lucid("Alternate Route", "Dhannica's fate was to meet either Nick or Alec. In this state, she can now choose to ignore them, leading to a new branch of story.")

    #main thing
    call screen lucid

    $ renpy.pause(0.5, hard=True)

    stop music fadeout 1.0
    hide grout onlayer front
    hide lucid_menu_bg
    hide overlay
    with blur_dissolve

screen lucid_modal(message, first_btn, second_btn, first_action, second_action):
    style_prefix "dialog_lucid"
    modal True

    zorder 200

    frame at slideup(50):
        xsize 800
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        text _(message):
            xalign 0.5
            text_align 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton first_btn action first_action
            textbutton second_btn action second_action

    key "game_menu" action Hide()

################## DIALOG SCREEN ##################
screen dialog_lucid(title, message):
    zorder 200

    style_prefix "dialog_lucid"

    frame at slideup(50):
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label title:
            style "dialog_lucid_label"
            xalign 0.5
        
        text message:
            xalign 0.5
            text_align 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton "Proceed." action Return()

    key "K_RETURN" action Return()

style dialog_lucid_frame:
    align (0.5, 0.5)
    xsize 1200
    background Frame("gui/lucid/lucid_frame.png", gui.frame_borders, gui.frame_tile)
    padding(90, 90, 90, 90)

style dialog_lucid_label_text is default:
    xalign 0.5
    size (gui.interface_text_size + 15)
    text_align 0.5
    font "fonts/Lmromancaps10Oblique-BWV4G.otf"

transform dream_thumb:
    crop(720, 340, 470, 720)
    matrixcolor SaturationMatrix(0.25)

transform desaturate:
    matrixcolor SaturationMatrix(0.25)

################## DREAM SCREEN ##################
screen lucid():
    style_prefix "lucid"
    
    frame:
        style "lucid_content_frame"
        at slideup(50)
        vbox:
            xfill True
            spacing 50

            label "Choose a dream.":
                xalign 0.5

            hbox:
                spacing 50
                xalign 0.5

                button:
                    xsize 470
                    ysize 720
                    background "gui/lucid/slot_locked.png"
                    foreground "gui/lucid/slot_border.png"
                    action None

                button:
                    xsize 470
                    ysize 720
                    background AlphaMask(At("bg stage", dream_thumb), "gui/lucid/slot_mask.png")
                    foreground "gui/lucid/slot_border.png"
                    hover_background Composite(
                        (470, 720),
                        (0,0), AlphaMask(At("dream1_cg_part5", dream_thumb), "gui/lucid/slot_mask.png"),
                        (0,0), "gui/lucid/slot_hover.png"
                    )
                    action ShowTransient("lucid_modal", message="Are you sure you want to enter this dream?", first_btn="Yes", first_action=Replay("dream1"), second_btn="No", second_action=Hide())
                    at transform:
                        on idle:
                            easein .25 zoom 1.0
                        on hover:
                            zoom 1.0
                            easein .25 zoom 1.025

                button:
                    xsize 470
                    ysize 720
                    background "gui/lucid/slot_locked.png"
                    foreground "gui/lucid/slot_border.png"
                    action None
    

    # HEADER
    hbox:
        at slidein_left(50)
        pos(50, 25)
        spacing 50

        style_prefix "title_lucid"
        
        textbutton "<" action ShowTransient("lucid_modal", message="Are you sure you want to end the state of lucid somnamnbulism?", first_btn="Yes", first_action=Return(False), second_btn="No", second_action=Hide()):
            yoffset -5
        label "Lucid Somnambulism"
    hbox:
        at slidein_right(50)
        xalign 1.0
        offset(-75, 25)
        spacing 50

        style_prefix "title_lucid"
        
        textbutton "?" action Jump("lucid_tutorial")

style lucid_frame is empty
style lucid_content_frame:
    background None
    xfill True
    top_margin 150

style title_lucid_label_text:
    yalign 0.5
    font "fonts/Lmromancaps10Oblique-BWV4G.otf"
    size 85
    slow_cps 20

style title_lucid_button_text is title_lucid_label_text:
    size 75

style lucid_label_text:
    text_align 0.5
    font "fonts/Lmromancaps10Oblique-BWV4G.otf"
    slow_cps 20

style lucid_text:
    xalign 0.5
    font "fonts/damase_v.2.ttf"

style lucid_button:
    xalign 0.5

style lucid_button_text:
    xalign 0.5
    font "fonts/Lmromancaps10Oblique-BWV4G.otf"

transform slidein_left(x):
    on show:
        xoffset -x alpha 0.0 blur 15
        easein 0.5 xoffset 0 alpha 1.0 blur 0
    on hide:
        xoffset 0 alpha 1.0 blur 0
        easein 0.5 xoffset -x alpha 0.0 blur 15

transform slidein_right(x):
    on show:
        xoffset x alpha 0.0 blur 15
        easein 0.5 xoffset 0 alpha 1.0 blur 0
    on hide:
        xoffset 0 alpha 1.0 blur 0
        easein 0.5 xoffset x alpha 0.0 blur 15

transform slideup(y):
    on show:
        yoffset y alpha 0.0 blur 15
        easein 0.5 yoffset 0 alpha 1.0 blur 0
    on hide:
        yoffset 0 alpha 1.0 blur 0
        easein 0.5 yoffset y alpha 0.0 blur 15

transform slidedown(y):
    on show:
        yoffset -y alpha 0.0 blur 15
        easein 0.5 yoffset 0 alpha 1.0 blur 0
    on hide:
        yoffset 0 alpha 1.0 blur 0
        easein 0.5 yoffset -y alpha 0.0 blur 15
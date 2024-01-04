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

    if persistent.seen_lucid == False:
        label lucid_intro:
            stop music fadeout 1.0
            camera:
                parallel:
                    desaturate
                parallel:
                    noBlur
            show black_bars onlayer dream
            scene bg hospital
            play ambient hospital volume 0.5 fadein 1.0
            with blur_fade
            $ current_scene = "dream"
            "The sterile scent of antiseptic hung heavy in the air as the doctor clicked his pen, preparing to discuss the case of a patient with the mother at their the side."
            "They sat in a small consultation room within the hospital, the only sounds being the faint hum of fluorescent lights and the distant murmur of the busy ward outside."
            doctor "I understand this has been a very distressing time for you and your family. I wanted to discuss [persistent.playername]'s condition and what might have led to her current state."
            girlMom "Please, Doctor, tell me what's happening to my daughter."
            "Taking a deep breath, the doctor opened the medical file before him."
            doctor "We've conducted several tests, including neurological examinations and imaging scans."
            doctor "Physically, [persistent.playername] appears healthy, but her symptoms suggest a psychological component."
            girlMom "I fear that something in the school must've led her to become like this."
            doctor "It's not always easy to pinpoint, Ma'am."
            doctor "Based on our discussions, we suspect that the combination of emotional stress and her introverted nature led her into this frozen state as a defense mechanism."
            doctor "Introverts often internalize their struggles. In her case, the trauma of feeling alone may have overwhelmed her emotionally."
            "The mother clenched her fists with tears welling in her eyes."
            girlMom "Can she wake up? How long until she wakes up?"
            doctor "We're doing everything we can to support her physically."
            doctor "But emotionally, she needs a supportive environment. Familiar faces, comforting voices..."
            doctor "You, as her mother, are crucial to her recovery. She needs to feel connected and understood."
            "As the mother absorbed the doctor's words, a heavy silence filled in the room."
            girlMom "{i}Oh, [persistent.playername]...{/i}"
            scene black
            hide black_bars onlayer dream
            stop ambient fadeout 1.0
            with blur_fade
    
    camera at withBlur
    play music into_a_dream
    show lucid_menu_bg:
        matrixcolor SaturationMatrix(0.0)
    show expression "gui/lucid/confirm_overlay.png" as overlay:
        alpha 0.75
    # show expression "gui/lucid/grout.png" as grout at pulse onlayer front:
    #     alpha 0.5
    with blur_dissolve

    if persistent.seen_lucid == False:
        $ persistent.seen_lucid = True
        $ renpy.save_persistent()
        label lucid_tutorial:
            call screen dialog_lucid("Welcome to Lucid Somnambulism", "Lucid Somnambulism is a state of dreamlike, surreal atmosphere where you have control over [persistent.playername]'s dream.", centered_text=True)
            call screen dialog_lucid("Introduction", "After choosing none of the love interests in the game, [persistent.playername] underwent through an emotional outburst, triggering her trauma.\n\nThis state is her mind's way of coping and trying to resolve the trauma that led her to a coma. [persistent.playername] must traverse through her subconscious, revisiting key moments of her life, particularly focusing on her first day of school.\n\nThis day was pivotal as she met two significant characters, Alec and Nick. However, in the lucid somnambulistic state, [persistent.playername] needs to navigate without encountering them, exploring alternate interactions and experiences that leads to a new branch of story.")
            call screen dialog_lucid("Objective", "[persistent.playername] must traverse through these altered memories to find a path that reconciles her independence with her need for connection.\n\nThis journey is about understanding that self-assertion doesn't necessarily mean isolation and that independence can coexist with interdependence.")
            call screen dialog_lucid("Note", "You can also choose to leave the dream as is and the lucid somnambulism state will end as if nothing will happen. You can replay the dreams as much as you want.", centered_text=True)
            
    #main thing
    call screen lucid

    $ renpy.pause(0.5, hard=True)

    stop music fadeout 1.0
    hide grout onlayer front
    hide lucid_menu_bg
    hide overlay
    with blur_dissolve
    $ renpy.pause(0.5, hard=True)

screen lucid_modal(message, first_btn, second_btn, first_action, second_action):
    style_prefix "dialog_lucid"
    modal True

    zorder 200

    frame at slideup(50):
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
screen dialog_lucid(title, message, centered_text=False):
    zorder 200

    style_prefix "dialog_lucid"

    frame at slideup(50):
        xsize 1200
        has vbox:
            xalign .5
            yalign .5
            spacing 30

        label title:
            style "dialog_lucid_label"
            xalign 0.5
        
        text message:
            xalign 0.5
            if centered_text:
                text_align 0.5

        hbox:
            xalign 0.5
            spacing 100

            textbutton "Proceed." action Return()

    key "K_RETURN" action Return()

style dialog_lucid_frame:
    align (0.5, 0.5)
    background Frame("gui/lucid/lucid_frame.png", gui.frame_borders, gui.frame_tile)
    padding(90, 90, 90, 90)

style dialog_lucid_label_text is default:
    xalign 0.5
    size (gui.interface_text_size + 15)
    text_align 0.5
    font "fonts/Lmromancaps10Oblique-BWV4G.otf"

transform dream_thumb:
    crop(720, 340, 470, 720)
    desaturate
    blur 10

transform hover_dream_thumb:
    parallel:
        dream_thumb
    parallel:
        matrixcolor SaturationMatrix(0.5)

transform desaturate:
    matrixcolor SaturationMatrix(0.25)

################## DREAM SCREEN ##################
screen lucid():
    style_prefix "lucid"
    
    frame:
        style "lucid_content_frame"
        at slideup(50, 0.5)
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
                    background AlphaMask(At("dream1_cg_part5", dream_thumb), "gui/lucid/slot_mask.png")
                    hover_background AlphaMask(At("dream1_cg_part5", hover_dream_thumb), "gui/lucid/slot_mask.png")
                    action ShowTransient("dream_enter", which_dream="dream1", transition=Dissolve(0.2))
                    # action ShowTransient("lucid_modal", message="Are you sure you want to commence this dream?", first_btn="Yes", first_action=[Hide(), Replay("dream1")], second_btn="No", second_action=Hide())
                
                button:
                    xsize 470
                    ysize 720
                    background AlphaMask("gui/lucid/slot_locked.png", "gui/lucid/slot_mask.png")
                    action None

                button:
                    xsize 470
                    ysize 720
                    background AlphaMask("gui/lucid/slot_locked.png", "gui/lucid/slot_mask.png")
                    action None

    # HEADER
    hbox:
        at slidein_left(50)
        pos(50, 25)
        spacing 50

        style_prefix "title_lucid"
        
        textbutton "<" action ShowTransient("lucid_modal", message="Are you sure you want to wake up?", first_btn="Yes", first_action=Return(False), second_btn="No", second_action=Hide()):
            yoffset -5
        label "Lucid Somnambulism"
    hbox:
        at slidein_right(50)
        xalign 1.0
        offset(-75, 25)
        spacing 50

        style_prefix "title_lucid"
        
        textbutton "Replay" action ShowTransient("lucid_modal", message="Are you sure you want to rewatch the cutscene?", first_btn="Yes", first_action=Jump("lucid_intro"), second_btn="No", second_action=Hide())

        textbutton "?" action Jump("lucid_tutorial")

    key "game_menu" action ShowTransient("lucid_modal", message="Are you sure you want to wake up?", first_btn="Yes", first_action=Return(False), second_btn="No", second_action=Hide())

init python:
    dream_dict = {
        'dream1': {
            'title': "Enigmatic Concert",
            'desc': "The audience roars. A spotlight illuminated the center stage, revealing a figure. The artist, obscured in a paperbag, began to weave a sonic tapestry that transcended the ordinary.",
            'thumb': "bg stage",
            'label': "dream1"
        }
    }

screen dream_enter(which_dream):
    modal True
    frame:
        xfill True
        yfill True
        background Composite(
            (1920, 1080),
            (0, 0), At(dream_dict[which_dream]['thumb'], desaturate),
            (0, 0), "gui/lucid/vigenette.png"
        )

        textbutton "<" style_prefix "title_lucid":
            action [With(Dissolve(0.2)),Hide()]
            pos(75, 15)

        frame:
            background None
            padding(25,25,25,25)
            yalign 1.0
            vbox:
                spacing 10
                label dream_dict[which_dream]['title'] style_prefix "title_lucid"
                
                hbox:
                    xfill True
                    box_wrap_spacing 1920
                    text dream_dict[which_dream]['desc']:
                        font "fonts/damase_v.2.ttf"
                        xsize 0.5
                        slow_cps 100
                        line_spacing 10

                    textbutton "Start" style_prefix "title_lucid":
                        xalign 1.0
                        yalign 1.0
                        action Replay(dream_dict[which_dream]['label'])

    key "game_menu" action [With(Dissolve(0.2)),Hide()]


style lucid_frame is empty
style lucid_content_frame:
    background None
    top_margin 150

style title_lucid_label_text:
    yalign 0.5
    font "fonts/Lmromancaps10Oblique-BWV4G.otf"
    size (gui.interface_text_size + 27)
    slow_cps 20

style title_lucid_button_text is title_lucid_label_text:
    size (gui.interface_text_size + 20)
    hover_color "#919191"

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
    hover_color "#919191"

transform slidein_left(x, delay_pause=0.0):
    on show:
        xoffset -x alpha 0.0 blur 15
        pause delay_pause
        easein 0.5 xoffset 0 alpha 1.0 blur 0
    on hide:
        xoffset 0 alpha 1.0 blur 0
        easein 0.5 xoffset -x alpha 0.0 blur 15

transform slidein_right(x, delay_pause=0.0):
    on show:
        xoffset x alpha 0.0 blur 15
        pause delay_pause
        easein 0.5 xoffset 0 alpha 1.0 blur 0
    on hide:
        xoffset 0 alpha 1.0 blur 0
        easein 0.5 xoffset x alpha 0.0 blur 15

transform slideup(y, delay_pause=0.0):
    on show:
        yoffset y alpha 0.0 blur 15
        pause delay_pause
        easein 0.5 yoffset 0 alpha 1.0 blur 0
    on hide:
        yoffset 0 alpha 1.0 blur 0
        easein 0.5 yoffset y alpha 0.0 blur 15

transform slidedown(y, delay_pause=0.0):
    on show:
        yoffset -y alpha 0.0 blur 15
        pause delay_pause
        easein 0.5 yoffset 0 alpha 1.0 blur 0
    on hide:
        yoffset 0 alpha 1.0 blur 0
        easein 0.5 yoffset -y alpha 0.0 blur 15
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

init python:
    lucid_info_dict = {
        'dialog_1': {
            'title': "Welcome to Lucid Somnambulism",
            'info': "Lucid Somnambulism is a state of dreamlike, surreal atmosphere where you have control over [persistent.playername]'s dream.",
            "centered": True
        },
        'dialog_2': {
            'title': "Introduction",
            'info': "After choosing none of the love interests in the game, [persistent.playername] underwent through an emotional outburst, triggering her trauma of loneliness.\n\nThis state is her mind's way of coping and resolving the trauma. [persistent.playername] must traverse through her subconscious, revisiting key moments of her life.\n\nIn the lucid somnambulistic state, she needs to navigate without encountering Alec or Nick, exploring alternate interactions and experiences that leads to a new branch of story.",
            "centered": False
        },
        'dialog_3': {
            'title': "Objective",
            'info': "You must traverse through these altered memories to find a path that reconciles her independence with her need for connection. This journey is about understanding that loneliness doesn't mean isolation and that independence can coexist with interdependence.\n\nSometimes we are happy to be by ourselves, and sometimes we wish for the company of others.",
            "centered": False
        },
        'dialog_4': {
            'title': "Note",
            'info': "There are times where you are made to choose a choice. You can also choose to leave the dream as is, and the lucid somnambulism state will end as if nothing happened. You can replay the dreams as many times as you want.\n\n\n{i}{size=-10}(You will notice that you are in the state of lucid somnambulism when the game becomes desaturated.){/i}",
            "centered": True
        },
    }

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
                desaturate
            show black_bars onlayer dream
            scene bg hospital
            play ambient hospital volume 0.5 fadein 1.0
            with blur_fade
            $ current_scene = "dream"
            "The sterile scent of antiseptic hung heavy in the air as the doctor clicked his pen."
            "On the other side of the room, a caretaker beside the patient precautiously examines the doctor's actions."
            "They sat in a small consultation room within the hospital, the only sounds being the faint hum of fluorescent lights and the distant murmur of the busy ward outside."
            doctor "I understand this has been a very distressing time for you."
            doctor "I wanted to discuss [persistent.playername]'s condition and what might have led to her current state."
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
            hide grout onlayer front
            stop ambient fadeout 1.0
            with blur_fade
    
    play music into_a_dream
    show lucid_menu_bg:
        parallel:
            blur 5
        parallel:
            bw
    show expression "gui/lucid/confirm_overlay.png" as overlay:
        alpha 0.75
    show expression "gui/lucid/grout.png" as grout at pulse onlayer front:
        alpha 0.5
    with blur_dissolve

    if persistent.seen_lucid == False:
        $ persistent.seen_lucid = True
        $ renpy.save_persistent()
        label lucid_tutorial:
            python:
                for key, value in lucid_info_dict.items():
                    renpy.call_screen("dialog_lucid", title=value['title'], message=value['info'], centered_text=value['centered'])
            
    #main thing
    call screen lucid

    $ renpy.pause(0.5, hard=True)

    stop music fadeout 1.0
    hide grout onlayer front
    hide lucid_menu_bg
    hide overlay
    with blur_dissolve
    $ renpy.pause(0.5, hard=True)


################## CONFIRM SCREEN ##################
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

transform move_around:
    parallel:
        choice:
            ease_quad 1.0 xoffset 5 yoffset 10
        choice:
            ease_quad 2.5 xoffset -5 yoffset 10
        choice:
            ease_quad 3.0 xoffset 5 yoffset -10
        choice:
            ease_quad 2.0 xoffset -5 yoffset -10
        repeat
    

transform hover_dream_thumb:
    parallel:
        dream_thumb
    parallel:
        matrixcolor SaturationMatrix(0.5)

transform desaturate:
    matrixcolor SaturationMatrix(0.25)

transform bw:
    matrixcolor SaturationMatrix(0.0)

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
                    background AlphaMask(At("bg stage", dream_thumb), "gui/lucid/slot_mask.png")
                    hover_background AlphaMask(At("bg stage", hover_dream_thumb), "gui/lucid/slot_mask.png")
                    action [ShowTransient("dream_enter", which_dream="dream1", transition=Dissolve(0.2))]
                    at move_around
                    
                button:
                    xsize 470
                    ysize 720
                    background AlphaMask(At("bg classroom2", dark_tint, dream_thumb), "gui/lucid/slot_mask.png")
                    hover_background AlphaMask(At("bg classroom2", dark_tint, hover_dream_thumb), "gui/lucid/slot_mask.png")
                    action [ShowTransient("dream_enter", which_dream="dream2", transition=Dissolve(0.2))]
                    at move_around

                button:
                    xsize 470
                    ysize 720
                    background AlphaMask("gui/lucid/slot_locked.png", "gui/lucid/slot_mask.png")
                    action None
                    at move_around

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
            'desc': "The audience roars. A spotlight illuminated the center stage, revealing a figure, obscured in a paperbag. It began to weave a sonic tapestry that uplifted the audience.",
            'thumb': "bg stage",
            'label': "dream1"
        },
        'dream2': {
            'title': "Torn Notes",
            'desc': "Things are get interesting. Piecing the torn pages back together, whatever it was, unfolds a hidden story behind Nick that changes everything.",
            'thumb': "puzzle_thumb",
            'label': "puzzle_test"
        }
    }

transform blur_nick:
    xalign 0.5 zoom 2.0 matrixcolor BrightnessMatrix(-1) blur 30

image puzzle_thumb = Composite(
    (1920, 1080),
    (0, 0), At("bg classroom2", dark_tint),
    (450, 145), At("nick", blur_nick, move_around, dark_tint)
    )

screen dream_enter(which_dream):
    modal True
    frame:
        align(0.5, 0.5)
        xfill True
        yfill True
        background Composite(
            (1920, 1080),
            (0, 0), At(dream_dict[which_dream]['thumb'], desaturate),
            (0, 0), "gui/lucid/vigenette.png"
        )

        textbutton "<" style_prefix "title_lucid":
            action [Hide(transition=Dissolve(0.2))]
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
                        outlines [ (1, "#000", 1, 1) ]

                    textbutton "Start" style_prefix "title_lucid":
                        xalign 1.0
                        yalign 1.0
                        action Call(dream_dict[which_dream]['label'])

    key "game_menu" action [Hide(transition=Dissolve(0.2))]


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
screen dialog(message, ok_action):
    on "show" action Function(renpy.show_layer_at, dialogue_withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, dialogue_noBlur, layer="master")
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png":
        at transform:
            on show:
                alpha 0.0
                easein .25 alpha 0.5
            on hide:
                alpha 0.5
                easein .25 alpha 0.0

    key "K_RETURN" action [ok_action]

    frame at screen_appear:
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        label _(message):
            style "confirm_prompt"
            xalign 0.5
        hbox:
            xalign 0.5
            spacing 100

            imagebutton:
                auto "gui/navigation/confirm_btn_%s.png"
                foreground Text(_("OK"), style="confirm_btn")
                hover_foreground Text(_("OK"), style="confirm_btn_hover")
                selected_foreground Text(_("OK"), style="confirm_btn_selected")
                action ok_action

############################
# CUSTOM NAME INPUT SCREEN #
############################

default Main = ''

#custom name input
screen name_input(ok_action, back_action):
    dismiss action back_action
    on "show" action Function(renpy.show_layer_at, dialogue_withBlur, layer="screens")
    on "hide" action Function(renpy.show_layer_at, dialogue_noBlur, layer="screens")
    zorder 200
    style_prefix "confirm"
    key "K_RETURN" action [ok_action]

    frame:
        modal True
        at screen_appear
        has vbox:
            xalign 0.5
            yalign 0.5
            spacing 30

        vbox:
            # spacing 10
            text "What is your name?"
            text "(Press Enter without typing your name to use default name.)" size 30

        input default "" value VariableInputValue("Main") length 12 allow "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
            color u'#000'
            xalign 0.5
            yalign 0.5
            size 69

style confirm_text:
    xalign 0.5
    yalign 0.5
    color u'#000'
    text_align 0.5
    font gui.interface_text_font

style confirm_input:
    font "fonts/MyPrettyCutie.ttf"

init python:
    def SavePlayerName():
        persistent.playername = Main

####################
# CHOOSE MC SCREEN #
####################

transform pulse:
    alpha 0
    choice:
        ease 2.0 alpha 0.5
    choice:
        ease 4.0 alpha 0.5
    choice:
        ease 1.0 alpha 0.8
    choice:
        ease 10 alpha 1.0
    ease 7 alpha 0
    repeat

transform blink:
    choice:
        ease 1.0 alpha 1.0
    choice:
        ease 0.2 alpha 1.0
    choice:
        ease 0.5 alpha 1.0
    choice:
        ease 0.7 alpha 1.0
    ease 1.0 alpha 0.0
    repeat

image firefly:
    "gui/firefly.png"
    choice:
        ease 1.0
        "gui/fireflyellow.png"
    choice:
        ease 0.2
        "gui/fireflyellow.png"
    choice:
        ease 0.5
        "gui/fireflyellow.png"
    choice:
        ease 0.7
        "gui/fireflyellow.png"
    ease 1.0
    repeat

image fireflies = SnowBlossom(At("firefly", blink), count=20, xspeed=(0,-10), yspeed=(-150,-90), fast=False, horizontal=False)

image girlMC:
    im.MatrixColor("images/characters/dhannica/base.png", im.matrix.brightness(1))

image boyMC:
    im.MatrixColor("images/characters/nick/base.png", im.matrix.brightness(1))

screen chooseMC():
    add "black"
    add "gui/chooseMC.png" at pulse
    add "fireflies"
    if persistent.first_gameplay == False:
        text "Please choose your gender.":
            color u"#fff"
            xalign 0.5
            yalign 0.25
            at transform:
                alpha 1.0
                5.0
                ease 1.0 alpha 0.0
    fixed:
        at transform:
            zoom 1.0 xalign 0.5 yalign 1.0
            on hide:
                easein .25 zoom 0.95 alpha 0.0
        spacing 10
        imagebutton:
            xalign 0.0
            yalign 1.0
            idle "girlMC"
            action (Show(screen='name_input',_layer="front", ok_action=(Hide(screen='name_input',_layer="front"),Call("chooseFemale")), back_action=Hide(screen='name_input',_layer="front")))
            tooltip "I'm a girl."
            focus_mask True
            activate_sound "audio/sfx/click.mp3"
            at showButtons(-0.5, 0.0)
        imagebutton:
            xalign 1.0
            yalign 1.0
            idle "boyMC"
            action (Show(screen='name_input',_layer="front", ok_action=(Hide(screen='name_input',_layer="front"),Call("chooseMale")), back_action=Hide(screen='name_input',_layer="front")))
            tooltip "I'm a boy."
            focus_mask True
            activate_sound "audio/sfx/click.mp3"
            at showButtons(1.5, 1.0)

    $ tooltip = GetTooltip(screen="chooseMC")

    if tooltip:
        frame:
            background None
            xalign 0.5
            yalign 0.35
            text tooltip:
                color u'#fff'
                size 50

transform showButtons(x1, x2):
    xalign x1 zoom 1.0
    easein_back 1.0 xalign x2
    on hover:
        easein .25 zoom 1.05
    on idle:
        easein .25 zoom 1.0

#setting the correct variables before starting the route

label chooseFemale:
    pause 0.1
    $ current_route = 'dhannica'
    $ mcNameboy = 'Nick'
    if not Main:
        $ Main = "Dhannica"
    $ mcNamegirl = Main
    return

label chooseMale:
    pause 0.1
    $ current_route = 'nick'
    $ mcNamegirl = 'Dhannica'
    if not Main:
        $ Main = "Nick"
    $ mcNameboy = Main
    return

screen emptymenu:
    tag menu
    style_prefix "emptymenu"

    use game_menu(""):
        vbox:
            text "Chapter [chapter]":
                size 90
            text "{0}".format(chapter_list[current_chapter]):
                size 70

style emptymenu_vbox is vbox:
    xalign 0.5
    yalign 0.5

style emptymenu_text:
    xalign 0.5
    color '#fff'

screen controls_modal():
    $ persistent.seen_controls = True
    if main_menu:
        dismiss action Hide()
    else:
        dismiss action Return()

    style_prefix "controls"

    add "gui/overlay/confirm.png":
        at transform:
            on show:
                alpha 0.0
                easein .25 alpha 0.5
            on hide:
                alpha 0.5
                easein .25 alpha 0.0

    frame at screen_appear:
        modal True
        vbox:
            spacing 25
            if main_menu:
                text "Help" style_prefix "controls_title"
            else:
                text "In case if you missed it,\nhere's the controls!" style_prefix "controls_title"
                null height 25

            hbox:
                hbox:
                    style_prefix "gesture"
                    label "Tap Right Screen"
                    add "gui/tap.png":
                        yalign 0.5
                text "Advances dialogue."

            hbox:
                hbox:
                    style_prefix "gesture"
                    label "Swipe Right/Tap Left Screen"
                    hbox:
                        yalign 0.5
                        spacing 10
                        add "gui/swipe_right.png":
                            yalign 0.5
                        text "or"
                        add "gui/tap.png":
                            yalign 0.5
                text "Rolls back to earlier dialogue.":
                    yalign 0.5
    
            hbox:
                hbox:
                    style_prefix "gesture"
                    label "Swipe Down"
                    add "gui/swipe_down.png":
                        yalign 0.5
                text "Accesses the game menu\nwhile in-game."


            if not main_menu:
                null height 25
                text "If you're still overwhelmed with the controls, you can\nview them again on the main menu.":
                    size 30
            # null height 25

            # hbox:
            #     xalign 0.5
            #     text "{i}Tip: Touching the small ":
            #         size 30
            #     add "gui/purple_ctc.png":
            #         yalign 0.5
            #     text "{i} will toggle the quick menu.":
            #         size 30



style controls_frame:
    background Frame("gui/frame.png", Borders(50,50,50,50), tile=False)
    padding gui.confirm_frame_borders.padding
    xalign 0.5
    yalign 0.5

style controls_vbox:
    spacing 25

style controls_hbox:
    spacing 25

style controls_title_text:
    is game_menu_label_text
    xalign 0.5
    text_align 0.5

style gesture_hbox is empty
style gesture_label:
    is help_label

style gesture_label_text:
    is help_label_text
    color gui.accent_color
    font "fonts/MyPrettyCutie.ttf"

style controls_text:
    text_align 0.5
    xalign 0.5
    font gui.interface_text_font


default persistent.seen_controls = False

label after_load:
    if not persistent.seen_controls:
        play sound "audio/sfx/phone_notif.ogg"
        call screen controls_modal
        $ persistent.seen_controls = True
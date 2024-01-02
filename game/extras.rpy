screen extras_game_menu(title, withMargin=True):
    tag menu

    style_prefix "extras_game_menu"

    if main_menu:
        use bg

    add "gui/overlay/confirm.png":
        alpha 0.65
    add "gui/menu/logo_white.png":
            xalign 0.5
            yalign 0.5
            zoom 0.75
            alpha 0.05

    add "gui/overlay/game_menu.png"
    
    frame:
        if withMargin == True:
            bottom_margin 0.01
        else:
            pass
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            vbox:
                transclude

    if main_menu:
        if not renpy.get_screen("extras"):
            key "game_menu" action ShowMenu("extras")
        else:
            key "game_menu" action ShowMenu("main_menu")

    imagebutton:
        auto "gui/navigation/return_%s.png"
        activate_sound "audio/sfx/click.ogg"
        hover_sound "audio/sfx/hover.ogg"
        focus_mask True
        xalign 0.0
        yalign 0.0
        if not renpy.get_screen("extras"):
            action ShowMenu("extras")
        else:
            action Return()

    label title style "game_menu_label"

style extras_game_menu_frame is empty
style extras_game_menu_frame:
    xsize 1200
    xalign 0.5
    yalign 0.5
    top_margin 0.15

style extras_game_menu_side:
    spacing 0

style extras_game_menu_viewport:
    xfill True

style extras_game_menu_vscrollbar is vscrollbar:
    unscrollable gui.unscrollable

transform slight_transparent:
    alpha 0.25

screen extras():
    tag menu

    use extras_game_menu("Extras"):
        style_prefix "extras"

        vbox:
            xalign 0.5

            button:
                action ShowMenu("achievements")
                foreground "gui/extras/extras_achieve_[prefix_]foreground.png"

                frame:
                    style_prefix "extras_btn_content"
                    yalign 0.5
                    vbox:
                        spacing 5
                        label "Achievements"
                        text "View your achievements here."

            button:
                action ShowMenu("gallery")
                foreground "gui/extras/extras_gallery_[prefix_]foreground.png"

                frame:
                    style_prefix "extras_btn_content"
                    yalign 0.5
                    vbox:
                        spacing 5
                        label "Gallery"
                        text "See those memorable moments again."
            
            if mainMenu_ach.has():
                button:
                    action Start("enter_lucid")
                    #action If(persistent.seen_dream1, true=Show("confirm", message="Are you sure you want to replay Dream 1?", yes_action=[Replay("dream1"), Hide()], no_action=Hide()), false=Show("dialog", message="You have not seen this part yet.", ok_btn="OK", ok_action=Hide()))
                    foreground "lucid_button"

                    frame:
                        style_prefix "extras_btn_content"
                        yalign 0.5
                        vbox:
                            style_prefix "extras_lucid"
                            label "{gtext}{font=fonts/Lmromancaps10Oblique-BWV4G.otf}{size=70}Lucid Somnambulism{/font}{/gtext}"
            else:
                button:
                    action None
                    foreground "gui/extras/extras_locked_foreground.png"

                    frame:
                        style_prefix "extras_btn_content"
                        yalign 0.5
                        vbox:
                            spacing 5
                            style_prefix "extras_locked"
                            label "???"
                            text "???"

image lucid_button:
    glitch("gui/extras/extras_lucid_foreground.png", chroma=False, offset=10, minbandheight=50, randomkey=None)
    pause 0.05
    glitch("gui/extras/extras_lucid_hover_foreground.png", chroma=False, offset=10, minbandheight=50, randomkey=None)
    pause 0.05
    repeat

style extras_button:
    background None
    xsize 1200
    ysize 300
    
    padding(325, 50, 0, 50)

    
style extras_btn_content_frame is empty

style extras_btn_content_label_text:
    font gui.game_menu_label_font
    size (gui.name_text_size + 15)
    outlines [(7, "#16161d", 0, 2)]
    hover_outlines [(7, "#6667ab", 0, 2)]

style extras_btn_content_text is gui_text:
    hover_color "#abace0"

style extras_locked_label_text is extras_btn_content_label_text:
    color u'#b5b5b5'
    outlines [(0, "#00000000", 0, 0)]
    
style extras_locked_text is extras_btn_content_text:
    color u'#b5b5b5'

style extras_lucid_label_text:
    font "fonts/Lmromancaps10Oblique-BWV4G.otf"
    size (gui.name_text_size + 25)

style extras_lucid_text is gui_text:
    font "fonts/Labrada-Regular.ttf"
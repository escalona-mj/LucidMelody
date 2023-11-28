################################################################################
## Initialization
################################################################################

init offset = -1


################################################################################
## Styles
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    # properties gui.text_properties("hyperlink", accent=True)
    properties gui.text_properties("hyperlink", accent=False)
    font gui.interface_text_font
    # hover_underline True
    underline True
    activate_sound "audio/sfx/click.mp3"

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")
    activate_sound "audio/sfx/click.mp3"

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5
    activate_sound "audio/sfx/click.mp3"


style label_text is gui_text:
    # properties gui.text_properties("label", accent=True)
    properties gui.text_properties("label")

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################


## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say
screen say(who, what):
    style_prefix "say"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

    use quick_menu
    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    # if not renpy.variant("small"):
    add SideImage() xalign 0.0 yalign 1.0 xoffset 140 yoffset -7:
        zoom 0.75

## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    # background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    # padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    # xalign gui.name_xalign
    xalign 0.5
    yalign 0.5
    color u"#fff"
    # outlines [(5, "#16161d", 2, 2)]

style say_dialogue:
    properties gui.text_properties("dialogue")
    # outlines [(5, "#16161d", 2, 2)]
    # line_spacing -5
    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

image ctc:
    xalign 0.875 yalign 0.975 subpixel True alpha 0.0 zoom 1.03
    "gui/ctc.png"
    block:
        ease 0.5 alpha 1.0 yoffset 2
        ease 0.5 alpha 0.5 yoffset -5
        repeat

# screen ctc(arg=None):
#     imagebutton:
#         xalign 0.975
#         yalign 0.975
#         at transform:
#             subpixel True alpha 0.0 zoom 1.5
#             block:
#                 ease 0.5 alpha 1.0 yoffset 2
#                 ease 0.5 alpha 0.5 yoffset -5
#                 repeat
#         idle "ctc"
#         activate_sound "audio/sfx/click.mp3"
#         action ToggleVariable("persistent.quick_menu_frame", True, False)
#         tooltip "Menu"


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width



## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

transform screen_appear:
    subpixel True
    xalign 0.5
    # yalign 0.5
    on show:
        zoom 0.95 alpha 0.0
        easein .25 zoom 1.0 alpha 1.0
    on hide:
        easein .25 zoom 0.95 alpha 0.0

screen choice(items):
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")

    add "gui/overlay/menu_overlay.png":
        at transform:
            alpha 0.0
            on show:
                easein .25 alpha 0.5
            on hide:
                easein .25 alpha 0.0

    style_prefix "choice"

    hbox:
        at screen_appear
        for i in items:
            textbutton i.caption action i.action:
                at transform:
                    on idle:
                        easein .25 zoom 1.0
                    on hover:
                        easein .25 zoom 1.25

style choice_hbox is hbox
style choice_button is button
style choice_button_text:
    is button_text
    yalign 0.5

style choice_hbox:
    xanchor 0.5
    xalign 0.5
    # ypos 405
    yalign 0.5
    # yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")
    activate_sound "audio/sfx/click.mp3"
    yalign 0.5

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")
    # outlines [(10, "#16161d", 2, 2)]

#     style_prefix "choice"

#     vbox:
#         for i in items:
#             textbutton i.caption action i.action

# style choice_vbox is vbox
# style choice_button is button
# style choice_button_text:
#     is button_text
#     yalign 0.5

# style choice_vbox:
#     xalign 0.5
#     ypos 405
#     yanchor 0.5

#     spacing gui.choice_spacing

# style choice_button is default:
#     properties gui.button_properties("choice_button")
#     activate_sound "audio/sfx/click.mp3"

# style choice_button_text is default:
#     properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("History") action ShowMenu('history')
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Save") action ShowMenu('save')
            textbutton _("Q.Save") action QuickSave()
            textbutton _("Q.Load") action QuickLoad()
            textbutton _("Prefs") action ShowMenu('preferences')

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main and Game Menu Screens
################################################################################

## Navigation screen ###########################################################
##
## This screen is included in the main and game menus, and provides navigation
## to other menus, and to start the game.

transform nav_item:
    subpixel True
    on show:
        alpha 0.0
        yoffset 100
        time 1.5
        easein .75 alpha 1.0 yoffset 0

screen navigation():

    if renpy.get_screen("main_menu"):
        vbox:
            xalign 1.0
            xoffset -50
            yoffset 50
            imagebutton:
                auto "gui/navigation/controls_%s.png"
                activate_sound "audio/sfx/click.mp3"
                focus_mask True
                action Show("controls_modal")
            if not persistent.seen_controls:
                add "gui/notif_dot.png" xoffset 65 yoffset -100
                
        hbox at nav_item:
            style_prefix "navigation"

            xalign 0.5
            yalign 0.95
            spacing 30

            textbutton "START" action Start()
            textbutton "SAVES" action ShowMenu('file_slots')
            textbutton "SETTINGS" action ShowMenu("preferences")
            textbutton "EXTRAS" action ShowMenu("achievements")
            textbutton "ABOUT" action ShowMenu("about")
            textbutton "EXIT" action Quit(confirm=True)

    else:
        hbox:
            style_prefix "navigation"
            xalign 0.5
            yalign 0.985
            spacing 0

            if not main_menu:
                imagebutton:
                    auto "gui/navigation/history_%s.png"
                    foreground Text(_("History"), style="navigation_btn")
                    hover_foreground Text(_("History"), style="navigation_btn_hover")
                    selected_foreground Text(_("History"), style="navigation_btn_selected")
                    action ShowMenu("history")
                    
            imagebutton:
                auto "gui/navigation/save_%s.png"
                foreground Text(_("Saves"), style="navigation_btn")
                hover_foreground Text(_("Saves"), style="navigation_btn_hover")
                selected_foreground Text(_("Saves"), style="navigation_btn_selected")
                action ShowMenu('file_slots')

            imagebutton:
                auto "gui/navigation/preferences_%s.png"
                foreground Text(_("Settings"), style="navigation_btn")
                hover_foreground Text(_("Settings"), style="navigation_btn_hover")
                selected_foreground Text(_("Settings"), style="navigation_btn_selected")
                action ShowMenu("preferences")

            if main_menu:
                imagebutton:
                    auto "gui/navigation/extras_%s.png"
                    foreground Text(_("Extras"), style="navigation_btn")
                    hover_foreground Text(_("Extras"), style="navigation_btn_hover")
                    selected_foreground Text(_("Extras"), style="navigation_btn_selected")
                    action ShowMenu("achievements")

                imagebutton:
                    auto "gui/navigation/about_%s.png"
                    foreground Text(_("About"), style="navigation_btn")
                    hover_foreground Text(_("About"), style="navigation_btn_hover")
                    selected_foreground Text(_("About"), style="navigation_btn_selected")
                    action ShowMenu("about")

            if not main_menu:
                imagebutton:
                    auto "gui/navigation/mainmenu_%s.png"
                    foreground Text(_("Title"), style="navigation_btn")
                    hover_foreground Text(_("Title"), style="navigation_btn_hover")
                    selected_foreground Text(_("Title"), style="navigation_btn_selected")
                    action MainMenu()

            imagebutton:
                auto "gui/navigation/quit_%s.png"
                foreground Text(_("Quit"), style="navigation_btn")
                hover_foreground Text(_("Quit"), style="navigation_btn_hover")
                selected_foreground Text(_("Quit"), style="navigation_btn_selected")
                action Quit(confirm=True)

            if _in_replay:
                imagebutton:
                    auto "gui/navigation/gallery_%s.png"
                    foreground Text(_("End Replay"), style="navigation_btn")
                    hover_foreground Text(_("End Replay"), style="navigation_btn_hover")
                    action EndReplay(confirm=True)

    #if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

        ## Help isn't necessary or relevant to mobile devices.
        #textbutton _("Help") action ShowMenu("help")

style navigation_image_button:
    activate_sound "audio/sfx/click.mp3"

style navigation_button is gui_button
style navigation_button_text:
    is gui_button_text
    xalign 0.5
    font gui.name_text_font
    text_align 0.5
    outlines [(5, "#16161d", 2, 2)]


style navigation_btn_hover:
    color u"#fff"
    yalign 0.5
    xpos 95
    font gui.interface_text_font
    size 40

style navigation_btn_selected:
    color u"#fff"
    yalign 0.5
    xpos 95
    font gui.interface_text_font
    size 40

style navigation_btn:
    yalign 0.5
    color u"#fff"
    xpos 95
    font gui.interface_text_font
    size 40

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")


## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

transform dandelion_spin:
    xpos 0.5
    ypos 0.5
    linear 5 rotate 360
    rotate 0
    repeat

image dandelions = SnowBlossom(At("gui/menu/dandelion.png", dandelion_spin), count=10, xspeed=(100,250), yspeed=(-150,-90), fast=True, horizontal=False)

init python:
    def dynamicMCMenu():
        last_save = renpy.slot_json(renpy.newest_slot())

        if last_save is None or 'common' in last_save:
            return "gui/menu/menu_NONE.png"
        elif last_save['route'] == 'dhannica':
            return "gui/menu/menu_dhannica.png"
        elif last_save['route'] == 'alec':
            return "gui/menu/menu_alec.png"
        elif last_save['route'] == 'nick':
            return "gui/menu/menu_nick.png"


screen bg():
    add "gui/menu/sky1.png"
    add "gui/menu/clouds2.png":
        at Pan((1920, 0), (0, 0), 200, repeat=True)
        at transform:
            on show:
                alpha 0.0
                xoffset 0
                time 0.5
                easein .75 alpha 1.0 xoffset 50
    add "gui/menu/clouds1.png":
        at Pan((1920, 0), (0, 0), 50, repeat=True)
        at transform:
            on show:
                alpha 0.0
                xoffset 0
                time 0.5
                easein .75 alpha 1.0 xoffset 50

    default last_character = dynamicMCMenu()
    add last_character:
        xalign 0.875
        yalign 0.65
        at transform:
            on show:
                alpha 0.0
                xoffset 50
                time 1.5
                easein .75 alpha 1.0 xoffset 0

    add "gui/menu/grasshill.png":
        pos (0, 700)
        zoom 1.1
        at transform:
            on show:
                alpha 0.0
                yoffset 100
                time 1.0
                easein .75 alpha 1.0 yoffset 0


    add "dandelions":
        at transform:
                on show:
                    alpha 0.0
                    yoffset 100
                    time 1.0
                    easein .75 alpha 1.0 yoffset 0

    # add "gui/menu/grassblur.png":
    #     pos (0, 750)
    #     zoom 1.5
    #     at transform:
    #         on show:
    #             alpha 0.0
    #             yoffset 100
    #             time 1.0
    #             easein .75 alpha 1.0 yoffset 0

    if renpy.get_screen("main_menu"):
        add "gui/menu/logo.png":
            xalign 0.5
            yalign 0.5
            zoom 0.75
            at transform:
                subpixel True
                on show:
                    zoom 1.03 alpha 0.0
                    time 2.0
                    ease 0.7 alpha 1.0 zoom 1.0

screen fake_mainMenu():
    tag menu

    use bg

    fixed:
        textbutton "":
            xfill True
            yfill True
            activate_sound None
            action [Show(screen="main_menu",transition=dissolve), Hide(screen="fake_mainMenu")]

screen main_menu():

    tag menu

    use bg
    use navigation

    add "gui/menu/grassblur.png":
        pos (0, 750)
        zoom 1.5
        at transform:
            on show:
                alpha 0.0
                yoffset 100
                time 1.0
                easein .75 alpha 1.0 yoffset 0

    if gui.show_name:

        vbox:
            style "main_menu_vbox"

            text "[config.name!t]":
                style "main_menu_title"

            text "[config.version]":
                style "main_menu_version"

    timer 300 action [Show(screen="fake_mainMenu", transition=dissolve), Function(mainMenu_ach.grant)]

style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    # background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -30
    xmaximum 1200
    yalign 1.0
    yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Game Menu screen ############################################################
##
## This lays out the basic common structure of a game menu screen. It's called
## with the screen title, and displays the background, title, and navigation.
##
## The scroll parameter can be None, or one of "viewport" or "vpgrid".
## This screen is intended to be used with one or more children, which are
## transcluded (placed) inside it.

image overlay_dhannica:
    "gui/overlay/game_menu_dhannica_1.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "gui/overlay/game_menu_dhannica_2.png"
    .10
    repeat

image overlay_alec:
    "gui/overlay/game_menu_alec_1.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "gui/overlay/game_menu_alec_2.png"
    .10
    repeat

image overlay_nick:
    "gui/overlay/game_menu_nick_1.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "gui/overlay/game_menu_nick_2.png"
    .10
    repeat

screen game_menu(title, scroll=None, yinitial=0.0):
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")

    style_prefix "game_menu"

    if main_menu:
        use bg

    add "gui/overlay/confirm.png":
        alpha 0.65
    add "gui/menu/logo_white.png":
            xalign 0.5
            yalign 0.5
            zoom 0.75
            alpha 0.05
    if current_route == "alec":
        add "overlay_alec"
    elif current_route == "nick":
        add "overlay_nick"
    elif current_route == "dhannica":
        add "overlay_dhannica"
    elif current_route == "common":
        add "gui/overlay/game_menu.png"

    frame:
        style "game_menu_outer_frame"
        # background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)
        xalign 0.5
        yalign 0.5

        vbox:
            ## Reserve space for the navigation section.
            # frame:
            #     style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"
               
                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        transclude

                else:

                    transclude
    
    use navigation

    imagebutton:
        auto "gui/navigation/return_%s.png"
        activate_sound "audio/sfx/click.mp3"
        focus_mask True
        xalign 0.0
        yalign 0.0
        action Return()

    label title

    if main_menu:
        key "game_menu" action ShowMenu("main_menu")

    $ tooltip = GetTooltip()

    if tooltip:
        frame:
            background None
            xalign 1.0
            yalign 0.15
            text tooltip:
                size 35
                textalign 1.0
                color u'#fff'
                font gui.interface_text_font


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text


style return_button is navigation_button
style return_button_text is navigation_button_text

# style game_menu_outer_frame:
    # background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 420
    yfill True

style game_menu_content_frame:
    xalign 0.5
    yalign 0.5
    top_padding 0.15
    bottom_padding 0.15


style game_menu_viewport:
    # xsize 1380
    xsize 1200

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 15

style game_menu_label:
    xpos 340
    yalign 0.03

style game_menu_label_text:
    font gui.game_menu_label_font
    size gui.title_text_size
    outlines [(10, "#6667ab", 2, 2)]
    # color gui.accent_color
    yalign 0.5

style return_button:
    xpos gui.navigation_xpos
    yalign 1.0
    yoffset -45


## About screen ################################################################
##
## This screen gives credit and copyright information about the game and Ren'Py.
##
## There's nothing special about this screen, and hence it also serves as an
## example of how to make a custom screen.

screen about():

    tag menu

    ## This use statement includes the game_menu screen inside this one. The
    ## vbox child is then included inside the viewport inside the game_menu
    ## screen.
    use game_menu(_("About"), scroll="viewport"):

        style_prefix "about"

        null height 25

        frame style "empty_frame":
            xfill True
            has vbox:
                spacing 10
                xfill True
            add "gui/menu/logo_white.png":
                zoom 0.35
                xalign 0.5
            text "Beta [config.version!t]":
                xalign 0.5
                size 30
            text "Game entry for the subject Game Development.":
                xalign 0.5
                size 30
        
        null height 100

        vbox:
            xfill True

            ###STORY
            frame style "empty_frame":
                style_prefix "about_title"
                label "STORY"
                
            frame style "empty_frame":
                has vbox:
                    style_prefix "about_role"
                label "Writer"

                frame style "empty_frame":
                    style_prefix "about_person"
                    has vbox
                    text "Ace Brian Laraño"
                    text "Kaia Buenafe"

            null height 100

            ###DEVS
            frame style "empty_frame":
                style_prefix "about_title"
                label "DEVELOPMENT"
                
            frame style "empty_frame":
                has vbox:
                    style_prefix "about_role"
                label "Programming"

                frame style "empty_frame":
                    style_prefix "about_person"
                    has vbox
                    text "Mark John Escalona"
            
            null height 100

            ###ART
            frame style "empty_frame":
                style_prefix "about_title"
                label "ART"
            
            hbox:
                xalign 0.5
                spacing 100

                frame style "empty_frame":
                    has vbox:
                        style_prefix "about_role"
                    label "BG Artist"

                    frame style "empty_frame":
                        style_prefix "about_person"
                        has vbox
                        text "Cindy Angeles"
                
                frame style "empty_frame":
                    has vbox:
                        style_prefix "about_role"
                    label "Artist"

                    frame style "empty_frame":
                        style_prefix "about_person"
                        has vbox
                        text "Zenrich Jordan Keh"
                        text "Kaia Buenafe"
                        text "Mark John Escalona"

            null height 100

            ###AUDIO
            frame style "empty_frame":
                style_prefix "about_title"
                label "MUSIC"
            
            frame style "empty_frame":
                style_prefix "about_person"
                has vbox
                text "Mekaella Joy Muit"
                text "Neil Moises Maneja"
                text "Ivan Barzaga"
                text "Rechelle Añover"
                text "Kristian Magallanes"
                text "John Christian Mantele"
                    
        null height 100
               
            # label "[config.name!t]"
            # text _("Version [config.version!t]\n")

            # ## gui.about is usually set in options.rpy.
            # if gui.about:
            #     text "[gui.about!t]\n"

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")
        
        null height 25


style empty_frame:
    background None
    xalign 0.5
    text_align 0.5
    padding(0,0,0,0)

style about_title_label_text:
    font "fonts/MyPrettyCutie.ttf"
    outlines [(10, "#16161d", 2, 2)]
    size 60
    text_align 0.5
    xalign 0.5

style about_role_label:
    xalign 0.5

style about_role_label_text:
    size 45
    text_align 0.5
    xalign 0.5

style about_person_text:
    font gui.interface_text_font
    size 35
    text_align 0.5
    xalign 0.5

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Preferences screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

default pref_text = True
default pref_vol = False

screen preferences():
    tag menu

    use game_menu(_("Settings"), scroll="viewport"):
        vbox:
            xfill True
            xalign 0.5
            null height 25
            hbox:
                style_prefix "header"
                xalign 0.5
                spacing 100
                textbutton "TEXT" action [SetScreenVariable("pref_text", True),SetScreenVariable("pref_vol", False)]
                textbutton "MUSIC" action [SetScreenVariable("pref_vol", True),SetScreenVariable("pref_text", False)]

            null height 25

            if pref_text and not pref_vol:

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 50
                    hbox:
                        spacing 100
                        vbox:
                            # xsize 550
                            style_prefix "check"
                            label _("Text")
                            textbutton _("Unseen Text") action Preference("skip", "toggle"):
                                tooltip "Skips the dialogue regardless\nif seen or unseen."
                            textbutton _("After Choices") action Preference("after choices", "toggle"):
                                tooltip "Keeps skipping, even on choices."
                            textbutton _("Comma Pausing") action ToggleField(persistent, "comma_pause"):
                                tooltip "Adds a slight delay per comma."

                        vbox:
                            style_prefix "radio"
                            label _("Rollback Side")
                            textbutton _("Disable") action Preference("rollback side", "disable"):
                                tooltip "Disable rollback entirely."
                            textbutton _("Left") action Preference("rollback side", "left"):
                                tooltip "Tapping the left side of the screen will\nrollback to a previous dialogue."
                            textbutton _("Right") action Preference("rollback side", "right"):
                                tooltip "Tapping the right side of the screen will\nrollback to a previous dialogue."

                    vbox:
                        xalign 0.5
                        xsize 700
                        style_prefix "slider"
                        label _("Text Speed")
                        bar value Preference("text speed"):
                            style "bar"
                            tooltip "The speed of the in-game dialogue text."

                        label _("Auto-Forward Time")
                        bar value Preference("auto-forward time"):
                            style "bar"
                            tooltip "The speed of the automation per dialogue.\n(The lower it is, the faster it gets.)"

            elif pref_vol and not pref_text: 

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 50
                    style_prefix "slider"
                    vbox:
                        xsize 700
                        if config.has_music:
                            label _("BGM Volume")
                            bar value Preference("music volume"):
                                style "bar"
                                tooltip "The loudness of background music throughout the game."

                        if config.has_sound:
                            label _("Sound Volume")
                            vbox:
                                bar value Preference("sound volume"):
                                    style "bar"
                                    tooltip "The loudness of sound effects throughout the game."

                                if config.sample_sound:
                                    textbutton _("Test") action Play("sound", config.sample_sound)
                    vbox:
                        xsize 700
                        if config.has_voice:
                            label _("Voice Volume")
                            hbox:
                                bar value Preference("voice volume"):
                                    style "bar"
                                    tooltip "The loudness of voice throughout the game."

                                if config.sample_voice:
                                    textbutton _("Test") action Play("voice", config.sample_voice)

                        label _("Ambient Volume")
                        bar value Preference("ambient volume"):
                            style "bar"
                            tooltip "The loudness of ambience throughout the game."

                    textbutton _("Mute All"):
                        action Preference("all mute", "toggle")
                        tooltip "Mute all sounds."
                        style "mute_all_button"
                        foreground "gui/phone/button/sound_[prefix_]foreground.png"
                        padding (75, 6, 6, 6)
                        xalign 0.5

        #         ## Additional vboxes of type "radio_pref" or "check_pref" can be
        #         ## added here, to add additional creator-defined preferences.

        #     # null height (4 * gui.pref_spacing)

        #     # null height 400

        #     label _("Music Settings"):
        #         xalign 0.5

        #     # null height 25

        #     hbox:
        #         style_prefix "slider"
        #         spacing 50
        #         vbox:
        #             xsize 550
        #             if config.has_music:
        #                 label _("BGM Volume")
        #                 bar value Preference("music volume"):
        #                     style "bar"
        #                     tooltip "The loudness of background music throughout the game."

        #             if config.has_sound:
        #                 label _("Sound Volume")
        #                 vbox:
        #                     bar value Preference("sound volume"):
        #                         style "bar"
        #                         tooltip "The loudness of sound effects throughout the game."

        #                     if config.sample_sound:
        #                         textbutton _("Test") action Play("sound", config.sample_sound)
        #         vbox:
        #             xsize 550
        #             if config.has_voice:
        #                 label _("Voice Volume")
        #                 hbox:
        #                     bar value Preference("voice volume"):
        #                         style "bar"
        #                         tooltip "The loudness of voice throughout the game."

        #                     if config.sample_voice:
        #                         textbutton _("Test") action Play("voice", config.sample_voice)

        #             label _("Ambient Volume")
        #             bar value Preference("ambient volume"):
        #                 style "bar"
        #                 tooltip "The loudness of ambience throughout the game."

        #     null height 20

        #     textbutton _("Mute All"):
        #         action Preference("all mute", "toggle")
        #         tooltip "Mute all sounds."
        #         style "mute_all_button"
        #         foreground "gui/phone/button/sound_[prefix_]foreground.png"
        #         padding (75, 6, 6, 6)
        #         xalign 0.5

        #             # null height 35

        #             # if config.has_music or config.has_sound or config.has_voice:
        #             #     null height gui.pref_spacing

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 675

style header_button_text:
    size 60
    font "fonts/MyPrettyCutie.ttf"
    outlines [(10, "#16161d", 2, 2)]


## History screen ##############################################################
##
## This is a screen that displays the dialogue history to the player. While
## there isn't anything special about this screen, it does have to access the
## dialogue history stored in _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Avoid predicting this screen, as it can be very large.
    predict False

    use game_menu(_("History"), scroll=("viewport"), yinitial=1.0):

        style_prefix "history"

        for h in _history_list:

            window:

                ## This lays things out properly if history_height is None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Take the color of the who text from the Character, if
                        ## set.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False
            
            null height 40

        if not _history_list:
            label _("The dialogue history is empty.")


## This determines what tags are allowed to be displayed on the history screen.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    # xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign
    # font gui.text_font
    font gui.name_text_font
    size 50

style history_text:
    xpos gui.history_text_xpos
    # ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize 900
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")
    font gui.text_font

# style history_label:
#     xfill True

# style history_label_text:
#     xalign 0.5


## Help screen #################################################################
##
## A screen that gives information about key and mouse bindings. It uses other
## screens (keyboard_help, mouse_help, and gamepad_help) to display the actual
## help.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Help"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Keyboard") action SetScreenVariable("device", "keyboard")
                textbutton _("Mouse") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Gamepad") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Space")
        text _("Advances dialogue without selecting choices.")

    hbox:
        label _("Arrow Keys")
        text _("Navigate the interface.")

    hbox:
        label _("Escape")
        text _("Accesses the game menu.")

    hbox:
        label _("Ctrl")
        text _("Skips dialogue while held down.")

    hbox:
        label _("Tab")
        text _("Toggles dialogue skipping.")

    hbox:
        label _("Page Up")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Page Down")
        text _("Rolls forward to later dialogue.")

    hbox:
        label "H"
        text _("Hides the user interface.")

    hbox:
        label "S"
        text _("Takes a screenshot.")

    hbox:
        label "V"
        text _("Toggles assistive {a=https://www.renpy.org/l/voicing}self-voicing{/a}.")

    hbox:
        label "Shift+A"
        text _("Opens the accessibility menu.")


screen mouse_help():

    hbox:
        label _("Left Click")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Middle Click")
        text _("Hides the user interface.")

    hbox:
        label _("Right Click")
        text _("Accesses the game menu.")

    hbox:
        label _("Mouse Wheel Up\nClick Rollback Side")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Mouse Wheel Down")
        text _("Rolls forward to later dialogue.")


screen gamepad_help():

    hbox:
        label _("Right Trigger\nA/Bottom Button")
        text _("Advances dialogue and activates the interface.")

    hbox:
        label _("Left Trigger\nLeft Shoulder")
        text _("Rolls back to earlier dialogue.")

    hbox:
        label _("Right Shoulder")
        text _("Rolls forward to later dialogue.")


    hbox:
        label _("D-Pad, Sticks")
        text _("Navigate the interface.")

    hbox:
        label _("Start, Guide")
        text _("Accesses the game menu.")

    hbox:
        label _("Y/Top Button")
        text _("Hides the user interface.")

    textbutton _("Calibrate") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.button_text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Additional screens
################################################################################


## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):
    
    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png":
        alpha 0.5

    frame:
        at screen_appear

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150
                imagebutton:
                    auto "gui/navigation/confirm_btn_%s.png"
                    foreground Text(_("Yes"), style="confirm_btn")
                    hover_foreground Text(_("Yes"), style="confirm_btn_hover")
                    selected_foreground Text(_("Yes"), style="confirm_btn_selected")
                    action yes_action
                imagebutton:
                    auto "gui/navigation/confirm_btn_%s.png"
                    foreground Text(_("No"), style="confirm_btn")
                    hover_foreground Text(_("No"), style="confirm_btn_hover")
                    selected_foreground Text(_("No"), style="confirm_btn_selected")
                    action no_action
                # textbutton _("Yes") action yes_action
                # textbutton _("No") action no_action

    ## Right-click and escape answer "no".
    key "game_menu" action no_action

style confirm_image_button:
    activate_sound "audio/sfx/click.mp3"

style confirm_btn_hover:
    color u"#fff"
    xalign 0.5
    yalign 0.5
    size gui.interface_text_size
    font gui.interface_text_font

style confirm_btn_selected:
    color u"#fff"
    xalign 0.5
    yalign 0.5
    size gui.interface_text_size
    font gui.interface_text_font

style confirm_btn:
    color gui.accent_color
    xalign 0.5
    yalign 0.5
    size gui.interface_text_size
    font gui.interface_text_font

style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"
    color gui.accent_color

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"
    add "gui/overlay/confirm.png":
        alpha 0.5

    vbox:
        xalign 0.5
        yalign 0.5
        text _("Skipping"):
            size 75
        hbox:
            spacing 9
            xalign 0.5
            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"

        if not renpy.is_seen(ever=True):
            text "C'mon. At least read the game."

    # frame:

    #     hbox:
    #         spacing 9

    #         text _("Skipping")

    #         text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
    #         text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
    #         text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## This transform is used to blink the arrows one after another.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text:
    is gui_text
    # color gui.accent_color
    outlines [(10, "#16161d", 2, 2)]
    xalign 0.5
    text_align 0.5
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## We have to use a font that has the BLACK RIGHT-POINTING SMALL TRIANGLE
    ## glyph in it.
    font "DejaVuSans.ttf"


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"
        # xalign 0.5
        # yalign 0.1

    timer 3.25 action Hide('notify')

# transform notify_appear:
#     on show:
#         alpha 0 xoffset -100
#         easein .5 alpha 1.0 xoffset 0
#     on hide:
#         easein .5 alpha 0.0 yoffset -50

transform notify_appear:
    on show:
        alpha 0 xanchor 1.0
        easein .5 xanchor 0.0 xoffset 10 alpha 1
    on hide, replaced:
        easein .5 alpha 0 yoffset -50


style notify_frame is empty
style notify_text:
    is gui_text
    color gui.accent_color
    # outlines [(5, "#000000b6", 2, 2)]

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", Borders(60,10,60,10), tile=gui.frame_tile)
    padding(50,35,50,35)
    # background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    # padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")


## Bubble screen ###############################################################
##
## The bubble screen is used to display dialogue to the player when using speech
## bubbles. The bubble screen takes the same parameters as the say screen, must
## create a displayable with the id of "what", and can create displayables with
## the "namebox", "who", and "window" ids.
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.


screen quick_menu():
    variant "mobile"
    style_prefix "quickmenu"
    zorder 1000

    if quick_menu:
        frame:
            hbox:
                xfill True
                box_wrap_spacing 1920
                hbox:
                    spacing 50
                    imagebutton auto _("gui/quickmenu/history_%s.png"):
                        action ShowMenu('history')
                        tooltip "History"
                    imagebutton auto _("gui/quickmenu/hide_%s.png"):
                        action HideInterface()
                        tooltip "Hide"
                    # imagebutton auto _("gui/quickmenu/load_%s.png"):
                    #     action ShowMenu('load')
                    #     tooltip "Load"
                    imagebutton auto _("gui/quickmenu/save_%s.png"):
                        action ShowMenu('file_slots')
                        tooltip "Saves"

                hbox:
                    spacing 50
                    xalign 1.0
                    if config.developer:
                        imagebutton auto _("gui/quickmenu/back_%s.png"):
                            action Rollback()
                            tooltip "Back"
                    imagebutton auto _("gui/quickmenu/settings_%s.png"):
                        action ShowMenu('emptymenu')
                        tooltip "Settings"
                    imagebutton auto _("gui/quickmenu/auto_%s.png"):
                        action Preference("auto-forward", "toggle")
                        tooltip "Auto"
                    imagebutton auto _("gui/quickmenu/skip_%s.png"):
                        action Skip() alternate Skip(fast=True, confirm=True)
                        tooltip "Skip"

        frame:
            yoffset 890
            xoffset -35
            xalign 1.0
            if journal:
                vbox:
                    imagebutton auto _("gui/quickmenu/journal_%s.png"):
                        action [ShowMenu('journal'), SetVariable("notify_journal", False)]
                        tooltip "Journal"
                        activate_sound None
                    if notify_journal:
                        add "gui/notif_dot.png" xoffset 45 yoffset -80

    # This has to be the last thing shown in the screen.

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            style_prefix "tooltip"
            prefer_top True
            frame:
                xalign 0.5
                # yoffset 125
                text tooltip:
                    size 35

style quickmenu_frame:
    background None
    padding(50,50,50,50)

style quickmenu_button_text:
    color gui.accent_color

style quickmenu_image_button:
    activate_sound "audio/sfx/click.mp3"

style tooltip_frame:
    background None
    padding(25,15,25,15)

style tooltip_text:
    xalign 0.5
    color u'#fff'
    yalign 0.5
    font gui.interface_text_font
    outlines [(3, "#16161d", 2, 2)]

style window:
    variant "mobile"
    background "gui/phone/textbox.png"

style radio_button:
    variant "mobile"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "mobile"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "mobile"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "mobile"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "mobile"
    # background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "mobile"
    xsize 420

style game_menu_content_frame:
    variant "mobile"
    # top_margin 0

style pref_vbox:
    variant "mobile"
    xsize None

style bar:
    variant "mobile"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)
    activate_sound "audio/sfx/click.mp3"

style vbar:
    variant "mobile"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "mobile"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb_offset 4

style vscrollbar:
    variant "mobile"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb_offset 4

style slider:
    variant "mobile"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "mobile"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "mobile"
    xsize None

style slider_slider:
    variant "mobile"
    xsize 525
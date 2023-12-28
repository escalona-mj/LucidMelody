screen extras_game_menu(title):
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
        viewport:
            scrollbars "vertical"
            mousewheel True
            draggable True
            pagekeys True
            side_yfill True
            vbox:
                transclude

    if main_menu:
        if not renpy.get_screen("extras_emptymenu"):
            key "game_menu" action ShowMenu("extras_emptymenu")
        else:
            key "game_menu" action ShowMenu("main_menu")

    imagebutton:
        auto "gui/navigation/return_%s.png"
        activate_sound "audio/sfx/click.ogg"
        hover_sound "audio/sfx/hover.ogg"
        focus_mask True
        xalign 0.0
        yalign 0.0
        if not renpy.get_screen("extras_emptymenu"):
            action ShowMenu("extras_emptymenu")
        else:
            action Return()

    label title style "game_menu_label"

style extras_game_menu_frame is empty
style extras_game_menu_frame:
    xsize 1200
    xalign 0.5
    yalign 0.5
    top_margin 0.15
    bottom_margin 0.01
    # background Frame("gui/test_frame.png", gui.frame_borders, tile=gui.frame_tile)

style extras_game_menu_side:
    spacing 0

style extras_game_menu_viewport:
    xfill True

style extras_game_menu_vscrollbar:
    unscrollable gui.unscrollable

screen extras_emptymenu():
    tag menu

    use extras_game_menu("Extras"):
        vbox:
            textbutton "Achievements" action ShowMenu("achievements")
            textbutton "CG GALLERY" action ShowMenu("cg_gallery")
            # textbutton "REPLAY GALLERY" action NullAction()
            textbutton "DREAM 1" action If(persistent.seen_dream1,
                                            true=Show("confirm",
                                                    message="Are you sure you want to replay Dream 1?",
                                                    yes_action=[Replay("dream1"), Hide()],
                                                    no_action=Hide()),
                                            false=Show("dialog",
                                                    message="You have not seen this part yet.",
                                                    ok_btn="OK",
                                                    ok_action=Hide())
                                            )
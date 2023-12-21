image splash_white = '#ECECF4'
image sky_color = '#008eff'
image logo_studio = "gui/logo_studio.png"
image renpy_logo = "gui/renpy-logo.png"

image splash_text = ParameterizedText(
    xalign=0.5,
    yalign=0.5,
    color='#ffffff',
    text_align=0.5,
    font='fonts/QuinnGothic.ttf'
)

label splashscreen:
    if renpy.variant("android") and not renpy.variant("tv"):
        $ renpy.music.play(config.main_menu_music)
        scene splash_white with None
        # show renpy_logo at truecenter:
        #     yalign 0.45
        # show splash_text "Made with Ren'Py.":
        #     yalign 0.6
        # with dissolve
        # pause 3.0
        # hide renpy_logo
        # hide splash_text
        # with dissolve
        show logo_studio:
            truecenter
            on show:
                alpha 0.0 zoom 1.5
                easein_back 1.0 alpha 1.0 zoom 1.0
        pause 3.0
        hide logo_studio
        show sky_color
        show splash_text "Some text here that will be changed."
        with dissolve
        pause 2.0
        return
    else:
        jump notAndroid

label notAndroid:
    # no
    if renpy.variant("tv"):
        call screen dialog(message="This game is only playable on Android devices.\n\nExcluding Android TV devices.", ok_action=Quit(confirm=False))
    else:
        call screen dialog(message="This game is only playable on Android devices.", ok_action=Quit(confirm=False))
    return
image splash_white = '#ECECF4'
image sky_color = '#008eff'
image logo_studio = "gui/logo_studio.png"
image renpy_logo = "gui/renpy-logo.png"

image splash_text = ParameterizedText(
    xalign=0.5,
    yalign=0.5,
    color='#ffffff',
    text_align=0.5,
    font='fonts/QuinnGothic.ttf',
    size=gui.interface_text_size
)


label splashscreen:
    if not renpy.variant("tv"):
        if renpy.variant("pc"):
            call screen dialog(message="The game has detected that you're running on a PC. The UI was initially\nmeant for small devices, so UI components might look big.", ok_btn="I understand.", ok_action=Return())
        $ config.rollback_enabled = False
        $ renpy.music.play(config.main_menu_music)
        scene splash_white with None
        if renpy.variant("small"):
            show logo_studio:
                truecenter
                on show:
                    alpha 0.0 zoom 1.5
                    easein_back 1.0 alpha 1.0 zoom 1.0
        else:
            show logo_studio:
                truecenter
                on show:
                    alpha 0.0 zoom 1.5
                    easein_back 1.0 alpha 1.0 zoom 0.75
        pause 3.0
        hide logo_studio
        show sky_color
        show splash_text "The melody is very lucid."
        with dissolve
        pause 2.0
        $ config.rollback_enabled = True
        return
    else:
        jump detectTV

label detectTV:
    call screen dialog(message="This game cannot be played on Android TV devices.", ok_btn="OK", ok_action=Quit(confirm=False))
    return
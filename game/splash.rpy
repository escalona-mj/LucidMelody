image splash_white = '#ECECF4'
image logo_studio = "gui/logo_studio.png"

label splashscreen:
    $ renpy.music.play(config.main_menu_music)
    scene splash_white
    show logo_studio:
        truecenter
        alpha 0.0 zoom 1.03
        ease 1.0 alpha 1.0 zoom 1.0
    pause 3.0
    hide logo_studio with dissolve
    return
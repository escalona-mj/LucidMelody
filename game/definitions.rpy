init python:
    def eyewarp(x):
        return x**1.33

#############################
#           IMAGES          #
#############################
image bg highway:
    im.Blur("images/bg/highway.jpg", 2.5)

image paimon = ("images/bg/Paimon.webp")


# Transform that blurs the background when opening screens.
transform withBlur:
    blur 30
transform noBlur:
    blur 0

transform tcommon:
    yanchor 1.0 subpixel True
    on show:
        ypos 1.03
        zoom 0.95 alpha 0.0
        xcenter 0.5 yoffset -20
        easein .25 yoffset 0 zoom 1.00 alpha 1.0
    on replace:
        alpha 1.00
        parallel:
            easein .25 xcenter 0.5 zoom 1.00
        parallel:
            easein .15 yoffset 0 ypos 1.03
    on hide:
        easein .25 zoom 0.95 alpha 0.0 yoffset -20


#############################
#        TRANSITIONS        #
#############################
define config.say_attribute_transition = Dissolve(.25, alpha=True)
define config.say_attribute_transition_layer = "master"



define wipeleft = ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64)
define wipeleft_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/wipeleft.png", 0.5, ramplen=64),
    True])
    
define long_dissolve = MultipleTransition([
    False, Dissolve(1.5),
    Solid("#000"), Pause(1.5),
    Solid("#000"), Dissolve(1.5),
    True])

define eye_scene = MultipleTransition([
    False, ImageDissolve("images/transitions/eyes.png", .5, ramplen=128, reverse=True, time_warp=eyewarp),
    Solid("#000"), Pause(1),
    Solid("#000"), ImageDissolve("images/transitions/eyes.png", .5 ,ramplen=128, time_warp=eyewarp),
    True])

define wipeleft_menu = ImageDissolve("images/transitions/wipeleft.png", 0.10, ramplen=64)
define wipeleft_menu_reverse = ImageDissolve("images/transitions/wipeleft.png", 0.10, reverse=True, ramplen=64)
define wipeleft_menu_afterLoad = MultipleTransition([
    False, ImageDissolve("images/transitions/wipeleft.png", 0.10, ramplen=64),
    Solid("#000"), Pause(0.25),
    Solid("#000"), ImageDissolve("images/transitions/wipeleft.png", 0.10, ramplen=64),
    True])

image camera_flash:
    Solid("#ffffff2c")
    pause 0.1
    Solid("#00000000")

# init:
#     $ fastdiv = {"master" : wipeleft}

define audio.merrygoround2 = "<loop 24.162>audio/bgm/merrygoround2.mp3"
default show_point = 0

default nick_likePoints = 0
default nick_likePointsMax = 100

default alec_likePoints = 0
define alec_likePointsMax = 100

#######################
# RELATIONSHIP SYSTEM #
#######################
init python:
    class AlecLoveMeter:
        def add(points):
            global show_point, alec_likePoints, alec_likePointsMax
            renpy.show_screen('alec_love_bar')
            renpy.play("audio/sfx/love_ding.mp3", channel="sfx2")
            renpy.pause(0)

            new_points = alec_likePoints + points
            show_point = points
            if new_points > alec_likePointsMax:
                alec_likePoints = alec_likePointsMax
            else:
                alec_likePoints = new_points

            
        def remove(points):
            global show_point, alec_likePoints, alec_likePointsMax
            renpy.show_screen('alec_love_bar')
            renpy.pause(0)
            alec_likePoints = max(0, alec_likePoints - points)


    class NickLoveMeter:
        def add(points):
            global show_point, nick_likePoints, nick_likePointsMax
            renpy.show_screen('nick_love_bar')
            renpy.play("audio/sfx/love_ding.mp3", channel="sfx2")
            renpy.pause(0)
            new_points = nick_likePoints + points
            show_point = points
            if new_points > nick_likePointsMax:
                nick_likePoints = nick_likePointsMax
            else:
                nick_likePoints = new_points


        def remove(points):
            global show_point, nick_likePoints, nick_likePointsMax
            renpy.show_screen('nick_love_bar')
            renpy.pause(0)
            nick_likePoints = max(0, nick_likePoints - points)


screen nick_love_bar():

    frame at screen_appear:
        xalign 0.5
        yalign 0.0
        yoffset -25
        background None
        has vbox
        
        hbox:
            text "[n_name]":
                yoffset 45
                xoffset 50
                textalign 0.0
                color '#e61841'
                font gui.game_menu_label_font
                size 60
                outlines [(5, "#ffffff", 2, 2)]

            text "+[show_point]":
                at transform:
                    alpha 0.0 yoffset 25
                    easein 0.5 yoffset 0 alpha 1.0
                    pause 1.0
                    easein 0.5 yoffset -25 alpha 0.0
                yoffset 50
                xoffset 200
                color '#138940'
                font gui.game_menu_label_font
                outlines [(5, "#ffffff", 2, 2)]

        bar value AnimatedValue(nick_likePoints, nick_likePointsMax, delay=1.0):
            xalign 0.5
            xmaximum 375
            ymaximum 90
            left_gutter 75
            right_gutter 23
            left_bar Frame("gui/bar/love_full.png")
            right_bar Frame("gui/bar/love_empty.png")

    timer 3.0 action Hide(screen="nick_love_bar")

screen alec_love_bar():

    frame at screen_appear:
        xalign 0.5
        yalign 0.0
        yoffset -25
        background None
        has vbox

        hbox:
            text "[mcNameboy]":
                yoffset 45
                xoffset 50
                textalign 0.0
                color '#e61841'
                font gui.game_menu_label_font
                size 60
                outlines [(5, "#ffffff", 2, 2)]

            text "+[show_point]":
                    at transform:
                        alpha 0.0 yoffset 25
                        easein 0.5 yoffset 0 alpha 1.0
                        pause 1.0
                        easein 0.5 yoffset -25 alpha 0.0
                    yoffset 50
                    xoffset 200
                    color '#138940'
                    font gui.game_menu_label_font
                    outlines [(5, "#ffffff", 2, 2)]

        bar value AnimatedValue(alec_likePoints, alec_likePointsMax, delay=1.0):
            xalign 0.5
            xmaximum 375
            ymaximum 90
            left_gutter 75
            right_gutter 23
            left_bar Frame("gui/bar/love_full.png")
            right_bar Frame("gui/bar/love_empty.png")

    timer 3.0 action Hide(screen="alec_love_bar")

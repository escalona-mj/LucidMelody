
############# achievement toast
transform achievement_transform:
    on show:
        alpha 0.0
        yoffset -150 alpha 0.0
        easein 0.7 yoffset 0 alpha 1.0
    on hide:
        alpha 1.0
        easeout 0.7 alpha 0.0
        

screen achievement_toast(title, description):
    zorder 500
    frame at achievement_transform:
        xalign 0.0
        yalign 0.0
        padding (20,20,40,20)
        background Frame("gui/achievements/achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
        hbox:
            yalign 0.5
            add "unlocked_medal" size (150, 150) yalign 0.5

            vbox:
                yalign 0.5
                label title style "achievements_label"
                text description style "achievements_text"
    timer 5.0 action Hide("achievement_toast")

init python:
    def achievement_get(ach_id):
        ach = persistent.achievement_list[ach_id]
        if not achievement.has(ach_id):
            achievement.grant(ach_id)
            persistent.unlocked_achievement += 1
            renpy.show_screen(_screen_name='achievement_toast', title=ach[0], description=ach[1])
            # renpy.play("audio/sfx/notify.ogg", channel="sound")
        else:
            pass
        
############# achievement list
default persistent.unlocked_achievement = 0 #counts the unlocked achievements
default locked_achievement = len(persistent.achievement_list)

define persistent.achievement_list = {
    # "ach_id": [
        #_("ach[0]"),
        #_("ach[1]"),
        #],
        
    "start": [
        _("New Beginnings"),
        _("Start a new game for the very first time.")
        ],

    "end": [
        _("Closure"),
        _("The story ends here.")
        ],

    "dsvds": [
        _("sds"),
        _("The sts ends here.")
        ],
    
    "dsvads": [
        _("sds"),
        _("Theasdss here.")
        ],

    "dsvassds": [
        _("sds"),
        _("Thaaa ends here.")
        ]

    ,"dsvssads": [
        _("sds"),
        _("The stsdashere.")
        ]

    }

define lockaname = "Achievement Locked."
define lockdesc = "???"

image unlocked_medal = "gui/achievements/medal.png"
image locked_medal = "gui/achievements/locked_medal.png"

screen achievements():
    tag menu
    use bg
    add "gui/overlay/confirm.png":
        alpha 0.75
    add "gui/phone/overlay/game_menu.png"

    use game_menu(_("Achievements [persistent.unlocked_achievement]/[locked_achievement]"), scroll="viewport"):

        style_prefix "achievements"
        vbox:
            spacing 5
            for k, v in persistent.achievement_list.items():
                frame:
                    if achievement.has(k):
                        hbox:
                            yalign 0.5
                            add "unlocked_medal" yalign 0.5

                            vbox:
                                yalign 0.5
                                label _(v[0])
                                text _(v[1])
                    else:
                        hbox:
                            yalign 0.5
                            add "locked_medal" yalign 0.5

                            vbox:
                                yalign 0.5
                                style_prefix "locked"
                                label _("[lockaname]")
                                text _("[lockdesc]")
            # text "You have unlocked [persistent.unlocked_achievement] out of [locked_achievement] achievements.":
            #     xalign 0.5
            #     size 45
    use extras_navigation
        
style achievements_vbox is vbox
style achievements_frame is empty

style achievements_label_text: #unlocked achievement name
    yalign 0.5
    color u'#fff'

style achievements_text: #unlocked achievement description
    yalign 0.5
    color u'#fff'
    size 30

style locked_label_text: #locked achievement name
    yalign 0.5
    color u'#b5b5b5'

style locked_text: #locked description
    yalign 0.5
    color u'#b5b5b5'
    size 30



style achievements_frame:
    background Frame("gui/achievements/achievement_frame.png", gui.achievement_frame_borders, tile=gui.frame_tile)
    padding (20, 20, 20, 20)
    xfill True

define dev_note = _p("""
Your dedication to completing the game means the world to us. In our gratitude, please accept this small gift from us.
""")

screen secret_menu():
    tag menu
    if main_menu:
        use bg
        add "gui/phone/overlay/game_menu.png"
    else:
        add "gui/phone/overlay/game_menu.png"
    use extras_navigation

    label "Hall of Completionists" style "game_menu_label":
        xalign 0.5
        
    viewport:
        xsize 1200
        ysize 750   
        xalign 0.5
        yalign 0.55 
        scrollbars "vertical"
        mousewheel True
        draggable True
        pagekeys True
        vbox:
            frame:
                style_prefix "achievements"
                xalign 0.5
                # background Frame("gui/achievements/hidden_achievement_frame.png", gui.confirm_frame_borders, tile=gui.frame_tile)
                xfill True
                hbox:
                    yalign 0.5
                    xalign 0.5
                    add "unlocked_medal" size (150, 150) yalign 0.5
                    
                    vbox:
                        yalign 0.5
                        xalign 0.5
                        label _("Outstanding!"):
                            xalign 0.5
                        text _("You unlocked all achievements!"):
                            xalign 0.5
                    
                    add "unlocked_medal" size (150, 150) yalign 0.5
            text "[dev_note]":
                xalign 0.5
            text "{a=https://www.youtube.com/watch?v=dQw4w9WgXcQ}Click here to get your gift!{/a}":
                xalign 0.5

## Extras Navigation screen ############################################################
##
## This is the same as the Game Menu Navigation screen, but just for the Extras.
screen extras_navigation():

    hbox:
        style_prefix "navigation"
        xalign 0.5
        yalign 0.95
        spacing 70

        textbutton _("Achievements") action ShowMenu("achievements") alt "Achievements"

        #for completionists
        # if persistent.unlocked_achievement == locked_achievement:
        textbutton _("Hall of Completionists") action ShowMenu("secret_menu") alt "Hall of Completionist"

        # else:

        #     textbutton _("???") action None alt "Locked Option"
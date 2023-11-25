init python:
    if not renpy.variant("pc"):
        config.always_shown_screens = ["dev_screen"]

    def delete_all_saves():
        for i in renpy.list_saved_games(fast=True):
            renpy.unlink_save(i)
            
    def delete_persistent():
        persistent._clear(True)
        delete_all_saves()
        renpy.reload_script()

    def addPointToAlec():
        Alec.add(10)
    def addPointToNick():
        Nick.add(10)

    def removePointToAlec():
        Alec.remove(10)
    def removePointToNick():
        Nick.remove(10)

    def AddDream():
        add_entry(entry1)
    def RemoveDream():
        remove_entry(entry1)

screen dev_screen():
    default devtools = False
    zorder 1000

    showif devtools:
        add "gui/overlay/confirm.png":
            at transform:
                truecenter
                on show:
                    alpha 0
                    easein .25 alpha 0.75
                on hide:
                    alpha 0.75
                    easein .25 alpha 0

        frame at screen_appear:
            background None
            modal True
            xalign 0.5
            yalign 0.5
            text "Dev Tools" style "game_menu_label_text":
                xalign 0.5
                yalign 0.0

            grid 3 2:
                xalign 0.5
                yalign 0.5
                spacing 10
                vbox:
                    yalign 0.5
                    label "Other stuff"
                    style_prefix "check"
                    textbutton "Open achievements" action ShowMenu("achievements")
                    textbutton "Force rollback" action Rollback()
                    textbutton "Toggle developer mode" action ToggleVariable("config.developer", True, False)
                if not main_menu:
                    vbox:
                        yalign 0.5
                        label "Journal testing"
                        style_prefix "check"
                        textbutton "has Journal? {0}".format(journal) action ToggleVariable("journal", True, False)
                        if current_route == "dhannica" or current_route == "alec":
                            textbutton "meet Alec? {0}".format(meetAlec) action ToggleVariable("meetAlec", True, False)
                            textbutton "meet Nick? {0}".format(meetNick) action ToggleVariable("meetNick", True, False)
                        elif current_route == "nick":
                            textbutton "meet Dhannica? {0}".format(meetDhannica) action ToggleVariable("meetDhannica", True, False)
                        textbutton "Add dream entry" action Function(AddDream)
                        textbutton "Remove dream entry" action Function(RemoveDream)
                vbox:
                    yalign 0.5
                    label "Progress (very destructive)"
                    style_prefix "check"
                    textbutton "Delete all saves" action Show("confirm", message="Are you sure you want to delete all the saves?", yes_action=[Function(delete_all_saves), Hide()], no_action=Hide(), _layer="front")
                    textbutton "Delete persistent" action Show("confirm", message="Are you sure you want to delete persistent data?\n(This will also delete all the saves.)", yes_action=Function(delete_persistent), no_action=Hide(), _layer="front")
                vbox:
                    yalign 0.5
                    label "Screen size (testing only)"
                    style_prefix "check"
                    textbutton _("toggle fullscreen") action If(preferences.fullscreen==False, Preference('display', 'fullscreen'), Preference('display', 'window'))
                    textbutton "tablet screen" action Preference("display", 0.5)
                    textbutton "phone screen" action Preference("display", 0.35)
                if not main_menu:
                    vbox:
                        label "Point manager"
                        style_prefix "check"
                        textbutton "Add 10pts to Alec" action Function(addPointToAlec)
                        textbutton "Remove 10pts to Alec" action Function(removePointToAlec)
                        textbutton "Add 10pts to Nick" action Function(addPointToNick)
                        textbutton "Remove 10pts to Alec" action Function(removePointToNick)
                    vbox:
                        yalign 0.5
                        text "Alec points = {0}".format(alec_likePoints) color "#fff"
                        text "Nick points = {0}".format(nick_likePoints) color "#fff"
                
    fixed:
        imagebutton:
            xalign 0.5
            yalign 0.0
            yoffset 25
            at transform:
                zoom 0.5
            idle "gui/dev_tools.png"
            activate_sound "audio/sfx/click.mp3"
            action ToggleLocalVariable("devtools", True, False)


# init python:
#     build.classify("**debug.rpy", None)
#     build.classify("**debug.rpyc", None)

init python:
    if config.developer:
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

style test_text:
    outlines [(3, "#16161d", 0, 1)]

init python:
    def make_it_unseen():
        renpy.mark_label_unseen("dream1")

screen dev_screen():
    default devtools = False
    zorder 1000

    vbox:
        at transform:
            alpha 0.5
        style_prefix "test"
        $ small_output = renpy.variant("small")
        text "Is Small Variant?: [small_output]"
        $ pc_output = renpy.variant("pc")
        text "Is PC Variant?: [pc_output]"
        $ mobile_output = renpy.variant("mobile")
        text "Is Mobile Variant?: [mobile_output]"
        $ touch_output = renpy.variant("touch")
        text "Is Touch Variant?: [touch_output]"
        $ android_output = renpy.variant("android")
        text "Is Android Variant?: [android_output]"
        $ dev_mode = config.developer
        text "Is developer?: [dev_mode]"
        $ ingameMenu = _game_menu_screen
        text "Which game menu are we in: [ingameMenu]"
        $ what_replay = _in_replay
        text "We're in replay [what_replay]"
        $ underscore_skip = _skipping
        text "_skipping = [underscore_skip]"
        $ seen_label = renpy.seen_label("dream1")
        text "Dream1 has been seen? [seen_label]"
        # textbutton "make it unseen" action make_it_unseen()
        text "Alec points = {0}".format(alec_likePoints)
        text "Nick points = {0}".format(nick_likePoints)

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
                    textbutton "Open extras" action ShowMenu("extras")
                    textbutton "Open menu" action ShowMenu("emptymenu")
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
                
    fixed:
        imagebutton:
            xalign 0.5
            yalign 0.0
            yoffset 25
            at transform:
                zoom 0.5
            idle "gui/dev_tools.png"
            activate_sound "audio/sfx/click.ogg"
            action ToggleLocalVariable("devtools", True, False)

style test_text:
    size 25

# init python:
#     build.classify("**debug.rpy", None)
#     build.classify("**debug.rpyc", None)

# screen dialog(message, ok_action):
#     on "show" action Function(renpy.show_layer_at, withBlur, layer="master")
#     on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
#     modal True

#     zorder 200

#     style_prefix "confirm"

#     add "gui/overlay/confirm.png"
#     key "K_RETURN" action [ok_action]

#     frame:

#         has vbox:
#             xalign .5
#             yalign .5
#             spacing 30

#         label _(message):
#             style "confirm_prompt"
#             xalign 0.5

#         hbox:
#             xalign 0.5
#             spacing 100

#             imagebutton:
#                 auto "gui/navigation/confirm_btn_%s.png"
#                 foreground Text(_("Yes"), style="confirm_btn")
#                 hover_foreground Text(_("Yes"), style="confirm_btn_hover")
#                 selected_foreground Text(_("Yes"), style="confirm_btn_selected")
#                 action ok_action

################    CHOOSE MC     ######################
transform blur_img:
    alpha 0
    choice:
        ease 2.0 alpha 0.5
    choice:
        ease 4.0 alpha 0.5
    choice:
        ease 1.0 alpha 0.8
    choice:
        ease 10 alpha 1.0
    ease 7 alpha 0
    repeat

transform blink:
    choice:
        ease 1.0 alpha 1.0
    choice:
        ease 0.2 alpha 1.0
    choice:
        ease 0.5 alpha 1.0
    choice:
        ease 0.7 alpha 1.0
    ease 1.0 alpha 0.0
    repeat

image firefly:
    "gui/firefly.png"
    choice:
        ease 1.0
        "gui/fireflyellow.png"
    choice:
        ease 0.2
        "gui/fireflyellow.png"
    choice:
        ease 0.5
        "gui/fireflyellow.png"
    choice:
        ease 0.7
        "gui/fireflyellow.png"
    ease 1.0
    repeat

image fireflies = SnowBlossom(At("firefly", blink), count=20, xspeed=(0,-10), yspeed=(-150,-90), fast=False, horizontal=False)

image girlMC:
    im.MatrixColor("images/characters/dhannica/base.png", im.matrix.brightness(1))

image boyMC:
    im.MatrixColor("images/characters/alec/base.png", im.matrix.brightness(1))

screen chooseMC():
    add "black"
    add "gui/chooseMC.png" at blur_img
    add "fireflies"
    if persistent.first_gameplay == False:
        text "Please choose your gender.":
            xalign 0.5
            yalign 0.25
    else:
        pass
    fixed:
        spacing 10
        imagebutton:
            xalign 0.0
            yalign 1.0
            idle "girlMC"
            action Hide("chooseMC", transition=eye_scene), Call("chooseFemale")
            tooltip "I'm a girl."
            focus_mask True
        imagebutton:
            xalign 1.0
            yalign 1.0
            idle "boyMC"
            action Hide("chooseMC", transition=eye_scene), Call("chooseMale")
            tooltip "I'm a boy."
            focus_mask True

    $ tooltip = GetTooltip()

    if tooltip:
        frame:
            xalign 0.5
            yalign 0.35
            style_prefix "tooltip"
            text tooltip:
                size 50

style text:
    color u'#fff'
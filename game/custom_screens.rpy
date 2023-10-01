screen chooseMC():
    add "gui/overlay/confirm.png"
    text "Choose a character":
        xalign 0.5
        yalign 0.25
    fixed at tcommon:
        imagebutton:
            idle "lucy"
            action Call("femaleMC")
            xalign -0.1
            yalign 1.0
            tooltip "girl"
            focus_mask True
        imagebutton:
            idle "images/bg/nick.png"
            action Call("maleMC")
            xalign 0.9
            yalign 1.0
            tooltip "boy"
            focus_mask True

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True

            frame:
                xalign 0.5
                padding (30,20,20,20)
                text tooltip style "tooltip_hover":
                    size 45
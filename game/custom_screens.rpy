screen chooseMC():
    add "gui/overlay/confirm.png"
    text "Choose a character":
        xalign 0.5
        yalign 0.25
    fixed at tcommon:
        imagebutton:
            idle "dhannica"
            action Call("choseFemale")
            xalign -0.1
            yalign 1.0
            tooltip "girl"
            focus_mask True
        imagebutton:
            idle "alec"
            action Call("choseMale")
            xalign 0.9
            yalign 1.0
            tooltip "boy"
            focus_mask True

    $ tooltip = GetTooltip()

    if tooltip:

        nearrect:
            focus "tooltip"
            prefer_top True
            style_prefix "tooltip"
            frame:
                xalign 0.5
                text tooltip:
                    size 35
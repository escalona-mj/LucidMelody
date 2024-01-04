image intro_text = ParameterizedText(
    xalign=0.5,
    yalign=0.5,
    color='#ffffff',
    text_align=0.5
)



label start:
    scene black
    stop music fadeout 3.0
    with blur_fade
    show intro_text "The story adapts on the choices you make.\nIt is tailored by how you play." with dissolve
    pause 5.0
    hide intro_text with dissolve

    call chap1_dhannica from _call_chap1_dhannica
    call chap2_dhannica from _call_chap2_dhannica

    return
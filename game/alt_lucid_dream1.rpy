label alt_lucid_dream1:
    # get out of replay
    $ _in_replay = False
    # lucid dream. completely out of the main timeline
    $ current_route = "lucid"
    camera:
        matrixcolor SaturationMatrix(1.0)
        easein 1.0 matrixcolor SaturationMatrix(0.5)
    dhannica "You must have misunderstood me."
    show dirt_overlay onlayer dream behind black_bars:
        alpha 0.0
        linear 5.0 alpha 1.0
        parallel:
            pulse_bright
    camera:
        zoom 1.5 xalign 0.5
    show dhannica_gojo_bg
    show dhannica_gojo eyeclose:
        subpixel True xalign 0.5 blur 50 yalign -0.5 zoom 2
    show dhannica_gojo_light at pulse_bright
    with dissolve
    d_singer "H-huh?"
    show cg_dhannica_gojo
    hide cg_dhannica_gojo
    show dhannica_gojo -eyeclose:
        easein 0.5 xalign 0.5 yalign 1.0 zoom 1.0 blur 0 
    camera:
        easein 0.5 zoom 1.1 truecenter
        parallel:
            choice:
                ease 1.0 xoffset 5 yoffset 10
            choice:
                ease 1.0 xoffset -5 yoffset 10
            choice:
                ease 1.0 xoffset 5 yoffset -10
            choice:
                ease 1.0 xoffset -5 yoffset -10
            repeat
    dhannica "I don't think you understand."
    show dhannica_gojo eyeclose:
        xalign 0.5 yalign 1.0 zoom 1.0 blur 0 
        easein .1 yoffset 20
        easeout .1 yoffset 0
    dhannica "I said..."
    show cg_dhannica_gojo_nah
    hide cg_dhannica_gojo_nah
    with None
    show dhannica_gojo -eyeclose with None
    show nah onlayer dream:
        xpos 1100 ypos 150 alpha 0.0
        ease 1.0 alpha 1.0
    dhannica "No thanks."
    stop ambient 
    camera:
        parallel:
            desaturate
    hide nah onlayer dream
    hide black_bars onlayer dream
    hide dust_particle onlayer dream behind black_bars
    hide dust_particle_blur onlayer dream behind black_bars
    scene bg dhannica room
    with None
    $ DreamScene.stop("dream1")
    if not config.developer:
        $ renpy.block_rollback()
    dhannica ".....!{fast}" with vpunch
    dhannica_i "..."
    dhannica "Another nightmare..."
    "You look around your room to find your phone and check the time."
    dhannica "5:30AM..."
    "Since it was still early, you made your bed before leaving your bedroom. Once you were done, you head downstairs."
    window auto
    scene bg living room with blur_fade
    dhannica_i "Time to make breakfast."
    "You went through the kitchen and rummage through everything to cook something for yourself."
    dhannica_i "Maybe I should cook some for my Mom as well."
    "You found eggs, thawed out hotdogs and some leftover food last night."
    dhannica_i "Oh yeah, I didn't get to eat last night..."
    dhannica_i "Eh, might as well reheat it."
    "The sound of sizzling of your cooking echoes throughout the house."
    unknown "Hello?"
    "You turn around and see someone in peeking in the kitchen doorway."
    show mom at trans3
    girlMom "Oh, good morning."
    dhannica "Hi Mom, good morning."
    girlMom "What made you cook this early?"
    dhannica "Had a nightmare... Just trying to get it off my mind by cooking."
    girlMom "Oh sweetie..."
    hide mom at trans3
    "Your mother wrapped her arms around you."
    "The hug of motherly love eases you off."
    dhannica "Thanks Mom."
    girlMom "Now, now. I'll handle the cooking, and you get yourself prepared for your first day of school."
    "You nodded, and went back to you room."
    scene bg dhannica room with blur_fade
    dhannica_i "Now, let's see."
    $ journal = True
    $ update_journal("Journal unlocked.")
    "You rummage through your room, looking for your newly bought bag and school supplies."
    dhannica_i "I guess that's everything."
    block "END"
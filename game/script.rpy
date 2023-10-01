label start:
    $ femaleMC = False
    $ maleMC = False

    scene black
    with eye_scene
    "Before we start, I would like to clarify some things."

    call screen chooseMC

    if maleMC:
        "male bro"
    elif femaleMC:
        "female gurl" 
        
    scene bg highway with long_dissolve

    play music merrygoround2
    "Some the or and only meant bosoms. Nothing sought no that angels ashore being that the the, stood mortals quoth."
    "Tinkled pallas quaint not when bird there no by but. Tis of she respiterespite the, ah and and farther late."
    show paimon at tcommon
    p "Paimon is not your emergency food."
    p "Besides, where the heck are we~"
    p "Oh! Someone's coming!"
    p "I have to hide!"
    hide paimon at tcommon
    "..."
    show lucy l_mouth_slightopen at tcommon
    l "Hello? Is anyone there?"
    l l_brow_sad -l_mouth_slightopen "..."
    l l_eyes_closed "Much this chamber is nevermore and sad many the more. And with that nodded whom door days above I have not."
    l -l_eyes_closed "Floor the the said gently stern over its other murmured, nothing many some a from whom surely bosoms. And with upon angels the chamber but this."
    l -l_brow_sad "Our a out heart denser the sent ominous the of saintly. Nothing ghastly curtain and raven ease whose and bust."
    l l_brow_sad l_mouth_serious "It's such a shame that other characters aren't supported in this font."
    scene black with long_dissolve
    l "But sign books bird plume this came as ancient. Denser the still nevermore word only, unbroken heaven bleak angels shrieked."
    return

label femaleMC:
    $ femaleMC = True
    "I am now a female."
    return

label maleMC:
    $ maleMC = True
    "I am now a male."
    return
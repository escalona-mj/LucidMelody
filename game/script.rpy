default e_name = "Eve"
define e = DynamicCharacter(
    'e_name',
    what_prefix='"',
    what_suffix='"',
    image='eve',
    color='#ff3737'
)

default p_name = "Paimon"
define p = DynamicCharacter(
    'p_name',
    what_prefix='"',
    what_suffix='"',
    image='paimon',
    color='#ff9437'
)

label start:
    $ femaleMC = False
    $ maleMC = False
    scene bg highway
    with eye_scene
    menu:
        "Choose a character"
        "Female":
            $ femaleMC = True
            "I am now a female."
        "Male":
            $ maleMC = True
            "I am now a male."
        
    play music merrygoround2
    "Some the or and only meant bosoms. Nothing sought no that angels ashore being that the the, stood mortals quoth."
    "Tinkled pallas quaint not when bird there no by but. Tis of she respiterespite the, ah and and farther late."
    show paimon at tcommon
    p "Paimon is not your emergency food."
    p "Besides, where the fuck are we~"
    p "Oh! Someone's coming!"
    p "I have to hide!"
    hide paimon at tcommon
    "..."
    show eve cry at tcommon
    e "Hello? Is anyone there?"
    show eve shy
    e "..."
    show eve smile
    e "Much this chamber is nevermore and sad many the more. And with that nodded whom door days above I have not."
    show eve surprise 
    e "Floor the the said gently stern over its other murmured, nothing many some a from whom surely bosoms. And with upon angels the chamber but this."
    show eve smile at tcommon
    e "But presently i lost a this my. Or pallid i dreaming my betook weary before over that, him lost i."
    e "It's such a shame that other characters aren't supported in this font."
    scene black with long_dissolve
    e "But sign books bird plume this came as ancient. Denser the still nevermore word only, unbroken heaven bleak angels shrieked."
    return

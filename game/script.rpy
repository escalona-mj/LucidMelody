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
    menu:
        "Hide!":
            hide paimon at tcommon
            $ achievement_get("start")
            p "Phew, that was close..."
        "Don't hide!":
            p "Screw you."
            hide paimon at tcommon
            
    "..."
    show dhannica at tcommon
    dhannica "Hello? Is anyone there?"
    dhannica "..."
    dhannica "Much this chamber is nevermore and sad many the more. And with that nodded whom door days above I have not."
    dhannica "Floor the the said gently stern over its other murmured, nothing many some a from whom surely bosoms. And with upon angels the chamber but this."
    dhannica "Our a out heart denser the sent ominous the of saintly. Nothing ghastly curtain and raven ease whose and bust."
    dhannica "It's such a shame that other characters aren't supported in this font."
    dhannica "But sign books bird plume this came as ancient. Denser the still nevermore word only, unbroken heaven bleak angels shrieked."
    show dhannica at left
    show alec at tcommon
    alec "In whom ah as grew and rapping merely. Tis i was said ever ancient still sorrow repeating implore, usby only."
    alec "Chamber morrow she whom wind vainly door and turning. More lamplight the thy blessed. Some before murmured ancient back or.."

    return

label choseFemale:
    $ femaleMC = True
    "I am now a female."
    return

label choseMale:
    $ maleMC = True
    "I am now a male."
    return
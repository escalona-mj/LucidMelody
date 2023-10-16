init python:
    new_game_messages = [
    "You know the drill.",
    "Did you want to take a different path?",
    "It's all the same.",
    "Why even bother toying with them?"
    ]

default current_route = 'common'
default persistent.first_gameplay = False

default Main = ""

image intro_text = ParameterizedText(
    xalign=0.5,
    yalign=0.5,
    color='#ffffff',
    text_align=0.5
)

label chooseFemale:
    $ current_route = 'dhannica'
    $ mcNameboy = 'Alec'
    $ Main = renpy.input("Enter your name (Press Enter without typing your name to use default name.)", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    $ Main = Main.strip()
    if not Main:
        $ Main = "Dhannica"
    $ mcNamegirl = "[Main]"
    return

label chooseMale:
    $ current_route = 'alec'
    $ mcNamegirl = 'Dhannica'
    $ Main = renpy.input("Enter your name (Press Enter without typing your name to use default name.)", length=12, allow="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz")
    $ Main = Main.strip()
    if not Main:
        $ Main = "Alec"
    $ mcNameboy = "[Main]"
    return

label start:
    scene black
    with eye_scene
    if persistent.first_gameplay == True:
        $ intro = renpy.random.choice(new_game_messages)
        show intro_text "[intro]" with Dissolve(0.5)
        pause 3.0
        hide intro_text with Dissolve(0.5)
    if persistent.first_gameplay == False:
        show intro_text "Before you start, the game would like to clarify some things." with Dissolve(0.5)
        pause 3.0
        hide intro_text with Dissolve(0.5)
        $ persistent.first_gameplay = True

    call screen chooseMC with eye_open

    pause 1.0

    show intro_text "The story adapts on the choices you make.\nIt is tailored by how you play." with Dissolve(0.5)
    pause 5.0
        
    scene bg highway with long_dissolve

    "boy name is [alec] girl name is [dhannica]"

    # play music merrygoround2
    $ welcome.grant()
    $ achievement2.grant()

    "Some the or and only meant bosoms. Nothing sought no that angels ashore being that the the, stood mortals quoth."
    show dhannica at appear_center
    "Let me go to left"
    show dhannica at appear_left
    "I go left"
    show dhannica at appear_right
    "..."
    show dhannica at appear_center
    "brb"
    hide dhannica at appear
    "Tinkled pallas quaint not when bird there no by but. Tis of she respiterespite the, ah and and farther late."
    show paimon at appear_center
    p "Paimon is not your emergency food."
    p "Besides, where the heck are we~"
    p "Oh! Someone's coming!"
    menu:
        p "What should I do?!"
        "Hide!":
            hide paimon at appear_center
            p "Phew, that was close..."
        "Don't hide!":
            p "Screw you."
            hide paimon at appear_center
            
    "..."
    show dhannica at appear_center
    dhannica "Hello? Is anyone there?"
    dhannica "..."
    dhannica "Much this chamber is nevermore and sad many the more. And with that nodded whom door days above I have not."
    dhannica "Floor the the said gently stern over its other murmured, nothing many some a from whom surely bosoms. And with upon angels the chamber but this."
    dhannica "Our a out heart denser the sent ominous the of saintly. Nothing ghastly curtain and raven ease whose and bust."
    dhannica "It's such a shame that other characters aren't supported in this font."
    dhannica "But sign books bird plume this came as ancient. Denser the still nevermore word only, unbroken heaven bleak angels shrieked."
    show dhannica at appear_left
    show alec at appear_center
    alec "In whom ah as grew and rapping merely. Tis i was said ever ancient still sorrow repeating implore, usby only."
    alec "Chamber morrow she whom wind vainly door and turning. More lamplight the thy blessed. Some before murmured ancient back or.."

    return
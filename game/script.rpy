default current_route = 'common'
default chapter = 0
default persistent.first_gameplay = False

image intro_text = ParameterizedText(
    xalign=0.5,
    yalign=0.5,
    color='#ffffff',
    text_align=0.5
)

init python:
    new_game_messages = [
    "Did you want to take a different path?",
    "Something tells me you're curious about the other.",
    "Trying to change something?"
    ]

label start:
    $ _game_menu_screen = None
    $ DisableSkip.start()
    scene black
    with fade

    if persistent.first_gameplay == False:
        show intro_text "Before you start, the game would like to clarify some things." with dissolve
        pause 3.0
        hide intro_text with dissolve
    else:
        $ random_intro = renpy.random.choice(new_game_messages)
        show intro_text "[random_intro]" with dissolve
        pause 3.0
        hide intro_text with dissolve

    call screen chooseMC with fade
    $ persistent.first_gameplay = True

    pause 1.0

    stop music fadeout 3.0
 
    show intro_text "The story adapts on the choices you make.\nIt is tailored by how you play." with dissolve
    pause 5.0
    hide intro_text with dissolve

    if current_route == "dhannica":
        jump dhannica_chap1
    elif current_route == "alec":
        jump alec_chap1

    return
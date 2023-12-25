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
    "You ever wonder how things would've gone\nif you just did one thing differently?"
    ]

label start:
    #declare the characters in the journal
    $ Dhannica = CharInfo(
    char_name="[mcNamegirl]",
    description="[dhannica_description]",
    points="dhannica_likePoints",
    max_points="dhannica_likePointsMax",
    pic="journal_dhannica")

    $ Nick = CharInfo(
    char_name="[mcNameboy]",
    description="[nick_description]",
    points="nick_likePoints",
    max_points="nick_likePointsMax",
    pic="journal_nick")

    $ Alec = CharInfo(
    char_name="[a_name]",
    description="[alec_description]",
    points="alec_likePoints",
    max_points="alec_likePointsMax",
    pic="journal_alec")

    $ DisableSkip.start()
    scene black
    with scenefade

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
    if not config.developer:
        $ renpy.block_rollback()
    show intro_text "The story adapts on the choices you make.\nIt is tailored by how you play." with dissolve
    pause 5.0
    hide intro_text with dissolve

    if current_route == "dhannica":
        jump chap1_dhannica
    elif current_route == "nick":
        jump chap1_nick

    return
image chapter_num = ParameterizedText(
    xalign=0.5,
    yalign=0.45,
    size=70,
    color='#ffffff',
    text_align=0.5
)

image chapter_text = ParameterizedText(
    xalign=0.5,
    yalign=0.53,
    size=50,
    color='#ffffff',
    text_align=0.5
)

label chapter_transition:
    $ DisableSkip.start()
    scene black with fade
    $ chapter = chapter+1
    play sound "audio/sfx/new_chapter.mp3" noloop
    pause 0.45
    if current_route == "dhannica":
        if chapter == 1:
            show chapter_num "Chapter 1"
            pause 0.5
            show chapter_text "The Enigmatic Concert"
            pause 4.0
        elif chapter == 2:
            show chapter_num "Chapter 2"
            pause 0.5
            show chapter_text "A Connection Beyond Dreams"
            pause 4.0
        elif chapter == 3:
            show chapter_num "Chapter 3"
            pause 0.5
            show chapter_text "Fragments of Reality"
            pause 4.0
        elif chapter == 4:
            show chapter_num "Chapter 4"
            pause 0.5
            show chapter_text "Echoes of the Past"
            pause 4.0
        elif chapter == 5:
            show chapter_num "Chapter 5"
            pause 0.5
            show chapter_text "Harmonies and Dissonances"
            pause 4.0
    elif current_route == 'alec':
        if chapter == 1:
            show chapter_num "Chapter 1"
            pause 0.5
            show chapter_text "Death"
            pause 4.0
    
    hide chapter_num
    hide chapter_text
    with dissolve
    $ DisableSkip.stop()
    $ _game_menu_screen = 'save_screen'
    return
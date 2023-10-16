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
    scene black with fade
    $ chapter = chapter+1
    play sound "audio/sfx/new_chapter.mp3" noloop
    pause 0.45
    if chapter == 1:
        if current_route == "dhannica":
            show chapter_num "Chapter 1"
            pause 0.5
            show chapter_text "The Enigmatic Concert"
            pause 4.0
    $ DisableSkip.stop()
    return
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

default chapter = 0
default chapter_name = None
default current_chapter = 0
default chapter_list = ['The Enigmatic Concert', #1
                'A Connection Beyond Dreams', #2
                'Fragments of Reality', #3
                'Echoes of the Past', #4
                'Harmonies and Dissonances' #5
                ]

label chapter_transition:
    $ DisableSkip.start()
    scene black with fade
    $ chapter = chapter + 1
    $ current_chapter = current_chapter + 1
    $ chapter_name = chapter_list[current_chapter - 1]
    play sound "audio/sfx/new_chapter.mp3" volume 0.5
    pause 0.45
    show chapter_num "Chapter [chapter]"
    pause 0.5
    show chapter_text "[chapter_name]"
    pause 4.0
    hide chapter_num
    hide chapter_text
    with dissolve
    $ DisableSkip.stop()
    return
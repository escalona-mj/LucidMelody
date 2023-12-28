##################################################################################################################
#                              CHARACTER INFO + RELATIONSHIP METER                                               #
##################################################################################################################
init python:
    class CharInfo:
        def __init__(self, char_name='', age='', description='', mainChr=False, points='', max_points='', pic=None):
            self.name = char_name
            self.age = age
            self.description = description
            self.mainChr = mainChr
            self.points_var = points
            self.max_points_var = max_points
            self.pic = pic

        #from the old LoveMeter
        @property
        def points(self):
            return getattr(store, self.points_var, 0)

        @property
        def max_points(self):
            return getattr(store, self.max_points_var, 0)

        #single method
        def __add__(self, value):
            self.show_points = f'{value:+}'
            self.new_points = min(max(self.points + value, 0), self.max_points)
            renpy.hide_screen('love_bar') # hide the screen so it resets the timer
            renpy.show_screen('love_bar', char=self) # then show with self as its arg. all you need is this object
            renpy.play("audio/sfx/love_ding.ogg", channel="notif")
            return self

        # this makes add/remove methods completely optional.
        def __sub__(self, value): self.__add__(-value)
        def add(self, value): self.__add__(value)
        def remove(self, value): self.__add__(-value)

        # we'll need this later
        def update(self):
            setattr(store, self.points_var, self.new_points)

    def update_journal(message):
        renpy.notify(message)
        renpy.play("audio/sfx/journal.ogg", channel="notif2")
        store.notify_journal = True

    def add_entry(entry):
        store.journal_entries.append(entry)
        update_journal("Entry added.")

    def remove_entry(entry):
        store.journal_entries.remove(entry)
        update_journal("Entry removed.")

    def next_page():
        store.first_page += 2
        store.second_page += 2
    
    def back_page():
        store.first_page -= 2
        store.second_page -= 2

screen love_bar(char): # char reference is all you need
    style_prefix 'love_bar'
    timer 0.1 action Function(char.update)
    timer 3.0 action Hide()

    frame at screen_appear:
        has vbox

        hbox:
            text char.name style 'love_bar_name'
            text '[char.show_points]' style 'love_bar_value':
                at value_appear()

        bar value AnimatedValue(char.points, char.max_points, delay=1.0)


style love_bar_frame is default:
    xalign 0.5
    yalign 0.1
    yanchor 0.5
    yoffset -25
    background None

style love_bar_text is default:
    font gui.game_menu_label_font
    color '#e61841'
    outlines [(5, "#ffffff", 2, 2)]

style love_bar_name is love_bar_text:
    yoffset 45
    xoffset 50
    text_align 0.0
    size 60
    
style love_bar_value is love_bar_text:
    yoffset 50
    xoffset 200

style love_bar_bar is default:
    xalign 0.5
    xmaximum 375
    ymaximum 90
    left_gutter 75
    right_gutter 23
    left_bar Frame("gui/bar/love_full.png")
    right_bar Frame("gui/bar/love_empty.png")

transform value_appear:
    alpha 0.0 yoffset 25
    easein 0.5 yoffset 0 alpha 1.0
    pause 2.5
    easein 0.5 yoffset -25 alpha 0.0

transform book_appear_pc:
    subpixel True
    on show:
        yoffset 500
        zoom 0.5 alpha 0.0
        easein .25 zoom 0.85 alpha 1.0 yoffset 0

transform book_appear_touch:
    subpixel True
    on show:
        yoffset 500
        zoom 0.5 alpha 0.0
        easein .25 zoom 1.0 alpha 1.0 yoffset 0

transform bookmark_side:
    rotate -5 zoom 0.35 yoffset -50 xoffset 50

transform page_flip:
    xzoom 0
    easein_back .5 xzoom 1

screen journal():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master"), Play("sfx2", "audio/sfx/journal_open.ogg")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master"), Play("sfx2", "audio/sfx/journal_close.ogg")

    dismiss action Return()

    add "gui/overlay/confirm.png":
        alpha 0.65

    for char in all_chars:
        if current_page == char.name:
            $ name = "Name: " + char.name
            $ description = "Description:\n" + char.description
            $ mainChr = char.mainChr
            $ points = char.points
            $ max_points = char.max_points
            $ pic = char.pic

            if char.mainChr:
                $ LoveMeter = False
            else:
                $ LoveMeter = True

    frame:
        modal True
        if renpy.variant("small"):
            at book_appear_touch
        else:
            at book_appear_pc

        background Frame("gui/journal/journal.png")
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 10
            
            #BOOKMARK SECTION
            frame:
                xsize 0
                ysize 0
                yoffset 40
                xoffset 55
                style_prefix "bookmark"
                vbox:
                    xalign 1.0
                    spacing 25
                    if isDhannica:
                        imagebutton auto "gui/journal/dhannica_bookmark_%s.png":
                            foreground Text("", style="bookmark_btn")
                            idle_foreground At("side dhannica", bookmark_side)
                            hover_foreground At("side dhannica", bookmark_side)
                            selected_foreground Text("{0}".format(Main), style="bookmark_btn")
                            action [SetVariable("current_page", MC.name)]
                            focus_mask True
                        if meetNick:
                            imagebutton auto "gui/journal/nick_bookmark_%s.png":
                                foreground Text("", style="bookmark_btn")
                                idle_foreground At("side nick", bookmark_side)
                                hover_foreground At("side nick", bookmark_side)
                                selected_foreground Text("{0}".format(mcNameboy), style="bookmark_btn")
                                action [SetVariable("current_page", Nick.name)]
                                focus_mask True
                        if meetAlec:
                            imagebutton auto "gui/journal/alec_bookmark_%s.png":
                                foreground Text("", style="bookmark_btn")
                                idle_foreground At("side alec", bookmark_side)
                                hover_foreground At("side alec", bookmark_side)
                                selected_foreground Text("{0}".format(a_name), style="bookmark_btn")
                                action [SetVariable("current_page", Alec.name)]
                                focus_mask True
                    
                    elif isNick:
                        imagebutton auto "gui/journal/nick_bookmark_%s.png":
                            foreground Text("", style="bookmark_btn")
                            selected_foreground Text("{0}".format(Main), style="bookmark_btn")
                            action [SetVariable("current_page", MC.name)]
                            focus_mask True
                        if meetDhannica:
                            imagebutton auto "gui/journal/dhannica_bookmark_%s.png":
                                foreground Text("", style="bookmark_btn")
                                selected_foreground Text("{0}".format(mcNamegirl), style="bookmark_btn")
                                action [SetVariable("current_page", Dhannica.name)]
                                focus_mask True
            #FIRST PAGE
            frame:
                at page_flip
                background None
                padding(80,30,30,90)
                vbox:
                    style_prefix "page"
                    viewport:
                        xsize 600
                        ysize 800
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        vbox:
                            if not current_page == "Journal":
                                text name
                                null height 10
                                text description
                            else:
                                if len(journal_entries) > 0:
                                    text "{0}".format(journal_entries[first_page - 1])

                    if current_page == "Journal":
                        if len(journal_entries) > 0:
                            text "[first_page]" color "#000":
                                xalign 0.5

            #SECOND PAGE
            frame:
                at page_flip
                background None
                padding(30,30,90,60)
                vbox:
                    style_prefix "page"
                    viewport:
                        xsize 600
                        ysize 800
                        draggable True
                        mousewheel True
                        scrollbars "vertical"
                        vbox:
                            if not current_page == "Journal":
                                add pic xalign 0.5 zoom 0.70 yalign 0.5 rotate 2
                                if LoveMeter == True:
                                    vbox:
                                        xalign 0.5
                                        text "Current points: [points]" style 'love_bar_text':
                                            size 40
                                            xoffset 55
                                            yoffset 40
                                        bar style "love_bar_bar":
                                            value points
                                            range max_points
                            else:
                                if first_page < len(journal_entries):
                                    text "{0}".format(journal_entries[second_page - 1])

                    if current_page == "Journal":
                        if first_page < len(journal_entries):
                            text "[second_page]" color "#000":
                                xalign 0.5
                                
            #JOURNAL BOOKMARK
            frame:
                xsize 0
                ysize 0
                yoffset 700
                xoffset -55
                style_prefix "dream_bookmark"
                hbox:
                    imagebutton auto "gui/journal/bookmark_%s.png":
                        foreground Text("", style="dream_bookmark_btn")
                        selected_foreground Text("Journal", style="dream_bookmark_btn")
                        action [SetVariable("current_page", "Journal")]
                        focus_mask True

    if current_page == "Journal":
        if (first_page >= 3) and (len(journal_entries) >= 3):
            imagebutton action Function(back_page) style_prefix "page":
                idle "gui/journal/prev_page.png"
                xalign 0.05
                yalign 0.5
            
        if second_page < len(journal_entries):
            imagebutton action Function(next_page) style_prefix "page":
                idle "gui/journal/next_page.png"
                xalign 0.95
                yalign 0.5

style page_text:
    color "#000"
    font gui.journal_font
    size 35

style page_image_button:
    activate_sound "audio/sfx/journal_page_flip.ogg"

style bookmark_image_button:
    activate_sound "audio/sfx/journal_page_flip.ogg"

style bookmark_btn:
    text_align 0.5
    xalign 0.5
    yalign 0.5
    font gui.name_text_font
    color "#fff"
    size 45
    outlines [(5, "#16161d", 0, 2)]

style page_vscrollbar:
    base_bar Frame("gui/scrollbar/vertical_journal_bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_journal_thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    unscrollable gui.unscrollable

style dream_bookmark_image_button is bookmark_image_button
style dream_bookmark_btn is bookmark_btn

image journal_dhannica = LayeredImageMask("dhannica",
    Transform(crop=(170, 0, 500, 600)),
    background="gui/journal/photo_bg.png",
    mask="gui/journal/photo_mask.png",
    foreground="gui/journal/photo_fg.png")

image journal_nick = LayeredImageMask("nick",
    Transform(crop=(170, -50, 500, 600)),
    background="gui/journal/photo_bg.png",
    mask="gui/journal/photo_mask.png",
    foreground="gui/journal/photo_fg.png")

image journal_alec = LayeredImageMask("alec",
    Transform(crop=(190, 0, 500, 600)),
    background="gui/journal/photo_bg.png",
    mask="gui/journal/photo_mask.png",
    foreground="gui/journal/photo_fg.png")
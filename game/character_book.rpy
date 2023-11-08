##################################################################################################################
#                              CHARACTER INFO + RELATIONSHIP METER                                               #
##################################################################################################################
init python:
    class CharInfo:
        def __init__(self, char_name, age, description, mainChr, points, max_points, pic=None):
            self.name = char_name
            self.age = age
            self.description = description
            self.mainChr = mainChr
            self.points_var = points
            self.max_points_var = max_points
            self.pic = pic

        #from the old LoveMeter
        @property
        def points(self): return getattr(store, self.points_var, 0)

        @property
        def max_points(self): return getattr(store, self.max_points_var, 0)

        #single method
        def __add__(self, value):
            self.show_points = f'{value:+}'
            self.new_points = min(max(self.points + value, 0), self.max_points)
            renpy.hide_screen('love_bar') # hide the screen so it resets the timer
            renpy.show_screen('love_bar', char=self) # then show with self as its arg. all you need is this object
            renpy.play("audio/sfx/love_ding.ogg", channel="sfx2")
            return self

        # this makes add/remove methods completely optional.
        def __sub__(self, value): self.__add__(-value)
        def add(self, value): self.__add__(value)
        def remove(self, value): self.__add__(-value)

        # we'll need this later
        def update(self):
            setattr(store, self.points_var, self.new_points)

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
    yalign 0.0
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
    pause 1.0
    easein 0.5 yoffset -25 alpha 0.0


transform book_appear:
    subpixel True
    on show:
        rotate 2
        zoom 0.95 alpha 0.0
        easein .25 zoom 1.0 alpha 1.0 rotate -2
    on hide:
        rotate -2
        easein .25 zoom 0.95 alpha 0.0 rotate 2

screen chr_book():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master"), Play("sfx2", "audio/sfx/chrBook_open.ogg")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master"), Play("sfx2", "audio/sfx/chrBook_close.ogg")
    dismiss action Return()

    for char in all_chars:
        if viewing == char.name:
            $ name = "Name: " + char.name
            $ age = "Age: " + char.age
            $ description = "Description:\n\n" + char.description
            $ mainChr = char.mainChr
            $ points = char.points
            $ max_points = char.max_points
            $ pic = char.pic

            if char.mainChr:
                $ LoveMeter = False
            else:
                $ LoveMeter = True

    frame:
        at book_appear
        modal True
        background Frame("gui/chrBook/chrBook.png")
        xalign 0.5
        yalign 0.5
        hbox:
            spacing 10
            
            frame:
                xsize 0
                ysize 0
                xoffset -150
                vbox:
                    spacing 75
                    if current_route == "dhannica" or current_route == "alec":
                        textbutton "[Main]" action [SetVariable("viewing", Dhannica.name)]
                        if meetNick:
                            textbutton "[mcNameboy]" action [SetVariable("viewing", Nick.name)]
                    
                    elif current_route == "nick":
                        textbutton "[Main]" action [SetVariable("viewing", Nick.name)]
                        if meetDhannica:
                            textbutton "[mcNamegirl]" action [SetVariable("viewing", Dhannica.name)]
                    
                    if meetAlec:
                        textbutton "[a_name]" action [SetVariable("viewing", Alec.name)]

            frame:
                background None
                padding(90,30,30,30)
                viewport:
                    xsize 600
                    ysize 800
                    vbox:
                        if LoveMeter == True:
                            hbox:
                                vbox:
                                    spacing 25
                                    text "Current points:" style 'love_bar_text':
                                        size 40
                                        xoffset 55
                                        yoffset 40
                                    bar style "love_bar_bar":
                                        value points
                                        range max_points
                                text "[points]" style 'love_bar_text':
                                    yalign 0.5
                                    size 60
                        style_prefix "page"
                        text name
                        text age
                        text description

            frame:
                background None
                padding(30,30,90,60)
                viewport:
                    xsize 600
                    ysize 800
                    xinitial 0.5
                    vbox:
                        add pic xalign 0.5

style page_text:
    color "#000"
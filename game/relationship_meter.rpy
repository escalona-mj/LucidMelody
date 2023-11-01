default nick_likePoints = 0
default nick_likePointsMax = 100

default alec_likePoints = 0
default alec_likePointsMax = 100

#######################
# RELATIONSHIP SYSTEM #
#######################
init python:
    class LoveMeter:
        def __init__(self, char_name, points, max_points):
            self.name = char_name
            self.points_var = points
            self.max_points_var = max_points

        @property
        def points(self): return getattr(store, self.points_var, 0)

        @property
        def max_points(self): return getattr(store, self.max_points_var, 0)

        # single method
        def __add__(self, value):
            self.show_points = f'{value:+}'
            self.new_points = min(max(self.points + value, 0), self.max_points)
            renpy.hide_screen('love_bar') # hide the screen so it resets the timer
            renpy.show_screen('love_bar', char=self) # then show with self as its arg. all you need is this object
            renpy.play("audio/sfx/love_ding.mp3", channel="sfx2")
            return self

        # this makes add/remove methods completely optional.
        def __sub__(self, value): self.__add__(-value)
        def add(self, value): self.__add__(value)
        def remove(self, value): self.__add__(-value)

        # we'll need this later
        def update(self):
            setattr(store, self.points_var, self.new_points)
            
define alecLoveMeter = LoveMeter("[mcNameboy]", points="alec_likePoints", max_points="alec_likePointsMax")
define nickLoveMeter = LoveMeter("[n_name]", points="nick_likePoints", max_points="nick_likePointsMax")

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

##########################
# NEW ACHIEVEMENT SYSTEM #
##########################
init -50 python:
    import datetime, time

    TAG_ALPHABET = "abcdefghijklmnopqrstuvwxyz"
    def get_random_screen_tag(k=4): #generate a random k-letter word out of alphabet letters

        # Shuffle the list and pop k items from the front
        alphabet = list(store.TAG_ALPHABET)
        renpy.random.shuffle(alphabet)
        return ''.join(alphabet)
    
    class Achievement():

        # list all achievements
        all_achievements = []
        achievement_dict = dict()
        def __init__(self, name, id=None, description=None, unlocked_image=None, locked_image=None):

            self._name = name
            self.id = id
            self._description = description
            self.unlocked_image = unlocked_image or None #alternate way if the achievement does not need to have an image
            self.locked_image = locked_image or "locked_achievement" #failsafe if a specified locked image is not found

            # Add to list of all achievements
            self.all_achievements.append(self)
            # Add to the dictionary for a quick lookup
            self.achievement_dict[self.id] = self
        
        @property
        def ach_img(self):
            #returns the image based on its status whether it is unlocked or locked

            if self.has():
                return self.unlocked_image
            else:
                return self.locked_image

        @property
        def name(self):
            #returns the name of the achievement

            if self.has():
                return self._name
            else:
                return "Achievement Locked."

        @property
        def description(self):
            #returns the description of the achievement
            
            if self.has():
                return self._description
            else:
                return "???"

        def clear(self):
            #remove the achievement from the persistent file
            return achievement.clear(self.id)

        def grant(self):
            #grants the player the achievement

            has_achievement = self.has()
            x = achievement.grant(self.id)

            #show a toast if this is the first time
            if not has_achievement:
                self.achievement_popup()
                renpy.play("audio/sfx/notify.mp3", channel="sfx2")
                config.skipping = False

            #double check achievement sync to avoid syncing issues
            achievement.sync()
            return x

        def has(self):
            #checks if player has achieved this achievement
            return achievement.has(self.id)

        def achievement_popup(self):
            #show an achievement notification to indicate a granted achievement

            if renpy.is_init_phase(): #this is init time; we don't show a popup screen
                return
            elif not self.has(): # if player doesn't have this achievement yet, no popup
                return

            #if all above is True, show the achievement toast in the onscreen_achievement dictionary every granted achievement
            for i in range(6): #range is how many times the achievement toast will display on the y axis
                if store.onscreen_achievements.get(i, None) is None:
                    store.onscreen_achievements[i] = True
                    break
            # Generate a random tag for this screen
            tag = get_random_screen_tag(6)
            renpy.show_screen('achievement_toast', a=self, tag=tag, num=i, _tag=tag)

        def Toggle(self):
            #a toggle to easily test the status of an achievement
            return [SelectedIf(self.has()),
                If(self.has(),
                    Function(self.clear),
                    Function(self.grant))]
        
        def Grant(): #grant an achievement for buttons
            return Function(self.grant)

        @classmethod
        def num_earned(self): #a class property which returns the number of unlocked achievements
            return len([a for a in self.all_achievements if a.has()])

        @classmethod
        def num_total(self): #a class property which returns the total number of achievements
            return len(self.all_achievements)

## Tracks the number of achievement toasts, especially when multiple achievements are earned at once
default onscreen_achievements = dict()

screen finish_animating_achievement(num):
    timer 1.0:
        action [SetDict(onscreen_achievements, num, None), Hide()]

image locked_achievement = "gui/achievements/icons/locked.png"

################
# ACHIEVEMENTS #
################

define dream = Achievement(
    name=_("Lucid Melody"),
    id="dream",
    description=_("Complete dreaming."),
    unlocked_image="gui/achievements/icons/start.png",
    locked_image="locked_achievement",
)

define welcome = Achievement(
    name=_("Welcome to STI!"),
    id="welcome",
    description=_("Get to the school."),
    unlocked_image="gui/achievements/icons/start.png",
    locked_image="locked_achievement",
)

define mainMenu_ach = Achievement(
    name=_("Scenery Lover"),
    id="mainMenu_ach",
    description=_("Stay on the main menu screen for quite some time."),
    unlocked_image="gui/achievements/icons/start.png",
    locked_image="locked_achievement",
)

define independent = Achievement(
    name=_("Independent"),
    id="independent",
    description=_("Get through the game without dating either of the love interests."),
    unlocked_image="gui/achievements/icons/start.png",
    locked_image="locked_achievement",
)

define girlArc = Achievement(
    name=_("Dhannica's Tribute"),
    id="girlArc",
    description=_("Finish the game during her route."),
    unlocked_image="gui/achievements/icons/start.png",
    locked_image="locked_achievement",
)

define boyArc = Achievement(
    name=_("Alec's Tribute"),
    id="boyArc",
    description=_("Finish the game during his route."),
    unlocked_image="gui/achievements/icons/start.png",
    locked_image="locked_achievement",
)

define nickArc = Achievement(
    name=_("Nick's Intervention"),
    id="nickArc",
    description=_("Finish the game by choosing Nick over Alec during Dhannica's route."),
    unlocked_image="gui/achievements/icons/start.png",
    locked_image="locked_achievement",
)

#####################
# ACHIEVEMENT TOAST #
#####################

transform achievement_transform():
    on show:
        xpos 1.0 xanchor 0.0
        easein .5 xpos 1.0 xanchor 1.0
    on hide, replaced:
        xpos 1.0 xanchor 1.0 yoffset 0 alpha 1.0
        easein 0.5 yoffset -100 alpha 0.0

screen achievement_toast(a, tag, num):

    zorder 500
    #the offset that achievement should take vertically each granted achievement as to not overlap one another
    #num gets increased each granted achievement
    default achievement_yoffset = num*130

    style_prefix 'achievement_toast'

    frame:
        at achievement_transform
        yoffset achievement_yoffset

        hbox:
            spacing 15
            vbox:
                yalign 0.5
                add a.unlocked_image fit "contain" ysize 100
            vbox:
                yalign 0.5
                label a.name
                text a.description

    #hide the screen after 5 seconds
    timer 5.0 action [Hide("achievement_toast"), Show('finish_animating_achievement', num=num, _tag=tag+"1")]

style achievement_toast_frame:
    background Frame("gui/achievements/achievement_toast.png", gui.achievement_frame_borders, tile=gui.frame_tile)
    padding (20, 20, 50, 20)

style achievement_toast_label_text:
    is achievements_label_text
    color '#fff'
    outlines [(0, "#000", 0, 0)]
    

style achievement_toast_text:
    is achievements_text
    color '#fff'

#######################
# ACHIEVEMENT GALLERY #
#######################

screen achievements():
    tag menu

    use game_menu(__("Achievements: ") + "{earned}/{total}".format(earned=Achievement.num_earned(), total=Achievement.num_total()), scroll="viewport"):

        style_prefix "achievements"
        vbox:
            spacing 5
            for a in Achievement.all_achievements:
                button:
                    if a.has():
                        background Frame("gui/achievements/unlocked_achievement_frame.png", gui.achievement_frame_borders, tile=gui.frame_tile)
                    else:
                        pass
                    if config.developer:
                        action a.Toggle()
                    hbox:
                        yalign 0.5
                        spacing 30
                        add a.ach_img yalign 0.5 fit "contain" ysize 125

                        vbox:
                            yalign 0.5
                            if not a.has():
                                style_prefix "locked"
                                label a.name
                                text a.description
                            else:
                                label a.name
                                text a.description
                # null height 10
        
style achievements_vbox is vbox

style achievements_label_text: #unlocked achievement name
    yalign 0.5
    outlines [(5, "#6667ab", 2, 2)]
    color '#fff'

style achievements_text: #unlocked achievement description
    yalign 0.5
    color gui.accent_color
    size 30

style locked_label_text: #locked achievement name
    yalign 0.5
    color u'#b5b5b5'

style locked_text: #locked description
    yalign 0.5
    color u'#b5b5b5'
    size 30

style achievements_button:
    background Frame("gui/achievements/achievement_frame.png", gui.achievement_frame_borders, tile=gui.frame_tile)
    padding (20, 20, 20, 20)
    xfill True

define gui.achievement_frame_borders = Borders(115, 25, 25, 25)
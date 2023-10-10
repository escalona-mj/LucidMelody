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
            self.unlocked_image = unlocked_image or None #failsafe if the image isnt found
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
            elif not self.has(): # if player doesn't yet have this achievement, no popup
                return

            #if all above is True, show the achievement toast in the onscreen_achievement dictionary every granted achievement
            for i in range(6): #range is how many times the achievement toast will display on the y axis
                if store.onscreen_achievements.get(i, None) is None:
                    store.onscreen_achievements[i] = True
                    break
            # Generate a random tag for this screen
            tag = get_random_screen_tag(6)
            renpy.show_screen('achievement_popup', a=self, tag=tag, num=i, _tag=tag)

        def Toggle(self):
            #a toggle to easily test the status of an achievement
            return [SelectedIf(self.has()),
                If(self.has(),
                    Function(self.clear),
                    Function(self.grant))]
        
        def Grant(): #an action to easily achieve a particular achievement for buttons
            return Function(self.grant)

        @classmethod
        def reset(self): #a class method which resets all achievements and clears all the current progress
            for achievement in self.all_achievements:
                achievement.clear()

        @classmethod
        def num_earned(self):#a class property which returns the number of unlocked achievements
            return len([a for a in self.all_achievements if a.has()])

        @classmethod
        def num_total(self):#a class property which returns the total number of achievements
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

define welcome = Achievement(
    name=_("Welcome to STI!"),
    id="welcome",
    description=_("Start a new game for the very first time."),
    unlocked_image="gui/achievements/icons/start.png",
    locked_image="locked_achievement",
)

define achievement2 = Achievement(
    name=_("2nd Achievement"),
    id="achievement2",
    description=_("Testing for granting multiple achievements."),
    unlocked_image="gui/achievements/icons/end.png",
    locked_image="locked_achievement",
)


#####################
# ACHIEVEMENT TOAST #
#####################

screen achievement_popup(a, tag, num):

    zorder 500
    #the offset that achievement should take vertically each granted achievement as to not overlap one another
    #num gets increased each granted achievement
    default achievement_yoffset = num*185

    style_prefix 'achievement_toast'

    frame:
        at achievement_popout()
        yoffset achievement_yoffset
        has hbox
        yalign 0.5
        add a.unlocked_image fit "contain" ysize 150
        vbox:
            yalign 0.5
            label a.name style "achievements_label"
            text a.description style "achievements_text"

    #hide the screen after 5 seconds
    timer 5.0 action [Hide("achievement_popup"), Show('finish_animating_achievement', num=num, _tag=tag+"1")]

transform achievement_popout():
    on show:
        xpos 0.0 xanchor 1.0
        easein_back 1.0 xpos 0.0 xanchor 0.0
    on hide, replaced:
        easeout_back 1.0 xpos 0.0 xanchor 1.0

style achievement_toast_frame:
    background Frame("gui/achievements/achievement_toast.png", gui.achievement_frame_borders, tile=gui.frame_tile)
    padding (20, 20, 50, 20)

screen achievements():
    tag menu
    use bg
    add "gui/overlay/confirm.png":
        alpha 0.75
    add "gui/phone/overlay/game_menu.png"

    use game_menu(__("Achievements: ") + "{earned}/{total}".format(earned=Achievement.num_earned(), total=Achievement.num_total()), scroll="viewport"):

        style_prefix "achievements"
        vbox:
            spacing 5
            for a in Achievement.all_achievements:
                button:
                    if config.developer:
                        action a.Toggle()
                    hbox:
                        yalign 0.5
                        spacing 15
                        add a.ach_img yalign 0.5

                        vbox:
                            yalign 0.5
                            label a.name
                            text a.description
                null height 10
            # text "You have unlocked [persistent.unlocked_achievement] out of [locked_achievement] achievements.":
            #     xalign 0.5
            #     size 45
        
style achievements_vbox is vbox
style achievements_frame is empty

style achievements_label_text: #unlocked achievement name
    yalign 0.5
    color u'#fff'

style achievements_text: #unlocked achievement description
    yalign 0.5
    color u'#fff'
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
label after_load:
    $ _side_image_attributes = None
    if persistent.playername == '':
        scene black
        stop music
        stop sound
        stop sfx2
        stop sfx3
        stop ambient
        stop ambient2
        $ _history_list = []
        $ quick_menu = False
        $ renpy.block_rollback()
        "The game has detected an external save file.\nPlease start a new game before loading or delete this save file."
        call screen returntoMain
    #remove any ghost side images
    if not persistent.seen_controls:
        play notif phone_notif
        call screen controls_modal
        $ persistent.seen_controls = True
    # play notif phone_notif
    # call screen dialog("Journal updates are tied to their specific save files. Which means future versions with new descriptions will not update in old save files.\n\nWhile it doesn't change the overall structure of the story, it'll have some inconsistencies as you progress. Hence why you are provided the option to delete save files.\n\n{b}Please be aware of that!{/b}", ok_action=Return())

screen returntoMain():
    timer 0.1 action MainMenu(confirm=False)
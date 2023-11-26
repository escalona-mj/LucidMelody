label after_load:
    if not persistent.seen_controls:
        play notif phone_notif
        call screen controls_modal
        $ persistent.seen_controls = True
    # play notif phone_notif
    # call screen dialog("Journal updates are tied to their specific save files. Which means future versions with new descriptions will not update in old save files.\n\nWhile it doesn't change the overall structure of the story, it'll have some inconsistencies as you progress. Hence why you are provided the option to delete save files.\n\n{b}Please be aware of that!{/b}", ok_action=Return())
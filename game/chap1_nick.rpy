label chap1_nick:
    call chapter_transition

    #nick route, so he takes the MC role
    $ MC = CharInfo(
    char_name="[Main]",
    age="[nick_age]",
    description="[nick_description]",
    mainChr=True,
    points="nick_likePoints",
    max_points="nick_likePointsMax",
    pic="journal_nick")

    $ all_chars = [MC, Dhannica, Nick, Alec]
    $ current_page = "[Main]" #set the default screen when opening the character book for the first time

    $ dhannica = DynamicCharacter('mcNamegirl', kind=speak, color='#ff9b9b') #remove side image

    $ mcNamegirl = "???"

    "..."
    play sound "audio/sfx/phone_notif.ogg"
    call screen dialog(message="Nick's route is not available at the moment.", ok_action=Return())
    return
label chap1_nick:
    call chapter_transition

    #nick route, so he takes the MC role
    $ MC = CharInfo(
    char_name="[Main]",
    description="[nick_description]",
    mainChr=True,
    pic="journal_nick")

    $ all_chars = [MC, Dhannica, Nick, Alec]
    $ current_page = "[Main]" #set the default screen when opening the character book for the first time

    $ mcNamegirl = "???"

    "..."
    play sound phone_notif
    call screen dialog(message="Nick's route is not available at the moment.", ok_btn="OK", ok_action=Return())
    return
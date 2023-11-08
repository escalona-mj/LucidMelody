label chap1_nick:
    call chapter_transition
    $ dhannica = DynamicCharacter('mcNamegirl', kind=speak, color='#ff9b9b') #remove side image
    play sound "audio/sfx/phone_notif.ogg"
    call screen dialog(message="Nick's route is not available at the moment.", ok_action=Return())
    return
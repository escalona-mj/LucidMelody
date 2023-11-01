label chap1_alec:
    call chapter_transition
    play sound "audio/sfx/phone_notif.ogg"
    call screen dialog(message="Alec's route is not available at the moment.", ok_action=Return())
    return
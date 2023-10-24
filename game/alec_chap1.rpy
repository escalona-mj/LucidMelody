label alec_chap1:
    call chapter_transition
    play sound "audio/sfx/phone_notif.ogg"
    call screen dialog(message="Alec's route is not available at the moment.", ok_action=Rollback())
    return
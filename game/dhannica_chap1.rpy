default beLate = False
default usePhone = False
default eatBreakfast = False
default clinic = False

default alec_likePoints = 0

label dhannica_chap1:
    call chapter_transition
    if config.developer == False:
        $ renpy.block_rollback()
    pause 2.0
    scene bg stage with dissolve
    camera:
        subpixel True
        truecenter
        ease 0.1 zoom 1.05
        choice:
            easeout_bounce 1.0 yalign 0.55
            easeout_bounce 1.0 yalign 0.45
            repeat
    play sound cheer fadein 3.0 volume 0.2 loop
    
    "The audience roars."
    "You find yourself in an opulent concert hall, with golden chandeliers casting a warm glow above you."
    "The crowd's anticipation is palpable."
    "There lies a singer on stage, his face obscured by a quirky lunchbox bag, decided to hide his face from the world and remain unknown."
    "His mystery has always captivated you."
    "The atmosphere is almost too electric, with fans waving glow sticks in rhythm."
    "You are in the front of the stage, shouting your deepest exaggeration of support to the singer."
    "So happy that tears started to fall from your eyes."
    dhannica_i "I never thought I got to be on front stage..."
    dhannica_i "Now I get to observe him closer!"
    dhannica_i "This is all making me teary...!"
    d_singer "{size=+50}YOU THERE!{/size}{fast}" with vpunch
    "The lead singer shouted, while looking at your teary soulful eyes."
    dhannica "Wh-wha? Me?"
    d_singer "Yes you! You'd been crying there for so long."
    d_singer "Seems like you need to get a hold of yourself together!"
    dhannica "H-huh?"
    "You became so ecstatic and shocked at what had occured."
    "Hesitant, he held out his hand inviting you to accompany him for a song."
    d_singer "Come on, sing with me on stage."
    "Hurriedly, fans cheering around you helped you get up on stage."
    d_singer "Whadd'ya wanna sing?"
    dhannica "Oh uhm... Maybe..."
    "You whisper to him discreetly the song."
    d_singer "Ah, I see. Alright, get yourself ready, as this crowd's about to get hectic!"
    "Both of you started singing, and the crowd goes even wilder as headlights were spotted to both of you."
    "But you don't care of that. Your eyes only focused on him as you sang, trying hard not to cry as you look at his masked face."
    "But the harsh light gleamed against to you so strongly that you caught a glimpse of his eyes."
    "They were green..."
    "You were lost in the song, in his eyes, having caught a milisecond of his identity."
    "You wonder and think, will this last forever?"
    play sfx2 alarmloop volume 0.25 loop
    "Maybe..."
    play sfx2 alarmloop volume 0.5 loop
    "Maybe.."
    play sfx2 alarmloop volume 0.75 loop
    "{cps=15}Mayb{nw}"
    stop sfx2
    $ config.skipping = False
    if not config.developer:
        $ renpy.block_rollback()
    window hide(None)
    camera
    play sound alarm
    scene black
    pause 4.0
    window auto
    menu:
        "Get up and turn off the alarm":
            scene bg dhannica room with eye_open
            dhannica_i "Ugh... That was such a dream."
            dhannica_i "Why did I set this alarm so early?"
            play sound stomachgrowl
            window hide(None)
            pause 1.25
            window auto
            dhannica_i "Oh shoot, I forgot! I never really had dinner last night."
            play sound phone_notif
            dhannica_i "Huh?"
            menu:
                "Check my phone":
                    $ usePhone = True
                    $ beLate = True
                    "You extended your hand to grab your phone."
                    dhannica_i "Eh, it's still early."
                    dhannica_i "I'll go watch something first to pass the time."
                    scene bg dhannica room with long_dissolve
                    dhannica_i "Wow, this short video is really funny~"
                    pause 1.5
                    dhannica_i "Lol, cute kitty."
                    pause 1.5
                    dhannica_i "Yeah, that's how you do it!"
                    pause 1.5
                    "It didn't take long for you to finally remember something."

                "Go eat breakfast":
                    $ eatBreakfast = True
                    dhannica_i "Nah, I think I've had enough with social media."
                    "Since it was still early, you made your bed before leaving your bedroom. Once you were done, you changed into your uniform and head downstairs."

        "Snooze for another 5 minutes":
            $ beLate = True
            dhannica_i "Nooo, I need to remember..."
            dhannica_i "I don't wanna wake up..."
            "You try to remember the dream the best you could."
            "Attempting to replay the entire thing isn't working, it's only making it worse."
            "The more you try to remember it... The more you forget..."
            "Like it's trying to run away from you." 
            "And the feeling of having found something so surreal, and slowly losing it."
            "Slowly forgetting it..."
            "Till there's nothing to remember."
            "Just the empty feeling of loosing something you never had."
            play sound alarm fadein 3.0 loop volume 0.6
            window hide(None)
            pause 3.0
            scene bg dhannica room with eye_open
            window auto
            dhannica_i "Urk..."
            dhannica_i "Alright, alright! I'm awake!"
            "Feeling somewhat disoriented, you extended your hand to grab your phone and checked the time."
            stop sound fadeout 0.2

    if beLate:
        dhannica "IT'S 7:55?!" with vpunch
        dhannica "SHOOT!"
        if usePhone:
            "You jumped out of bed after spending a good 45 minutes scrolling on your phone and head downstairs."
        else:
            "You jumped out of bed, changed into your uniform, rushed out the door and head downstairs."

    scene black with eye_close
    play sound thump
    pause 0.5
    scene bg living room with eye_open
    dhannica "Ow!" with vpunch

    if beLate or usePhone:
        "Out of the rush, you accidentally bumped your toe on the baluster."
        dhannica "Arrrrgh....!"
        "You hold your poor pinky toe, checking if you've lost your toenail to the stair rail."
        dhannica_i "Thank God it's still intact."
        dhannica_i "It looks swollen though, and it hurts like hell..."
        "A mental reminder went off in your mind that you realized you're late."
        "You rushed down the stairs limping on your other foot for support and immediately chugged the glass of milk overlooking the toast and eggs your mother had prepared for you."
        girlMom "Honey, aren't you going to eat your breakfast?"
        dhannica "I'm late mom, I have to go!"
        "As soon as you're off, your mother stepped towards you and noticed your groggy appearance."
        girlMom "Why are you limping? What's wrong with your foot?"
        dhannica "I stubbed my toe but it's fine, it'll go away in a few minutes."
        girlMom "I don't think you should go to school today, that might get worse if you force yourself to school."
        dhannica "Too late mom."
        girlMom "At least bring an ice pack!"
        dhannica "I'm going, bye~"
    elif eatBreakfast:
        "You accidentally bumped your toe on the baluster."
        dhannica "Arrrrgh...this sucks, what the hell."
        dhannica_i "Why did it have to be on the first day of school?"
        dhannica_i "This smells like bad luck to me."
        dhannica "This day just started in a bad note. Let's hope it doesn't get worse for the rest of the day."
        "You came down the stairs limping on your one leg, while checking your phone for the notification that had rung a few moments ago."
        "Suddenly, your mother swiftly came through the scene and noticed your groggy appearance."
        girlMom "What happened hon?!"
        dhannica "I'm fine mom, I just stubbed my toe on the way down the stairs. I'm fine."
        girlMom "You don't seem fine. I don't think you'd have a pretty good day at school limping like that."
        dhannica "It doesn't hurt that much."
        dhannica_i "It hurts a lot~"
        dhannica "I just stubbed my toe, it's not like I dislocated it. It's gonna be fine after a few minutes."
        girlMom "You sure? I can send your teacher a note."
        dhannica "I'd rather go limping to school than be the weird kid who misses the first day, and ends up having no friends for the rest of the school year."
        girlMom "Well, if you say so. Just make sure not to overexert yourself. We don't wanna spend money to the doctors now, do we?"
        dhannica "Yes mom, I won't~"
        dhannica_i "My foot still hurts..."
    
    "You rushed outside."
    scene black with eye_close
    play sound doorclose
    pause 0.5
    scene bg highway with eye_open
    if beLate:
        "Running frantically on a Monday morning with nothing to eat and an injured toe can surely do something to you."
        "You felt weak and drained, when you've barely even started the day."
        dhannica_i "Hopefully the milk is enough to heal my toe..."
        "You saw the bus drive right pass you while you're barely catching up because of your current situation."
        dhannica_i "Oh crap!"
        "You tried to keep up with the bus as much as you could."
        "You started to look like a zombie from an apocalypse movie, just limping as fast to get there in time."
        "As the bus took its momentary halt at the bus stop, tons of people were also waiting to get on."
        "People who were trying to get out of the bus were even struggling to get out because the people who want to get in are obstructing their path."
        "Which meant more time for you to be able to '{i}limp{/i}' your way to the bus stop."
        dhannica_i "Almost there...!"
        "You're quite confident that you would get there in time, despite the fact that you look like an absolute ninny."
        "But you started to notice the bus was reaching its capacity, and people were getting fewer by the second."
        "You started to feel left out."
        dhannica_i "Wait, please!"
        "You had to do something..."
        menu:
            dhannica_i "Should I just run for it?"
            "Yes":
                "#block of code to run"
            "No":
                "#block of code to run"
            
    else:
        "The air around you was chilly, and the birds were all up and singing."
        "Not sure what the time was, you checked your phone. You just needed to make sure you had time before the class started."
        if beLate:
            dhannica_i "Dang it, I don't have enough time if I strut around. And as if this toe would get any better. I should just run and endure the pain."
            dhannica_i "And hopefully I can make it before the class starts."
            jump school
        else:
            dhannica_i "Guess I should hurry up."
            dhannica_i "As if this stupid toe would make it easier for me."
            jump school
    
    label school:
        scene bg school with eye_scene
        $ welcome.grant()
        "You finally reached the school, walking through the gates limping on your other foot."
        dhannica_i "I look like a loser. That's just great."
        dhannica_i "Is this how people are gonna remember me...? The limping kid on the first day of school."
        "You gaze before you a school, with an interesting color choice that seem be used redundantly everywhere."
        "..."
        "It didn't take long for you to finally realize what you're here for."
        dhannica "Oh right, my class schedule."
        "You rummaged through your bag, only to find out your outer pocket was open and your class schedule had fallen out."
        dhannica_i "This day just gets better and better."
        "Sarcasm was the only thing that could sugarcoat this situation."
        "You start to trace back your previous steps, carefully searching for your schedule, with your eyes glued to the ground."
        "Suddenly...a hand appeared in your field of vision, holding a piece of paper."
        "You read, '{i}Purposive Communication - 7:15 - 8-15 am{/i}'."
        "It was your schedule."
        show alec at appear_center
        "You looked at his hand and followed the trail of grungy accessories, to his chain necklace up to his green eyes."
        "You don't know what you felt, but you felt something. Maybe gratitude?"
        "That you wouldn't have to pay an extra 100 to get another copy of your schedule."
        dhannica "Uhm...thank you... for the, uhm...this."
        $ alec_likePoints += 3
        alec "No biggie."
        alec "I noticed this on the ground then looked ahead and saw your bag was open, so I had to hand it to you."
        alec "It seems that we're in the same class. Nice to meet you classmate."
        "He stretches out his hand for a handshake."
        "In which, you relunctantly returned the offer."
        alec "By the way, are you okay? You don't seem to be walking right."
        dhannica "Oh...yeah haha, I stubbed my toe this morning. And well, I thought it was gonna be okay after a few minutes, but I guess that's still yet to come."
        alec "Would you like me to accompany you to the nurse's office?"

        menu:
            "Accept":
                $ alec_likePoints += 2
                $ clinic = True
                dhannica "I mean, sure? Classes are about to start though. We'll be late if we did."

            "Deny":
                dhannica "You dont have to, I mean I wouldn't want to be a bother."
                alec "Nonsense, friends don't bother me."
                dhannica_i "What~"
                alec "We're friends, right?"
                dhannica "I guess...?"
                dhannica_i "I've made a friend~"
                dhannica "But we'll be late if we go now."
            
        alec "I guess so. How about after the first subject? We have 30 mins vacant. I'm sure that's enough time for the nurse to patch you up."

        if clinic:
            dhannica "Thanks, but you really don't have to do this."
            alec "And leave my first friend to an injury? I don't think so."
            dhannica_i "I've made a friend~"

        dhannica "I mean if you insist, how dare would I refuse hahaha."
        alec "Let's go, we'll be late for first sub."
        "Alec offers his hand for you to hold unto as you both walk to your classroom."
        jump classroom
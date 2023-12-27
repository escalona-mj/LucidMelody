label chap1_dhannica:
    call chapter_transition

    #dhannica route, so she takes the MC role
    $ MC = CharInfo(
    char_name="[Main]",
    description="[dhannica_description]",
    mainChr=True,
    pic="journal_dhannica")

    $ all_chars = [MC, Dhannica, Nick, Alec]
    $ current_page = "[Main]" #set the default screen when opening the character book for the first time

    $ a_name = "???"
    $ mcNameboy = "???"

    if not config.developer:
        $ renpy.block_rollback() #prevent from going back to mc selection screen
        
    label dream1:
        $ DreamScene.start()    
        pause 2.0
        scene bg stage with scenefade
        
        play ambient cheer fadein 3.0 volume 0.2
        
        "The audience roars."
        "A palpable blend of excitement and anticipation vibrates through the crowd."
        "You find yourself in an opulent concert hall, with golden spotlights casting a warm glow above you."
        "Thousands of fans, a mosaic of diverse faces and emotions, are gathered, their eyes alight with the fervor of shared passion."
        show bg stage:
            truecenter
            ease 1.0 zoom 1.4
        show dust_particle onlayer dream behind textbox_dream
        show dust_particle_blur onlayer dream behind textbox_dream
        "The crowd's anticipation is palpable."
        show dream_cg_scene1:
            offscreenright
            ease 1.0 xalign 0.5
        "There lies a singer on stage, his face obscured by a quirky lunchbox bag, hidden from the world."
        "His mystery has always captivated you."
        scene dream_cg_scene2:
            zoom 2.2 yoffset 125
            block:
                xoffset 0
                ease 5.0 xoffset -100
                ease 5.0 xoffset 0
                repeat
        with dissolve
        "The atmosphere is charged with an electric buzz, with fans waving their light sticks in rhythm."
        "The light sticks wave, dip, and swirl, an orchestrated chaos of color, creating patterns and waves that ebb and flow with the melody."
        "In some moments, they form a unified field of color, a single, massive wave of light that rolls across the audience, following the performance of the band."
        show dream_cg_scene2:
            ease 1.0 zoom 1.0 xoffset 0
        with None
        show dream_cg_scene2_light at pulse with dissolve
        "Being close to the front of the stage, you shout your deepest exaggeration of support to the band that tears started to fall from your eyes."
        dhannica_i "I never thought I got to be on front stage..."
        dhannica_i "Now I get to observe him closer!"
        dhannica_i "This is all making me teary...!"
        show dream_cg_scene2_singer:
            xpos 1.0 xanchor 0.0
            easein 0.25 xpos 1.0 xanchor 1.0
        d_singer "{sc}{size=+50}YOU THERE!{/size}{/sc}{fast}" with vpunch
        "The singer shouted, while looking at your teary soulful eyes."
        show dream_cg_scene2_dhannica:
            xpos 0.0 xanchor 1.0
            easein 0.25 xpos 0.0 xanchor 0.0
        dhannica "Wh-wha? Me?"
        d_singer "Yes you! You've been crying for quite a while there."
        d_singer "Seems like you need to get a hold of yourself together!"
        dhannica "H-huh?"
        "You became so ecstatic and shocked at what had occured."
        dhannica_i "Oh gosh... He called me out...!"
        dhannica_i "W-wait! I'm still trying to process what just happened!"
        scene black with eye_close
        "You close your eyes and pinched yourself if all of this is real."
        "*pinch*"
        dhannica_i "Ow!" with vpunch
        camera at dizzy
        scene dream_cg_scene3
        show dream_cg_scene3_light
        with eye_open
        dhannica_i "I'm not dreaming! I-It's real!"
        show dream_cg_scene3_hand behind dream_cg_scene3_light:
            xalign 0.5
            ypos 0.0 yanchor 1.0
            ease 1.5 ypos 0.0 yanchor 0.0
        "Suddenly, he held out his hand in front of you."
        dhannica_i "H-huh?"
        d_singer "Let's get you up here."
        dhannica "W-where?"
        d_singer "On the stage!"
        "Hurriedly, fans cheering around you helped you get up on stage."
        camera at reset_dizzy
        scene dream_cg_scene4 with eye_scene
        show dream_cg_scene4_dhannica:
            yalign 0.25
            xpos 0.0 xanchor 1.0
            ease 1.5 xpos 0.0 xanchor -0.25
        show dream_cg_scene4_light at pulse
        show dream_cg_scene4_singer:
            yalign 0.5
            xpos 1.0 xanchor 0.0
            ease 1.5 xpos 1.0 xanchor 1.0
        d_singer "You know, you're pretty lucky."
        d_singer "What's your name?"
        dhannica "O-oh, it's [Main]."
        show dream_cg_scene4_dhannica:
            ease .25 yalign 0.5
        d_singer "{sc}{size=+20}ALRIGHT, LET'S GIVE AN APPLAUSE TO [Main!u]!{/size}{/sc}" with vpunch
        "The crowd goes wilder."
        dhannica_i "Ow! That was pretty loud."
        dhannica_i "But quite exhilirating!"
        d_singer "I want you to accompany me for a song of your choice!"
        dhannica "R-really?"
        d_singer "Yeah!"
        d_singer "Whadd'ya wanna sing?"
        dhannica "Oh uhm... Maybe..."
        scene black with eye_close
        "You whisper to him discreetly the song."
        d_singer "Ah, I see. Alright, get yourself ready, as this crowd's about to get hectic!"
        camera:
            zoom 1.03
            choice:
                ease_quad 1.0 xoffset 5 yoffset 10
            choice:
                ease_quad 1.0 xoffset -5 yoffset 10
            choice:
                ease_quad 1.0 xoffset 5 yoffset -10
            choice:
                ease_quad 1.0 xoffset -5 yoffset -10
            repeat
        scene dream_cg_scene5:
            yalign 0.5
        show dream_cg_scene5_both:
            xalign 0.5
            yalign 1.0
        show dream_cg_scene5_light at pulse
        with scenedissolve
        "Both of you started singing, and the crowd goes even wilder as headlights were spotted to both of you."
        "But you don't care about that. Your eyes only focused on him as you sang, while trying hard not to cry from the excitement as you look at his masked face."
        "The harsh light gleamed against to him so strongly that you caught a glimpse of his eyes."
        "They were green..."
        "You were lost in the song in his eyes, having caught a milisecond of his identity."
        "You wonder and think, will this last forever?"
        $ renpy.music.set_volume(0.0, delay=0.0, channel='sfx2')
        play sfx2 alarmloop loop
        $ renpy.music.set_volume(1.0, delay=5.0, channel='sfx2')
        "Maybe..."
        "Maybe.."
        "{cps=15}Mayb{nw}"
        $ renpy.music.set_volume(1.0, delay=0.0, channel='sfx2')
        stop sfx2 fadeout 1.0
        stop ambient
        camera
        hide dust_particle onlayer dream behind textbox_dream
        hide dust_particle_blur onlayer dream behind textbox_dream
        window hide(None)
        play sound alarm
        scene black
        pause 4.0
        $ DreamScene.stop()
        $ renpy.end_replay()

    $ dream.grant()
    $ dhannica_age = "18"
    $ dhannica_description = "There's not much to say anything about me."
    $ entry1 = "Entry No. 1\n\nThe dream was something else. The person in my dreams... I saw them. It felt familiar. Emerald eyes... Oh, if only it were real, I would never wake up. One can dream though, haha."
    $ journal_entries.append(entry1)

    if not config.developer:
        $ renpy.block_rollback()
    window auto
    menu:
        "Get up and turn off the alarm":
            camera at dizzy
            scene bg dhannica room with eye_open
            dhannica_i "Ugh... That was such a dream."
            dhannica_i "Why did I set this alarm so early?"
            play sound stomachgrowl
            window hide(None)
            pause 1.25
            window auto
            dhannica_i "Oh shoot, I forgot! I never really had dinner last night."
            camera at reset_dizzy
            play sound phone_notif
            dhannica_i "Huh? My phone..."
            dhannica_i "..."
            dhannica_i "It won't hurt to peek right?"
            menu:
                "Check your phone":
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
                    $ journal = True
                    $ update_journal("Journal unlocked.")
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
            "Until there's nothing to remember."
            "Just the empty feeling of loosing something you never had."
            play sound alarm fadein 3.0 loop volume 0.6
            window hide(None)
            pause 3.0
            camera at dizzy
            scene bg dhannica room with eye_open
            window auto
            dhannica_i "Urk..."
            dhannica_i "Alright, alright! I'm awake!"
            "Feeling somewhat disoriented, you extended your hand to grab your phone and checked the time."
            stop sound fadeout 0.2

    if beLate:
        camera at reset_dizzy
        dhannica "{sc}IT'S 7:55?!{/sc}" with vpunch
        dhannica "{sc}SHOOT!{/sc}"
        $ journal = True
        $ update_journal("Journal unlocked.")
        if usePhone:
            "You jumped out of bed after spending a good 45 minutes scrolling on your phone and head downstairs."
        else:
            "You jumped out of bed, changed into your uniform, rushed out the door and head downstairs."

    scene black with scenedissolve
    play sound thump
    scene bg living room with scenedissolve
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
        show mom at trans3
        girlMom "Why are you limping? What's wrong with your foot?"
        dhannica "I stubbed my toe but it's fine, it'll go away in a few minutes."
        girlMom "I don't think you should go to school today, that might get worse if you force yourself to school."
        dhannica "Too late mom."
        hide mom at trans3
        girlMom "At least bring an ice pack!"
        dhannica "I'm going, bye~"
        $ update_journal("Journal updated.")
        $ dhannica_description = "{0} Well, a bit tardy I suppose.".format(dhannica_description)
        "You rushed outside."
    elif eatBreakfast:
        "You accidentally bumped your toe on the baluster."
        dhannica "Arrrrgh...this sucks, what the hell."
        dhannica_i "Why did it have to be on the first day of school?"
        dhannica_i "This smells like bad luck to me."
        dhannica "This day just started in a bad note. Let's hope it doesn't get worse for the rest of the day."
        "You came down the stairs limping on your one leg, while checking your phone for the notification that had rung a few moments ago."
        "Suddenly, your mother swiftly came through the scene and noticed your groggy appearance."
        show mom at trans3
        girlMom "What happened hon?!"
        dhannica "I'm fine mom, I just stubbed my toe on the way down the stairs. I'm fine."
        girlMom "You don't seem fine. I don't think you'd have a pretty good day at school limping like that."
        dhannica "It doesn't hurt that much."
        dhannica_i "It hurts a lot~"
        dhannica "I just stubbed my toe, it's not like I dislocated it. It's gonna be fine after a few minutes."
        girlMom "You sure? I can send your teacher a note."
        dhannica "I'd rather go limping to school than be the weird kid who misses the first day, and ends up having no friends for the rest of the school year."
        girlMom "Well, if you say so. Just make sure not to overexert yourself. We don't wanna spend money to the doctors now, do we?"
        hide mom at trans3
        dhannica "Yes mom, I won't~"
        dhannica_i "Though my foot still hurts..."
        "You ate breakfast with your mother and went outside."
    
    scene black with scenedissolve
    play sound doorclose
    scene bg highway with scenedissolve
    play ambient birds fadein 1.0

    if beLate:
        "Running frantically on a Monday morning with nothing to eat and an injured toe can surely do something to you."
        "You felt weak and drained, when you've barely even started the day."
        dhannica_i "Hopefully the milk is enough to heal my toe..."
        "You saw the bus drive right pass you while you're barely catching up because of your current situation."
        dhannica_i "Oh crap!"
        "You tried to keep up with the bus as much as you could."
        "You started to look like a zombie from an apocalypse movie, just limping as fast to get there in time."
        "As the bus took its momentary halt at the bus stop, tons of people were also waiting to get on."
        "Which meant more time for you to be able to '{i}limp{/i}' your way to the bus stop."
        scene bg busstop with scenefade
        play ambient2 busengine fadein 1.0
        dhannica_i "Almost there...!"
        "You're quite confident that you would get there in time, despite the fact that you look like an absolute ninny."
        "But you started to notice the bus was reaching its capacity, and people were getting fewer by the second."
        dhannica_i "Wait, please!"
        "You had to do something..."
        menu:
            dhannica_i "Should I just run for it?"
            "Yes":
                "You mustered up the courage to suck up the pain and just run for it, and that's exactly what you did."
                "You didn't care about your appearance, even if you felt people were staring at you, wondering if you were okay or if they should help you."
                play sound bus_open fadeout 0.5
                stop ambient2 fadeout 10.0
                show bg busstop_no_bus with dissolve
                "However, as you were about to reach the door, it immediately closed, which could only mean one thing: it was already full and the bus had already left."
                dhannica_i "No..."
                "A sudden pang of pain rushed through you."
                dhannica_i "Aaargh!" with vpunch
                dhannica_i "I forgot about my injury."
                dhannica_i "Wait, it's been 10 minutes since this happened. Why hasn't it gone away?"
                "The pain wasn't getting any better. Your decision to overwork yourself and recklessly run had only made it worse."
                "You couldn't even move your foot without feeling like it was being twisted 180 degrees."
                "You sat down on a nearby bench, contemplating if you could still manage to walk to school."
                "Glancing to your right, you checked the time for the next bus."
                camera:
                    truecenter
                    ease 1.0 zoom 1.5 xalign 0.3 yalign 0.6
                dhannica_i "...the next 15 minutes, huh? That's better than walking 30 minutes to school."
                dhannica_i  "But, good heavens, it still hurt."
                camera:
                    ease 2.0 xalign 0.5
                show nick:
                    offscreenleft
                    ease 2.5 xalign 0.5 ypos 1.03
                "As you kept your gaze fixed on the bus schedule, you noticed a presence beside you."
                show nick at trans3
                "If you hadn't looked up, you might not have even noticed him."
                camera:
                    ease 1.0 yalign 0.55
                "His head appeared to be facing the street, as if he paid no attention to his surroundings, but you caught a glimpse of his eyes directed at your feet."
                "It's as if he was trying to discreetly assess what was wrong with you."
                camera:
                    ease 1.0 yalign 0.6
                show flask:
                    alpha 0.0
                    zoom 0.7
                    blur 10
                    xalign 0.5
                    yalign 0.9
                    parallel:
                        ease 3.0 alpha 1.0
                "You decided not to pay him any mind and sat uncomfortably, trying to remain calm and not draw attention to yourself."
                "Suddenly, a cold sensation touched your skin."
                menu:
                    "Accept it":
                        $ Nick.add(5)
                        $ n_takeIcedTea = True
                    "Refuse":
                        $ n_refuseIcedTea = True
                        pass
                $ meetNick = True
                $ current_route = 'nick'
                $ update_journal("Character added.")
                play music meet fadein 1.0
                camera:
                    ease 1.0 zoom 1.5 truecenter
                hide flask with Dissolve(0.2)
                dhannica "Umm... what's this?"
                nick "Put this on your foot."
                dhannica "Excuse me?"

                if n_takeIcedTea:
                    nick "You sprained yourself, right?"
                    dhannica "I uh, stubbed my toe."
                    "He let out a small chuckle, but it sounded more like he was mocking."
                    dhannica_i "Was he laughing at my situation?"
                    dhannica_i "I swear, this guy..."
                    dhannica "What's so funny?"
                    nick "Nothing. Here."
                    show nick:
                        ease_back 1.0 yalign 7.0 
                    "He applies the cold side of his flask to the affected area."
                    dhannica "H-hey, isn't this a bit too much?"
                    nick "Just take it, or it'll get worse."
                    dhannica "But it'll get dirty!"
                    
                elif n_refuseIcedTea:
                    nick "Something for your foot."
                    dhannica_i "What's he talking about? The heck is this guy's problem?"
                    nick "It's just iced tea."
                    dhannica "And? I'm not gonna drink that."
                    nick "Didn't I say it was for your foot?"
                    "There was a tone of pushiness and arrogance when he responded."
                    dhannica_i "Pushy and arrogant? I can play that game."
                    dhannica "I barely know you."
                    "What kind of a half-baked response was that?"
                    nick "You soon will."
                    show nick:
                        ease_back 1.0 yalign 7.0 
                    "He rose from his seat and knelt down to your level, leaving you confused."
                    dhannica "W-what are you doing?"
                    nick "I've had these injuries last month, and trust me, you wouldn't want this to get worse than it already is."
                    "You feel embarassed, after hearing his intentions."
                    dhannica "A-actually, it was my toe..."
                    nick "What?"
                    dhannica "I stubbed my toe because I was running late."
                    "You explained with a hint of annoyance, which made him chuckled. But this only frustrated you even further."
                    dhannica "What's so funny?"
                    "He didn't answer. Instead, he removed your shoe and held the flask close to your foot."
                    dhannica "Wait!" with vpunch
                    nick "What is it?"
                    dhannica "I-it'll get dirty."

                dhannica "Aren't you bothered that I'm going to get your drink dirty from my foot?"

                if n_takeIcedTea:
                    nick "I'm not going to drink it from the side anyway. As long as the mouth of the flask isn't soiled, then it's fine."
                    dhannica_i "Why is he so pushy?"
                    "He retrieved a hand towel from his bag that looked like it could cover the entire surface of a flask."
                    "He took the flask from your hands and started wrapping around it."
                    "You looked at him for a moment, convincing yourself that it was okay while you're applying the flask on your affected area."
                    "At first, it hurt, but the pain had subsided."
                    camera:
                        ease 1.0 yalign 0.6
                    "As you knelt down, tending to your swollen toe, you couldn't help but notice his shoes."
                    
                else:
                    nick "You have socks on. It's fine."
                    dhannica "It's not! It'll be gross!"
                    "With a sigh, he seemed to give in and took out a hand towel from his bag. He wrapped it around the flask, not too thick that it would insulate the cold, but not too thin that it would hurt."
                    "Gently, he handled your foot with caution, trying not to cause any pain, and positioned it on his knee."
                    "He then began patting the cold flask to your foot. At first, it hurt, but you soon felt immense relief."
                    dhannica_i "This is weird."
                    "He gave you a quick glance, checking if you were alright and if he'd done a good job."
                    "In that moment, you saw them clearly: his eyes, one blue and the other green. Something about him felt peculiar to you."
                    "As he tended to your foot, you couldn't help but notice his shoes."
                    
            "No":
                $ n_takeBus = True
                dhannica_i "You know what? I think it's safest to just keep my pace; I know I'll get there anyways."
                "You continued walking at the same limping pace, enduring the persistent pain in your foot."
                "As you approached the bus stop, you noticed a commotion of people rushing onto the bus."
                "The crowd dwindled to four, then three, then two, until only one person remained."
                play sound bus_open fadeout 3.0
                "The last person tried to board, but was rejected by the conductor informing that the bus was already full."
                "You stood there, observing the commotion, unintentionally fixating on a man berating the driver."
                stop ambient2 fadeout 3.0
                show bg busstop_no_bus with dissolve
                "You didn't realize you'd been standing there for 20 seconds, nor did you know why you had."
                "He finally looked in your direction, and when both of your eyes met, you instinctively glanced at the ground, as if you hadn't already been caught staring."
                $ meetNick = True
                $ current_route = 'nick'
                $ update_journal("Character added.")
                play music meet fadein 1.0
                nick "Why are you looking at me like that?"
                "You tried your best not to appear obvious and began to slowly make your way to a nearby bench, attempting not to limp to hide your injury."
                "He continued to stand there, waiting for the next bus to arrive."
                ".{w=1.0}.{w=1.0}.{w=1.0}"
                "The silence was there, stagnating in the air."
                dhannica "You can sit down if you'd like. The next bus comes in about 15 minutes anyway."
                ".{w=0.5}.{w=0.5}.{w=0.5}"
                dhannica_i "DID I JUST SAY THAT, [Main!u]?!" with vpunch
                show nick at trans3
                "Dumbfounded, he joined you on the bench after a few moments."
                hide nick at trans3
                "The rest of the wait was quiet. You didn't pay him much attention, your primary concern being your throbbing toe."
                "It was becoming increasingly worrisome that such a minor incident was causing so much pain."
                ".{w=1.0}.{w=1.0}.{w=1.0}"
                dhannica_i "Sometimes, I don't even know why I hit the snooze button."
                dhannica "{size=-10}How does anyone wake up after the first alarm?{/size}"
                play ambient2 busengine fadein 2.0
                show bg busstop with dissolve
                "As you sat there contemplating your life choices, the next bus had already arrived."
                play sound busopen
                "Both of you stood up at the same time, despite the atmosphere being thick between the two of you."
                "He seem to have rushed and went ahead of you before boarding into the bus."
                "It appeared to be full, but you needed to check if you could squeeze in."
                stop ambient fadeout 1.0
                stop ambient2 fadeout 1.0
                scene bg bus with scenefade
                "Upon entering, you scanned the area for seats, only to meet disatisfaction as all were taken."
                dhannica_i "No seats. Great, more fun."
                dhannica_i "Guess I'll be standing then."
                "By this point, you had grown accustomed to discomfort. Getting comfortable with it seemed like the only way to endure."
                dhannica_i "Dang, this sucks. I never should've catch more zZz."
                dhannica_i "But thank goodness for these handrails. I could barely maintain my balance."
                "To alleviate your pain, you decided to entertain yourself by gazing out the window, watching people going about their lives without a care in the world."
                "Sighing, you eventually turned your gaze on your left."
                dhannica_i "Great, it's that guy from the bus stop."
                "Your eyes met him, and the only thought that entered your mind was about his eyes."
                "He was gazing at you, with his laid back posture and his bleak expression before drifting his eyes to the ground."
                "You hadn't even realized you were staring until you watched him rise from his seat, towering over you."
                nick "Sit down."
                "He commanded with a strong yet mellow voice, which your body obeyed, and took a seat."
                dhannica "U-uhm, okay."
                "You were quite embarrassed, trying not to look at his face."
                "You draped your hair over your features as you bent down, concealing your expression, which was in complete utter embarrassment."
                dhannica "{size=-5}Thank you...{/size}"
                "He handed you a flask, with its exterior dripping wet with pebbles of moist water sliding off of it."
                show nick at trans3
                nick "Here."
                nick "Put this on your foot. The cold will help your swelling."
                menu:
                    "Take the flask":
                        $ Nick.add(5)
                        $ n_takeFlask = True
                        dhannica "Are you sure?"
                        nick "Just do it."
                        hide nick at trans3
                        "You wrapped the bottle with his hand towel, mindful of the fact that a complete stranger had just offered you his personal belonging to alleviate your discomfort."
                        "He doesn't look like the helping type."
                        "In fact, he appears as though he doesn't want to interact with anyone."
                        "You gently applied the cold flask to the side of your foot and instantly began to experience relief. Your pinky toe had swelled and grown warm, but this remedy appeared to be reducing the discomfort."
                        "Leaning down as you tended your injury, you couldn't help but notice his shoes."
                    "Refuse":
                        $ n_refuseTake = True
                        dhannica "You wouldn't want me to do that."
                        nick "Why not?"
                        dhannica "I mean, you drink from that. Wouldn't you be bothered if I put it on my foot?"
                        "In response, he retrieved a hand towel from his shoulder bag."
                        nick "Here, wrap this around the bottle. That'll keep it cleaner, if that's your concern."
                        dhannica "Please, you don't have to. I'm fine."
                        "You plead in the most convincing way you could."
                        hide nick at trans3
                        "However, your efforts were in vain, as he knelt down and took matters into his own hands."
                        dhannica "W-what are you doing?"
                        nick "I've had these injuries last month, and trust me, you wouldn't want this to get worse than it already is."
                        "As he glanced at you, you saw his eyes clearly."
                        "Blue and green, a peculiar and intriguing combination."
                        nick "Remove the shoe."
                        dhannica "O-oh, right."
                        "He carefully wrapped the bottle in his hand towel and gently placed your foot on his knee, applying the cold bottle to the sore area."
                        "You winced at the pain."
                        dhannica_i "Ow...!" with vpunch
                        dhannica_i "No wait, that's actually not bad."
                        "You watched as he continued to gently pat the cool towel on your foot. Your gaze wandered to his features."
                        "You scrutinized him and couldn't help but notice his shoes."

        "They were quite rugged, classic black and white high-top Chuck Taylors."
        dhannica_i "Hmm...cute."
        dhannica_i "There are little cute spiderhero webs drawn all over the tips of his shoes." 

        if n_takeIcedTea:
            $ Nick.add(5)
            camera:
                ease 1.0 truecenter zoom 1.0
            show nick:
                ease_back 1.0 yalign 1.0
            nick "There, that should do it."
            show nick at trans3
            nick "..."
            dhannica "..."
            nick "I uhh, gotta go."
            show nick:
                ease_back 1.0 offscreenright
            dhannica "Wait! Your flask!..."
            "You're clueless at what just happened."
            dhannica_i "Guess I'll return this..."

        if n_refuseIcedTea:
            show nick:
                ease_back 1.0 yalign 1.03
            show nick at trans3
            "He rose abruptly, seemingly aware that the interaction between you two was drawing attention."
            camera:
                ease 1.0 truecenter zoom 1.0
            "It was sort of giving a public display of affection, garnering curious glances from onlookers."
            nick "J-just put that there. Give the bottle back to me when you get a chance."
            hide nick at trans3
            "He soon left at a fastened pace, leaving you all alone in the bus stop."
            dhannica_i "Well that was...interesting."
            jump school

        if n_takeFlask:
            show nick at trans3
            nick "There, that should do it."
            nick "..."
            dhannica "..."
            nick "Err...keep that until the cold is gone. Just give it back to me when you're done."
            show nick:
                ease 1.0 offscreenleft
            pause 1.0
            play sound busopen
            pause 1.2
            play ambient busengine fadein 0.7
            pause 1.6
            play sound busopen
            pause 1.0
            stop ambient fadeout 1.2
            window auto
            "He disembarked at the next bus stop, and you never saw him again."
            "Silence came after, for the rest of the ride."
            play ambient birds fadein 2.0
            jump school

        if n_refuseTake:
            $ Nick.add(10)
            "After a few minutes, you began to feel better, albeit only slightly."
            "Part of you felt embarrassed by how conspicuous your situation with him must have appeared, considering that he had been kneeling for a while."
            "With the bus being so crowded, you both stood out for sure."
            show nick at trans3
            "He seemed to notice it too. It's obvious because of how he promptly stood up, maintaining his composure."
            nick "Err...keep that until the cold is gone. Just give it back to me when you're done."
            show nick:
                ease 1.0 offscreenleft
            pause 1.0
            play sound busopen
            pause 1.2
            play ambient busengine fadein 0.7
            pause 1.6
            play sound busopen
            pause 1.0
            stop ambient fadeout 1.2
            window auto
            "He disembarked at the next bus stop, and you never saw him again."
            "Silence came after, for the rest of the ride."
            play ambient birds fadein 2.0
            jump school

    else:
        "The air around you was chilly, and the birds were all up and singing."
        "Not sure what the time was, you checked your phone. You just needed to make sure you had time before the class started."
        dhannica_i "Guess I should hurry up."
        dhannica_i "As if this stupid toe would make it easier for me."
        jump school
    
label school:
    camera:
        ease 1.0 truecenter zoom 1.0
    scene bg school with scenefadehold
    $ welcome.grant()
    if beLate:
        $ update_journal("Character updated.")
        $ nick_description = "A strange guy that offered me help. Had blue and green eyes...\n\nIt's weird that he had to leave me his flask. Couldn't he just wait for it before leaving me?"
        "You finally reached the school in a faster pace, thanks to the cold flask that was applied to you by a stranger."
        dhannica_i "I gotta thank him for this."
        dhannica_i "But first, my classroom!"
        stop ambient fadeout 1.0

    else:
        $ update_journal("Journal updated.")
        $ dhannica_description = "{0} Well, an early bird I suppose.".format(dhannica_description)
        "You finally reached the school, walking through the gates limping on your other foot."
        dhannica_i "I look like a total loser. That's just great."
        dhannica_i "Is this how people are gonna remember me...? The limping kid on the first day of school..."
        "You gaze before you a school, with an interesting color choice that seem be used redundantly everywhere."
        "..."
        "It didn't take long for you to finally realize what you're here for."
        dhannica "Right, my class schedule."
        "You rummaged through your bag, only to find out your outer pocket was open and your class schedule had fallen out."
        dhannica_i "Oh great! This day just gets better and better."
        "Sarcasm was the only thing that could sugarcoat this situation."
        "You start to trace back your previous steps, carefully searching for your schedule, with your eyes glued to the ground."
        "Suddenly...a hand appeared in your field of vision, holding a piece of paper."
        "You read, '{i}Purposive Communication - 7:15 am - 8-15 am{/i}'."
        "It was your schedule."
        play music meet fadein 1.0
        $ meetAlec = True
        $ current_route = 'alec'
        $ update_journal("Character added.")
        show alec at trans3
        "You looked at his hand and followed the trail of grungy accessories, to his chain necklace up to his green eyes."
        "You don't know what you felt, but you felt some sort of gratitude."
        "That you wouldn't have to pay extra to get another copy of your schedule."
        dhannica "Uhm...thank you... for the, uhm...this."
        $ Alec.add(3)
        alec "No biggie."
        alec "I noticed your bag was open and this fell out."
        alec "It seems that we're in the same class. Nice to meet you classmate."
        "He stretches out his hand for a handshake."
        "In which, you relunctantly returned the offer."
        $ a_name = "Alec"
        $ update_journal("Character updated.")
        alec "I'm Alec."
        alec "By the way, are you okay? You don't seem to be walking right."
        dhannica "Oh...yeah haha, I stubbed my toe this morning. And well, I thought it was gonna be okay after a few minutes, but I guess that's still yet to come."
        alec "Is that so?"

        menu:
            alec "Would you like me to accompany you to the infirmary?"
            "Accept":
                $ Alec.add(2)
                $ a_clinic = True
                dhannica "I mean, sure? Classes are about to start though and we'll be late if we did."

            "Deny":
                dhannica "You don't have to, I mean I wouldn't want to bother you."
                alec "Nonsense, friends don't bother me."
                dhannica "..."
                alec "We're friends, right?"
                dhannica "I guess...?"
                dhannica_i "I've made a friend~"
                dhannica_i "And he's quite upfront with it."
                dhannica "But we'll be late if we go now."
            
        alec "I guess so. How about after the first subject? We have 30 minutes vacant. I'm sure that's enough time for the nurse to patch you up."

        if a_clinic:
            dhannica "Thanks, but you really don't have to do this."
            alec "And leave my first friend to an injury? I don't think so."
            dhannica_i "I've made a friend~"
            dhannica_i "And he's quite upfront with it."

        $ update_journal("Character updated.")
        $ alec_description = "A really stylish guy. Had green eyes... Quite friendly and offered me help. Literally added me as his friend. Well, in real life."
        dhannica "I mean if you insist, how dare would I refuse hahaha."
        alec "Let's go, we'll be late for our first subject."
        hide alec at trans3
        "He offers his hand for you to hold unto as you both walk to your classroom."
    
    stop ambient fadeout 1.0
    jump classroom

label classroom:
    scene bg classroom2 with scenefadehold
    play ambient2 classroom volume 0.5 fadein 1.0
    if beLate:
        "You hustle to class, pulling yourself towards the door with just a minute to spare before the teacher arrives."
        "Suddenly, a gentle touch on your arm catches your attention."
        show alec at trans3
        $ meetAlec = True
        $ update_journal("Character added.")
        "You turn to see a person with white hair and adorned with lots of jewelry."
        "Those unmistakable green eyes meet yours."
        dhannica "O-oh, thanks."
        alec "No problem, I was about to get in anyway."
        "He guides you to an empty seat, introducing himself along the way."
        $ a_name = "Alec"
        alec "I'm Alec, by the way."
        hide alec at trans3
        "The teacher calls the class to order."
    else:
        "You both made your way to class, arriving right on time, with the professor trailing behind as you entered."
    
    prof "Good morning, class! Lots of fresh blood I see today!"
    prof "Well, freshmen, I hope you all have an educational yet memorable time here as an STIer."
    prof "I expect you all to wear our school colors, its name, legacy, as well as your IDs."
    prof "Because believe me, the guards outside won't let you in without it. Hahaha."
    "The entire class laughs."
    stop music fadeout 1.0
    stop ambient2 fadeout 1.0
    prof "No, but seriously though, three strikes and you're out."
    prof "Alright, let's take attendance first before we discuss the school rules, shall we?"
    scene bg classroom with long_dissolve
    play ambient2 classroom volume 0.5 fadein 1.0
    "As the professor continued with the lively discussion while inserting puns to keep the atmosphere engaging, you find it challenging to focus."
    "The pain in your left foot is intensifying, and you sense Alec noticing your discomfort."
    dhannica_i "When is he gonna stop blabbering?"
    if beLate:
        "The door opens, and a newcomer rushes in, catching his breath."
        unknown_guy "Sorry, I'm late!"
        prof "Ah, first day and he's already late."
    "Suddenly, Alec raises his hand, catching the professor's attention."
    prof "Yes, Mr. Boyband with the grunge style. What's up?"
    alec "My friend here has sprained herself on the way to school and she wanted to ask if she could go to the nurse's office to get it checked out."
    prof "Well, why didn't you go there before class started?"
    if beLate:
        dhannica "Uhh..."
        "Alec looks at you as if he's expecting a better answer."
    else:
        dhannica "Uhh, we didn't want to be marked late, so we came in and took attendance first."
    prof "Well, you could've just given me the nurse's note and come in after you've gone to see her, and you'd still be marked as present, just excused."
    dhannica "W-we didn't think about that."
    prof "Well, now you have."
    prof "Class, next time prioritize your health, as long as it's valid, alright?"
    prof "You may go."
    "You stood up, limping, and headed towards the door."
    if beLate:
        prof "Are you going alone looking like that? I don't think so."
        "The professor signals the newcomer standing next to him and points at you."
        prof "Make yourself useful, since you're late. Escort her to the nurse's office."
        show nick:
            trans3
            ease 1.0 offscreenleft
        "As you take a good look at your assigned escort, surprise washes over you."
        stop ambient2 fadeout 1.0
        dhannica "{sc}It's YOU?!{/sc}" with vpunch
    else:
        prof "Aren't you going to bring your friend?"
        "Alec walks towards you to escort you to the nurse's room."
        dhannica "Thanks."
        alec "No problem."
        stop ambient2 fadeout 1.0
        scene bg school hallway with scenefadehold
        show nick:
            offscreenright
            ease 1.0 xalign 0.5
            pause .1
            ease 1.0 offscreenleft
        "As you exited, a guy rushed towards the door, abruptly halting in front of you before swerving to enter."
        nick "Sorry, I'm late!"
    jump chap2_dhannica

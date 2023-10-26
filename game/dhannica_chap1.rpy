default beLate = False
default usePhone = False
default eatBreakfast = False

default takeIcedTea = False
default clinic = False
default refuseTake = False

default alec_likePoints = 0
default nick_likePoints = 0

label dhannica_chap1:
    call chapter_transition
    $ n_name = "???"
    $ mcNameboy = "???"
    if config.developer == False:
        $ renpy.block_rollback()
    pause 2.0
    scene bg stage with scenefade
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
        show mom at appear_center
        girlMom "Why are you limping? What's wrong with your foot?"
        dhannica "I stubbed my toe but it's fine, it'll go away in a few minutes."
        girlMom "I don't think you should go to school today, that might get worse if you force yourself to school."
        dhannica "Too late mom."
        hide mom at appear_center
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
        show mom at appear_center
        girlMom "What happened hon?!"
        dhannica "I'm fine mom, I just stubbed my toe on the way down the stairs. I'm fine."
        girlMom "You don't seem fine. I don't think you'd have a pretty good day at school limping like that."
        dhannica "It doesn't hurt that much."
        dhannica_i "It hurts a lot~"
        dhannica "I just stubbed my toe, it's not like I dislocated it. It's gonna be fine after a few minutes."
        girlMom "You sure? I can send your teacher a note."
        dhannica "I'd rather go limping to school than be the weird kid who misses the first day, and ends up having no friends for the rest of the school year."
        girlMom "Well, if you say so. Just make sure not to overexert yourself. We don't wanna spend money to the doctors now, do we?"
        hide mom at appear_center
        dhannica "Yes mom, I won't~"
        dhannica_i "My foot still hurts..."
    
    "You rushed outside."
    scene black with scenedissolve
    play sound doorclose
    scene bg highway with scenedissolve
    play ambient birds
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
                "You didn't care about your appearance, because at that moment, you felt people were staring at you, wondering if you were okay or if they should help you."
                play sound bus_open fadeout 3.0
                stop ambient2 fadeout 3.0
                "However, as you were about to reach the door, it immediately closed, which could only mean one thing: it was already full and the bus had already left."
                dhannica_i "No..."
                "A sudden pang of pain rushed through me."
                dhannica_i "Aaargh!" with vpunch
                dhannica_i "I forgot about my injury."
                dhannica_i "Wait, it's been 10 minutes since this happened. Why hasn't it gone away?"
                "The pain wasn't getting any better. Your decision to overwork myself and recklessly run had only made it worse."
                "You couldn't even move your foot without feeling like it was being twisted 180 degrees."
                "You sat down on a nearby bench, contemplating if you could still manage to walk to school."
                "Glancing to your right, you checked the time for the next bus."
                dhannica_i "...the next 15 minutes, huh? That's better than walking 30 minutes to school."
                dhannica_i  "But, good heavens, it still hurt."
                "As you kept your gaze fixed on the bus schedule, you noticed a presence beside you."
                "If you hadn't looked up, you might not have even noticed him."
                "His head appeared to be facing the street, as if he paid no attention to his surroundings, but you caught a glimpse of his eyes directed at your feet."
                "It's as if he was trying to discreetly assess what was wrong with you."
                "You decided not to pay him any mind and sat uncomfortably, trying to remain calm and not draw attention to yourself."
                "Suddenly, a cold sensation touched your skin."
                "The guy sitting beside you handed something. It appeared harmless at first glance."
                menu:
                    "Accept it":
                        $ nick_likePoints += 5
                        $ takeIcedTea = True
                    "Refuse":
                        pass

                dhannica "Umm... what's this?"
                nick "Put this on your foot."
                dhannica "Excuse me?"

                if takeIcedTea:
                    nick "You sprained yourself?"
                    dhannica "I uh, stubbed my toe."
                    "Nick let out a small laugh, but it sounded more like he was mocking."
                    dhannica_i "Did he just laugh at my situation?"
                    dhannica "What's so funny?"
                    nick "Nothing. Here, take it."
                    "He offers you a cold cylinder."
                    nick "It's iced tea, the cold will help your foot."
                    "He applies the cold side of his iced tea drink to the bruised area."
                    dhannica "H-hey, isn't this a bit too much?"
                    nick "Just take it, or it'll get worse."
                    dhannica "But it'll get dirty!"
                    
                else:
                    nick "Something for your foot."
                    dhannica_i "What the heck is this guy's problem?"
                    nick "It's just iced tea."
                    dhannica "I'm not gonna drink that."
                    nick "Didn't I say it was for your foot?"
                    "He responded, in a tone of pushiness and arrogance."
                    dhannica_i "Pushy and arrogant? I can play that game."
                    dhannica "I barely know you."
                    "You replied back with dominance."
                    nick "You soon will."
                    "He rose from his seat and knelt down to your level, leaving you confused."
                    dhannica "W-what are you doing?"
                    nick "I've had these injuries last month, and trust me, you wouldn't want this to get worse than it already is."
                    "You feel embarassed, after hearing his intentions."
                    dhannica "A-actually, it was my toe..."
                    nick "What?"
                    dhannica "I stubbed my toe because I was running late."
                    "You explained with a hint of annoyance, which made Nick chuckled. But this only frustrated you even further."
                    dhannica "What's so funny?"
                    "He didn't answer. Instead, he removed your shoe and held the tumbler close to your foot."
                    dhannica "Wait!" with vpunch
                    nick "What is it?"
                    dhannica "I-it'll get dirty."

                dhannica "Aren't you bothered that I'm going to get your drink dirty from my foot?"

                if takeIcedTea:
                    nick "I'm not going to drink it from the side anyway. As long as the mouth of the tumbler isn't soiled, then it's fine."
                    dhannica_i "Why is he so pushy?"
                    "Nick retrieved a hand towel from his bag that looked like it could cover the entire surface of a tumbler."
                    "He took the tumbler from your hands and started wrapping around it."
                    "You looked at him for a moment, convincing yourself that it was okay as you took it and applied it."
                    "At first, it hurt, but the pain had subsided."
                    "As you knelt down, tending to your swollen toe, you couldn't help but notice his shoes."
                    
                else:
                    nick "You have socks on. It's fine."
                    dhannica "It's not! It'll be gross!"
                    "With a sigh, Nick seemed to give in and took out a hand towel from his bag. He wrapped it around the tumbler, not too thick that it would insulate the cold, but not too thin that it would hurt."
                    "Gently, he handled your foot with caution, trying not to cause any pain, and positioned it on his knee."
                    "He then began patting the cold tumbler to your foot. At first, it hurt, but you soon felt immense relief."
                    dhannica_i "This is weird."
                    "He gave you a quick glance, checking if you were alright and if he'd done a good job."
                    "In that moment, you saw them clearly: his eyes, one blue and the other green. Something about him felt peculiar to you."
                    "As he tended to your foot, you couldn't help but notice his shoes."
                    
            "No":
                dhannica_i "You know what? I think it's safest to just keep my pace; I know I'll get there anyways."
                "You continued walking at the same limping pace, enduring the persistent pain in your foot."
                "As you approached the bus stop, you noticed a commotion of people rushing onto the bus."
                "The crowd dwindled to four, then three, then two, until only one person remained."
                play sound bus_open fadeout 3.0
                "The last person tried to board, but was rejected by the conductor informing that the bus was already full."
                "You stood there, observing the commotion, unintentionally fixating on a man berating the driver."
                stop ambient2 fadeout 3.0
                "You didn't realize you'd been standing there for 20 seconds, nor did you know why you had."
                "He finally looked in your direction, and when both of your eyes met, you instinctively glanced at the ground, as if you hadn't already been caught staring."
                nick "Why are you looking at me like that?"
                "You tried your best not to appear obvious and began to slowly make your way to a nearby bench, attempting not to limp to hide your injury."
                "The man continued to stand there, waiting for the next bus to arrive."
                ".{w=1.0}.{w=1.0}.{w=1.0}"
                dhannica "You can sit down if you'd like. The next bus comes in about 15 minutes anyway."
                dhannica_i "DID I JUST SAY THAT, [Main!u]?!" with vpunch
                "Dumbfounded, he joined you on the bench after a few moments."
                "The rest of the wait was quiet. You didn't pay him much attention, your primary concern being your throbbing toe."
                "It was becoming increasingly worrisome that such a minor incident was causing so much pain."
                ".{w=1.0}.{w=1.0}.{w=1.0}"
                dhannica_i "Sometimes, I don't even know why I hit the snooze button."
                dhannica "{size=-20}How does anyone wake up after the first alarm?{/size}"
                play ambient2 busengine fadein 2.0
                "As you sat there contemplating your life choices, the next bus had already arrived."
                play sound busopen
                "It appeared to be full, but you needed to check if you could squeeze in."
                "You glanced to see if the person next to you had departed, and it seemed he had. You spotted him boarding the bus."
                stop ambient fadeout 1.0
                stop ambient2 fadeout 1.0
                scene bg bus with scenefade
                "Upon entering, you scanned the area for seats."
                "Unfortunately, all the seats were taken."
                dhannica_i "No seats. Great, more fun."
                dhannica_i "Guess I'll be standing then."
                "By this point, you had grown accustomed to discomfort. Getting comfortable with it seemed like the only way to endure."
                dhannica_i "Dang, this sucks. I never should've rushed."
                dhannica_i "Thank goodness for these handrails. I could barely maintain my balance."
                "To alleviate your pain, you decided to entertain yourself by gazing out the window, watching people going about their lives without a care in the world."
                "Sighing, you eventually turned your gaze downward."
                dhannica_i "It's that guy before from the bus stop!"
                "Your eyes met him, and the only thought that entered your mind was about his eyes."
                "He was gazing at you, with his laid back posture and his bleak expression before drifting his eyes to the ground."
                "You hadn't even realized you were staring until you watched him rise from his seat, towering over you."
                nick "Sit down."
                "He commanded with a strong yet mellow voice, which your body obeyed, and took a seat."
                dhannica "U-uhm, okay."
                "You were quite embarrassed but dared not look at his face."
                "You draped your hair over your features as you bent down, concealing your expression, which was complete utter embarrassment."
                dhannica "{size=-20}Thank you...{/size}"
                "He handed you a tumbler, with its exterior dripping wet with pebbles of moist water sliding off of it."
                nick "Here."
                nick "Put this on your foot. The cold will help your swelling."
                menu:
                    "Take the tumbler":
                        $ nick_likePoints += 5
                        dhannica "Are you sure?"
                        nick "Just do it."
                        "You wrapped the bottle with his hand towel, mindful of the fact that a complete stranger had just offered you his personal belonging to alleviate your discomfort."
                        "He doesn't look like the helping type."
                        "In fact, he appears as though he doesn't want to interact with anyone."
                        "You gently applied the cold tumbler to the side of your foot and instantly began to experience relief. Your pinky toe had swelled and grown warm, but this remedy appeared to be reducing the discomfort."
                        "Leaning down as you tended your injury, you couldn't help but notice his shoes."
                    "Refuse to take it":
                        $ refuseTake = True
                        dhannica "You wouldn't want me to do that."
                        nick "Why not?"
                        dhannica "I mean, you drink from that. Wouldn't you be bothered if I put it on my foot?"
                        "In response, he retrieved a hand towel from his shoulder bag."
                        nick "Here, wrap this around the bottle. That'll keep it cleaner, if that's your concern."
                        dhannica "Please, you don't have to. I'm fine."
                        "You plead in the most convincing way you could."
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

        if not refuseTake or refuseTake:
            "They were quite rugged, classic black and white high-top Chuck Taylors."
            dhannica_i "Hmm...cute."
            dhannica_i "There are little cute spiderhero webs drawn all over the tips of his shoes." 
            if refuseTake:
                $ nick_likePoints += 10
                "After a few minutes, you began to feel better, albeit only slightly."
                "Part of you felt embarrassed by how conspicuous your situation with him must have appeared, considering that he had been kneeling for a while."
                "With the bus being so crowded, you both stood out for sure."
                "And he seemed to notice it too. It's obvious because of how he promptly stood up, maintaining his composure."
                nick "Keep that until the cold is gone. Just give it back to me when you're done."
                window hide
                pause 4.0
                window auto
                "Then, silence came after."
                "Pretty soon, he disembarked at the next bus stop, and I never saw him again."

    else:
        "The air around you was chilly, and the birds were all up and singing."
        "Not sure what the time was, you checked your phone. You just needed to make sure you had time before the class started."
        dhannica_i "Guess I should hurry up."
        dhannica_i "As if this stupid toe would make it easier for me."
        jump school
    
    label school:
        scene bg school with scenefade
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
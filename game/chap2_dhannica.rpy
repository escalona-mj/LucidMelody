label chap2_dhannica:
    window auto hide
    call chapter_transition
    
    if beLate:
        prof "Oh? So you've met this student before?"
        dhannica "Y-yes."
        prof "I see."
        prof "Take her to the infirmary."
        scene bg school hallway with blur_fadehold
        "You both walk in the long hallways of the school, searching for the infirmary."
        "You tried to maintain your posture, but your limping slowed you down."
        nick "Hey, slow down. You're going to hurt yourself more."
        dhannica browangy eyeclose sad"I know what I'm doing. I can manage."
        nick eyelook "You know what? I'll walk with you. Just in case."
        "You appreciate his concern, but you felt a bit embarrassed about being so dependent."
        "His insistence was comforting in a way."
        nick "There's the infirmary."
        nick -eyelook smile "Let's get you there."
        "As you both walked, the hallways were bustling with students and you noticed them stealing a glance at both of you, probably wondering about the unusual pair."

    else:
        dhannica_i eyehappy browsad sweat "Sheesh, talk about being late..."
        dhannica_i -eyehappy -browsad -sweat "Glad I woke up in time."
        "You both walk in the long hallways of the school, searching for the infirmary."
        alec "Ah, there it is."
        alec smile "Let's get you there."
        "He holds you from the side to offer support from your limping state."
        dhannica_i sad "Woah-"
        dhannica_i eyehappy browsad sweat -sad "Yep. Very upfront."

    scene bg clinic
    show nurse at trans3
    with long_dissolve
    nurse "It seems you've broken your pinky toe pretty badly. It's been dislocated."
    dhannica sad browsad sweat "Yeah... I stubbed my toe this morning pretty hard because I was in a hurry."

    if beLate:
        show nurse at trans2
        show nick smile browsus at trans3
        "You stole a glance at him and he was concealing a mockingly irritiating smirk, as if laughing at you."
        show nick eyeclose
        dhannica browangy -sweat "Tsk."
        hide nick at trans3
        show nurse at trans3
        "He collects himself and acts as if nothing happened."
        dhannica browsad "Anyways, yeah that happened. And well, it got a bit worse because I kind of ran for the bus because I was running late."
        "You turn your head in a snap, glaring at him, with your eyes narrowed. Mentally screaming at him to shut up."
        dhannica_i browangy eyeclose "This guy has an unbelievable way of making my blood boil."
        nurse look "Well, I can't do anything about your case. It's gotten quite severe, although I expected it to look a lot worse since you mentioned that you ran."
        nurse "But to my suprise, it's not as worse as I'd expected it to be. Although, this is not something that I can treat without making it worse."
        nurse "I'll have to arrange an excuse letter for this because this injury is needed to be treated and taken to the hospital."
        "The nurse seems to be looking for something, and it looks like whatever it was, it wasn't in the room."
        nurse -look "Please wait for me here."
        hide nurse at trans3
        "The nurse goes outside."
        window hide
        pause 2.5
        window auto
        "There was a moment of brief silence."
        "You could feel the awkwardness. Like lost words in the air, not able to form anything but tension. Uncomfortable tension in the silence is surrounding the both of you."
        "A slight hint of guilt suddenly reminded you of his act this morning."
        dhannica -browangy -eyeclose "Oh! Before I forget..."
        show nick browsus at trans3
        "You rummage through your bag to give back his flask."
        show expression "images/misc/return_flask.png":
            zoom 1.5
            xalign 0.5 yoffset 250 xoffset 0
            ypos 1.0 yanchor 0.0
            ease 1.0 ypos 1.0 yanchor 1.0
        dhannica eyehappy -sad"Thank you, by the way."
        show nick eyeclose -browsus smile at trans3
        nick "I've been waiting for that."
        show nick -eyeclose
        show expression "images/misc/return_flask.png":
            ypos 1.0 yanchor 1.0
            ease 0.25 ypos 1.0 yanchor 0.0
        "..."
        dhannica -eyehappy sad "I'm sorry, but your eyes look unusual."
        nick eyelook -smile "Eh, I get that a lot."
        show nick -eyelook
        dhannica "I know what it is. I've heard of it, but I forgot what it's called."
        show nick browsus
        dhannica "Heterosexual...?"
        show nick eyeclose
        dhannica "Homosapien...?"
        "Your thoughts start to wander as he noticed you doing your best retrieving the word you were looking for."
        nick "Heterochromia."
        dhannica "Hetero-what?"
        nick -eyeclose -browsus "It's heterochromia."
        dhannica "Yep, I knew it."
        dhannica_i eyehappy -sad"Heterochromia..."
        "You repeated, trying to imprint the word in your memory."
        dhannica "It's unique."
        nick smile eyelook raise_arm  "Well y-yeah, it's a genetic thing. Nothing special."
        "You sense a hint of defensiveness in his tone, like he had to downplay it. It made you curious."
        dhannica -eyehappy "So, why were you late this morning? Is it a habit or just bad luck today?"
        show nick -smile
        "He hesitated for a moment, as if weighing whether to share."
        nick -raise_arm "Just one of those days, I guess. Overslept, missed the alarm."
        "You wanted to probe further but decided against it. You both sat in silence for a moment, before you realized you haven't properly introduced yourself."
        dhannica "I'm [Main], by the way."
        $ n_name = 'Nick'
        $ update_journal("Character updated.")
        nick -eyelook "Nick. Nice to officially meet you, [Main]."
        show nick at trans1
        show nurse at trans3
        "Just then, the nurse returned, holding a slip of paper."
        nurse "[Main], you'll need to visit the hospital for proper treatment."
        nurse "Should I call your parent or guardian to bring you to the hospital?"
        dhannica "My mother. Yeah, here's her number."
        "You gave your mother's number to the nurse."
        nurse "And Nick, since you escorted her, you're excused from being late. I'll inform your teachers."
        show nick smile
        "Nick seemed relieved, almost grateful for the excuse."
        nurse "Take care of your foot, [Main]. And try not to be too adventurous with stairs."
        hide nurse at trans3
        show nick at trans3
        "She handed you the note, and you took it, mixed with a feeling of embarrassment and gratitude."
        dhannica "Thanks for everything, Nick. I guess I'll see you around?"
        show nick raise_arm -smile
        nick eyelook "Yeah, sure. Take care of that foot. And, uh, maybe try not to rush so much."
        "He gave a small, almost shy smile, which seemed out of character from the Nick you encountered earlier."
        "It made you wonder about the many layers he might have."
        hide nick at trans3
        "As he walked away, you couldn't help but feel a strange connection to him."
        "Something about his eyes, his mannerisms, or maybe just the way the morning unfolded."
        $ update_journal("Character updated.")
        $ nick_description = "{0}\n\nDespite his annoying facade, he can be quite helpful. I'm not sure, as it seemed out of character for Nick to act like that. He was probably just being polite.".format(nick_description)
        dhannica_i "Nick, huh? You sure an interesting individual."
        "Sitting in the clinic while waiting for your mother, you couldn't shake off the feeling that today was the start of something new."
        "Maybe it was the pain in your foot or the unexpected kindness from a stranger..."
        "But you felt like this was a turning point."
        show mom worried at trans3
        "Soon enough, your mother arrived, her face etched with worry."
        if Main == "Dhannica":
            girlMom "Dhanni, you really need to be more careful. Why the rush this morning?"
        else:
            girlMom "[Main], you really need to be more careful. Why the rush this morning?"
        "You explained the situation, leaving out the part about Nick. Somehow, you weren't ready to share that detail yet."

    else:
        alec "Eesh, that's painful."
        alec "I remember it happening to me to the point I felt like I was dying."
        alec "But yours looks worse. I can't imagine how you're feeling right now." 
        dhannica "Kinda meh. Gotten used to the pain."
        "You gave him a thumbs up and acted cool to hide the pain in front of him."
        show alec at trans4
        show nurse at trans2
        alec "Oh stop acting cool, it doesn't suit you, hahaha."
        dhannica "Well I try my best, hahaha."
        nurse "D'aww, you guys are cute."
        nurse "You both make a great couple!"

        menu:
            dhannica_i "Uh..."
            "\"Oh no, we're just friends.\"":
                $ Alec.remove(5)
                nurse "Is that so? Well, I bet you're really good friends then?"
                alec "Very much so, hahaha. Am I right?"
                dhannica "Yeah, I don't even know this guy, hahaha."

            "Laugh it off":
                $ Alec.add(10)
                dhannica "Ahaha..."

        hide alec at trans3
        show nurse at trans3
        dhannica_i "But we do seem to get along quite well."
        nurse "Well, I suggest you get this treated at a hospital so they can patch up your dislocated toe. I can't do anything since I'm only a nurse; that's beyond my skills."
        nurse "I treat students with injuries but yours seems to have gotten worse."

        menu:
            nurse "Did you do anything to cause it to swell up so badly?"
            "Yes":
                dhannica "Well, I walked here."
                nurse "You should've taken your time, or asked your mother to take you."

            "No":
                dhannica "No, I just walked here."
                nurse "Well, that may still strain and worsen the condition. It's probably why it gotten so swollen."

        nurse "{bt=3} *sighs* {/bt}"
        nurse "Well it would probably take you a few days of rest before you can come back to school, so I'll make you an excuse letter."
        dhannica_i "Great, just when I thought this would be a normal week."
        nurse "Give this to your professor as a pass for the days you're going to miss."
        nurse "Should I call your parent or guardian to bring you to the hospital?"
        dhannica "My mother. Yeah, here's her number."
        "You gave your mother's number to the nurse."
        dhannica_i "I guess I need some catching up to do once all of this is over."
        show alec at trans4
        show nurse at trans2
        alec "Well, I'll better be going, I don't want to miss too much in class."
        dhannica "Okay, thanks for helping me by the way!"
        alec "No problem, I'll send you some of my notes so you'd be able to keep up with us."
        "Hearing that, an indescribable weight has fell off from your shoulders."
        dhannica "That'd be great! Thanks a bunch!"
        alec "Take care!"
        hide alec at trans3
        show nurse at trans3
        "He fastened his pace and went outside of the infirmary."
        $ update_journal("Character updated.")
        $ alec_description = "{0}\n\nHe's quite very upfront with everything, but I don't mind. But for a moment, someone actually looks after me despite everything. And Alec is no greater example of that.".format(alec_description)
        dhannica "Yeah... you too."


    scene bg hospital with long_dissolve
    play ambient hospital volume 0.5 fadein 1.0
    $ update_journal("Journal updated.")
    $ dhannica_description = "{0}\n\nFirst day of school went horribly. Not only I was sent to a hospital due to negligence of my 'initally thought a small scratch that wouldn't be that much of a problem' turned out to be a big problem.".format(dhannica_description)
    "After quite some time, your mother picked you up from school and took you to a nearby hospital."
    girlMom "Didn't I tell you to just stay at home?"
    dhannica "Yes, but it was the first day I didn't want to mis-{nw}"
    if Main == "Dhannica":
        girlMom "But look where it got you. Next time Dhanni, when you know you can't take it, just tell me. Making a letter is easier than seeing you like this. Alright?"
    else:
        girlMom "But look where it got you. Next time, when you know you can't take it, just tell me. Making a letter is easier than seeing you like this. Alright?"
    dhannica_i "She's right."
    dhannica_i "But she doesn't know how it would feel like to be alone because everyone already has their own circle and I'm left with no one..."
    dhannica_i "But I do admit that pushing this was too far."
    dhannica "Yes Mom."
    "You just put up a silly little smile to hide your feelings. She smiles back at you."
    doctor "There, all done."
    "You look down and see your foot all wrapped up, and your pinky toe casted to prevent anymore damage."
    doctor "The damage wasn't that severe. Although there was a slight dislocation, it wasn't much to have caused actual damage that would take too much time to heal."
    dhannica_i "Phew, thank goodness."
    doctor "Although you're going to have to wear that for 2 weeks."
    dhannica_i "Two weeks?"
    dhannica "{sc}Two weeks?{/sc} So I'd have to miss school for two weeks?" with vpunch
    doctor "Not necessarily. You can rest for a week."
    doctor "You can then proceed to attending your classes. But you'd still have the cast on the remaining week if you choose to attend school."
    doctor "A week would be enough time for your injury to recover a bit for you to be able to move around."
    dhannica_i "So I can go back to school after a week."
    dhannica_i "Great, a week."
    dhannica_i "This is much worse than what I wanted to avoid. Just great."
    girlMom "You heard the doctor. No movements and no going outside for a week."
    dhannica "Yes Mom, I'm right here."
    dhannica_i "And no chores for me for a week~"
    girlMom "Alright, let's not get sassy. You still have chores."
    dhannica "Oh come on Mom! What chore can I do while sitting down?"
    girlMom "Oh, there's tons. Folding clothes, hanging up the laundry, cleaning your room..."
    dhannica "While sitting down? How can I possibly clean my room while sitting down?"
    girlMom "Clean your bed, at least.{w=0.1}{nw}" with vpunch
    girlMom "Your bed is a mess.{w=0.1}{nw}" with vpunch
    girlMom "There's piles of clothes all over.{w=0.1}{nw}" with vpunch
    girlMom "How can you sleep with all th-{w=0.1}{nw}" with vpunch
    stop ambient fadeout 1.0
    window hide(None)
    pause 2.5
    window auto
    "There was a moment of brief silence."
    "You forgot about the doctor being present in the room and noticed him listening to both of you bickering about chores."
    dhannica "S-sorry, where are my manners."
    girlMom "Doctor, if you may."
    play ambient hospital volume 0.2 fadein 1.0
    doctor "Oh! Yes."
    "The doctor begins to scribble down your prescription meds."
    doctor "Bring this down to the pharmacy downstairs. These are just pain killers to help with the pain."
    doctor "Because that's going to get worse before it gets better. So she's really going to need it."
    dhannica_i "Wow. I'm getting pretty terrified about what's to come."
    if Main == "Dhannica":
        girlMom "Alright, Dhanni, no more arguments. You need to rest."
    else:
        girlMom "Alright, no more arguments. You need to rest."
    "You nodded, understanding the concern in her voice."
    "The doctor handed the prescription, and both of you left the hospital."
    stop ambient fadeout 3.0
    scene bg living room with long_dissolve

    if beLate:
        "The week at home gave you ample time to think about Nick."
        "Depending on your earlier choice, your thoughts about him varied between curiosity and cautious dismissal."
        menu:
            dhannica_i "Maybe..."
            "\"There's more to Nick than meets the eye.\"":
                $ Nick.add(4)
            "\"I shouldn't read too much into it. He was probably just being polite.\"":
                $ Nick.remove(2)
        dhannica_i "Ah nevermind about that. Who knows, only time will tell on what truly is he."

    else:
        "The first couple of days at home were a mix of boredom and restlessness."
        "You couldn't help but think about school and how everyone was getting along without you."
        "Your phone buzzed occasionally with messages from Alec, each one a reminder of the friendship that was just beginning to form."
        phone_alec "Hey, how's the foot? Surviving the boredom?"
        "You smiled at his message."
        phone_dhannica "Barely. I'm officially a professional couch potato now."
        "A small laughing emoji react surfaces below your message."
        phone_alec "Hey, I'm planning to drop by in your house with some class notes and stuff. Is that cool?"
        dhannica_i "Oh crap! Already?"
        dhannica_i "But, this would be fine, right?"
        dhannica_i "I get to study my missed discussions with someone, but I can just grab the modules online and study alone..."

        menu:
            dhannica_i "What should I reply?"
            "\"That'd be great, actually.\"":
                $ a_hangOut = True
                $ Alec.add(5)
                phone_dhannica "That'd be great, actually."
                phone_alec "Alright! I'll see you there."
                dhannica_i "I don't know if Mom will let me bring a guy over to our house..."
                dhannica_i "Hopefully Mom would understand, right?"
                scene bg living room with long_dissolve
                play music meet fadein 4.0
                "It's been a few hours since you've invited him."
                dhannica_i "It's good that Mom understood the assignment."
                dhannica_i "But she'll be monitoring us, which I completely understand."
                play sound knock
                "Finally, a knock can be heard from the door."
                alec "[Main]? I'm here."
                alec "You know what, I'll just let myself in, I don't want you to walk here limping to open the door for me."
                "Alec came in with a stack of notes and some snacks, and a USB drive."#.with his band's music."
                show alec at trans3
                alec "Thought this might cheer you up a bit."
                dhannica "What's with the USB drive?"
                alec "Binge-music. I forgot to mention to you I play in a band, so I have copies of our session."
                alec "Hope you don't mind if I play it while we study, right?"
                "Your eyes enlargen for a while."
                dhannica_i "A band? Come to think of it, it kind of reminded me of the band I saw in my dream."
                dhannica_i "Alec was wearing the same clothes from the guy in my dream."
                dhannica_i "And he had green eyes."
                dhannica_i "So does Alec..."
                dhannica_i "That can't be it..."
                dhannica_i "Can it?"
                dhannica "A band?"
                alec "Yeah, here. I'll play it for you."
                alec "But first, let's study your missed discussions."
                scene bg living room with long_dissolve
                "You spent the afternoon going over class notes, sharing stories, and listening to music."
                "His company was a pleasant distraction from the monotony of being at home."
                show alec at trans3
                alec "You seem to be holding up well. Glad to see that."
                dhannica "Thanks to you. This visit really brightened up my day."
                alec "Well, I should get going. It's getting dark."
                dhannica "Yeah... take care on your way out."
                alec "You too, take care."
                hide alec at trans3
                stop music fadeout 2.0
                "Alec packs up his things and leaves your house."
                girlMom "So, is this a new boyfriend?~"
                dhannica "Ew Mom. We're just friends."
                girlMom "Alright, if you say so."

            "\"I appreciate it, but I think I need some time alone.\"":
                $ Alec.remove(2)
                phone_dhannica "I appreciate it, but I think I need some time alone."
                phone_alec "Ah, I see."
                phone_alec "No worries, I get it. I'll just send it here."
                phone_alec "Rest up, and let me know if you need anything."
                "Although you needed the solitude, part of you regretted not accepting his offer."
                "It felt like a missed opportunity to strengthen your budding friendship with him."
                "Whether he visited or not, you found yourself reflecting on the new friendship that was forming."
                "Alec's thoughtfulness was evident, but you couldn't help but feel curious about the other students, especially those you hadn't had a chance to connect with yet."
                dhannica_i "Hopefully turning down his offer was the right thing to do..."

    scene bg school hallway with long_dissolve
    show screen time_intermission("{size=+15}A week later...")
    play ambient schoolhallway fadein 1.0 volume 0.4
    "You prepared yourself mentally to return to school."
    "You're curious about how your interactions with the others would develop."
    dhannica_i "I hope everything goes well."
    hide screen time_intermission
    show alec at trans3
    alec "Hey [Main]."
    "On your first day back, you are greeted with warm welcomes. Alec was particularly supportive."
    menu:
        alec "Great to see you back. Need help getting to class?"
        "\"Thanks, but I can manage.\"":
            $ Alec.remove(2)
            dhannica "Thanks, Alec, but I can manage on my own."
            "Alec gave a nod of understanding, though you could tell he was slightly disappointed."
            alec "Alright, just let me know if you change your mind."
            hide alec at trans3
            "As Alec walked away, you took a deep breath and continued down the hallway. Despite the discomfort, you were determined to handle things on your own."
            "But then, a sharp pain shot through your foot, causing you to wince."
            if beLate:
                "That's when you noticed Nick approaching. His timing was almost uncanny."
            else:
                "That's when you noticed someone familiar approaching. His timing was almost uncanny."

            show nick at trans3
            nick "Hey, you're back. How's the foot?"
            "Caught off guard by his sudden appearance and the concern in his voice, you hesitated for a moment."
            dhannica "It's getting there, thanks. Just trying to, you know, manage."

            if not beLate:
                dhannica "Uhh..."
                $ meetNick = True
                $ n_name = "Nick"
                $ update_journal("Character added.")
                nick "Nick."

            nick "Looks like you could use a hand. Mind if I walk with you to your next class?"
            "You were surprised by his offer. Despite your initial intent to manage on your own, you found yourself nodding."
            dhannica "Sure, thanks, Nick."
            $ Nick.add(3)
            "As you both walked, the pain in your foot became more bearable, not just because of the physical support, but also due to the unexpected companionship."
            if beLate:
                "Nick's presence, once a source of annoyance, now offered a different kind of comfort."

        "\"I'd appreciate that, thanks.\"":
            $ Alec.add(3)
            dhannica "I'd appreciate that, thanks."
            "Walking with Alec through the halls, you felt a sense of comfort. His support was reassuring."
            alec "Just give me a shout if you need anything, okay?"
            if not beLate:
                dhannica "Thanks, Alec. I didn't realize how much I'd miss school until I couldn't come."
                "He chuckled, and for a moment, you saw a different side of him. Not just the helpful classmate but someone who could become a close friend."
            else:
                dhannica "Thanks, Alec."
                "He chuckled for a moment."
            alec "Well, if you need a recap of what you've missed or just someone to hang with during lunch, I'm here."
            "His offer made you smile, a genuine sense of gratitude welling up inside you."
            dhannica "I might take you up on that. Thanks again, Alec."
            "You felt a newfound appreciation for his friendship. It was nice that you had someone like Alec at school."

    stop ambient fadeout 1.0

label classroom2:
    scene bg classroom with blur_fadehold
    play ambient classroom fadein 1.0 volume 0.2
    "Settling into your seat, with the remnants of pain in your foot, your thoughts drifted back to the dream you had before the start of school."
    if a_hangOut:
        dhannica_i "I wonder if that was Alec. He did say he was in a band after all."
        dhannica_i "There's no mistaking it."
        dhannica_i "The singer with the paper bag mask, and those vividly green eyes."
    "It felt surreal, almost a premonition of the complexities you were now facing in your waking life."
    "Alec, sitting next to you, leaned in with a whisper, breaking your reverie."
    alec "You sure you're okay? You seem a bit... distant."
    dhannica "Oh! U-uh..."
    "You hesitated, feeling the weight of your thoughts."

    if not beLate:
        menu:
            dhannica_i "Should I reveal it to him?"
            "Tell him about the dream":
                $ Alec.add(2)
                dhannica "Y-Yeah, just a strange dream about a concert. It popped back in my mind."
                "His eyes lit up with curiosity."
                alec "A dream about a concert? Sounds interesting. Care to share more?"
                dhannica "O-okay, so it went like this..."
                scene bg classroom with long_dissolve
                "You found yourself opening up about the dream, describing about the mysterious singer and the emotional intensity of the experience."
                "However, you left the part about the color of the eyes that you found mesmerizing."
                "During your explanation, Alec listened intently, nodding along."
                "There were times where Alec found it confusing, but it's understandable given that dreams tend to not make sense."
                alec "Sounds like a powerful dream. Maybe it means something important about your life right now."
                alec "You explaining the dream in great detail tells me that this could be destiny, haha."
                alec "It must have taken a sharp mind to remember it all in detail."
                dhannica "Well, I keep a journal to my side always, so I won't forget them after I wake up."
                alec "That's even better. You know, you could piece your dreams together and hope for some miracle to happen."
                dhannica "That only happens in movies, haha."
                alec "Well either way, your dream sounds interesting."
                dhannica "Yeah..."
                "His positive response encouraged you to ponder the deeper significance of your dream."
                dhannica_i "Maybe I should keep an eye to that."
            "Keep it to yourself":
                label .keepit:
                    dhannica "I'm fine, just a bit tired. Thanks for asking."
                    alec "Alright, just letting you know I'm here if you need to talk."
                    "You appreciated his respect for your privacy, and it made you feel more at ease knowing you had a friend like Alec in class."
                    "As the lesson began, you found yourself splitting your attention between the professor's words and your lingering thoughts about the dream."
                    "You couldn't quite decipher its meaning behind the paperbag mask of the singer."
                    if not beLate:
                        dhannica_i "The resemblance is there..."
                        dhannica_i "Green eyes. Alec has those."
                        if a_hangOut:
                            dhannica_i "He also plays in a band, though I'm not sure if he's the singer or just the bassist."
                        "You continued to wander through your thoughts."
                    dhannica_i "Oh, what the heck. I'll just forget it."
    
    else:
        jump .keepit

    stop ambient fadeout 1.0
    scene bg classroom2 with long_dissolve

    "The day finally concluded."
    "The room slowly began to empty itself as everyone leaves."
    "You find yourself thinking what should you do after class."

    if not meetNick:
        jump .goAlec

    else:
        menu:
            dhannica "Let's see..."
            "Go with Alec":
                label .goAlec:
                    dhannica "I guess I'll go with Alec."
            "Go with Nick" if meetNick:
                dhannica "I guess I'll go with Nick."
                scene bg school hallway with blur_dissolve

    

    block "END"
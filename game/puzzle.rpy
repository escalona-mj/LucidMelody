init python:
    def setup_puzzle():
        for i in range(page_pieces):
            start_x = 1200
            start_y = 200
            end_x = 1700
            end_y = 800
            rand_loc = (renpy.random.randint(start_x, end_x), renpy.random.randint(start_y, end_y))
            initial_piece_coordinates.append(rand_loc)

    def piece_drop(dropped_on, dragged_piece):
        
        if dragged_piece[0].drag_name == dropped_on.drag_name:
            dragged_piece[0].snap(dropped_on.x, dropped_on.y)
            dragged_piece[0].draggable = False
            store.finished_pieces += 1

            if finished_pieces == page_pieces:
                renpy.restart_interaction()
                renpy.call("assemble_complete")

default page_pieces = 12
default full_page_size = (711, 996)
default piece_coordinates = [(451, 149), (719, 139), (868, 238), (421, 399), (658, 318), (700, 488), (796, 538), (453, 718), (776, 773), (464, 925), (743, 958), (921, 888)]
default initial_piece_coordinates = []
default finished_pieces = 0

screen reassemble_puzzle():
    on "show" action Function(renpy.show_layer_at, withBlur, layer="master"), Play("sfx3", "audio/sfx/page.ogg")
    on "hide" action Function(renpy.show_layer_at, noBlur, layer="master")
    frame:
        background None
        # background Frame("gui/test_frame.png")
        xysize full_page_size

    draggroup:
        at slideup(100)
        for i in range(page_pieces):
            drag:
                drag_name i
                pos initial_piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                drag_raise True
                image "images/Pieces/piece-%s.png" % (i + 1)
                
        for i in range(page_pieces):
            drag:
                drag_name i
                draggable False
                droppable True
                dropped piece_drop
                pos piece_coordinates[i]
                anchor(0.5, 0.5)
                focus_mask True
                image "images/Pieces/piece-%s.png" % (i + 1) alpha 0.1

transform dark_tint:
    matrixcolor TintMatrix(Color(rgb=(0.2353, 0.1882, 0.3961)))*BrightnessMatrix(-0.02)

label puzzle_test:
    $ Main = persistent.playername
    $ n_name = "Nick"
    camera at dark_tint
    scene bg school hallway
    play ambient night volume 0.1 fadein 1.0
    with blur_fade
    window auto
    "The moon hung low in the night sky, casting a silvery glow over the school grounds."
    dhannica_i "M-maybe this was a bad idea..."
    "Tonight was the night you had chosen to infiltrate the school, armed with nothing but curiosity towards Nick."
    dhannica_i "There's no way he would do that... right?"
    "As you tiptoed through the empty hallways, you heard a faint rustling coming from one of the classrooms."
    scene bg classroom2
    show nick:
        xalign 0.25
        yalign 1.0
        matrixcolor BrightnessMatrix(-1) blur 30
    with blur_fade
    "You instinctively pressed yourself against the wall and peeked through the slightly ajar door."
    show nick:
        ease 1.0 xalign 0.5
    "In the dim light, you saw a figure, hunched over a desk, tearing sheets of paper with an intensity that seemed almost desperate."
    show nick eyeclose:
        ease 1.0 xalign 0.75 matrixcolor BrightnessMatrix(0) blur 0
        easein .1 yoffset 20
        easeout .1 yoffset 0
    "As the figure moves pass at the dim light shining from the moon, a familiar face emerges."
    show nick eyelook
    "It's... Nick?"
    dhannica_i "What's he doing here?"
    show nick:
        ease_back 2.0 offscreenright
    "Curiosity overpowering caution, you waited until Nick hastily gathered the torn pieces and slipped out of the room."
    hide nick
    "Fortunately, you managed to remain out of sight even after he unknowingly passes by at your side."
    "As he left, you switfly darted inside, scanning the remnants that were left scattered across the desk."
    "You picked up a few pieces, each containing fragments of what appeared to be a handwritten note."
    "You pulled out a small flashlight from your backpack and began to examine each torn edge."
    dhannica_i "Let's see..."
    $ setup_puzzle()
    call screen reassemble_puzzle
    return

label assemble_complete:
    if not config.developer:
        $ renpy.block_rollback()
    # hide screen reassemble_puzzle
    "You look at the paper."
    show expression "images/Pieces/full-page.png" as paper:
        xalign 0.5
        parallel:
            slideup(50)
    "The scribbled handwriting on the neatly reconstructed paper suggested a message of some importance."
    "It was clear that Nick had gone to great lengths to keep whatever it was a secret."
    hide paper at slidedown(50)
    "Just as you finished reconstructing the note, you heard footsteps approaching the classroom."
    dhannica_i "Oh crap! Someone's coming!"
    "Panic surged through your whole body. But even with little time, you managed to slip the reassembled message into your pocket."
    show nick browsus at trans3
    "The door creaked open, revealing Nick with an expression of surprise and suspicion."
    nick "[Main]? What are you doing here?"
    # dhannica "I... uh, heard some strange noises and thought I'd check it out."
    $ renpy.end_replay()
    return
transform dust_blur:
    blur 3
    linear 1.0 alpha 0.5
    linear 2.0 alpha 0.0
    repeat

transform dust:
    zoom .5
    linear 1.0 alpha 0.0
    linear 5.0 alpha 1.0
    repeat

image dust_particle = SnowBlossom(At("gui/menu/particle.png", dust), count=10, border=150, xspeed=(0, -10), start=10, fast=False, horizontal=False)
image dust_particle_blur = SnowBlossom(At("gui/menu/particle.png", dust_blur), border=150, count=10, start=0.00000000001, fast=False,  yspeed=(-100, -80),  xspeed=(-200,200), horizontal=False)

image dream1_cg_scene1_singer = "images/cg/cg_dream1/dream1_cg_scene1_singer.png"

image dream1_cg_scene2 = "images/cg/cg_dream1/dream1_cg_scene2.png"
image dream1_cg_scene2_light = "images/cg/cg_dream1/dream1_cg_scene2_light.png"
image dream1_cg_scene2_dhannica = "images/cg/cg_dream1/dream1_cg_scene2_dhannica.png"
image dream1_cg_scene2_singer = "images/cg/cg_dream1/dream1_cg_scene2_singer.png"

image dream1_cg_scene3 = "images/cg/cg_dream1/dream1_cg_scene3.png"
image dream1_cg_scene3_hand = "images/cg/cg_dream1/dream1_cg_scene3_hand.png"
image dream1_cg_scene3_light = "images/cg/cg_dream1/dream1_cg_scene3_light.png"

image dream1_cg_scene4 = "images/cg/cg_dream1/dream1_cg_scene4.png"
image dream1_cg_scene4_dhannica = "images/cg/cg_dream1/dream1_cg_scene4_dhannica.png"
image dream1_cg_scene4_light = "images/cg/cg_dream1/dream1_cg_scene4_light.png"
image dream1_cg_scene4_singer = "images/cg/cg_dream1/dream1_cg_scene4_singer.png"

image dream1_cg_scene5 = "images/cg/cg_dream1/dream1_cg_scene5.png"
image dream1_cg_scene5_light = "images/cg/cg_dream1/dream1_cg_scene5_light.png"
image dream1_cg_scene5_both = "images/cg/cg_dream1/dream1_cg_scene5_both.png"

image dream1_cg_part1 = Composite(
    (1920, 1080),
    (0, 0), "dream1_cg_scene5",
    (550, 136), "dream1_cg_scene1_singer")

image dream1_cg_part2 = Composite(
    (1920, 1080),
    (0, 0), "dream1_cg_scene2",
    (0, 0), At("dream1_cg_scene2_light", pulse))

image dream1_cg_part2_2 = Composite(
    (1920, 1080),
    (0, 0), "dream1_cg_scene2",
    (0, 0), At("dream1_cg_scene2_light", pulse),
    (0, 0), "dream1_cg_scene2_dhannica",
    (0, 0), "dream1_cg_scene2_singer")

image dream1_cg_part3 = Composite(
    (1920, 1080),
    (0, 0), "dream1_cg_scene3",
    (600, 0), "dream1_cg_scene3_hand",
    (0, 0), "dream1_cg_scene3_light")

image dream1_cg_part4 = Composite(
    (1920, 1080),
    (0, 0), "dream1_cg_scene4",
    (100, 146), "dream1_cg_scene4_dhannica",
    (0, 0), At("dream1_cg_scene4_light", pulse),
    (969, 0), "dream1_cg_scene4_singer")

image dream1_cg_part5 = Composite(
    (1920, 1080),
    (0, 0), "dream1_cg_scene5",
    (650, 96), "dream1_cg_scene5_both",
    (0, 0), At("dream1_cg_scene5_light", pulse))

image dhannica_gojo_bg = "images/cg/cg_extras/dhannica_gojo_bg.png"

image dhannica_gojo_blink:
    "images/cg/cg_extras/dhannica_gojo_eye_open.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/cg/cg_extras/dhannica_gojo_eye_close.png"
    .10
    repeat

image dhannica_gojo_light = "images/cg/cg_extras/dhannica_gojo_light.png"

transform pulse_bright:
    alpha 1.0
    choice:
        ease 2.0 alpha 0.5
    choice:
        ease 4.0 alpha 0.5
    choice:
        ease 1.0 alpha 0.8
    choice:
        ease 10 alpha 0.2
    ease 7 alpha 1.0
    repeat

image dirt_overlay:
    "images/cg/cg_extras/dirt_overlay.png"
    alpha 0.75
image nah = "images/cg/cg_extras/nah.png"

image cg_dhannica_gojo = Composite(
    (1920, 1080),
    (0, 0), "dhannica_gojo_bg",
    (0, 0), "dhannica_gojo",
    (0, 0), At("dhannica_gojo_light", pulse_bright),
    (0, 0), At("dirt_overlay", pulse_bright))

image cg_dhannica_gojo_nah = Composite(
    (1920, 1080),
    (0, 0), "cg_dhannica_gojo",
    (1100, 150), "nah")

layeredimage dhannica_gojo:
    group base: #body
        attribute base default:
            "images/cg/cg_extras/dhannica_gojo_base.png"
    group eyes:
        attribute blink default:
            "dhannica_gojo_blink"
        attribute eyeclose:
            "images/cg/cg_extras/dhannica_gojo_eye_close.png"
    group accesories:
        attribute glasses default:
            "images/cg/cg_extras/dhannica_gojo_glasses.png"


image cg_nick_busstop_blink:
    "images/cg/cg_nick/cg_nicknoBlink_busstop.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "images/cg/cg_nick/cg_nickBlink_busstop.png"
    .10
    repeat

image cg_nick_busstop = Composite(
    (1920, 2160),
    (0, 0), "images/cg/cg_nick/cg_nick_busstop.png",
    (0, 0), "cg_nick_busstop_blink"
)

image cg_nick_bus = "images/cg/cg_nick/cg_nick_bus.png"
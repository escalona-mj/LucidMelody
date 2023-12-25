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

image dream_cg_scene1 = "images/cg/dream_cg_scene1.png"
image dream_cg_scene2 = "images/cg/dream_cg_scene2.png"
image dream_cg_scene2_light = "images/cg/dream_cg_scene2_light.png"
image dream_cg_scene2_dhannica = "images/cg/dream_cg_scene2_dhannica.png"
image dream_cg_scene2_singer = "images/cg/dream_cg_scene2_singer.png"
image dream_cg_scene3 = "images/cg/dream_cg_scene3.png"
image dream_cg_scene3_hand = "images/cg/dream_cg_scene3_hand.png"
image dream_cg_scene3_light = "images/cg/dream_cg_scene3_light.png"
image dream_cg_scene4 = "images/cg/dream_cg_scene4.png"
image dream_cg_scene4_light = "images/cg/dream_cg_scene4_light.png"
image dream_cg_scene4_dhannica = "images/cg/dream_cg_scene4_dhannica.png"
image dream_cg_scene4_singer = "images/cg/dream_cg_scene4_singer.png"
image dream_cg_scene5 = "images/cg/dream_cg_scene5.png"
image dream_cg_scene5_light = "images/cg/dream_cg_scene5_light.png"
image dream_cg_scene5_both = "images/cg/dream_cg_scene5_both.png"
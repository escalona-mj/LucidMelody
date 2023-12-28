init python:
    cg_gallery_items = [
    "dream1_cg_part1", "dream1_cg_part2", "dream1_cg_part3", "dream1_cg_part4", "dream1_cg_part5"
    ]

    cg_galleryrows = 2
    cg_gallerycols = 3

    thumbnail_x = 380
    thumbnail_y = 213

    cg_gallery = Gallery()

    cg_gallery.transition = Dissolve(0.2)

    cg_gallery.button("dream1_cg_part1")
    cg_gallery.unlock_image("dream1_cg_part1")

    cg_gallery.button("dream1_cg_part2")
    cg_gallery.unlock_image("dream1_cg_part2")
    cg_gallery.unlock_image("dream1_cg_part2_2")

    cg_gallery.button("dream1_cg_part3")
    cg_gallery.unlock_image("dream1_cg_part3")

    cg_gallery.button("dream1_cg_part4")
    cg_gallery.unlock_image("dream1_cg_part4")

    cg_gallery.button("dream1_cg_part5")
    cg_gallery.unlock_image("dream1_cg_part5")

transform resize_thumb:
    zoom 0.2

image dream1_cg_scene1_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part1", resize_thumb), "gui/gallery/slot_mask.png"))
image dream1_cg_scene2_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part2", resize_thumb), "gui/gallery/slot_mask.png"))
image dream1_cg_scene3_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part3", resize_thumb), "gui/gallery/slot_mask.png"))
image dream1_cg_scene4_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part4", resize_thumb), "gui/gallery/slot_mask.png"))
image dream1_cg_scene5_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part5", resize_thumb), "gui/gallery/slot_mask.png"))

screen cg_gallery():
    tag menu
    use extras_game_menu("CG Gallery"):
        grid cg_gallerycols cg_galleryrows:
            spacing 20
            add cg_gallery.make_button(name="dream1_cg_part1", unlocked="dream1_cg_scene1_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
            add cg_gallery.make_button(name="dream1_cg_part2", unlocked="dream1_cg_scene2_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
            add cg_gallery.make_button(name="dream1_cg_part3", unlocked="dream1_cg_scene3_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
            add cg_gallery.make_button(name="dream1_cg_part4", unlocked="dream1_cg_scene4_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
            add cg_gallery.make_button(name="dream1_cg_part5", unlocked="dream1_cg_scene5_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
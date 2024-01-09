init python:
    galleryrows = 4
    gallerycols = 3

    thumbnail_x = 380
    thumbnail_y = 213

    cg_gallery = Gallery()

    #allow navigation
    cg_gallery.navigation = True

    #add transition
    cg_gallery.transition = Dissolve(0.2)

    cg_gallery.button("dream1_cg_part1")
    cg_gallery.unlock_image("dream1_cg_part1")

    cg_gallery.button("dream1_cg_part2")
    cg_gallery.unlock_image("dream1_cg_part2")
    cg_gallery.unlock_image("dream1_cg_part2_2")

    cg_gallery.button("dream1_cg_part3")
    cg_gallery.image("dream1_cg_part3", "dust_particle")
    cg_gallery.unlock("dream1_cg_part3")

    cg_gallery.button("dream1_cg_part4")
    cg_gallery.unlock_image("dream1_cg_part4")

    cg_gallery.button("dream1_cg_part5")
    cg_gallery.unlock_image("dream1_cg_part5")


    #EXTRAS
    extras_gallery = Gallery()

    #allow navigation
    extras_gallery.navigation = True

    #add transition
    extras_gallery.transition = Dissolve(0.2)

    extras_gallery.button("cg_dhannica_gojo")
    extras_gallery.unlock_image("cg_dhannica_gojo", "dust_particle")
    extras_gallery.unlock_image("cg_dhannica_gojo_nah", "dust_particle")

    extras_gallery.button("extras_dhannica_gojo")
    extras_gallery.image("images/cg/cg_extras/dhannica_gojo.png")
    extras_gallery.unlock("cg_dhannica_gojo")

    extras_gallery.button("new_year_special")
    extras_gallery.image("images/cg/cg_extras/new_year_artwork.png")


transform resize_thumb:
    xsize thumbnail_x
    ysize thumbnail_y

transform zoom_thumb:
    zoom 0.6
    truecenter

default which_gallery = "cg_gallery"

screen gallery():
    tag menu

    use extras_game_menu("Gallery", withMargin=False):
        showif which_gallery == "cg_gallery":
            use cg_gallery 
        showif which_gallery == "extras_gallery":
            use extras_gallery
    
    fixed:
        vbox:
            style_prefix "gal_nav"
            xalign 0.02
            yalign 0.5
            imagebutton:
                auto "gui/navigation/blank_%s.png"
                foreground Text(_("General"), style="gal_nav_btn")
                hover_foreground Text(_("General"), style="gal_nav_btn_hover")
                selected_foreground Text(_("General"), style="gal_nav_btn_selected")
                action [SetScreenVariable("which_gallery", "cg_gallery"), SelectedIf(which_gallery == "cg_gallery")]
            imagebutton:
                auto "gui/navigation/blank_%s.png"
                foreground Text(_("Extras"), style="gal_nav_btn")
                hover_foreground Text(_("Extras"), style="gal_nav_btn_hover")
                selected_foreground Text(_("Extras"), style="gal_nav_btn_selected")
                action [SetScreenVariable("which_gallery", "extras_gallery"), SelectedIf(which_gallery == "extras_gallery")]

style gal_nav_image_button is button

style gal_nav_btn:
    color gui.accent_color
    xalign 0.5
    text_align 0.5
    font gui.interface_text_font
    size gui.interface_text_size

style gal_nav_btn_hover is gal_nav_btn:
    color gui.interface_text_color

style gal_nav_btn_selected is gal_nav_btn_hover

image dream1_cg_scene1_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part1", resize_thumb), "gui/gallery/slot_mask.png"))
image dream1_cg_scene2_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part2", resize_thumb), "gui/gallery/slot_mask.png"))
image dream1_cg_scene3_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part3", resize_thumb), "gui/gallery/slot_mask.png"))
image dream1_cg_scene4_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part4", resize_thumb), "gui/gallery/slot_mask.png"))
image dream1_cg_scene5_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("dream1_cg_part5", resize_thumb), "gui/gallery/slot_mask.png"))

screen cg_gallery():
    grid gallerycols galleryrows:
        spacing 20
        add cg_gallery.make_button(name="dream1_cg_part1", unlocked="dream1_cg_scene1_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
        add cg_gallery.make_button(name="dream1_cg_part2", unlocked="dream1_cg_scene2_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
        add cg_gallery.make_button(name="dream1_cg_part3", unlocked="dream1_cg_scene3_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
        add cg_gallery.make_button(name="dream1_cg_part4", unlocked="dream1_cg_scene4_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
        add cg_gallery.make_button(name="dream1_cg_part5", unlocked="dream1_cg_scene5_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")

image cg_dhannica_gojo_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("cg_dhannica_gojo", resize_thumb), "gui/gallery/slot_mask.png"))
image extras_dhannica_gojo_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("images/cg/cg_extras/dhannica_gojo.png", zoom_thumb), "gui/gallery/slot_mask.png"))
image new_year_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("images/cg/cg_extras/new_year_artwork.png", zoom_thumb), "gui/gallery/slot_mask.png"))

screen extras_gallery():
    grid gallerycols galleryrows:
        spacing 20
        if persistent.seen_dream1:
            add extras_gallery.make_button(name="cg_dhannica_gojo", unlocked="cg_dhannica_gojo_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
            add extras_gallery.make_button(name="extras_dhannica_gojo", unlocked="extras_dhannica_gojo_unlocked", hover_border="gui/gallery/slot_scene_hover.png", locked="gui/gallery/slot_scene_locked.png")
        add extras_gallery.make_button(name="new_year_special", unlocked="new_year_unlocked", hover_border="gui/gallery/slot_scene_hover.png")
    
default gal_navi = False

screen gallery_navigation:
    hbox:
        style_prefix "gallery_nav"
        align (0.98, 0.98)
        spacing 20
        at transform:
            alpha 0.2
        textbutton "Previous" action gallery.Previous()
        textbutton "Slideshow" action gallery.ToggleSlideshow()
        textbutton "Next" action gallery.Next()
        textbutton "Return" action gallery.Return()

style gallery_nav_button_text:
    color "#666"
    hover_color "#fff"
    selected_color "#fff"
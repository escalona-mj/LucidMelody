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

    extras_gallery.button("extras_dhannica_gojo")
    extras_gallery.image("gui/gallery/dhannica_gojo.png")


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
    
    use gallery_nav
    
screen gallery_nav():
    fixed:
        vbox:
            style_prefix "header"
            xalign 0.02
            yalign 0.5
            imagebutton:
                auto "gui/navigation/pref_general_%s.png"
                foreground Text(_("General"), style="header_btn")
                hover_foreground Text(_("General"), style="header_btn_hover")
                selected_foreground Text(_("General"), style="header_btn_selected")
                action [SetVariable("which_gallery", "cg_gallery"), SelectedIf(which_gallery == "cg_gallery")]
            imagebutton:
                auto "gui/navigation/pref_general_%s.png"
                foreground Text(_("Extras"), style="header_btn")
                hover_foreground Text(_("Extras"), style="header_btn_hover")
                selected_foreground Text(_("Extras"), style="header_btn_selected")
                action [SetVariable("which_gallery", "extras_gallery"), SelectedIf(which_gallery == "extras_gallery")]

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

image extras_dhannica_gojo_unlocked = Composite((380, 213), (0, 0), "gui/gallery/slot_scene_shadow.png", (0, 0), AlphaMask(At("gui/gallery/dhannica_gojo.png", zoom_thumb), "gui/gallery/slot_mask.png"))

screen extras_gallery():
    grid gallerycols galleryrows:
        spacing 20
        add extras_gallery.make_button(name="extras_dhannica_gojo", unlocked="extras_dhannica_gojo_unlocked", hover_border="gui/gallery/slot_scene_hover.png")
    
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
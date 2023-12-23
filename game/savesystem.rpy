image save_dhannica_indicator:
    "gui/save_indicator/save_dhannica_1.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "gui/save_indicator/save_dhannica_2.png"
    .10
    repeat

image save_alec_indicator:
    "gui/save_indicator/save_alec_1.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "gui/save_indicator/save_alec_2.png"
    .10
    repeat

image save_nick_indicator:
    "gui/save_indicator/save_nick_1.png"
    choice:
        4.5
    choice:
        3.5
    choice:
        1.5
    "gui/save_indicator/save_nick_2.png"
    .10
    repeat

init python:
    def save_indicator(data):
        data['route'] = current_route
        data['chapter'] = chapter
        data['ch_name'] = chapter_name
    config.save_json_callbacks = [save_indicator]            

transform save_hover:
    zoom 1.5
    crop (213, 100, config.thumbnail_width, config.thumbnail_height)
    linear 10 crop (213, 400, config.thumbnail_width, config.thumbnail_height)

    zoom 2.0
    crop (0, 352, config.thumbnail_width, config.thumbnail_height)
    linear 10 crop (625, 352, config.thumbnail_width, config.thumbnail_height)
    repeat

transform save_idle:
    zoom 1.5
    crop (213, 100, config.thumbnail_width, config.thumbnail_height)

default slot_selected = None

screen file_slots():
    tag menu

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu("Saves"):
    
        vbox:
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value
                

            vbox:
                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(3):

                    $ slot = i 

                    button:
                        xfill True
                        xsize 1250
                        ysize 200

                        frame:
                            background None 
                            add "gui/button/slot_shadow.png"
                            if FileLoadable(slot):
                                if slot_selected == slot:
                                    add AlphaMask(At(FileScreenshot(slot), save_hover),"gui/button/slot_mask.png")
                                    add "gui/button/slot_overlay.png"
                                else:
                                    add AlphaMask(At(FileScreenshot(slot), save_idle),"gui/button/slot_mask.png")
                            else:
                                add "gui/button/slot_idle.png"
                                text "empty slot" xalign 0.5 yalign 0.5 yoffset 10 color "#ffffff47" font gui.interface_text_font
                                if not main_menu:
                                    if slot_selected == slot:
                                        add "gui/button/slot_overlay.png"

                        if main_menu:
                            if FileLoadable(slot):
                                action SetScreenVariable("slot_selected", slot)
                            elif not FileLoadable(slot):
                                pass
                        else:
                            if ((FileLoadable(slot)) or (not FileLoadable(slot))):
                                action SetScreenVariable("slot_selected", slot)

                        frame:
                            background None
                            padding (25,25,25,25)
                            hbox:
                                xfill True
                                box_wrap_spacing 1250
                                vbox:
                                    yoffset 80
                                    $ cur_chap = FileJson(slot, key='chapter')
                                    $ cur_chap_name = FileJson(slot, key='ch_name')
                                    text FileTime(slot, format=_("{#file_time}%A | %m/%d/%y | %H:%M\nChapter [cur_chap]: [cur_chap_name]"), empty=_("")):
                                        style "slot_time_text"
                                    text FileSaveName(slot):
                                        style "slot_name_text"
                                hbox:
                                    yoffset 110
                                    xoffset 20
                                    xalign 1.0
                                    spacing 20
                                    style_prefix "load_save"
                                    if slot_selected == slot:
                                        if main_menu:
                                            if FileLoadable(slot):
                                                textbutton "LOAD" action FileLoad(slot)
                                        else:
                                            if FileLoadable(slot):
                                                textbutton "LOAD" action FileLoad(slot)
                                            textbutton "SAVE" action FileSave(slot)

                            $ cur_route = FileJson(slot, key='route')
                            if cur_route == 'common':
                                pass
                            elif cur_route == 'dhannica':
                                add 'save_dhannica_indicator' xpos 1085 ypos -25
                            elif cur_route == 'alec':
                                add 'save_alec_indicator' xpos 1085 ypos -25
                            elif cur_route == 'nick':
                                add 'save_nick_indicator' xpos 1085 ypos -25
                            
                            if slot_selected == slot:
                                if FileLoadable(slot):
                                    imagebutton auto "gui/button/delete_save_%s.png" action FileDelete(slot) xpos -25 ypos -25:
                                        activate_sound "audio/sfx/click.ogg"
                                        hover_sound "audio/sfx/hover.ogg"
                            

            ## Buttons to access other pages.
            null height 15
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}Q") action FilePage("quick")

                    ## range(1, 10) gives the numbers from 1 to 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
    
    fixed:
        vbox:
            xalign 0.025
            yalign 0.5
            style_prefix "header"
            if config.has_sync:
                imagebutton:
                    auto "gui/navigation/cloud_%s.png"
                    foreground Text(_("Cloud"), style="header_btn")
                    hover_foreground Text(_("Cloud"), style="header_btn_hover")
                    selected_foreground Text(_("Cloud"), style="header_btn_selected")
                    action Show("cloud_modal", message="What do you want to do with saves?", first_btn="Upload", first_action=UploadSync(), second_btn="Download", second_action=DownloadSync())
                    tooltip "Access your saves via cloud."
                
screen cloud_modal(message, first_btn, second_btn, first_action, second_action):
    on "show" action Play("sfx3", "audio/sfx/modal_open.ogg")

    modal True

    zorder 200

    dismiss action Hide()

    style_prefix "confirm"

    add "gui/overlay/confirm.png":
        at transform:
            on show:
                alpha 0.0
                easein .25 alpha 0.5
            on hide:
                alpha 0.5
                easein .25 alpha 0.0

    frame at screen_appear:
        has vbox:
            xalign .5
            yalign .5
            spacing 30
        label _(message):
            style "confirm_prompt"
            xalign 0.5
        hbox:
            xalign 0.5
            spacing 100

            imagebutton:
                auto "gui/navigation/confirm_btn_%s.png"
                foreground Text(first_btn, style="confirm_btn")
                hover_foreground Text(first_btn, style="confirm_btn_hover")
                selected_foreground Text(first_btn, style="confirm_btn_selected")
                action first_action

            imagebutton:
                auto "gui/navigation/confirm_btn_%s.png"
                foreground Text(second_btn, style="confirm_btn")
                hover_foreground Text(second_btn, style="confirm_btn_hover")
                selected_foreground Text(second_btn, style="confirm_btn_selected")
                action second_action

    key "game_menu" action Hide()

init -1:
    screen sync_confirm():
        on "show" action Play("sfx3", "audio/sfx/modal_open.ogg")

        modal True

        zorder 100

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:
            at screen_appear

            vbox:
                xalign .5
                yalign .5
                spacing 45

                label _("This will upload your saves to the {a=https://sync.renpy.org}Ren'Py Sync Server{/a}.\nDo you want to continue?"):
                    style "confirm_prompt"
                    xalign 0.5

                hbox:
                    xalign 0.5
                    spacing 150
                    imagebutton:
                        auto "gui/navigation/confirm_btn_%s.png"
                        foreground Text(_("Yes"), style="confirm_btn")
                        hover_foreground Text(_("Yes"), style="confirm_btn_hover")
                        selected_foreground Text(_("Yes"), style="confirm_btn_selected")
                        action Return(True)
                    imagebutton:
                        auto "gui/navigation/confirm_btn_%s.png"
                        foreground Text(_("No"), style="confirm_btn")
                        hover_foreground Text(_("No"), style="confirm_btn_hover")
                        selected_foreground Text(_("No"), style="confirm_btn_selected")
                        action Return(False)

        ## Right-click and escape answer "no".
        key "game_menu" action Return(False)

    screen sync_prompt(prompt):
        on "show" action Play("sfx3", "audio/sfx/modal_open.ogg")

        modal True

        zorder 100

        style_prefix "confirm"

        add "gui/overlay/confirm.png"
        
        frame:
            at screen_appear

            vbox:
                xalign .5
                yalign .5
                spacing 45

                vbox:
                    label _("Enter Sync ID"):
                        style "confirm_prompt"
                        xalign 0.5

                    text prompt:
                        xalign 0.5
                        textalign 0.5
                        color gui.accent_color
                    
                    null height 25
                    
                    input:
                        id "input"
                        xalign 0.5
                        yalign 0.5
                        color u'#000'
                        size 69
                    
                    null height 25

                    text _("This will contact the {a=https://sync.renpy.org}Ren'Py Sync Server{/a}."):
                        xalign 0.5
                        textalign 0.5
                        color gui.accent_color
                
                imagebutton:
                    xalign 0.5
                    auto "gui/navigation/confirm_btn_%s.png"
                    foreground Text(_("Return"), style="confirm_btn")
                    hover_foreground Text(_("Return"), style="confirm_btn_hover")
                    selected_foreground Text(_("Return"), style="confirm_btn_selected")
                    action Return("")

        ## Right-click and escape answer "no".
        key "game_menu" action Return(False)

    screen sync_success(sync_id):
        on "show" action Play("sfx3", "audio/sfx/modal_open.ogg")

        modal True

        zorder 100

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:
            at screen_appear

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 45

                vbox:
                    xalign 0.5
                    label _("Sync Success"):
                        style "confirm_prompt"
                        xalign 0.5

                    text _("The Sync ID is:"):
                        xalign 0.5
                        color gui.accent_color

                text sync_id:
                    xalign 0.5
                    color u'#000'
                    font gui.game_menu_label_font
                    size 69

                text _("You can use this ID to download your save on another device.\nThis sync will expire in an hour.\nRen'Py Sync is supported by {a=https://www.renpy.org/sponsors.html}Ren'Py's Sponsors{/a}."):
                    xalign 0.5
                    textalign 0.5
                    color gui.accent_color

                imagebutton:
                    xalign 0.5
                    auto "gui/navigation/confirm_btn_%s.png"
                    foreground Text(_("Continue"), style="confirm_btn")
                    hover_foreground Text(_("Continue"), style="confirm_btn_hover")
                    selected_foreground Text(_("Continue"), style="confirm_btn_selected")
                    action Return(True)

        ## Right-click and escape answer "no".
        key "game_menu" action Return(False)

    screen sync_error(message):
        on "show" action Play("sfx3", "audio/sfx/modal_open.ogg")

        modal True

        zorder 100

        style_prefix "confirm"

        add "gui/overlay/confirm.png"

        frame:
            at screen_appear

            vbox:
                xalign .5
                yalign .5
                spacing 45

                vbox:
                    label _("Sync Error"):
                        style "confirm_prompt"
                        xalign 0.5

                    text message:
                        xalign 0.5
                        textalign 0.5
                        color gui.accent_color

                imagebutton:
                    xalign 0.5
                    auto "gui/navigation/confirm_btn_%s.png"
                    foreground Text(_("Continue"), style="confirm_btn")
                    hover_foreground Text(_("Continue"), style="confirm_btn_hover")
                    selected_foreground Text(_("Continue"), style="confirm_btn_selected")
                    action Return(True)

        ## Right-click and escape answer "no".
        key "game_menu" action Return(False)

style load_save_button_text:
    properties gui.button_text_properties("load_save_button")
    # color "#fff"
    # font "fonts/MyPrettyCutie.ttf"

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is empty
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text:
    is slot_button_text

style slot_name_text:
    is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color
    outlines [(3, "#16161d", 0, 1)]

style page_button:
    properties gui.button_properties("page_button")
    activate_sound "audio/sfx/click.ogg"
    hover_sound "audio/sfx/hover.ogg"

style page_button_text:
    textalign 0.5
    selected_color '#c4c4c4'
    properties gui.button_text_properties("page_button")

# style slot_button:
#     properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
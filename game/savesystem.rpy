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
                            add "gui/phone/button/slot_shadow.png"
                            if FileLoadable(slot):
                                if slot_selected == slot:
                                    add AlphaMask(At(FileScreenshot(slot), save_hover),"gui/phone/button/slot_mask.png")
                                    add "gui/phone/button/slot_overlay.png"
                                else:
                                    add AlphaMask(At(FileScreenshot(slot), save_idle),"gui/phone/button/slot_mask.png")
                            else:
                                add "gui/phone/button/slot_idle.png"
                                text "empty slot" xalign 0.5 yalign 0.5 yoffset 10 color "#ffffff47"
                                if not main_menu:
                                    if slot_selected == slot:
                                        add "gui/phone/button/slot_overlay.png"

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
                                    style_prefix "load_save_btn"
                                    if slot_selected == i:
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
                            
                            if slot_selected == i:
                                if FileLoadable(slot):
                                    imagebutton auto "gui/phone/button/delete_save_%s.png" action FileDelete(slot) xpos -25 ypos -25:
                                        activate_sound "audio/sfx/click.mp3"
                            

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

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Upload Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Download Sync"):
                            action DownloadSync()
                            xalign 0.5


style load_save_btn_button_text:
    color "#fff"
    font "fonts/MyPrettyCutie.ttf"
    outlines [(5, "#16161d", 0, 2)]

style page_label is gui_label
style page_label_text is gui_label_text
style page_button is empty
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text:
    is slot_button_text
    outlines [(5, "#16161d", 0, 2)]

style slot_name_text:
    is slot_button_text
    outlines [(5, "#16161d", 0, 2)]

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color
    outlines [(5, "#16161d", 0, 2)]

style page_button:
    properties gui.button_properties("page_button")
    activate_sound "audio/sfx/click.mp3"

style page_button_text:
    textalign 0.5
    selected_color '#c4c4c4'
    properties gui.button_text_properties("page_button")
    outlines [(5, "#16161d", 0, 2)]

# style slot_button:
#     properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
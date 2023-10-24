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

## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():

    tag menu

    use file_slots(_("Save"))


screen load():

    tag menu

    use file_slots(_("Load"))

init python:
    def save_indicator(data):
        data['route'] = current_route
    config.save_json_callbacks = [save_indicator]            


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))

    use game_menu(title):
        
        vbox:
            ## This ensures the input will get the enter event before any of the
            ## buttons do.
            order_reverse True

            ## The page name, which can be edited by clicking on a button.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## The grid of file slots.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        null height 5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("unknown dream")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        $ cur_route = FileJson(slot, key='route')
                        if cur_route == 'common':
                            pass
                        elif cur_route == 'dhannica':
                            add 'save_dhannica_indicator' xpos 215 ypos -280
                        elif cur_route == 'alec':
                            add 'save_alec_indicator' xpos 215 ypos -280
                        elif cur_route == 'nick':
                            add 'save_nick_indicator' xpos 215 ypos -280

                        key "save_delete" action FileDelete(slot)

            ## Buttons to access other pages.
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


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is empty
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text:
    is slot_button_text
    color u'#000000'
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    textalign 0.5
    selected_color u'#a8a8a8'
    properties gui.button_text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.button_text_properties("slot_button")
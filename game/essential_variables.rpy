default current_route = 'common'
default persistent.first_gameplay = False
default persistent.seen_controls = False
default persistent.seen_lucid = False
default current_scene = None

default Main = ''
default persistent.playername = ''

#CHARACTER JOURNAL
define MC = CharInfo(
    char_name="[Main]",
    description="[dhannica_description]",
    mainChr=True,
    pic="journal_dhannica")

define Nick = CharInfo(
    char_name="[n_name]",
    description="[nick_description]",
    points="nick_likePoints",
    max_points="nick_likePointsMax",
    pic="journal_nick")

define Alec = CharInfo(
    char_name="[a_name]",
    description="[alec_description]",
    points="alec_likePoints",
    max_points="alec_likePointsMax",
    pic="journal_alec")

default all_chars = [MC, Nick, Alec]

default journal = False
default journal_entries = []
default current_page = "Journal" #set the default screen when opening the character book for the first time

default notify_journal = True
default first_page = 1
default second_page = 2

#DHANNICA VARIABLES
default meetDhannica = False
default beLate = False
default usePhone = False
default eatBreakfast = False
default dhannica_likePoints = 10
default dhannica_likePointsMax = 100
default dhannica_description = ""

#NICK VARIABLES
default meetNick = False
default n_takeIcedTea = False
default n_refuseIcedTea = False
default n_refuseTake = False
default n_takeFlask = False
default n_takeBus = False
default nick_likePoints = 10
default nick_likePointsMax = 100
default nick_description = ""

#ALEC VARIABLES
default meetAlec = False
default a_clinic = False
default a_hangOut = False
default alec_likePoints = 10
default alec_likePointsMax = 100
default alec_description = ""
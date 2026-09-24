# Character definitions

define p = Character("나", color="#d7e5ff")
define older = Character("서윤", color="#d7d0ff")
define friend = Character("하린", color="#ffd2dc")
define junior = Character("유나", color="#cbd6d8")
define prof = Character("교수", color="#dddddd")
define narrator = Character(None)

# Prototype images: current AI-generated character sheets.
# Later replace these with sprite sets while keeping the image names stable.
image older_sheet = "images/heroine1/character_sheet.png"
image friend_sheet = "images/heroine2/character_sheet.png"
image junior_sheet = "images/heroine3/character_sheet.png"
image older_fullbody_joy = "images/heroine1/fullbody_joy.png"
image friend_fullbody_joy = "images/heroine2/fullbody_joy.png"
image junior_fullbody_joy = "images/heroine3/fullbody_joy.png"
image older fullbody_default = "images/heroine1/fullbody_default.png"
image older fullbody_joy = "images/heroine1/fullbody_joy.png"
image older fullbody_shy = "images/heroine1/fullbody_shy.png"
image older fullbody_sadness = "images/heroine1/fullbody_sadness.png"
image older fullbody_surprise = "images/heroine1/fullbody_surprise.png"
image older fullbody_flustered = "images/heroine1/fullbody_flustered.png"
image older fullbody_hurt = "images/heroine1/fullbody_hurt.png"
image older fullbody_jealousy = "images/heroine1/fullbody_jealousy.png"
image older fullbody_anger = "images/heroine1/fullbody_anger.png"
image friend fullbody_default = "images/heroine2/fullbody_default.png"
image friend fullbody_joy = "images/heroine2/fullbody_joy.png"
image friend fullbody_shy = "images/heroine2/fullbody_shy.png"
image friend fullbody_sadness = "images/heroine2/fullbody_sadness.png"
image friend fullbody_surprise = "images/heroine2/fullbody_surprise.png"
image friend fullbody_flustered = "images/heroine2/fullbody_flustered.png"
image friend fullbody_hurt = "images/heroine2/fullbody_hurt.png"
image friend fullbody_jealousy = "images/heroine2/fullbody_jealousy.png"
image friend fullbody_anger = "images/heroine2/fullbody_anger.png"
image junior fullbody_default = "images/heroine3/fullbody_default.png"
image junior fullbody_joy = "images/heroine3/fullbody_joy.png"
image junior fullbody_shy = "images/heroine3/fullbody_shy.png"
image junior fullbody_sadness = "images/heroine3/fullbody_sadness.png"
image junior fullbody_surprise = "images/heroine3/fullbody_surprise.png"
image junior fullbody_flustered = "images/heroine3/fullbody_flustered.png"
image junior fullbody_hurt = "images/heroine3/fullbody_hurt.png"
image junior fullbody_jealousy = "images/heroine3/fullbody_jealousy.png"
image junior fullbody_anger = "images/heroine3/fullbody_anger.png"
image bg university_common = "images/bg_university_morning.png"
image bg event_harin_commute = "images/events/event_harin_commute.png"
image bg event_seoyun_office = "images/events/event_seoyun_office.png"
image bg event_yuna_classroom = "images/events/event_yuna_classroom.png"

transform sheet_fit:
    xalign 0.5
    yalign 0.5
    zoom 0.45

transform fullbody_fit:
    xalign 0.5
    yalign 1.0
    zoom 0.68

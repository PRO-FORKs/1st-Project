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
image bg university_common = "images/bg_university_morning.png"

transform sheet_fit:
    xalign 0.5
    yalign 0.5
    zoom 0.45

transform fullbody_fit:
    xalign 0.5
    yalign 1.0
    zoom 0.86

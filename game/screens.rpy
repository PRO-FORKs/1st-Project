################################################################################
## Self-contained prototype screens - Ren'Py 8.5
##
## This file intentionally avoids Ren'Py's generated GUI image assets and most
## gui.* variables, so the project can be extracted as a standalone project.
################################################################################

init offset = -1

init python:
    def choice_face_for_caption(caption):
        if "서윤" in caption:
            return "images/ui/choice_seoyun.png"
        if "하린" in caption:
            return "images/ui/choice_harin.png"
        if "유나" in caption:
            return "images/ui/choice_yuna.png"
        return None


transform choice_face_pop:
    on hover:
        zoom 1.08
    on idle:
        zoom 1.0

# ------------------------------------------------------------------------------
# Dialogue
# ------------------------------------------------------------------------------

screen say(who, what):
    window:
        id "window"
        xalign 0.5
        yalign 1.0
        xsize 1280
        ysize 190
        background Solid("#14110fcc")
        padding (48, 24)

        vbox:
            spacing 10

            if who is not None:
                text who:
                    id "who"
                    size 30
                    color "#f3b8a8"

            text what:
                id "what"
                size 27
                color "#fff7ed"
                line_spacing 6


screen input(prompt):
    modal True

    frame:
        xalign 0.5
        yalign 0.5
        xsize 900
        background Solid("#111827")
        padding (40, 32)

        vbox:
            spacing 20
            text prompt size 28 color "#f8fafc"
            input:
                id "input"
                size 28
                color "#ffffff"


screen choice(items):
    modal True

    add Solid("#07050444")

    vbox:
        xalign 0.5
        yalign 0.62
        xsize 940
        spacing 12

        for i in items:
            $ choice_face = choice_face_for_caption(i.caption)

            button:
                action i.action
                xfill True
                ysize 78
                background Solid("#16110de8")
                hover_background Solid("#7a4b3add")

                fixed:
                    xfill True
                    yfill True

                    add Solid("#d88a5a"):
                        xalign 0.0
                        yalign 0.5
                        xysize (5, 78)

                    text i.caption:
                        xalign 0.5
                        yalign 0.5
                        xmaximum 720
                        size 26
                        color "#fff7ed"
                        text_align 0.5
                        outlines [(1, "#140d09aa", 0, 1)]

                    if choice_face:
                        frame:
                            xalign 0.965
                            yalign 0.5
                            xysize (62, 62)
                            background Solid("#fff2e6")
                            padding (3, 3)

                            add choice_face at choice_face_pop:
                                xysize (56, 56)


screen chapter_transition(title, subtitle=""):
    modal True

    add "images/bg_university_morning.png":
        xysize (1280, 720)

    add Solid("#080504aa")

    frame:
        xalign 0.5
        yalign 0.48
        xsize 760
        background Solid("#15100ce8")
        padding (54, 44)

        vbox:
            xalign 0.5
            spacing 18

            text "NEXT CHAPTER":
                xalign 0.5
                size 20
                color "#e9a26d"
                bold True

            text title:
                xalign 0.5
                xmaximum 640
                size 44
                color "#fff7ed"
                text_align 0.5
                outlines [(2, "#2d160faa", 0, 2)]

            if subtitle:
                text subtitle:
                    xalign 0.5
                    xmaximum 600
                    size 22
                    color "#eac8b0"
                    text_align 0.5
                    line_spacing 5

            null height 16

            textbutton _("다음 챕터로 진행"):
                action Return()
                xalign 0.5
                xsize 340
                ysize 58
                background Solid("#b85f4a")
                hover_background Solid("#df7a56")
                text_size 24
                text_color "#fffaf4"
                text_xalign 0.5
                text_yalign 0.5


# ------------------------------------------------------------------------------
# Main menu / pause menu
# ------------------------------------------------------------------------------

screen main_menu():
    tag menu

    add "images/main_menu.png":
        xysize (1280, 720)

    add Solid("#0a060477")

    vbox:
        xalign 0.68
        yalign 0.2
        spacing 10

        text "복학생의 가을":
            xalign 0.5
            size 64
            color "#fff7ed"
            outlines [(3, "#2f1f18aa", 0, 3)]

        text "Campus Life Prototype":
            xalign 0.5
            size 24
            color "#ffd6ba"
            outlines [(1, "#2f1f1880", 0, 1)]

    frame:
        xalign 0.09
        yalign 0.56
        xsize 400
        background Solid("#130f0be8")
        padding (38, 36)

        vbox:
            xalign 0.5
            spacing 12

            text "[config.name]":
                xalign 0.5
                size 32
                color "#fff7ed"
                text_align 0.5
                outlines [(1, "#3b241a99", 0, 1)]

            text "다시 돌아온 캠퍼스에서 시작되는 세 갈래의 가을":
                xalign 0.5
                xsize 310
                size 18
                color "#e7c7ad"
                text_align 0.5
                line_spacing 4

            null height 16

            textbutton _("게임 시작"):
                action Start()
                xalign 0.5
                xsize 316
                ysize 62
                background Solid("#b85f4a")
                hover_background Solid("#d97757")
                text_size 26
                text_color "#fffaf4"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("불러오기"):
                action ShowMenu("load")
                xalign 0.5
                xsize 316
                ysize 56
                background Solid("#2a211bcc")
                hover_background Solid("#5f4638")
                text_size 24
                text_color "#fff7ed"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("종료"):
                action Quit(confirm=False)
                xalign 0.5
                xsize 316
                ysize 56
                background Solid("#2a211bcc")
                hover_background Solid("#5f4638")
                text_size 24
                text_color "#fff7ed"
                text_xalign 0.5
                text_yalign 0.5

# Ren'Py calls the game_menu screen for the ESC/menu context. Keep this screen
# intentionally simple and route to our save/load screens.
screen game_menu(title=None, scroll=None, yinitial=0.0, spacing=0):
    tag menu
    modal True

    add "images/bg_university_morning.png":
        xysize (1280, 720)

    add Solid("#120f0c99")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        background Solid("#17120ee6")
        padding (50, 44)

        vbox:
            xalign 0.5
            spacing 18

            text (title if title else _("게임 메뉴")):
                xalign 0.5
                size 42
                color "#fff7ed"

            textbutton _("돌아가기"):
                action Return()
                xalign 0.5
                xsize 390
                ysize 58
                background Solid("#2d241dcc")
                hover_background Solid("#5f4638")
                text_size 25
                text_color "#fff7ed"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("저장"):
                action ShowMenu("save")
                xalign 0.5
                xsize 390
                ysize 58
                background Solid("#2d241dcc")
                hover_background Solid("#5f4638")
                text_size 25
                text_color "#fff7ed"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("불러오기"):
                action ShowMenu("load")
                xalign 0.5
                xsize 390
                ysize 58
                background Solid("#2d241dcc")
                hover_background Solid("#5f4638")
                text_size 25
                text_color "#fff7ed"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("메인 메뉴"):
                action MainMenu(confirm=False)
                xalign 0.5
                xsize 390
                ysize 58
                background Solid("#2d241dcc")
                hover_background Solid("#5f4638")
                text_size 25
                text_color "#fff7ed"
                text_xalign 0.5
                text_yalign 0.5


# ------------------------------------------------------------------------------
# Save / Load
# ------------------------------------------------------------------------------

screen save():
    tag menu
    modal True

    add "images/bg_university_morning.png":
        xysize (1280, 720)

    add Solid("#120f0c99")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1040
        background Solid("#17120ee6")
        padding (48, 42)

        vbox:
            spacing 24
            text _("저장") size 42 color "#fff7ed"

            grid 3 2:
                spacing 16

                for slot in range(1, 7):
                    textbutton _("슬롯 [slot]"):
                        action FileSave(slot)
                        xsize 290
                        ysize 100
                        background Solid("#2d241dcc")
                        hover_background Solid("#5f4638")
                        text_size 24
                        text_color "#fff7ed"
                        text_xalign 0.5
                        text_yalign 0.5

            hbox:
                spacing 16
                textbutton _("돌아가기") action Return() xsize 220 ysize 56 text_xalign 0.5 text_yalign 0.5
                textbutton _("메인 메뉴") action MainMenu(confirm=False) xsize 220 ysize 56 text_xalign 0.5 text_yalign 0.5


screen load():
    tag menu
    modal True

    add "images/bg_university_morning.png":
        xysize (1280, 720)

    add Solid("#120f0c99")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1040
        background Solid("#17120ee6")
        padding (48, 42)

        vbox:
            spacing 24
            text _("불러오기") size 42 color "#fff7ed"

            grid 3 2:
                spacing 16

                for slot in range(1, 7):
                    textbutton _("슬롯 [slot]"):
                        action FileLoad(slot)
                        xsize 290
                        ysize 100
                        background Solid("#2d241dcc")
                        hover_background Solid("#5f4638")
                        text_size 24
                        text_color "#fff7ed"
                        text_xalign 0.5
                        text_yalign 0.5

            hbox:
                spacing 16
                textbutton _("돌아가기") action Return() xsize 220 ysize 56 text_xalign 0.5 text_yalign 0.5
                if not main_menu:
                    textbutton _("메인 메뉴") action MainMenu(confirm=False) xsize 220 ysize 56 text_xalign 0.5 text_yalign 0.5


# ------------------------------------------------------------------------------
# Utility screens Ren'Py may invoke.
# ------------------------------------------------------------------------------

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200

    add "images/bg_university_morning.png":
        xysize (1280, 720)

    add Solid("#120f0caa")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        background Solid("#17120ee6")
        padding (44, 38)

        vbox:
            spacing 24
            text message xalign 0.5 text_align 0.5 size 28 color "#fff7ed"
            hbox:
                xalign 0.5
                spacing 20
                textbutton _("예") action yes_action xsize 180 ysize 56 text_xalign 0.5 text_yalign 0.5
                textbutton _("아니오") action no_action xsize 180 ysize 56 text_xalign 0.5 text_yalign 0.5


screen notify(message):
    zorder 100

    frame:
        xalign 0.98
        yalign 0.05
        background Solid("#17120ee6")
        padding (24, 16)
        text message size 20 color "#fff7ed"

    timer 3.0 action Hide("notify")


screen skip_indicator():
    zorder 100

    frame:
        xalign 0.98
        yalign 0.02
        background Solid("#17120ee6")
        padding (18, 10)
        text _("SKIPPING") size 18 color "#f3b8a8"


# Simple in-game overlay. It avoids depending on Ren'Py's generated GUI.
default quick_menu = True

screen quick_menu():
    zorder 100

    if quick_menu:
        hbox:
            xalign 0.5
            yalign 0.985
            spacing 12

            textbutton _("뒤로") action Rollback() text_size 16
            textbutton _("저장") action ShowMenu("save") text_size 16
            textbutton _("불러오기") action ShowMenu("load") text_size 16
            textbutton _("스킵") action Skip() text_size 16
            textbutton _("메뉴") action ShowMenu("game_menu") text_size 16


init python:
    if "quick_menu" not in config.overlay_screens:
        config.overlay_screens.append("quick_menu")

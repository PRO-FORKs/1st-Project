################################################################################
## Self-contained prototype screens - Ren'Py 8.5
##
## This file intentionally avoids Ren'Py's generated GUI image assets and most
## gui.* variables, so the project can be extracted as a standalone project.
################################################################################

init offset = -1

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
        background Solid("#111827")
        padding (48, 24)

        vbox:
            spacing 10

            if who is not None:
                text who:
                    id "who"
                    size 30
                    color "#f9a8d4"

            text what:
                id "what"
                size 27
                color "#f8fafc"
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

    vbox:
        xalign 0.5
        yalign 0.65
        xsize 900
        spacing 14

        for i in items:
            textbutton i.caption:
                action i.action
                xfill True
                xpadding 30
                ypadding 18
                background Solid("#1f2937")
                hover_background Solid("#374151")
                text_size 25
                text_color "#f8fafc"
                text_hover_color "#fbcfe8"
                text_xalign 0.5


# ------------------------------------------------------------------------------
# Main menu / pause menu
# ------------------------------------------------------------------------------

screen main_menu():
    tag menu

    # 메인 배경 이미지
    add "images/main_menu.png":
        xysize (1280, 720)

    # 왼쪽 메뉴 영역
    frame:
        xalign 0.06
        yalign 0.55
        xsize 380
        background Solid("#111827CC")
        padding (35, 35)

        vbox:
            xalign 0.5
            spacing 18

            text "[config.name]":
                xalign 0.5
                size 42
                color "#ffffff"
                outlines [(2, "#00000080", 0, 0)]

            null height 15

            textbutton _("게임 시작"):
                action Start()
                xalign 0.5
                xsize 300
                ysize 60
                background Solid("#be185dcc")
                hover_background Solid("#db2777")
                text_size 26
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("불러오기"):
                action ShowMenu("load")
                xalign 0.5
                xsize 300
                ysize 56
                background Solid("#1f2937cc")
                hover_background Solid("#374151")
                text_size 24
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("종료"):
                action Quit(confirm=False)
                xalign 0.5
                xsize 300
                ysize 56
                background Solid("#1f2937cc")
                hover_background Solid("#374151")
                text_size 24
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5

# Ren'Py calls the game_menu screen for the ESC/menu context. Keep this screen
# intentionally simple and route to our save/load screens.
screen game_menu(title=None, scroll=None, yinitial=0.0, spacing=0):
    tag menu
    modal True

    add Solid("#0b1020")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 700
        background Solid("#111827")
        padding (50, 44)

        vbox:
            xalign 0.5
            spacing 18

            text (title if title else _("게임 메뉴")):
                xalign 0.5
                size 42
                color "#ffffff"

            textbutton _("돌아가기"):
                action Return()
                xalign 0.5
                xsize 390
                ysize 58
                background Solid("#1f2937")
                hover_background Solid("#374151")
                text_size 25
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("저장"):
                action ShowMenu("save")
                xalign 0.5
                xsize 390
                ysize 58
                background Solid("#1f2937")
                hover_background Solid("#374151")
                text_size 25
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("불러오기"):
                action ShowMenu("load")
                xalign 0.5
                xsize 390
                ysize 58
                background Solid("#1f2937")
                hover_background Solid("#374151")
                text_size 25
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5

            textbutton _("메인 메뉴"):
                action MainMenu(confirm=False)
                xalign 0.5
                xsize 390
                ysize 58
                background Solid("#1f2937")
                hover_background Solid("#374151")
                text_size 25
                text_color "#ffffff"
                text_xalign 0.5
                text_yalign 0.5


# ------------------------------------------------------------------------------
# Save / Load
# ------------------------------------------------------------------------------

screen save():
    tag menu
    modal True

    add Solid("#0b1020")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1040
        background Solid("#111827")
        padding (48, 42)

        vbox:
            spacing 24
            text _("저장") size 42 color "#ffffff"

            grid 3 2:
                spacing 16

                for slot in range(1, 7):
                    textbutton _("슬롯 [slot]"):
                        action FileSave(slot)
                        xsize 290
                        ysize 100
                        background Solid("#1f2937")
                        hover_background Solid("#374151")
                        text_size 24
                        text_color "#ffffff"
                        text_xalign 0.5
                        text_yalign 0.5

            hbox:
                spacing 16
                textbutton _("돌아가기") action Return() xsize 220 ysize 56 text_xalign 0.5 text_yalign 0.5
                textbutton _("메인 메뉴") action MainMenu(confirm=False) xsize 220 ysize 56 text_xalign 0.5 text_yalign 0.5


screen load():
    tag menu
    modal True

    add Solid("#0b1020")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 1040
        background Solid("#111827")
        padding (48, 42)

        vbox:
            spacing 24
            text _("불러오기") size 42 color "#ffffff"

            grid 3 2:
                spacing 16

                for slot in range(1, 7):
                    textbutton _("슬롯 [slot]"):
                        action FileLoad(slot)
                        xsize 290
                        ysize 100
                        background Solid("#1f2937")
                        hover_background Solid("#374151")
                        text_size 24
                        text_color "#ffffff"
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

    add Solid("#0b1020")

    frame:
        xalign 0.5
        yalign 0.5
        xsize 760
        background Solid("#111827")
        padding (44, 38)

        vbox:
            spacing 24
            text message xalign 0.5 text_align 0.5 size 28 color "#ffffff"
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
        background Solid("#111827")
        padding (24, 16)
        text message size 20 color "#ffffff"

    timer 3.0 action Hide("notify")


screen skip_indicator():
    zorder 100

    frame:
        xalign 0.98
        yalign 0.02
        background Solid("#111827")
        padding (18, 10)
        text _("SKIPPING") size 18 color "#f9a8d4"


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

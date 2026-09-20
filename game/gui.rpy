# Korean-capable GUI bootstrap for Ren'Py 8.5.
# Uses SourceHanSansLite.ttf bundled with the Ren'Py SDK.

init -2 python:
    gui.init(1280, 720)

# Korean font used by dialogue, names, menus, buttons and system UI.
define gui.text_font = "SourceHanSansLite.ttf"
define gui.name_text_font = "SourceHanSansLite.ttf"
define gui.interface_text_font = "SourceHanSansLite.ttf"
define gui.system_font = "SourceHanSansLite.ttf"
define gui.button_text_font = "SourceHanSansLite.ttf"
define gui.choice_button_text_font = "SourceHanSansLite.ttf"

# Korean text is written with spaces; use Ren'Py's Korean line-breaking mode.
define gui.language = "korean-with-spaces"

# Compatibility with screens that check this value.
define gui.show_name = True

# Our custom screens mostly inherit from the default style, so force the
# Korean-capable SDK font here as well.
style default:
    font "SourceHanSansLite.ttf"
    language "korean-with-spaces"

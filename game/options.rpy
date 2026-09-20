# Ren'Py 8.5 prototype project settings

# Add the font directory bundled with the Ren'Py SDK to the resource search
# path. This gives the project Korean glyph coverage without requiring a
# separate font download during development.
init -3 python:
    if config.renpy_base + "/sdk-fonts" not in config.searchpath:
        config.searchpath.append(config.renpy_base + "/sdk-fonts")

define config.name = _("복학생의 가을 - Prototype")
define config.version = "0.1.3"
define build.name = "campus_vn_prototype_v013"

define config.has_sound = True
define config.has_music = True
define config.has_voice = True

define config.enter_transition = dissolve
define config.exit_transition = dissolve

define config.window = "auto"

define config.save_directory = "campus_vn_prototype_v013"

# When creating a distribution from the SDK, include SDK fonts as Ren'Py's
# own tutorial project does.
init python:
    build.classify_renpy("sdk-fonts/**", "all")
    build._sdk_fonts = True

#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

available_OSs = ["WINDOWS", "LINUX", "MAC"]
available_keyboard_layouts = ["US", "UK", "ES", "DE", "FR"]
available_keycodes = ["US", "UK", "ES", "DE", "FR"]


def get_layout(layout, os):
    # --- lib ---
    # Official repo: https://github.com/adafruit/Adafruit_CircuitPython_HID
    from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayoutUs
    # Official repo: https://github.com/Neradoc/Circuitpython_Keyboard_Layouts
    from lib.other_languages.layouts.keyboard_layout_win_uk import KeyboardLayout as KeyboardLayoutUk
    from lib.other_languages.layouts.keyboard_layout_win_es import KeyboardLayout as KeyboardLayoutEs
    from lib.other_languages.layouts.keyboard_layout_win_de import KeyboardLayout as KeyboardLayoutDe
    from lib.other_languages.layouts.keyboard_layout_mac_fr import KeyboardLayout as KeyboardLayoutMacFr
    from lib.other_languages.layouts.keyboard_layout_win_fr import KeyboardLayout as KeyboardLayoutWinFr

    if layout == "UK":
        keyboard_layout = KeyboardLayoutUk
    elif layout == "ES":
        keyboard_layout = KeyboardLayoutEs
    elif layout == "DE":
        keyboard_layout = KeyboardLayoutDe
    elif layout == "FR" and os == "MAC":
        keyboard_layout = KeyboardLayoutMacFr
    elif layout == "FR":
        keyboard_layout = KeyboardLayoutWinFr
    else:
        keyboard_layout = KeyboardLayoutUs

    return keyboard_layout


def get_keycode(layout, os):
    # --- lib ---
    # Official repo: https://github.com/adafruit/Adafruit_CircuitPython_HID
    from lib.adafruit_hid.keyboard import Keycode as KeycodeUs
    # Official repo: https://github.com/Neradoc/Circuitpython_Keyboard_Layouts
    from lib.other_languages.keycodes.keycode_win_uk import Keycode as KeycodeUk
    from lib.other_languages.keycodes.keycode_win_es import Keycode as KeycodeEs
    from lib.other_languages.keycodes.keycode_win_de import Keycode as KeycodeDe
    from lib.other_languages.keycodes.keycode_mac_fr import Keycode as KeycodeMacFr
    from lib.other_languages.keycodes.keycode_win_fr import Keycode as KeycodeWinFr

    if layout == "UK":
        keycode = KeycodeUk
    elif layout == "ES":
        keycode = KeycodeEs
    elif layout == "DE":
        keycode = KeycodeDe
    elif layout == "FR" and os == "MAC":
        keycode = KeycodeMacFr
    elif layout == "FR":
        keycode = KeycodeWinFr
    else:
        keycode = KeycodeUs

    return keycode

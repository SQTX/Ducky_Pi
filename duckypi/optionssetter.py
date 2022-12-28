#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

available_OSs = ["WINDOWS", "LINUX", "MAC"]
available_keyboard_layouts = ["US", "UK", "ES", "DE", "FR"]
available_keycodes = ["US", "UK", "ES", "DE", "FR"]


def get_layout(layout, os):
    # Official repo: https://github.com/Neradoc/Circuitpython_Keyboard_Layouts
    if layout == "UK":
        from lib.libraries.layouts.keyboard_layout_win_uk import KeyboardLayout as KeyboardLayoutUk
        keyboard_layout = KeyboardLayoutUk
    elif layout == "ES":
        from lib.libraries.layouts.keyboard_layout_win_es import KeyboardLayout as KeyboardLayoutEs
        keyboard_layout = KeyboardLayoutEs
    elif layout == "DE":
        from lib.libraries.layouts.keyboard_layout_win_de import KeyboardLayout as KeyboardLayoutDe
        keyboard_layout = KeyboardLayoutDe
    elif layout == "FR" and os == "MAC":
        from lib.libraries.layouts.keyboard_layout_mac_fr import KeyboardLayout as KeyboardLayoutMacFr
        keyboard_layout = KeyboardLayoutMacFr
    elif layout == "FR":
        from lib.libraries.layouts.keyboard_layout_win_fr import KeyboardLayout as KeyboardLayoutWinFr
        keyboard_layout = KeyboardLayoutWinFr
    else:
        # Official repo: https://github.com/adafruit/Adafruit_CircuitPython_HID
        from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS as KeyboardLayoutUs
        keyboard_layout = KeyboardLayoutUs

    return keyboard_layout


def get_keycode(layout, os):
    # Official repo: https://github.com/Neradoc/Circuitpython_Keyboard_Layouts
    if layout == "UK":
        from lib.libraries.keycodes.keycode_win_uk import Keycode as KeycodeUk
        keycode = KeycodeUk
    elif layout == "ES":
        from lib.libraries.keycodes.keycode_win_es import Keycode as KeycodeEs
        keycode = KeycodeEs
    elif layout == "DE":
        from lib.libraries.keycodes.keycode_win_de import Keycode as KeycodeDe
        keycode = KeycodeDe
    elif layout == "FR" and os == "MAC":
        from lib.libraries.keycodes.keycode_mac_fr import Keycode as KeycodeMacFr
        keycode = KeycodeMacFr
    elif layout == "FR":
        from lib.libraries.keycodes.keycode_win_fr import Keycode as KeycodeWinFr
        keycode = KeycodeWinFr
    else:
        # Official repo: https://github.com/adafruit/Adafruit_CircuitPython_HID
        from lib.adafruit_hid.keyboard import Keycode as KeycodeUs
        keycode = KeycodeUs

    return keycode

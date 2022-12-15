#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

from duckypi.optionssetter import get_keycode


class KeycodeOperator:
    def __init__(self, layout, os):
        self.layout = layout
        self.os = os

        self.Keycode = get_keycode(self.layout, self.os)

    def get_key(self, key):
        key_formula = "Keycode."

        alp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
        if key in alp:
            key_formula += str(key).upper()
        else:
            if self.os == "MAC":
                key = convert_mac_keys(key)
            key_formula += key

        key = eval(key_formula, {"Keycode": self.Keycode})
        return key


def convert_mac_keys(mac_key):
    if mac_key == "COMMAND" or mac_key == "CMD":
        return "WINDOWS"
    elif mac_key == "OPTION":
        return "LEFT_ALT"
    elif mac_key == "CONTROL":
        return "LEFT_CONTROL"
    elif mac_key == "Clear":
        return "KEYPAD_NUMLOCK"
    else:
        return mac_key

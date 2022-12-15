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
            # TODO: convert mac key to windows key
            key_formula += key

        key = eval(key_formula, {"Keycode": self.Keycode})
        return key

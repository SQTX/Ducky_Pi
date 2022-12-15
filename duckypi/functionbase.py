#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************
all_functions = ["^OPTS", "^COM", "^COMB", "^SENTEN", "^WRITE", "^HOLD", "^KEY", "^WAIT", "^END"]

from time import sleep
from duckypi.optionssetter import get_layout
from duckypi.keycodeoperator import KeycodeOperator
# --- lib ---
import usb_hid
# Official repo: https://github.com/adafruit/Adafruit_CircuitPython_HID
from lib.adafruit_hid.keyboard import Keyboard


class FunctionBase:
    # Constructor:
    def __init__(self, layout, os, keycode_op: KeycodeOperator):
        self.layout = layout
        self.os = os
        self.keycode_op = keycode_op  # Set StandardKeyMap object as keys_map
        self.start_time = 0.01

        self.KeyboardLayout = get_layout(self.layout, self.os)
        self.controller = Keyboard(usb_hid.devices)
        self.keyboard_layout = self.KeyboardLayout(self.controller)

    # Functions:
    def key_func(self, decoded_key):
        sleep(self.start_time)
        self.controller.press(decoded_key)
        self.controller.release(decoded_key)

    def comb_func(self, keys_list):
        sleep(self.start_time)
        for key in keys_list:
            self.controller.press(key)
        for key in keys_list:
            self.controller.release(key)

    def hold_func(self, decoded_key, time):
        sleep(self.start_time)
        self.controller.press(decoded_key)
        sleep(time)
        self.controller.release(decoded_key)

    def senten_func(self, text):
        sleep(self.start_time)
        self.keyboard_layout.write(text)
        self.controller.press(self.keycode_op.get_key("ENTER"))  # Get dictionary keys_map form self.keys_map
        self.controller.release(self.keycode_op.get_key("ENTER"))

    def write_func(self, text, time):
        sleep(self.start_time)
        for letter in text:
            self.keyboard_layout.write(letter)
            sleep(time)
        self.controller.press(self.keycode_op.get_key("ENTER"))
        self.controller.release(self.keycode_op.get_key("ENTER"))

    def wait_func(self, time):
        sleep(time)

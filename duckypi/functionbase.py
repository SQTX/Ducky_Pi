all_functions = ["^OPTS", "^COM", "^COMB", "^SENTEN", "^WRITE", "^HOLD", "^KEY", "^WAIT", "^END"]

from time import sleep
from duckypi.optionssetter import get_layout
# --- lib ---
from duckypi.standardkeymap import StandardKeyMap
import usb_hid
from lib.adafruit_hid.keyboard import Keyboard


class FunctionBase:
    def __init__(self, layout, os, keys_map: StandardKeyMap):
        self.layout = layout
        self.os = os
        self.keys_map = keys_map # Set StandardKeyMap object as keys_map
        self.start_time = 0.01

        self.KeyboardLayout = get_layout(self.layout, self.os)
        self.controller = Keyboard(usb_hid.devices)
        self.keyboard_layout = self.KeyboardLayout(self.controller)


    def key_func(self, decoded_key, is_key):
        sleep(self.start_time)
        if is_key:
            self.controller.press(decoded_key)
            self.controller.release(decoded_key)
        else:
            self.keyboard_layout.write(decoded_key)

    def comb_func(self, keys_list):
        sleep(self.start_time)
        for key in keys_list:
            self.controller.press(key)
        for key in keys_list:
            self.controller.release(key)

    def hold_func(self, decoded_key, is_key, time):
        sleep(self.start_time)
        if is_key:
            self.controller.press(decoded_key)
            sleep(time)
            self.controller.release(decoded_key)
        else:
            self.controller.press(decoded_key)
            sleep(time)
            self.controller.release(decoded_key)

    def senten_func(self, text):
        sleep(self.start_time)
        self.keyboard_layout.write(text)
        self.controller.press(self.keys_map.keys_map.get("ENTER"))  # Get dictionary keys_map form self.keys_map
        self.controller.release(self.keys_map.keys_map.get("ENTER"))

    def write_func(self, text, time):
        sleep(self.start_time)
        for letter in text:
            self.controller.press(letter)
            self.controller.release(letter)
            sleep(time)
        self.controller.press(self.keys_map.keys_map.get("ENTER"))
        self.controller.release(self.keys_map.keys_map.get("ENTER"))

    def wait_func(self, time):
        sleep(time)

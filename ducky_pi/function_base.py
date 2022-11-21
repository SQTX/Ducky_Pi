all_functions = ["^OPTS", "^COM", "^COMB", "^SENTEN", "^WRITE", "^HOLD", "^KEY", "^WAIT", "^END"]

# Descriptions of functions:
# ^OPTS -
from time import sleep
from standard_keymap import keys_map
import usb_hid
from lib.adafruit_hid.keyboard import Keyboard
from lib.adafruit_hid.keyboard_layout_us import KeyboardLayoutUS

controller = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(controller)

start_time = 0.01


def key_func(decoded_key, is_key):
    sleep(start_time)
    if is_key:
        controller.press(decoded_key)
        controller.release(decoded_key)
    else:
        keyboard_layout.write(decoded_key)


def comb_func(keys_list):
    sleep(start_time)
    for key in keys_list:
        controller.press(key)
    for key in keys_list:
        controller.release(key)


def hold_func(decoded_key, is_key, time):
    sleep(start_time)
    if is_key:
        controller.press(decoded_key)
        sleep(time)
        controller.release(decoded_key)
    else:
        controller.press(decoded_key)
        sleep(time)
        controller.release(decoded_key)


def senten_func(text):
    sleep(start_time)
    keyboard_layout.write(text)
    controller.press(keys_map.get("ENTER"))
    controller.release(keys_map.get("ENTER"))


def write_func(text, time):
    sleep(start_time)
    for letter in text:
        controller.press(letter)
        controller.release(letter)
        sleep(time)
    controller.press(keys_map.get("ENTER"))
    controller.release(keys_map.get("ENTER"))


def wait_func(time):
    sleep(time)


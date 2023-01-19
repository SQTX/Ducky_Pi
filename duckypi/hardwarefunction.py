#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

from time import sleep
import board
import digitalio

LED = digitalio.DigitalInOut(board.LED)
LED.direction = digitalio.Direction.OUTPUT


def edit_mode_led():
    while True:
        LED.value = True
        sleep(5.0)
        LED.value = False
        sleep(5.0)


def script_start_led():
    flashing_led(3, 0.09)


def error_led():
    flashing_led(15, 0.09)


def script_done_led():
    LED.value = True


def flashing_led(count: int, time):
    for i in range(count):
        LED.value = True
        sleep(time)
        LED.value = False
        sleep(time)


# anti-autorun
# Patent with cable connection to block autorun inspired by dbisu
def is_edit_mode():
    mode = digitalio.DigitalInOut(board.GP0)
    mode.direction = digitalio.Direction.INPUT
    mode.pull = digitalio.Pull.UP

    if not mode.value:  # Mod ON
        return True
    else:  # Mod OFF
        return False

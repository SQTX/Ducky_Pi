from lib.adafruit_hid.keyboard import Keycode

keys_map = {
    # Function F Keycodes
    "F1": Keycode.F1,
    "F2": Keycode.F2,
    "F3": Keycode.F3,
    "F4": Keycode.F4,
    "F5": Keycode.F5,
    "F6": Keycode.F6,
    "F7": Keycode.F7,
    "F8": Keycode.F8,
    "F9": Keycode.F9,
    "F10": Keycode.F10,
    "F11": Keycode.F11,
    "F12": Keycode.F12,
    # Options Keycodes
    "ESC": Keycode.ESCAPE,
    "TAB": Keycode.TAB,
    "CAPSLOCK": Keycode.CAPS_LOCK,
    "SHIFT": Keycode.SHIFT,
    "SHIFTL": Keycode.LEFT_SHIFT,
    "SHIFTR": Keycode.RIGHT_SHIFT,
    # "fn": Keycode.fn, TODO nie wiem co to za klawisz
    "CTRL": Keycode.CONTROL,   # Control on Mac
    "CTRLL": Keycode.LEFT_CONTROL,
    "CTRLR": Keycode.RIGHT_CONTROL,
    "BACKSPACE": Keycode.BACKSPACE,     # Delete on Mac
    "ENTER": Keycode.ENTER,
    "CMD": Keycode.WINDOWS,
    # "CMDL": Keycode.,
    # "CMDR": Keycode.cmd_r,
    "ALT": Keycode.ALT,     # Option on Mac
    "ALTL": Keycode.LEFT_ALT,
    "ALTR": Keycode.RIGHT_ALT,
    "SPACE": Keycode.SPACE,
    #
    "HOME": Keycode.HOME,
    "END": Keycode.END,
    # TODO error z tymi klawiszami, pradopodobnie wynika z limitu lawiszy w laptopie
    # "INSERT": Keycode.insert,
    # "DELETE": Keycode.delete,
    # "PAGEUP": Keycode.page_up,
    # "PAGEDOWN": Keycode.page_down,
    # "PRINTSCREEN": Keycode.print_screen,
    # "PTRSRC": Keycode.scroll_lock,
    # "PAUSEBREAK": Keycode.pause,
    # Arrows Keycodes
    "ARRUP": Keycode.UP_ARROW,
    "ARRDOWN": Keycode.DOWN_ARROW,
    "ARRLEFT": Keycode.LEFT_ARROW,
    "ARRRIGHT": Keycode.RIGHT_ARROW,
    # Numbers Keycodes
    # "NUMLOCK": Keycode.num_lock,
}

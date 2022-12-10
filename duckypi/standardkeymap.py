from duckypi.optionssetter import get_keycode


class StandardKeyMap:
    def __init__(self, layout, os):
        self.layout = layout
        self.os = os

        self.Keycode = get_keycode(self.layout, self.os)

        self.keys_map = {
            # --- Function F Keycodes ---
            "F1": self.Keycode.F1,
            "F2": self.Keycode.F2,
            "F3": self.Keycode.F3,
            "F4": self.Keycode.F4,
            "F5": self.Keycode.F5,
            "F6": self.Keycode.F6,
            "F7": self.Keycode.F7,
            "F8": self.Keycode.F8,
            "F9": self.Keycode.F9,
            "F10": self.Keycode.F10,
            "F11": self.Keycode.F11,
            "F12": self.Keycode.F12,
            # --- Options Keycodes ---
            "ESC": self.Keycode.ESCAPE,
            "TAB": self.Keycode.TAB,
            "CAPSLOCK": self.Keycode.CAPS_LOCK,
            "SHIFT": self.Keycode.SHIFT,
            "SHIFTL": self.Keycode.LEFT_SHIFT,
            "SHIFTR": self.Keycode.RIGHT_SHIFT,
            # "fn": self.Keycode.fn, TODO: nie wiem co to za klawisz
            "CTRL": self.Keycode.CONTROL,  # Control on Mac
            "CTRLL": self.Keycode.LEFT_CONTROL,
            "CTRLR": self.Keycode.RIGHT_CONTROL,
            "BACKSPACE": self.Keycode.BACKSPACE,  # Delete on Mac
            "ENTER": self.Keycode.ENTER,
            "CMD": self.Keycode.WINDOWS,
            # "CMDL": self.Keycode.,
            # "CMDR": self.Keycode.cmd_r,
            "ALT": self.Keycode.ALT,  # Option on Mac
            "ALTL": self.Keycode.LEFT_ALT,
            "ALTR": self.Keycode.RIGHT_ALT,
            "SPACE": self.Keycode.SPACE,
            # --- sth ---
            "HOME": self.Keycode.HOME,
            "END": self.Keycode.END,
            # TODO: error:: z tymi klawiszami, pradopodobnie wynika z limitu lawiszy w laptopie
            # "INSERT": self.Keycode.insert,
            # "DELETE": self.Keycode.delete,
            # "PAGEUP": self.Keycode.page_up,
            # "PAGEDOWN": self.Keycode.page_down,
            # "PRINTSCREEN": self.Keycode.print_screen,
            # "PTRSRC": self.Keycode.scroll_lock,
            # "PAUSEBREAK": self.Keycode.pause,
            # Arrows self.Keycodes
            "ARRUP": self.Keycode.UP_ARROW,
            "ARRDOWN": self.Keycode.DOWN_ARROW,
            "ARRLEFT": self.Keycode.LEFT_ARROW,
            "ARRRIGHT": self.Keycode.RIGHT_ARROW,
            # Numbers self.Keycodes
            # "NUMLOCK": self.Keycode.num_lock,
        }

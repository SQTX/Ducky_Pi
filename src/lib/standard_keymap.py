from pynput.keyboard import Key

keys_map = {
    # FX keys
    "F1": Key.f1,
    "F2": Key.f2,
    "F3": Key.f3,
    "F4": Key.f4,
    "F5": Key.f5,
    "F6": Key.f6,
    "F7": Key.f7,
    "F8": Key.f8,
    "F9": Key.f9,
    "F10": Key.f10,
    "F11": Key.f11,
    "F12": Key.f12,
    # Options keys
    "ESC": Key.esc,
    "TAB": Key.tab,
    "CAPSLOCK": Key.caps_lock,
    "SHIFT": Key.shift,
    "SHIFTL": Key.shift_l,
    "SHIFTR": Key.shift_r,
    # "fn": Key.fn, TODO nie wiem co to za klawisz
    "CTRL": Key.ctrl,   # Control on Mac
    "CTRLL": Key.ctrl_l,
    "CTRLR": Key.ctrl_r,
    "BACKSPACE": Key.backspace,     # Delete on Mac
    "ENTER": Key.enter,
    "CMD": Key.cmd,
    "CMDL": Key.cmd_l,
    "CMDR": Key.cmd_r,
    "ALT": Key.alt,     # Option on Mac
    "ALTL": Key.alt_l,
    "ALTR": Key.alt_r,
    "SPACE": Key.space,
    #
    "HOME": Key.home,
    "END": Key.end,
    # "INSERT": Key.insert,
    # "DELETE": Key.delete,
    # "PAGEUP": Key.page_up,
    # "PAGEDOWN": Key.page_down,
    # "PRINTSCREEN": Key.print_screen,
    # "PTRSRC": Key.scroll_lock,
    # "PAUSEBREAK": Key.pause,
    # Arrows keys
    "ARRUP": Key.up,
    "ARRDOWN": Key.down,
    "ARRLEFT": Key.left,
    "ARRRIGHT": Key.right,
    # Numbers keys
    # "NUMLOCK": Key.num_lock,
}

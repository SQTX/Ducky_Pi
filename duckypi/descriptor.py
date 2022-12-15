#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

from duckypi.functionbase import FunctionBase
from duckypi.keycodeoperator import KeycodeOperator
# --- err ---
from duckypi.allexceptions import ScryptError
from duckypi.allexceptions import OptionsNotExistError
from duckypi.allexceptions import InvalidArguments


def descriptor(payload_file):
    options = set_options(payload_file)
    keycode_op = KeycodeOperator(options[2], options[0])
    function = FunctionBase(options[2], options[0], keycode_op)

    payload_file.seek(0)

    script_line_index = 0
    for line in payload_file:
        script_line_index += 1  # Line's index in script

        # Ignore empty lines
        if line == ' ' or line == '\n':
            continue

        line = line.strip('\n')  # Cut off 'white' charracters

        from duckypi.errordetector import function_ok
        if not function_ok(line, script_line_index):
            continue

        words = line.split(' ')  # Divide full line into single words

        # ------------------------------------------------------------------
        # End of script and app work
        if 'str' in line or str(words[0]) == "^END" or str(words[0]) == "^END\n":
            payload_file.close()
            break
        # ------------------------------------------------------------------
        # Comment line, ignored by descriptor (another ^OPTS also)
        if words[0] == "^COM" or words[0] == "^OPTS":
            # Skip other options setter
            pass
        # ------------------------------------------------------------------
        # Get only function key form keyboard or only one letter and "click" it
        if words[0] == "^KEY":
            # Too many arguments
            if len(words) > 2:
                raise InvalidArguments(script_line_index)

            keyboard_key = words[1].strip('\n').upper()

            right_arg = False
            for key in dir(keycode_op.Keycode):
                if key == keyboard_key:
                    right_arg = True
                    function.key_func(keycode_op.get_key(key))
                    break
            if not right_arg:
                raise InvalidArguments(script_line_index)
        # ------------------------------------------------------------------
        # Press at the same time couple of keys
        if words[0] == "^COMB":
            # Too less arguments
            if len(words) < 3:
                raise InvalidArguments(script_line_index)
            # TODO: anti ghosting function

            index = 1
            keys_to_press = []

            while index < len(words):
                keyboard_key = (words[index].strip('\n').upper())

                right_arg = False
                for key in dir(keycode_op.Keycode):
                    if key == keyboard_key:
                        right_arg = True
                        keys_to_press.append(keycode_op.get_key(key))
                        break
                if not right_arg:
                    raise InvalidArguments(script_line_index)
                index += 1
            function.comb_func(keys_to_press)
        # ------------------------------------------------------------------
        # Works similar to ^KEY but button is pressed for set time
        if words[0] == "^HOLD":
            # Too many arguments
            if len(words) > 3:
                raise InvalidArguments(script_line_index)

            time = float(words[2].strip('\n'))
            keyboard_key = words[1].strip('\n').upper()

            right_arg = False
            for key in dir(keycode_op.Keycode):
                if key == keyboard_key:
                    right_arg = True
                    function.hold_func(keycode_op.get_key(key), time)
                    break
            if not right_arg:
                raise InvalidArguments(script_line_index)
        # ------------------------------------------------------------------
        # In the one moment it write all sentence
        if words[0] == "^SENTEN":
            # TODO: error:: max size
            text = ""
            index = 1
            while index < len(words):
                if index == (len(words) - 1):
                    text += str(words[index])
                    break
                text += str(words[index] + ' ')
                index += 1
            function.senten_func(text)
        # ------------------------------------------------------------------
        if words[0] == "^WRITE":
            # Writes each letter at constant period
            # TODO: error:: max size
            text = ""
            time = float(words[len(words) - 1])     # The last agrument is the time of pasue
            index = 1
            while index < (len(words) - 1):
                if index == (len(words) - 2):
                    text += str(words[index])
                    break
                text += str(words[index] + ' ')
                index += 1
            function.write_func(text, time)
        # ------------------------------------------------------------------
        if words[0] == "^WAIT":
            time = float(words[1])
            function.wait_func(time)
        # ------------------------------------------------------------------


def set_options(payload_file):
    user_settings = []
    set_diffult = [True, True, True]  # os-keycode-layout

    script_line_index = 0
    for line in payload_file:
        script_line_index += 1

        line = line.strip('\n')
        words = line.split(' ')

        if words[0] == "^OPTS":
            if len(words) <= 1:
                raise InvalidArguments(script_line_index)

            options = words[1].split(';')
            opt_elements = []
            for opt in options:
                opt_elements.append(opt.split('='))

            import duckypi.optionssetter as options

            for opt in opt_elements:
                category = str(opt[0]).upper()
                option = str(opt[1]).upper()

                is_ok = False
                # Check if the "OS" category is rightly passed and if it wasn't set earlier
                if category == "OS" and set_diffult[0]:
                    set_diffult[0] = False
                    for os in options.available_OSs:
                        if option == os:
                            user_settings.append(os)
                            is_ok = True
                            continue
                    if not is_ok:
                        raise OptionsNotExistError("OS", script_line_index, options.available_OSs)
                # Check if the "LANG" category is rightly passed and if it wasn't set earlier
                elif category == "LANG" and set_diffult[1]:
                    set_diffult[1] = False
                    for keycode in options.available_keycodes:
                        if option == keycode:
                            user_settings.append(keycode)
                            is_ok = True
                            continue
                    if not is_ok:
                        raise OptionsNotExistError("language", script_line_index, options.available_keycodes)
                # Check if the "LAYOUT" category is rightly passed and if it wasn't set earlier
                elif category == "LAYOUT" and set_diffult[2]:
                    set_diffult[2] = False
                    for layout in options.available_keyboard_layouts:
                        if option == layout:
                            user_settings.append(layout)
                            is_ok = True
                            continue
                    if not is_ok:
                        raise OptionsNotExistError("layout", script_line_index, options.available_keyboard_layouts)
            break   # Other ^OPTS will be ignored
    # TODO: set options in function base class and keycode base class
    print(set_diffult)
    print(user_settings)

    settings = user_settings
    return settings

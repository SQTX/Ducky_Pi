from duckypi.functionbase import FunctionBase
from duckypi.standardkeymap import StandardKeyMap
# --- err ---
from duckypi.allexceptions import ScryptError
from duckypi.allexceptions import OptionsNotExistError
from duckypi.allexceptions import InvalidArguments


def descriptor(payload_file):
    options = set_options(payload_file)
    keymap_obj = StandardKeyMap(options[2], options[0])
    function = FunctionBase(options[2], options[0], keymap_obj)
    keys_map = keymap_obj.keys_map

    payload_file.seek(0)

    script_line_index = 0
    for line in payload_file:
        script_line_index += 1  # Line's index in script

        # Ignore empty lines
        if line == ' ' or line == '\n':
            continue

        line = line.strip('\n')  # Cut off white charracters

        from duckypi.errordetector import function_ok
        if not function_ok(line, script_line_index):
            continue

        words = line.split(' ')  # Divide full line into single words

        # ------------------------------------------------------------------
        if 'str' in line or str(words[0]) == "^END" or str(words[0]) == "^END\n":
            payload_file.close()
            break
        # ------------------------------------------------------------------
        if words[0] == "^COM" or words[0] == "^OPTS":
            # Skip other options setter
            pass
        # ------------------------------------------------------------------
        if words[0] == "^KEY":
            is_key = False
            keyboard_key = words[1].upper()
            for key in keys_map:
                if key == keyboard_key.strip('\n'):
                    is_key = True
                    function.key_func(keys_map.get(key), is_key)
                    break
            if not is_key:
                letter = words[1]
                function.key_func(letter, False)
        # ------------------------------------------------------------------
        if words[0] == "^COMB":
            # TODO: error:: Too less arguments
            index = 1
            keys = []
            while index < len(words):
                words[index] = (words[index].upper())
                for key in keys_map:
                    if key == words[index].strip('\n'):
                        keys.append(keys_map.get(key))
                        break
                index += 1
            function.comb_func(keys)
        # ------------------------------------------------------------------
        if words[0] == "^HOLD":
            is_key = False
            time = float(words[len(words) - 1])
            if not is_it_number(time, script_line_index):
                continue
            keyboard_key = words[1].upper()
            for key in keys_map:
                if key == keyboard_key.strip('\n'):
                    is_key = True
                    function.key_func(keys_map.get(key), is_key)
                    break
            if not is_key:
                letter = words[1]
                function.hold_func(letter, False, time)
        # ------------------------------------------------------------------
        if words[0] == "^SENTEN":
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
            text = ""
            time = float(words[len(words) - 1])
            if not is_it_number(time, script_line_index):
                continue
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
            if not is_it_number(words[1], script_line_index):
                continue
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
                # Sprawdzenie czy kategoria OS została podana oraz czy nic nie zostało już ustawione
                if category == "OS" and set_diffult[0]:
                    set_diffult[0] = False
                    for os in options.available_OSs:
                        if option == os:
                            user_settings.append(os)
                            is_ok = True
                            continue
                    if not is_ok:
                        raise OptionsNotExistError("OS", script_line_index, options.available_OSs)
                # Sprawdzenie czy kategoria LANG została podana oraz czy nic nie zostało już ustawione
                elif category == "LANG" and set_diffult[1]:
                    set_diffult[1] = False
                    for keycode in options.available_keycodes:
                        if option == keycode:
                            user_settings.append(keycode)
                            is_ok = True
                            continue
                    if not is_ok:
                        raise OptionsNotExistError("language", script_line_index, options.available_keycodes)
                # Sprawdzenie czy kategoria LAYOUT została podana oraz czy nic nie zostało już ustawione
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


def is_it_number(word, script_line_index):
    # TODO: nie wiem czy jest potrzeby
    number = float(word)
    if 0.0 < number < 1000000.0:
        return True
    raise ScryptError(f"Podany argument: \"{word}\", nie jest liczba", script_line_index)

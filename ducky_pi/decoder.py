from error_detector import error_detector


def payload():
    with open("payload_file_exec.txt", "r") as payload_file:
        # TODO: File open errors
        if not error_detector(payload_file):
            payload_file.close()

        payload_file.seek(0)
        decoder(payload_file)


# def open_file():
#     pass

# import function_base as function #TODO: do podmiany
import test_function_base as function
# from standard_keymap import keys_map #TODO: do podmiany
from test_standard_keymap import keys_map


def decoder(payload_file):
    for line in payload_file:
        line = line.strip('\n')
        words = line.split(' ')
        if 'str' in line or str(words[0]) == "^END" or str(words[0]) == "^END\n":
            payload_file.close()
            break
        if words[0] == "^COM":
            pass
        # ------------------------------------------------------------------
        if words[0] == "^END":
            break
        # ------------------------------------------------------------------
        if words[0] == "^OPTS":
            pass
            # Kod... TODO
            # import iOS
            # Keys / Windows
            # import language
            #     flag = False
            #     flag = language and os
            #     set
            #     up
            # if flag:
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

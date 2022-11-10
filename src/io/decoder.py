def payload():
    with open("payload_file_exec.txt", "r") as payload_file:
        for line in payload_file:
            line = line.strip('\n')
            words = line.split(' ')
            if 'str' in line or str(words[0]) == "^END" or str(words[0]) == "^END\n":
                payload_file.close()
                break
                # TODO
#             if str(words[0]) == "^OPS":
# #                 import iOS Keys/Windows
# #                 import language
#                 flag = False
# #                 flag = language and os set up
#                 if flag:

            import src.lib.standard_keymap as keys_file
            from pynput.keyboard import Controller
            controller = Controller()
            if str(words[0]) == "^KEY":
                words[1] = words[1].upper()
                for key in keys_file.keys_map:
                    if str(key) == str(words[1].strip('\n')):
                        controller.press(keys_file.keys_map.get(key))
                        controller.release(keys_file.keys_map.get(key))
                        break










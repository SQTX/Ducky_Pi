# from function_base import all_functions #TODO: do podmiany
from test_function_base import all_functions
# from src.exceptions.script_exceptions import * # All types of errors
from ducky_pi.exceptions.script_exceptions import FunctionDoesntExistError
from ducky_pi.exceptions.script_exceptions import SyntaxError


# Function whitch detected errors in script
def error_detector(payload_file):
    is_ok = True

    script_line_index = 0
    try:
        for line in payload_file:
            script_line_index += 1  # Line index

            # Ignore empty lines
            if line == ' ' or line == '\n':
                continue

            line = line.strip('\n')
            words = line.split(' ')

            function_doesnt_exist_flag = True
            for single_function in all_functions:
                # Does function exist? ***************************************************
                if words[0][0] == '^' and words[0] == single_function:
                    function_doesnt_exist_flag = False
                # Illegal funcions combination ***************************************************
                if len(words) > 1 and words[0] != "^SENTEN" and words[0] == single_function and words[1][0] == '^':
                    raise SyntaxError(f"Dwie funkcje wystąpiły po sobie nielegalnie: \"{words[0]} {words[1]}\"",
                                      script_line_index)
                # Not a number in WAIT/HOLD/WRITE TODO
                # Too less arguments in COMB TODO
                # Chceck all flag
                if not function_doesnt_exist_flag:
                    break

            if function_doesnt_exist_flag:
                raise FunctionDoesntExistError(f"Podana funkcja nie istnieje: \"{words[0]}\"", script_line_index)
    # try_end
    except FunctionDoesntExistError as e:
        e.mess()
    except SyntaxError as e:
        e.mess()

    return is_ok

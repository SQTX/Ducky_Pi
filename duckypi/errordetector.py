#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

from duckypi.descriptor import descriptor
# --- err ---
from duckypi.allexceptions import ScryptError
from duckypi.allexceptions import OptionsNotExistError
from duckypi.allexceptions import InvalidArguments


# =========== Main error detector in script ===========================================================================
def error_detected(payload_file):
    try:
        descriptor(payload_file)
        return False
    except ScryptError as err:
        err.mess()
        return True
    except OptionsNotExistError as err:
        err.mess()
        return True
    except InvalidArguments as err:
        err.mess()
        return True
    except ValueError as err:
        print("The argument isn't a number")
        return True


# =========== Function whitch detected errors in script ===============================================================
def function_ok(line, script_line_index):
    from duckypi.functionbase import all_functions as functions
    line = line.strip('\n')
    words = line.split(' ')

    function_doesnt_exist = True
    for function in functions:
        # *************************************************************************************************************
        # Does function exist?
        if words[0][0] == '^' and words[0] == function:
            function_doesnt_exist = False
        # *************************************************************************************************************
        # Illegal funcions combination
        if len(words) > 1 and words[0] != "^SENTEN" and words[0] == function and words[1][0] == '^':
            raise ScryptError(f"This two functions cannot be passed next to each other \"{words[0]} {words[1]}\"",
                              script_line_index)
        # *************************************************************************************************************
        # Check "function_doesnt_exist_flag" flag
        if not function_doesnt_exist:
            break

    if function_doesnt_exist:
        raise ScryptError(f"The passed function doesn't exist: \"{words[0]}\"", script_line_index)

    return True

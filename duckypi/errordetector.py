from duckypi.descriptor import descriptor
from duckypi.exceptions.scriptexceptions import ScryptError
from duckypi.exceptions.scriptexceptions import OptionsNotExistError
from duckypi.exceptions.scriptexceptions import InvalidArguments


# =========== Main error detector in script ===========================================================================
def is_it_error(payload_file):
    try:
        descriptor(payload_file)
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
        print("Podany argument nie jest liczba")
        return True


# =========== Function whitch detected errors in script ===============================================================
def function_ok(line, script_line_index):
    # from duckypi.test_function_base import all_functions as functions
    from duckypi.functionbase import all_functions as functions   #TODO: do podmiany
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
            raise ScryptError(f"Dwie funkcje wystąpiły po sobie nielegalnie: \"{words[0]} {words[1]}\"",
                              script_line_index)
        # *************************************************************************************************************
        # Check "function_doesnt_exist_flag" flag
        if not function_doesnt_exist:
            break

    if function_doesnt_exist:
        raise ScryptError(f"Podana funkcja nie istnieje: \"{words[0]}\"", script_line_index)

    return True

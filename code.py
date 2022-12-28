#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

from duckypi.hardwarefunction import is_edit_mode, script_start_led, edit_mode_led
from duckypi.main import payload

if not is_edit_mode():
    script_start_led()
    payload()
else:
    edit_mode_led()

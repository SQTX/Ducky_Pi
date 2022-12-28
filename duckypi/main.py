#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

# Main information about project
__title__ = "Ducky_Pi"
__version__ = "0.2.6"
__author__ = "Jakub SQTX Sitarczyk"

from duckypi.errordetector import error_detected  # Start main code


def payload():
    payload_file_name = "payload.txt"
    try:
        with open(payload_file_name, "r") as payload_file:
            if error_detected(payload_file):
                payload_file.close()
                from duckypi.hardwarefunction import error_led
                error_led()
            else:
                payload_file.close()
    except IOError:
        print(f"Couldn't read file: {payload_file_name}")

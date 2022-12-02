# Main Information about project
__title__ = "Ducky_Pi"
__version__ = "0.1.2"
__author__ = "Jakub SQTX Sitarczyk"

# Starting function
from duckypi.errordetector import is_it_error


def payload():
    with open("payload.txt", "r") as payload_file:  # TODO do podmiany
    # with open("payload_file_exec.txt", "r") as payload_file:
        # TODO: File open errors
        if is_it_error(payload_file):
            payload_file.close()

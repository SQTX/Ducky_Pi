#  ***********************************
#  Copyright © 2022.
#  Author: Jakub SQTX Sitarczyk
#  ***********************************

# TODO: Przetłumaczyć komunikaty na angielski
class ScryptError(Exception):
    def __init__(self, message, line_index):
        self.message = str(message)
        self.line_index = int(line_index)

    def mess(self):
        print(f"The \'{self.line_index}\' line contains the following error:")
        print(self.message)


class OptionsNotExistError(Exception):
    def __init__(self, message, line_index, available_options):
        self.message = str(message)
        self.line_index = int(line_index)
        self.available_options = available_options

    def mess(self):
        print(f"The \'{self.line_index}\' line contains the following error:")
        print(f"The selected option doesn't exist + {self.message}")
        print("These're the possible options:")
        for opt in self.available_options:
            print(str(opt))


class InvalidArguments(Exception):
    def __init__(self, line_index):
        self.line_index = int(line_index)

    def mess(self):
        print(f"In the line \'{self.line_index}\', the wrong argument was passed to the function")

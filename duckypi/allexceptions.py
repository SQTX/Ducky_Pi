class ScryptError(Exception):
    def __init__(self, message, line_index):
        self.message = str(message)
        self.line_index = int(line_index)

    def mess(self):
        print(f"W linii \'{self.line_index}\' znajduje się poniższy błąd:")
        print(self.message)


class OptionsNotExistError(Exception):
    def __init__(self, message, line_index, available_options):
        self.message = str(message)
        self.line_index = int(line_index)
        self.available_options = available_options

    def mess(self):
        print(f"W linii \'{self.line_index}\' znajduje się poniższy błąd:")
        print(f"Wybrana opcja nie istnieja + {self.message}")
        print("Możliwe opcje to:")
        for opt in self.available_options:
            print(str(opt))

class InvalidArguments(Exception):
    def __init__(self, line_index):
        self.line_index = int(line_index)

    def mess(self):
        print(f"W linii \'{self.line_index}\' do funkcji przekazano niewlasciwe argumenty")
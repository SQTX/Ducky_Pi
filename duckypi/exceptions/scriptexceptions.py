class FunctionDoesntExistError(Exception):
    def __init__(self, message, line_index):
        self.message = str(message)
        self.line_index = int(line_index)

    def mess(self):
        print(f"W linii \'{self.line_index}\' znajduje się poniższy błąd:")
        print(self.message)


# TODO: możliwa optymalizacja
class SyntaxError(Exception):
    def __init__(self, message, line_index):
        self.message = str(message)
        self.line_index = int(line_index)

    def mess(self):
        print(f"W linii \'{self.line_index}\' znajduje się poniższy błąd:")
        print(self.message)

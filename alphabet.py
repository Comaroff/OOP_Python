import string


class Alphabet:
    def __init__(self, language, letters):
        self.lang = language
        self.letters = list(letters)

    # Печатаем все буквы алфавита
    def print(self):
        print(self.letters)

    # Возвращаем кол-во букв в алфавите
    def letters_num(self):
        len(self.letters)

# Английский алфавит
class EngAlphabet(Alphabet):

    __letters_num = 26

    def __init__(self):
        super().__init__('En', string.ascii_uppercase)

    # Проверяем, относится ли буква к английскому алфавиту
    def is_en_letter(self, letter):
        if letter.upper() in self.letters:
            return 'Это буква английского алфавита'
        else:
            return 'Это буква не принадлежит английскому алфавиту'

    # Возвращаем кол-во букв в алфавите
    def letters_num(self):
        return EngAlphabet.__letters_num

    # Печатаем пример текста на английском языке
    @staticmethod
    def example():
        print("Пример на английском языке:\nDon't judge a book by it's cover.")

# Тесты
if __name__ == '__main__':
    eng_alphabet = EngAlphabet()
    eng_alphabet.print()
    print(eng_alphabet.letters_num())
    print(eng_alphabet.is_en_letter('F'))
    print(eng_alphabet.is_en_letter('х'))
    EngAlphabet.example()
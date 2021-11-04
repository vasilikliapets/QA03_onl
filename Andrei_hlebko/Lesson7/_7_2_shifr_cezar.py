def encode_cesar(text, step):
    stroka_after_enc = ""
    for word in text:
        for symbol in word:
            if symbol.isupper():
                stroka_after_enc += en_alphabet[(en_alphabet.index(symbol.lower())) - step % 26].upper()
            elif symbol.islower():
                stroka_after_enc += en_alphabet[(en_alphabet.index(symbol)) - step % 26]
            else:
                stroka_after_enc += symbol
        stroka_after_enc += ' '
        return stroka_after_enc


def decode_cesar(text, step):
    stroka_after_dec = ""
    for word in text:
        for symbol in word:
            if symbol.isupper():
                stroka_after_dec += en_alphabet[(step + en_alphabet.index(symbol.lower())) % 26].upper()
            elif symbol.islower():
                stroka_after_dec += en_alphabet[(step + en_alphabet.index(symbol)) % 26]
            else:
                stroka_after_dec += symbol
        stroka_after_dec += ' '
    return stroka_after_dec


en_alphabet = [chr(x) for x in range(ord('a'), ord('z') + 1)]


# en_alphabet = [chr(i) for i in range(65, 91)] + [chr(j) for j in range(97, 123)]  # все буквы англ алфавита
# ru_alphabet = [chr(i) for i in range(1040, 1104)]  # все бувы рус алфавита
def start_shifr():
    """
    The progrom shifr cesar encrypts or decrypts a text.
    You input your text and input step, and get result
    """
    choose_operation = int(input("""
        Выберите операцию в программе Шифр Цезаря:
        1)Encode(Разкодировать)
        2)Decode(Закодировать)
        :"""))

    phrase = input("Введите фразу для зашифровки:").split()
    numb = int(input("Введите число на какое количество символов сделать сдвиг:"))

    if choose_operation == 1:
        print(encode_cesar(phrase, numb))
    elif choose_operation == 2:
        print(decode_cesar(phrase, numb))


if __name__ == 'main':
    start_shifr()

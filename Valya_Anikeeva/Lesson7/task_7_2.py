# Шифр Цезаря. При шифровании каждый символ заменяется другим,
# отстоящим от него в алфавите на фиксированное число позиций.

eng_lower = 'abcdefghijklmnopqrstuvwxyz'
eng_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
rus_lower = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"


def encode(text: str, shifr: int):
    """
    Ф-ция кодирования сообщений
    """
    text_out = ''
    for char in text:
        if char in rus_lower:
            i = (rus_lower.index(char) + shifr) % 33
            text_out += rus_lower[i]
        elif char in rus_upper:
            i = (rus_lower.index(char) + shifr) % 33
            text_out += rus_upper[i]
        elif char in eng_lower:
            i = (eng_lower.index(char) + shifr) % 26
            text_out += eng_lower[i]
        elif char in eng_upper:
            i = (eng_upper.index(char) + shifr) % 26
            text_out += eng_upper[i]
        else:
            text_out += char
    return text_out


def decode(text: str, shifr: int):
    """
    Ф-ция декодирования сообщений
    """
    text_out = ''
    for char in text:
        if char in rus_lower:
            i = (rus_lower.index(char) - shifr) % 33
            text_out += rus_lower[i]
        elif char in rus_upper:
            i = (rus_lower.index(char) - shifr) % 33
            text_out += rus_upper[i]
        elif char in eng_lower:
            i = (eng_lower.index(char) - shifr) % 26
            text_out += eng_lower[i]
        elif char in eng_upper:
            i = (eng_upper.index(char) - shifr) % 26
            text_out += eng_upper[i]
        else:
            text_out += char
    return text_out


def code():
    """
    Выбор кодирования/декодирования текста
    """
    print("Выберите шифрование: encode - 1, decode - 2")
    chifr = input()
    print("Введите ключ шифрования")
    key = int(input())
    print("Введите фразу")
    text = input()
    if chifr == '1':
        print(encode(text, key))
    elif chifr == '2':
        print(decode(text, key))
    else:
        print('Неверный выбор')


if __name__ == '__main__':        
    code()

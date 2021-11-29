# При шифровании каждый символ заменяется другим,
# стоящим от него в алфавите на фиксированное число позиций.

RUS1 = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RUS2 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
LAT1 = 'abcdefghijklmnopqrstuvwxyz'
LAT2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encode(text: str, shift: int):
    """
    The function encodes the text, replacing each character with another,
    which is located from it in the alphabet by the specified shift number.
    """
    text_out = ''
    for char in text:
        if char in RUS1:
            i = (RUS1.index(char) + shift) % 33
            text_out += RUS1[i]
        elif char in RUS2:
            i = (RUS1.index(char) + shift) % 33
            text_out += RUS2[i]
        elif char in LAT1:
            i = (LAT1.index(char) + shift) % 26
            text_out += LAT1[i]
        elif char in LAT2:
            i = (LAT2.index(char) + shift) % 26
            text_out += LAT2[i]
        else:
            text_out += char
    return text_out


def decode(text: str, shift: int):
    """
    The function decodes the text, replacing each character with another,
    which is located from it in the alphabet by the specified shift number.
    """
    text_out = ''
    for char in text:
        if char in RUS1:
            i = (RUS1.index(char) - shift) % 33
            text_out += RUS1[i]
        elif char in RUS2:
            i = (RUS1.index(char) - shift) % 33
            text_out += RUS2[i]
        elif char in LAT1:
            i = (LAT1.index(char) - shift) % 26
            text_out += LAT1[i]
        elif char in LAT2:
            i = (LAT2.index(char) - shift) % 26
            text_out += LAT2[i]
        else:
            text_out += char
    return text_out


def code():
    """
    The function to select text encoding or decoding.
    """
    op = input('Выберите операцию: 1 - Encode, 2 - Decode ')
    text = input('Введите фразу: ')
    shift = int(input('Введите число для сдвига позиций: '))
    if op == '1':
        print(encode(text, shift))
    elif op == '2':
        print(decode(text, shift))
    else:
        print('Неправильно выбрана операция')


if __name__ == "__main__":
    code()

# 2. Шифр Цезаря!

r_lower = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
r_upper = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
l_lower = 'abcdefghijklmnopqrstuvwxyz'
l_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def encode(txt: str, shift: int):
    """
    The function replaces each character of the text with another one that is separated from it in the alphabet by a
    fixed number of positions
    """
    txt_result = ''
    for char in txt:
        if char in r_lower:
            i = (r_lower.index(char) + shift) % 33
            txt_result += r_lower[i]
        elif char in r_upper:
            i = (r_lower.index(char) + shift) % 33
            txt_result += r_upper[i]
        elif char in l_lower:
            i = (l_lower.index(char) + shift) % 26
            txt_result += l_lower[i]
        elif char in l_upper:
            i = (l_upper.index(char) + shift) % 26
            txt_result += l_upper[i]
        else:
            txt_result += char
    return txt_result


def decode(txt: str, shift: int):
    """
    The function replaces each character of the text with another one that is separated from it in the alphabet by a
    fixed number of positions
    """
    txt_result = ''
    for char in txt:
        if char in r_lower:
            i = (r_lower.index(char) - shift) % 33
            txt_result += r_lower[i]
        elif char in r_upper:
            i = (r_lower.index(char) - shift) % 33
            txt_result += r_upper[i]
        elif char in l_lower:
            i = (l_lower.index(char) - shift) % 26
            txt_result += l_lower[i]
        elif char in l_upper:
            i = (l_upper.index(char) - shift) % 26
            txt_result += l_lower[i]
        else:
            txt_result += char
    return txt_result


def code():
    """
    The function accepts arguments when choosing encode or decode operation
    """
    oper = input('Выберите операцию: 1 - Encode, 2 - Decode: ')
    txt = input('Введите фразу: ')
    shift = int(input('Введите число позиций для сдвига: '))
    if oper == '1':
        print(encode(txt, shift))
    elif oper == '2':
        print(decode(txt, shift))
    else:
        print('Данная операция не существует')


if __name__ == "__main__":
    code()
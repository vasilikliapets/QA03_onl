#2.1
"""
Модуль для использования "Шифра Цезаря"
"""

def encode(str, x):
    """
    Функция закодирует сообщение
    """
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc = list(abc)
    enc = []
    lst = str.split()
    b = 0
    for i in lst:
        for j in i:
            a = (abc.index(j) + x)
            if a + x < 26:
                b = abc[a]
            elif a + x >= 26:
                b = abc[a - 26]
            enc.append(b)
        enc.append('')
    s = ''
    for t in enc:
        if t == '':
            s = s + ' '
        else:
            s = s + t
    return s
    

#2.2
def decode(str, x):
    """
    Функция раскодирует сообщение
    """
    abc = 'abcdefghijklmnopqrstuvwxyz'
    abc = list(abc)
    enc = []
    lst = str.split()
    b = 0
    for i in lst:
        for j in i:
            a = (abc.index(j) + (26 -x))
            if a + x < 26:
                b = abc[a]
            elif a + x >= 26:
                b = abc[a - 26]
            enc.append(b)
        enc.append('')
    s = ''
    for t in enc:
        if t == '':
            s = s + ' '
        else:
            s = s + t
    return s    


def run_code():
    op = input('Выберите операцию Encode либо Decode: ')
    str = input('Введите сообщение: ')
    if op == 'Encode':
        print(encode(str, 3))
    elif op == 'Decode':
        print(decode(str, 3))


if __name__ == 'main':
    run_code()
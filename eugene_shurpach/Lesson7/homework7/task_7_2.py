"""Шифр Цезаря — один из древнейших шифров.
При шифровании каждый символ заменяется другим, отстоящим от него в алфавите на фиксированное число позиций.
"""
import string


def cezar():
    def encode(a, step):
        """Кодирует фразу а с шагом step"""
        g = list(string.punctuation) + list(range(0, 10))  # Знаки препинания и цифры
        b = list(2 * string.ascii_uppercase + 2 * string.ascii_lowercase)
        c = list(b[step:52] + list(string.ascii_uppercase[:step]) + b[52 + step:] + list(string.ascii_lowercase[:step]))
        punct = dict(zip(g, g))
        punct[" "] = " "
        di = dict(zip(b, c))  # Словарь соответсвия буква-закодированная буква
        di.update(punct)
        d = []
        for i in a:
            d.append(di[i])
        return print(''.join(d))

    def decode(a, step):
        """Раскодирует фразу а по шагу step"""
        g = list(string.punctuation) + list(range(0, 10))  # Знаки препинания и цифры
        b = list(2 * string.ascii_uppercase + 2 * string.ascii_lowercase)
        c = list(b[step:52] + list(string.ascii_uppercase[:step]) + b[52 + step:] + list(string.ascii_lowercase[:step]))
        punct = dict(zip(g, g))
        punct[" "] = " "
        di = dict(zip(c, b))  # Словарь соответствия закодированная буква-буква
        di.update(punct)
        d = []
        for i in a:
            d.append(di[i])
        return print(''.join(d))

    choise_user = input(f"Выберите операцию:\n1)Encode\n2)Decode:\n")
    while choise_user not in ["1", "2"]:  # Проверка допустимости операции
        print("Прости, но эта операция пока не разработана!")
        choise_user = input(f"Выберите операцию:\n1)Encode\n2)Decode:\n")
    else:
        if choise_user == "1":
            user_string = input("Введите фразу для кодирования: ")
            user_step = int(input("Введите шаг: "))
            encode(user_string, user_step)
        elif choise_user == "2":
            user_string = input("Введите фразу для расшифровки: ")
            user_step = int(input("Введите шаг: "))
            decode(user_string, user_step)

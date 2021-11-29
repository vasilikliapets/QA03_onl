"""Написать функцию, которая вычисляет банковский вклад
Пользователь делает вклад в размере a рублей сроком на years лет под 10% годовых
 каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада,
 и на них в следующем году тоже будут проценты).
Написать функцию bank, принимающая аргументы a и years, и возвращающую сумму, которая будет на счету пользователя.
"""


def babank():
    def bank(a, years):
        result = float(a) * (1.1 ** int(years))
        return print(round(result, 2))

    b = input("Введите сумму вклада: ")
    c = input("Введите количество лет: ")

    def is_number(x):
        try:
            float(x)
            return True
        except ValueError:
            return False

    while is_number(b) is not True and is_number(c) is not True:
        print("Не очень похоже на цифры! Попробуй еще раз")
        b = input("Введите сумму вклада: ")
        c = input("Введите количество лет: ")
    else:
        bank(b, c)

# 1. Написать функцию, которая вычисляет банковский вклад. Пользователь делает вклад в размере a рублей сроком на years
# лет под 10% годовых (каждый год размер его вклада увеличивается на 10%. Эти деньги прибавляются к сумме вклада, и на
# них в следующем году тоже будут проценты). Написать функцию bank, принимающая аргументы a и years, и возвращающую
# сумму, которая будет на счету пользователя.
def vklad(a, years):
    """
    The function that calculates a bank deposit.
    """
    i = 0
    while i < years:
        # Подсчет суммы с процентами за год
        a = a + a * 0.1
        # Подсчет лет
        i = i + 1
    return a


def bank():
    """
    The function that takes the arguments a and years, and returns the amount that will be on the user's account.
    """
    a = float(input('Введите сумму вклада:'))
    years = int(input('Введите срок вклада:'))
    print('Сумма на счете:', vklad(a, years))


if __name__ == '__main__':
    bank()

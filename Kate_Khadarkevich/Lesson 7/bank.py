def bank(a, years):
    """
    The function calculates the total amount of the deposit
    """
    i = 0
    while i < years:
        a = a + a * 0.1  # высчитываем сумму с процентом за год
        i += 1  # считаем года
    a = round(a, 2)  # округляем до 2-х знаков после запятой
    return a


def for_bank():
    a = float(input('Введите сумму взноса:'))
    years = int(input('Введите срок вклада:'))
    print('Итоговая сумма:', bank(a, years))


if __name__ == '__main__':
    for_bank()

# 1
def bank(a, years):
    """
    Функция вычисляет банковский вклад
    :param a: сумма вклада
    :param years: срок вклада
    :return: итоговая сумма
    """
    sum = a
    x = years
    for i in range(0, years):
        sum = 1.1 * sum
    return round(sum, 2)

a = float(input('Сумма вклада: '))
years = int(input('Срок вклада: '))
print(bank(a, years))

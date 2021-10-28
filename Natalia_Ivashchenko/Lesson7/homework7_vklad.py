# функция bank, принимает аргументы a и years,
# и возвращающую сумму, которая будет на счету пользователя.

def bank():
    """
    The function calculates a bank deposit,
    each year the size of the deposit increases by 10%.
    """
    a = int(input('Сумма вклада: '))
    years = int(input('Количество лет: '))
    i = 0
    while i < years:
        a = a + a * 0.1
        i += 1
    print('Сумма на счете:', a)


if __name__ == "__main__":
    bank()

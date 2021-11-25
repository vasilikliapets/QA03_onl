# Функция bank, которая вычисляет банковский вклад -
# функция, принимающая аргументы a и years, и возвращающая сумму,
# которая будет на счету пользователя.

# Пользователь делает вклад в размере a рублей сроком на years лет
# под 10% годовых. Каждый год размер его вклада увеличивается на 10%.
# Эти деньги прибавляются к сумме вклада, и на них в следующем году
# тоже будут проценты.

def bank(a, years):
    summa = 0
    """
    This function counts user's savings based on initial deposit and years
    :param a: int
    :param years: int
    :return: summa
    """
    if years == 0:
        summa = a
    elif years == 1:
        summa = a + a * 0.1
    else:
        summa = bank(int(a) * 0.1, int(years)-1) + bank(a, int(years) - 1)
    return summa


def run_bank():
    """
    This functions runs program Bank deposit
    :return:
    """
    user_deposit = int(input("Введите сумму вашего вклада: "))
    user_years = input("Введите количество лет: ")
    print("Сумма вашего вклада будет: ", str(bank(user_deposit, user_years)))


if __name__ == '__main__':
    run_bank()

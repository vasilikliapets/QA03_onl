def bank_deposit(a, years):
    """
    This function Bank deposite calculate your money(rubles) in the bank.
    You input summ and term, and get result

    """
    count = a
    for i in range(years):
        count += count // 100 * 10
    return print(f"Сумма вклада через {years} года/лет будет равна: {count} рублей")


def start_bank():
    summa_deposit = int(input("Напишите сумму вклада в рублях:"))
    term_deposit = int(input("Введите срок на сколько лет внести депозит:"))
    bank_deposit(summa_deposit, term_deposit)


if __name__ == 'main':
    start_bank()

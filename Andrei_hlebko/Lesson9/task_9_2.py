# 2-Банковский вклад

class Invest:
    def __init__(self, name, N, R):
        """

        N = summ rubl
        R = Term years
        """
        self.name = name
        self.summa = N
        self.term = R
        Bank.deposite(name, N, R)


class Bank:
    def deposite(self, summa_inv, years):
        count = summa_inv
        for i in range(years):
            count += round(count / 100 * 10)
        return print(f"Сумма вклада клиента {self} через {years} года/лет будет равна: {count} рублей")


Invest("Andry", 1000, 3)
Invest("Daria", 500000, 10)

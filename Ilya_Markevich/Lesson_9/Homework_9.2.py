# 2 Банковский вклад
class Investment:
    def __init__(self, n, r):
        self.n = n
        self.r = r

    pass


class Bank:
    @staticmethod
    def deposit(investment):
        """Расчет процентов с капитализацией"""
        summ = investment.n * (1 + 10 / 100 / 12) ** (investment.r * 12)
        return summ


invest1 = Investment(2000, 3)

print(Bank.deposit(invest1))

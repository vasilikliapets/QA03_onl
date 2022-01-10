# Инвестиции

class Investment:
    def __init__(self, n, r):
        """Констурктор класса Инвестиции"""
        self.n = n  # Сумма
        self.r = r  # Cрок
    pass


class Bank:
    @staticmethod
    def deposit(investment):
        """Расчет сложных процентов с капитализацией каждый месяц"""
        result = investment.n * ((1 + 10 / 100 / 12) ** (investment.r * 12))
        return round(result, 2)


invest_1 = Investment(100, 2)  # Добавляем инвестиции

print(Bank.deposit(invest_1))  # Печать результата по инвестиции

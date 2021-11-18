# Инвестиции

class Investment:
    def __init__(self, N, R):
        """Констурктор класса Инвестиции"""
        self.N = N  # Сумма
        self.R = R  # Cрок
    pass


class Bank:
    @staticmethod
    def deposit(Investment):
        """Расчет сложных процентов с капитализацией каждый месяц"""
        result = Investment.N * ((1 + 10 / 100 / 12) ** (Investment.R * 12))
        return round(result, 2)


invest_1 = Investment(100, 2)  # Добавляем инвестиции

print(Bank.deposit(invest_1))  # Печать результата по инвестиции

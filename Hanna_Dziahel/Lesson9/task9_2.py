# Создайте класс инвестиция. Который содержит необходимые поля и методы,
# например сумма инвестиция и его срок. Пользователь делает инвестиция
# в размере N рублей сроком на R лет под 10% годовых (инвестиция с возможностью
# ежемесячной капитализации - это означает, что проценты прибавляются к сумме
# инвестиции ежемесячно). Написать класс Bank, метод deposit принимает
# аргументы N и R, и возвращает сумму, которая будет на счету пользователя.


class Investment:
    """Investment properties"""

    def __init__(self, deposit: int, years: int):
        self.deposit = deposit
        self.years = years

    def count_summa(self, rate=10):
        """
        This function counts user's savings based on initial deposit and months
        :param rate: int
        :return:
        """
        months = self.years * 12
        summa = 0
        if months == 0:
            summa = self.deposit
            return summa
        else:
            summa = self.deposit * ((1 + rate/100/12)**months)
            return summa

investment = Investment(1000, 2)
print(investment.count_summa())
class Investment:
    def __init__(self, name, N, R):
        """This is constructor of investments"""
        self.name = name    #имя пользователя
        self.N = N          #cумма вклада в рублях
        self.R = R          #срок вклада, лет

class Bank:

    @staticmethod
    def deposit(invest):
        """This function calculates the end summa of investment"""
        whole_summ = invest.N*(1+10/100/12)**(invest.R*12)
        return whole_summ

#создаём инвестиции в классе Investment
invest_1 = Investment('Darya Tyupa', 1000, 5)
invest_2 = Investment('Dmitry Tyupa', 2000, 10)
invest_3 = Investment('Olga Ivanova', 50000, 7)

#расчитываем конечную суммы инвестиций
print(Bank.deposit(invest_1))
print(Bank.deposit(invest_2))
print(Bank.deposit(invest_3))



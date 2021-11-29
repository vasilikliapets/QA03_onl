#1
"""
Модуль расчета банковского вклада
"""
def bank(a, years):
    """
    Функция высчитывает итоговую сумму на счету с учетом процентов
    """
    
    procent = 0
    for i in range(years):
        procent = (a * 10) / 100
        a = a + procent
    return print(f'Сумма депозита = {a}')


def run_bank():
    a = int(input('Сумма депозита: '))
    years = int(input('Срок вклада: '))
    
    bank(a, years)

if __name__ == 'main':
    run_bank()
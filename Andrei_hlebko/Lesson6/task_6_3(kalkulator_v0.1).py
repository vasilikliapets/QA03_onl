def calculator(chislo1, chislo2, oper):
    """
    This function work as a simple calculator
    choose operators, input 2 values, get a result
    """
    chislo1 = int(chislo1)
    chislo2 = int(chislo2)
    if oper == "1":
        return chislo1 + chislo2
    elif oper == "2":
        return chislo1 - chislo2
    elif oper == "3":
        return chislo1 * chislo2
    elif oper == "4":  # +проверка деления на 0
        if chislo2 == 0:
            return "Деление на 0!"
        else:
            return f"Деление: {chislo1 / chislo2}, Остаток от деления: {chislo1 % chislo2}"
    else:
        print("Выберите из предложенного списка")


oper_chisla = input('''Выберите необходимую операцию: 
    1 = Сложение 
    2 = Вычитание 
    3 = Умножение
    4 = Деление
    :''')

chislo1 = input("Введите первое число: ")
chislo2 = input("Введите второе число: ")
print(calculator(chislo1, chislo2, oper_chisla))

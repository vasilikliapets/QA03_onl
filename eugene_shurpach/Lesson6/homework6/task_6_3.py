def summa(a, b):
    """Считает сумму"""
    return print(a + b)


def diff(a, b):
    """Считает разность"""
    return a - b


def comp(a, b):
    """Считает произведение"""
    return a * b


def quot(a, b):
    """Считает частное"""
    return a / b


choise_user = input(f"Выберите операцию:\n1.Сумма\n2.Разность\n3.Произведение\n4.Частное\n")
if choise_user not in ["1", "2", "3", "4"]:  # Проверка на входимость в список доступных операций
    print("Недопустимая операция")
else:
    x = float(input("Введите первое число: "))
    y = float(input("Введите второе число: "))
    if choise_user == "1":
        summa(x, y)
    elif choise_user == "2":
        print(diff(x, y))
    elif choise_user == "3":
        print(comp(x, y))
    elif choise_user == "4":
        if y == 0:
            print("Нельзя делить на 0, даже если очень хочется!")  # проверка деления на 0
        else:
            print(quot(x, y))

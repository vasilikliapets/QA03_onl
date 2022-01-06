# 1
def validate(card):
    """
    Функция проверяет введенный номер карты на наличение любых символов отличных от цифр
    """
    if card.isdigit() is True:
        check_card(card)
        print(card)
    else:
        print("Номер карты должен содержать только цифры")
        validate(input('Введите номер карты: '))



def check_card(a):
    """Функция проверяет номер карты на соотвествие алгоритму Луна"""
    a = list(map(int, str(a)))
    b = a[-2::-2]
    c = a[-1::-2]
    n = len(b)
    for i in range(0, n):
        if b[i] * 2 > 9:
            b[i] = b[i] * 2 - 9
        else:
            b[i] = b[i] * 2
    summa = sum(c) + sum(b)
    if summa % 10 == 0:
        print('Карта валидна')
    else:
        print('Карта невалидна')


a = input('Введите номер карты: ')
validate(a)

# 2
def count_text(a):
    """
    Функция считает количество букв
    """
    count = 1
    x = 1
    y = a[x:x + 1]
    for i in a:
        if i in y:
            count += 1

        else:
            print(i, end='')
            if count > 1:
                print(count, end='')
                count = 1
        x += 1
        y = a[x:x + 1]

a = input("Введите любое значение:")
count_text(a)

# 3
def calc():
    while True:
        print("Дествие, которое хотите сделать:\n"
              "Сложить: +\n"
              "Вычесть: -\n"
              "Умножить: *\n"
              "Поделить: /\n")
        action = input("Выберите действие: ")
        if action not in ('+', '-', '*', '/'):
            print("Фиг что посчитаешь")
            break
        if action in ('+', '-', '*', '/'):
            x = float(input("x = "))
            y = float(input("y = "))
            if action == '+':
                print(x+y)
                break
            elif action == '-':
                print(x-y)
                break
            elif action == '*':
                print(x*y)
                break
            elif action == '/':
                if y != 0:
                    print( x/y)
                    break
                else:
                    print("Делить на ноль нельзя!")
                    break

calc()

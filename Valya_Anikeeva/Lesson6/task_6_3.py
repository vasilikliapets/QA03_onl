#3 Простейший калькулятор

while True:
    s = input("Введите знак операции: \n"
              "Сложение: +\n"
              "Вычитание: -\n"
              "Умножение: *\n"
              "Деление: /\n"
              "Выйти: q\n")
    if s == 'q':
        break
    if s in ('+', '-', '*', '/'):
        x = float(input("x="))
        y = float(input("y="))
        if s == '+':
            print("%.2f" % (x+y))
        elif s == '-':
            print("%.2f" % (x-y))
        elif s == '*':
            print("%.2f" % (x*y))
        elif s == '/':
            if y != 0:
                print("%.2f" % (x/y))
            else:
                print("Делить на 0 нельзя!")
    else:
        print("Неверный знак операции!")

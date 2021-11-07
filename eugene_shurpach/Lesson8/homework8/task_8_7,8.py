from eugene_shurpach.Lesson8.homework8.decorators import timer, func_name, before_after, func_2


@timer
@func_name
def fibo(elements):
    """Фибонатор"""
    counter = 0
    while counter < elements:
        li = [0, 1]
        for i in range(1, elements):
            counter += 1
            li.append(li[i] + li[i-1])
    print(li[1::])


@before_after
@func_2
def matem(x, y):
    """Фунцкия считает результат выражения"""
    c = x ** y / abs(x * y) + x // y - y ** .85
    return c


user_choise = input(f'Выберите программу для проверки:\n1 - Фиббонатор\n2 - Математика\n')
while user_choise.isdigit():
    if user_choise == '1':
        print("Ты выбрал Фиббонатор!")
        el = int(input("Введи необходимое количество элементов: "))
        fibo(el)
        break
    elif user_choise == '2':
        print("Ты выбрал Математику!")
        a = float(input("Введи первое число: "))
        b = float(input("Введи второе число: "))
        matem(a, b)
        break
    elif user_choise not in ['1', '2']:
        print("Не очень похоже на цифру! Попробуй еще раз")
        user_choise = input(f"Выберите программу для проверки:\n1 - Фиббонатор\n2 - Математика\n")
        continue

from Andrei_hlebko.Lesson8.decorators import change, timer, func_name, add_1, insert_before_and_after


@change
def reverse(zna4):
    return zna4


def start_reverse():
    x = [1, 2, 3, 4, 5]
    print(reverse(x))


# Fibonacci
@func_name
@timer
def fibonacci(n):
    i = 1
    fib1, fib2 = 0, 1
    while i <= n:
        tmp = fib1
        fib1 = fib2
        fib2 = tmp + fib2
        if i == n:
            return fib1
        i += 1


def start_fibonacci():
    fibo_num = int(input("Введите число чтобы получить число фибоначчи введенного числа: "))
    print(f"От вашего числа {fibo_num}, число фибоначчи:", fibonacci(fibo_num))


@insert_before_and_after
@add_1
def start_complex_equation(x):
    return (5 * (x - 1) - 3 / (x + 1) + 1500 / (x ** 2 - 1))


vybor = int(input("""
        Выбери программу:
        1) Вычисляет значение фибоначчи с работой таймера(6) и именем функции (4)+
        2) Программа вычисляет сложное математическое уравнение добавляя в него программу 1 и 2
        3) Работа функции с декоратором которая переворачивает значения листа подаётся list[1,2,3,4,5]+
        :"""))

if vybor == 1:
    start_fibonacci()
elif vybor == 2:
    x = int(input("Введите число для вычисления сложной математической функции: "))
    start_complex_equation(x)
elif vybor == 3:
    start_reverse()
else:
    print("Вы ввели неправильно число!")

# 1 Напишите декоратор, который печатает перед и после вызова функции слова “Before” and “After”
def decorator_1(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper


@decorator_1
def my_precious():
    print("Вуаля! Декоратор!")

my_precious()

# 2 Напишите функцию декоратор, которая добавляет 1 к заданному числу
def func_1 (func):
    def wrapper (*args):
        result = func(*args)+1
        return result
    return wrapper


@func_1
def summa(x):
    x=5
    return x

b = summa(4)
print(b)

# 3 Напишите функцию декоратор, которая переводит полученный текст в верхний регистр
def decorator_3(func):
    def wrapper(text):
        return func(text).upper()
    return wrapper


@decorator_3
def func_text(text):
    return text


print(func_text("Hello, Python!"))

# 4 Напишите декоратор func_name, который выводит на экран имя функции (func.__name__)
def decorator_4(func):
    def wrapper(*args):
        print(func.__name__)

    return wrapper

@decorator_4
def func_name(text):
    return text

func_name()

# 5 Напишите декоратор change, который делает так, что задекорированная функция принимает все свои не именованные аргументы в порядке, обратном тому, в котором их передали
def change(func):
    def wrapper(*args):
        result = func(args[::-1])
        return result

    return wrapper

@change
def new_list(*args):
    list_args = list(*args)
    return list_args


print(new_list(1, 2, 3, 4, 5))

# 6 Напишите декоратор, который вычисляет время работы декорируемой функции (timer)
def timer(func):
    def wrapper(*args):
        start_time = time.perf_counter_ns()
        res = func(*args)
        print(f"{time.perf_counter_ns() - start_time} наносекунд")
        return res

    return

# 7 Напишите функцию, которая вычисляет значение числа Фибоначчи для заданного количество элементов последовательности и возвращает его и оберните ее декоратором timer и func_name
@timer
def decorator_7(n):
    num_1 = 0
    num_2 = 1
    print(f'Последовательность Фибоначчи до {n} числа: ')
    for i in range(0, n):
        num_1, num_2 = num_2, num_1 + num_2
        result = print(num_1, end = ' ')
    print()
    return result

# 8 Напишите функцию, которая вычисляет сложное математическое выражение и оберните ее декоратором из пункта 1, 2
@decorator_1
@func_1
def decorator_8(x, y):
    result = x ** 3.14 * y - 5 * x * y ** 8 * (x - y)/10
    return result


decorator_8(5, 10)

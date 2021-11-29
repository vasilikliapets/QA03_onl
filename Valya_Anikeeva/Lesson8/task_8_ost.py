from task_8 import dec_1
from task_8 import dec_2
from task_8 import dec_3
from task_8 import func_name
from task_8 import change
from task_8 import timer


@dec_3
def new_text(text):
    print(text)


new_text('good day')


@change
def argument(*args):
    print(*args)


argument(0, 'x', 1, 'y', 2, 'z')


@timer
@func_name
def fibonachi(e):
    f1 = f2 = 1
    i = 0
    while i < e - 2:
        f_sum = f1 + f2
        f1 = f2
        f2 = f_sum
        i = i + 1
    return f2


@dec_1
@dec_2
def formula(x, y):
    answer = (x * y ** y) / y
    return answer


choice = input(f'Выбери ф-цию:'
               f'\n1 - Фибоначчи'
               f'\n2 - Мат.выражение\n')
while choice:
    if choice == '1':
        e = int(input("Количество элементов = "))
        fibonachi(e)
        break
    elif choice == '2':
        x = float(input("первое число = "))
        y = float(input("второе число = "))
        formula(x, y)
        break

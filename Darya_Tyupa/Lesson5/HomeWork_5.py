# 1 Быки и коровы
import random

# создаём список четырёхзначных чисел с неповторяющимися цифрами

all_cases = []
for i in range(10000):
    temp = str(i).zfill(4)
    if len(set(map(int, temp))) == 4:
        all_cases.append(list(map(int, temp)))

# компьютер загадывает число
number = random.choice(all_cases)


# игрок угадывает число
def guess_number():
    while True:
        guess = input('Введи 4 неповторяющиеся цифры: ')
        if len(guess) != 4 or not guess.isdigit():
            continue
        guess = list(map(int, guess))
        if len(set(guess)) == 4:
            break
    return guess


# сравниваем числа
def check(guess, true_guess):
    bulls = 0
    cows = 0
    for i, num in enumerate(guess):
        if num in true_guess:
            if guess[i] == true_guess[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


# описываем сам ход игры
while True:
    num = guess_number()
    bulls, cows = check(num, number)
    if bulls == 4:
        print('Вы выиграли')
        break
    print('Быки: ', bulls, 'Коровы: ', cows)

# 2
names = str(input())  # вводим имена

names = names.replace(',', '')  # убираем запятые
names_arr = names.split()  # создаём список, чтобы потом считать длину
n = len(names_arr)

if n == 1:
    print(names, 'likes this')
elif n == 2:
    print(names_arr[n - 2], 'and', names_arr[n - 1], 'like this')
elif n == 3:
    print(names_arr[n - 3], ',', names_arr[n - 2], 'and', names_arr[n - 1], 'like this')
elif n > 3:
    print(names_arr[0], ',', names_arr[1], 'and', (n - 2), 'like this')
else:
    print('No one likes this')

# 3 BuzzFuzz
for i in range(1, 100):
    if i % 3 == 0 and i % 5 != 0:  # кратное трём
        print('Fuzz')
    elif i % 5 == 0 and i % 3 != 0:  # кратное пяти
        print('Buzz')
    elif i % 5 == 0 and i % 3 == 0:  # кратное трём и пяти
        print('BuzzFuzz')
    else:
        print(i)

# 4
a = ['a', 'b', 'c']
n = len(a)
for i in range(n):
    a[i] = str(i + 1) + ':' + a[i]  # добавляем к каждому значению списка нумерацию
print(a)

# 5 Проверить, все ли элементы одинаковые
a = [1, 1, 1]
if len(set(a)) == 1 or a == []:
    print(True)
else:
    print(False)

# 6
c = ['true/false', ['caTdoG']]  # нужно проверить подстроку
a = list(c[1][0])  # вычленяем строку
b = []
for i in a:
    if 'A' <= i <= 'Z':
        b.append(i)
if b == []:
    c[0] = True
    c[1] = b
    print(c)
else:
    c[0] = False
    c[1] = b
    print(c)

# 7 Сложить все числа в списке,если список пустой вернуть 0
list_1 = []
if bool(list_1) is True:
    print('сумма чисел равна', sum(list_1))
else:
    print(0)

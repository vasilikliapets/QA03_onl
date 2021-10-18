import random
# 1. Быки и коровы
# компьютер загадыват число
pc_number_list = []

while len(pc_number_list) < 4:
    pc_number_list.append(random.randrange(0, 9))
    pc_number_list = list(set(pc_number_list))

pc_number = ''
for digit in pc_number_list:
    pc_number += str(digit)

#print(pc_number)

# игрок вводит комбинации
def user_input():
    while True:
        user_number = input('Введите 4х значное число: ')
        if len(set(user_number)) < 4:
            print('Число должно быть 4х значным с неповторяющимия символами!')
        else:
            return user_number

# сравнения чисел
# сколько цифр угадано без совпадения с их позициями в тайном числе - количество коров
# сколько угадано вплоть до позиции в тайном числе - количество быков
def check(pc_number, user_number):
    cows = 0
    bulls = 0
    for pos, user_digit in enumerate(user_number):
        if user_digit in pc_number:
            cows += 1
        if user_digit == pc_number[pos]:
            bulls += 1
    return cows, bulls


while True:
    user_number = user_input()
    cows, bulls = check(pc_number, user_number)

    if bulls == 4:
        print('Вы выиграли!')
        break
    else:
        print(f'Коров {cows}, быков {bulls}')


# 2. Like
# ввод имен
names = input('Введите имена через запятую: ')
names_list = names.split(',')
# возвращает строку описывающая количество лайков
if len(names_list) == 1:
    if names_list[0] == '':
        print(f'No one likes this')
    else:
        print(f'{names_list[0]} likes this')
elif len(names_list) == 2:
    print(f'{names_list[0]} and {names_list[1]} like this')
elif len(names_list) == 3:
    print(f'{names_list[0]}, {names_list[1]} and {names_list[2]} like this')
elif len(names_list) > 3:
    print(f'{names_list[0]}, {names_list[1]} and {len(names_list[2:])} others like this')

# 3. BuzzFuzz
# перебирает последовательность от 1 до 100
# Для чисел кратных 3 - "Fuzz"
# для чисел кратных 5  - "Buzz"
# Для чисел которые кратны 3 и 5 - "FuzzBuzz"
# Иначе печатать число.
for i in range(1, 101):
    if i % 15 == 0:
        print('FuzzBuzz')
    elif i % 5 == 0:
        print('Buzz')
    elif i % 3 == 0:
        print('Fuzz')
    else:
        print(i)

# 4. Напишите код, который возьмет список строк и пронумерует их.
# Нумерация начинается с 1, имеет “:” и пробел
def numerate_list(l):
    enumerated_list = []
    for pos, string in enumerate(l, start=1):
        enumerated_list.append(f'{pos}: {string}')
    print(enumerated_list)

numerate_list(['a', 'b', 'c'])

# 5. Проверить, все ли элементы одинаковые
def check_equal(l):
    if len(set(l)) == 1 or len(l) == 0:
        print(True)
    else:
        print(False)

check_equal([1, 1, 1])

# 6. Проверка строки.
# В данной строке проверить все ли буквы в строчном регистре или нет и вернуть список не подходящих.
def check_if_upper(s):
    upper_letters = []
    for i in s:
        if i.isupper():
            upper_letters.append(i)
    if len(upper_letters) != 0:
        print([False, upper_letters])
    else:
        print([True, []])

check_if_upper('doGCat')

# 7. Сложите все числа в списке, они могут быть отрицательными,
# если список пустой вернуть 0
def sum_list(l):
    if not l:
        print(0)
    else:
        print(sum(l))
sum_list([1, 2, 3])

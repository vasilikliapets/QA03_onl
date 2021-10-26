# 1. Быки и коровы
from random import choice
z = '0123456789'
x = choice(z[1:10])  # создание строки из одного случайно выбранного символа из среза строки z (без 0)
for i in range(3):
    z = ''.join(j for j in z if j != x[i])  # удаление из строки z символа который был добавлен в строку x
    x += choice(z)  # добавление к строке x случайно выбранных символов из строки z
while True:
    y = input("Введите 4-х значное число: ")  # ввод числа
    b = 0
    c = 0  # создание переменных для Bulls и Cows
    if len(y) != 4:
        continue
    for i in range(4):
        if x[i] == y[i]:  # проверка наличия цифры месте
            b += 1  # если цифра на месте, то +1 бык
        elif y[i] in x:  # если цифра не на месте, то проверка наличия цифры в загаданном числе
            c += 1  # если цифра есть в числе, то +1 корова
    print(y + ' содержит ' + str(b) + ' бык и ' + str(c) + ' коровы')
    if b == 4:
        print('Вы победили')
        break

# 2. Like. Создать программу, которая, принимая массив имён, возвращает строку описывающая количество лайков
# (как в Facebook).
names = input('Введите имена через запятую: ').split(',')
if len(names) == 1:
    print(f'{names[0]} like this')
elif len(names) == 2:
    print(f'{names[0]} and {names[1]} like this')
elif len(names) == 3:
    print(f'{names[0]}, {names[1]} and {names[2]} like this')
elif len(names) == 4:
    print(f'{names[0]}, {names[1]} and 2 others like this')
else:
    print(f'No one likes this')
    
# 3. Написать программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3 она должна написать:
# "Fuzz" вместо печати числа, для чисел кратных 5 печатать "Buzz", для чисел кратных 3 и 5 надо печатать "FuzzBuzz".
# Иначе печатать число.
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('FuzzBuzz')
    elif i % 3 == 0:
        print('Fuzz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 4. Нумерация строк в списках. Нумерация должна начинатся с 1, иметь “:” и пробел
l41 = ["a", "b", "c"]
length = len(l41)
for i in range(length):
    l41[i] = str(i + 1) + ":" + l41[i]
print(l41)

# 5. Проверить, все ли элементы одинаковые
l51 = [1, 1, 1]
l52 = [1, 2, 1]
l53 = ['a', 'a', 'a']
l54 = []
print(all(i == l51[0] for i in l51))
print(all(i == l52[0] for i in l52))
print(all(i == l53[0] for i in l53))
print(all(i == l54[0] for i in l54))

# 6. В данной подстроке проверить все ли буквы в строчном регистре или нет и вернуть список не подходящих.
str6 = input('Введите слово: ')
if str6.lower() in str6:
    a = [i for i in str6 if i.isupper()]
    print(True, a)
else:
    a = [i for i in str6 if i.isupper()]
    print(False, a)

# 7. Сложить все числа в списке, они могут быть отрицательными, если список пустой вернуть 0.
l1 = []
l2 = [1, 2, 3]
l3 = [1.1, 2.2, 3.3]
l4 = [4, 5, 6]
l5 = range(101)
print(sum(l1))
print(sum(l2))
print(sum(l3))
print(sum(l4))
print(sum(l5))

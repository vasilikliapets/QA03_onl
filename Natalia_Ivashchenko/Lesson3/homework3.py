import random
import math
# 1) a = 10, b=23, поменять значения местами, в “a” записать значение “23”, в “b” - значение “-10”
a = 10
b = 23
a, b = b, -a
print('a =', a)
print('b =', b)
# 2) значение переменной “a” увеличить в 3 раза, значение “b” уменьшить на 3
a = a*3
b = b-3
print('a =', a)
print('b =', b)
# 3) преобразовать значение “a” из целочисленного в float, значение в переменной “b” в строку
a = float(a)
b = str(b)
print('type a -', type(a))
print('type b -', type(b))
# 4) Разделить значение “a” на 11, результат 3 знака после запятой
print('rezultat =', round(a/3, 3))
# 5) Преобразовать значение “b” в float и записать в “c”. Возвести полученное число в 3-ю степень.
c = float(b)
print('stepen =', pow(c, 3))
# 6)Получить случайное число, кратное 3-м
print('chislo =', random.randrange(0, 1000, 3))
# 7) Получить квадратный корень из 100 и возвести в 4 степень
print('otvet =', pow(math.sqrt(100), 4))
# 8)	Строку “Hi guys” вывести 3 раза и в конце добавить “Today” - “Hi guysHi guysHi guysToday”
stroka = 'Hi guys'*3 + 'Today'
print(stroka)
# 9) Получить длину строки из предыдущего задания
print('dlina =', len(stroka))
# 10) Взять предыдущую строку и вывести слово “Today” в прямом и обратном порядке
print('v priamom = ', stroka[-5::1])
print('v obratnom =', stroka[:-6:-1])
# 11)“Hi guysHi guysHi guysToday” вывести каждую 2-ю букву в прямом и обратном порядке
print('v priamom = ', stroka[1::2])
print('v obratnom =', stroka[-2::-2])
# 12) результаты из задания 10, 11 в строку “Task 10: <в прямом>, <в обратном> Task 11: <в прямом>, <в обратном>”
stroka12 = 'Task 10: {pr10}, {obr10} Task 11: {pr11}, {obr11}'.format(pr10=stroka[-5::1], obr10=stroka[:-6:-1], pr11=stroka[1::2], obr11=stroka[-2::-2])
print(stroka12)
# 13) Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя
print('my name is {name}'.format(name='Natalia'))
# 14) Полученную строку в задании 12 вывести:
# а) Каждое слово с большой буквы
# б) все слова в нижнем регистре
# в) все слова в верхнем регистре
print('s bolshoi', stroka12.title())
print('nizni registr', stroka12.lower())
print('verhni registr', stroka12.upper())
# 15)	Посчитать сколько раз слово “Task” встречается в строке из задания 12
print("slovo Task v stroke =", stroka12.count('Task'))

#1) a = 10, b=23, поменять значения местами, чтобы в переменную “a” было записано значение “23”, в “b” - значение “-10”
a, b = 10, 23
a, b = b, a
print(a, b)
#2) значение переменной “a” увеличить в 3 раза, а значение “b” уменьшить на 3
a *= 3
b -= 3
print(a, b)
#3) преобразовать значение “a” из целочисленного в число с плавающей точкой (float), а значение в переменной “b” в строку
a = float(a)
b = str(b)
print(type(a), type(b))
#4) Разделить значение в переменной “a” на 11 и вывести результат с точностью 3 знака после запятой
print(round(a / 11.0, 3))

#5) Преобразовать значение переменной “b” в число с плавающей точкой и записать в переменную “c”. Возвести полученное число в 3-ю степень.
b = float(b)
c = b**3
print(c)

#6) Получить случайное число, кратное 3-м
import random
print(random.randrange(0, 100, 3))

#7) Получить квадратный корень из 100 и возвести в 4 степень
import math
print('Корень из 100 в 4 степени= ', math.sqrt(100)**4)

#8) Строку “Hi guys” вывести 3 раза и в конце добавить “Today”
h = 'Hi guys'
j = 'Today'
h_str = h * 3 + j
print(h_str)

#9) Получить длину строки из предыдущего задания
print(len(h_str))

#10) Взять предыдущую строку и вывести слово “Today” в прямом и обратном порядке
print(h_str[21:26])
print(j[::-1])

#11) “Hi guysHi guysHi guysToday” вывести каждую 2-ю букву в прямом и обратном порядке
print(h_str[::2])
print(h_str[::-2])

#12) Используя форматирования подставить результаты из задания 10 и 11 в следующую строку
#“Task 10: <в прямом>, <в обратном> Task 11: <в прямом>, <в обратном>”
print('Task 10: {today_index}, {revers_today} Task 11: {sentence}, {sentence_revers}'.format(today_index=j[0:6], revers_today=j[::-1], sentence=h_str[::2], sentence_revers=h_str[::-2]))

#13) Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
my_name = "my name is name"
new_name = my_name.replace("name", "Artem", )
print(new_name.replace("Artem", "name", 1))

#14) Полученную строку в задании 12 вывести:
#а) Каждое слово с большой буквы
#б) все слова в нижнем регистре
#в) все слова в верхнем регистре
task14 = "Task 10: Today, yadoT Task 11: H usigyH usoa, ydTygisu Hygi"
print("Title -", task14.title())
print("Lower -", task14.lower())
print("Upper -", task14.upper())

#15) Посчитать сколько раз слово “Task” встречается в строке из задания 12
print(task14.count("Task"))
#1 поменять значение местами
a,b = 10,23
a,b = b,-a
print("a=", a, "b=", b)

#2 “a” увеличить в 3 раза,“b” уменьшить на 3
print("a=", a*3, "b=", b-3)

#3 преобразовать значение “a” в float, а значение “b” в строку
a = float(a)
b = str(b)
print(type(a), type(b))

#4 “a” разделить на 11 и вывести результат с 3 знаками после запятой
print("a=", round(a/11, 3))

#5 “b” преобразовать в число с плавающей точкой и записать в переменную “c”.
# Возвести полученное число в 3-ю степень
c = (float(b)**3)
print("c=", c)

#6 получить случайное число, кратное 3-м
import random

print(random.randrange(0, 50, 3))

#7 квадратный корень из 100 и возвести в 4 степень
import math

print(math.sqrt(100)**4)

#8 “Hi guys” вывести 3 раза и в конце добавить “Today”
stroka = "Hi guys"
print(stroka*3 + "Today")

#9 получить длину строки
print(len(stroka*3 + "Today"))

#10 вывести слово “Today” в прямом и обратном порядке
t = stroka*3 + 'Today'
print(t[21:26])
print(t[:20:-1])

#11 вывести каждую 2-ю букву в прямом и обратном порядке
print(t[::2])
print(t[::-2])

#12 подставить результаты из задания 10 и 11 в строку
r = t[21:26]
f = t[:20:-1]
y = t[::2]
h = t[::-2]
print("Task10: {r}, {f} Task11: {y}, {h}". format(r=r,f=f,y=y,h=h))

#13 в строке “my name is name” вместо 2го “name” вставьте ваше имя
v = 'my name is name'
print(v.replace("is name", "is Valya"))

#14 строку с 12-го задания вывести
m = 'Task10: {r}, {f} Task11: {y}, {h}'. format(r=r,f=f,y=y,h=h)
print("Title\t\t", m.title()) #каждое слово с большой буквы
print("Lower\t\t", m.lower()) #все слова в нижнем регистре
print("Upper\t\t", m.upper()) #все слова в верхнем регистре

#15 посчитать сколько раз слово “Task” встречается в строке из задания 12
print(m.count('Task'))

# поменять значения местами, чтобы в переменную “a” было записано значение “23”, в “b” - значение “-10
import random
a = 10
b = 23
a, b = b, -a
print(a, b)

# значение переменной “a” увеличить в 3 раза, а значение “b” уменьшить на 3
a = 3 * a
b = b-3
print(a, b)

"""преобразовать значение “a” из целочисленного в число с плавающей точкой (float), 
а значение в переменной “b” в строку"""
a = float(a)
b = str(b)
print(a, b)

# Разделить значение в переменной “a” на 11 и вывести результат с точностью 3 знака после запятой
a = a / 11
print(round(a, 3))

# Преобразовать значение переменной “b” в число с плавающей точкой и записать в переменную “c”.
# Возвести полученное число в 3-ю степень.
c = float(b)
print(c**3)

# Получить случайное число, кратное 3-м
print(random.randrange(0, 100000, 3))

# Получить квадратный корень из 100 и возвести в 4 степень
print((100**.5)**4)

# Строку “Hi guys” вывести 3 раза и в конце добавить “Today”
var_guys = "Hi guys" * 3+"Today"
print(var_guys)

# Получить длину строки из предыдущего задания
print(len(var_guys))

# Взять предыдущую строку и вывести слово “Today” в прямом и обратном порядке
var_direct = var_guys[-5:]
var_revers = var_direct[::-1]
print(var_direct)
print(var_revers)

# вывести из var_guys каждую 2-ю букву в прямом и обратном порядке
step_two_letter_dir = var_guys[1::2]
step_two_letter_rev = var_guys[-2::-2]
print(step_two_letter_dir)
print(step_two_letter_rev)

# Используя форматирования подставить результаты из задания 10 и 11 в следующую строку
task_12 = f"Task 10: {var_direct}, {var_revers} Task 11: {step_two_letter_dir},{step_two_letter_rev}"
print(task_12)

# Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.
line_1 = str('my name is name')
print(line_1.replace('is name', 'is Eugene'))

# Полученную строку в задании 12 вывести:
# а) Каждое слово с большой буквы
print(task_12.title())
# б) все слова в нижнем регистре
print(task_12.lower())
# в) все слова в верхнем регистре
print(task_12.upper())

# Посчитать сколько раз слово “Task” встречается в строке из задания 12
print(task_12.count('Task'))

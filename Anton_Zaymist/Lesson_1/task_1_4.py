#  Даны два действительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел.
from math import sqrt
a = 33
b = 20

average_num = (a + b) / 2
geometric_mean = sqrt(a * b)

print("Дано два числа", a, "и", b, "Среднее арифметическое этих чисел =", average_num,
      "среднее геометрическое этих чисел =", geometric_mean)
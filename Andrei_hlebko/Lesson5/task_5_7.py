spis1 = []
spis2 = [1, 2, 3]
spis3 = [1.1, 2.2, 3.3]
spis4 = [4, 5, 6]
spis5 = [-5, -7, -3, -12]

# Длинное решение через цикл for
x = 0
for i in spis2:
    x += i
print(x)

# Короткое решение через sum
print(sum((spis2)))

# Цикл For с range
x = 0
for i in range(101):
    x += i
print(x)

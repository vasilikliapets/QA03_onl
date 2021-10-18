spis1 = []
spis2 = [1, 2, 3]
spis3 = [1.1, 2.2, 3.3]
spis4 = [4, 5, 6]
spis5 = [-5, -7, -3, -12]

#
x = 0
for i in spis2:
    x += i
print(x)

# другой вариант через sum
print(sum(spis2))
print(sum(range(101)))

# Цикл For с range
x = 0
for i in range(101):
    x += i
print(x)

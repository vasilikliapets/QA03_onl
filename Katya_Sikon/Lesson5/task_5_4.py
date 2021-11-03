# Напишите код, который возьмет список строк и пронумерует их.

spis = list(input('Введите список через пробел: ').split())
i = 0

for i in range(0, len(spis)):
    print(i+1, ':', spis[i], end=', ')
    i = i + 1
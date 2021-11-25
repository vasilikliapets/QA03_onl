# 1 игра Быки и коровы
from random import choice
z = '0123456789'
x = choice(z[1:10])                         # создаем строку x из одного случайно выбранного символа из среза строки z
for i in range(3):
    z = ''.join(z.split(x[i]))              # удаляем из строки z символ который добавили в строку x
    x += choice(z)                          # добавляем к строке x случайно выбранные символы из строки z
print('Загадано число:', x)
while True:
    y = input("Введите 4-значное число: ")
    bulls = 0; cows = 0
    for i in range(4):
        if x[i] == y[i]:
            bulls += 1
        elif y[i] in x:
            cows += 1
    print(y + ' содержит ' + str(bulls) + ' быка и ' + str(cows) + ' коровы')
    if bulls == 4:
        print('Вы победили')
        break

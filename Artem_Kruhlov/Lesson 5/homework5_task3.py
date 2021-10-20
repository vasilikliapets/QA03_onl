numbers = range(1, 100) # задаем диапазон чисел от 1 до 100
for i in numbers:
    if i % 3 == 0 and i % 5 == 0: # если делится на 3 и 5 без остатчи
        print('FuzzBuzz')
    elif i % 3 == 0: # делится на 3 без остачи
        print('Fuzz')
    elif i % 5 == 0: # делится на 5 без остачи
        print('Buzz')

    else:
        print(i)
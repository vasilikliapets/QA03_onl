import random
cows_bulls = list(range(0, 9)) # создаем лист от 0 до 9
random.shuffle(cows_bulls) # создаем шафл с генерацией перемешки этих чисел
cows_bulls = cows_bulls[0:4] # делаем срез до 4 чисел
print(cows_bulls)
cows_dict = {1: "Одна корова", 2: "Две коровы", 3: "Три коровы", 4: "Четыри коровы", 0: 'ноль коров'}
bulls_dict = {1: "Один бык", 2: "Два быка", 3: "Три быка", 0: "ноль быков"}
while True:
    guess = list(map(int, list(input()))) #создаем вводимый лист
    bulls = 0
    for i in range(0, 4):

        if cows_bulls[i] == guess[i]: #если положение и цифра совпадает плюсуем 1 к быкам
            bulls += 1

    if bulls == 4: #если 4 числа одинаковы
        print('WIN')
        break
    cows = 0
    for i in cows_bulls:
        if i in guess:
            cows += 1
    print(f'{cows_dict[cows - bulls]}, {bulls_dict[bulls]}')

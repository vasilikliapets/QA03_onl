# В классическом варианте игра рассчитана на двух игроков. Каждый из игроков задумывает и записывает тайное 4-значное число
# с неповторяющимися цифрами. Игрок, который начинает игру по жребию, делает первую попытку отгадать число.
# Попытка — это 4-значное число с неповторяющимися цифрами, сообщаемое противнику.
# Противник сообщает в ответ, сколько цифр угадано без совпадения с их позициями
# в тайном числе (то есть количество коров) и сколько угадано вплоть до позиции в тайном числе (то есть количество быков).
#
# При игре против компьютера игрок вводит комбинации одну за другой, пока не отгадает всю последовательность.
#
# Ваша задача реализовать программу, против которой можно сыграть в "Быки и коровы"

import random


computer_number = list(random.sample(range(0,9), 4))
computer_number_str = ''.join(str(i) for i in computer_number)

bull = 0
cow = 0

while bull != 4:

    person_number = int(input('Введите 4-значное число: '))
    person_number_str = str(person_number)
    print(person_number_str, ':', end=' ')

    cow = 0
    bull = 0

    for i in range(0, len(person_number_str)):
        for j in range(0, len(computer_number_str)):
            if person_number_str[i] == computer_number_str[j] and i != j:
                cow = cow + 1
            elif person_number_str[i] == computer_number_str[j] and i == j:
                bull = bull + 1

    if cow == 0 and bull == 0:
        print(cow, 'коров и ', bull, ' быков')
    elif cow == 1 and bull == 0:
        print(cow, 'корова и ', bull, ' быков')
    elif cow == 0 and bull == 1:
        print(cow, 'коров и ', bull, ' бык')
    elif cow >= 2 and bull == 0:
        print(cow, 'коровы и ', bull, ' быков')
    elif cow == 1 and bull == 1:
        print(cow, 'корова и ', bull, ' бык')
    elif cow >= 2 and bull == 1:
        print(cow, 'коровы и ', bull, ' бык')
    elif cow == 1 and bull >= 2:
        print(cow, 'корова и ', bull, ' быка')
    elif cow >= 2 and bull >= 2:
        print(cow, 'коровы и ', bull, ' быка')
    elif cow == 0 and bull >= 2:
        print(cow, 'коровы и ', bull, ' быка')

else:
    print('Вы выиграли!')
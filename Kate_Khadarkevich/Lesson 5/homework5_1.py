computer_number = 1587  # число компьютера
computer_number_l = str(computer_number)

cow = 0
bull = 0

while bull != 4:
    print('Введите четырехзначное число с неповторяющимися цифрами:')  # игрок вводит число
    player_number = int(input())
    player_number_l = str(player_number)

    cow = 0
    bull = 0

    for i in range(len(player_number_l)):
        for g in range(len(player_number_l)):
            if computer_number_l[i] == player_number_l[g] and i != g:
                cow = cow + 1
            if computer_number_l[i] == player_number_l[g] and i == g:
                bull = bull + 1
    print('Чило коров:', cow)
    print('Число быков:', bull)
else:
    print('Вы выиграли!')

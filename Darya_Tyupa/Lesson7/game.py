b = [['', '', ''], ['', '', ''], ['', '', '']]
game = False


def create_board(b):
    '''
    This function draws the board
    '''
    print('  ', b[0][0], '|', b[0][1], '|', b[0][2], ' ')
    print('------------')
    print('  ', b[1][0], '|', b[1][1], '|', b[1][2], ' ')
    print('------------')
    print('  ', b[2][0], '|', b[2][1], '|', b[2][2], ' ')


def player_step(a):
    '''
    This function takes the player's turn
    '''
    global b
    i = input('Введите координаты: ')
    i = list(map(int, i.split(',')))
    b[i[0] - 1][i[1] - 1] = a
    return b


def computer_step(c):
    '''
    This function creates a computer move
    '''
    global b
    import random
    while True:
        i = random.randrange(0, 3)
        j = random.randrange(0, 3)
        if b[i][j] == '':
            b[i][j] = c
            break
    return b


def check_the_winner(b, a, c):
    '''
    This function checks the win
    '''
    global game
    win = (
        set(b[0]), set(b[1]), set(b[2]), {b[0][0], b[1][0], b[2][0]}, {b[0][1], b[1][1], b[2][1]},
        {b[0][2], b[1][2], b[2][2]},
        {b[0][0], b[1][1], b[2][2]}, {b[2][0], b[1][1], b[0][2]})  # все варианты побед
    for i in win:
        if len(i) == 1:
            if a in i:
                print('Выиграл игрок')
                game = True
                return game
            elif c in i:
                print('Выиграл компьютер')
                game = True
                return game


def offer_next_game():
    '''
    This function for choosing the next option after game
    '''
    global game
    global b
    print('''Игра окончена:
    1) Сыграть ещё одну партию
    2) Выйти из программы
    ''')
    choice = int(input())
    if choice == 1:
        game = False  # обнуляем статус игры
        b = [['', '', ''], ['', '', ''], ['', '', '']]  # обнуляем результат
        main()
    else:
        print('Вы вышли из программы')


def main():
    '''
    This is the main function describes the whole game process
    '''
    global b
    global game
    create_board(b)
    print('''Выберите команду:
    1) Крестики
    2) Нолики ''')
    a = int(input())  # определяем кто за крестики, кто за нолики
    if a == 1:
        a = 'X'
        c = 'O'
    else:
        a = 'O'
        c = 'X'
    while game == False:
        player_step(a)
        check_the_winner(b, a, c)
        if game == True:
            create_board(b)
            break
        computer_step(c)
        check_the_winner(b, a, c)
        create_board(b)
    offer_next_game()


if __name__ == '__main__':
    main()

import random
list_of_number = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
random.shuffle(list_of_number)
b = list_of_number[0:4]
bulls = 0
while bulls < 4:
    cows = 0
    bulls = 0
    gamer_number = input('Введите число: ')
    c = list(str(gamer_number))
    if len(c) != 4:
        continue
    else:
        if c[0] == c[1] or c[1] == c[2] or c[2] == c[3] or c[0] == c[2] or c[1] == c[3]:
            continue
        else:
            if c[0] == b[0]:
                bulls += 1
            else:
                if c[0] == b[1] or c[0] == b[2] or c[0] == b[3]:
                    cows += 1
            if c[1] == b[1]:
                bulls += 1
            else:
                if c[1] == b[0] or c[1] == b[2] or c[1] == b[3]:
                    cows += 1
            if c[2] == b[2]:
                bulls += 1
            else:
                if c[2] == b[1] or c[2] == b[0] or c[2] == b[3]:
                    cows += 1
            if c[3] == b[3]:
                bulls += 1
            else:
                if c[3] == b[0] or c[3] == b[1] or c[3] == b[2]:
                    cows += 1
            print(f'{cows} cows, {bulls} bulls')
print('Ты победил!')

# взял готовое решение, в алгоритме разобрался, но не хватает времени реализовать.
import random

all_cases = []
for i in range(10000):
    temp = str(i).zfill(4)
    if len(set(map(int, temp))) == 4:
        all_cases.append(list(map(int, temp)))

number = random.choice(all_cases)


def guess_number():
    while True:
        guess = input('Введи 4 неповторяющиеся цифры: ')
        if len(guess) != 4 or not guess.isdigit():
            continue
        guess = list(map(int, guess))
        if len(set(guess)) == 4:
            break
    return guess

def check(guess, true_guess):
    bulls = 0
    cows = 0
    for i, num in enumerate(guess):
        if num in true_guess:
            if guess[i] == true_guess[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows


while True:
    num = guess_number()
    bulls, cows = check(num, number)
    if bulls == 4:
        print('Вы выиграли!')
        break
    print('Быки: ', bulls, 'Коровы: ', cows)

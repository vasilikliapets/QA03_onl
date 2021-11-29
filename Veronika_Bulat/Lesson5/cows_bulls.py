import random

# 1. Bulls & Cows

random_num = ''
while len(set(random_num)) != 4:
    var_int = str(random.randrange(0, 9))
    if random_num.find(var_int):
        random_num += var_int


def check(number, check_number):
    num = list(str(number))
    guess_num = list(str(check_number))
    if len(set(guess_num)) == 4:
        bulls = 0
        cows = 0
        for v in num:
            if v in guess_num:
                if guess_num.index(v) == num.index(v):
                    bulls += 1
                else:
                    cows += 1
        print('Bulls - {}, Cows - {}'.format(bulls, cows))
    else:
        print('Invalid number')


guess_number = input('Enter number: ')

while random_num != guess_number:
    check(random_num, guess_number)
    guess_number = input('Enter number: ')
else:
    print('Guessed!')

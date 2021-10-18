# BuzzFuzz

for i in range(1, 101):
    if i%3==0:
        print('Fuzz')     # не кратные 3
    elif i%5==0:
        print('Buzz')     # не кратные 5
    elif i%3==0 and i%5==0:     # не кратные и 3 и 5
        print('FuzzBuzz')
    else:
        print(i)

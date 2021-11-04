# 3. FuzzBuzz

for integer in range(1, 100):
    if integer % 5 == 0 and integer % 3 == 0:
        integer = 'FuzzBuzz'
    elif integer % 3 == 0:
        integer = 'Buzz'
    elif integer % 5 == 0:
        integer = 'Fuzz'
    print(integer)

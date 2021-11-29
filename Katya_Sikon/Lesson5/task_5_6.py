# Проверка строки. В данной подстроке проверить все ли буквы в строчном регистре или нет и вернуть список не подходящих.

str = input('Введите строку: ')
wrong_letter = []

for i in range(0, len(str)):
    if str[i].isupper():
        wrong_letter = wrong_letter + list(str[i])

print(len(wrong_letter) == 0, wrong_letter)

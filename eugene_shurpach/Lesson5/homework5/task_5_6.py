# В данной подстроке проверить все ли буквы в строчном регистре или нет и вернуть список не подходящих
line = input('Type a word: ')  # ввод слова
a = len(line)
b = []
for i in range(a):  # ограничение цикла по длине строки
    if "A" <= line[i] <= "Z":  # проверка вхожести в заглавные
        b.append(line[i])  # добавление заглавных букв в список b
print(f'{str.islower(line)}, {b}')

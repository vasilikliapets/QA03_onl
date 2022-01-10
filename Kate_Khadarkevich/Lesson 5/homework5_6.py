# Проверка строки. В данной подстроке проверить все ли буквы в строчном регистре или нет и вернуть список не подходящих.
# dogcat => [True, []]
# doGCat => [False, ['G', 'C']]

word = 'doGCat'
big_let = []
for i in word:
    if i.isupper():
        big_let.append(i)
if len(big_let) > 0:
    print(False, big_let)
else:
    print(True, big_let)



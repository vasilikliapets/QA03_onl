# 3 программа, которая перебирает последовательность от 1 до 100. Для чисел
# кратных 3 - написать: Fuzz вместо печати числа, а для чисел кратных 5 - Buzz.
# Для чисел которые кратны 3 и 5 - печатать FuzzBuzz. Иначе печатать число
for i in range(1,100):
    if i%3 == 0:
        print('Fuzz')
    elif i%5 == 0:
        print('Buzz')
    elif i%5 == 0 and i%3 == 0:
        print('BuzzFuzz')
    else:
        print(i)

# 4 Напишите код, который возьмет список строк и пронумерует их
spisok = ['a', 'b', 'c']
a = len(spisok)
for i in range(a):
    spisok[i] = str(i+1)+': '+spisok[i]
print(spisok)

# 5 Проверить, все ли элементы одинаковые
my_list = [1, 1, 1]
print(all(i == my_list[0] for i in my_list))

# 6 проверить все ли буквы в строчном регистре или нет и вернуть список не подходящих
reg = 'doGCat'
if reg.lower() in reg:
    a = [i for i in reg if i.isupper()]
    print(True, a)
else:
    a = [i for i in reg if i.isupper()]
    print(False, a)

# 7 Сложите все числа в списке, могут быть отрицательными. Если список пустой вернуть 0
list_1 = [1, 2, 3]
print(sum(list_1))



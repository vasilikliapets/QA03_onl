# 2)
# Like
# Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).
# Примеры:
# Введите имена через запятую: "Ann"
# -> "Ann likes this"
# Введите имена через запятую: "Ann, Alex"
# -> "Ann and Alex like this"
# Введите имена через запятую: "Ann, Alex, Mark"
# -> "Ann, Alex and Mark like this"
# Введите имена через запятую: "Ann, Alex, Mark, Max"
# -> "Ann, Alex and 2 others like this"
# Если ничего не вводить должен быть вывод:
# -> "No one likes this"
names = input("Введите имена через запятую: ").split()
if len(names) == 1:
    print(f"{names[0]} likes this")
elif len(names) == 2:
    print(f"{names[0]} and {names[1]} like this")
elif len(names) == 3:
    print(f"{names[0]},{names[1]} and {names[2]} like this")
elif len(names) > 3:
    print(f"{names[0]} {names[1]} and {len(names) - 2} other like this")
else:
    print("No one likes this")

# 3)
# BuzzFuzz
# Напишите программу, которая перебирает последовательность от 1 до 100. Для чисел кратных 3 она должна написать:
# "Fuzz" вместо печати числа, а для чисел кратных 5  печатать "Buzz". Для чисел которые кратны 3 и 5 надо печатать
# "FuzzBuzz". Иначе печатать число.
# Вывод должен быть следующим:
# 1
# 2
# fuzz
# 4
# buzz
# fuzz
# 7
# 8
# ..
for i in range(0, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FuzzBuzz")
        continue
    if i % 3 == 0:
        print("Fuzz")
        continue
    if i % 5 == 0:
        print("Buzz")
        continue
    print(i)

# 4) Напишите код, который возьмет список строк и пронумерует их.
# Нумерация начинается с 1, имеет “:” и пробел
# [] => []
# ["a", "b", "c"] => ["1: a", "2: b", "3: c"]
list_4 = ["a", "b", "c"]
a_4 = []
for i, item in enumerate(list_4):
    b = [str(i + 1) + ':' + item]
    a_4.extend(b)
print(a_4)

# 5) Проверить, все ли элементы одинаковые
# [1, 1, 1] == True
# [1, 2, 1] == False
# ['a', 'a', 'a'] == True
# [] == True
a_5 = [2, 2, 2]
if len(set(a_5)) == 1 or a_5 == []:
    print(True)
else:
    print(False)
# 6) Проверка строки. В данной подстроке проверить все ли буквы в строчном регистре или нет и вернуть список не подходящих.
# dogcat => [True, []]
# doGCat => [False, ['G', 'C']]
a_6 = "doGCat"
let_6 = []
for i in a_6:
    if i.isupper():
        let_6.append(i)
if len(let_6) == 0:
    print(True, let_6)
else:
    print(False, let_6)

# 7) Сложите все числа в списке, они могут быть отрицательными, если список пустой вернуть 0.
# [] == 0
# [1, 2, 3] == 6
# [1.1, 2.2, 3.3] == 6.6
# [4, 5, 6] == 15
list_7 = range(101)
if sum == 0:
    print("0")
else:
    s = sum(list_7)
    print(s)

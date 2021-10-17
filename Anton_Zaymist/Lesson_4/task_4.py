import collections

# 1) Перевести строку в массив
# "Robin Singh" => ["Robin”, “Singh"]
# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
a = "Robin Singh"
b = "I love arrays they are my favorite"

a = sorted(a.split(' '))
b = sorted(b.split(' '))
print(a, b)
# 2) Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
a = ["Ivan", "Ivanou"]
b = "Minsk Belarus"
a = " ".join(a)
print("Привет,", a, "! Добро пожаловать в", b)

# 3) Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку
# => "I love arrays they are my favorite"
list_1 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(" ".join(list_1))

# 4) Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
list_2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_2.insert(2, "s")
list_2.remove(6)
print(list_2)
# 5) Есть 2 словаря
#                  a = { 'a': 1, 'b': 2, 'c': 3}
#                  b = { 'c': 3, 'd': 4,'e': “”}
#
# 6. Изменить значение под одним из ключей и вывести все значения
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': ''}
# 1. Создайте словарь, который будет содержать в себе все элементы обоих словарей
c = {**a, **b}
print(c)
# 2. Обновите словарь “a” элементами из словаря “b”
a.update(b)
print(a)
# 3. Проверить что все значения в словаре “a” не пустые либо не равны нулю
print(all(a.values()))
# 4. Проверить что есть хотя бы одно пустое значение (результат выполнения должен быть True)
print(any(a.values()))
# 5. Отсортировать словарь по алфавиту в обратном порядке
print(dict(sorted(a.items(), reverse=True)))
# 6. Изменить значение под одним из ключей и вывести все значения
a['e'] = 33
print(a)

# 6) Создать список из элементов list_a = [1,2,3,4,4,5,2,1,8]
list_a = [1, 2, 3, 4, 4, 5, 2, 1, 8]
# Вывести только уникальные значения и сохранить их в отдельную переменную
set_list = list(set(list_a))
print(set_list)
# Добавить в полученный объект значение 22
set_list.append(22)
print(set_list)
# Сделать list_a неизменяемым
list_b = list(list_a)
# или
list_a = tuple(list_a)
# Измерить его длинну
print(len(list_a))

# Задачи на закрепление форматирования:
# 1) Есть переменные a=10, b=25
# Вывести 'Summ is <сумма этих чисел> and diff = <их разница>.'
# При решении задачи использовать оба способа форматирования
a = 10
b = 25
summ_1 = a + b
diff_1 = a - b
print(f'Summ is {summ_1} and diff = {diff_1}')
print('Summ is {} and diff = {}'.format(summ_1, diff_1))

# 2) Есть список list_of_children = [“Sasha”, “Vasia”, “Nikalai”]
# Вывести “First child is <первое имя из списка>, second is “<второе>”, and last one – “<третье>””
list_of_children = ["Sasha", "Vasia", "Nikalai"]
print('First child is', list_of_children[0], ', second is', list_of_children[1], 'and last one – ', list_of_children[2])

# *1) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару,
# кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
tsk_list = [1, 5, 2, 9, 2, 9, 1]
count = collections.Counter(tsk_list)
print(min(count, key=count.get))

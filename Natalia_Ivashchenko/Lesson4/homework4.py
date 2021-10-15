import collections

# 1. Перевести строку в массив
string1 = 'Robin Singh'
string2 = 'I love arrays they are my favorite'
print(string1.split())
print(string2.split())

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
name = ['Ivan', 'Ivanou']
city = 'Minsk'
country = 'Belarus'
print(f"Привет, {' '.join(name)}! Добро пожаловать в {city} {country}")

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
arr = ["I", "love", "arrays", "they", "are", "my", "favorite"]
string3 = ' '.join(arr)
print(string3)

# 4. Создайте список из 10 элементов,
# вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
list1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
list1.insert(2, 'new_word')
print(list1)
del list1[6]
print(list1)

# 5. 2 словаря
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': ""}

# Создайте словарь, который будет содержать в себе все элементы обоих словарей
c = {**a, **b}
print(c)
# Обновите словарь “a” элементами из словаря “b”
a.update(b)
print(a)
# Проверить что все значения в словаре “a” не пустые либо не равны нулю
print(all(a.values()))
# Проверить что есть хотя бы одно пустое значение (результат выполнения должен быть True)
print(any(a.values()))
# Отсортировать словарь по алфавиту в обратном порядке
print(dict(sorted(a.items(), reverse=True)))

# Изменить значение под одним из ключей и вывести все значения
a['d'] = 5
print(a)

# 6. Создать список из элементов list_a = [1,2,3,4,4,5,2,1,8]
list_a = [1, 2, 3, 4, 4, 5, 2, 1, 8]
# Вывести только уникальные значения и сохранить их в отдельную переменную
list_b = set(list_a)
print(list_b)
# Добавить в полученный объект значение 22
list_b.add(22)
print(list_b)
# Сделать list_a неизменяемым
list_a = tuple(list_a)
# Измерить его длинну
print(len(list_a))

# форматирования:
a = 10
b = 25
# Вывести 'Summ is <сумма этих чисел> and diff = <их разница>.
print('Summ is {summ} and diff = {diff}'.format(summ=a + b, diff=a - b))

list_of_children = ["Sasha", "Vasia", "Nikalai"]
# Вывести “First child is <первое имя из списка>, second is “<второе>”, and last one – “<третье>””
print(f"First child is {list_of_children[0]}, second is {list_of_children[1]}, and last one – {list_of_children[2]}")

# Массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число
arr2 = [1, 5, 2, 9, 2, 9, 1]
unique_number = collections.Counter(arr2)
print('unique_number =', min(unique_number, key=unique_number.get))

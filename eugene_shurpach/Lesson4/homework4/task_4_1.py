# Перевести строку в массив
line_1 = str('Robin Singh')
line_2 = str('I love arrays they are my favorite')
list_1 = (line_1.split())
list_2 = (line_2.split())
print(f"{list_1}\n{list_2}")

# Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
name = ['Ivan', 'Ivanou']
country = str('Belarus')
city = str('Minsk')
print(f"Привет, {name[0]} {name[1]}! Добро пожаловать в {city} {country}")

# Дан список  сделайте из него строку
list_task_4_3 = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
str_task_4_3 = ' '.join(list_task_4_3)
print(str_task_4_3)

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
list_task_4_4 = [1, 2, 3, 4, 5, 5.1, 7, 8, 9, 10]
list_task_4_4.insert(2, 11)
del list_task_4_4[6]
print(list_task_4_4)

# task 5
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': ""}
# 1. Создайте словарь, который будет содержать в себе все элементы обоих словарей
c = {**a, **b}
print(c)

# 2. Обновите словарь “a” элементами из словаря “b”
a.update(b)
print(a)

# 3. Проверить что все значения в словаре “a” не пустые либо не равны нулю
empty = False
print(empty in a.values())

# 4. Проверить что есть хотя бы одно пустое значение (результат выполнения должен быть True)
print(any(a))

#   5. Отсортировать словарь по алфавиту в обратном порядке
print(sorted(a.items(), reverse=True))

#  6. Изменить значение под одним из ключей и вывести все значения
a['a'] = 666
print(a)

# task_4_6 Создать список из элементов
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

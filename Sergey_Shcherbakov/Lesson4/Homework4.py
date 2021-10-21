# 1. Перевод строки в массив
string1 = 'Robin Singh'
string2 = 'I love arrays they are my favorite'
name_surname = string1.split()
arrays = string2.split()
print(name_surname, arrays)

# 2. Печать текста
a = ['Ivan', 'Ivanou']
b = 'Minsk'
c = 'Belarus'
print("Привет, {name_surname2}! Добро пожаловать в {city} {country}".format(name_surname2=' '.join(a), city=b,
                                                                            country=c))

# 3. Сделать из списка строку
l3 = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
print(' '.join(l3))

# 4. Создать список из 10 элементов, вставить на 3-ю позицию новое значение, удалить элемент из списка под индексом 6
l4 = ['a', 1, 'b', 3, 'c', 4, 'd', 5, 'e', 6]
l4.insert(3, 2)  # Вставка значения на 3-ю позицию
del l4[6]  # Удаление элемента из списка под индексом 6
print(l4)

# 5.1 Создать словарь, который будет содержать в себе все элементы обоих словарей
a5 = {'a': 1, 'b': 2, 'c': 3}
b5 = {'c': 3, 'd': 4, 'e': ""}
c5 = {**a5, **b5}
print(c5)

# 5.2 Обновить словарь "a5" элементами из словаря "b5"
a5.update(b5)
print(a5)

# 5.3 Проверить что все значения в словаре "a5" не пустые либо не равны нулю
print(all(a5.values()))

# 5.4 Проверить, что есть хотя бы одно пустое значение (результат выполнения должен быть True)
print(any(a5.values()))

# 5.5 Отсортировать словарь по алфавиту в обратном порядке
print(dict(sorted(a5.items(), reverse=True)))

# 5.6 Изменить значение под одним из ключей и вывести все значения
a5['e'] = 5
print(a5)

# 6. a) Создать список из элементов. Вывести только уникальные значения и сохранить их в отдельную переменную
list_a = [1, 2, 3, 4, 4, 5, 2, 1, 8]
set_a6 = set(list_a)
print(set_a6)

# 6. б) Добавить в полученный объект значение 22
set_a6.add(22)
print(set_a6)

# 6. в) Сделать list_a неизменяемым
list_a = tuple(list_a)
print(type(list_a))

# 6. в) Измерить его длину
dlina = len(list_a)
print(dlina)

# 7.1 Задачи на закрепление форматирования:
# Есть переменные, Вывести 'Summ is <сумма этих чисел> and diff = <их разница>.' При решении задачи использовать оба
# способа форматирования
a7 = 10
b7 = 25
print('Summ is {summa} and diff = {raznica}'.format(summa=a7 + b7, raznica=b7 - a7))
print(f'Summ is {a7 + b7} and diff = {b7 - a7}.')

# 7.2 Есть список. Вывести "First child is <первое имя из списка>, second is "<второе>", and last one – "<третье>""
list_of_children = ["Sasha", "Vasia", "Nikalai"]
print("First child is {first}, second is {second}, and last one – {third}.".format(first="Sasha", second="Vasia",
                                                                                   third="Nikalai"))

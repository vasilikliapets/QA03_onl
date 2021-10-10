# 1. Перевести строку в массив
#"Robin Singh" => ["Robin”, “Singh"]
#"I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
string1 = "Robin Singh"
string1 = string1.split()
print("первый массив из строки:", string1)

string2 = "I love arrays they are my favorite"
string2 = string2.split()
print("первый массив из строки:", string2)

# 2. Дан список: [‘Ivan’, ‘Ivanou’], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
a1 = ["Ivan", "Ivanou"]
print("Привет,{a1}! Добро пожаловать в {a2} {a3}".format(a1=' '.join(a1), a2="Minsk", a3="Belarus"))

# 3. Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"] сделайте из него строку => "I love arrays they are my favorite"
b=["I", "love", "arrays", "they", "are", "my", "favorite"]
b=' '.join(b)
print(b)

# 4. Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение, удалите элемент из списка под индексом 6
list4= [ 10, 11, 34, 67, 88, 55, 99, 66, 56, 44]
print("начальный список:", list4)
list4[3]=100
del list4[5]
print("измененный список:", list4)

# 5. Есть 2 словаря
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': ""}
# Создайте словарь, который будет содержать в себе все элементы обоих словарей
z = {**a, **b}
print("объединенный словарь:", z)
# Обновите словарь “a” элементами из словаря “b”
a.update(b)
print("обновленный словарь:", a)
# Проверить что все значения в словаре “a” не пустые либо не равны нулю
y = ['',{},[],None,0]
print(y[0] not in a.values() and y[1] not in a.values() and y[2] not in a.values() and y[3] not in a.values() and y[4] not in a.values())

# Проверить что есть хотя бы одно пустое значение (результат выполнения должен быть True)
print(y[0] not in a.values() or y[1] not in a.values() or y[2] not in a.values() or y[3] not in a.values() or y[4] not in a.values())

# Отсортировать словарь по алфавиту в обратном порядке
a_new = dict(sorted(a.items(), reverse = True))
print("отсортированный в обратном порядке:", a_new)
# Изменить значение под одним из ключей и вывести все значения
a['c']=99
print("словарь после изменения одного из значений:", a)
# 6. Создать список из элементов
list_a = [1,2,3,4,4,5,2,1,8]
# Вывести только уникальные значения и сохранить их в отдельную переменную
list_new=set(list_a)
print("уникальные значения списка:", list_new)
# Добавить в полученный объект значение 22
list_new.add(22)
print("обновленный список:", list_new)
# Сделать list_a неизменяемым
list_a=tuple(list_a)
# Измерить его длинну
print("длина списка:", len(list_a))


#Задачи на закрепление форматирования:
# 1. Есть переменные a=10, b=25
#Вывести 'Summ is <сумма этих чисел> and diff = <их разница>.'
#При решении задачи использовать оба способа форматирования
a=10
b=25
summ=a+b
diff=a-b
print('Summ is', summ,'and diff =', diff)
print('Summ is {} and diff={}'.format(summ,diff))

# 2. Есть список list_of_children = [“Sasha”, “Vasia”, “Nikalai”]
#Вывести “First child is <первое имя из списка>, second is “<второе>”, and last one – “<третье>””
list_of_children = ["Sasha", "Vasia", "Nikalai"]
print('First child is', list_of_children[0],', second is', list_of_children[1],', and last one -', list_of_children[2])



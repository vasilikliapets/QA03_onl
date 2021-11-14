#1 Перевести строку в массив
st1 = "Robin Singh"
st2 = "I love arrays they are my favorite"

print (st1.split())
print (st2.split())

#2 Дан список и 2 строки.
# Напечатать текст “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
name = ['Ivan', 'Ivanou']
stroka1 = "Minsk"
stroka2 = "Belarus"
print(f"Привет, {name[0]} {name[1]}! Добро пожаловать в {stroka1} {stroka2}")

#3 Дан список. Сделайте из него строку
spisok = ['I', 'love', 'arrays', 'they', 'are', 'my', 'favorite']
print(' '.join(spisok))

#4 Создайте список из 10 элементов
list1 = [1,2,3,4,5,6,7,8,9,10]
list1.insert(2, 0) #вставьте на 3-ю позицию новое значение
del list1[6] #удалите элемент из списка под индексом 6
print(list1)

#5 Есть 2 словаря
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4,'e': ""}

#5.1 Создайте словарь, который будет содержать в себе все элементы обоих словарей
print({**a,**b})

#5.2 Обновите словарь “a” элементами из словаря “b”
print(a.update(b))

#5.3 Проверить что все значения в словаре “a” не пустые либо не равны нулю
print(all(a.values()))

#5.4 Проверить что есть хотя бы одно пустое значение
print(any(a))

#5.5 Отсортировать словарь по алфавиту в обратном порядке
for k, v in sorted(a.items(), reverse=True):
    print(k, v)

#5.6
a['d'] = 5
print(a)

#6 Создать список из элементов list_a = [1,2,3,4,4,5,2,1,8]
list_a = [1,2,3,4,4,5,2,1,8]
#a Вывести только уникальные значения и сохранить их в отдельную переменную
list_x = list(set(list_a))
print("уникальные значения:", list_x)

#b Добавить в полученный объект значение 22
list_x.add('22')
print(list_x)

#c Сделать list_a неизменяемым
list_a = tuple(list_a)

#d Измерить его длинну
print("длина:", len(list_a))

#Закрепление форматирования:
#1 Есть переменные a=10, b=25
# Вывести Summ is <сумма этих чисел> and diff = <их разница>
a= 10
b= 25
summ = a+b
diff = a-b
print(f'Summ is {summ} and diff = {diff}')
print("Summ is {summ} and diff = {diff}".format(summ=summ,diff=diff))

#2 Есть список list_of_children = [“Sasha”, “Vasia”, “Nikalai”]
# Вывести “First child is <первое имя из списка>, second is "<второе>”, and last one – "<третье>"
name = ["Sasha", "Vasia", "Nikalai"]
print(f"First child is {name [0]}, second is {name[1]}, and last one - {name[2]}")

#1*) Вам передан массив чисел. Известно, что каждое число в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
# Напишите программу, которая будет выводить уникальное число

massiv = [1, 5, 2, 9, 2, 9, 1]
import collections
count = collections.Counter(massiv) #подсчет кол-ва каждого значения
print(min(count, key=count.get))

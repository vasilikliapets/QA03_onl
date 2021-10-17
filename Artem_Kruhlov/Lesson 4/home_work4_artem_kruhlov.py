#1
str_1 = "Robin Singh"
str_2 = "I love arrays they are my favorite"

arr_1 = str_1.split()
arr_2 = str_2.split()    # переводим строку в массив

print(arr_1)
print(arr_2)

#2
name_surname = ['Ivan','Ivanov']
city = 'Minsk'
country = 'Belarus'
print(f'“Привет, {name_surname[0]} {name_surname[1]}! Добро пожаловать в {city} {country}”') # подставляем значение в предложение

#3
arr2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]

str_3 = ' '.join(arr2)     # преводим список в строку

print(str_3)

#4
arr3 = [1, 2, 3, 10, 16, 7, 'Global', 'Albion', 'b', 32]

arr3.insert(2, 'new')     # добавляем на 3 позицию новое слово
del arr3[6]               # удаляем элемент под индексом 6

print(arr3)

#5
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4, 'e': ''}

ab = {**a, **b} # словарь, который будет содержать в себе все элементы обоих словарей
print(ab)
a.update(b) # Обновите словарь “a” элементами из словаря “b”
print(a)

print(all(a.values())) # Проверить что все значения в словаре “a” не пустые либо не равны нулю
print('' in a.values()) # Проверить что есть хотя бы одно пустое значение

for k, v in sorted(a.items(), reverse=True):    # сортируем по алфавиту в обратном порядке
    print(k, v)

a['c'] = 5          # изменяем значение одного ключа
print(a.values())    # выводим все значения

#6
list_a = [1,2,3,4,4,5,2,1,8]

list_b = list(set(list_a))    # выводим только уникальтые значения и оставляем списком
print(list_b)

list_b.append(22)           # добавляем значение
print(list_b)

list_a = tuple(list_a)        # делаем переменную неизменяемой
print('Длина объекта =', len(list_a))     #измеряем длину

#Задачи на закрепление форматирования
#1
a = 10
b = 25

summ = a + b
diff = a - b

print(f'Summ is {summ} and diff={diff}')
print('Summ is {} and diff={}'.format(summ,diff))
#2
list_of_children=['Sasha', 'Vasia', 'Nikalai']

print('First child is, ' + list_of_children[0] + ' second is ' + list_of_children[1] + ' and last one – ' + list_of_children[2])

# 1**
list_1 = [1, 5, 2, 9, 2, 9, 1]
import collections
list_count = collections.Counter(list_1) # считаем количество каждого значения
print(min(list_count, key=list_count.get))
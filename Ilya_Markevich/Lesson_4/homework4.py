txt1 = 'Robin Singh'
txt2 = 'I love arrays they are my favorite'
result1 = txt1.split()
result2 = txt2.split()
print(result1, result2) # 1. Перевести строку в массив

name = ['Ivan', 'Ivanou']
city = 'Minsk'
country = 'Belarus'
print('Привет,{a}!Добро пожаловать в {b} {c}'.format (a=' '.join(name),b=city,c=country )) #2 Список + строки

a = ["I", "love", "arrays", "they", "are", "my", "favorite"]
str_a = ' '.join(a)
print(str_a) # 3 Перевести массив в строку

l4 = list(range(1, 11))
l4.insert(2, 'Test')
l4.pop(6)
print(l4) # 4 Вставка и удаление в массив

a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': ''}
z = {**a, **b}
print(z) # 5.1 Объеденить оба

a.update(b)
print(a) # 5.2 Обновите словарь “a” элементами из словаря “b”

print(all(a.values())) # 5.3 Проверка есть ли пустые либо =0 значения в а

print(any(a.values())) #5.4 Проверить что есть хотя бы одно пустое значение

print(dict(sorted(a.items(), reverse = True))) #5.5 Сортиврока по алфавиту в обратном порядке

a['d'] = 'zamena'
print(a) #5.5 Заменить значение массива и вывести весь

list_a = [1,2,3,4,4,5,2,1,8]
list_a_1 = set(list_a)
print(list_a_1) #6.a Уникальные значения в отдельной переменной

list_a.append (22)
print(list_a) #6.b Добавить в лист 22

list_a = tuple(list_a)
print(type(list_a)) #6.c Сделать неизменяемым

print(len(list_a)) #6d Измерять длинну

# Задачи на закрепление форматирования:
per_1 = 10
per_2 =25
print('Summ is {s} and diff = {d}.'.format(s=per_1+per_2, d=per_1-per_2)) #1 format
print(f'Summ is {per_1+per_2} and diff = {per_1-per_2}.') #1 f-strings

list_of_children = ['Sasha', 'Vasia', 'Nikalai']
print('First child is {man_1}, second is {man_2}, and last one - {man_3}'.format(man_1=list_of_children[0], man_2=list_of_children[1],man_3= list_of_children[2]))
# Элементы списка в строке

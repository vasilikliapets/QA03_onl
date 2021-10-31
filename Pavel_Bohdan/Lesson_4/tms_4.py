#1
str_1 = "Robin Singh"
str_2 = "I love arrays they are my favorite"

str_1 = str_1.split(" ")
str_2 = str_2.split(" ")
print(str_1, str_2)

#2
lst_1 = ['Ivan', 'Ivanou']
str_3 = 'Minsk'
str_4 = 'Belarus'
print(f'Привет {lst_1[0]} {lst_1[1]}! Добро пожаловать в {str_3} {str_4}')

#3
lst_2 = ["I", "love", "arrays", "they", "are", "my", "favorite"]
lst_2 = ' '.join(lst_2)
print(lst_2)

#4
lst_3 = ['123', 'baton', '7.34', 'tetrad', 'card', '3', '[]', '8', '2020', '4']
lst_3[2] = 'ruchka'
del lst_3[6]
print(lst_3)

#5.1
a = {'a':1, 'b':2, 'c':3}
b = {'c':3, 'd':4, 'e':''}
c = {**a, **b}
print(c)

#5.2
a.update(b)
print(a)

#5.3
print(all(a.values()))

#5.4
print(not all(a.values()))

#5.5
lst_4 = []
lst_5 = []
for k, v in a.items():
    lst_4.append(k)
    lst_5.append(v)
lst_4.reverse()
lst_5.reverse()
d = dict(zip(lst_4, lst_5) )
print(d)

#5.6
a['b'] = 89
print(a)

#6.a
list_a = [1,2,3,4,4,5,2,1,8]
st_1 = set(list_a)
print(st_1)

#6.b
st_1.add(22)
print(st_1)

#6.c
list_a = tuple(list_a)  #перевел List в tuple, тем самым сделал его неизменяемым
print(type(list_a))  

#6.d
print(list_a)
print(len(list_a))


#Задачи на закрепление форматирования:

#1)
a = 10
b = 25
print(f'Summ is {a + b} and diff = {a - b}')
print('Summ is {sum} and diff = {dif}'.format(sum = a + b, dif = a - b))

#2)
list_of_children = ['Sasha', 'Vasia', 'Nikalai']
print(f'First child is {list_of_children[0]}, second is {list_of_children[1]}, and last one - {list_of_children[2]}')

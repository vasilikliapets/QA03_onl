#1
print('Robin,Singh'.split(','))
print('I,love,arrays,they,are,my,favorite'.split(','))

#2
l=['Ivan','Ivanov']
s1='Minsk'
s2='Belarus'

print('Привет,{} {}! Добро пожаловать в {} {}'.format(l[0],l[1],s1,s2))

#3
l2=['I', 'love', 'arrays', 'they', 'are', 'my','favorite']
s3=' '.join(l2)
print(s3)

#4
# создание списака с рандомыми числами
from random import randrange
n=10
s4=[randrange(1, 100) for i in range(n)]
print(s4)

# вставка на 3-ю позицию нового значения
s4.insert(2,'10')

# удаление элемента из списка под индексом 6
del s4[6]

# результат
print(s4)

#5
a={'a': 1, 'b': 2, 'c': 3}
b={'c': 3, 'd': 4, 'e': ''}

#5.1
c={**a,**b}
print(c)

#5.2
a.update(b)
print(a)

#5.3
print(all(a.values()))

#5.4
print(any(a.values()))

#5.5
print(dict(sorted(a.items(), reverse = True)))

#5.6
a['b']=10
print(a)

#6
list_a=[1,2,3,4,4,5,2,1,8]

#6.a
print(set(list_a))

#6.b
list_a.append(22)
print(list_a)

#6.c
list_a=tuple(list_a)
print(type(list_a))

#6.d
print(len(list_a))

#Задачи
#1.1
a=10
b=25
print('Summ is {c} and diff = {d}'.format(c=a+b, d=a-b))

#1.2
list_of_children=['Sasha', 'Vasia', 'Nikalai']
print('First child is {s}, second is {t}, and last one is {r}'.format(s=list_of_children[0],t=list_of_children[1],r=list_of_children[2]))

#2.2
#Убрать все символы кроме букв
s='123 When I consider every thing that grows Holds in perfection but a little moment  That this huge stage presenteth nought but shows Whereon the stars in secret influence comment;'
s1="".join(c for c in s if c.isalpha())
print (s1)

#все буквы перевести в нижний регистр
s1=s1.lower()
print(s1)

import collections
results = collections.Counter(s1)
print(min(results, key=results.get))

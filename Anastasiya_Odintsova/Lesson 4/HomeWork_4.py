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

#1
a = 10
b = 23
a,b = b,a

#2
a = a * 3
b = b - 3

#3
a = float(a)
b = str(b)

#4
print(round(a / 11, 3))

#5
c = (float(b) ** 3)

#6
import random
print(random.randrange(0, 100, 3))

#7
import math
print(math.sqrt(100) ** 4)

#8
print('Hi guys' * 3 + 'Today')

#9
print(len('Hi guys' * 3 + 'Today'))

#10
f = 'Hi guys' * 3 + 'Today'
print(f[21:26])
print(f[:20:-1])

#11
print(f[1::2])
print(f[::-2])

#12
q = f[21:26]
w = f[:20:-1]
e = f[1::2]
r = f[::-2]
stroka = 'Task 10: {}, {} Task11: {}, {}'.format(q,w,e,r)
print(stroka)

#13
t = 'my name is name'
l = t.replace('name', 'Pavel')
h = l.replace('Pavel', 'name', 1)
print(h)

#14
print(stroka.title())
print(stroka.lower())
print(stroka.upper())

#15
print(stroka.count('Task'))


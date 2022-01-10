#1
a=10
b=23
a,b=b,-a

#2
a=a*3
b=b-3

#3
a=float(a)
b=str(b)

#4
a=a/3
print(round(a,3))

#5
c=float(b)
print(c**3)

#6
import random
print(random.randrange(0,100,3))

#7
import math
print(math.sqrt(100)**4)

d='Hi guys'
e='Today'
print(d*3+e)

#9
print(len(d*3+e))

#10
print(e)
print(e[::-1])

#11
print(d+e[::2])
print(d+e[::-2])

#12
print('Task 10: {}, {} Task 11: {}, {}'.format(e,e[::-1], d+e[::2],d+e[::-2]))

#13
name='my name is name'
my_name=name.replace("is name", "is Nastya")
print(my_name)

#14
task_12='Task 10: Today, yadoT Task 11: igyH usigyTdy, ydTygisu Hygi'
print(task_12.title())
print(task_12.lower())
print(task_12.upper())

#15
print(task_12.count('Task'))

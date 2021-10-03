a = 23
b = 10
a,b = b,a
print(a,b)  # 1

a=a*3
b=b-3
print(a,b)  # 2

a = float(30)
b = str('20')
print(type(b))  #3
print(type(a))  #3

print(round(a/11 ,3)) #4

b = float(b)
c = b
c = pow(20, 3)
print(c) #5

import random
print(random.randrange(0, 100, 3)) #Как сделать, чтобы число кратоное трем выбиралось не из диапазона, а просто рандомное ?

import math
print(math.pow(math.sqrt(100),3)) #7

print('Hi Gues'*3+'Today') #8

print(len('Hi GuesHi GuesHi GuesToday')) #9

g = 'Hi GuesHi GuesHi GuesToday'
print(g[21:])
print(g[-1:-6:-1]) #10

print(g[::2])
print(g[::-2]) #11


u = 'Test'
j = 20
print('Hello {Privet}'.format(Privet=u))

print('Task 10: {в_прямом1}, {в_обратном1} Task 11: {в_прямом}, {в_обратном}'.format(
    в_прямом1=g[21:],
в_обратном1=g[-1:-6:-1],
в_прямом=g[::2],
в_обратном=g[::-2])) #12

print('my name is {name}'.format(name='Ilya')) #13

txt = 'Task 10: {в_прямом1}, {в_обратном1} Task 11: {в_прямом}, {в_обратном}'.format(
    в_прямом1=g[21:],
в_обратном1=g[-1:-6:-1],
в_прямом=g[::2],
в_обратном=g[::-2])

print (txt.title()) #14 a
print (txt.capitalize()) #14 б
print (txt.upper()) #14 c

print(txt.count('Task')) #15

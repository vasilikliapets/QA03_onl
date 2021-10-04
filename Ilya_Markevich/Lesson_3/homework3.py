a = 10
b = 23
a,b = b,(-a)
print(a,b)  # 1

a=a*3
b=b-3
print(a,b)  # 2

a = float(a)
b = str('20')
print(type(b))  #3
print(type(a))  #3

print(round(a/11 ,3)) #4

c = pow(float(b), 3)
print(c) #5

import random
print(random.randrange(0, 100, 3)) #Как сделать, чтобы число кратоное трем выбиралось не из диапазона, а просто рандомное ?

import math
print(math.pow(math.sqrt(100),4)) #7

st = 'Hi Gues'
print(st*3+'Today') #8

st2 = st*3+'Today'
print(len(st2)) #9

print(st2[21:])
print(st2[-1:-6:-1]) #10

print(st2[::2])
print(st2[::-2]) #11

print('Task 10: {v_priamom1}, {v_obratnom1} Task 11: {v_priamom}, {v_obratnom}'.format(v_priamom1=st2[21:],v_obratnom1=st2[-1:-6:-1],v_priamom=st2[::2],v_obratnom=st2[::-2])) #12

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

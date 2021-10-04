#1
a = 10
b = 23
a,b = b,-a
print(a,b)
#2
a = a*3
b = b-3
print(a,b)
#3
a = float(a)
b = str(b)
print(type(a),type(b))
#4
a = a/11
print(round(a, 3))
#5
c = float(b)
c = c**3
print(c)
#6
import random
print(random.randrange(0, 10000, 3))
#7
print((100**0.5)**4)
#8
line = "Hi guys"*3+"Today"
print(line)
#9
print(len(line))
#10
today = (line[-5:])
yadot = (today[::-1])
print(today, yadot)
#11
letter1 = line[1::2]
letter2 = line[::-1]
print(letter1, letter2)
#12
line2 = 'Task 10: {}, {} Task 11: {}, {}'.format(today, yadot, letter1, letter2)
print(line2)
#13
name = "my name is name"
print(name.replace("is name", "is Artyom"))
#14
print(my_name.title())

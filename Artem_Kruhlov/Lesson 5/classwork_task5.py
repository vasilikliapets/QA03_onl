# IF

a = int(input())
if a > 0:
    print("a > 0")
else:
    print("a < 0")

b = int(input())
if b == 4:
    print('b == 4')
elif b > 4:
    print('b > 4')
else:
    print('b < 4')


# ELIF

num = 10
num2 = 8
if num > num2:
    num3 = num - num2
    print(num3)
elif num < num2:
    num3 = num + num2
    print(num3)
else:
    num3 = num
    print(num3)

numm = int(input())
numm2 = int(input())
if numm > numm2:
    print(numm * numm2)
elif numm < numm2:
    print('numm < numm2')
elif numm == 0 and numm2 == 0:
    print("we have zero")
else:
    print("gg")


# FOR

list_str = ['Global', 'Albion', 'How', 'Car']
for i in list_str:
    for g in i:
        print(g, end="-")
print()
list_int = [9, 10, 12, 2]
for f in list_int:
    print(float(f))

# WHILE
x,y=0,5
while y <= 25:
    print(y)
    x,y = y,x+y

i = 0
while i <= 20:
    i += 1
    if i % 2 == 0:
        print(i) # ряд четных чисел от 0 до 20
n = 1
while n >= -20:
    n = n + (-2)
    print(n)  # каждое третье число в ряде от -1 до -21


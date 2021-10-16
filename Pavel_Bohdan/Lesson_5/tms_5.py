#1
# Решение идет отдельным файлом Bulls and Cows.py



#2
name = input('Введите имена через запятую: ')
name = name.split(',')
if name == ['']:
    print('No one likes this')
elif len(name) == 1:
    print(f'{name[0]} like this')
elif len(name) == 2:
    print(f'{name[0]} and {name[1]} like this')
elif len(name) == 3:
    print(f'{name[0]}, {name[1]} and {name[2]} like this')
elif len(name) > 3:
    print(f'{name[0]}, {name[1]} and {len(name) - 2} others like this')





#3
for i in range(1,1):
    if i % 15 == 0:
        i = 'FuzzBuzz'
    elif i % 3 == 0:
        i = 'Buzz'
    elif i % 5 == 0:
        i = 'Fuzz'
    print(i)    

#4
str_4 = ["a", "b", "c"]
a = []
for i, item in enumerate(str_4):
    b = [str(i + 1) + ':' + item]
    a.extend(b)
print(a)

#5
str_3 = ['a', 'a', 'a']
a = str_3[0]
for i in str_3:
    a, i = i ,a
    if i == a:
        answer = 'True'
    else:
        answer = 'False'
print(answer)

#6
i = True
b = []
str_1 = 'dogcat'
for i in str_1:
    a = i 
    i = i.islower()
    if i == False:
        b.append(a)
print(i, b)

str_2 = 'doGCat'
b = []
for i in str_2:
    a = i 
    i = i.islower()
    if i == False:
        b.append(a)
print(i, b)

#7
sum = 0
lst_1 = range(101) 
for i in lst_1:
    sum = i + sum
print(sum)
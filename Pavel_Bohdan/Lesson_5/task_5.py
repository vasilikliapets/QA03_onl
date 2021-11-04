#IF:

#1
var_1 = 4 #int(input())
if var_1 > 0:
    print("Переменная > 0")

#2
var_2 = 4 #int(input())
if var_2 > 0:
    print('1')
else:
    print('-1')

#3
var_3 = 4 #int(input())
if var_3 > 0:
    print('Varuable > 0')
elif var_3 < 0:
    print('Variable < 0')
else:
    print('Variable = 0')

#ELIF:

#1
var_4 = 4 #int(input())
var_5 = 4 #int(input())
if var_4 > var_5:
    res_ult = var_4 - var_5
elif var_4 < var_5:
    res_ult = var_4 + var_5
else:
    res_ult = var_4
print(res_ult)

#2
if 3 <= var_4 <= 5:
    print('Spring')
elif 6 <= var_4 <= 8:
    print('Summer')
elif 9 <= var_4 <= 11:
    print('Autumn') 
elif var_4 == 12 or 1 or 2:
    print('Winter')
else:
    print('Wrong input')


#FOR

#1
lst_1 = ['Spring', 'Summer', 'Autumn', 'Winter']
for season in lst_1:
    print(season)

#2
lst_1 = ['Spring', 'Summer', 'Autumn', 'Winter']
for season in lst_1:
    for letter in season:
        print(letter, end = '-')
print()

#3
#a
lst_2 = [2,5,3,8,2,1]
lst_2 = list(map(float, lst_2))
print(lst_2)

#b
c = [int(i) for i in lst_2]
print(c)

#WHILE

#1
a = 0
i = 1
while i < 30: 
    a, i = i, a + i
    print(i, end = ' ')
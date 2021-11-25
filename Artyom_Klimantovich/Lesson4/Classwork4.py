#Списки
list1 = [12, 34, 28, 9, 27]
list2 = [3, 35, 19, 48, 51]
print(list1[1])
list2[4] = 99
print(list2)
list3 = list1+list2
print(list3)
list4 = list3[int(len(list3)/2-1):int(len(list3)/2+1)]
print(list4)
list4.append('hello')
list4.append('world')
print(list4)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(set(a).intersection(set(b))))

list1 = [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(list(set(list1)))

#Логические операции
a = 34
b = 24
print(a == 34 and b ==24)
print(a >= 33 and b <= 29)
print(a > 35 and b >= 108)
print(a ==31 and b == 108)

print(a > 9 or b < 13)
print(a > 13 or b == 24)
print(a == 24 or b == 34)
print(a < 9 or b < 13)

c = 'my name is Artyom'
print(c.startswith("my") or c.startswith("name") or c.startswith("is") or c.startswith("Artyom"))
print(c.startswith("myy") or c.startswith("name") or c.startswith("is") or c.startswith("Artyom"))

#Словари
school = {'1a': 14, '1b': 18, '2b': 16, '6a': 17, '7v': 19}
print(school['1a'])
school['1a'] = 13
school['1b'] = 17
school['2b'] = 15
school['2a'] = 14
school['6b'] = 20
del school['7v']
print(school)
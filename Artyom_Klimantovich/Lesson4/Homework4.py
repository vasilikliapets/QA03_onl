#1
line1 = "Robin Singh"
line2 = "I love arrays they are my favorite"
line1 = line1.split()
line2 = line2.split()
print(line1)
print(line2)
#2
list_name = ['Ivan', 'Ivanou']
list_name2 = ' '.join(list_name)
line1 = "Minsk"
line2 = "Belarus"
print(f'Привет, {list_name2}! Добро пожаловать в {line1} {line2}')
#3
list_name = ["I", "love", "arrays", "they", "are", "my", "favorite"]
list_name2 = ' '.join(list_name)
print(list_name2)
#4
list1 = ['1','2','3','4','5','6','7','8','9','10']
list1.insert(3, 33)
list1.remove('6')
print(list1)
#5.1
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4, 'e': ''}
res = {**a, **b}
print(res)
#5.2
a.update(c=3, d=4, e='')
print(a)
#5.3
print(all(a.values()))
#5.4
b =['',{}]
print(not all(a.values()))
#5.5
print(sorted(a.items(), reverse=True))
#5.6
a['d']=13
print(a)
#6
list_a = [1,2,3,4,4,5,2,1,8]
#6.a
list_b = list(set(list_a))
print(list_b)
#6.b
list_b.append(22)
print(list_b)
#6.c
list_a=tuple(list_a)
#6.d
print(len(list_a))

#Задачи на закрепление форматирования
#1
a = 10
b = 25
summa = a+b
raznost = a-b
print(f'Summ is {summa} and diff={raznost}.')
print('Summ is {} and diff={}'.format(summa,raznost))
#2
list_of_children = ['Sasha', 'Vasia', 'Nikalai']
print('First child is',list_of_children[0],', second is',list_of_children[1],'and last one – ',list_of_children[2])

#1
string_1="Robin Singh"
string_2="I love arrays they are my favorite"

arr_1=string_1.split()    #переводим строку в массив
arr_2=string_2.split()    #переводим строку в массив

print(arr_1)
print(arr_2)
#2
arr=['Ivan','Ivanov']
city='Minsk'
coutry='Belarus'

print('Привет,{} {}! Добро пожаловать в {} {}'.format(arr[0],arr[1],city,coutry))
#3
arr2=["I", "love", "arrays", "they", "are", "my", "favorite"]

string2=' '.join(arr2)     #преводим список в строку

print(string2)
#4
arr3=['a',2,3,'hello',16,7,'world',50.0,'b',10000]

arr3.insert(2, 'new')     #вставляем на третью позицию новое значение
del arr3[6]               #удаляем элемент под индексом 6

print(arr3)
#5
a = { 'a': 1, 'b': 2, 'c': 3}
b = { 'c': 3, 'd': 4, 'e': ''}

ab={**a,**b}      #словарь который имеет все элементы обоих словарей
a.update(b)       #словарь а обновляем элементами из словаря b


print(all(a.values()))          #проверяем что все значения в словаре “a” не пустые либо не равны нулю
b=['',{},[]]                    #создаём список с пустыми значениями
print(b[0] in a.values() or b[1] in a.values() or b[2] in a.values())     #проверяем есть ли хоть одно пустое значение

for k, v in sorted(a.items(), reverse=True):    #сортируем по алфавиту в обратном порядке
    print(k,v)
a['c']=4          #изменяем значение одного ключа
print(a.values())    #выводим все значения
#6
list_a = [1,2,3,4,4,5,2,1,8]

list_b=list(set(list_a))    #выводим только уникальтые значения и оставляем списком
print(list_b)

list_b.append(22)           #добавляем значение
print(list_b)

list_a=tuple(list_a)        #делаем переменную неизменяемой
print('Длина объекта =',len(list_a))     #измеряем длину
#Задачи на закрепление форматирования
#1
a=10
b=25

summ=a+b
diff=a-b

print(f'Summ is {summ} and diff={diff}')
print('Summ is {} and diff={}'.format(summ,diff))
#2
list_of_children=['Sasha','Vasia','Nikalai']

print('First child is',list_of_children[0],', second is',list_of_children[1],'and last one – ',list_of_children[2])

#*1
a=[1, 5, 2, 9, 2, 9, 1]
from collections import Counter
c=dict(Counter(a))     #считаем сколько раз каждая цифра встречается
print(list(c.keys())[list(c.values()).index(1)])          #выводим ключ со значением 1
#*2
a='1One or more of the measurements from the attached calibration certificate were assessed against customer-defined tolerances.'

a=a.lower()     #приводим к нижнему регистру

import string
symbols=string.punctuation
remove_symbols=a.maketrans('','',symbols)
a_without_symbols=a.translate(remove_symbols)       #убираем все символы

no_space_a=a_without_symbols.replace(' ','')       #убираем пробелы

from string import digits
remove_digits=no_space_a.maketrans('','',digits)
a_withot_digits=no_space_a.translate(remove_digits)    #убираем цифры


ct=Counter(a_withot_digits)                             #считаем сколько раз повторяется каждая буква
most_commons = ct.most_common(1)                   #вычленяем максимальное количество

print(most_commons)





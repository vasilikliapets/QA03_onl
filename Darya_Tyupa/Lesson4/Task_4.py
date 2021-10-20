#списки
a=[1,2,3]
b=[4,5,6]
print(a[1])      #извлекаем из первого списка второй элемент

b[2]=7           #изменяем во втором списке последний элемент
print(b)

c=a+b            #соединяем оба списка
print(c)

d=c[int(len(c)/2-1):int(len(c)/2+1)]              #извлекаем срез из центра
print(d)

d.append('dad')           #добавляем два новых элемента
d.append('mum')
print(d)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(list(set(a).intersection(set(b))))    #выводим список из общих элементов

list_1= [1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(list(set(list_1)))          #выводим только уникальные значения

#логические операции

a=1
b=2

print(a == 1 and b == 2)     #true
print(a > 0 and b >= 1)      #true
print(a == 1 and b != 2)     #false
print(a < 1 and b > 1)       #false

print(a != 1 or b != 2)     #true
print(a == 0 and b == 1)      #true
print(a == 1 or b != 2)     #false
print(a < 1 or b > 1)       #false

c='Hello world'
print(c.startswith("Hello") or c.startswith("ho"))   #true

#словари

school={'1a':30, '1b':25, '2b':20, '6a':15, '7b':10}

print(school['1a'])     #узнаем сколько учащихся в определённом классе
school['1a']=25         #меняем колчество учащихся
school['1b']=15         #меняем колчество учащихся
school['2b']=17         #меняем колчество учащихся
school['8a']=7          #добавляем новый класс
school['9b']=18         #добавляем новый класс
del school['6a']        #удаляем класс
print(school)

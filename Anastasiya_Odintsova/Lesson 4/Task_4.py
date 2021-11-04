#Списки
#1
l=[1,2,3]
l1=[4,5,6]

#2
print(l[1])

#3
l1[2]=7
print(l1)

#4
l2=l+l1
print(l2)

#5
l3=l2[1:4]
print(l3)

#6
l2.insert(2,10)
l2.insert(3,20)
print(l2)

#7
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list((set(a)).intersection(set(b))))

#8
c=[1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3]
print(list(set(c)))

#Логические операции
#1
a=1
b=5

#2
print(a==1 and b==5)
print(a>0 and b>a)
print(a==b and b==a)
print(a!=a and b!=b)

#3
print(a==a or b==b)
print(a>0 or b>0)
print(a==b or b==a)
print(a>b or b<a)

#4
c='Python is a language'
print(c.isnumeric())

#Словари
#1
school={'1а':10,'1б': 11, '2а': 12, '2б': 11,'3а': 10, '3б': 9, '4а': 14, '4б': 12, '5а': 11, '5б': 15,}

#2
print(school['1а'])

#3
#в трех классах изменилось количество учащихся
school['1б']=10 
school['2б']=12
school['3б']=14

#в школе появилось два новых класса
school['1в']=10
school['2в']=15

#в школе расформировали один из классов
del school['5б']

#4
print(school)

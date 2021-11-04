#Типы данных
#1
var_int=10
var_float=8.4
var_str="No"

#2
big_int=var_int*3.5

#3
var_float=var_float-1

#4
print(var_int/var_float)
print(big_int/var_float)

#5
var_str=var_str*2+"Yes"*3

#6
print(var_int)
print(var_float)
print(big_int)
print(var_str)

#Строки
#1
a='Anastasiya'
print(a[0])
print(a[-1])
print(a[2])
print(a[-3])
print(len(a))

#2
b='Anastasiya Odintsova'
print(b[:8])
print(b[int((len(b)/2-2)):int((len(b)/2+2))])
print(b[3::3])
print(b[::-1])

#3
name='my name is name'
my_name=name.replace("is name", "is Nastya")
print(my_name)

#4
test_tring="Hello world!"
print(test_tring.index('w'))
print(test_tring.count('l'))
print(test_tring.startswith('Hello'))
print(test_tring.endswith('qwe'))

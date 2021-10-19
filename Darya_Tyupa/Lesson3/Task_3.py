#Типы данных
#1
var_int=10
var_float=8.4
var_str="No"
#2
big_int=var_int*3.5
#3
var_float-=1    #уменьшаем на единицу
#4
print("var_int/var_float =",var_int/var_float)
print("big_int/var_float =",big_int/var_float)
#5
var_str=var_str*2+"Yes"*3
#6
print("var_int =",(var_int))
print("var_float =",(var_float))
print("var_str =",(var_str))
print("big_int =",(big_int))

#Строки
#1
string_1="My name id Darya"
print(string_1[0])     #первый символ
print(string_1[-1])      #последний символ
print(string_1[2])      #третий символ с начала
print(string_1[-3])     #третий символ с конца
print(len(string_1))    #длина строки
#2
string_2="My name is Darya and I have two cats"
print(string_2[0:8])     #первые 8 символов
print(string_2[int((len(string_2)/2-2)):int((len(string_2)/2+2))])    #находим по центру 4 символа
print(string_2[3::3])      #индексы кратные трём
print(string_2[::-1])      #перевёрнутая строка
#3
name='my name is name'
my_name=name.replace("is name", "is Darya")     #замена слова в строке (наверное это читерство :)
print(my_name)
#4
test_string = "Hello world!"
print(test_string.find("w"))     #находим индекс символа
print(test_string.count("l"))    #колличесво "l" в строке
print(test_string.startswith("Hello"))   #проверяем начинается ли строка на ...
print(test_string.endswith("qwe"))       #проверяем оканчивается ли строка на ...

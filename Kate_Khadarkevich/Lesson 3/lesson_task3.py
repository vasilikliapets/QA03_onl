#1. Переменной var_int присвойте значение 10, var_float - значение 8.4, var_str - "No".
var_int = 10
var_float = 8.4
var_str = 'No'

#2. Измените значение, хранимое в переменной var_int, увеличив его в 3.5 раза, результат свяжите с переменной big_int.
big_int = var_int*3.5
print('big_int=', big_int)

#3. Измените значение, хранимое в переменной var_float, уменьшив его на единицу, результат свяжите с той же переменной.
var_float = var_float - 1
print('var_float=', var_float)

#4. Разделите var_int на var_float, а затем big_int на var_float. Результат данных выражений не привязывайте ни к каким переменным.
print('var_int/var_float=',var_int/var_float)
print('big_int/var_float=',big_int/var_float)

#5. Измените значение переменной var_str на "NoNoYesYesYes". При формировании нового значения используйте операции конкатенации (+) и повторения строки (*).
var_str = var_str*2 + 'Yes'*3
print('var_str=',var_str)

#6. Свяжите переменную с любой строкой, состоящей не менее чем из 8 символов. Извлеките из строки первый символ, затем последний, третий с начала и третий с конца. Измерьте длину вашей строки.
a='56789yuiop'
print('первый символ строки=', a[0])
print('последний символ строки=',a[-1])
print('третий символ строки=', a[2])
print('третий символ с конца=', a[-3])
print('длина строки=',len('56789yuiop'))
#7. Присвойте произвольную строку длиной 10-15 символов переменной и извлеките из нее следующие срезы:

b='1236548790rfv'
print('первые восемь символов=', b[:7]) #первые восемь символовки
print('четыре символа из центра=', b[int(len(b)/2-2):int(len(b)/2+2)])#четыре символа из центра строки
print('с индексами кратными трем=', b[::2]) #символы с индексами кратными трем
print('перевернутая строка=', b[::-1])  #переверните строку

#8.Есть строка: “my name is name”. Напечатайте ее, но вместо 2ого “name” вставьте ваше имя.

c='my name is name'
print(c.replace('is name', 'is Kate'))

#9 Есть строка: test_tring = "Hello world!", необходимо

test_tring = "Hello world!"
print('порядок буквы w=', test_tring.index("w"))    #напечатать на каком месте находится буква w
print('всего букв l=', test_tring.count("l"))    #кол-во букв l
print('начинается строка с подстроки: “Hello”=', test_tring.startswith("Hello"))   #Проверить начинается ли строка с подстроки: “Hello”
print('заканчивается строка подстрокой: “qwe”=', test_tring.endswith("Hello"))#Проверить заканчивается ли строка подстрокой: “qwe”
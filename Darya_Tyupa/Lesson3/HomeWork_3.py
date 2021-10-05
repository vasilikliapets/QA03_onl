# №1
print("task 1")
a,b=10,23
a,b=b,-(a)
print(f"a={a}, b={b}")
# №2
print("task 2")
a=a*3
b=b-3
print(f"a={a}, b={b}")
# №3
print("task 3")
a=float(a)        #преобразование в число с плавающей точкой
b=str(b)          #преобразование в строку
print(f"type a={type(a)}, type b={type(b)}")
# №4
print("task 4")
a=a/11
print("a=",round(a, 3))    #выводим значение с точностью 3 знака после запятой
# №5
print("task 5")
c=float(b)      #преобразование в число с плавающей точкой
print(f"с = {c}, c в третьей степени =",(c**3))
# №6
#print("task 6")
#print("случайное число кратное трём =",random.randrange(0, 100, 3))     #случайное число кратное трём
# №7
print("task 7")
print((100**0.5)**4)   #квадратный корень из ста в четвёртой степени
# №8
print("task 8")
string_1="Hi guys"*3+"Today"
print(string_1)
# №9
print("task 9")
print("длина строки =",len(string_1))    #узнаем длину строки
# №10
vpr_1=string_1[-5:]     #вычленяем слово
vobr_1=vpr_1[::-1]   #пишем его задом наперёд
print(vpr_1)
print(vobr_1)
# №11
vpr_2=string_1[1::2]    #каждая вторая буква
vobr_2=vpr_2[::-1]    #каждая вторая буква в обратном порядке
print(vpr_2)
print(vobr_2)
# №12
print("task 10-12")
print('Task 10: {}, {} Task 11: {}, {}'.format(vpr_1, vobr_1, vpr_2,vobr_2))
# №13
print("task 13")
name='my name is name'
my_name=(name.replace("name", "Darya") ).replace("Darya","name",1)     #меняем второе name на имя
print(my_name)
# №14
print("task 14")
print(my_name.title())     #Каждое слово с большой буквы
print(my_name.lower())     #все слова в нижнем регистре
print(my_name.upper())     #все слова в верхнем регистре
# №15
print("task 15")
task_12='Task 10: Today, yadoT Task 11: igyH usigyTdy, ydTygisu Hygi'    #строка из задания №12
print('Количество слова Task -', task_12.count('Task'))                  #считаем количество тлова таск в строке
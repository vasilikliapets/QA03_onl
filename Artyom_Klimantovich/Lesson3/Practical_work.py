#Типы данных
var_int = 10
var_float = 8.4
var_str = "No"
big_int = var_int*3.5
var_float -= 1
print(var_int/var_float)
print(big_int/var_float)
var_str = var_str*2+"Yes"*3
print(var_int)
print(var_float)
print(var_str)
print(big_int)

#Строки
line1 = "congratulations"
print(line1[0])
print(line1[-1])
print(line1[2])
print(line1[-3])
print(len(line1))

line2 = "congratulations winners"
print(line2[0:8])
print(line2[int((len(line2)/2-2)):int((len(line2)/2+2))])
print(line2[3::3])
print(line2[::-1])

a = "my name is name"
print(a.replace("is name", "is Artyom"))

test_tring = "Hello world!"
print(test_tring.find("w"))
print(test_tring.count("l"))
print(test_tring.startswith("Hello"))
print(test_tring.endswith("qwe"))
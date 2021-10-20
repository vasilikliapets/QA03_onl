# 1)
var_int = 10
var_float = 8.4
var_str = "No"
# 2)
big_int = var_int * 3.5
# 3)
var_float = var_float - 1
# 4)
print(var_int / var_float)
print(big_int / var_float)
# 5)
var_str = var_str + var_str + "Yes"*3
print(var_str)
# 6)
print(var_int, var_float, var_str, big_int)




# 1)
a = 'aadaagak'
print(a[0], a[-1], a[2], a[-3])
print(len(a))

# 2)
b = 'asdfghjklz'
print(b[0:8], b[4:8], b[3::3], b[::-1])

# 3)
my_name = "my name is name"
new_name = my_name.replace("name", "Artem", )
print(new_name.replace("Artem", "name", 1))

# 4)
test_tring = "Hello world!"
print(test_tring.find('w'))
print(test_tring.count("l"))
print(test_tring.startswith("Hello"))
print(test_tring.endswith("qwe"))
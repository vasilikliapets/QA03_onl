print("\n***Data types***")

# 1. Creating variables
print("\n1.Creating variables")
var_int = 10
var_float = 8.4
var_str = "No"
print(var_int, var_float, var_str)

# 2. Multiplication
print("\n2.Multiplication")
big_int = var_int * 3.5
print(big_int)

# 3. Subtraction
print("\n3.Subtraction")
var_float -= 1
print(var_float)

# 4. Division
print("\n4.Division")
var_int /= var_float
big_int /= var_float
print(var_int, big_int)

# 5. Duplication and Concatenation
print("\n5.Duplication & Concatenation")
var_str *= 2
var_str += "Yes" * 3
print(var_str)

# 6. Output
print("\n6.Output")
print(var_float)
print(var_int)
print(big_int)
print(var_str)

print("\n***Strings***")

# 1. Index access
print("\n1.Index access")
var_str2 = "BegiNner"
print(var_str2)
print(var_str2[0])
print(var_str2[-1])
print(var_str2[2])
print(var_str2[-3])
print(len(var_str2))

# 2. Extracting a slice
print("\n2.Extracting a slice")
var_big_str = "The Big Book of Berenstain Bears"
print(var_big_str[:7])
offset = round((len(var_big_str) - 4) / 2)
print(var_big_str[offset:-offset])
print(var_big_str[3::3])
print(var_big_str[::-1])

# 3. Replace
print("\n3.Replace")
name = "Veronika"
print("my name is name".replace("name", name).replace(name, "name", 1))

# 4. "Hello world!"
print("\n4.Hello world!")
test_string = "Hello world!"
print(test_string.index("w"))
print(test_string.count("l"))
print(test_string.startswith("Hello"))
print(test_string.endswith("qwe"))

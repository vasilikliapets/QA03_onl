# Lists
print("\n*** Lists ***")
# 1.
print("\nTask 1")
var_list1 = [3, 9, 7, 4, 2]
var_list2 = list([12, 26, 1, 7, 3])
print(var_list1)
print(var_list2)

# 2.
print("\nTask 2")
print(var_list1[1])

# 3.
print("\nTask 3")
var_list2[-1] = 8
print(var_list2)

# 4.
print("\nTask 4")
var_list3 = var_list1 + var_list2
print(var_list3)

# 5.
print("\nTask 5")
offset1 = int(len(var_list1) / 2)
offset2 = -int(len(var_list2) / 2)
var_list4 = var_list3[offset1:offset2]
print(var_list4)

# 6.
print("\nTask 6")
var_list4.extend([76, 18])
print(var_list4)

# 7.
print("\nTask 7")
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
print(list(set(a).intersection(set(b))))

# 8.
print("\nTask 8")
print(list({1, 2, 3, 4, 3, 2, 5, 1, 4, 6, 7, 1, 8, 2, 3}))

# True/False
print("\n*** True/False ***")
# 1.
print("\nTask 1")
var1 = 58
var2 = 37

# 2.
print("\nTask 2")
print(var1 != var2 and var1 > var2)
print(var1 == 58 and var2 < var1)
print(var1 == var2 and var1 > var2)
print(var1 == 37 and var2 < var1)

# 3.
print("\nTask 3")
print(var1 == var2 or var1 > var2)
print(var1 == 37 or var1 > var2)
print(var1 == var2 or var1 < var2)
print(var1 == 37 or var1 < var2)

# 4.
print("\nTask 4")
var_str = 'string'
print(var1 == var_str or var_str == 'string')
print(type(var_str) is str and var_str == 'string')

# Dicts
print("\n*** Dicts ***")
# 1.
print("\nTask 1")
school = {
    '1a': 23,
    '1b': 15,
    '1c': 26,
    '2a': 17,
    '2b': 21,
    '2c': 22,
    '3a': 19,
    '3b': 26,
    '3c': 21,
    '4a': 14,
}

# 2.
print("\nTask 2")
print(school['3a'])

# 3.
print("\nTask 3")
school.update({
    '1a': 26,
    '2c': 17,
    '3b': 20
})

school.update({
    '4b': 17,
    '4c': 7
})

del school['1c']

# 4.
print("\nTask 4")
print(school)

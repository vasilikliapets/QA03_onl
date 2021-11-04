# 4.
list_str = ["a", "b", "c"]
for i, v in enumerate(list_str):
    list_str[i] = f'{i + 1}: {v}'

print(list_str)

# 5.

var_list = []
if len(set(var_list)) <= 1:
    print(True)
else:
    print(False)

# 6.

var_str = 'dogcat'
result = [True, []]
for i in list(var_str):
    if i.isupper():
        result[0] = False
        result[1].append(i)

print(result)

# 7.
var_list_2 = [0, 0]
if bool(var_list_2) is True:
    print(sum(var_list_2))
else:
    print(0)

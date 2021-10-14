list_1 = list(input())
for i in range(len(list_1)):
    list_1[i] = str(i + 1) + ': ' + list_1[i]
print(list_1)
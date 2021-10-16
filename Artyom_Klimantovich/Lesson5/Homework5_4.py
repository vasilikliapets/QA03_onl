string = ['a', 'b', 'c', 'd', 'e']
string1 = len(string)

for i in range(string1):
    string[i] = str(i+1) + ':' + string[i]

print(string)
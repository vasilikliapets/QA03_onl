# Напишите код, который возьмет список строк и пронумерует их.
list_str = ['a', 'b', 'c']
a = len(list_str)
for i in range(a):
    list_str[i] = str(i+1)+': '+list_str[i]
print(list_str)

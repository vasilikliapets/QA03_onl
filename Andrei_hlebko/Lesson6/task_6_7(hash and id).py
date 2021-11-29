#Написать пример чтобы hash от объекта 1 и 2 были одинаковые, а id разные.
a = 257
b = 257.0

print('a id=', id(a), 'b id=', id(b))
print('a hash=', hash(a), ' b hash=', hash(b))

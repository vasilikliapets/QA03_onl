# 7. Написать пример чтобы hash от объекта 1 и 2 были одинаковые, а id разные.

a = 15
b = 15.0

print(id(a), id(b))
print(hash(a), hash(b))


print(a is b)

# 7. Написать пример чтобы hash от объекта 1 и 2 были одинаковые, а id разные.

obj1 = 1
obj2 = 1.0

print('id первого объекта: ', id(obj1), '\nid второго объекта: ', id(obj2))
print('id одинаковые: ', obj1 is obj2)
print('\nhash первого объекта: ', hash(obj1), '\nhash второго объекта: ', hash(obj2))
print('hash одинаковые: ', obj1 == obj2)

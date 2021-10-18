prim1 = [1, 1, 1]
prim2 = [1, 2, 1]
prim22 = [1, 2, 3]
prim3 = ['a', 'a', 'a']
prim4 = []

if len(set(prim2)) == 1 or prim2 == []:
    print(True)
else:
    print(False)

status = True  # флаг True на то что все значения в листе одинаковые

for i in prim4:  # Проходимся циклом по каждому значению в списке и записываем в i
    if prim4.count(i) != len(prim4):  # Условие:Если в списке количество значений(i) в листе не равно длине этого списка
        status = False  # Флаг меняем на False
        break
print(status)

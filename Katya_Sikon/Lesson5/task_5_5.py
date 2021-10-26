# Проверить, все ли элементы одинаковые

spis = list(input('Введите список через пробел: ').split())
#i = 1

#if len(spis) == 0:
#    print('список пустой')
#else:
#    while 0 < i < len(spis):
#        if spis[0] == spis[i]:
#            i = i + 1
#        else:
#            break

#if 0 < i < len(spis):
#    print(spis[0] == spis[i])
#elif 0 < len(spis) <= i:
#    print(spis[0] == spis[i-1])

spis_uniq = set(spis) #оставляем только уникальные значения

if len(spis_uniq) == 0:
    print('список пустой')
elif len(spis_uniq) == 1:
    print('все элементы списка одинаковые')
else:
    print('не все элементы списка одинаковые')

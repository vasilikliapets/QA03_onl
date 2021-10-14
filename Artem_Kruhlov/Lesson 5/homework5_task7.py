# задача №7
list_2 = range(int(input())) # задаем ренж с клавиатуры
new_list_2 = list(map(int, list_2)) # разварачиваем лист_2 в интовые значения
for i in range(len(new_list_2)):
    print(new_list_2)
    if new_list_2 == 0: # если лист пустой выводим 0
        print(0)
    print(sum(new_list_2)) # выводим сумму листа
    list_3 = list(input())
    new_list_3 = list(map(int, list_3))
    for v in range(len(new_list_3)):
        print(new_list_3)
        if new_list_3 == 0:
            print(0)
        print(sum(new_list_3))
        break
    break
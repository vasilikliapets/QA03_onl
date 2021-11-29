# Создайте программу, которая, принимая массив имён, возвращает строку описывающая количество лайков (как в Facebook).
str_5_2 = (input('Введите имена через запятую '))  # Ввод данных
list_5_2 = str_5_2.split()  # Перевод строки в массив
a = len(list_5_2)  # длина масива
if a == 0:  # Цикл (если =0, =1 и тд)
    print("No one likes this")
else:
    if a == 1:
        print(f'{list_5_2[0]} likes this')
    else:
        if a == 2:
            print(f'{list_5_2[0]} and {list_5_2[1]} like this')
        else:
            if a == 3:
                print(f'{list_5_2[0]}, {list_5_2[1]} and {list_5_2[2]} like this')
            else:
                if a > 3:
                    print(f'{list_5_2[0]}, {list_5_2[1]} and {a-2} others like this')

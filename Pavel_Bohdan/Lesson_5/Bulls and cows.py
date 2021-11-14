import random
  #  Компьютер загадывает число
comp_numbr = []
while len(comp_numbr) != 4:
        numbr = random.randint(1,9)
        if numbr not in comp_numbr :
            comp_numbr.append(numbr)
#print(f'Zagadal {comp_numbr}')  # Вывод загаданного компьютером числа для проверки


a = ''
b = ''
usr_nmbr = []
while usr_nmbr != comp_numbr:  # Условие победы в игре
    bull = 0
    cow = 0
    count = 0
    input_nmbr = str(input('Введите число с неповторяющимися цифрами '))  # Предложение пользователю ввести число
    if len(set(input_nmbr)) == 4:  # Проверка на правильность введенного числа
        usr_nmbr = list(map(int, input_nmbr))  # Перевод введенного числа в лист
        for i in usr_nmbr:  # Проверка наличия одинаковых цифр в заданном и введенном числах
            if i in comp_numbr:
                cow = cow + 1
                if cow > 1:  # Условие для корректного вывода слова "Корова"
                    a = 'Коровы'
                else:
                    a = 'Корова'
        print(f'{cow} {a}')  # Вывод количества одинаковых чисел
        
        for (q, x) in zip(comp_numbr, usr_nmbr):  # Проверка на соответствие позициям одинаковых цифр в числах
            if q == x:
                bull = bull + 1
                if bull > 1:  # Условие для корректного вывода слова "Бык"
                    b = 'Быка'
                else:
                    b = 'Бык'
        print(f'{bull} {b}')  # Вывод количества совпавших позиций цифр
    else:
        print('Введите корректное число')
           
else:
    print(f'Отгадал')
    

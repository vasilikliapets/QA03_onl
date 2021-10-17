import random


def create_igrok_chislo():
    igrok_chislo = input(f"Игрок {name_igrok}, введи 4-значное число с неповторяющимися цифрами: ")
    return igrok_chislo  # Возвращает число которое ввел пользователь


def the_game(comp_chislo):
    bull = 0
    cow = 0
    igrok_chislo = create_igrok_chislo()
    print(comp_chislo)  # вывод сгенерированного рандом числа что бы проверить победу.
    for i in range(len(igrok_chislo)):
        for l in range(len(comp_chislo)):
            if igrok_chislo[i] == comp_chislo[l]:
                if i == l:
                    bull += 1
                else:
                    cow += 1
    if bull < 4:
        print(f"К сожалению {name_igrok}, Вы не угадали, Количество быков: {bull}, количество коров {cow}. "
              f"Продолжаем игру...")
        the_game(comp_chislo)
    elif bull == 4:
        return print((f"Вы выиграли! Количество быков: {bull}! Поздравляем!"))


name_igrok = input("Игрок, введите ваше имя: ")
comp_chislo = ""
while len(comp_chislo) < 4:
    zna4 = str(random.randint(0, 9))
    if zna4 in comp_chislo:
        continue
    else:
        comp_chislo += zna4
the_game(comp_chislo)

def luhn(card):
    checksum = 0
    # Переводим номер карточки из строки в массив чисел
    cardnumbers = list(map(int, card))
    for count, num in enumerate(cardnumbers):
        # Если index чётный, значит число стоит на нечётной позиции
        # Так получается потому что считаем с нуля
        if count % 2 == 0:
            buffer = num * 2
            # Если удвоенное число больше 9, то вычитаем из него 9 и прибавляем к контрольной сумме
            if buffer > 9:
                buffer -= 9
            # Если нет, то сразу прибавляем к контрольной сумме
            checksum += buffer
        # Если число стоит на чётной позиции, то прибавляем его к контрольной сумме
        else:
            checksum += num
    # Если контрольная сумма делится без остатка на 10, то номер карты правильный
    return checksum % 10 == 0


number = input("Введите номер карты: ")
if number.isdigit():
    print("Номер карты должен содержать цифры")
else:
    print(luhn(number))

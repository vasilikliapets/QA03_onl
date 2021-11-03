def luhn(card):
    """
    The function checks the card number
    """
    checksum = 0
    cardnumbers = list(map(int, card))
    for count, num in enumerate(cardnumbers):
        if count % 2 == 0:
            buffer = num * 2
            if buffer > 9:
                buffer -= 9
            checksum += buffer
        else:
            checksum += num
    return checksum % 10 == 0


card = input('Введите номер карты:')
if card.isdigit() == False:    # проверяем что ввденное значение содержит только цифры
    print('Номер карты должен содержать цифры!')
else:
    print(luhn(card))

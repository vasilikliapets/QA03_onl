alphabet = 'abcdefghijklmnopqrstuvwxyz'  # создала алфавит
new_message = ''  # создала пустую строку, куда буду вносить буквы


def encode(message, n):
    """
    Function encodest messages
    """
    global alphabet, new_message
    for i in message:
        position = alphabet.find(i)  # нахожу позицию буквы из слова в алфавите
        new_position = position + n  # высчитываю новую позицию по шагу
        if i in alphabet:
            new_message += alphabet[new_position]  # добавляю букву новой позиции в пустую строку
        else:
            new_message += i  # добавляю в пустую строку всё то, что не нахожу в алфавите
    return new_message


# для расшифровки все те же действия, только для нахождения позиции по шагу использую "-"
def decode(message, n):
    """
    Function decodest messages
    """
    global alphabet, new_message
    for i in message:
        position = alphabet.find(i)
        new_position = position - n
        if i in alphabet:
            new_message += alphabet[new_position]
        else:
            new_message += i
    return new_message


def shifr():
    print('Выберите операцию:\n1) Encode \n2) Decode')
    choice = input()
    if choice != '1' and choice != '2':  # исключаю возмужную ошибку в выборе несуществующей операции
        print('Такой операции нет!')
    elif choice == '1':
        message = str(input('Введите фразу, используя английский алфавит:'))
        message = str.lower(message)  # привожу все буквы в сообщении к строчному регистру, т.к. алфавит из строчных
        n = int(input('Задайте число-сдвиг:'))
        print(encode(message, n))
    else:
        message = str(input('Введите фразу, используя английский алфавит:'))
        message = str.lower(message)
        n = int(input('Задайте число-сдвиг:'))
        print(decode(message, n))


if __name__ == '__main__':
    shifr()

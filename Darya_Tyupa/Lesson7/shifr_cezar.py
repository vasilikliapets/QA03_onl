init_alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
             'v',
             'w', 'x', 'y', 'z']
steps = 3  # шифруем с шагом 3


def select_decoder_type():
    '''
    This function for selection the decoder type
    '''
    global steps
    encode_type = int(input('''Выберете, что сделать:
                      1 - Зашифровать
                      2 - Дешифровать'''))
    if encode_type == 2:
        steps = steps * (-1)
    return True


def en_de_code(phrase):
    '''
    This function encrypts and decrypts the phrase
    '''
    result = ''
    for i in phrase:
        try:  # c помощью исключения оставляем пробелы и символы
            index = init_alph.index(i.lower())
            if index + steps > len(init_alph):  # определяем индексы для шифрования/дешифрования
                new_index = index + steps - len(init_alph)
            else:
                new_index = index + steps
            if i.isupper():  # сохраняем регистры
                result += init_alph[new_index].upper()
            else:
                result += init_alph[new_index]
        except ValueError:
            result += i
    return result


def main():
    '''
    This is the main function describes the whole process
    '''
    select_decoder_type()
    string = str(input("Введите фразу для шифровки/дешифровки:"))
    print(en_de_code(string))


if __name__ == '__main__':
    main()

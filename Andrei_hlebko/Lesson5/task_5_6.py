slovo1 = 'dogcat'
slovo2 = 'doGCat'

#Вариант с вводимым словом
#slovo_input = input("Введите слово которое хотите проверить на наличие больших букв: ")

letters = []
for i in slovo2:
    if i.isupper():
        letters.append(i)
if len(letters) == 0:
    print(True, letters)
else:
    print(False, letters)


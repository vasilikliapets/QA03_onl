import random  # импортирую модуль random

# создает список всех возможных ответов
def get_all_answers():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        # print(tmp)
        # Функция zfill() делает заданную строку не меньше указанной длины,
        # по необходимости заполняя первые символы нулями
        # отфильтруем повторяющиеся значения
        # вариант 1 - через set
        # убедимся, что 4 элемента уникальны
        # map() принимает два аргумента: функцию и аргумент составного типа данных.
        # map применяет к каждому элементу списка переданную функцию.
        if len(set(map(int,tmp))) == 4:
            ans.append(list(map(int, tmp))) # append() добавляет значения в список
        # print(ans) # получим 5040 уникальных значений
        # вариант 2 - через генератор списков
        #lst = ['x' for num in tmp if tmp.count(num) == 1]
        #if len(lst) == 4:
           # ans.append(list(map(int, tmp)))
    # print(ans)
    return (ans)

# выбирает один ответ из списка всех возможных ответов
def get_one_answer(ans):
    # через random.choice берется одно из уникальных значений списка ans
    num = random.choice(ans)
    return num

# запрашиваем у пользователя неповторящиеся цифры
def input_number():
    while True:
        nums = input('Введите 4 неповторяющиеся цифры: ')
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
            break
    return nums

# сравнивает два числа и сообщает количество быков и коров
def check(nums, true_nums):  # nums - предполагаемое число, true_nums - реально загаданное число
    bulls, cows = 0, 0
    for i, num in enumerate(nums):  # i - счетчик, num - содержимое переменной nums
        if num in true_nums:  # проверяем входит ли предполагаемое число в список реально загаданных
            if nums[i] == true_nums[i]:  # проверяем совпадают ли позиции(индексы)
                bulls += 1
            else:
                cows += 1
    return bulls, cows

# удаляет неподходящие варианты из спика возможных
def del_bad_answers(ans, computer_try, bull, cow):
    for num in ans[:]:  # с помощью среза слздали копию ans списка
        temp_bull, temp_cow = check(num, computer_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
    return ans

print('Игра Быки и Коровы')
answers = get_all_answers()  # положили в переменную 5040 вариантов ответа
player = input_number()  # число игрока
# Рандомно берется одно из уникальных значений answers и сохраняется в переменную player_2
computer = get_one_answer(answers)  # число противника

while True:
    print('=' * 15, 'Ход игрока', '=' * 15)
    print('Угадайте число компьютера')
    number = input_number()
    bulls, cows = check(number, computer)
    print('Быки: ', bulls, 'Коровы: ', cows)
    if bulls == 4:
        print('Победил игрок')
        print('Компьютер загадал число: ', computer)
        break
    print('=' * 15, 'Ход компьютера', '=' * 15)
    computer_try = get_one_answer(answers)
    print('Компьютер считает, что вы загадали число ', computer_try)
    bulls, cows = check(computer_try, player)
    print('Быки: ', bulls, 'Коровы: ', cows)
    if bulls == 4:
        print('Победил компьютер')
        print('Компьютер загадал число: ', computer)
        break
    else:
        answers = del_bad_answers(answers, computer_try, bulls, cows)
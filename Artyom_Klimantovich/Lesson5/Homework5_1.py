#Быки и коровы

import random

#создаёт список всех возможных ответов
def all_answers():
    ans = []
    for i in range(10000):
        tmp = str(i).zfill(4)
        if len(set(map(int, tmp))) == 4:
            ans.append(list(map(int, tmp)))
            return ans

#выбирает один ответ из списка возможных
def one_answer(ans):
    num = random.choice(ans)
    return num

#запрашивает у пользователя неповторяющиеся цифры
def number():
    while True:
        nums = input('Введите 4 неповторяющиеся цифры')
        if len(nums) != 4 or not nums.isdigit():
            continue
        nums = list(map(int, nums))
        if len(set(nums)) == 4:
                break
    return nums

#сравнивает 2 числа и сообщает количество быков и коров
def check(nums, true_nums):
    bulls, cows = 0 , 0
    for i, num in enumerate(nums):
        if num in true_nums:
            if nums[i] == true_nums[i]:
                bulls += 1
            else:
                cows += 1
    return bulls, cows

#удаляет не подходящие варианты
def del_bad_answers(ans, enemy_try, bull, cow):
    for num in ans[:]:
        temp_bull, temp_cow = check(num, enemy_try)
        if temp_bull != bull or temp_cow != cow:
            ans.remove(num)
    return ans


answers = all_answers()
player = number()
enemy = one_answer(answers)

while True:
    print('=' * 15, 'Ход игрока', '=' * 15)
    print('Угадайте число')
    number2 = number()
    bulls, cows = check(number2, enemy)
    print('Быки: ', bulls, 'Коровы: ', cows)



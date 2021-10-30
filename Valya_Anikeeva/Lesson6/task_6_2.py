#2 На вход подается строка, например, cccbbaa результат работы программы - строка c3b2a2

string = 'cccbbaa'
currCh = string[:1]
currCount = 1
result = ''
for ch in string[1:]:
    if ch != currCh:
        result += (currCh + str(currCount))
        currCh = ch
        currCount = 1
    else:
        currCount += 1
result += (currCh + str(currCount))

print(result)

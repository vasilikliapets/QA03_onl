import random

lambda name: f"Hello,{name}"

func_l = lambda name: f"Hello, {name}"
# print(func_l("Eugene"))

func_3 = lambda list_name: [f"Hello, {name}" for name in list_name]
# print(func_3(["Max", "Anton", "Tur"]))

x = [1, 3, 5, 7, 9]
func_4 = map(lambda x: str(x), [1, 3, 5, 7, 9])

# print(list(func_4))

names = ["Andrei", "Veronika", "Kotik"]
result = filter(lambda x: 'k' in x, names)
# print(list(result))


def summa(a, b):
    """Считает сумму"""
    return print(a + b)


def diff(a, b):
    """Считает разность"""
    return a - b


print(random.choice((summa,diff))(4, 4))
# a = random.choice((summa,diff)(4, 4)


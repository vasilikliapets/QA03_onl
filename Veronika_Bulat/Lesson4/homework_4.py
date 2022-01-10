# 1.
print("\nTask 1")
print("Robin Singh".split())
print("I love arrays they are my favorite".split())

# 2.
print("\nTask 2")
name = ["Ivan", "Ivanou"]
city = "Minsk"
country = "Belarus"
print(f"Привет, {' '.join(name)}! Добро пожаловать в {city} {country}")
# 3.
print("\nTask 3")
print(" ".join(["I", "love", "arrays", "they", "are", "my", "favorite"]))

# 4.
print("\nTask 4")
var_list1 = ["home", "nose", "rose", "clock", "short", "zero", "photo", "metro", "tomato", "dog"]
var_list1.insert(2, "cat")
del var_list1[6]
print(var_list1)

# 5.
print("\nTask 5")
a = {'a': 1, 'b': 2, 'c': 3}
b = {'c': 3, 'd': 4, 'e': ""}

print({**a, **b})

a.update(b)
print(a)

print(all(a.values()))

print(any(a.values()))

print(sorted(a.items(), reverse=True))

a['d'] = 44
print(a)

# 6.
print("\nTask 6")
list_a = [1, 2, 3, 4, 4, 5, 2, 1, 8]

set_a = set(list_a)
print(set_a)

set_a.add(22)
print(set_a)

list_a = tuple(list_a)
print(len(list_a))

# Format
print("\n*** Format ***")
# 1.
print("\nTask 1")
a = 10
b = 25
summ = a + b
diff = a - b
print(f"Sum is {summ} and diff {diff}")
print("Sum is {} and diff {}".format(summ, diff))

# 2.
print("\nTask 2")
list_of_children = ["Sasha", "Vasia", "Nikalai"]
print(f"First child is {list_of_children[0]}, second is {list_of_children[1]}, and last one – {list_of_children[-1]}")

# Tasks with *
print("\n*** Tasks with * ***")
from collections import Counter
from string import punctuation, digits

# 1.
print("\nTask 1")
list_b = [1, 5, 2, 9, 2, 9, 1]
for k, v in Counter(list_b).most_common():
    if v == 1:
        print(k)

# 2.
print("\nTask 2")
text = "Lorem 99 ipsum dolor sit amet, consectetur 5 adipiscing elit. Sed convallis purus vitae accumsan luctus. Etiam 7 commodo turpis sit amet convallis porta. Cras gravida nibh eu enim pulvinar, in cursus nisi eleifend. Phasellus id libero tincidunt, tempus diam eget, maximus 23 urna."
text_letters = text.translate(text.maketrans('', '', punctuation + digits + ' '))
print(Counter(sorted(list(text_letters.lower()))).most_common(1))

# Нумерация начинается с 1, имеет “:” и пробел
# [] => []
# ["a", "b", "c"] => ["1: a", "2: b", "3: c"]

spisok_strok = ["a", "b", "c"]
new_spisok = []

new_spis = [str(i + 1) + ": " + l for i, l in enumerate(spisok_strok)]
print(new_spis)

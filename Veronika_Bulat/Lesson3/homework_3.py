import math
import random

# Task 1
print("\nTask 1")
a, b = 10, 23
a, b = b, -a
print(f"a={a}, b={b}")

# Task 2
print("\nTask 2")
a *= 3
b -= 3
print(f"a={a}, b={b}")

# Task 3
print("\nTask 3 - type")
a = float(a)
b = str(b)
print("a=", type(a))
print("b=", type(b))

# Task 4
print("\nTask 4 - round")
print(round(a / 11, 3))

# Task 5
print("\nTask 5 - type & pow")
c = float(b)
print(type(c))
print(pow(c, 3))

# Task 6
print("\nTask 6 - random.randrange")
print(random.randrange(0, 1000, 3))

# Task 7
print("\nTask 7 - pow & math.sqrt")
print(pow(math.sqrt(100), 4))

# Task 8
print("\nTask 8")
var_str = "Hi guys" * 3 + "Today"
print(var_str)

# Task 9
print("\nTask 9 - len task 8")
print(len(var_str))

# Task 10
print("\nTask 10 - 'Today'")
t_str = var_str[-5:]
t_back = var_str[-5:][::-1]
print(t_str)
print(t_back)

# Task 11
print("\nTask 11 - 'Hi guys'")
el_str = var_str[1::2]
el_back = var_str[-2::-2]
print(el_str)
print(el_back)

# Task 12
print("\nTask 12 - format")
for_f = "Task 10: {}, {} Task 11: {}, {}".format(t_str, t_back, el_str, el_back)
print(for_f)

# Task 13
print("\nTask 13 - replace")
name = "Veronika"
print("my name is name".replace("name", name).replace(name, "name", 1))

# Task 14
print("\nTask 14 - title, lower, upper")
print(for_f.title())
print(for_f.lower())
print(for_f.upper())

# Task 15
print("\nTask 15 - count")
print(for_f.count("Task"))

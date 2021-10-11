names_like = input("Введите имена через запятую: ").split(",")
if len(names_like) == 1:
    print(f"{names_like[0]} likes this")
elif len(names_like) == 2:
    print(f"{names_like[0]} and {names_like[1]} likes this")
elif len(names_like) == 3:
    print(f"{names_like[0]},{names_like[1]} and {names_like[2]} likes this")
elif len(names_like) > 3:
    print(f"{names_like[0]},{names_like[1]} and {len(names_like)-2} other likes this")
else:
    print("No one likes this")

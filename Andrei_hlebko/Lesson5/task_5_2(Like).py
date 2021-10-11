
#name = ["Ann", "Alex", "Mark", "Max"]
names = input("Введите имена через запятую: ").split()
if len(names) == 1:
    print(f"{names[0]} likes this")
elif len(names) == 2:
    print(f"{names[0]} and {names[1]} like this")
elif len(names) == 3:
    print(f"{names[0]},{names[1]} and {names[2]} like this")
elif len(names) > 3:
    print(f"{names[0]} {names[1]} and {len(names)-2} other like this")
else:
    print("No one likes this")


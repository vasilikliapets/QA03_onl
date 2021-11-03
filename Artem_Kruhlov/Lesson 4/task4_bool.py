a = 5
b = 7

print(a == 5 and b == 7)     #true
print(a > 0 and b >= 7)      #true
print(a == 1 and b != 2)     #false
print(a < 1 and b > 1)       #false

print(a != 1 or b != 2)     #true
print(a == 5 and b == 7)      #true
print(a == 6 or b != 7)     #false
print(a < 4 or b < 7)       #false

c='Hello world'
print(c.startswith("Hello") or c.startswith("ho"))   #true
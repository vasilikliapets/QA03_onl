import math
import random

a, b = 10, 23  #1
a, b = b, a  #1

a *= 3  #2
b -= 3  #2

a = float(a)  #3
b = str(b)  #3

print(round(a / 11, 3))  #4

c = float(b)  #5
c = c ** 3  #5

r = random.randrange(3, 29, 3)  #6

k = math.sqrt(100)  #7
k = k ** 4  #7

s = "Hi guys" * 3 + "Today"  #8

print(len(s))  #9

print(s[21:])  #10
print(s[30:20:-1])  #10

print(s[1::2])  #11
print(s[::-2])  #11

s12 = f"Task 10: {s[21:]}, {s[30:20:-1]} Task 11: {s[1::2]}, {s[::-2]}"   #12
print(f"Task 10: {s[21:]}, {s[30:20:-1]} Task 11: {s[1::2]}, {s[::-2]}")  #12

s2 = "My name is name"  #13
print(s2.replace("is name", "is Andry"))  #13

#14
print(s12.title())  #A
print(s12.lower())  #Б
print(s12.upper())  #В

print(s12.count('Task'))  #15


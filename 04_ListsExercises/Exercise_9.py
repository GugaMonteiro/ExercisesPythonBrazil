from random import randint

num = [randint(1, 10) for c in range(0, 10)]

s = 0

for i in range(0, 10):
    total = num[i] ** 2
    s += total

print(num)
print(s)

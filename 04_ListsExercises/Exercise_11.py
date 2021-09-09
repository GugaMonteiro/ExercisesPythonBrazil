from random import randint

num_1 = [randint(1, 20) for c in range(0, 10)]
num_2 = [randint(1, 20) for i in range(0, 10)]
num_3 = [randint(1, 20) for f in range(0, 10)]

num_1.extend(num_2)
num_1.extend(num_3)

print(num_1)

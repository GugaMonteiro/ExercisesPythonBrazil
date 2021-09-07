import random

num = [round(random.uniform(1, 100), 2) for c in range(0, 10)]

print(num[::-1])

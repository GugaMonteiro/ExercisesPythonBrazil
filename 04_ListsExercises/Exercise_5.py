from random import randint

num = [randint(1, 100) for c in range(0, 20)]
num_odd = []
num_even = []

for c in range(0, 20):
    if num[c] % 2 == 0:
        num_even.append(num[c])
    else:
        num_odd.append(num[c])

print(f"Numbers list: {num}")
print(f"Pair numbers: {num_even}")
print(f"Odd numbers: {num_odd}")

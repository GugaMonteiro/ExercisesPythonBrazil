from random import randint

num = [randint(0, 20) for c in range(0, 5)]

mult = 1

for i in range(0, 5):
    mult *= num[i]

print(f"Sum: {sum(num)}")
print(f"Multiplication: {mult}")
print(f"Terms: {num}")

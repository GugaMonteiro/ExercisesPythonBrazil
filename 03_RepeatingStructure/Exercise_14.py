num = []

for n in range(1, 11):
    x = int(input("Type a number: "))
    num.append(x)

even = []
odd = []

q_even = 0
q_odd = 0

for y in num:
    if y % 2 == 0:
        even.append(y)
        q_even += 1
    else:
        odd.append(y)
        q_odd += 1

print(f"\nThere are {q_even} even numbers.")
print(f"There are {q_odd} odd numbers.")

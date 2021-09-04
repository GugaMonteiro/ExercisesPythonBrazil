num = -1

while num < 0:
    num = int(input("Type the end of the equation: "))
    if num < 0:
        print("Error. Try again.")

print("H = 1 + ")
total = 0
h = 1

for c in range(1, num + 1):
    total += h
    h = 1 / c
    print(f"1 / {c} + ")

print(f" = {round(total, 2)}")

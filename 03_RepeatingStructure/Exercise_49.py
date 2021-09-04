num = -1

while num < 0:
    num = int(input("Type the times do you wanna repeat the equation: "))
    if num < 0:
        print("Error. Try again.")

num_1 = 0
num_2 = -1
total = 0

print("S =")

for c in range(1, num + 1):
    num_1 += 1
    num_2 += 2
    s = num_1 / num_2
    total += round(s, 2)
    print(f" {num_1} / {num_2} + ")

print(f" = {round(total, 2)}")

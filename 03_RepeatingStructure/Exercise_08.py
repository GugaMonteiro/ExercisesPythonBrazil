num = []

for n in range(1, 6):
    y = int(input("Type an integer number: "))
    num.append(y)

total = sum(num)
mean = total / len(num)

print(f"The sum of the numbers is {total} and the mean is {mean}")

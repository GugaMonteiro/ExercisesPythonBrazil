from random import randint

print("---- Greater, Minor, Sum ----\n")

series = -1

while series < 0:
    series = int(input("Type the maximum series of numbers do you want: "))
    if series < 0:
        print("The number has to be greater than zero. Try again.\n")

num = []

for n in range(0, series):
    y = randint(1, 100)
    num.append(y)

print(f"The greater value is {max(num)}, the minor is {min(num)} and the sum is {sum(num)}")

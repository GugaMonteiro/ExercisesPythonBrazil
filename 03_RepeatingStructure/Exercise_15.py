print("---- Fibonacci Sequence ----\n")

num = 0

while num <= 0:
    num = int(input("Type the maximum term do you want: "))
    if num <= 0:
        print("The number has to be positive. Try again.\n")

first = 0

print(first)

sec = 1

for n in range(0, num):
    print(sec)
    third = first + sec
    first = sec
    sec = third

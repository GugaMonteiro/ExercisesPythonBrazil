num = -1

while num < 0:
    num = int(input("Type the number do you want to know that is prime: "))
    if num < 0:
        print("The value has to be more than zero. Try again.")

count = 0

for c in range(1, num + 1):
    result = num % c
    if result == 0:
        count += 1
        if count == 2:
            print("prime")

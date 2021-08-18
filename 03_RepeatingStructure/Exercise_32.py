num = -1

while num <= 0:
    num = int(input("Type the number do you want the factorial: "))
    if num <= 0:
        print("The number has to be more than zero. Try again.")

factorial = 1

print(f"Factorial of {num}")
print(f"{num} = ")
for i in reversed(range(2, num + 1)):
    print(f"{i} *")
    factorial *= i

print(f"1 = {factorial}")

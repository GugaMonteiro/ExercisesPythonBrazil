print("---- Factorial Calculator ----\n")

num = 0

while num <= 0:
    num = int(input("Type a number: "))
    if num <= 0:
        print("The number has to be greater than zero. Try again.\n")

fact = 1

for n in range(1, num + 1):
    fact *= n

print(fact)

num = 0

while num <= 0:
    num = int(input("Type an integer number: "))
    if num <= 0:
        print("The number has to be more than zero. Try again.")

mult = 0

for n in range(2, num):
    if num % n == 0:
        mult += 1

if mult == 0:
    print("It's a prime")
else:
    print("Not a prime")

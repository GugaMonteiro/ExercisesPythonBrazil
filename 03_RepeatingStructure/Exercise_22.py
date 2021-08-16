n1 = -1

while n1 < 0:
    n1 = int(input("Type an integer number: "))
    if n1 < 0:
        print("The number has to be more than zero. Try again.")

mult = 0

for n in range(2, n1):
    if n1 % n == 0:
        mult += 1
        print(f"It's multiple of {mult}")

if mult == 0:
    print("It's a prime")
else:
    print("Not a prime")

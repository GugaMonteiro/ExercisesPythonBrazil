quant = 0

while quant <= 0:
    quant = int(input("How many numbers do you wanna know: "))
    if quant <= 0:
        print("The quantity has to be more than zero. Try again.")

quantDiv = 0
for n in range(1, quant + 1):
    prime = True
    par = n / 2
    for c in range(2, int(par) + 1):
        quantDiv += 1
        if n % c == 0:
            prime = False
            break
    if prime:
        print(n)

print(f"\nNumber of divisions: {quantDiv}")

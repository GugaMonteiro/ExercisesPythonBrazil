quant = 0

while quant <= 0:
    quant = int(input('How many numbers do you want calculate: '))
    if quant <= 0:
        print("The quantity has to be more than zero. Try again.")

for n in range(0, quant):
    t = 0
    while (t <= 0) or (t > 16):
        t = int(input('Type the number do you want the factorial: '))
        if t <= 0:
            print("The term has to be more than zero. Try again.")
        if t > 16:
            print("The ter has to be less than 16. Try again.")

    fact = 1
    for i in range(1, t + 1):
        fact *= i

    print(fact)

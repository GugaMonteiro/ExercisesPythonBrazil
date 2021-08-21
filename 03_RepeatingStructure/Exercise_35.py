from math import sqrt
num = -1

while num < 0:
    num = int(input("Type a number: "))
    if num < 0:
        print("The value has to be more than zero. Try again.")

aux = 0
aux1 = 0

while num > 1:
    aux = sqrt(num)
    aux = int(aux)
    aux1 = 0
    while aux >= 2:
        if num % aux == 0:
            aux1 += 1
        if aux == 2:
            if aux1 == 0:
                print(num)
        aux -= 1
    num -= 1

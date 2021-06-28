import math

a = int(input("Type the value of 'A': "))

if a == 0:
    print("The equation is not of the second degree.")
else:
    b = int(input("Type the value of 'B': "))
    c = int(input("Type the value of 'C': "))

delta = (b ** 2) - (4 * a * c)

if delta < 0:
    print("The equation hasn't real roots.")
elif delta == 0:
    print("The equation has one real root.")
    y = (-b + (math.pow(delta, 1/2))) / (2 * a)
    print(f"y = {y}")
else:
    print("The equation has two real root.")
    y_1 = (-b + (math.pow(delta, 1/2))) / (2 * a)
    y_2 = (-b - (math.pow(delta, 1/2))) / (2 * a)
    print(f"y¹ = {y_1}\ny² = {y_2}")


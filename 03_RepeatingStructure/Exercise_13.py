root = int(input("Type the root: "))

exp = -1

while exp < 0:
    exp = int(input("Type the exponent: "))
    if exp < 0:
        print("Exponent has to be positive. Try again.")

for n in range(0, exp + 1):
    total = n * root

print(f"{root} to the {exp} = {total}")

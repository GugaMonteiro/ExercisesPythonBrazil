price_l = []

x = 1
for c in range(1, x + 1):
    reg = -1
    while reg != 0:
        reg = int(input(f"Product {c}: $ "))
        price_l.append(reg)
        x += 1
        c += 1
        if reg < 0:
            print("The value has to be more than zero. Try again.")

total = sum(price_l)

value_c = -1

while value_c < 0:
    value_c = float(input("Money: $ "))
    if value_c < 0:
        print("The value has to be more than zero. Try again.")

change = value_c - total

print(f"Change: ${round(change, 2)}")

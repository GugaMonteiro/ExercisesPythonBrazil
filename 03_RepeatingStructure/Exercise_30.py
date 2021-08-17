value = -1

while value < 0:
    value = float(input("Type the price of the bread: "))
    if value < 0:
        print("The value has to be more than zero. Try again.")

print(f"\nBread value: ${value}")

for c in range(1, 51):
    total = c * value
    print(f"{c}\t-\t${round(total, 2)}")

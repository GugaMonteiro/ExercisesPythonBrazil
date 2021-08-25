debt = -1

while debt < 0:
    debt = int(input("Type the value of your loan: "))
    if debt < 0:
        print("The value has to be more than zero. Try again.")

fees = 0
parc = [1]

for c in range(1, 12 + 1):
    if c % 3 == 0:
        parc.append(c)

print("\nDebt Value:\t\tFee Value:\t\tInstallments:\t\tInstallments Value:\n")

for c in range(0, 5):
    total_fees = debt * (fees / 100)
    total = debt + total_fees
    parc_value = total / parc[c]
    print(f"{total}:\t\t\t{total_fees}\t\t\t\t{parc[c]}\t\t\t\t{round(parc_value, 2)}")
    if fees >= 1:
        fees += 5
    else:
        fees += 10

print("Minimum value to withdraw: $10")
print("Maximum value to withdraw: $600")

cash = int(input("Type the withdraw amount: "))

banknotes = [100, 50, 10, 5, 1]

print(f"R$ {cash}:")

for x in banknotes:
    print(f"{int((cash/x))} banknote(s) of ${int(x)},00")
    cash %= x

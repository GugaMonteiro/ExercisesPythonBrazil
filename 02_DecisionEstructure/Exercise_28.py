print("\t\t\t\tUp to 5kg\t\tMore than 5kg")
print("File duplo\t\t$4,90/kg\t\t$5,80/kg")
print("Alcatra\t\t\t$5,90/kg\t\t$6,80/kg")
print("Picanha\t\t\t$6,90/kg\t\t$7,80/kg")

print("\n5% discount on tabajara card payment.")

meat = input("\nChoose only one type of meat: ")
quant = int(input("Type the amount of meat you're buying(kg): "))
pay = input("Method of payment: ")

meat.lower()
pay.lower()

if meat == "file duplo":
    if 0 < quant <= 5:
        total = 4.9 * quant
        print(total)
    elif quant > 5:
        total = 5.8 * quant
    else:
        print("Wrong value")
elif meat == "alcatra":
    if 0 < quant <= 5:
        total = 5.9 * quant
    elif quant > 5:
        total = 6.8 * quant
    else:
        print("Wrong value")
elif meat == "picanha":
    if 0 < quant <= 5:
        total = 6.9 * quant
    elif quant > 5:
        total = 7.8 * quant
    else:
        print("Wrong value")
else:
    print("Wrong value.")

if pay == "tabajara" or "tabajara card":
    disc = total * 0.05
    total_disc = total - disc
else:
    print("You chose another method of payment.")

print(f"Meat type\t\t  ----------- {meat}")
print(f"Quantity\t\t  ----------- {quant}kg")
print(f"Total\t\t\t  ----------- ${total}")
print(f"Method of payment ----------- {pay}")
print(f"Discount\t\t  ----------- ${round(disc, 2)}")
print(f"Subtotal\t\t  ----------- ${total_disc}")

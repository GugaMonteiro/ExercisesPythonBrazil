liters = float(input("How many liters was sold: "))

print("\nG - Gasoline\tE - Ethanol")

f_type = input("Choose an fuel type above: ")
f_type = f_type.upper()

g = 2.5
e = 1.9

g_total = liters * g
e_total = liters * e

if f_type == "E":
    if 20 >= liters > 0:
        desc = e_total * 0.03
        final_price = e_total - desc
        print(f"\nYou put {liters} liters of ethanol at {g} dollars and had a discount of {desc} dollars."
              f"\nTotal: {e_total}"
              f"\nWith discount: {final_price}")
    elif liters > 20:
        desc = e_total * 0.05
        final_price = e_total - desc
        print(f"\nYou put {liters} liters of ethanol at {g} dollars and had a discount of {desc} dollars."
              f"\nTotal: {e_total}"
              f"\nWith discount: {final_price}")
    else:
        print("\nInvalid entry.")
elif f_type == "G":
    if 20 >= liters > 0:
        desc = e_total * 0.04
        final_price = e_total - desc
        print(f"\nYou put {liters} liters of gasoline at {g} dollars and had a discount of {desc} dollars."
              f"\nTotal: {g_total}"
              f"\nWith discount: {final_price}")
    elif liters > 20:
        desc = e_total * 0.06
        final_price = e_total - desc
        print(f"\nYou put {liters} liters of gasoline at {g} dollars and had a discount of {desc} dollars."
              f"\nTotal: {g_total}"
              f"\nWith discount: {final_price}")
    else:
        print("\nInvalid entry.")
else:
    print("\nInvalid entry.")

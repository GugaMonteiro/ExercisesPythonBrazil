country_a = -1

while country_a < 0:
    country_a = int(input("Type the initial population of the country A: "))
    if country_a < 0:
        print("The valor has to be greater than zero. Try again.")

country_b = -1

while country_b < country_a:
    country_b = int(input("Type the initial population of the country B: "))
    if country_b < country_a:
        print("The valor has to be greater than the population of the country A. Try again.")

tax_a = -1

while tax_a < 0:
    tax_a = float(input("\nType the initial tax rate of the country A(%): "))
    tax_a = (tax_a / 100) + 1
    if tax_a < 0:
        print("The valor has to be greater than zero. Try again.")

tax_b = 2

while tax_b > tax_a:
    tax_b = float(input("Type the initial tax rate of the country B(%): "))
    tax_b = (tax_b / 100) + 1
    if tax_b > tax_a:
        print("The valor has to be greater than the tax rate of the country A. Try again.")

year = 0

while country_a != country_b:
    grow = country_a * tax_a
    country_a += grow
    grow2 = country_b * tax_b
    country_b += grow2
    year += 1

print(f"\nIt will be necessary {year} years to country A catch up country B.")

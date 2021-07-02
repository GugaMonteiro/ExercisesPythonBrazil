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

grow_a = -1

while grow_a < 0:
    grow_a = float(input("\nType the initial tax rate of the country A(%): "))
    grow_a = (grow_a / 100) + 1
    if grow_a < 0:
        print("The valor has to be greater than zero. Try again.")

grow_b = 2

while grow_b > grow_a:
    grow_b = float(input("Type the initial growth rate of the country B(%): "))
    grow_b = (grow_b / 100) + 1
    if grow_b > grow_a:
        print("The valor has to be minor than the growth rate of the country A. Try again.")

year = 0

while country_a != country_b:
    grow_total = country_a * grow_a
    country_a += grow_total
    grow2_total = country_b * grow_b
    country_b += grow2_total
    year += 1

print(f"\nIt will be necessary {year} years to country A catch up country B.")

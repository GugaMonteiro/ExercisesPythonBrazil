wage = -1

while wage < 0:
    wage = int(input("Type the employee initial wage: "))
    if wage < 0:
        print("The value has to be more than zero. Try again.")

year = -1

while year < 0:
    year = int(input("Type the employee contract year: "))
    if year < 0:
        print("The value has to be more than zero. Try again.")

limit = 2021 - year
bonus = 0.015

for c in range(0, limit):
    rise = wage * bonus
    wage_final = wage + rise
    bonus *= 2

total = '{0:,}'.format(wage_final).replace(',', '.')

print(f"Wage actualized: {total}")

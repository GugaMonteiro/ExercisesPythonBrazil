print("Projection of Allowance Expenses")
print("="*15)

aw_min = 100    # Minimum Allowance

aw = 0.2

wage = -1
wage_dict = {}
x = 0

while wage != 0:
    wage = float(input("Wage: "))
    if wage > 0:
        if wage >= 1000:
            total = wage * aw
        else:
            total = aw_min
        wage_dict[wage] = wage_dict.get(x, 0) + total

print("\nWage\t-\tAllowance")

for k, y in wage_dict.items():
    print(f"{k}\t-\t{y}", end='\n')

print(f"\n{len(wage_dict)} employees were processed")
print(f"Total spent in Allowance: {sum(wage_dict.values())}")

employee = 0

for k, y in wage_dict.items():
    if y == aw_min:
        employee += 1

print(f"Minimum amount paid to {employee} employees")
print(f"Highest amount of bonus paid: {max(wage_dict.values())}")

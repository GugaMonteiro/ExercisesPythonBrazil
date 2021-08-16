quant_grade = -1

# Ask how many grades that will be calculate
while quant_grade <= 0:
    quant_grade = int(input("How many grades do you want calculate: "))
    if quant_grade <= 0:
        print("The number has to be more than zero. Try again.")

grade = []
print("\n")

# Ask the grades that will be calculate
for c in range(1, quant_grade + 1):
    n = float(input(f"Type the {c}º grade: "))
    grade.append(n)

# Calculates the average
av = sum(grade) / len(grade)

print(f"\nYour average was {round(av, 2)}!")

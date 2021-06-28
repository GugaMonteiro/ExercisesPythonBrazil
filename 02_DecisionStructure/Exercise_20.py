grade = []

for x in range(1, 4):
    g = float(input(f"Type your {x}º grade: "))
    grade.append(g)

grade_m = (sum(grade)) / 3

if 7 <= grade_m < 9.9:
    print("Approved. ")
elif grade_m <= 7:
    print("Reproved.")
elif grade_m == 10:
    print("Approved with distinction.")
else:
    print("Invalid grade.")

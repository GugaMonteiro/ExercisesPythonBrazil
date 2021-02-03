grade = []

for x in range(1, 3):
    num = float(input(f"Type the {x}º grade: "))
    grade.append(num)

grade_sum = sum(grade) / 2

if 7 <= grade_sum < 9.9:
    print(f"\nYour average was {grade_sum}. You passed.")
elif grade_sum == 10:
    print(f"\nYour average was {grade_sum}. You passed respectfully.")
elif 0 <= grade_sum < 7:
    print(f"\nYour average was {grade_sum}. You failed.")
else:
    print("Error.")

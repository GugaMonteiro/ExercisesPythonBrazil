import random

grade = [round(random.uniform(0, 10), 1) for c in range(0, 4)]

print(f"Grades: {grade}")
print(f"Mean: {round(max(grade) / len(grade), 1)}")

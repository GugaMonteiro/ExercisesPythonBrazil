import random

age = [random.randint(0, 100) for c in range(0, 30)]
height = [round(random.uniform(0.54, 2.51), 2) for i in range(0, 30)]

mean = round(sum(height) / len(height), 2)
student = 0

for x in range(0, 30):
    if age[x] > 13 and height[x] < mean:
        student += 1

print(f"{student} students have height less than the average height of students")

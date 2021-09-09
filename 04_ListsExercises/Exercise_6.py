import random

mean = []
student = 0
total = 0

for e in range(0, 10):
    for c in range(1, 5):
        grade = round(random.uniform(0, 10), 1)
        total += grade
    sub_total = total / 4
    mean.append(round(sub_total, 1))
    total = total - total

student = 0

for i in range(0, 10):
    if mean[i] >= 7:
        student += 1

print(f"{student} students got more than 7.0")

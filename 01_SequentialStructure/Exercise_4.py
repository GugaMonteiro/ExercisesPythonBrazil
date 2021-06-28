grade = []


for v in range(1, 5):
    num = float(input(f'Type your grade in the {v}º semester: '))
    grade.append(num)

sum = 0
for n in range(len(grade)):
    sum += grade[n]

total = sum / len(grade)

print(total)


# Numbers of classroom
c_room = -1

while c_room < 0:
    c_room = int(input("How many classroom exists: "))
    if c_room < 0:
        print("The value has to be more than zero. Try again.")

# Numbers of students
students = []

for c in range(1, c_room + 1):
    quant_s = -1
    while quant_s < 0 or quant_s > 40:
        quant_s = int(input(f"How many students are in the {c}º classroom: "))
        if quant_s < 0 or quant_s > 40:
            print("The value has to be more than zero. Try again.")
    students.append(quant_s)

av = sum(students) / c_room

print(f"The school have {c_room} classrooms and the average of {round(av)} students per class.")

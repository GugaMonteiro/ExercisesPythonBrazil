grade = -1

while grade <= 0 or grade > 10:
    grade = int(input("Type a grade: "))
    if grade <= 0 or grade > 10:
        print("\nInvalid grade. Try again")

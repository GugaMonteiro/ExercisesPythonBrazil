salary = float(input("Type the employee's salary: "))

if salary <= 280:
    rise = salary * 0.2
    new_salary = salary + rise
    print(f"\nYour salary was ${salary}")
    print(f"You had a 20% increase. That's equal to ${rise} rise.")
    print(f"Your new salary is ${new_salary}")
elif 280 < salary <= 700:
    rise = salary * 0.15
    new_salary = salary + rise
    print(f"\nYour salary was ${salary}")
    print(f"You had a 15% increase. That's equal to ${rise} rise.")
    print(f"Your new salary is ${new_salary}")
elif 700 < salary <= 1500:
    rise = salary * 0.1
    new_salary = salary + rise
    print(f"\nYour salary was ${salary}")
    print(f"You had a 20% increase. That's equal to ${rise} rise.")
    print(f"Your new salary is ${new_salary}")
elif salary > 1500:
    rise = salary * 0.05
    new_salary = salary + rise
    print(f"\nYour salary was ${salary}")
    print(f"You had a 20% increase. That's equal to ${rise} rise.")
    print(f"Your new salary is ${new_salary}")
else:
    print("Invalid Entry!")

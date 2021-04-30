num_1 = float(input("Type the first grade: "))
num_2 = float(input("Type the second grade: "))

average = (num_1 + num_2) / 2

if 9 < average <= 10:
    concept = "A"
    print(f"\nYour first grade was {num_1} and your second was {num_2}.")
    print(f"Your average was {average}.")
    print(f"Your concept was {concept}.")
    print("You've pass.")
elif 7.5 < average <= 9:
    concept = "B"
    print(f"\nYour first grade was {num_1} and your second was {num_2}.")
    print(f"Your average was {average}.")
    print(f"Your concept was {concept}.")
    print("You've pass.")
elif 6 < average <= 7.5:
    concept = "C"
    print(f"\nYour first grade was {num_1} and your second was {num_2}.")
    print(f"Your average was {average}.")
    print(f"Your concept was {concept}.")
    print("You've pass.")
elif 4 < average <= 6:
    concept = "D"
    print(f"\nYour first grade was {num_1} and your second was {num_2}.")
    print(f"Your average was {average}.")
    print(f"Your concept was {concept}.")
    print("You've fail.")
elif 0 < average <= 4:
    concept = "E"
    print(f"\nYour first grade was {num_1} and your second was {num_2}.")
    print(f"Your average was {average}.")
    print(f"Your concept was {concept}.")
    print("You've fail.")
else:
    print("\nInvalid Entry!")

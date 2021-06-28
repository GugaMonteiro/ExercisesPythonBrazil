opt = input("Choose F or M: ")
x = opt.upper()

if x == "F":
    print(f"You chose feminine.")
elif x == "M":
    print(f"You chose masculine.")
else:
    print(f"You chose another or a invalid entry.")

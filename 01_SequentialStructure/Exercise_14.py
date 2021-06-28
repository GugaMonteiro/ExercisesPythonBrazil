w = float(input("Type the weight of the fish: "))

maxW = 50  # Maximum weight
fine = 4   # Fine for kg

if w > maxW:
    ex = w - maxW  # excess calculation
    total = ex * fine
    print(f"You exceeded {ex}kg.")
    print(f"You have to pay ${total} dollars in fine.")
else:
    print("All good.")

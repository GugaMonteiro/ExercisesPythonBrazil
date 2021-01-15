g = input("Type 'M' if you're male or 'F' if you're female: ")

h = float(input("Type your height: "))

if g.lower() == 'm':
    w = (72.7 * h) - 58
    print(f"Your ideal weight is {round(w, 2)} kg.")
elif g == 'f':
    w = (62.1 * h) - 44.7
    print(f"Your ideal weight is {round(w, 2)}kg.")
else:
    print("Error 303 (exercise to dawn old) or you typed wrong. Try again.")

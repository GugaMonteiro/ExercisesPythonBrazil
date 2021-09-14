control = "."
leap_l = []

while control != "":
    control = input("Athlete: ")
    if control != "":
        name = control
        for c in range(1, 6):
            leap = float(input(f"{c}º Leap: "))
            leap_l.append(leap)

print("\nFinal Result:")
print(f"Athlete: {name}")
print(f"Leaps: {leap_l}")
print(f"Leaps Average: {round(sum(leap_l) / len(leap_l), 2)}")

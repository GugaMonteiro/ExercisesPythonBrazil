print("M - Morning\tE - Evening\tN - Nocturnal")

c = input("\nWhat shift do you study?(M/E/N) ")

if c.upper() == "M":
    print("Good Morning.")
elif c.upper() == "E":
    print("Good Afternoon.")
elif c.upper() == "N":
    print("Good Night.")
else:
    print("Invalid entry.")

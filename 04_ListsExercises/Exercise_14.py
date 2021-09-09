questions = ["Did you call the victim?", "Were you at the crime scene?",
             "Do you live near the victim?", "Did you owe the victim money?",
             "Have you worked with the victim?"]

quant = 0

for c in range(0, 5):
    x = input(f"{questions[c]}")
    answer = x.upper()
    if answer == "YES" or answer == "Y":
        quant += 1

if quant == 2:
    print("Suspect.")
elif 2 < quant <= 4:
    print("Accomplice")
elif quant == 5:
    print("Killer.")
else:
    print("Innocent.")

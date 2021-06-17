questions = ["Did you call to the victim?",
             "Were you at the crime scene?",
             "Do you live near the victim?",
             "Did you owe to the victim?",
             "Have you worked with the victim?"]

answers = []

for i in questions:
    q = input(f"{i} ")
    a = q.upper()
    answers.append(a)

count = 0

for x in answers:
    if x == "YES":
        count += 1

if count == 2:
    print("Suspect.")
elif count == 3 or 4:
    print("Accomplice")
elif count == 5:
    print("Killer.")
else:
    print("Innocence")

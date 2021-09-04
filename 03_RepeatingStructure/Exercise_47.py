leave = "."
score = []

while leave != "Y":
    name = input("Athlete: ")
    if name != "":
        for c in range(1, 8):
            s = float(input(f"Score {c}: "))
            score.append(s)
    x = input("Do you wanna exit(Y/N): ")
    leave = x.upper()

score.remove(max(score))
score.remove(min(score))

print("-"*20)
print("\nFinal Result:")
print(f"Athlete: {name}")
print(f"Best score: {max(score)}")
print(f"Worst score: {min(score)}")

mean = sum(score)/len(score)

print(f"Mean: {round(mean, 2)}")

from random import randint

mouse_quest = {
    1: "Need Battery",
    2: "Need Cleaning",
    3: "Need Scroll",
    4: "Broken/Unusab",
    0: "Exit"
}

mouse_fix = {}

for k, v in mouse_quest.items():
    print(f"{k}: {v}")

for c in range(0, 200):
    mouse = randint(1, 4)
    if mouse in mouse_quest:
        mouse_fix[mouse] = mouse_fix.get(mouse, 0) + 1

print("\nSituation\t\t\tQuantity\t\tPercentage")

for k, v in mouse_fix.items():
    print(f"{mouse_quest[k]}: \t\t{v}\t\t\t\t{round(v * 100 / 200, 2)} %")

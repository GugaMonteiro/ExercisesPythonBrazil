from random import randint

dice = {
    1: '',
    2: '',
    3: '',
    4: '',
    5: '',
    6: '',
}

dice_result = {}

for c in range(1, 101):
    throw = randint(1, 6)
    if throw in dice:
        dice_result[throw] = dice_result.get(throw, 0) + 1

for k, v in dice_result.items():
    print(f"{k}: {v}")

straw = int(input("How many kg of strawberry do you wanna buy: "))
apple = int(input("How many kg of apple do you wanna buy: "))

if straw == 0 and apple > 0:
    if 0 < apple <= 5:
        total = apple * 1.8
    elif apple > 5:
        total = apple * 1.5
elif straw > 0 and apple == 0:
    if 0 < straw <= 5:
        total = straw * 2.5
    elif straw > 0:
        total = straw * 2.2
else:
    if 0 < straw <= 5:
        total = straw * 2.5
    elif straw > 0:
        total = straw * 2.2
    elif 0 < apple <= 5:
        total = apple * 1.8
    elif apple > 5:
        total = apple * 1.5

fruit_total = apple + straw

if fruit_total > 8 or total > 25:
    desc = total * 0.1

total -= desc

print(f"You buyed {straw}kg of strawberries and {apple}kg of apples.")
print(f"You have to pay ${total}.")

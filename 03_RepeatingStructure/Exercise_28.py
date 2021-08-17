# quantity of cd's
num_c = -1

while num_c < 0:
    num_c = int(input("How many cd's do you have: "))
    if num_c < 0:
        print("The value has to be more than zero. Try again.")

price = []
print("-"*20)

for c in range(1, num_c + 1):
    value = -1
    while value < 0:
        value = float(input(f"Type the valor for the {c}º cd: "))
        if value < 0:
            print("The value has to be more than zero. Try again.")
    price.append(value)

print("-"*20)
total = sum(price)
av = total / len(price)

print(f"You invested ${round(total, 2)}, with an average of ${round(av, 2)} per cd.")

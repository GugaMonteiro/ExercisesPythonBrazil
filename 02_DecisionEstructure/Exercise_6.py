num = []

for x in range(1, 4):
    n = float(input(f"Type the {x}º number: "))
    num.append(n)

maxi = max(num)

print(f"\n{maxi} is the biggest number.")

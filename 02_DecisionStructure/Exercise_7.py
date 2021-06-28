num = []

for i in range(1, 4):
    n = int(input(f"Type the {i}º number: "))
    num.append(n)

print(f"\n{max(num)} is the maximum number typed.")
print(f"{min(num)} is the minimum number typed.")

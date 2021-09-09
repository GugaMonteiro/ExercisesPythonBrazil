age = []
weight = []

for c in range(1, 6):
    a = int(input(f"Type the {c}º age: "))
    age.append(a)
    w = float(input(f"Type the {c}º weight: "))
    weight.append(w)

print(f"Age: {age[::-1]}")
print(f"Weight: {weight[::-1]}")

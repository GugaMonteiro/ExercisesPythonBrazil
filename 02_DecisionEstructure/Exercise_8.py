product = []

for i in range(1, 4):
    p = float(input(f"What's the price of the {i}º product: "))
    product.append(p)

print(f"The chosen product costs ${min(product)}. It's the cheaper.")

country_a = 80000
country_b = 200000

year = 0

while country_a != country_b:
    grow = country_a * 1.015
    country_a += grow
    grow2 = country_b * 1.03
    country_b += grow2
    year += 1

print(f"It will be necessary {year} years to country A catch up country B.")

base_wage = 200
sellers = [0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0, 10):
    sale = float(input("Type how much the seller sell in the week: : "))
    wage = sale * 0.09 + base_wage
    ind = int(wage / 100) - 1
    if ind > 9:
        ind = 9
    elif ind < 1:
        ind = 1
    sellers[ind - 1] += 1

for i in range(0, 9):
    print(f"{i * 100 + 200} - {(i + 1) * 100 + 199} : {sellers[i]}")

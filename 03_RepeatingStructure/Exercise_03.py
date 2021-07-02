name = ""

while len(name) <= 3:
    name = input("Type your name:")

age = -1

while age < 0 or age > 150:
    age = int(input("Type your age: "))

wage = -1

while wage < 0:
    wage = float(input("Type your salary: "))

id_sex = ""

while id_sex != "f" and id_sex != "m":
    id_sex = input("Type your sex (M/F): ").lower()

c_status = ""

while c_status != "s" and c_status != "m" and c_status != "w" and c_status != "d":
    c_status = input("Type your civil state (S/M/W/D): ")

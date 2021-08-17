quant = -1

while quant < 0:
    quant = int(input("Type the people quantity: "))
    if quant < 0:
        print("The number has to be more than zero. Try again.")

people = []
print("-"*20)
x = -1

for n in range(1, quant + 1):
    x = int(input(f"Type the age of the {n}º person: "))
    people.append(x)

av = sum(people) / len(people)

if 0 < av <= 25:
    print(f"The average is {av}. It was between 0 - 25. The class is young.")
elif 25 < av <= 60:
    print(f"The average is {av}. It was between 26 - 60. The class is adult.")
elif av > 60:
    print(f"The average is {av}. It was more than 60. The class is elderly.")
else:
    print("Error. Try again.")

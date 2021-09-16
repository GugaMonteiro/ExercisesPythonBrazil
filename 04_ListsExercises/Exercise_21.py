print("Fuel Consumption Comparison")
vehicles = []
cons = []
price = 2.25

for i in range(1, 6):
    vehicles.append(input(f'Vehicle {i}: '))
    cons.append(float(input('Km per liter: ')))

print("Final Result")

for i in range(0, 5):
    cost = 1000 / cons[i]
    spend = cost * price
    print (f"{vehicles[i]} - {cons[i]} - {round(cost, 2)} - {round(spend, 2)}")
    if ('lessConsumption' not in vars()) or (cons[i] > cons[lessConsumption]):
        lessConsumption = i

print(f"The lowest consumption is {lessConsumption}")

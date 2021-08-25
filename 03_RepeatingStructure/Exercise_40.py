total_vehicles = 0
total_ac_final = 0
total_city_final = 0

for i in range(0, 5):
    cod = int(input("Type the city code: "))
    vehicles = int(input("Type the vehicles quantity: "))
    accidents = int(input('Type the accident quantity in the year: '))

    index_ac = accidents / float(vehicles)
    total_vehicles += vehicles

    if ('high_ac' not in vars()) or (index_ac > high_ac):
        high_ac = index_ac
        cod_high_ac = cod
    if ('low_ac' not in vars()) or (index_ac < low_ac):
        low_ac = index_ac
        cod_low_ac = cod

    if vehicles < 2000:
        total_ac_final += accidents
        total_city_final += 1

print(f"The city with the highest number of accidents is {cod_high_ac} with {round(high_ac, 2)}")
print(f"TThe city with the highest number of accidents is {cod_low_ac} with {round(low_ac, 2)}")
print(f"The average of vehicles in the cities is {total_vehicles / 5.0}")
print(f"The average of accidents in the cities, with less than 2k vehicles, is "
      f"{round(total_ac_final / float(total_city_final))}")

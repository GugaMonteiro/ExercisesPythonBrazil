area = int(input("Type the area to be painted: "))
print("\n\t1 - Buy all paints in cans.\n\t2 - Buy all cans in gallons.\n\t3 - Mix gallons and cans.")
paint_type = int(input("Choose one of the options above: "))

limit = 6            # One liter paint 6 meters
can = 18             # 1 can contain 18 liters

can_meters = can * limit

gallon = 3.6         # 1 gallon contain 3.6 liters

gallon_meters = gallon * float(limit)

can_price = 80
gallon_price = 25

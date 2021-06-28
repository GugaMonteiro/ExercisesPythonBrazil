area = int(input("Type the size of the area to be painted: "))

paint_limit = 3     # meters
price = 80.0          # dollars
paint_can = 18      # liters

can_meters = paint_can * paint_limit    # One can paint 54 meters
total = area / can_meters
cash = total * 80

if total > 1:
    print(f"You have to buy {round(total - 0.5)} cans and you will pay ${round(cash, 2)}.")
else:
    print(f"You have to buy just one and you will pay ${price}.")
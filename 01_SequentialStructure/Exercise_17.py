area = int(input("Type the area to be painted: "))
print("\n\t1 - Buy all paints in cans.\n\t2 - Buy all paints in gallons.\n\t3 - Mix gallons and cans.")
paint_type = int(input("\nChoose one of the options above: "))

limit = 6            # One liter paint 6 meters
can = 18             # 1 can contain 18 liters

can_meters = can * limit

gallon = 3.6         # 1 gallon contain 3.6 liters

gallon_meters = gallon * float(limit)

paint_mix = (can_meters + gallon_meters) * 1.1

can_price = 80
gallon_price = 25

if paint_type == 1:
    total = area / can_meters
    if 0 < total < 1:
        print(f"\nYou have to buy {round(total+0.5)} can for ${float(can_price)}.")
    else:
        total = area / can_meters
        final_price = round(total+0.5) * can_price
        print(f"You have to buy {round(total+0.5)} cans for ${round(final_price, 2)}")
elif paint_type == 2:
    total = area / gallon_meters
    if 1 < total < 0:
        print(f"\nYou have to buy {round(total+0.5)} gallon for ${float(gallon_price)}.")
    else:
        total = area / gallon_meters
        final_price = round(total+0.5) * gallon_price
        print(f"\nYou have to buy {round(total+0.5)} gallon for ${round(final_price, 2)}.")
elif paint_type == 3:
    total = area / paint_mix
    if 1 < total < 0:
        print(f"\nYou have to buy {round(total+0.5)} mixed types of cans.")
    else:
        total = area / paint_mix
        print(f"You have to buy {round(total+0.5)} mixed types of cans.")
else:
    print("Something gone wrong. Try again.")

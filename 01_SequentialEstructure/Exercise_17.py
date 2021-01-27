area = int(input("Type the area to be painted: "))
print("\n\t1 - Buy all paints in cans.\n\t2 - Buy all paints in gallons.\n\t3 - Mix gallons and cans.")
paint_type = int(input("\nChoose one of the options above: "))

limit = 6            # One liter paint 6 meters
can = 18             # 1 can contain 18 liters

can_meters = can * limit

gallon = 3.6         # 1 gallon contain 3.6 liters

gallon_meters = gallon * float(limit)

can_price = 80
gallon_price = 25

if paint_type == 1:
    total = area % can_meters
    if total == 1:
        print(f"\nYou have to buy {total} can for $ 80,00.")
    else:
        q_can = area / can_meters       # can quantity
        final_price = float(total) * can_price
        round(final_price+0.5)
        print(f"You have to buy {q_can} cans for ${final_price}")


side_1 = float(input("Type the first side of the triangle: "))
side_2 = float(input("Type the second side of the triangle: "))
side_3 = float(input("Type the third side of the triangle: "))

if ((side_2 + side_3) > side_1) or ((side_1 + side_3) > side_2)\
        or ((side_1 + side_2) > side_3):
    print("It's a triangle.")
    if side_1 == side_2 and side_1 == side_3 and side_2 == side_3:
        print("\nIt's an Equilateral Triangle.")
    elif side_1 == side_2 or side_1 == side_3 or side_2 == side_3:
        print("\nIt's an Isosceles Triangle.")
    else:
        print("\nIt's a Scalene Triangle.")
else:
    print("Isn't a triangle.")

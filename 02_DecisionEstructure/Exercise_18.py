data = input("Type a date(dd/mm/yyyy): ")

day = int(data[:2])
month = int(data[3:5])
year = int(data[6:])

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    leap_year = True
else:
    leap_year = False

valida = True
if month in (1, 3, 5, 7, 8, 10, 12):
    if (day < 1) or (day > 31):
        valida = False
elif month in (4, 6, 9, 11):
    if (day < 1) or (day > 30):
        valida = False
else:
    if leap_year:
        if (day < 1) or (day > 29):
            valida = False
    else:
        if (day < 1) or (day > 28):
            valida = False

if valida:
    print("Valid date.")
else:
    print("Invalid date.")

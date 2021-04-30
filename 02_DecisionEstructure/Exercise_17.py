year = int(input("Type a year(yyyy): "))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    print("Leap year.")
else:
    print("It's not a Leap year.")

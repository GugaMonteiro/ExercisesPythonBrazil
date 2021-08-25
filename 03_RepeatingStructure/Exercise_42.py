num = 1
count_1 = []
count_2 = []
count_3 = []
count_4 = []

print("----Type a negative number to exit----\n")

while num > 0:
    num = int(input("Type a number(1 - 100): "))
    if 0 < num <= 25:
        count_1.append(num)
    elif 25 < num <= 50:
        count_2.append(num)
    elif 50 < num <= 75:
        count_3.append(num)
    elif 75 < num <= 100:
        count_4.append(num)

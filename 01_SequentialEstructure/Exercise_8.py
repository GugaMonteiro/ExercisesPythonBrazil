money = float(input('How much money do you earn per hour? '))
hour = float(input("What's the total of hours you worked in the month: "))

total = money * hour

print(f'You earned ${round(total, 2)} dollars in this month.')


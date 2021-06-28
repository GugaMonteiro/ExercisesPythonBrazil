num1 = int(input('Type a integer number: '))
num2 = int(input('Type another integer number: '))
num3 = float(input('Type a real number: '))

a = (num1 * 2) * (num2 / 2)
b = (num1 * 3) + num3
c = num3 ** 3

print(f'\nThe product of the double of the first with the half of the second is {a}.')
print(f'The sum of the triple of the first with the third is {b}.')
print(f'The third cubed is {c}.')

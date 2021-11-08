def omission_value(value1):
    if value1 == '':
        return int(1)
    else:
        return min_max_band(int(value1))


def min_max_band(value2):
    if value2 < 1:
        return 1
    elif value2 > 20:
        return 20
    else:
        return value2


def line_creator(line1):
    x = '+'
    for i in range(line1):
        x += '-'
    x += '+'
    print(x)


def column_creator(line2, column2):
    for y in range(column2):
        c = '|'
        c += ' ' * line2
        c += '|'
        print(c)


def draw(line3, column3):
    line_creator(line3)
    column_creator(line3, column3)
    line_creator(line3)


print("="*20)
print("Drawing a triangle")
print("="*20)

line = int(input('\nType how many lines do you want(between 1 e 20): '))
column = int(input('Type how many columns do you want(between 1 e 20): '))
draw(omission_value(line), omission_value(column))

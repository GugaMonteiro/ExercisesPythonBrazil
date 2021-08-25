for i in range(0, 10):
    cod = int(input('\nType the student code: '))
    height = int(input('Type the student height: '))
    if ('big_height' not in vars()) or (height > big_height):
        big_height = height
        cod_big = cod
    if ('min_height' not in vars()) or (height < min_height):
        min_height = height
        cod_min = cod

print(f"The student with the highest height has the code {cod_big} with {big_height}")
print(f"The student with the lowest height has the code {cod_min} com {min_height}")

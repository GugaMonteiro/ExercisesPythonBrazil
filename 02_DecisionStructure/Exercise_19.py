num_1 = int(input("Type a number less than a thousand: "))

if 0 < num_1 < 1000:
    hundred = num_1 / 100
    int(hundred)
    ten = (num_1 % 100) / 10
    int(ten)
    unity = ((num_1 % 100) % 10)
    int(unity)
    if hundred > 1 and ten > 1 and unity > 1:
        print(f"{num_1} = {int(hundred)} hundreds, {int(ten)} tens and "
              f"{round(unity - 0.5)} unities.")
    elif hundred > 1 and ten > 1 and unity == 0 or 1:
        print(f"{num_1}  = {int(hundred)} hundreds, {int(ten)} tens and {int(unity)} unities.")
    elif hundred > 1 and ten == 0 or 1 and unity > 1:
        print(f"{num_1}  = {int(hundred)} hundreds, {int(ten)} ten and {int(unity)} unities.")
    elif hundred > 1 and ten == 0 or 1 and unity == 0 or 1:
        print(f"{num_1}  = {int(hundred)} hundreds, {int(ten)} ten and {int(unity)} unity.")
    elif hundred == 0 or 1 and ten == 0 or 1 and unity == 0 or 1:
        print(f"{num_1}  = {int(hundred)} hundred, {int(ten)} ten and {int(unity)} unity.")
    elif hundred == 0 and ten > 1 and unity > 1:
        print(f"{num_1} = {int(ten)} tens and {int(unity)} unities.")
    elif hundred == 0 and ten == 0 or 1 and unity == 0 or 1:
        print(f"{num_1} = {int(ten)} ten and {int(unity)} unity.")
    elif hundred == 0 and ten == 0 and unity > 1:
        print(f"{num_1} = {int(unity)} unities.")
    elif hundred == 0 and ten == 0 and unity == 0 or 1:
        print(f"{num_1} = {int(unity)} unity.")
    else:
        print("Error.")
else:
    print("Error!")

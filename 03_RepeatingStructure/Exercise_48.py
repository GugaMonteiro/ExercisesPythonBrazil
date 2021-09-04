leave = ""
inv_num = []
num = -1

while leave != "Y":
    while num > 0 or num != 0:
        num = int(input("Type a positive number: "))
        if num > 0:
            inv_num.append(num)
    x = input("Do you wanna exit(Y/N): ")
    leave = x.upper()

print(inv_num[::-1])

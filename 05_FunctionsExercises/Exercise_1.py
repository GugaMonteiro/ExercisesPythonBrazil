def repeat_num(n):
    for i in range(n):
        i += 1
        print(str(i) * i)


num = int(input("Type a number: "))
repeat_num(num)

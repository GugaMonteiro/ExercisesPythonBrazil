def line(num_1):
    for n in range(1, num_1 + 1):
        print(f"  {n} ", end='')
    print()


def seq(num_2):
    for num_2 in range(num_2 + 1):
        line(num_2)


num = int(input("Type a number: "))
seq(num)

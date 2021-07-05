num_1 = int(input("Type a number: "))
num_2 = int(input("Type another number: "))

num_1 += 1

num_v = []

for n in range(num_1, num_2):
    print(n)
    num_v.append(n)

print(sum(num_v))

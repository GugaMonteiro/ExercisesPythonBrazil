print("---- Times Tables Generator ----")

num = -1

while num < 0 or num > 10:
    num = int(input("\nType a number between 1 and 10: "))
    if num < 0 or num > 10:
        print("The number has to be between 1 and 10. Try again.")

for n in range(1, 11):
    total = num * n
    print(f"{num} x {n} = {total}")

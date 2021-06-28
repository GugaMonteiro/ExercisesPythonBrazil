num_1 = int(input("Type a number: "))
num_2 = int(input("Type another number: "))

print("\n1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
choose = int(input("\nChoose one above: "))

if choose == 1:
    result = num_1 + num_2
elif choose == 2:
    result = num_1 - num_2
elif choose == 3:
    result = num_1 * num_2
elif choose == 4:
    result = num_1 / num_2
else:
    print("Invalid entry")

print(f"\n{result} it is:\n")

if result > 0:
    print("Plus")
else:
    print("Minus")

if result % 2 == 0:
    print("Even")
else:
    print("Odd")

if result == int(result):
    print("Integer")
else:
    print("Float")

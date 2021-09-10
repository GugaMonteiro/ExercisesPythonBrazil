num = 0
num_collection = []

while num != -1:
    num = int(input("Type a number: "))
    if num != -1:
        num_collection.append(num)

print(f"a) {len(num_collection)}")

print(f"b) {num_collection}")

print("c) ")
num_inverse = num_collection[::-1]
for c in range(0, len(num_collection)):
    print(num_inverse[c])

print(f"d) {sum(num_collection)}")

mean = sum(num_collection) / len(num_collection)
print(f"e) {round(mean-0.5)}")

total = 0
value = 0

for c in range(0, len(num_collection)):
    if num_collection[c] > mean:
        total += num_collection[c]
        value += 1

print(f"f)Quantity {value} + sum {total}")

total_2 = []

for c in range(0, len(num_collection)):
    if num_collection[c] < 7:
        total_2.append(num_collection[c])

print(f"g) {total_2} and the sum {sum(total_2)}")
print("Good Bye.")

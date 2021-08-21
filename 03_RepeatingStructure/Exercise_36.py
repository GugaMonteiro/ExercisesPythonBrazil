num = -1

while num < 0:
    num = int(input("Assemble the multiplication table of: "))
    if num < 0:
        print("The value has to be more than zero. Try again.")

init = -1

while init < 0:
    init = int(input("Begin with: "))
    if num < 0:
        print("The value has to be more than zero. Try again.")

end = -1

while end < 0:
    end = int(input("End with: "))
    if num < 0:
        print("The value has to be more than zero. Try again.")

if end > init:
    for c in range(init, end + 1):
        total = num * c
        print(f"{num} * {c} = {total}")
else:
    print("Error. Initial value bigger than the End value.")


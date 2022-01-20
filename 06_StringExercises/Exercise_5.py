name = input("Type your name: ")

for n in range(0, len(name)):
    if n == 0:
        print(name)
    else:
        print(f"{name[:-n]}", end='\n')

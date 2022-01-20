name = input("Type your name: ")
name = name.strip()

for n in range(0, len(name)):
    print(f"{name[0:n+1]}", end='\n')

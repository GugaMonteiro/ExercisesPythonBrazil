psw = ""
name = ""

while psw == name:
    name = input("Type your name:")
    psw = input("Type your password: ")
    if psw == name:
        print("Wrong password")

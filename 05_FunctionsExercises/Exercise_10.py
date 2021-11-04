from random import randint
k = 0


def craps():
    k = randint(2, 12)
    if k == 7 or k == 11:
        print(f"You rolled {k}. You won the game.")
    elif k == 2 or k == 3 or k == 12:
        print(f" You rolled {k}. Craps!!! You lost the game!")
    elif k in range(4, 6) or k in range(8, 10):
        print(f"You rolled {k}. This is your point")
        while True:
            x = input("Press Y to trow the dice again: ")
            decision = x.upper()
            if decision == 'Y':
                z = randint(2, 12)
                print(f"You rolled {z}.")
                if z == 7:
                    print("You lost!!!")
                    break
            if z == k:
                print("You won!")
                break


craps()

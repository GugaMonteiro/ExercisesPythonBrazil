req = -1
quant = -1
leave = ""
total_final = 0

total_dog = 0
total_bsim = 0
total_begg = 0
total_burger = 0
total_xburger = 0
total_soda = 0

quant_dog = 0
quant_bsim = 0
quant_begg = 0
quant_burger = 0
quant_xburger = 0
quant_soda = 0


while leave != "Y":
    req = int(input("Type the code of your request: "))
    quant = int(input("Type the quantity do you want: "))
    if req < 0 or quant < 0:
        print("The value has to be more than zero. Try again.")
    if req == 100:
        total = 1.2 * quant
        total_dog += total
        quant_dog += quant
    elif req == 101:
        total = 1.3 * quant
        total_bsim += total
        quant_bsim += quant
    elif req == 102:
        total = 1.5 * quant
        total_begg += total
        quant_begg += quant
    elif req == 103:
        total = 1.2 * quant
        total_burger += total
        quant_burger += quant
    elif req == 104:
        total = 1.3 * quant
        total_xburger += total
        quant_xburger += quant
    elif req == 105:
        total = 1 * quant
        total_soda += total
        quant_soda += quant
    total_final = total_soda + total_dog + total_begg + total_bsim + total_burger + total_xburger
    leave = input("Do you want close you request(Y/N)?\n")
    leave = leave.upper()

print(f"Food\t\t-\t\tQuantity\t\t-\t\tPrice")
print(f"Hot Dog: \t\t\t{quant_dog}\t\t\t\t\t\t{round(total_dog, 2)}")
print(f"Simple Bauru: \t\t{quant_bsim}\t\t\t\t\t\t{round(total_bsim, 2)}")
print(f"Bauru with Egg: \t{quant_begg}\t\t\t\t\t\t{round(total_begg, 2)}")
print(f"Burger: \t\t\t{quant_burger}\t\t\t\t\t\t{round(total_burger, 2)}")
print(f"X-Burger: \t\t\t{quant_xburger}\t\t\t\t\t\t{round(total_xburger, 2)}")
print(f"Soda: \t\t\t\t{quant_soda}\t\t\t\t\t\t{round(total_soda, 2)}")
print(f"\nTotal: {round(total_final, 2)}")

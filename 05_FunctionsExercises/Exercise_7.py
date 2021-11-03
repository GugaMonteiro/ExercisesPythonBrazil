def pag_value(value, days):
    if days == 0:
        print(value)
        return value
    else:
        fee = value * 0.03
        fee_day = (value * 0.001) * days
        print(value + fee + fee_day)
        return value + fee + fee_day


count = 0
installment = []

while True:
    value1 = float(input("Type the installment value: "))
    day = int(input("Type how long is the installment late: "))
    installment.append(pag_value(value1, day))
    out = input("\nType 0 to leave: ")
    count += 1
    if out == '0':
        print(installment, count)
        break

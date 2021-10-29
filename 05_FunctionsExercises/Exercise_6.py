def conv_h(hour, minute):
    if 0 < x <= 12:
        print(f"{hour}:{minute}AM")
    else:
        new_hour = hour - 12
        return out_h(new_hour, minute)


def out_h(hour2, minute2):
    print(f"{hour2}:{minute2} PM")


while True:
    x = int(input("Type the hour: "))
    y = int(input("Type the minute: "))
    conv_h(x, y)
    z = input("Do you want to leave(Y/N): ")
    out = z.upper()
    if out == "Y":
        break


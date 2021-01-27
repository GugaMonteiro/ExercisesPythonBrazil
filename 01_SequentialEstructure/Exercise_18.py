size = int(input("Type the archive size(MB): "))
link = int(input("\nType the link speed(Mbps): "))

speed = size / link

time = speed / 60

print(f"\nYou'll spent approximately {round(time+0.5)} min to download the file")

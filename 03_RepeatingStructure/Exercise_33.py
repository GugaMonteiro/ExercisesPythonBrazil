c = ""
temp_values = []

while c != "exit":
    celsius = float(input("Type the temperature(celsius) you want: "))
    x = input("Type 'exit' to leave: ")
    c = x.lower()
    temp_values.append(celsius)

print(min(temp_values))
print(max(temp_values))
print(round(sum(temp_values)/len(temp_values), 2))

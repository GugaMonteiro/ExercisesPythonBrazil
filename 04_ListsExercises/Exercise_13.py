import random

temp_mean = []
months = ['1 - January', '2 - February', '3 - March', '4 - April', '5 - May', '6 - June', '7 - July',
          '8 - August', '9 - September', '10 - October', '11 - November', '12 - December']

for c in range(0, 12):
    x = round(random.uniform(0, 50), 2)
    temp_mean.append(x)

annual_mean = round(sum(temp_mean) / len(temp_mean), 2)
month = ""

for i in range(0, 12):
    if temp_mean[i] > annual_mean:
        month = months[i]
        print(f"{month}: {temp_mean[i]}")

from random import randint

print("****Elections****\n")
print("Candidates:\n1 - Theo\t4 - Elena\n2 - Gustav\t5 - Invalid Vote"
      "\n3 - Lucas\t6 - Blank Vote")

cod = 0
cod_total = 0

c_1 = 0
c_2 = 0
c_3 = 0
c_4 = 0
c_5 = 0
c_6 = 0

for c in range(0, 100):
    cod = randint(1, 6)
    if cod == 1:
        c_1 += 1
    elif cod == 2:
        c_2 += 1
    elif cod == 3:
        c_3 += 1
    elif cod == 4:
        c_4 += 1
    elif cod == 5:
        c_5 += 1
    elif cod == 6:
        c_6 += 1
    cod_total += 1

print(f"\nVotes on candidate 1: {c_1}")
print(f"Votes on candidate 1: {c_2}")
print(f"Votes on candidate 1: {c_3}")
print(f"Votes on candidate 1: {c_4}")
print(f"\nTotal of Invalid Votes: {c_5}")
print(f"Total of Blank Votes: {c_6}")

perc_votes = (c_5 * 100) / cod_total
print(f"Percentage of invalid votes out of total votes: {perc_votes}")

perc_votes_b = (c_6 * 100) / cod_total
print(f"The percentage of blank votes out of total votes: {perc_votes_b}")

from random import randint

print("-----Elections-----")

print("\nCandidate 1: John Mackenzie")
print("Candidate 2: Elena Myller")
print("Candidate 3: Trevor Maya\n")

quant_voter = -1

while quant_voter < 0:
    quant_voter = int(input("How many voter are: "))
    if quant_voter < 0:
        print("The number of voters has to be more than zero. Try again.")

election = []
print("-"*20)

for c in range(1, quant_voter + 1):
    x = randint(1, 3)
    election.append(x)

john_voters = election.count(1)
elena_voters = election.count(2)
trevor_voters = election.count(3)

print(f"John Mackenzie got {john_voters} votes.")
print(f"Elena Myller got {elena_voters} votes.")
print(f"Trevor Maya got {trevor_voters} votes.")

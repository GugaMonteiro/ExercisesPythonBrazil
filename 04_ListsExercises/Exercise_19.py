from random import randint
import operator

print("What is the best SO for servers?\n")

so_dict = {
    1: "Windows",
    2: "Unix",
    3: "Linux",
    4: "Netware",
    5: "Mas Os",
    6: "Other"
}

for k, v in so_dict.items():
    print(f"{k}: {v}")

votes = {}

while True:
    cont_vote = randint(0, 6)
    if cont_vote == 0:
        break
    if cont_vote not in so_dict:
        print("The value has to be between 1 to 6 or 0 to leave.")
    if cont_vote in so_dict:
        votes[cont_vote] = votes.get(cont_vote, 0) + 1

print("Operational System\t\tVotes\t\t%")
print("-----------------\t\t-----\t\t---")

for c in votes.items():
    total = votes.get(1) + votes.get(2) + votes.get(3) + votes.get(4) + votes.get(5) + votes.get(6)

for k, v in votes.items():
    print(f"{so_dict[k]}\t\t\t\t\t{v}\t\t\t{round(v * 100 / total, 2)}")

print("-----------------\t\t-----")
print(f"Total\t\t\t\t\t{total}")

max_key = max(votes.items(), key=operator.itemgetter(1))[0]

print(f"\nThe most voted Operating System was the {so_dict[max_key]}, with {votes.get(max_key)} votes,"
      f"corresponding to {round(votes.get(max_key)*100/total, 2)} of the votes")

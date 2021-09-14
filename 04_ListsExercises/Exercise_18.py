print("---- Survey: Who was the best player ----")

players = {
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        '10': 10,
        '11': 11,
        '12': 12,
        '13': 13,
        '14': 14,
        '15': 15,
        '16': 16,
        '17': 17,
        '18': 18,
        '19': 19,
        '20': 20,
        '21': 21,
        '22': 22,
        '23': 23}
votes = {}

while True:
    vote = input("Player number (0 = End): ")
    if vote == "0":
        break
    if vote not in players:
        print("Type a value between 1 - 23 or 0 to leave")
    if vote in players:
        votes[vote] = votes.get(vote, 0) + 1

for num, quant in votes.items():
    print(f"{players[num]}: {quant}")

import random
import string

vowels = ["a", "e", "i", "o", "u"]
letter = [random.choice(string.ascii_lowercase) for c in range(0, 10)]

num_con = 0

for c in range(0, 10):
    if letter[c] not in vowels:
        num_con += 1
        print(letter[c], end=" ")

print(f"\nNumber of Consonants: {num_con}")

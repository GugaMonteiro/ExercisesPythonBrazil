import random


def scrambles(a):
    shuffle = random.sample(a, len(a))
    new_word = ''.join(shuffle)
    print(new_word.upper())


word = input("Type a word: ")

scrambles(word)

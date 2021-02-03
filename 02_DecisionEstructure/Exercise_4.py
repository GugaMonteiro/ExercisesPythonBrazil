letter = input("Type a letter: ")

v = ["A", "E", "I", "O", "U"]

if letter.upper() in v:
    print(f"\n{letter.upper()} is a vowel.")
else:
    print(f"\n{letter.upper()} is a consonant.")

class StringCompare:

    def __init__(self, string):
        self._string = string

    def __len__(self):
        return len(self._string)

    def __eq__(self, other):
        return self._string == other


string_1 = StringCompare("Brazil Hexa 2006")
string_2 = StringCompare("Brazil Hexa 2006!")

length_1 = len(string_1)
length_2 = len(string_2)

print(f"'Brazil Hexa 2006' length: {length_1}\n")
print(f"'Brazil Hexa 2006!' length: {length_2}\n")

if length_1 > length_2:
    print(f"The first string is bigger than the second.")
elif length_2 > length_1:
    print(f"The second string is bigger than the first.")
elif length_1 == length_2:
    print(f"The two strings have the same lengths.")

if string_1 == string_2:
    print("The two string have the same content")
else:
    print("The two strings have different content.")


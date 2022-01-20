class RevertName:

    def __init__(self, name_1):
        self._name = name_1
        self.convert_name()

    def convert_name(self):
        return self._name[::-1].upper()


name = input("Type you name (using uppercase or lowercase letters): ")

new_name = RevertName(name)
revert = RevertName.convert_name(new_name)

print(f"'Your name in caps and in the reverse order is {revert}")





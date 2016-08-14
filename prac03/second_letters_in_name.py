__author__ = 'Donald Cull'

def main():
    name, name_length = get_name()
    display_name(name, name_length)


def display_name(name, name_length):
    for char in range(name_length):
        if char % 2 == 0:
            print(name[char])


def get_name():
    name = input("Enter your name: ")
    name_length = len(name)
    while name_length == 0:
        name = input("Enter your name again: ")
        name_length = len(name)
    return name, name_length


main()
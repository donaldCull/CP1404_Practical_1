__author__ = 'Donald Cull'

def main():
    name, name_length = get_name()
    letter_frequency = int(input("What frequency of letters do you want: "))
    display_name(name, name_length, letter_frequency)


def display_name(name, name_length, step):
    for i in range(0, name_length, step):
            print(name[i], end=" ")


def get_name():
    name = input("Enter your name: ")
    name_length = len(name)
    while name_length == 0:
        name = input("Enter your name again: ")
        name_length = len(name)
    return name, name_length


main()
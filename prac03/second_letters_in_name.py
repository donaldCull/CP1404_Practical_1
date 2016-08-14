__author__ = 'Donald Cull'

def main():
    name = input("Enter your name: ")
    name_length = len(name)
    while name_length == 0:
        name = input("Enter your name again: ")
        name_length = len(name)
    for char in range(name_length):
        if char % 2 == 0:
            print(name[char])
main()
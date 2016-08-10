__author__ = 'Donald Cull'

"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 5
MAX_LENGTH = 15
SPECIAL_CHARS_REQUIRED = False
SPECIALS = "!@#$%^&*()_-=+`~,./o'[]\<>?O{}|"


def main():
    print("Please enter a valid password")
    print("Your password must be between {} and {} characters, and contain:".format(MIN_LENGTH, MAX_LENGTH))
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if SPECIAL_CHARS_REQUIRED:
        print("\tand 1 or more special characters: {}".format(SPECIALS))
    password = input("> ")
    while not is_valid_password(password, SPECIAL_CHARS_REQUIRED, MIN_LENGTH, MAX_LENGTH):
        print("Invalid password!")
        password = input("> ")
    print("Your {} character password is valid: {} ".format(len(password), password))


def is_valid_password(password, specials_included, min_length, max_length):

    length_of_password = len(password)
    if length_of_password < min_length or length_of_password > max_length:
        return False

    count_lower = 0
    count_upper = 0
    count_digit = 0
    count_special = 0
    for char in password:
        if char.islower():
            count_lower += 1
        elif char.isupper():
            count_upper += 1
        elif char.isdigit():
            count_digit += 1
        elif char in SPECIALS:
            count_special += 1

    print("Lower letters: {}\nUpper letters: {}\nDigits: {}\nSpecials: {}". format(count_lower, count_upper, count_digit, count_special))

    if count_lower == 0 or count_upper == 0 or count_digit == 0:
        return False
    if specials_included and count_special == 0:
        return False
    else:
        return True

main()
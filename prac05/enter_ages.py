__author__ = 'Donald Cull'

"""
CURRENT_YEAR = 2016
display message to input name and dob
birth_details = empty dictionary
for count from 1 to 5
    get name
    get date of birth and split on /
    age = CURRENT_YEAR - birthdate[year]
    birth_details[name]= birth date, age


"""
AMOUNT_PEOPLE = 5
CURRENT_YEAR = 2016
print("Input your name and Date of Birth:")
birth_details = {}
for people in range(AMOUNT_PEOPLE):
    name = input("Name: ")
    birth_strings = (input("Birth like 11/07/1993: ")).split("/")
    print(birth_strings)
    birth_numbers = [int(number) for number in birth_strings]
    age = CURRENT_YEAR - birth_numbers[2]
    print(age)
    birth_details[name]= birth_numbers, age
print(name, birth, age)
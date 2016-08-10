__author__ = 'Donald Cull'

temp_file = open("numbers.txt","w")
how_many_numbers = int(input("How many number would you like to input"))
for numbers in range(how_many_numbers):
    number = int(input("Number: "))
    print(number, file=temp_file)
temp_file.close()

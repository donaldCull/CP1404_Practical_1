__author__ = 'Donald Cull'

# #temp_file = open("names.txt", "w")
# read_file = open("names.txt", "r")
#
# #names = ["Donald", "Barry", "Greg", "Sam", "Harry"]
#
# #for name in names:
#     #print(name, file=temp_file)
#
# for line in read_file:
#     line = line.strip()
#     for char in line:
numbers = ["12.95", "2"]
for number in numbers:
    if number.replace('.', '').isdigit():
        new_number = float(number)
        print(new_number)
    else:
        print(test_number)
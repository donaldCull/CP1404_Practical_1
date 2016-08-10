__author__ = 'Donald Cull'

temp_file = open("numbers.txt", "r")
#number1 = int(temp_file.readline())
#number2 = int(temp_file.readline())
#print(number1 + number2)
total = 0
for line in temp_file:
    number = int(line)
    total += number
print(total)
temp_file.close()

__author__ = 'Donald Cull'

#temp_file = open("names.txt", "w")
read_file = open("names.txt", "r")

#names = ["Donald", "Barry", "Greg", "Sam", "Harry"]

#for name in names:
    #print(name, file=temp_file)

for line in read_file:
    line = line.strip()
    for char in line:
__author__ = 'Donald Cull'

name = input("What is your name: ")

temp_file = open("name.txt","w")
print(name, file=temp_file)
temp_file.close()

temp_file = open("name.txt", "r")
name = temp_file.read().strip()
print("Your name is {}".format(name))
temp_file.close()
__author__ = 'Donald Cull'

numbers = []
for i in range(5):
    numbers.append(int(input("Number: ")))
print("The first number is {}\nThe last number is {}\n The smallest number is {}\n The largest number is {} ".format(numbers[0], numbers[-1], min(numbers), max(numbers)))
print("The average number is {}".format(sum(numbers)/5))
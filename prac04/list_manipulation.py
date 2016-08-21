__author__ = 'Donald Cull'

numbers = [3, 1, 4, 1, 5, 9, 2]
print(numbers[0],'\n',numbers[-1], '\n', numbers[3], '\n', numbers[:-1], '\n', numbers[3:4])
print(5 in numbers, '\n', 7 in numbers, '\n', "3" in numbers, '\n', numbers + [6, 5, 3])

numbers[0] = "ten"
print(numbers)
numbers[-1] = 1
print(numbers)
print(numbers[2:])
print(9 in numbers)

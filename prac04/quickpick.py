__author__ = 'Donald Cull'
import random
number_of_quickpicks = int(input("How many quickpicks?"))
for i in range(number_of_quickpicks):
    print("\n")
    for i in range(6):
        print(random.randrange(1, 45, 1),end=" ")

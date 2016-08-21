__author__ = 'Donald Cull'
import random
number_of_quickpicks = int(input("How many quickpicks?"))
quick_pick_row = []

for i in range(number_of_quickpicks):
    print("\n")
    for i in range(6):
        quick_number = random.randint(1,45)
        if quick_number in quick_pick_row:
            quick_number = random.randint(1, 45)
        else:
            quick_pick_row.append(quick_number)
    print(quick_pick_row)
    quick_pick_row.clear()


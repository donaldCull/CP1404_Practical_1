__author__ = 'Donald Cull'
import random

MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_ROW = 6
rows = int(input("how many rows? "))
quick_pick_row = []
for row in range(rows):
    for i in range(NUMBERS_PER_ROW):
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        while number in quick_pick_row:
            number = random.randint(MIN_NUMBER, MAX_NUMBER)
        quick_pick_row.append(number)
    quick_pick_row.sort()
    print("{}".format(quick_pick_row))
    quick_pick_row.clear()
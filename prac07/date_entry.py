__author__ = 'Donald Cull'
from prac07.date_class import Date

new_date = Date(11, 6, 1991)
print(new_date)
new_date.add_days(9)
print(new_date, "expecting 20/6/1991")

other_date = Date(31, 1, 1875)
print(other_date)

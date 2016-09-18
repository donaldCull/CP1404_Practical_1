"""
Stores date and allows days to be added to a date
"""
__author__ = 'Donald Cull'
months_with_thirty_days = [4, 6, 9, 11]
months_with_thirty_one_days = [1, 3, 5, 7, 8, 10, 12]
february_normal_year = 28


class Date:
    def __init__(self, day=0, month=0, year=0):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self):
        return "{}/{}/{}".format(self.day, self.month, self.year)
    def add_days(self, number_of_days):
        # if self.month in months_with_thirty_one_days and self.day + number_of_days > 31:
        #     self.month += 1
        #     self.day = 0
        #     self.day += number_of_days
        # elif self.month in months_with_thirty_days:

        self.day += number_of_days








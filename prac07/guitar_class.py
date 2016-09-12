CURRENT_YEAR = 2016


class Guitar:
    def __init__(self, name="", year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        summary = "{} ({}) : ${:.2f}".format(self.name, self.year, self.cost)
        return summary

    def __repr__(self):
        return str(self)

    def get_age(self):
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        age = self.get_age()
        if age > 50:
            return True
        else:
            return False

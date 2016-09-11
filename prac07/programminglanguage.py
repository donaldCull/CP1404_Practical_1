DYNAMIC = "Dynamic"
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year
    def is_dynamic(self):
        if self.typing == DYNAMIC:
            return True
        else:
            return False
    def __str__(self):
        summary = "{}, {}, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection, self.year)
        return summary
BLANK = ""
from prac07.guitar_class import Guitar

guitars = []

print("My Guitars!")
# guitar_name = input("Name:")
guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
# while guitar_name != BLANK:
    # guitar_year = int(input("Year: "))
    # guitar_cost = float(input("Cost: "))
    # new_guitar = [Guitar(guitar_name, guitar_year, guitar_cost)]
    # print("{} ({}) : ${:.2f} added.".format(guitar_name, guitar_year, guitar_cost))
    # guitars.append(new_guitar)
    # guitar_name = input("Name:")
for number, guitar in enumerate(guitars):
    if guitar.is_vintage():
        vintage_string = "(Vintage)"
    else:
        vintage_string = ""
    print("Guitar {}: {:>20} ({}), worth ${:10,.2f} {}".format(number,guitar.name, guitar.year, guitar.cost, vintage_string))


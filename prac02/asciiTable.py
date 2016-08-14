__author__ = 'Donald Cull'
def main():
    lower = 10
    upper = 100
    print("Enter a number ({}-{})".format(lower,upper))
    get_number(lower, upper)

# for i in range(10, 120, 11):
#   print("{} {:>6}".format(chr(i), i))
# why does the 10 appear dedented

def get_number(minimum, maximum):
    number = 0
    while number < minimum or number > maximum:
        try:
            number = int(input(">>>"))
        except ValueError:
            print("Please enter a valid number:")

main()

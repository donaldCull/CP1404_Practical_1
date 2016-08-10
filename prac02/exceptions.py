__author__ = 'Donald Cull'

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")

# When will a ValueError occur?  When anything other than integer type is input
# When will a ZeroDivisionError Occur?  When 0 is entered as the denominator
# Could you change the code to avoid the possibility of a ZeroDivisonError?
# You could make the input type str and if its equal to 0 ask the user for another
# input

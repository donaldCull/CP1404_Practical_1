"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""
__author__ = 'Donald Cull'
def main():
    MENU = "C - Convert Celsius to Fahrenheit\nF - Convert Fahrenheit to Celsius\nQ (for quit)"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            convert_celsius_fahrenheit()
            choice = input(">>> ").upper()
        elif choice == "F":
            convert_fahrenheit_celsius()
            choice = input(">>> ").upper()
        else:
            print("Invalid option")
            print(MENU)
            choice = input(">>> ").upper()
    print("Thank you.")


def convert_celsius_fahrenheit():
            celsius = float(input("Celsius: "))
            fahrenheit = celsius * 9.0 / 5 + 32
            print("Result: {:.2f} F".format(fahrenheit))

def convert_fahrenheit_celsius():
        # Hint: celsius = 5 / 9 * (fahrenheit - 32)
        fahrenheit = float(input("Fahrenheit:  "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print("Result: {:.2f} C".format(celsius))
main()



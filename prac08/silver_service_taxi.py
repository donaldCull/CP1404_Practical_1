from prac08.taxi_class import SilverServiceTaxi
from prac08.taxi_class import Taxi

MENU = "q)uit, c)hoose taxi, d)rive"
VALID_MENU_CHOICES = ['q', 'c', 'd']
taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 200, 4)]
bill_to_date = 0
print("Let's Drive!")
print(MENU)
# menu_choice = input(">>> ")
menu_choice = 'c'
while menu_choice != 'q':
    if menu_choice not in VALID_MENU_CHOICES:
        print("Invalid option")
        print("Bill to date: ${:.2f}".format(bill_to_date))
        menu_choice = input(">>> ")

    elif menu_choice == 'c':
        print("Taxis Available:")
        available_taxi_numbers = []
        for number, taxi in enumerate(taxis):
            print("{} - {}".format(number, taxi))
            available_taxi_numbers.append(number)
        taxi_number = int(input("Choose taxi: "))
        while taxi_number not in available_taxi_numbers:
            print("Invalid number")
            taxi_number = int(input("Choose taxi: "))
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        menu_choice = input(">>> ")
    else:
        print("Drive how far?")
        print(MENU)





# new_taxi = SilverServiceTaxi('prius', 100)
# new_taxi.drive(10)
# print(new_taxi)
# print("Total cost ${:.2f} expecting $28.50".format(new_taxi.get_fare()))

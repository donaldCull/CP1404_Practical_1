from prac08.taxi_class import Taxi, SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"
VALID_MENU_CHOICES = ['q', 'c', 'd']
taxis = [Taxi('Prius', 100), SilverServiceTaxi('Limo', 100, 2), SilverServiceTaxi('Hummer', 200, 4)]
bill_to_date = 0
print("Let's Drive!")
print(MENU)
menu_choice = input(">>> ")
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
        taxi_choice = taxis[taxi_number]
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        menu_choice = input(">>> ")

    elif menu_choice == 'd':
        distance_requested = int(input("Drive how far? "))
        taxi_choice.drive(distance_requested)
        taxi_choice_cost = taxi_choice.get_fare()
        print("Your {} trip cost you ${:.2f}".format(taxi_choice.name,taxi_choice_cost))
        bill_to_date += taxi_choice_cost
        print("Bill to date: ${:.2f}".format(bill_to_date))
        print(MENU)
        menu_choice = input(">>> ")

print("Total trip cost: ${:.2f}\nTaxis are now:".format(bill_to_date))
for number, taxi in enumerate(taxis):
    print("{} - {}".format(number, taxi))

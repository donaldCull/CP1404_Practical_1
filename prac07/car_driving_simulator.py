__author__ = 'Donald Cull'

from prac07.car_class import Car

def main():
    print("Lets drive!")
    # car_name = input("Enter your car name: ")
    car_name = "The Bomb"
    new_car = Car(car_name)
    valid_menu_choices = ["d", "r", "q"]
    menu_choice = "start"
    while menu_choice != "q":
        print(new_car)
        print("Menu:")
        print("d) drive\nr) refuel\nq) quit")
        menu_choice = input("Enter your choice: ")
        if menu_choice not in valid_menu_choices:
            print("Invalid choice\n")
        elif menu_choice == 'd':
            kilometres = int(input("How many km do you wish to drive? "))
            while kilometres < 0:
                print("Distance must be >= 0")
                kilometres = int(input("How many km do you wish to drive? "))
            distance = new_car.drive(kilometres)
            if new_car.fuel == 0:
                print("The car drove {}km and ran out of fuel\n".format(distance))
            else:
                print("The car drove {}km\n".format(distance))
        elif menu_choice == 'r':
            fuel_units = int(input("How many units of fuel do you want to add to the car? "))
            while fuel_units < 0:
                print("Fuel amount must be >= 0")
                fuel_units = int(input("How many units of fuel do you want to add to the car? "))
            new_car.add_fuel(fuel_units)
            print("Added {} units of fuel".format(fuel_units))
    print("Good bye {}'s driver".format(car_name))


main()
"""
CP1404/CP5632 Practical
Client code to use the Car class
Note that the import has a folder (module) in it.
"""
from prac07.car_class import Car


def main():
    bus = Car(180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)
    print("Car {}, {}".format(bus.fuel, bus.odometer))
    print("Car {self.fuel}, {self.odometer}".format(self=bus))

    limo = Car("limo",100)
    limo.add_fuel(20)
    print("fuel =", limo.fuel)
    limo.drive(115)
    print("{} {}".format(limo.name, limo.odometer))
    print(str(limo))
main()
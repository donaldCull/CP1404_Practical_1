from random import randint

__author__ = 'Donald Cull'
"""
CP1404/CP5632 Practical
Car class
"""


class Car:
    """ represent a car object """

    def __init__(self, name="", fuel=0):
        """ initialise a Car instance """
        self.name = name
        self.fuel = fuel
        self.odometer = 0

    def __str__(self):
        return "{}, fuel={}, odo={}".format(self.name, self.fuel, self.odometer)

    def add_fuel(self, amount):
        """ add amount to the car's fuel"""
        self.fuel += amount

    def drive(self, distance):
        """ drive the car a given distance if it has enough fuel or drive until fuel runs out
        return the distance actually driven """
        if distance > self.fuel:
            distance_driven = self.fuel
            self.fuel = 0
        else:
            self.fuel -= distance
            distance_driven = distance
        self.odometer += distance_driven
        return distance_driven


class Taxi(Car):
    """ specialised version of a Car that includes fare costs """
    price_per_km = 1.20
    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)

        self.current_fare_distance = 0

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, ${:.2f}/km, {}km on current fare".format(super().__str__(), Taxi.price_per_km,
                                                             self.current_fare_distance)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven


class UnreliableCar(Car):
    """specialised version of Car that includes reliability of the car instance"""
    def __init__(self, name, fuel):
        """Initialises a unreliable car instance, based on parent class car"""
        super().__init__(name, fuel)
        self.car_reliability_rating = 50

    def drive(self, distance):
        reliability = randint(0, 100)
        if reliability < self.car_reliability_rating:
            super().drive(distance)
            return distance
        else:
            return "Car broke down!!"


class SilverServiceTaxi(Taxi):
    """Specialised version of taxi that includes fanciness of the taxi instance """
    fanciness = 2.0
    flagfall = 4.50
    def __init__(self, name, fuel):
        super().__init__(name, fuel)


    def get_fare(self):
        """ get the price for the taxi trip """
        super().get_fare()
        overall_price_per_km = SilverServiceTaxi.fanciness * Taxi.price_per_km
        return overall_price_per_km * self.current_fare_distance + SilverServiceTaxi.flagfall

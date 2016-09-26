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
    current_fare_distance = 0

    def __init__(self, name, fuel):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)

    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance,
                                                             Taxi.price_per_km)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.price_per_km * self.current_fare_distance

    def start_fare(self):
        """ begin a new fare """
        Taxi.current_fare_distance = 0

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
    flag_fall = 4.50

    def __init__(self, name, fuel, fanciness):
        """
        Initialises a Silver service taxi based on its parent class car
        :param name:
        :param fuel:
        """
        self.overall_price_per_km = fanciness * Taxi.price_per_km
        super().__init__(name, fuel)

    def get_fare(self):
        """ get the price for the taxi trip """
        super().get_fare()
        return (self.overall_price_per_km * Taxi.current_fare_distance) + SilverServiceTaxi.flag_fall

    def __str__(self):
        """Returns details about the SilverServiceTaxi"""
        Taxi.price_per_km = self.overall_price_per_km
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), SilverServiceTaxi.flag_fall)

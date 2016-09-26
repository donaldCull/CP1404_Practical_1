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
    price_per_km = 1.2

    def __init__(self, name, fuel, fanciness=1):
        """ initialise a Taxi instance, based on parent class Car """
        super().__init__(name, fuel)
        self.current_fare_distance = 0
        self.total_price_km = Taxi.price_per_km * fanciness


    def __str__(self):
        """ return a string representation like a car but with current fare distance"""
        return "{}, {}km on current fare, ${:.2f}/km".format(super().__str__(), self.current_fare_distance,
                                                             self.total_price_km)

    def get_fare(self):
        """ get the price for the taxi trip """
        return self.total_price_km * self.distance_driven

    def start_fare(self):
        """ begin a new fare """
        self.current_fare_distance = 0

    def drive(self, distance):
        """ drive like parent Car but calculate fare distance as well"""
        self.distance_driven = super().drive(distance)
        self.current_fare_distance += self.distance_driven
        return self.distance_driven


class UnreliableCar(Car):
    """specialized version of car that includes the reliability of car"""

    def __init__(self, name, fuel, reliability):
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        car_reliability = randint(1, 100)
        if self.reliability < car_reliability:
            distance_driven = super().drive(distance)
            return distance_driven
        else:
            return "The car broke down!"


class SilverServiceTaxi(Taxi):
    """Specialised version of taxi that scales the price_per_km based on the fanciness of the taxi"""
    flag_fall = 4.5

    def __init__(self, name, fuel, fanciness):
        super().__init__(name, fuel, fanciness)
        self.current_fare_distance = 0

    def drive(self, distance):
        distance_driven = super().drive(distance)
        self.current_fare_distance += distance_driven
        return distance_driven

    def get_fare(self):
        return super().get_fare() + SilverServiceTaxi.flag_fall

    def __str__(self):
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), SilverServiceTaxi.flag_fall)

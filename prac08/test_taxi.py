from prac08.taxi_class import Taxi, UnreliableCar, SilverServiceTaxi

new_taxi = Taxi('Prius 1', 100)
new_taxi.drive(40)
print(new_taxi)
new_taxi.start_fare()

new_taxi.drive(100)
print(new_taxi, '\n')

new_car = UnreliableCar('The bomb', 100, 50)
print(new_car)
print('Distance driven:', new_car.drive(40))
print(new_car, '\n')

fancy_car = SilverServiceTaxi('Hummer', 200, 4)
print(fancy_car)


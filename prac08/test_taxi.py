from prac08.taxi_class import Taxi, SilverServiceCar

new_taxi = Taxi('Prius 1', 100)
new_taxi.drive(40)
print(new_taxi)
new_taxi.start_fare()

new_taxi.drive(100)
print(new_taxi)

fancy_car = SilverServiceCar('Hummer', 200, 2)
fancy_car.drive(10)
print(fancy_car.get_fare())
print(fancy_car)
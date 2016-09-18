__author__ = 'Donald Cull'
from prac08.taxi_class import Taxi

new_taxi = Taxi('Prius 1', 100)
new_taxi.drive(40)
print(new_taxi)
print("Total cost ${:.2f}".format(new_taxi.get_fare()))

new_taxi.start_fare()
new_taxi.drive(100)
print(new_taxi)
print("Total cost ${:.2f}".format(new_taxi.get_fare()))
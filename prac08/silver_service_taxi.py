from prac08.taxi_class import SilverServiceTaxi

new_taxi = SilverServiceTaxi('prius', 100)
new_taxi.drive(10)
print(new_taxi)
print("Total cost ${:.2f} expecting $28.50".format(new_taxi.get_fare()))

# new_taxi.start_fare()
# new_taxi.drive(100)
# print(new_taxi)
# print("Total cost ${:.2f}".format(new_taxi.get_fare()))
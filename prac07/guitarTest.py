from prac07.guitar_class import Guitar

gibson = Guitar("Gibson L-5 CES",1922, 16035.40)
stratocaster = Guitar("Fender J1-1 STER", 2001, 120)
print(str(gibson))
print(gibson.get_age())
print(gibson.is_vintage())

print(str(stratocaster))
print(stratocaster.get_age(), "expecting 15")
print(stratocaster.is_vintage(), "expecting false")
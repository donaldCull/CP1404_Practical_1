__author__ = 'Donald Cull'

lower = 10
upper = 100
print("Enter a number ({}-{})".format(lower,upper))

for i in range(10, 120, 11):
    print("{} {:>6}".format(chr(i), i))

# why does the 10 appear dedented
MENU = "Please enter 2 numbers"
print(MENU)
x = int(input("The number for x: "))
y = int(input("The number for y: "))
print("Even numbers")
for i in range(x, y, 2):
    print(i)
print("Odd numbers")
for i in range(x, y):
    if i % 2 == 1:
        print(i)
print("Square numbers")
for i in range(x, y):
    print(i * i)
__author__ = 'Donald Cull'

items = int(input("How many items do you want: "))
total_item_cost = 0
for i in range(items):
    cost = float(input("What is the cost of item $ "))
    quantity = int(input("What is the quantity of item: "))
    total_cost = cost * quantity
    total_item_cost += total_cost

if total_item_cost >= 100:
    discount = (10 / 100) * total_item_cost
    total_item_cost -= discount

print('${:,.2f}'.format(total_item_cost))



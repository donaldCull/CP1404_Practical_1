MENU = "Shipping Calculator please input the name of the Item, Shipping cost per item" \
       "and item quantity"
print(MENU)
item_list = []
cost_list = []
quantity_list = []
item_price_list = []

data_entry = "incomplete"

while data_entry == "incomplete":
    item_name = input("Enter the items name: ")
    while not item_name.isalpha():
        print("Invalid item name")
        item_name = input("Enter the items name: ")
    item_name.capitalize()

    item_cost = input("Enter the items cost: ")
    while not item_cost.isdigit():
        print("Invalid item cost")
        item_cost = input("Enter the items cost: ")
    item_cost = int(item_cost)

    item_quantity = input("Enter quantity of item: ")
    while not item_quantity.isdigit():
        print("Invalid quantity")
        item_quantity = input("Enter quantity of item: ")
    item_quantity = int(item_quantity)

    total_item_cost = item_cost * item_quantity
    item_price_list.append(total_item_cost)
    item_list.append(item_name)
    cost_list.append(item_cost)
    quantity_list.append(item_quantity)

    print("Would you like to enter another item? ")
    new_item = input("(y) yes (n) no ").lower()
    while new_item != "y" and new_item != "n":
        print("Invalid entry try again")
        new_item = input("(y) yes (n) no ")
    if new_item == "n":
        data_entry = "complete"
    else:
        print("Invalid entry try again")

sum_total = sum(item_price_list)
if sum_total > 100:
    discount = (10 / 100) * sum_total
    discounted_price = sum_total - discount
    print("$ ", discounted_price)
else:
    print('${:,.2f}'.format(sum_total))

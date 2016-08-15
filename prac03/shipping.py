__author__ = 'Donald Cull'
def main():

    items = int(input("How many items do you want: "))
    total_cost = calculate_total_cost(items)
    display_discounted_cost(total_cost)


def calculate_total_cost(items):
    total_item_cost = 0
    for i in range(items):
        cost = float(input("What is the cost of item $ "))
        quantity = int(input("What is the quantity of item: "))
        total_cost = cost * quantity
        total_item_cost += total_cost
    return total_item_cost


def display_discounted_cost(total_cost):
    if total_cost >= 100:
        discount = (10 / 100) * total_cost
        total_cost -= discount
    print('total cost: ${:,.2f}'.format(total_cost))
main()




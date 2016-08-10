
# Asks input for first name, last name and capitalizes first letter for both. Checks if both are alphabetical names.
# Concatenates first and last name, stores them under name and outputs with a welcome string.
#  Name is returned to main.
def nameInput():
    valid = True
    while valid == True:
        print("What is your first name?")
        first = input(">> ").capitalize()
        print("What is your last name?")
        last = input(">> ").capitalize()
        if first.isalpha() and last.isalpha():
            name = first + " " + last
            valid = False
    print("Welcome to Tropical Airlines " + name)
    return name
# Displays menu to user.  User inputs selection into choice. Choice checked for validity.
# Menu options are looped until correct input given.
# If ordering for another person another name entry is available. New names are returned to main
# Exit returns exit message back to main to end program.
def menuCheck(name):
    print("\n(I) For Information\n(O) For Order ticket\n(E) To Exit program")
    choice = input().lower()
    while choice != "i" and choice != "o" and choice != "e":
        print("Invalid choice\n(I) For Information\n(O) For Order ticket\n(E) To Exit program")
        choice = input().lower()
    while choice != "o" and choice != "e":
        print("Thank you for choosing Tropical Airlines for your air travel needs.\n"
              "You will be asked questions regarding what type of ticket you would like to purchase"
              " as well as destination information.\n"
              "We also offer 50% discounted fares for children.")
        print("\n(I) For Information\n(O) For Order ticket\n(E) To Exit program")
        choice = input().lower()

    if choice == "o":
        print("Is the ticket for (Y)ou or is it for (S)omeone else")
        who = input().lower()
        while who != "s" and who != "y":
            print("Invalid choice (Y)ou or is it for (S)omeone else")
            who = input().lower()
        if who == "s":
            print("Please input the name for the ticket holder")
            name = nameInput()
            return name
        elif who == "y":
            return name
    else:
        status = "exit"
        return status

# Displays one way or return to users. Users inputs selection into choice. Choices are error checked for validity.
# Destinations are displayed to user. User inputs selection into destination
# Destination is returned to main.
def flightDetails():
    print("Is this ticket (O)ne way or (R)eturn")
    choice = input().lower()
    while choice != "o" and choice != "r":
        print("Invalid selection\nPlease select (O)ne way or (R)eturn ")
        choice = input().lower()
    if choice == "o":
        print("One way destinations\n(C)airns $250\n(S)ydney $420\n(P)erth $510")
        destination = input().lower()
        while destination != "c" and destination != "s" and destination != "p":
            print("Invalid selection please choose from\n(C)airns $250\n(S)ydney $420\n(P)erth $510")
            destination = input().lower()
        if destination == "c":
            destination = "One way Cairns $250"
        elif destination == "s":
            destination = "One Way Sydney $420"
        else:
            destination = "One way Perth $510"
        return destination
    else:
        print("Return destinations\n(C)airns $400\n(S)ydney $575\n(P)erth $700")
        destination = input().lower()
        while destination != "c" and destination != "s" and destination != "p":
            print("Invalid selection please choose from\n(C)airns $400\n(S)ydney $575\n(P)erth $700")
            destination = input().lower()
        if destination == "c":
            destination = "Return Cairns $400"
        elif destination == "s":
            destination = "Return Sydney $575"
        else:
            destination = "Return Perth $700"

        return destination
# Displays different fares to the user.  User inputs selection into choice. Choice is error checked for validity.
# Choice is returned to main
def fareType():
    print("Please choose the type of fare. Fees are displayed below and are in addition to the basic fare.\n"
          "Please note choosing Frugal fare means you will not be offered a seat choice\n"
          "(B)usiness - $275\n(E)conomy - $25\n(F)rugal - $0")
    choice = input(">>").lower()
    while choice != "b" and choice != "e" and choice != "f":
        print("Invalid selection please choose from\n(B)usiness - $275\n(E)conomy - $25\n(F)rugal - $0")
        choice = input(">>").lower()
    if choice == "b":
        choice = "Business $275"
    elif choice == "e":
        choice = "Economy $25"
    else:
        choice = "Frugal $0"
    return choice
# Displays different seats available to user. Seat selections are input into choice.
# Choice is error checked for validity. Seat is returned to main.
def seatType():
    print("Please choose the seat type.  Choosing the middle seat will deduct 25 from the total fare.\n"
          "(W)indow  $75\n(A)isle  $50\n(M)iddle -$25 ")
    choice = input(">>").lower()
    while choice != "w" and choice != "a" and choice != "m":
        print("Invalid selection please choose from\n(W)indow  $75\n(A)isle  $50\n(M)iddle -$25 ")
        choice = input(">>").lower()
    if choice == "w":
        seat = "Window $75"
    elif choice == "a":
        seat = "Aisle $50"
    else:
        seat = "Middle -$25"
    return seat

# Displays age information to the user. User inputs age into age. Age is error checked to be a number.
# If age is in the right age bracket return a discount or no discount to main
def ageCheck():
    while True:
        print("How old is the person travelling?"
              " Travellers under 16 years old will receive a 50% discount for the child fare.")
        age = input()
        if age.isdigit():
            age = int(age)
            if age > 0 and age < 16:
                discount = "50% discount"
                return discount
            elif age >= 16 and age < 120:
                discount = "No discount"
                return discount

# A list of selections are passed to orderPrice(). adds a price if it matches a condition.
# The price is stored in cost and is updated throughout the function.
# cost is output to the user and returned to main.
def orderPrice(orders):
    if orders[1] == "One way Cairns $250":
        cost = 250
    elif orders[1] == "One Way Sydney $420":
        cost = 420
    elif orders[1] == "One way Perth $510":
        cost = 510
    elif orders[1] == "Return Cairns $400":
        cost = 400
    elif orders[1] == "Return Sydney $575":
        cost = 575
    else:
        cost = 700
    if orders[2] == "Business $275":
        cost += 275
    elif orders[2] == "Economy $25":
        cost += 25
    else:
        cost += 0
    if orders[3] == "Window $75":
        cost += 75
    elif orders[3] == "Aisle $50":
        cost += 50
    else:
        cost -= 25
    if orders[4] == "50% discount":
        cost /= 2

    print("Your total is: $ ", cost)
    return cost

# Total costs of each order are passed to totalPurchase as well as a summary of each selection.
# Length of the total cost list is checked and outputs totals different depending on how many tickets bought.
# If more than one ticket is bought the tickets are sorted into ascending order and output to the user.

def totalPurchase(orderList,summary):
    orderLength = len(orderList)
    if orderLength == 0:
        print(summary, "Your orders are: None \nYour final total is: None")
        print("Thank you for choosing tropical Airlines\nGoodbye")
    elif orderLength == 1:
        print(summary[0], "Your orders are: $ ", orderList[0])
        print("Your final total is: $ ", orderList[0])
        print("Thank you for choosing tropical Airlines\nGoodbye")
    else:
        # sorts list of totals and adds them together
        orderList.sort()
        sumTotal = sum(orderList)
        displayList = []
        # each total made into a string so they can be joined together
        # appends each converted total into a new displayable list
        for i in orderList:
            str(i)
            price = "${}".format(i)
            displayList.append(price)
        # displays list of totals with 'and' in between and no 'and' at the end
        # displays sumtotal of the list of totals
        print(summary[0], ",your orders are:", end=" ")
        print(' and '.join(displayList))
        print("\nYour final total is: $", sumTotal)
        print("\nThank you for choosing tropical Airlines\nGoodbye")


# Contains all the lists that store all the user data.
# Main takes returned data from functions and appends to a relevant list.
# If the menu function returns "exit" the program will end.
# Each ticket cost is appended to orderCosts and totalled on exit.
# Ticket summary are cleared to allow for new summaries for the next ticket

def main():
    orderSummary = []
    orderCosts = []
    tickets = 0
    userName = nameInput()
    ticketProgram = True
    while ticketProgram == True:
        # this will be skipped if another ticket is purchased
        if tickets == 0:
            tickets = 1
            orderSummary.append(menuCheck(userName))
            if orderSummary[0] == "exit":
                totalPurchase(orderCosts, userName)
                ticketProgram = False
        else:
            orderSummary.append(flightDetails())
            orderSummary.append(fareType())
            orderSummary.append(seatType())
            orderSummary.append(ageCheck())
            for element in orderSummary:
                print(element)
            orderCosts.append(orderPrice(orderSummary))
            # second menu after summary has been displayed
            status = menuCheck(userName)
            if status == "exit":
                totalPurchase(orderCosts, orderSummary)
                ticketProgram = False

            # if user doesnt exit the ticket summary is cleared and last name entered into the menu is used
            orderSummary.clear()
            orderSummary.append(status)

main()
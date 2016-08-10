name = input("Please enter your name: ")
menu = "(H)ello\n(G)oodbye\n(Q)uit\n"
print(menu)
choice = input(">>>").upper()
while choice != "Q":
    if choice == "H":
        print("hello " , name)
    elif choice == "G":
        print("Goodbye " , name)
    else:
        print("invalid choice")
    print(menu)
    choice = input(">>>").upper()
print("Finished")


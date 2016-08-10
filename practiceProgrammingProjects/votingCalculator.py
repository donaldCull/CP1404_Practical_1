print("what is your age")
age = int(input(">>>> "))
if age >= 18:
    print("Are you enrolled to vote? ")
    enrollment = input("(Y) yes (N) no: ").upper()
    while enrollment != "Y" and enrollment != "N":
        print("Invalid selection please try again")
        enrollment = input("(Y) yes (N) no: ").upper()
    if enrollment == "Y":
        print("You can vote")
    else:
        print("You need to enroll")
else:
    print("Your too young to vote")

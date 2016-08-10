TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

menu = "Welcome to the electricity estimator please enter\n" \
       "Which tariff\n" \
       "daily use in Kwh\n" \
       "number of days in the billing period\n"
print(menu)

tariff_choice = input("Which tariff? 11 or 31: ")
while tariff_choice != "11" and not tariff_choice == "31":
    print("Invald choice please try again")
    tariff_choice = input("Which tariff? 11 or 31: ")

kwh_daily_use = float(input("Enter daily use KWh: "))
billing_period = float(input("Enter number of billing days: "))

if tariff_choice == "11":
    cost_per_day = TARIFF_11 * kwh_daily_use
    total_cost = cost_per_day * billing_period
    print("Estimated bill: ${:,.2f}".format(total_cost))
else:
    cost_per_day = TARIFF_31 * kwh_daily_use
    total_cost = cost_per_day * billing_period
    print("Estimated bill: ${:,.2f}".format(total_cost))
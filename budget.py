'''BUDGET CALCULATOR'''

'''
BUDGET LIST:
Income
Expenses
    Rent
    Utilities
    Electric
    Car
    Gas
    Insurance
    Credit Cards
    Internet
    Cable
    Phone
    Groceries
    Eat out
    Clothes
    Extras (allow to add own)
Left for month
'''

'''
TO DO:
Input income
    store income
Input expenses
    store expenses
Ask for extras
    store extras
subtract expenses + extras from income
return percent of income left

'''
incomes = []
expenses = []
expense_items = ["Rent", "Utilities", "Electric", "Car", "Gas", "Insurance", "Credit Card Debt", "Internet", "Cable",
                 "Phone", "Groceries", "Eat Out", "Clothes", "Extra"]
extras = []
total = 0



def budget():
    # Enter income
    income = (input("Enter Income: $"))
    while not income.isdigit():
        print("Please enter a valid number.")
        income = (input("Enter Income: $"))
    else:
        incomes.append(income)

    # Add more incomes option
    add_more = True
    while add_more:
        more_income = input("Do you have any other incomes? (y/n)")
        affirmative = ['yes', 'yeah', 'yup', 'y', 'yea', 'si', 'sí', 'oui', 'ja', 'ha', 'hai', 'da']
        negative = ['n', 'no', 'naw', 'nah', 'nope', 'non', 'nein', 'nahi', 'net', 'lie']
        if more_income.lower() in affirmative:
            budget()
            break
        elif more_income.lower() in negative:
            add_more = False
            print(incomes)
            for i in range(0, len(incomes)):
                global total
                total = total + int(incomes[i])
            print("$" + str(total) + " is your monthly income.")
            input("Press Enter to start entering expenses... ")
        else:
            print("\nYes or no.")
            add_more = True

    # Add expenses
    print("\nBelow will be a list of items. If it applies to you, enter the amount. If it doesn't, hit enter to skip.")
    input("Press Enter to continue... ")
    for i in expense_items:
        expense = input(i + ": ")
        expenses.append(expense)
    print(expenses)

### OPTION FOR EXTRA EXPENSES
### ADD EXPENSES TOGETHER

budget()



def budget():

    print("An Budget/Expense tracker")

    item_name = []

    price = []

    total = 0

    while len(item_name) <= 3:
   
        x = input("Enter the item name: ")

        y = input("Enter the corresponding price in CAD:")

        y_float = float(y)

        item_name.append(x)

        price.append(y_float)

        total = total+y_float



    report = input("Do you want to print class report?: ")

    if report == 'yes':

        for i, j in zip(item_name, price):

            print(i, ':', j)

    print("Your total budget is:", total)



budget()
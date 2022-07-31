MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

revenue = 0

# TODO 3. Print report. ✅

# TODO 3.1 When the user enters “report” to the prompt, a report should be generated that shows the current resource values.

def report():
    print("Coffee resources : ")
    for i in resources:
        print(i, resources[i])
    print(revenue)


# TODO: 1. Prompt user by asking "What would you like?" ✅

# TODO: 1.1 Check the user’s input to decide what to do next.

# TODO: 1.2 The prompt should show every time action has completed, e.g. once the drink is dispensed. The prompt should show again to serve the next customer.

# TODO 4. Check resources sufficient? ✅

# TODO 4.1 When the user chooses a drink, the program should check if there are enough resources to make that drink. ✅

# TODO 4.2 E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.” ✅

# TODO 4.3 The same should happen if another resource is depleted, e.g. milk or coffee. ✅

enough_resources = True
def check_resources():
    coffee_resources = (MENU[coffee_choice])
    print(coffee_resources)
    for i in coffee_resources["ingredients"]:
        if coffee_resources["ingredients"][i] > resources[i]:
            enough_resources = False
            print(f"Sorry there is not enough {i}.")

# TODO: 2. Turn off the Coffee Machine by entering "off” to the prompt.✅
# if coffee_choice == "off":
#     exit()

machine_resources_not_refilled = True

while machine_resources_not_refilled:

    coffee_choice = input("What would you like ☕️? (espresso/latte/cappuccino): ").lower()
    print(coffee_choice)

    if coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        check_resources()
    elif coffee_choice == "off":
        exit()
    elif coffee_choice == "report":
        report()
    else:
        print("That is not a valid option. Please choose from either: espresso, latte, or cappuccino. ")

    # TODO 5. Process coins. ✅

    # TODO 5.1 If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins. ✅

    # TODO 5.2 Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 ✅

    # TODO 5.3 Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2 pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52 ✅


    cost_of_coffee = int(MENU[coffee_choice]["cost"])
    if enough_resources:
        print(f"Please insert coins. A {coffee_choice} costs ${cost_of_coffee}")


    quarters = 0.25
    dimes = 0.10
    nickles = 0.05
    pennies = 0.01

    quarters_value = int(input("How many quarters?")) * 0.25
    dime_value = int(input("How many dimes?")) * 0.10
    nickles_value = int(input("how many nickles?")) * 0.05
    pennies_value = int(input("how many pennies?")) * 0.01

    coins_inserted = quarters_value + dime_value + nickles_value + pennies_value
    print(coins_inserted)



    # TODO 6. Check transaction successful? ✅

    # TODO 6.1 If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins. ✅

    # TODO 6.2 Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01 ✅

    # TODO 6.3 Calculate the monetary value of the coins inserted. ✅

    # turn in a while loop later
    # Maybe give the user the option to insert coins again or exit?
    # account for using typing in spaces etc.

    # TODO 7. Make Coffee. ✅

    # TODO 7.1 If the transaction is successful and there are enough resources to make the drink the user selected, then the ingredients to make the drink should be deducted from the coffee machine resources. ✅

    # TODO 7.2 Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink. ✅

    def make_coffee():
        for i in (MENU[coffee_choice]["ingredients"]):
            resources[i] -= (MENU[coffee_choice]["ingredients"][i])


    if coins_inserted < cost_of_coffee:
        enough_money = False
        print("Sorry that's not enough money. Money refunded.")
    else:
        refund = coins_inserted - cost_of_coffee
        print(f"Here is ${refund} dollars in change.")
        print("Making your coffee.")
        make_coffee()
        revenue += cost_of_coffee
        print(resources)
        print(f"Here is your {coffee_choice}. Enjoy!")

    # TODO 8. cash money

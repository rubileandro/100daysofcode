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


def report():
    """Prints coffee mechine resources"""
    print("Coffee resources : ")
    for i in resources:
        print(i, resources[i])
    print(revenue)


enough_resources = True
def check_resources():
    """Checks whether resources are sufficient to make cofffee"""
    coffee_resources = (MENU[coffee_choice])
    # print(coffee_resources)
    for i in coffee_resources["ingredients"]:
        if coffee_resources["ingredients"][i] > resources[i]:
            enough_resources = False
            print(f"Sorry there is not enough {i}.")


def run_machine():
    """Check if enough coins have been inserted and makes coffee"""
    cost_of_coffee = float(MENU[coffee_choice]["cost"])
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
        #revenue += cost_of_coffee
        print(resources)
        print(f"Here is your {coffee_choice}. Enjoy!")


machine_resources_not_refilled = True

while machine_resources_not_refilled:

    coffee_choice = input("What would you like ☕️? (espresso/latte/cappuccino): ").lower()
    # print(coffee_choice)

    if coffee_choice == "off":
        exit()
    elif coffee_choice == "report":
        report()
    elif coffee_choice == "espresso" or coffee_choice == "latte" or coffee_choice == "cappuccino":
        check_resources()
        run_machine()
    else:
        print("That is not a valid option. Please choose from either: espresso, latte, or cappuccino. ")

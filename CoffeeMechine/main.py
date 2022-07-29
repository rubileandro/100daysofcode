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


# TODO 3. Print report. ✅

def report():
    print("Coffee resources : ")
    for i in resources:
        print(i, resources[i])


# TODO: 1. Prompt user by asking "What would you like?" ✅

# TODO: 2. Turn off the Coffee Machine by entering "off” to the prompt.✅
# if coffee_choice == "off":
#     exit()

coffee_choice = input("What would you like ☕️? (espresso/latte/cappuccino): ").lower()
print(coffee_choice)

if coffee_choice == "espresso":
    pass
elif coffee_choice == "latte":
    pass
elif coffee_choice == "cappuccino":
    pass
elif coffee_choice == "off":
    exit()
elif coffee_choice == "report":
    report()
else:
    print("That is not a valid option. Please choose from either: espresso, latte, or cappuccino. ")



# TODO 4. Check resources sufficient?

# TODO 4.1 When the user chooses a drink, the program should check if there are enough resources to make that drink.

# TODO 4.2 E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should not continue to make the drink but print: “Sorry there is not enough water.”

# TODO 4.3 The same should happen if another resource is depleted, e.g. milk or coffee.

enough_resources = True

coffee_resources = (MENU[coffee_choice])
print(coffee_resources)
for i in coffee_resources["ingredients"]:
    if coffee_resources["ingredients"][i] > resources[i]:
        enough_resources = False
        print(f"Sorry there is not enough {i}.")



# TODO 5. Process coins.

# TODO 5.1 If there are sufficient resources to make the drink selected, then the program should prompt the user to insert coins.
cost_of_coffee = coffee_resources["cost"]
if enough_resources == True:
    coins = input(f"Please insert coins. A {coffee_choice} costs ${cost_of_coffee}")

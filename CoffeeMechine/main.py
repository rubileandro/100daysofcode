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


# TODO: 1. Prompt user by asking "What would you like?"
coffee_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
print(coffee_choice)

if coffee_choice == "espresso":
    pass
elif coffee_choice == "latte":
    pass
elif coffee_choice == "cappuccino":
    pass
elif coffee_choice == "off":
    exit()
else:
    print("That is not a valid option. Please choose from either: espresso, latte, or cappuccino. ")

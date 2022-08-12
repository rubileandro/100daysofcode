from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


is_on = True
choice = input("What would you like? (espresso/latte/cappuccino): ")
if choice == "report":
    coffee_report = CoffeeMaker()
    coffee_report.report()
    print(coffee_report)
elif choice == "off":
    is_on = False

else:
    drink = menu.find_drink(choice)
    if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        #money_machine.process_coins()

        coffee_maker.make_coffee(drink)

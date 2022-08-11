from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()


choice = input("What would you like? (espresso/latte/cappuccino): ")
if choice == "report":
    coffee_report = CoffeeMaker()
    coffee_report.report()
    print(coffee_report)
else:
    drink = menu.find_drink(choice)



if coffee_maker.is_resource_sufficient(drink):
    coffee_maker.make_coffee(drink)

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

choice = input("What would you like? (espresso/latte/cappuccino): ")
if choice == "report":
    coffee_report = CoffeeMaker()
    coffee_report.report()
    print(coffee_report)

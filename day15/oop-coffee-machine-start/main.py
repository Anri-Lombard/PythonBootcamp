from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

selection = Menu()
instructions = CoffeeMaker()
money = MoneyMachine()

is_on = True

while is_on:
    choice = input(f"What would you like? ({selection.get_items()}): ")
    if choice == "off":
        is_on = False
    if choice == "report":
        instructions.report()
        money.report()
    else:
        drink = selection.find_drink(choice)
        if instructions.is_resource_sufficient(drink) and money.make_payment(drink.cost):
            instructions.make_coffee(drink)




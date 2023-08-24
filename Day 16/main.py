from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

is_on = True
while is_on:
    user_choice = input(
        f"What would you like? ({menu.get_items()}): ")

    if user_choice == "report":
        coffee_machine.report()
        money_machine.report()

    elif user_choice == "off":
        is_on = False

    else:
        drink = menu.find_drink(user_choice)
        if coffee_machine.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)

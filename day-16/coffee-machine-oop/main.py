from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main_loop():
    menu = Menu()
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()

    while True:
        menu_items = menu.get_items()
        choice = input(f"What would you like ({menu_items}):")
        if choice == "off":
            print("Turning off.")
            break
        elif choice == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            order = menu.find_drink(choice)
            if order is not None and coffee_maker.is_resource_sufficient(
                    order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)


main_loop()

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def coffee_machine():
    my_menu = Menu()
    my_coffee_maker = CoffeeMaker()
    my_money_machine = MoneyMachine()
    machine_on = True
    while machine_on:
        order = input(f'What would you like? ({my_menu.get_items()}) ')
        if order == 'off':
            print('Shutting down. Good bye.')
            machine_on = False
        elif order == 'report':
            my_coffee_maker.report()
            my_money_machine.report()
        else:
            drink = my_menu.find_drink(order)
            if drink is not None and \
                    my_coffee_maker.is_resource_sufficient(drink) and \
                    my_money_machine.make_payment(drink.cost):
                my_coffee_maker.make_coffee(drink)


coffee_machine()

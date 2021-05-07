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
    "money": 0.0,
}


def check_resources(order):
    missing_resource = False
    if MENU[order]['ingredients']['water'] > resources['water']:
        print('Sorry there\'s not enough water.')
        missing_resource = True
    if order != 'espresso' and MENU[order]['ingredients']['milk'] > resources['milk']:
        print('Sorry there\'s not enough milk.')
        missing_resource = True
    if MENU[order]['ingredients']['coffee'] > resources['coffee']:
        print('Sorry there\'s not enough coffee.')
        missing_resource = True
    return missing_resource


def report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${resources["money"]:.2f}')


def get_coins():
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    return quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01


def update_resources(water, milk, coffee, cost):
    resources['water'] -= water
    resources['milk'] -= milk
    resources['coffee'] -= coffee
    resources['money'] += cost


def place(order):
    missing_resource = check_resources(order)
    if not missing_resource:
        cost = MENU[order]["cost"]
        print(f'One {order} is ${cost:.2f}.')
        amount = get_coins()
        change = amount - cost
        if change >= 0:
            print(f'Here is ${change:.2f} in change.')
            print(f'Here is your {order}. Enjoy!')
            water = MENU[order]['ingredients']['water']
            if order == 'espresso':
                milk = 0
            else:
                milk = MENU[order]['ingredients']['milk']
            coffee = MENU[order]['ingredients']['coffee']
            update_resources(water, milk, coffee, cost)

        else:
            print('Sorry that\'s not enough money. Money refunded.')


def coffee_machine():
    shutdown = False
    while not shutdown:
        order = input('What would you like? (espresso/latte/cappuccino): ').lower()
        if order == 'off':
            shutdown = True
        elif order == 'report':
            report()
        elif order in MENU:
            place(order)
        else:
            print('Sorry that\'s not available.')


coffee_machine()

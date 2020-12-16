import art
from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

print(art.logo)

#Objects that I'm getting from classes:
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

is_on = True

while is_on:
    options = menu.get_items()
    decision = input(f"What would you like? ({options}): ")
    if decision == 'off':
        is_on = False
    elif decision == 'report':
        machine_status = coffee_maker.report()
        machine_money_status = money_machine.report()
    else:
        drink = menu.find_drink(decision)
        enough_resources = coffee_maker.is_resource_sufficient(drink)
        if enough_resources:
            #in here we're putting the attribute "cost" assosiated with the "drink" object (which is menu.find_drink(decision))
            #which is a menu item.
            payment_successful = money_machine.make_payment(drink.cost)
            if payment_successful:
                coffee_maker.make_coffee(drink)







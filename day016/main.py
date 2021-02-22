from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def get_request(items):
    return input(f" What would you like? ({items}): ").lower()

coffee_maker = CoffeeMaker()
money_machine =  MoneyMachine()
menu = Menu()

coffee_maker.is_on = True

while coffee_maker.is_on:
    request = get_request(menu.get_items())
    if request == "off":
        coffee_maker.is_on = False
    elif request == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(request)
        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
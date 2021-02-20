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
}

money = 0.0

def get_request():
    return input(" What would you like? (espresso/latte/cappuccino): ").lower()

def display_report():
    print(f"water: {resources['water']}ml")
    print(f"milk: {resources['milk']}ml")
    print(f"coffee: {resources['coffee']}g")
    print(f"money: ${money}")

def check_resources(request):
    ingredients = MENU[request]["ingredients"]
    for key in ingredients:
        if ingredients[key] > resources[key]:
            print(f"Sorry there is not enough {key}")
            return False
    return True

def process_coins(request):
    print("Please insert coints.")
    quarters = float(input("how many quarters? "))
    dimes = float(input("how many dimes? "))
    nickels = float(input("how many nickels? "))
    pennies = float(input("how many pennies? "))
    return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

def make_coffee(request):
    ingredients = MENU[request]["ingredients"]
    for key in ingredients:
        resources[key] -= ingredients[key]

request = ""
while request != "off":
    request = get_request()
    if request == "report":
        display_report()
    elif request != "off":
        sufficient_resources = check_resources(request)
        if sufficient_resources:
            payment_amount = process_coins(request)
            cost = MENU[request]["cost"]
            if payment_amount < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                if payment_amount > cost:
                    print(f"Here is ${round(payment_amount - cost, 2)} in change.")
                money += cost
                make_coffee(request)
                print(f"Here is your {request}. Enjoy!”")
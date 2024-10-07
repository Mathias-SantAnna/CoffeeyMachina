from art import logo

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

profit = 0

resources = {
    "water": 900,
    "milk": 600,
    "coffee": 500,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough", item)
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted"""
    print("Please insert coins")
    total = int(input("How many coins of 50 cents?")) * 0.5
    total += int(input("How many coins of 1 euro?"))
    total += int(input("How many coins of 2 euro?")) * 2
    return total

def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, of False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        if change > 0:
            print(f"\nHere is your change: €{change}.")
        global profit
        profit += drink_cost
        return True
    else:
        print("\nNot enough money. Refund processed")
        return False

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"\n Here is your {drink_name.capitalize()} ☕. Enjoy!")


is_on = True

while is_on:
    print(logo)
    print("\nMenu:")
    for drink in MENU:
        print(f"{drink.capitalize()}: ${MENU[drink]['cost']}")

    user_request = input(" What would you like to order? Please type: ")
    if user_request == "off":
        is_on = False
    elif user_request == "report":
        print(f"\nWater: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[user_request]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_request, drink["ingredients"])

"""
def admin_user():
    admin_user_request = input(" What would you like to do?: 'report' 'machine maintenance' 'turn machine off'. ")
    if user_request == "turn machine off":
        is_on = False
    elif user_request == "report":
        print(resources)
    else:
        print("machine maintenance started, please wait until is finished.")
"""
#TODO: CREATE 2 DIFFERENT USERS: ADMIN AND CLIENT USER
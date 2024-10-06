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
    "milk": 60,
    "coffee": 500,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print("Sorry there is not enough", item)
            return False
    return True

is_on = True

while is_on:
#def user_order():
    user_request = input(" What would you like? (espresso/latte/cappuccino): ")
    if user_request == "off":
        is_on = False
    elif user_request == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: {profit}")
    else:
        drink = MENU[user_request]
        is_resource_sufficient(drink["ingredients"])


"""
def admin_user():
    admin_user_request = input(" What would you like to do?: 'report' 'machine maintenance'. ")
    if user_request == "machine maintenance":
        is_on = False
    elif user_request == "report":
        print(resources)
"""
#TODO: CREATE 2 DIFFERENT USERS: ADMIN AND CLIENT USER
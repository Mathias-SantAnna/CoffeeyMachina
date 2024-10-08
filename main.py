from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

from art import logo


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
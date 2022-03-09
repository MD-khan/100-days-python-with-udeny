#!/usr/bin/env python3
from random import choice

from torch import true_divide
from menu import MENU
from menu import resources


def check_resources(resourse, item):
    """take resourse and item and return the report"""
    if resourse['water'] < MENU[item]['ingredients']['water']:
        return f"Sorry there is not enough water."
    elif resourse['milk'] < MENU[item]['ingredients']['milk']:
        return f"Sorry there is not enough milk."
    elif resourse['coffee'] < MENU[item]['ingredients']['coffee']:
        return f"Sorry there is not enough coffe."


def update_resources(resourse, item):
    """Take resource and order item, and subtract"""
    resourse['water'] -= MENU[item]['ingredients']['water']
    resourse['milk'] -= MENU[item]['ingredients']['milk']
    resourse['coffee'] -= MENU[item]['ingredients']['coffee']


def customer_paid(quaters, dime, nickle, pennies):
    """Takes number of quaters, dime, nickle and pennies and return total"""
    return quaters * .25 + dime * 0.10 + nickle * 0.05 + pennies * 0.01


sale = 0
end_game = False

while end_game == False:

    # Ask user what they want
    order_item = input("What would you like? (espresso/latte/cappuccino): ")
    # show the price
    cost = float(MENU[order_item]['cost'])
    print(f"{order_item} cost ${cost}")

    # Check the resource / iningredients is enough to make coffe
    check = check_resources(resources, order_item)
    if check:
        print(check)
    # Ask user to insert money
    print("Please insert coins.")
    number_quaters = int(input("how many quarters?: "))
    number_dimes = int(input("how many dimes?: "))
    number_nickles = int(input("how many nickles?: "))
    number_pennies = int(input("how many pennies?: "))

    # check user inserted enouhg coins and return or refund
    customer_paid = customer_paid(
        number_quaters, number_dimes, number_nickles, number_pennies)

    if customer_paid >= cost:
        change = customer_paid - cost
        print("Here is your change " + "${0:.2f}".format(change))
        print(f"Here is your {order_item} ☕️ Enjoy!")
        # update resource
        update_resources(resources, order_item)
    elif customer_paid < cost:
        end_game = True
        print(f"Sorry! you don't have sufficent fund")

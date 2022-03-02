#!/usr/bin/env python3
# Python 3.9.6
from art import logo

print(logo)

# Add


def add(number_1, number_2):
    return float(number_1) + float(number_2)

# Subtract


def subtract(number_1, number_2):
    return float(number_1) - float(number_2)

# Multiply


def multiply(number_1, number_2):
    return float(number_1) * float(number_2)

# Devidfloat


def divide(number_1, number_2):
    return float(number_1) - float(number_2)


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}
"""this is amazing"""
# function = operations['*']
# print(function)
# print(multiply)


def calculator():
    number_1 = input("What's the first number?: ")
    for operator in operations:
        print(operator)

    end_calculation = True
    while end_calculation:
        operator = input("Pick an operato from the line above: ")
        number_2 = input("What's the next number?: ")
        calculation = operations[operator]
        result = calculation(number_1, number_2)

        print(f"{number_1} {operator} {number_2} = {result}")

        if input("Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation ") == 'y':
            number_1 = result
        else:
            end_calculation = False
            calculator()


calculator()

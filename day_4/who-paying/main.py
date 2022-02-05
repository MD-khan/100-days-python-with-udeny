#!/usr/bin/env python3
import random

# Split string method
#names_string = "Monir, Juma, Alex, Sarmila, Jhon"
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆
# Write your code below this line 👇

pick_the_name = random.randint(0, (len(names)-1))
#print(f"{names[pick_the_name]} is going to buy the meal today!")

"""

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
#print(fruits)
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

dirty_dozen = [fruits, vegetables]
print(dirty_dozen)
print(dirty_dozen[0])
print(dirty_dozen[1])
"""

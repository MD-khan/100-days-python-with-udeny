#!/usr/bin/env python3
# Python 3.9.6
import random

"""
Generate a strong password 
Take input from user
Then generate password
"""

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
           'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Password policy
# Minimum 4 letters
# Minimum 2 number
# Minimum 2 symbole
print("Welcome to the PyPassword Generator!")
min_letters = int(input("How many letters would you like in your password?\n"))
min_number = int(input(f"How many symbols would you like?\n"))
min_symbol = int(input(f"How many numbers would you like?\n"))

# min_letters = 4
# mini_number = 2
# mini_symbol = 2

# Get the 4 letters
total_characters = int(min_letters + min_number + min_symbol)

l = ""
n = ""
s = ""
for mix_chr in range(0, total_characters):
    if len(l) != min_letters:
        l += random.choice(letters)
    if len(n) != min_number:
        n += random.choice(numbers)
    if len(s) != min_symbol:
        s += random.choice(symbols)
password = l+n+s
# output nKEl10!*

p = []
for chr in password:
    p.append(chr)

mp = random.sample(p, len(p))
# Mixed them up
print("".join(mp))

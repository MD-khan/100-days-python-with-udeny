#!/usr/bin/env python3
"""
Take both people's names and check for the number of times 
the letters in the word TRUE occurs. T
hen check for the number of times the letters in the word LOVE occurs. 
Then combine these numbers to make a 2 digit number.
"""
from posixpath import split


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


ful_name = name1 + name2
ful_name = ful_name.lower()

# Count the characters in true sting
t = ful_name.count("t")
r = ful_name.count("r")
u = ful_name.count("u")
e = ful_name.count("e")

true = t + r + u + e

# Count the characters in true sting
l = ful_name.count("l")
o = ful_name.count("o")
v = ful_name.count("v")
e = ful_name.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))

if (int(love_score) < 10) or (int(love_score) > 90):
    print(
        f"Your Love score is {love_score}, \nyou go together like cock and mentos")
elif (int(love_score) < 40) or (int(love_score) > 50):
    print(
        f"Your Love score is {love_score}, \n you are alright together")


# print(name1.count('t'))

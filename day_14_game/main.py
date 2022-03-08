#!/usr/bin/env python3
import random
import os


from art import vs

from data import data


def formatData(data):
    """Take the account data and returns the printable format"""
    name = data["name"]
    describtion = data["description"]
    country = data["country"]
    return f"{name}, a {describtion}, from {country}"


def checkAnswer(guess, follower_a, follower_b):
    """Take the user guess and follower counts and returns if they got it right."""
    if follower_a > follower_b:
        return guess == "a"
    else:
        return guess == "b"


score = 0
game_end = False

account_b = random.choice(data)
while game_end == False:
    # Generate a random account from the game data
    account_a = account_b
    account_b = random.choice(data)

    # Making sure both are not the same
    while account_a == account_b:
        account_b = random.choice(data)
    print(f"Compare A: {formatData(account_a)}.")
    print(vs)
    print(f"Against B: {formatData(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    # Check if user is corect
    # get follower count of each account
    follower_count_account_a = account_a['follower_count']
    follower_count_account_b = account_b['follower_count']

    is_correct = checkAnswer(
        guess, follower_count_account_a, follower_count_account_b)
    os.system('clear')
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
    else:
        game_end = True
        print(f"Sorry! that's wrong. Final score: {score}.")

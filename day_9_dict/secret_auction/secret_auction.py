#!/usr/bin/env python3
# Python 3.9.6

from art import logo


print(logo)


def find_winner(biding_record):
    max_bid = 0
    winner = ""
    for bidder in biding_record:  # bidder get the key
        bid_amount = biding_record[bidder]  # geting the value
        if bid_amount > max_bid:
            max_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${max_bid}")


biding_record = {'monir': 120, 'juma': 340}
# find_winner(biding_record)


def secretAuction():
    bids = {}
    end_bid = False
    while end_bid is not True:
        name = input("What's your name: ")
        price = int(input("What's your bid?: "))
        bids[name] = price
        yes_no = input("Are their any bidders? \n Type y or n: ")
        if yes_no == "n":
            find_winner(bids)
            end_bid = True


secretAuction()
bidders = [
    {'name': 'Alex', 'bid': 120},
    {'name': 'Bob', 'bid': 30},
    {'name': 'Wilson', 'bid': 400},
    {'name': 'Smith', 'bid': 300},

]
# for bid in test:
#     max_bid = 0
#     print(bid.items())

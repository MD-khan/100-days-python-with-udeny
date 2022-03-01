#!/usr/bin/env python3
# Python 3.9.6
from cmath import inf
from art import logo

# print(logo)

info = []


def secretAuction():
    name = input("What's your name: ")
    bid = int(input("What's your bid?: "))
    global info
    info = [{"name": name, "bid": bid}]
    end_info = False
    while end_info is not True:
        yes_no = input("Are their any bidders? \n Type y or n: ")
        if yes_no == "y":
            more_info = {}
            name = input("What's your name: ")
            bid = input("What's your bid?: ")
            more_info["name"] = name
            more_info["bid"] = bid
            info.append(more_info)
        else:
            end_info = True
            print(info)


secretAuction()
# test = [
#     {'name': 'monir', 'bid': 120},
#     {'name': 'juma', 'bid': 30},
#     {'name': 'musa', 'bid': 400},
#     {'name': 'Munisa', 'bid': 300},

# ]
# for bid in test:
#     max_bid = 0
#     print(bid.items())

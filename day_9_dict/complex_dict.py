#!/usr/bin/env python3
# Python 3.9.6

travel_log = [
    {
        "country": "United State",
        "city_visited": ["Boston", "New York", "Los Angels", "Bufello"],
        "total_visited":10
    },
    {
        "country": "Bangladesh",
        "city_visited": ["Dhaka", "Khulna", "Shariatpur"],
        "total_visited":20
    }
]


def add_new_country(country, total_visited, city_visited):
    new_country = {}
    new_country["country"] = country
    new_country["city_visited"] = city_visited
    new_country["total_visited"] = total_visited
    travel_log.append(new_country)
    #travel_log += new_country


add_new_country("china", 9, ["honkong", "shanghai"])

print(travel_log)

#!/usr/bin/env python3

# with open("weather_data.csv") as file:
#     data = file.readlines()
# print(len(data))

import csv
import pandas

with open('weather_data.csv') as data_file:
    data = csv.reader(data_file)
    temparatures = []
    for raw in data:
        if raw[1] != 'temp':
            temparatures.append(int(raw[1]))

# print(temparatures)
data = pandas.read_csv('weather_data.csv')
print(data)

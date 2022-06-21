#!/usr/bin/env python3

import pandas
# print(temparatures)
data = pandas.read_csv('weather_data.csv')

# Convert data to dictionary
data_dict = data.to_dict()
print(data_dict)

#convert to list
temp_list = data["temp"].to_list()
print(temp_list)

# average temparature
average =  sum(temp_list) / len(temp_list)
print(round(average))

print(data['temp'].mean())

# get the max temparature
print(data['temp'].max())



# Get data in Row
print(data[data.day == "Monday"])

#!/usr/bin/env python3

import pandas

# Count the squirrel primary fur color
data = pandas.read_csv('squirrel_data.csv')
gray_squirrel_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrel_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrel_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black"],
    "Count" : [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

result = pandas.DataFrame(data_dict)
print(result)
#!/usr/bin/env python3
# import csv

# # images url
# imgs_url = []

# with open("sample_products.csv") as data_products:
#     product = csv.reader(data_products)
#     for row in product:
#         if row[28] != "Images":
#             imgs_url.append(row[28])
# #print(imgs_url)

# import pandas
# data = pandas.read_csv("rosdsle_products .csv")
# #print(data["Department"])

# data_dict = data.to_dict()
# #store the uniq category
# categories = []
# for cat, name in data_dict['Department'].items():
#     if name not in categories:
#         categories.append(name)
# print(len(categories))

# Read Woocomerce smple data
import pandas as pd

df_roseland = pd.read_csv("rosdsle_products .csv")
# convert to dectionary
df_rosedal_dict = df_roseland.to_dict()
# convert to datafarme
df = pd.DataFrame(df_rosedal_dict)
address = ["Delshi, dhaka"]
df["Address"] = address


df_woo_sample = pd.read_csv("sample_products.csv")
# get the shot desciption




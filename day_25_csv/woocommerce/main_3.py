#!/usr/bin/env python3

import pandas as pd
# sample_products.csv
# rosedale.csv.csv
df = pd.read_csv("rosedale-15.csv")
df2 = pd.read_csv("sample_products.csv", usecols=['Download 2 URL']
                  )
df["Download 2 URL"] = df2

df.to_csv('rosedale-16.csv', index=False)


print(df)

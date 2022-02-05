#!/usr/bin/env python3
# version Python 3.9.6
# Solved by Md Khan

# 🚨 Don't change the code below 👇
# 1     2    3
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
# print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆
# Write your code below this row 👇
#position = "23"

# Write your code above this row 👆
if len(position) != 2:
    print(f"Only two digits are allowed")
    exit()
column = int(position[0])  # horizontal
row = int(position[-1])  # Vertical

map[row - 1][column - 1] = "*"

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

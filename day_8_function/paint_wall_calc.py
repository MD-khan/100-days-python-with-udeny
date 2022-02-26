#!/usr/bin/env python3
# Python 3.9.6
"""
You are painting a wall. The instructions on the paint can says 
that 1 can of paint can cover 5 square meters of wall. Given a 
random height and width of wall, calculate how many cans of paint 
you'll need to buy.
number of cans = (wall height ✖️ wall width) ÷ coverage per can.
e.g. Height = 2, Width = 4, Coverage = 5
"""

from math import ceil


def wall_paint_calculator(height, width, coverage):
    area = height * width
    cans = ceil(area / coverage)
    print(f"You'll need {cans} cans of paint.")


wall_paint_calculator(2, 43, 5)

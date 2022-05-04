from itertools import count
from posixpath import split
import re
from unittest import result


sentence = "What is the Airspeed Velocity of an Unladen Swallow?"


result = { word:len(word) for word in sentence.split()}


print(result)